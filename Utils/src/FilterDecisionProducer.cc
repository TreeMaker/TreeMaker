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
#include "FWCore/Framework/interface/global/EDProducer.h"

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

class FilterDecisionProducer : public edm::global::EDProducer<> {
public:
  explicit FilterDecisionProducer(const edm::ParameterSet&);
  ~FilterDecisionProducer() override;
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  // ----------member data ---------------------------
  edm::InputTag trigResultsTag_;
  edm::EDGetTokenT<edm::TriggerResults> trigResultsTok_;
  std::string trigTagArg1_;
  std::string trigTagArg2_;
  std::string trigTagArg3_;
  std::string filterName_;
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
  // We we make the producer a little smarter. There are four cases we look at
  // 1) trigTagArg1_ and trigTagArg3_ are set, if this is the case we create the label bases on all three arguments
  // 2) trigTagArg3_ is not set, in this case we create the label based only on  trigTagArg1_
  // 3) Neither trigTagArg1_ or TrigTagArg3_ are set, in this case we default to searching for "TriggerResults"
  // 4) trigTag1_ is not set, but trigTagArg3_ is set, we look for "TriggerResults" in the process defined by trigTagArg3_

  if(trigTagArg1_.empty()) trigTagArg1_ = "TriggerResults";
  
  if(trigTagArg3_.empty()){
    trigResultsTag_ = edm::InputTag(trigTagArg1_);
  } else {
    trigResultsTag_ = edm::InputTag(trigTagArg1_,trigTagArg2_,trigTagArg3_);
  }
  trigResultsTok_ = consumes<edm::TriggerResults>(trigResultsTag_);

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
FilterDecisionProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{

  int passesTrigger = -1;
  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  trigResults = trigResults;
  iEvent.getByToken(trigResultsTok_,trigResults);
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults); 
  if(trigNames.triggerIndex(filterName_) < trigResults->size())
    passesTrigger=trigResults->accept(trigNames.triggerIndex(filterName_));

  auto htp = std::make_unique<int>(passesTrigger);
  iEvent.put(std::move(htp));
	
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
