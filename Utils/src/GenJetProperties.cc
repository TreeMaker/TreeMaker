// -*- C++ -*-
//
// Package:    GenJetProperties
// Class:      GenJetProperties
// 


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"

//
// class declaration
//

class GenJetProperties : public edm::global::EDProducer<> {
public:
  explicit GenJetProperties(const edm::ParameterSet&);
  ~GenJetProperties() override;
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  edm::InputTag GenJetTag;
  edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok;
  edm::InputTag PrunedTag, SoftDropTag;
  edm::EDGetTokenT<std::vector<reco::BasicJet>> PrunedTok, SoftDropTok;
  double distMax;
	
	
  // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
GenJetProperties::GenJetProperties(const edm::ParameterSet& iConfig) :
  GenJetTag(iConfig.getParameter<edm::InputTag>("GenJetTag")),
  GenJetTok(consumes<edm::View<reco::GenJet>>(GenJetTag)),
  PrunedTag(iConfig.getParameter<edm::InputTag>("PrunedGenJetTag")),
  SoftDropTag(iConfig.getParameter<edm::InputTag>("SoftDropGenJetTag")),
  PrunedTok(consumes<std::vector<reco::BasicJet>>(PrunedTag)),
  SoftDropTok(consumes<std::vector<reco::BasicJet>>(SoftDropTag)),
  distMax(iConfig.getParameter<double>("distMax"))
{
  //register your products
  produces<std::vector<double>>("invisibleEnergy");
  produces<std::vector<double>>("prunedMass");
  produces<std::vector<double>>("softDropMass");
}


GenJetProperties::~GenJetProperties()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
GenJetProperties::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;
	
  auto invisibleEnergy = std::make_unique<std::vector<double>>();
  auto prunedMass = std::make_unique<std::vector<double>>();
  auto softDropMass = std::make_unique<std::vector<double>>();

  edm::Handle< edm::View<reco::GenJet> > GenJets;
  iEvent.getByToken(GenJetTok,GenJets);
  if( GenJets.isValid() ) {
    edm::Handle<std::vector<reco::BasicJet>> PrunedJets;
    iEvent.getByToken(PrunedTok,PrunedJets);
    bool doPruned = PrunedJets.isValid();

    edm::Handle<std::vector<reco::BasicJet>> SoftDropJets;
    iEvent.getByToken(SoftDropTok,SoftDropJets);
    bool doSoftDrop = SoftDropJets.isValid();

    for(const auto& GenJet: *GenJets){
      invisibleEnergy->push_back( GenJet.invisibleEnergy() );
      double pruned = 0.0;
      double softdrop = 0.0;

      if(doPruned){
        for(const auto& PrunedJet: *PrunedJets){
          if(reco::deltaR(GenJet,PrunedJet)<distMax){
            pruned = PrunedJet.mass();
            break;
          }
        }
      }
      if(doSoftDrop){
        for(const auto& SoftDropJet: *SoftDropJets){
          if(reco::deltaR(GenJet,SoftDropJet)<distMax){
            softdrop = SoftDropJet.mass();
            break;
          }
        }
      }

      prunedMass->push_back(pruned);
      softDropMass->push_back(softdrop);
    }
  }

  iEvent.put(std::move(invisibleEnergy),"invisibleEnergy");
  iEvent.put(std::move(prunedMass),"prunedMass");
  iEvent.put(std::move(softDropMass),"softDropMass");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenJetProperties::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenJetProperties);
