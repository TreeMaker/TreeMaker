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
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//
// class declaration
//

class GenJetProperties : public edm::global::EDProducer<> {
public:
  explicit GenJetProperties(const edm::ParameterSet&);
  ~GenJetProperties();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  edm::InputTag GenJetTag;
  edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok;

	
	
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
GenJetProperties::GenJetProperties(const edm::ParameterSet& iConfig)
{
  GenJetTag = iConfig.getParameter<edm::InputTag>("GenJetTag");
  GenJetTok = consumes<edm::View<reco::GenJet>>(GenJetTag);
  //register your products
  /* Examples
   *   produces<ExampleData2>();
   * 
   *   //if do put with a label
   *   produces<ExampleData2>("label");
   * 
   *   //if you want to put into the Run
   *   produces<ExampleData2,InRun>();
   */
  //now do what ever other initialization is needed
  //register your products
  produces<std::vector<double>>("invisibleEnergy");

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
  using namespace edm;
  using namespace reco;
  edm::Handle< edm::View<reco::GenJet> > GenJets;
  iEvent.getByToken(GenJetTok,GenJets);
  if( GenJets.isValid() ) {
    for(unsigned int i=0; i<GenJets->size();i++)
      {
	invisibleEnergy->push_back( GenJets->at(i).invisibleEnergy() );
      }
  }

  iEvent.put(std::move(invisibleEnergy),"invisibleEnergy");
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
