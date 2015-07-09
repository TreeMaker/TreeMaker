// -*- C++ -*-
//
// Package:    FilterDecisionProducer
// Class:      FilterDecisionProducer
// 
/**\class FilterDecisionProducer FilterDecisionProducer.cc RA2Classic/FilterDecisionProducer/src/FilterDecisionProducer.cc
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
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"

//
// class declaration
//

class FilterDecisionProducer : public edm::EDProducer {
public:
  explicit FilterDecisionProducer(const edm::ParameterSet&);
  ~FilterDecisionProducer();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag trigResultsTag_;
  std::string trigTagArg1_;
  std::string trigTagArg2_;
  std::string trigTagArg3_;
  std::string filterName_;
	
	
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
FilterDecisionProducer::FilterDecisionProducer(const edm::ParameterSet& iConfig)
{
  filterName_ = iConfig.getParameter <std::string> ("filterName");
  trigTagArg1_ = iConfig.getParameter <std::string> ("trigTagArg1");
  trigTagArg2_ = iConfig.getParameter <std::string> ("trigTagArg2");
  trigTagArg3_ = iConfig.getParameter <std::string> ("trigTagArg3");
  trigResultsTag_ = edm::InputTag(trigTagArg1_,trigTagArg2_,trigTagArg3_);


  produces<int>("");


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
	
}


FilterDecisionProducer::~FilterDecisionProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
FilterDecisionProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  int passesTrigger = -1;
  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  trigResults = trigResults;
  iEvent.getByLabel(trigResultsTag_,trigResults);
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults); 
  if(trigNames.triggerIndex(filterName_) < trigResults->size())
    passesTrigger=trigResults->accept(trigNames.triggerIndex(filterName_));

  std::auto_ptr<int> htp(new int(passesTrigger));
  iEvent.put(htp);
	
}

// ------------ method called once each job just before starting event loop  ------------
void 
FilterDecisionProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
FilterDecisionProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
FilterDecisionProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
FilterDecisionProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
FilterDecisionProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
FilterDecisionProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FilterDecisionProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(FilterDecisionProducer);
