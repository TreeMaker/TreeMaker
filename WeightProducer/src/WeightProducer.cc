// -*- C++ -*-
//
// Package:    WeightProducer
// Class:      WeightProducer
//
/**\class WeightProducer WeightProducer.cc RA2/WeightProducer/src/WeightProducer.cc

 Description: <one line class summary>

 Implementation:
 <Notes on implementation>
 */
//
//         Created:  Tue Nov 10 17:58:04 CET 2009
// $Id: WeightProducer.cc,v 1.2 2012/10/04 18:17:16 mschrode Exp $
//
//


// system include files
#include <cmath>
#include <memory>
#include <string>
#include <iostream>
#include <vector>

#include "TFile.h"
#include "TH1.h"

// user include files
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"


//
// class declaration
//

class WeightProducer: public edm::EDProducer {
public:
  explicit WeightProducer(const edm::ParameterSet&);
  ~WeightProducer();
  
private:
  //  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob();
  
  enum weight_method { StartWeight = 0, FromEvent = 1, Constant = 2, other = 3 };
  
  const std::string _weightingMethodName;
  const double _startWeight;
  const double _xs;
  const double _NumberEvents;
  const double _lumi;
  edm::InputTag _weightName, _genEvtTag, _puInfoTag;
  edm::EDGetTokenT<double> _weightTok;
  edm::EDGetTokenT<GenEventInfoProduct> _genEvtTok;
  edm::EDGetTokenT<std::vector<PileupSummaryInfo>> _puInfoTok;
  TH1 *pu_central, *pu_up, *pu_down;
  double _weightFactor;
  bool _applyPUWeights;
  weight_method _weightingMethod;
  
  double getPUWeight(double trueint, TH1* pu) const;
};

WeightProducer::WeightProducer(const edm::ParameterSet& iConfig) :
   _weightingMethodName(iConfig.getParameter<std::string> ("Method")),
   _startWeight(iConfig.getParameter<double> ("weight")),
   _xs(iConfig.getParameter<double> ("XS")),
   _NumberEvents(iConfig.getParameter<double> ("NumberEvts")),
   _lumi(iConfig.getParameter<double> ("Lumi")),
   _weightName(iConfig.getParameter<edm::InputTag> ("weightName")),
   _genEvtTag(edm::InputTag("generator")),
   _puInfoTag(edm::InputTag("slimmedAddPileupInfo")),
   pu_central(0), pu_up(0), pu_down(0), _weightingMethod(other)
{

   // Option 1: weight constant, as defined in cfg file
   if (_startWeight >= 0) {
      _weightingMethod = StartWeight;
      std::cout << "WeightProducer: Using constant event weight of " << _startWeight << std::endl;
   }

   // Option 2: weight from event
   else if (_weightingMethodName == "FromEvent") {
      _weightingMethod = FromEvent;
      std::cout << "WeightProducer: Using weight from event" << std::endl;
      _weightTok = consumes<double>(_weightName);
   }

   // Option 3: compute new weight
   else if (_weightingMethodName == "Constant") {
      _weightingMethod = Constant;
      _weightFactor = _lumi * _xs / _NumberEvents;
      std::cout << "WeightProducer: Using constant event weight of " << _weightFactor << std::endl;
      std::cout << "  Target luminosity (1/pb) : " << _lumi << std::endl;
      std::cout << "        Cross section (pb) : " << _xs << std::endl;
      std::cout << "          Number of events : " << _NumberEvents << std::endl;
      _genEvtTok = consumes<GenEventInfoProduct>(_genEvtTag);
   }

   // No option specified
   else {
      std::cerr << "WARNING: WeightProducer: No weighting option specified. Using event weights of 1" << std::endl;
   }

   // Optionally, compute multiplicative weight factors for PU reweighting
   // The weights are a function of the generated PU interactions and the
   // expected data distribution is given as a histogram from a ROOT file.
   // See https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupReweighting
   std::string fileNamePU = iConfig.getParameter<std::string> ("FileNamePUDataDistribution");
   if (fileNamePU.length() != 0 && fileNamePU != "NONE") {
      _applyPUWeights = true;
      edm::FileInPath filePUDataDistr(fileNamePU);

      std::cout << "WeightProducer: Applying multiplicative PU weights" << std::endl;
      std::cout << "  Reading PU scenario from '" << filePUDataDistr.fullPath() << "'" << std::endl;
      TFile* file = TFile::Open(filePUDataDistr.fullPath().c_str(), "READ");
      pu_central = (TH1*)file->Get("pu_weights_central");
      if(pu_central) pu_central->SetDirectory(0);
      pu_up = (TH1*)file->Get("pu_weights_up");
      if(pu_up) pu_up->SetDirectory(0);
      pu_down = (TH1*)file->Get("pu_weights_down");
      if(pu_down) pu_down->SetDirectory(0);

      if(!pu_central || !pu_up || !pu_down) {
         std::cerr << "ERROR in WeightProducer: Pileup histograms missing from file '"
               << filePUDataDistr.fullPath() << std::endl;
         _applyPUWeights = false;
      }
      file->Close();
   } else {
      _applyPUWeights = false;
   }
   
   _puInfoTok = consumes<std::vector<PileupSummaryInfo>>(_puInfoTag);

   //register your products
   produces<double> ("weight");
   produces<double> ("xsec");
   produces<double> ("nevents");
   produces<int>    ("NumInteractions");
   produces<double> ("TrueNumInteractions");
   produces<double> ("PUweight");
   produces<double> ("PUSysUp");
   produces<double> ("PUSysDown");
}

WeightProducer::~WeightProducer() {
}

// ------------ method called to produce the data  ------------
void WeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

   double resultWeight = 1.;

   //Option 1: constant start weight from config file
   if (_weightingMethod == StartWeight) {
      resultWeight = _startWeight;
   }

   //Option 2: existing weight variable in the event named as in _weightName
   else if (_weightingMethod == FromEvent) {
      edm::Handle<double> event_weight;
      iEvent.getByToken(_weightTok, event_weight);
      resultWeight = (event_weight.isValid() ? (*event_weight) : 1.0);
   }

   //Option 3: weighting from lumi, xs, and num evts
   else if (_weightingMethod == Constant) {
      resultWeight = _weightFactor;
      
      //account for negative weights
      edm::Handle<GenEventInfoProduct> genEvtInfoHandle;
      iEvent.getByToken(_genEvtTok, genEvtInfoHandle);
      if (genEvtInfoHandle.isValid()) {
        double genweight_ = genEvtInfoHandle->weight();
        if(genweight_ < 0) resultWeight *= -1;
      }
   }

   // Optionally, include PU weight
   edm::Handle<std::vector<PileupSummaryInfo> > puInfo;
   iEvent.getByToken(_puInfoTok, puInfo);
   if (_applyPUWeights && puInfo.isValid()){
       int _NumInt = 0;
       double _TrueNumInt = 0.;
       double _PUweightFactor = 1.;
       double _PUSysUp = 1.;
       double _PUSysDown = 1.;
       
       //get PU info
       std::vector<PileupSummaryInfo>::const_iterator PVI;
       for(PVI = puInfo->begin(); PVI != puInfo->end(); ++PVI) {
           //look only at primary BX (in-time)
           if(PVI->getBunchCrossing()==0){
               _NumInt = PVI->getPU_NumInteractions();
               _TrueNumInt = PVI->getTrueNumInteractions();
               break;
           }
       }       
       
        _PUweightFactor = getPUWeight(_TrueNumInt,pu_central);
        _PUSysUp = getPUWeight(_TrueNumInt,pu_up);
        _PUSysDown = getPUWeight(_TrueNumInt,pu_down);

        std::auto_ptr<double> puOut1(new double(_PUweightFactor));
        iEvent.put(puOut1, "PUweight");
        
        std::auto_ptr<double> puOut2(new double(_PUSysUp));
        iEvent.put(puOut2, "PUSysUp");
        
        std::auto_ptr<double> puOut3(new double(_PUSysDown));
        iEvent.put(puOut3, "PUSysDown");
        
        std::auto_ptr<int> puOut4(new int(_NumInt));
        iEvent.put(puOut4, "NumInteractions");
        
        std::auto_ptr<double> puOut5(new double(_TrueNumInt));
        iEvent.put(puOut5, "TrueNumInteractions");
   }

   //---------------------------------------------------------------------------

   // put weight into the Event
   std::auto_ptr<double> pOut(new double(resultWeight));
   iEvent.put(pOut, "weight");
   
   std::auto_ptr<double> pOutX(new double(_xs));
   iEvent.put(pOutX, "xsec");

   std::auto_ptr<double> pOutN(new double(_NumberEvents));
   iEvent.put(pOutN, "nevents");
}

// ------------ method called once each job just before starting event loop  ------------
//void
//WeightProducer::beginJob()
//{
//}

// ------------ method called once each job just after ending the event loop  ------------
void WeightProducer::endJob() {
}

// Get weight factor dependent on true number of
// added PU interactions
// --------------------------------------------------
double WeightProducer::getPUWeight(double trueint, TH1* pu) const{
  double w = 1.;

   //std::cout<<"trueint "<<trueint<<std::endl;
  if (trueint < pu->GetBinLowEdge(pu->GetNbinsX()+1)) {
        w = pu->GetBinContent(pu->GetXaxis()->FindBin(trueint));
  } else {
    std::cerr << "WARNING in WeightProducer::getPUWeight: Number of interactions = " << trueint
              << " out of histogram binning." << std::endl;
    w = pu->GetBinContent(pu->GetNbinsX());
  }

   return w;
}

//define this as a plug-in
DEFINE_FWK_MODULE( WeightProducer);
