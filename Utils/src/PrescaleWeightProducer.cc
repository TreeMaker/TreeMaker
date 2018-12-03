// -*- C++ -*-
//
// Package:    PrescaleWeightProducer
// Class:      PrescaleWeightProducer
//
/**\class PrescaleWeightProducer PrescaleWeightProducer.cc AllHadronicSusy/Utils/src/PrescaleWeightProducer.cc
   Description: <one line class summary>
   Implementation:
   <Notes on implementation>
*/
//
// Created by Sam Bein, Tue Sept 10 17:58:04 CET 2015
// $Id: PrescaleWeightProducer.cc,v 1.7 2012/07/09 11:43:55 Bein Exp $

// system include files
#include <cmath>
#include <memory>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <cstdlib> 

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerResultsByName.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

using namespace std;
using namespace trigger;
using namespace edm;


class PrescaleWeightProducer: public edm::global::EDProducer<> {
public:
  explicit PrescaleWeightProducer(const edm::ParameterSet&);
  ~PrescaleWeightProducer() override;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

  edm::EDGetTokenT<edm::TriggerResults> _triggerBits;
  edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> _triggerObjects;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> _triggerPrescales;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> _triggerPrescalesL1min;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> _triggerPrescalesL1max;
};

PrescaleWeightProducer::PrescaleWeightProducer(const edm::ParameterSet& iConfig) :
  _triggerBits(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits"))), 
  _triggerObjects(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("objects"))), 
  _triggerPrescales(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescales"))), 
  _triggerPrescalesL1min(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescalesL1min"))), 
  _triggerPrescalesL1max(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescalesL1max"))) 
{

  produces<double> ("weight");
  produces<double> ("ht");
  produces<double> ("mht");

}

PrescaleWeightProducer::~PrescaleWeightProducer() {
}

void PrescaleWeightProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {

  double resultWeight = 1.;

  edm::Handle<edm::TriggerResults> triggerBits;
  iEvent.getByToken(_triggerBits, triggerBits);
  edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
  iEvent.getByToken(_triggerObjects, triggerObjects);
  edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;
  iEvent.getByToken(_triggerPrescales, triggerPrescales);
  edm::Handle<pat::PackedTriggerPrescales> triggerPrescalesL1min;
  iEvent.getByToken(_triggerPrescalesL1min, triggerPrescalesL1min);
  edm::Handle<pat::PackedTriggerPrescales> triggerPrescalesL1max;
  iEvent.getByToken(_triggerPrescalesL1max, triggerPrescalesL1max);


  const edm::TriggerNames & trigNames = iEvent.triggerNames(*triggerBits);

  vector<string> trigNameVec;
  vector<bool> trigPassVec;
  vector<int> trigThresholdVec;
  vector<int> trigPrescaleVec;
  int finalPrescale = 0;
  double ht = 0.0;
  double mht = 0.0;

  for (unsigned int i = 0; i < triggerBits->size(); i++) {
    const string& trigName = trigNames.triggerName(i);
    size_t strpos = trigName.find("HLT_PFHT");
    if (strpos == string::npos)
      continue;
    strpos = trigName.find("0_v");
    if (!(strpos == 10 || strpos==11)) continue;
    bool pass = triggerBits->accept(i);
    int ps = triggerPrescales->getPrescaleForIndex(i);
    int psL1min = triggerPrescalesL1min->getPrescaleForIndex(i);
    int psL1max = triggerPrescalesL1max->getPrescaleForIndex(i);
    string strthr = trigName.substr(8, strpos==10 ? 3 : 4);
    int thresh = stoi(strthr.c_str());
    if (psL1min==psL1max || psL1min==1) ps*=psL1min; 
    else ps = -1.0;
    trigNameVec.push_back(trigName);
    trigPassVec.push_back(pass);
    trigThresholdVec.push_back(thresh);
    trigPrescaleVec.push_back(ps);
  }   

  bool gotht = false; bool gotmht = false;
  for (pat::TriggerObjectStandAlone obj : *triggerObjects) 
    {
      obj.unpackPathNames(trigNames);
      if (!(obj.collection() == "hltPFHTJet30::HLT")) continue;//hltPFHT::HLT
      if ( abs(obj.filterIds()[0]) == 89) 
	{
	  ht = obj.pt();
	  gotht = true;
	  continue;
	}
      if ( abs((obj.filterIds()[0]) == 90) )
	{
	  mht = obj.pt(); 
	  gotmht = true;
	  continue;
	}
      if (gotht && gotmht)
	{
	  break;
	}
    }


  //int requiredTrigThreshold = 0;
  int requiredTrigPrescale = 9999999;
  int requiredTrigIndex = -1;
  for(unsigned int t=0; t<trigNameVec.size();t++)
      {
	if(trigPrescaleVec[t]<requiredTrigPrescale && trigThresholdVec[t]<ht)
	  {
	    requiredTrigPrescale = trigPrescaleVec[t];
	    requiredTrigIndex = t;
	  }
      }

    if( requiredTrigIndex==-1 || trigPassVec[requiredTrigIndex]==false)
      finalPrescale = 0;
    else
      finalPrescale = trigPrescaleVec[requiredTrigIndex];


  resultWeight*=finalPrescale;

  auto pOut = std::make_unique<double>(resultWeight);
  iEvent.put(std::move(pOut), "weight");

  auto htOut = std::make_unique<double>((ht));
  iEvent.put(std::move(htOut), "ht");

  auto mhtOut = std::make_unique<double>((mht));
  iEvent.put(std::move(mhtOut), "mht");

  
}


void PrescaleWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE( PrescaleWeightProducer);
