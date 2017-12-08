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
#include <algorithm>
#include <sstream>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "TLorentzVector.h"
//
// class declaration
//

class TriggerProducer : public edm::global::EDProducer<> {
public:
  explicit TriggerProducer(const edm::ParameterSet&);
  ~TriggerProducer();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  // ----------member data ---------------------------
  void GetInputTag(edm::InputTag& tag, std::string arg1, std::string arg2, std::string arg3, std::string arg1_default);
  edm::InputTag trigResultsTag_, trigPrescalesTag_;
  edm::EDGetTokenT<edm::TriggerResults> trigResultsTok_;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> trigPrescalesTok_;
  std::vector<std::string> parsedTrigNamesVec;
  edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> trigObjCollToken;
  bool saveHLTObj = true;
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
  parsedTrigNamesVec = iConfig.getParameter <std::vector<std::string> > ("triggerNameList");
  //sort the trigger names
  std::sort(parsedTrigNamesVec.begin(), parsedTrigNamesVec.end());
  //print triggers
  std::stringstream message;
  message << "List of stored triggers:" << "\n";
  for(unsigned t = 0; t < parsedTrigNamesVec.size(); ++t){
    message << t << ": " << parsedTrigNamesVec[t] << "\n";
  }
  edm::LogInfo("TreeMaker") << message.str();
  
  GetInputTag(trigResultsTag_,
              iConfig.getParameter <std::string> ("trigTagArg1"),
              iConfig.getParameter <std::string> ("trigTagArg2"),
              iConfig.getParameter <std::string> ("trigTagArg3"),
              "TriggerResults");

  GetInputTag(trigPrescalesTag_,
              iConfig.getParameter <std::string> ("prescaleTagArg1"),
              iConfig.getParameter <std::string> ("prescaleTagArg2"),
              iConfig.getParameter <std::string> ("prescaleTagArg3"),
              "patTrigger");

  trigResultsTok_ = consumes<edm::TriggerResults>(trigResultsTag_);
  trigPrescalesTok_ = consumes<pat::PackedTriggerPrescales>(trigPrescalesTag_);

  edm::InputTag theTrigObjLabel("selectedPatTrigger");
  trigObjCollToken = consumes<pat::TriggerObjectStandAloneCollection>(theTrigObjLabel);
  
  produces<std::vector<std::string> >("TriggerNames");
  produces<std::vector<int> >("TriggerPass");
  produces<std::vector<int> >("TriggerPrescales");
  if(saveHLTObj) produces<std::vector<TLorentzVector> >("HLTElectronObjects");
}


TriggerProducer::~TriggerProducer()
{}

//
// member functions
//

// ------------ helper function to make InputTags ------------
void
TriggerProducer::GetInputTag(edm::InputTag& tag, std::string arg1, std::string arg2, std::string arg3, std::string arg1_default=""){
  // We we make the producer a little smarter. There are four cases we look at
  // 1) arg1 and arg3 are set, if this is the case we create the label bases on all three arguments
  // 2) arg3 is not set, in this case we create the label based only on arg1
  // 3) Neither arg1 nor arg3 are set, in this case we default to searching for arg1_default
  // 4) arg1 is not set, but arg3 is set, we look for arg1_default in the process defined by arg3

  if(arg1.empty()) arg1 = arg1_default;
  
  if(arg3.empty()){
    tag = edm::InputTag(arg1);
  } else {
    tag = edm::InputTag(arg1,arg2,arg3);
  }	
}

// ------------ method called to produce the data  ------------
void
TriggerProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  auto passTrigVec = std::make_unique<std::vector<int>>(parsedTrigNamesVec.size(),-1);
  auto trigPrescaleVec = std::make_unique<std::vector<int>>(parsedTrigNamesVec.size(),1);
  auto trigNamesVec = std::make_unique<std::vector<std::string>>(parsedTrigNamesVec.size(),"");
  auto hltEleObj = std::make_unique<std::vector<TLorentzVector>>();

  //int passesTrigger;
  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  iEvent.getByToken(trigResultsTok_,trigResults);
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);
  edm::Handle<pat::PackedTriggerPrescales> trigPrescales;
  iEvent.getByToken(trigPrescalesTok_,trigPrescales);

  //Find the matching triggers
  std::string testTriggerName;
  for(unsigned int parsedIndex = 0; parsedIndex < parsedTrigNamesVec.size(); parsedIndex++){
    trigNamesVec->at(parsedIndex) = parsedTrigNamesVec[parsedIndex];
    for(unsigned int trigIndex = 0; trigIndex < trigNames.size(); trigIndex++){
      testTriggerName = trigNames.triggerName(trigIndex);
      if(testTriggerName.find(parsedTrigNamesVec.at(parsedIndex)) != std::string::npos){
        trigNamesVec->at(parsedIndex) = testTriggerName;
        passTrigVec->at(parsedIndex) = trigResults->accept(trigIndex);
        trigPrescaleVec->at(parsedIndex) = trigPrescales->getPrescaleForIndex(trigIndex);
        break; //We only match one trigger to each trigger name fragment passed
      }
    }
  }

  edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
  iEvent.getByToken(trigObjCollToken,triggerObjects);
  //save the trigger object corresponding to the trigger HLT_Ele27_WPTight_Gsf_v*. Obtained code from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#Trigger
  // loop over selected trigger objects                                                                                              
  for (pat::TriggerObjectStandAlone obj : *triggerObjects) {
    if(obj.pt() < 25.0) continue;//look for HLT objects with Pt > 25GeV only.
    obj.unpackPathNames(trigNames);
    const std::vector<std::string>& pathNamesAll = obj.pathNames(false);
    for (const auto& pathName : pathNamesAll){
      bool isBoth = obj.hasPathName( pathName, true, true );//object is associated wih l3 filter and associated to the last filter of a successfull path. this object caused the trigger to fire.
      const std::string& path_i = pathName;
      if(isBoth && path_i.find("HLT_Ele27_WPTight_Gsf_v")!= std::string::npos){
	hltEleObj->emplace_back(obj.px(),obj.py(),obj.pz(),obj.energy());
	break;
      }
    }
  }

  iEvent.put(std::move(passTrigVec),"TriggerPass");
  iEvent.put(std::move(trigPrescaleVec),"TriggerPrescales");
  iEvent.put(std::move(trigNamesVec),"TriggerNames");
  if(saveHLTObj) iEvent.put(std::move(hltEleObj),"HLTElectronObjects");

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
