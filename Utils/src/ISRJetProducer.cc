// system include files
#include <memory>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <iostream>
#include <TMath.h>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

//#define EDM_ML_DEBUG

class ISRJetProducer : public edm::EDProducer {
	public:
		explicit ISRJetProducer(const edm::ParameterSet&);
	private:
		virtual void produce(edm::Event&, const edm::EventSetup&);
		edm::InputTag GenPartTag_; 
		edm::EDGetTokenT<edm::View<reco::GenParticle>> GenPartTok_; 
		edm::InputTag JetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
		edm::InputTag JetLeptonTag_;
		edm::EDGetTokenT<std::vector<bool>> JetLeptonTok_;
		double MinPt_, MaxEta_;
};

ISRJetProducer::ISRJetProducer(const edm::ParameterSet& iConfig) :
	GenPartTag_(iConfig.getParameter<edm::InputTag>("GenPartTag")),
	GenPartTok_(consumes<edm::View<reco::GenParticle>>(GenPartTag_)),
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	JetLeptonTag_(iConfig.getParameter<edm::InputTag>("JetLeptonTag")),
	JetLeptonTok_(consumes<std::vector<bool>>(JetLeptonTag_)),
	MinPt_(iConfig.getParameter<double>("MinPt")),
	MaxEta_(iConfig.getParameter<double>("MaxEta"))
{
	produces<std::vector<bool> >("SubJetMask");
	produces<int>("");
}

void ISRJetProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	int nisr = 0;
	auto mask = std::make_unique<std::vector<bool>>();
	
	//get the input jet collection
	edm::Handle<edm::View<pat::Jet>> jets;
	iEvent.getByToken(JetTok_, jets);
	
	//get the mask for jets that are leptons (or isotracks)
	edm::Handle<std::vector<bool>> leptonMask;
	iEvent.getByToken(JetLeptonTok_, leptonMask);
	bool useLeptonMask = leptonMask.isValid();
	
	//get the gen particles collection
	edm::Handle<edm::View<reco::GenParticle> > genParticles;
	iEvent.getByToken(GenPartTok_, genParticles);
	
	//based on `bmaker_full::nisrMatch()` from babymaker/bmaker/plugins/bmaker_full.cc
	if(jets.isValid() && genParticles.isValid()){
		mask->resize(jets->size(),false);
		for (unsigned ijet=0; ijet<jets->size(); ++ijet){
			if(useLeptonMask && leptonMask->at(ijet)) continue;
			bool matched=false;
			for (unsigned imc=0; imc < genParticles->size(); ++imc){
				if (matched) break;
				const reco::GenParticle &mc = (*genParticles)[imc];
				if (mc.status()!=23 || abs(mc.pdgId())>5) continue;
				int momid = abs(mc.mother()->pdgId());
				if(!(momid==6 || momid==23 || momid==24 || momid==25 || momid>1e6)) continue; 
				//check against daughter in case of hard initial splitting
				for (unsigned idau=0; idau < mc.numberOfDaughters(); ++idau) {
					float dR = deltaR(jets->at(ijet).p4(), mc.daughter(idau)->p4());
					if(dR<0.3){
#ifdef EDM_ML_DEBUG
						std::cout<<"Jet: ("<<clean_jets[ijet].pt()<<", "<<clean_jets[ijet].eta()<<", "<<clean_jets[ijet].phi()
							<<"), MC: ("<<mc.daughter(idau)->pt()<<", "<<mc.daughter(idau)->eta()<<", "<<mc.daughter(idau)->phi()<<"), ID "<<mc.daughter(idau)->pdgId()<<". dR "<<dR <<std::endl;
#endif
						matched = true;
						break;
					}
				}
			} // Loop over MC particles
			if(!matched){
				mask->at(ijet) = true;
				//apply desired pt/eta cuts when counting
				if(jets->at(ijet).pt()>MinPt_ && std::abs(jets->at(ijet).eta() ) < MaxEta_) nisr++;
			}
		} // Loop over jets
	}
	
	auto htp = std::make_unique<int>(nisr);
	iEvent.put(std::move(htp));
	iEvent.put(std::move(mask),"SubJetMask");
}

DEFINE_FWK_MODULE(ISRJetProducer);

