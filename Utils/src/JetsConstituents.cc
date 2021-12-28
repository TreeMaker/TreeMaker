// system include files
#include <memory>
#include <string>
#include <vector>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
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

class JetsConstituents : public edm::global::EDProducer<> {
public:
	explicit JetsConstituents(const edm::ParameterSet&);
	~JetsConstituents() override {}

private:
	void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

	const std::string suffix_;
	std::vector<edm::InputTag> JetsTags_;
	std::vector<std::string> JetsNames_;
    std::vector<edm::EDGetTokenT<edm::View<pat::Jet>>> JetsToks_;
	edm::EDGetTokenT<edm::View<reco::Candidate>> CandTok_;
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
}

void JetsConstituents::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
	std::vector<edm::Handle<edm::View<pat::Jet>>> h_jets;
	std::vector<std::unique_ptr<std::vector<std::vector<int>>>> indices_out;
	for(unsigned i = 0; i < JetsToks_.size(); ++i){
		edm::Handle<edm::View<pat::Jet>> handle;
		iEvent.getByToken(JetsToks_[i], handle);
		h_jets.push_back(handle);
		auto ptr = std::make_unique<std::vector<std::vector<int>>>(handle->size());
		indices_out.push_back(std::move(ptr));
	}

	edm::Handle<edm::View<reco::Candidate>> h_cands;
	iEvent.getByToken(CandTok_, h_cands);
	auto cands_out = std::make_unique<std::vector<LorentzVector>>();

	//loop over PF candidate collection once: check every jet in every jet collection
	//only PF candidates found in a jet collection will be kept
	for(unsigned c = 0; c < h_cands->size(); ++c){
		const auto& cand = h_cands->at(c);
		const auto& candPtr = h_cands->ptrs()[c];
		//if this cand is kept, it will be appended to cands_out
		unsigned potential_index = cands_out->size();
		bool keep = false;
		for(unsigned i = 0; i < h_jets.size(); ++i){
			const auto& h_jet = h_jets[i];
			for(unsigned j = 0; j < h_jet->size(); ++j){
				const auto& jet = h_jet->at(j);
				const auto& daughterPtrs = jet.daughterPtrVector();
				auto& jet_indices = (*indices_out[i])[j];
				//optimization: skip find for jets whose constituents have all already been found
				if(jet_indices.size()==daughterPtrs.size()) continue;
				const auto& candPtr_in_jet = std::find(daughterPtrs.begin(), daughterPtrs.end(), candPtr);
				if(candPtr_in_jet != daughterPtrs.end()){
					jet_indices.push_back(potential_index);
					keep = true;
					//in a given jet collection, a candidate can only be in one jet
					break;
				}
			}
		}
		if(keep){
			cands_out->emplace_back(cand.pt(),cand.eta(),cand.phi(),cand.energy());
		}
	}

	for(unsigned i = 0; i < indices_out.size(); ++i){
		iEvent.put(std::move(indices_out[i]),JetsNames_[i]+suffix_);
	}
	iEvent.put(std::move(cands_out));
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetsConstituents);
