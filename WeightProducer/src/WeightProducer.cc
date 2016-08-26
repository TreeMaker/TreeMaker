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
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>

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
  
  enum weight_method { StartWeight = 0, FromEvent = 1, Constant = 2, FastSim = 3, other = 4 };
  
  const std::string _weightingMethodName;
  const double _startWeight;
  double _xs;
  const double _NumberEvents;
  const double _lumi;
  edm::InputTag _weightName, _genEvtTag, _puInfoTag, _SusyMotherTag;
  edm::EDGetTokenT<double> _weightTok, _SusyMotherTok;
  edm::EDGetTokenT<GenEventInfoProduct> _genEvtTok;
  edm::EDGetTokenT<std::vector<PileupSummaryInfo>> _puInfoTok;
  TH1 *pu_central, *pu_up, *pu_down;
  double _weightFactor;
  bool _applyPUWeights;
  weight_method _weightingMethod;
  std::unordered_map<double,double> _FastSimXsec;
  
  void process(std::string line, char delim, std::vector<std::string>& fields);
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
   _SusyMotherTag(edm::InputTag("SusyScan:SusyMotherMass")),
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
   
   // Option 4: assign cross section for FastSim
   else if (_weightingMethodName == "FastSim") {
      _weightingMethod = FastSim;
      std::cout << "WeightProducer: Finding cross sections for FastSim" << std::endl;
      std::cout << "  Target luminosity (1/pb) : " << _lumi << std::endl;
      std::cout << "          Number of events : " << _NumberEvents << std::endl;
      _SusyMotherTok = consumes<double>(_SusyMotherTag);
     
      //setup xsec map
      std::string inputXsecName = iConfig.getParameter<std::string> ("XsecFile");
	  bool foundXsec = true;
      if(inputXsecName.size()>0){
         edm::FileInPath fileXsec(inputXsecName);
         std::ifstream infile(fileXsec.fullPath().c_str());
         if(infile.is_open()){
            std::string line;
            while(getline(infile,line)){
               std::vector<std::string> items;
               process(line,'\t',items);
               //convert input to proper types
               if(items.size()==2){
                  double mass_tmp;
                  std::stringstream s0(items[0]);
                  s0 >> mass_tmp;
                  
                  double xsec_tmp;
                  std::stringstream s1(items[1]);
                  s1 >> xsec_tmp;
                  
                  //insert into map
                  _FastSimXsec.emplace(mass_tmp,xsec_tmp);
               }
            }
         }
         else foundXsec = false;
      }
      else foundXsec = false;
      
      if(!foundXsec) {
         std::cout << "WARNING: WeightProducer: Could not open FastSim xsec file: " << inputXsecName << std::endl;
         _weightingMethod = other;
      }
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
   
   //Option 4: get cross section from input file
   else if (_weightingMethod == FastSim) {
      _xs = 0;
      edm::Handle<double> SusyMotherHandle;
      iEvent.getByToken(_SusyMotherTok, SusyMotherHandle);
      if (SusyMotherHandle.isValid()){
         auto itr = _FastSimXsec.find(*SusyMotherHandle);
         if(itr!=_FastSimXsec.end()) _xs = itr->second;
      }
      resultWeight = _xs * _NumberEvents * _lumi;
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

        auto puOut1 = std::make_unique<double>(_PUweightFactor);
        iEvent.put(std::move(puOut1), "PUweight");
        
        auto puOut2 = std::make_unique<double>(_PUSysUp);
        iEvent.put(std::move(puOut2), "PUSysUp");
        
        auto puOut3 = std::make_unique<double>(_PUSysDown);
        iEvent.put(std::move(puOut3), "PUSysDown");
        
        auto puOut4 = std::make_unique<int>(_NumInt);
        iEvent.put(std::move(puOut4), "NumInteractions");
        
        auto puOut5 = std::make_unique<double>(_TrueNumInt);
        iEvent.put(std::move(puOut5), "TrueNumInteractions");
   }

   //---------------------------------------------------------------------------

   // put weight into the Event
   auto pOut = std::make_unique<double>(resultWeight);
   iEvent.put(std::move(pOut), "weight");
   
   auto pOutX = std::make_unique<double>(_xs);
   iEvent.put(std::move(pOutX), "xsec");

   auto pOutN = std::make_unique<double>(_NumberEvents);
   iEvent.put(std::move(pOutN), "nevents");
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
  
  if(!pu) return w;

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

//generalization for processing a line
void WeightProducer::process(std::string line, char delim, std::vector<std::string>& fields){
	std::stringstream ss(line);
	std::string field;
	while(getline(ss,field,delim)){
		fields.push_back(field);
	}
}

//define this as a plug-in
DEFINE_FWK_MODULE( WeightProducer);
