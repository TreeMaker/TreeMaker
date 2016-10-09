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
//         Created:  Tue Sept 10 17:58:04 CET 2015
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

//
// class decleration
//

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
  const double _startWeight;
  const double _LumiScale;
  const double _PrescaleCut;
  const bool _PFHTWeights;
  edm::InputTag _weightName;
  string _processName;

  edm::EDGetTokenT<edm::TriggerResults> _triggerBits;//Van
  edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> _triggerObjects;//Van
  edm::EDGetTokenT<pat::PackedTriggerPrescales> _triggerPrescales;//Van
};

PrescaleWeightProducer::PrescaleWeightProducer(const edm::ParameterSet& iConfig) :
  _startWeight(iConfig.getParameter<double> ("weight")), _LumiScale(iConfig.getParameter<double> ("LumiScale")), _PrescaleCut(iConfig.getParameter<double> ("PrescaleCut")), _PFHTWeights(iConfig.getParameter<bool> ("PFHTWeights")), _weightName(iConfig.getParameter<edm::InputTag> ("weightName")), _processName(iConfig.getParameter<string> ("HLTProcess")), _triggerBits(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits"))), _triggerObjects(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("objects"))), _triggerPrescales(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescales")))//last 3Van 
{
  if (_startWeight >= 0) {
    cout << "PrescaleWeightProducer: Using constant event weight of " << _startWeight << endl;
  } else {
    cout << "PrescaleWeightProducer: Using weight from event" << endl;
  }
  ///This is to consider the lumi-uncertainty, i.e. to scale the weights up- or down by 1sigma of the lumi-scale
  ///uncertainty. In general the scale is 1.0!
  if (_LumiScale != 1.) {
    cout << "PrescaleWeightProducer: Scaling event weights by factor " << _LumiScale << endl;
  }
  //register your products
  produces<double> ("weight");
  produces<double> ("ht");
  produces<double> ("mht");
}

PrescaleWeightProducer::~PrescaleWeightProducer() {
}

// ------------ method called to produce the data  ------------
void PrescaleWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  //set start weight
  double resultWeight = 1.;
  if (_startWeight >= 0) {
    resultWeight = _startWeight;
  } else {
    edm::Handle<double> event_weight;
    iEvent.getByLabel(_weightName, event_weight);
    resultWeight = (event_weight.isValid() ? (*event_weight) : 1.0);
  }
  ///This is to consider the lumi-uncertainty, i.e. to scale the weights up- or down by 1sigma of the lumi-scale
  ///uncertainty. In general the scale is 1.0!
  resultWeight *= _LumiScale;
  edm::Handle<edm::TriggerResults> triggerBits;//Vangelis
  iEvent.getByToken(_triggerBits, triggerBits);//Vangelis
  edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;//Vangelis
  iEvent.getByToken(_triggerObjects, triggerObjects);//Vangelis
  edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;//Vangelis
  iEvent.getByToken(_triggerPrescales, triggerPrescales);//Vangelis
  const edm::TriggerNames & trigNames = iEvent.triggerNames(*triggerBits);

  vector<string> trigNameVec;
  vector<bool> trigPassVec;
  vector<int> trigThresholdVec;
  vector<int> trigPrescaleVec;
  int finalPrescale = 0;
  double ht = 0.0;
  double mht = 0.0;
  //std::cout << "event==================="<< std::endl;
  if( _PFHTWeights ) {
    for (unsigned int i = 0; i < triggerBits->size(); i++) {
      const string trigName = trigNames.triggerName(i);
      size_t found;
      found = trigName.find("HLT_PFHT");
      if (found == string::npos)
	continue;
      found = trigName.find("0_v");
      if (found != 10)
	continue;
      //std::cout << "trigName=" << trigName << std::endl;
      bool pass = triggerBits->accept(i);
      int ps = triggerPrescales->getPrescaleForIndex(i);
      string strthr = trigName.substr(8, 3);
      int thresh = int(atof(strthr.c_str()));
      //std::cout << "trigname=" << trigName << "\tps=" << ps << "\tstrthr=" << strthr << "\tthresh"<<thresh<<std::endl;
      //cout << "we got strthr="<<strthr<<endl;
      trigNameVec.push_back(trigName);
      trigPassVec.push_back(pass);
      trigThresholdVec.push_back(thresh);
      trigPrescaleVec.push_back(ps);
    }   

    int gotht = 0; int gotmht = 0;
    for (pat::TriggerObjectStandAlone obj : *triggerObjects) 
      {
	obj.unpackPathNames(trigNames);
	//if ( (obj.collection() == "hltPFHT4JetPt50::HLT") && (obj.filterIds()[0] == 89) )//do we need collection?
	//std::cout << "obj.collection()=" << obj.collection() << std::endl;
	//std::cout << " loose cannon filterID="<<obj.filterIds()[0]<< " and obj.pt(), obj.eta()=" << obj.pt() << ", " << obj.eta() << ", " << obj.phi() << std::endl;
	//if (!(obj.collection() == "hltPFHT4JetPt50::HLT")) continue;    //hltPFHT::HLT 
	if (!(obj.collection() == "hltPFHT::HLT")) continue;
	if ( abs(obj.filterIds()[0]) == 89) 
	  {
	    ht = obj.pt();
	    //std::cout << " ht filterID="<<obj.filterIds()[0]<< " and obj.pt(), obj.eta()=" << obj.pt() << ", " << obj.eta() << ", " << obj.phi() << std::endl;
	    gotht = 1;
	    continue;
	  }
	if ( abs((obj.filterIds()[0]) == 90) )
	  {
	    mht = obj.pt(); 
	    //std::cout << "obj.collection()=" << obj.collection() << std::endl;
	    //std::cout << " mht filterID="<<obj.filterIds()[0]<< " and obj.pt(), obj.eta()=" << obj.pt() << ", " << obj.eta() << ", " << obj.phi() << std::endl;
	    gotmht = 1;
	    continue;
	    //std::cout<< "online_mht="<<mht<<std::endl;
	  }
	if (gotht+gotmht>1.5)
	  {
	    //std::cout << "weird condition"<< mht << std::cout << endl;
	  break;
	  }
	//if (obj.collection() == "hltPFHT4JetPt50::HLT")
	//  break;
      }

    //std::cout << "ht, mht = " << ht << "\t"<< mht<< std::endl;
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


    // cout << trigPassVec.size()<<"requiredTrigIndex=" << requiredTrigIndex<<endl;
    // cout << "requiredTrigThreshold=" << requiredTrigThreshold<<endl;
    // cout << "trigPrescaleVec[requiredTrigIndex]" << trigPrescaleVec[requiredTrigIndex] <<std::endl;
    if( requiredTrigIndex==-1 || trigPassVec[requiredTrigIndex]==false)
      finalPrescale = 0;
    else
      finalPrescale = trigPrescaleVec[requiredTrigIndex];
    //for(unsigned int i = 0; i<trigPassVec.size(); i++)
    //  std::cout << i << " " << trigNameVec[i] << " " << trigPassVec[i] << std::endl;
    //std::cout << "final ps = " << finalPrescale << std::endl;
  }

  //std:: cout << "prescale=" << finalPrescale << std::endl;
  resultWeight*=finalPrescale;
  // put weight into the Event
  auto_ptr<double> pOut(new double(resultWeight));
  iEvent.put(pOut, "weight");

  auto_ptr<double> htOut(new double(ht));
  iEvent.put(htOut, "ht");

  auto_ptr<double> mhtOut(new double(mht));
  iEvent.put(mhtOut, "mht");
  
}

// ------------ method called once each job just before starting event loop  ------------
  void PrescaleWeightProducer::beginJob() {
  }

  // ------------ method called once each job just after ending the event loop  ------------
  void PrescaleWeightProducer::endJob() {
  }

  // ------------ method called at beginning for each run  ---------------------------------
  void PrescaleWeightProducer::beginRun(edm::Run& iRun, edm::EventSetup const& iSetup) {

    cout << "beginning run" << endl;
  }

  void PrescaleWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  }

  //define this as a plug-in
  DEFINE_FWK_MODULE( PrescaleWeightProducer);
