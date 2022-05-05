// -*- C++ -*-
//
// Package:    GenLeptonRecoCand
// Class:      GenLeptonRecoCand
// 
/**\class GenLeptonRecoCand GenLeptonRecoCand.cc RA2Classic/GenLeptonRecoCand/src/GenLeptonRecoCand.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include <TVector3.h>

//
// class declaration
//

class GenLeptonRecoCand : public edm::global::EDProducer<> {
public:
  explicit GenLeptonRecoCand(const edm::ParameterSet&);
  ~GenLeptonRecoCand() override {}
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  edm::InputTag PrunedGenParticleTag_;
  edm::EDGetTokenT<edm::View<reco::GenParticle>> PrunedGenParticleTok_;
	
  const reco::GenParticle* BosonFound(const reco::GenParticle * particle) const;
  const reco::GenParticle* TauFound(const reco::GenParticle * particle) const;
};

//
// constructors and destructor
//
GenLeptonRecoCand::GenLeptonRecoCand(const edm::ParameterSet& iConfig) :
  PrunedGenParticleTag_(iConfig.getParameter<edm::InputTag >("PrunedGenParticleTag")),
  PrunedGenParticleTok_(consumes<edm::View<reco::GenParticle>>(PrunedGenParticleTag_))
{
  //register your product

  produces<std::vector<reco::GenParticle>>("Muon");
  produces<std::vector<reco::GenParticle>>("Electron");
  produces<std::vector<reco::GenParticle>>("Tau");
  produces<std::vector<bool>>("TauHadronic");
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void
GenLeptonRecoCand::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;	
  auto selectedMuon = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedElectron = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedTau = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedTauHadronic = std::make_unique<std::vector<bool>>();

  Handle<edm::View<reco::GenParticle> > pruned;
  iEvent.getByToken(PrunedGenParticleTok_,pruned);

  for(size_t i=0; i<pruned->size();i++)
    {
      if( (abs((*pruned)[i].pdgId() ) == 24 || abs((*pruned)[i].pdgId() ) == 23 || abs((*pruned)[i].pdgId() ) == 1000024 ) && (*pruned)[i].status()==22) // needs to be checked if this workes for Z 23 as well
	{
	  const reco::GenParticle * FinalBoson = BosonFound(&(*pruned)[i]);
	  size_t bosonDaughters = FinalBoson->numberOfDaughters();
	  for(size_t ii=0;ii< bosonDaughters; ii++)
	    {
	      if(abs(FinalBoson->daughter(ii)->pdgId())== 11) 
		{
		  selectedElectron->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));
		}
	      else if(abs(FinalBoson->daughter(ii)->pdgId())== 13) 
		{
		  selectedMuon->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));
		}
	      else if(abs(FinalBoson->daughter(ii)->pdgId())== 15) 
		{
		  selectedTau->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));

		  const reco::GenParticle * FinalTauDecay = TauFound((reco::GenParticle*)FinalBoson->daughter(ii));

		  bool hadTauDecay=true;
		  for(size_t iii=0; iii<FinalTauDecay->numberOfDaughters();iii++)
		    {
		      if(abs(FinalTauDecay->daughter(iii)->pdgId())== 11) 
			{
			  selectedElectron->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
			  hadTauDecay=false;
			}
		      else if(abs(FinalTauDecay->daughter(iii)->pdgId())== 13) 
			{
			  selectedMuon->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
			  hadTauDecay=false;
			}
          }
		  selectedTauHadronic->push_back(hadTauDecay);
		}
	  }

	}
	  
    }

  iEvent.put(std::move(selectedMuon),"Muon");
  iEvent.put(std::move(selectedElectron),"Electron");
  iEvent.put(std::move(selectedTau),"Tau");
  iEvent.put(std::move(selectedTauHadronic),"TauHadronic");

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenLeptonRecoCand::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

const reco::GenParticle* GenLeptonRecoCand::BosonFound(const reco::GenParticle * particle) const
{
  for(size_t i=0;i< particle->numberOfDaughters();i++)
    {
      if(abs(particle->daughter(i)->pdgId() )== 24 || abs(particle->daughter(i)->pdgId() ) == 23 || abs(particle->daughter(i)->pdgId() ) == 1000024) return BosonFound((reco::GenParticle*)particle->daughter(i));
    }
  return particle;
	
}

const reco::GenParticle* GenLeptonRecoCand::TauFound(const reco::GenParticle * particle) const
{
  for(size_t i=0;i< particle->numberOfDaughters();i++)
    {
      if(abs(particle->daughter(i)->pdgId()) == 15) return TauFound((reco::GenParticle*)particle->daughter(i));
    }
  return particle;
	
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenLeptonRecoCand);
