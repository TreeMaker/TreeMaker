// system include files
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <unordered_set>

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
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::PtEtaPhiELorentzVector LorentzVector;

typedef edm::Ptr<reco::Candidate> CandPtr;
struct ptr_cand_hash : public std::unary_function<CandPtr, std::size_t> {
	std::size_t operator()(const CandPtr& ptr) const {
		return size_t(ptr.product());
	}
};
typedef std::unordered_set<CandPtr,ptr_cand_hash> CandPtrSet;

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
		virtual void get_property(const reco::Candidate& cand) {}

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
		void get_property(const reco::Candidate& cand) override { push_back(cand.pdgId()); }
};
DEFINE_CAND_PROP(PdgId);

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
	std::vector<std::vector<CandPtrSet>> jets_cands_sets;
	std::vector<std::unique_ptr<std::vector<std::vector<int>>>> indices_out;
	for(unsigned i = 0; i < JetsToks_.size(); ++i){
		edm::Handle<edm::View<pat::Jet>> handle;
		iEvent.getByToken(JetsToks_[i], handle);
		h_jets.push_back(handle);

		//make a hash table to search jet constituent list more efficiently
		jets_cands_sets.emplace_back();
		auto& jet_cands_sets = jets_cands_sets.back();
		for(const auto& jet : *h_jets.back()){
			jet_cands_sets.emplace_back(jet.daughterPtrVector().begin(), jet.daughterPtrVector().end());
		}

		auto ptr = std::make_unique<std::vector<std::vector<int>>>(handle->size());
		indices_out.push_back(std::move(ptr));
	}

	edm::Handle<edm::View<reco::Candidate>> h_cands;
	iEvent.getByToken(CandTok_, h_cands);
	auto cands_out = std::make_unique<std::vector<LorentzVector>>();
	auto pdgids_out = std::make_unique<std::vector<int>>();

	//loop over PF candidate collection once: check every jet in every jet collection
	//only PF candidates found in a jet collection will be kept
	for(unsigned c = 0; c < h_cands->size(); ++c){
		const auto& cand = h_cands->at(c);
		const auto& candPtr = h_cands->ptrs()[c];
		//if this cand is kept, it will be appended to cands_out
		unsigned potential_index = cands_out->size();
		bool keep = false;
		for(unsigned i = 0; i < h_jets.size(); ++i){
			const auto& jet_cands_sets = jets_cands_sets[i];
			for(unsigned j = 0; j < jet_cands_sets.size(); ++j){
				const auto& jet_cands_set = jet_cands_sets[j];
				auto& jet_indices = (*indices_out[i])[j];
				//optimization: skip find for jets whose constituents have all already been found
				if(jet_indices.size()==jet_cands_set.size()) continue;
				const auto& candPtr_in_jet = jet_cands_set.find(candPtr);
				if(candPtr_in_jet != jet_cands_set.end()){
					jet_indices.push_back(potential_index);
					keep = true;
					//in a given jet collection, a candidate can only be in one jet
					break;
				}
			}
		}
		if(keep){
			cands_out->emplace_back(cand.pt(),cand.eta(),cand.phi(),cand.energy());
			for(auto & Prop : Props_){
				Prop->get_property(cand);
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
