// system include files
#include <memory>
#include <string>
#include <vector>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

// this is a simple module inspired by JetSubstructurePacker and PatJetUpdater
// just to provide references within a jet collection to an updated subjet collection
// that might have new userfloats, discriminators, etc.
class SubjetUpdater : public edm::global::EDProducer<> {
	public:
		explicit SubjetUpdater(const edm::ParameterSet&);
	private:
		void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		edm::InputTag JetTag_, SubjetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_, SubjetTok_;
		std::string SubjetOldName_, SubjetNewName_;
};

SubjetUpdater::SubjetUpdater(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	SubjetTag_(iConfig.getParameter<edm::InputTag>("SubjetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	SubjetTok_(consumes<edm::View<pat::Jet>>(SubjetTag_)),
	SubjetOldName_(iConfig.getParameter<std::string>("OldName")),
	SubjetNewName_(iConfig.getParameter<std::string>("NewName"))
{
	produces<std::vector<pat::Jet>>();
}

void SubjetUpdater::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	auto output = std::make_unique<std::vector<pat::Jet>>();

	edm::Handle<edm::View<pat::Jet>> jets;
	iEvent.getByToken(JetTok_, jets);
	edm::Handle<edm::View<pat::Jet>> subjets;
	iEvent.getByToken(SubjetTok_, subjets);

	//construct map of old subjets to jets
	std::map<edm::Ptr<reco::Candidate>,unsigned> oldMap;
	for(unsigned ij = 0; ij < jets->size(); ++ij){
		const auto& oldSubjets = jets->at(ij).subjets(SubjetOldName_);
		for(unsigned isj = 0; isj < oldSubjets.size(); ++isj){
			oldMap.emplace(oldSubjets[isj]->originalObjectRef(),ij);
		}
	}

	//construct map of jets to new subjets (using prev map)
	std::map<unsigned,std::vector<edm::Ptr<pat::Jet>>> newMap;
	for(unsigned isj = 0; isj < subjets->size(); ++isj){
		auto itr = oldMap.find(subjets->at(isj).originalObjectRef());
		if(itr!=oldMap.end()){
			unsigned ij = itr->second;
			auto& vec = newMap[ij];
			vec.push_back(subjets->ptrAt(isj));
		}
	}

	output->reserve(jets->size());
	for(unsigned idx = 0; idx < jets->size(); ++idx) {
		// construct the Jet from the ref -> save ref to original object
		output->push_back(jets->ptrAt(idx));
		output->back().addSubjets(newMap[idx],SubjetNewName_);
	}

	iEvent.put(std::move(output));
}

DEFINE_FWK_MODULE(SubjetUpdater);
