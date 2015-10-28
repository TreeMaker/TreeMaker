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
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
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
  
  const std::string _weightingMethod;
  const double _startWeight;
  const double _xs;
  const double _NumberEvents;
  const double _lumi;
  TH1 *hweights; 
  edm::InputTag _weightName;
  std::vector<double> _puWeights;
  double _weightFactor;
  double _PUweightFactor;
  double _PUSysUp;
  double _PUSysDown;
  reweight::PoissonMeanShifter PShiftDown_;
  reweight::PoissonMeanShifter PShiftUp_;
  bool _applyPUWeights;
   
  const int _PU; //use this for different PU scenarios
  
  double getPUNVtxWeight(int nvtx) const;
};

WeightProducer::WeightProducer(const edm::ParameterSet& iConfig) :
   _weightingMethod(iConfig.getParameter<std::string> ("Method")),
   _startWeight(iConfig.getParameter<double> ("weight")),
   _xs(iConfig.getParameter<double> ("XS")),
   _NumberEvents(iConfig.getParameter<double> ("NumberEvts")),
   _lumi(iConfig.getParameter<double> ("Lumi")),
   _weightName(iConfig.getParameter<edm::InputTag> ("weightName")),
   _PU(iConfig.getParameter<int> ("PU"))
{

   // Option 1: weight constant, as defined in cfg file
   if (_startWeight >= 0) {
      std::cout << "WeightProducer: Using constant event weight of " << _startWeight << std::endl;
   }

   // Option 2: weight from event
   else if (_weightingMethod == "FromEvent") {
      std::cout << "WeightProducer: Using weight from event" << std::endl;
   }

   // Option 3: compute new weight
   else if (_weightingMethod == "Constant") {
      _weightFactor = _lumi * _xs / _NumberEvents;
      std::cout << "WeightProducer: Using constant event weight of " << _weightFactor << std::endl;
      std::cout << "  Target luminosity (1/pb) : " << _lumi << std::endl;
      std::cout << "        Cross section (pb) : " << _xs << std::endl;
      std::cout << "          Number of events : " << _NumberEvents << std::endl;
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
      TFile file(filePUDataDistr.fullPath().c_str(), "READ");
      TH1 *h = 0;
      //TH1 *hup = 0;
      //TH1 *hdown = 0;
      file.GetObject("ratio", h);
      hweights=(TH1*)h->Clone("hweights");
      //file.GetObject("ratioUp", hup);
      //file.GetObject("ratioDown", hdown);
      PShiftDown_ = reweight::PoissonMeanShifter(-0.5);
      PShiftUp_ = reweight::PoissonMeanShifter(0.5);
      if (h) {
         h->SetDirectory(0);
      } else {
         std::cerr << "ERROR in WeightProducer: Histogram 'pileup' does not exist in file '"
               << filePUDataDistr.fullPath() << "'\n.";
         _applyPUWeights = false;
      }
      file.Close();

      std::cout << "  Computing weights for pile-up scenario " << std::flush;
      if(_PU==0){
        hweights->SetDirectory(0);
        std::cout << "2015" << std::endl;
      } else {
        std::cout << std::endl;
        std::cerr << "ERROR: Undefined pile-up scenario." << std::endl;
      }
       
      delete h;
   } else {
      _applyPUWeights = false;
   }

   //register your products
   produces<double> ("weight");
   produces<double> ("xsec");
   produces<double> ("nevents");
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
   if (_startWeight >= 0) {
      resultWeight = _startWeight;
   }

   //Option 2: existing weight variable in the event named as in _weightName
   else if (_weightingMethod == "FromEvent") {
      edm::Handle<double> event_weight;
      iEvent.getByLabel(_weightName, event_weight);
      resultWeight = (event_weight.isValid() ? (*event_weight) : 1.0);
   }

   //Option 3: weighting from lumi, xs, and num evts
   else if (_weightingMethod == "Constant") {
      resultWeight = _weightFactor;
	  
      //account for negative weights
      edm::Handle<GenEventInfoProduct> genEvtInfoHandle;
      iEvent.getByLabel("generator", genEvtInfoHandle);
      if (genEvtInfoHandle.isValid()) {
        double genweight_ = genEvtInfoHandle->weight();
        if(genweight_ < 0) resultWeight *= -1;
      }
   }

   // Optionally, include PU weight
   edm::Handle<std::vector<PileupSummaryInfo> > puInfo;
   iEvent.getByLabel("addPileupInfo", puInfo);
   edm::Handle<reco::VertexCollection> vertices;
   iEvent.getByLabel("offlineSlimmedPrimaryVertices",vertices);
   //int npu = 0;
   if (_applyPUWeights) {
      if(vertices.isValid()){
	    _PUweightFactor = getPUNVtxWeight(vertices->size());
	    _PUSysUp = _PUweightFactor*PShiftUp_.ShiftWeight((float)vertices->size());
	    _PUSysDown = _PUweightFactor*PShiftDown_.ShiftWeight((float)vertices->size());
//	    std::cout<<"PU weight "<<_PUweightFactor<<std::endl;
	  }

   }

   //---------------------------------------------------------------------------

   // put weight into the Event
   std::auto_ptr<double> pOut(new double(resultWeight));
   iEvent.put(pOut, "weight");
   
   std::auto_ptr<double> pOutX(new double(_xs));
   iEvent.put(pOutX, "xsec");

   std::auto_ptr<double> pOutN(new double(_NumberEvents));
   iEvent.put(pOutN, "nevents");
   
   std::auto_ptr<double> pOut2(new double(_PUweightFactor));
   iEvent.put(pOut2, "PUweight");

   std::auto_ptr<double> pOut3(new double(_PUSysUp));
   iEvent.put(pOut3, "PUSysUp");

   std::auto_ptr<double> pOut4(new double(_PUSysDown));
   iEvent.put(pOut4, "PUSysDown");
}

// ------------ method called once each job just before starting event loop  ------------
//void
//WeightProducer::beginJob()
//{
//}

// ------------ method called once each job just after ending the event loop  ------------
void WeightProducer::endJob() {
}

// Get weight factor dependent on number of
// added PU interactions
// --------------------------------------------------
double WeightProducer::getPUNVtxWeight(int nvtx) const{
  double w = 1.;

   //std::cout<<"nvtx "<<nvtx<<std::endl;
  if (nvtx < hweights->GetBinLowEdge(hweights->GetNbinsX()+1)) {
        w = hweights->GetBinContent(hweights->GetXaxis()->FindBin(nvtx));
  } else {
    std::cerr << "WARNING in WeightProcessor::getPUNVtxWeight: Number of PU vertices = " << nvtx
              << " out of histogram binning." << std::endl;
    w = hweights->GetBinContent(hweights->GetNbinsX());
  }

   return w;
}

//define this as a plug-in
DEFINE_FWK_MODULE( WeightProducer);
