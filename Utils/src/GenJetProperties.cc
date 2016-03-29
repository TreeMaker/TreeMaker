// -*- C++ -*-
//
// Package:    GenJetProperties
// Class:      GenJetProperties
// 


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//
// class declaration
//

class GenJetProperties : public edm::EDProducer {
public:
  explicit GenJetProperties(const edm::ParameterSet&);
  ~GenJetProperties();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
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
  const std::string string0("invisibleEnergy");
  produces<std::vector<double> > (string0).setBranchAlias(string0);

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
GenJetProperties::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
	
  std::auto_ptr< std::vector<double> > invisibleEnergy(new std::vector<double>);
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

  const std::string string0("invisibleEnergy");
  iEvent.put(invisibleEnergy,string0);
}

// ------------ method called once each job just before starting event loop  ------------
void 
GenJetProperties::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenJetProperties::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
GenJetProperties::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GenJetProperties::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GenJetProperties::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GenJetProperties::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
