// system include files
#include <memory>
#include <string>
#include <vector>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PluginManager/interface/PluginFactory.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::PtEtaPhiELorentzVector LorentzVector;

//base class for constituent properties
class CandPropBase {
	public:
		//constructor
		CandPropBase() : name("") {}
		CandPropBase(const std::string& name_, edm::stream::EDProducer<>* edprod) : name(name_) {}
		//destructor
		virtual ~CandPropBase() {}
		//accessors
		virtual void put(edm::Event& iEvent) {}
		virtual void reset() {}
		virtual void get_property(const pat::PackedCandidate& cand) {}

		//member variables
		std::string name;
};

template <class T>
class CandProp : public CandPropBase {
	public:
		//constructor
		CandProp() : CandPropBase() {}
		CandProp(const std::string& name_, edm::stream::EDProducer<>* edprod) : CandPropBase(name_, edprod) {
			edprod->produces<std::vector<T>>(name);
		}
		//destructor
		~CandProp() override {}
		//accessors
		void put(edm::Event& iEvent) override { iEvent.put(std::move(ptr),name); }
		void reset() override { ptr.reset(new std::vector<T>()); }
		void push_back(T tmp) { ptr->push_back(tmp); }

		//member variables
		std::unique_ptr<std::vector<T>> ptr;
};

// factory
typedef edmplugin::PluginFactory<CandPropBase *(const std::string&, edm::stream::EDProducer<>*)> CandPropFactory;
EDM_REGISTER_PLUGINFACTORY(CandPropFactory, "CandPropFactory");
#define DEFINE_CAND_PROP(type) DEFINE_EDM_PLUGIN(CandPropFactory,CandProp_##type,#type)

// helper classes
class CandProp_PdgId : public CandProp<int> {
	public:
		using CandProp<int>::CandProp;
		void get_property(const pat::PackedCandidate& cand) override { push_back(cand.pdgId()); }
};
DEFINE_CAND_PROP(PdgId);

class CandProp_PuppiWeight : public CandProp<double> {
	public:
		using CandProp<double>::CandProp;
		void get_property(const pat::PackedCandidate& cand) override { push_back(cand.puppiWeight()); }
};
DEFINE_CAND_PROP(PuppiWeight);

class CandProp_dz : public CandProp<double> {
	public:
		using CandProp<double>::CandProp;
		void get_property(const pat::PackedCandidate& cand) override { push_back(cand.dz()); }
};
DEFINE_CAND_PROP(dz);

class CandProp_dxy : public CandProp<double> {
	public:
		using CandProp<double>::CandProp;
		void get_property(const pat::PackedCandidate& cand) override { push_back(cand.dxy()); }
};
DEFINE_CAND_PROP(dxy);

//based on https://github.com/cms-sw/cmssw/blob/master/RecoBTag/FeatureTools/plugins/DeepBoostedJetTagInfoProducer.cc
class CandProp_dzsig : public CandProp<double> {
	public:
		using CandProp<double>::CandProp;
		void get_property(const pat::PackedCandidate& cand) override { push_back(cand.bestTrack() ? cand.dz() / cand.dzError() : 0); }
};
DEFINE_CAND_PROP(dzsig);

class CandProp_dxysig : public CandProp<double> {
	public:
		using CandProp<double>::CandProp;
		void get_property(const pat::PackedCandidate& cand) override { push_back(cand.bestTrack() ? cand.dxy() / cand.dxyError() : 0); }
};
DEFINE_CAND_PROP(dxysig);

class JetsConstituents : public edm::stream::EDProducer<> {
public:
	explicit JetsConstituents(const edm::ParameterSet&);
	~JetsConstituents() override;

private:
	void produce(edm::Event&, const edm::EventSetup&) override;

	const std::string suffix_;
	std::vector<edm::InputTag> JetsTags_;
	std::vector<std::string> JetsNames_;
	std::vector<edm::EDGetTokenT<edm::View<pat::Jet>>> JetsToks_;
	edm::EDGetTokenT<edm::View<reco::Candidate>> CandTok_;
	std::vector<CandPropBase*> Props_;
};

JetsConstituents::JetsConstituents(const edm::ParameterSet& iConfig) :
	suffix_(iConfig.getParameter<std::string>("suffix")),
	JetsTags_(iConfig.getParameter<std::vector<edm::InputTag>>("JetsTags")),
	JetsNames_(iConfig.getParameter<std::vector<std::string>>("JetsNames")),
	CandTok_(consumes<edm::View<reco::Candidate>>(iConfig.getParameter<edm::InputTag>("CandTag")))
{
	if(JetsTags_.size() != JetsNames_.size()) throw cms::Exception("VectorSizeMismatch") << "Inconsistent sizes for JetsTags and JetsNames";

	for(const auto& tag: JetsTags_) JetsToks_.push_back(consumes<edm::View<pat::Jet>>(tag));

	for(const auto& name: JetsNames_){
		produces<std::vector<std::vector<int>>>(name+suffix_);
	}
	produces<std::vector<LorentzVector>>();

	//get list of desired additional properties
	const auto& props = iConfig.getParameter<std::vector<std::string>>("properties");

	auto fac = CandPropFactory::get();
	Props_.reserve(props.size());
	for(const auto& p : props){
		Props_.push_back(fac->create(p,p,this));
	}
}

JetsConstituents::~JetsConstituents() {
	for(auto& Prop: Props_){
		delete Prop;
	}
	Props_.clear();
}

void JetsConstituents::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
	//reset ptrs
	for(auto & Prop : Props_){
		Prop->reset();
	}

	std::vector<edm::Handle<edm::View<pat::Jet>>> h_jets;
	std::vector<std::vector<int>> jets_cands_indices;
	std::vector<std::unique_ptr<std::vector<std::vector<int>>>> indices_out;
	//assumption: all constituents come from a single product (will be checked explicitly)
	std::vector<int> processIndex(JetsToks_.size(),-1);
	std::vector<int> productIndex(JetsToks_.size(),-1);
	for(unsigned i = 0; i < JetsToks_.size(); ++i){
		edm::Handle<edm::View<pat::Jet>> handle;
		iEvent.getByToken(JetsToks_[i], handle);
		h_jets.push_back(handle);
		const auto& h_jet = h_jets.back();

		//custom data structure ala perfect hash:
		//vector where index = constituent key (from edm::Ptr), value = jet index
		//relies on above assumption and each constituent only appearing in one jet in the collection
		jets_cands_indices.emplace_back();
		auto& jet_cands_indices = jets_cands_indices.back();
		for(unsigned j = 0; j < h_jet->size(); ++j){
			const auto& jet = h_jet->at(j);
			for(const auto& cand : jet.daughterPtrVector()){
				if(processIndex[i]==-1) processIndex[i] = cand.id().processIndex();
				if(productIndex[i]==-1) productIndex[i] = cand.id().productIndex();
				//grow vector when needed
				if(cand.key()>=jet_cands_indices.size()) jet_cands_indices.resize(cand.key()+1,-1);
				//within-collection safety check
				if(cand.id().processIndex()!=processIndex[i] or cand.id().productIndex()!=productIndex[i]){
					throw cms::Exception("CandidateMismatch") << "Candidate with key " << cand.key() << " has indices (" << cand.id().processIndex() << ", " << cand.id().productIndex() << ") but collection defaults are (" << processIndex[i] << ", " << productIndex[i] << ")";
				}
				jet_cands_indices[cand.key()] = j;
			}
		}

		auto ptr = std::make_unique<std::vector<std::vector<int>>>(handle->size());
		indices_out.push_back(std::move(ptr));
	}

	edm::Handle<edm::View<reco::Candidate>> h_cands;
	iEvent.getByToken(CandTok_, h_cands);
	auto cands_out = std::make_unique<std::vector<LorentzVector>>();
	auto pdgids_out = std::make_unique<std::vector<int>>();

	//between-collection safety check REMOVED to avoid need to rekey puppi to packedPF (order already preserved)

	//loop over PF candidate collection once: check every jet in every jet collection
	//only PF candidates found in a jet collection will be kept
	for(unsigned c = 0; c < h_cands->size(); ++c){
		const auto& candPtr = h_cands->ptrs()[c];
		//if this cand is kept, it will be appended to cands_out
		unsigned potential_index = cands_out->size();
		bool keep = false;
		for(unsigned i = 0; i < h_jets.size(); ++i){
			const auto& h_jet = h_jets[i];
			const auto& jet_cands_indices = jets_cands_indices[i];
			for(unsigned j = 0; j < h_jet->size(); ++j){
				const auto& jet = h_jet->at(j);
				const auto& daughterPtrs = jet.daughterPtrVector();
				auto& jet_indices = (*indices_out[i])[j];
				//optimization: skip find for jets whose constituents have all already been found
				if(jet_indices.size()==daughterPtrs.size()) continue;
				bool candPtr_in_jet = candPtr.key() < jet_cands_indices.size() and jet_cands_indices[candPtr.key()]==(int)j;
				if(candPtr_in_jet){
					jet_indices.push_back(potential_index);
					keep = true;
					//in a given jet collection, a candidate can only be in one jet
					break;
				}
			}
		}
		if(keep){
			const auto& cand = h_cands->at(c);
			const auto pcand = (pat::PackedCandidate*)(&cand);
			cands_out->emplace_back(cand.pt(),cand.eta(),cand.phi(),cand.energy());
			for(auto & Prop : Props_){
				Prop->get_property(*pcand);
			}
		}
	}

	for(unsigned i = 0; i < indices_out.size(); ++i){
		iEvent.put(std::move(indices_out[i]),JetsNames_[i]+suffix_);
	}
	iEvent.put(std::move(cands_out));
	for(auto & Prop : Props_){
		Prop->put(iEvent);
	}
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetsConstituents);
