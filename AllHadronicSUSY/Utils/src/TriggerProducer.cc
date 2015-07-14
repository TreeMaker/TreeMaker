// -*- C++ -*-
//
// Package:    TriggerProducer
// Class:      TriggerProducer
// 
/**\class TriggerProducer TriggerProducer.cc RA2Classic/TriggerProducer/src/TriggerProducer.cc
 */
//
// Original Author:  Sam Bein,
//         Created:  Wednesday June 24 2015
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

class TriggerProducer : public edm::EDProducer {
public:
  explicit TriggerProducer(const edm::ParameterSet&);
  ~TriggerProducer();
	
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
  std::string triggerNameList_;
  std::vector<std::string> parsedTrigNamesVec;
	
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
TriggerProducer::TriggerProducer(const edm::ParameterSet& iConfig)
{
  triggerNameList_ = iConfig.getParameter <std::string> ("triggerNameList");
  trigTagArg1_ = iConfig.getParameter <std::string> ("trigTagArg1");
  trigTagArg2_ = iConfig.getParameter <std::string> ("trigTagArg2");
  trigTagArg3_ = iConfig.getParameter <std::string> ("trigTagArg3");
  trigResultsTag_ = edm::InputTag(trigTagArg1_,trigTagArg2_,trigTagArg3_);

  produces<std::vector<std::string> >("TriggerNames");
  produces<std::vector<int> >("PassTrigger");
}


TriggerProducer::~TriggerProducer()
{}

//
// member functions
//

// ------------ method called to produce the data  ------------
void
TriggerProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::auto_ptr<std::vector<int> > passTrigVec(new std::vector<int>());
  std::auto_ptr<std::vector<std::string> > trigNamesVec(new std::vector<std::string>());

  //int passesTrigger;
  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  trigResults = trigResults;
  iEvent.getByLabel(trigResultsTag_,trigResults);
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults); 

  //Find the matching triggers

  std::string testTriggerName;
  for(unsigned int trigIndex = 0; trigIndex < trigNames.size(); trigIndex++){
    testTriggerName = trigNames.triggerName(trigIndex);
    for(unsigned int parsedIndex = 0; parsedIndex < parsedTrigNamesVec.size(); parsedIndex++){
      if(testTriggerName.find(parsedTrigNamesVec.at(parsedIndex)) != std::string::npos){
	  trigNamesVec->push_back(testTriggerName.c_str());
	  passTrigVec->push_back(trigResults->accept(trigIndex));
	  //std::cout << "Matched: " << testTriggerName << std::endl;
	  //break; //We only match one trigger to each trigger name fragment passed
      }
    }
  }
      /*
 for(unsigned int i = 0; i < parsedTrigNamesVec.size(); i++)
    {
      passesTrigger = -1;
      trigNamesVec->push_back(parsedTrigNamesVec.at(i).c_str());
      if((trigNames.triggerIndex(parsedTrigNamesVec.at(i)) < trigResults->size())) 
	{
	  passesTrigger=trigResults->accept(trigNames.triggerIndex(parsedTrigNamesVec.at(i).c_str()));
	}
	  passTrigVec->push_back(passesTrigger);
    }
      */
  // for (int iHLT = 0 ; iHLT<static_cast<int>(trigResults->size()); ++iHLT) 
  // {	
  //   //std::cout << "tname="<< trigNames.triggerName(iHLT)<< std::endl;
  //   //std::cout << "tndex="<< trigNames.triggerIndex(trigNames.triggerName(iHLT)) << std::endl;
  //   passesTrigger=trigResults->accept(iHLT);
  //   passTrigVec->push_back(passesTrigger);
  // }
  iEvent.put(passTrigVec,"PassTrigger");
  iEvent.put(trigNamesVec,"TriggerNames");	
}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerProducer::beginJob()
{
  std::cout << "will store trigger information for..." << std::endl;
  std::stringstream ss(triggerNameList_);
  std::istream_iterator<std::string> begin(ss);
  std::istream_iterator<std::string> end;
  std::vector<std::string> vstrings(begin, end);
  std::copy(vstrings.begin(), vstrings.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
  for(unsigned int i = 0; i< vstrings.size(); i++)
    parsedTrigNamesVec.push_back(vstrings.at(i));
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
TriggerProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
TriggerProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TriggerProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TriggerProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerProducer);
