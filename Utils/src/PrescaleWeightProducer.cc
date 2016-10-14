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
#include <stdlib.h> 

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
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


class PrescaleWeightProducer: public edm::EDProducer {
public:
  explicit PrescaleWeightProducer(const edm::ParameterSet&);
  ~PrescaleWeightProducer();
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);//Van

private:
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void beginJob();
  virtual void endJob();
  virtual void beginRun(edm::Run&, edm::EventSetup const&);

  edm::EDGetTokenT<edm::TriggerResults> _triggerBits;
  edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> _triggerObjects;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> _triggerPrescales;
};

PrescaleWeightProducer::PrescaleWeightProducer(const edm::ParameterSet& iConfig) :
  _triggerBits(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits"))), 
  _triggerObjects(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("objects"))), 
  _triggerPrescales(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescales"))) 
{

  produces<double> ("weight");
  produces<double> ("ht");
  produces<double> ("mht");

}

PrescaleWeightProducer::~PrescaleWeightProducer() {
}

void PrescaleWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  double resultWeight = 1.;

  edm::Handle<edm::TriggerResults> triggerBits;
  iEvent.getByToken(_triggerBits, triggerBits);
  edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
  iEvent.getByToken(_triggerObjects, triggerObjects);
  edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;
  iEvent.getByToken(_triggerPrescales, triggerPrescales);
  const edm::TriggerNames & trigNames = iEvent.triggerNames(*triggerBits);

  vector<string> trigNameVec;
  vector<bool> trigPassVec;
  vector<int> trigThresholdVec;
  vector<int> trigPrescaleVec;
  int finalPrescale = 0;
  double ht = 0.0;
  double mht = 0.0;

  for (unsigned int i = 0; i < triggerBits->size(); i++) {
    const string trigName = trigNames.triggerName(i);
    size_t found;
    found = trigName.find("HLT_PFHT");
    if (found == string::npos)
      continue;
    found = trigName.find("0_v");
    if (found != 10)
      continue;
    bool pass = triggerBits->accept(i);
    int ps = triggerPrescales->getPrescaleForIndex(i);
    string strthr = trigName.substr(8, 3);
    int thresh = int(atof(strthr.c_str()));
    trigNameVec.push_back(trigName);
    trigPassVec.push_back(pass);
    trigThresholdVec.push_back(thresh);
    trigPrescaleVec.push_back(ps);
  }   

  int gotht = 0; int gotmht = 0;
  for (pat::TriggerObjectStandAlone obj : *triggerObjects) 
    {
      obj.unpackPathNames(trigNames);
      if (!(obj.collection() == "hltPFHT::HLT")) continue;
      if ( abs(obj.filterIds()[0]) == 89) 
	{
	  ht = obj.pt();
	  gotht = 1;
	  continue;
	}
      if ( abs((obj.filterIds()[0]) == 90) )
	{
	  mht = obj.pt(); 
	  gotmht = 1;
	  continue;
	}
      if (gotht+gotmht>1.5)
	{
	  break;
	}
    }

  int requiredTrigThreshold = 0;
  int requiredTrigIndex = -1;
  for(unsigned int t=0; t<trigNameVec.size();t++)
      {
	if(trigThresholdVec[t]>requiredTrigThreshold && trigThresholdVec[t]<ht)
	  {
	    requiredTrigThreshold = trigThresholdVec[t];
	    requiredTrigIndex = t;
	  }
      }

    if( requiredTrigIndex==-1 || trigPassVec[requiredTrigIndex]==false)
      finalPrescale = 0;
    else
      finalPrescale = trigPrescaleVec[requiredTrigIndex];


  resultWeight*=finalPrescale;

  auto_ptr<double> pOut(new double(resultWeight));
  iEvent.put(pOut, "weight");

  auto_ptr<double> htOut(new double(ht));
  iEvent.put(htOut, "ht");

  auto_ptr<double> mhtOut(new double(mht));
  iEvent.put(mhtOut, "mht");
  
}

  void PrescaleWeightProducer::beginJob() {
  }

  void PrescaleWeightProducer::endJob() {
  }

  void PrescaleWeightProducer::beginRun(edm::Run& iRun, edm::EventSetup const& iSetup) {

    cout << "beginning run" << endl;
  }

  void PrescaleWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  }

  DEFINE_FWK_MODULE( PrescaleWeightProducer);
