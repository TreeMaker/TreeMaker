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
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "TreeMaker/Utils/interface/parse.h"

//
// class declaration
//

//helper function to get histogram and disconnect from file
//and optionally normalize
namespace {
    TH1* getHisto(TFile* file, std::string name, bool norm=false){
        TH1* hist = (TH1*)file->Get(name.c_str());
        if(hist) {
          hist->SetDirectory(nullptr);
          if(norm) hist->Scale(1.0/hist->Integral(1,hist->GetNbinsX()));
        }
        return hist;
    }
}

class WeightProducer: public edm::global::EDProducer<> {
public:
  explicit WeightProducer(const edm::ParameterSet&);
  ~WeightProducer() override;
  
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  
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
  bool _remakePU, _applyPUWeights;
  weight_method _weightingMethod;
  std::unordered_map<double,double> _FastSimXsec;
  
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
   _SusyMotherTag(iConfig.getParameter<edm::InputTag> ("modelIdentifier")),
   pu_central(nullptr), pu_up(nullptr), pu_down(nullptr),
   _remakePU(iConfig.getParameter<bool>("RemakePU")),
   _weightingMethod(other)
{
   // Option 1: weight constant, as defined in cfg file
   if (_startWeight >= 0) {
      _weightingMethod = StartWeight;
      edm::LogInfo("TreeMaker") << "WeightProducer: Using constant event weight of " << _startWeight;
   }
   // Option 2: weight from event
   else if (_weightingMethodName == "FromEvent") {
      _weightingMethod = FromEvent;
      edm::LogInfo("TreeMaker") << "WeightProducer: Using weight from event";
      _weightTok = consumes<double>(_weightName);
   }
   // Option 3: compute new weight
   else if (_weightingMethodName == "Constant") {
      _weightingMethod = Constant;
      _weightFactor = _lumi * _xs / _NumberEvents;
      edm::LogInfo("TreeMaker")
        << "WeightProducer: Using constant event weight of " << _weightFactor << "\n"
        << "  Target luminosity (1/pb) : " << _lumi << "\n"
        << "        Cross section (pb) : " << _xs << "\n"
        << "          Number of events : " << _NumberEvents;
      _genEvtTok = consumes<GenEventInfoProduct>(_genEvtTag);
   }
   // Option 4: assign cross section for FastSim
   else if (_weightingMethodName == "FastSim") {
      _weightingMethod = FastSim;
      edm::LogInfo("TreeMaker")
        << "WeightProducer: Finding cross sections for FastSim" << "\n"
        << "  Target luminosity (1/pb) : " << _lumi << "\n"
        << "          Number of events : " << _NumberEvents;
      _SusyMotherTok = consumes<double>(_SusyMotherTag);
      //setup xsec map
      std::string inputXsecName = iConfig.getParameter<std::string> ("XsecFile");
	  bool foundXsec = true;
      if(!inputXsecName.empty()){
         edm::FileInPath fileXsec(inputXsecName);
         std::ifstream infile(fileXsec.fullPath().c_str());
         if(infile.is_open()){
            std::string line;
            while(getline(infile,line)){
               std::vector<std::string> items;
               parse::process(line,'\t',items);
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
         edm::LogWarning("TreeMaker") << "WARNING: WeightProducer: Could not open FastSim xsec file: " << inputXsecName;
         _weightingMethod = other;
      }
   }
   // No option specified
   else {
      edm::LogWarning("TreeMaker") << "WARNING: WeightProducer: No weighting option specified. Using event weights of 1";
   }

   // Optionally, compute multiplicative weight factors for PU reweighting
   // The weights are a function of the generated PU interactions and the
   // expected data distribution is given as a histogram from a ROOT file.
   // See https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupReweighting
   std::string fileNamePU = iConfig.getParameter<std::string> ("FileNamePUDataDistribution");
   std::string fileNamePUMC = iConfig.getParameter<std::string> ("FileNamePUMCDistribution");
   if (!fileNamePU.empty()) {
      _applyPUWeights = true;
      fileNamePU = edm::FileInPath(fileNamePU).fullPath();
      //don't use FileInPath for xrootd
      if(!fileNamePUMC.empty() and fileNamePUMC.compare(0,5,"root:")!=0) fileNamePUMC = edm::FileInPath(fileNamePUMC).fullPath();

      edm::LogInfo("TreeMaker") << "WeightProducer: Applying multiplicative PU weights" << "\n"
        << "  Reading PU scenario from '" << fileNamePU << "'"
        << ((!fileNamePUMC.empty() and _remakePU) ? "and '"+fileNamePUMC+"'" : "");

      TFile* dfile = TFile::Open(fileNamePU.c_str(), "READ");

      //recalculate from provided MC and data histos
      if(!fileNamePUMC.empty() and _remakePU){
        TFile* mfile = TFile::Open(fileNamePUMC.c_str(), "READ");
        TH1* pu_mc_in = getHisto(mfile,"NeffFinder/TrueNumInteractions");

        pu_central = getHisto(dfile,"data_pu_central",true);
        pu_up = getHisto(dfile,"data_pu_up",true);
        pu_down = getHisto(dfile,"data_pu_down",true);

        TH1* pu_mc = new TH1F("hMC25ns","",pu_central->GetNbinsX(),0,pu_central->GetNbinsX());
        for(int b = 0; b < pu_central->GetNbinsX(); ++b){
          pu_mc->SetBinContent(b+1, b < pu_mc_in->GetNbinsX() ? pu_mc_in->GetBinContent(b+1) : 0);
          pu_mc->SetBinError(b+1, 0);
        }
        pu_mc->Scale(1.0/pu_mc->Integral(1,pu_mc->GetNbinsX()));

        pu_central->Divide(pu_mc);
        pu_up->Divide(pu_mc);
        pu_down->Divide(pu_mc);

        mfile->Close();
      }
      //use already calculated ones
      else {
        pu_central = getHisto(dfile,"pu_weights_central");
        pu_up = getHisto(dfile,"pu_weights_up");
        pu_down = getHisto(dfile,"pu_weights_down");
      }

      if(!pu_central || !pu_up || !pu_down) {
         edm::LogWarning("TreeMaker") << "ERROR in WeightProducer: Pileup histograms missing from file '" << fileNamePU;
         _applyPUWeights = false;
      }
      dfile->Close();
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
void WeightProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {

   double resultWeight = 1.;
   double xsEvt = _xs;

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
      xsEvt = 0;
      edm::Handle<double> SusyMotherHandle;
      iEvent.getByToken(_SusyMotherTok, SusyMotherHandle);
      if (SusyMotherHandle.isValid()){
         auto itr = _FastSimXsec.find(*SusyMotherHandle);
         if(itr!=_FastSimXsec.end()) xsEvt = itr->second;
      }
      resultWeight = xsEvt * _NumberEvents * _lumi;
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
       for(const auto& PVI : *puInfo) {
           //look only at primary BX (in-time)
           if(PVI.getBunchCrossing()==0){
               _NumInt = PVI.getPU_NumInteractions();
               _TrueNumInt = PVI.getTrueNumInteractions();
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
   
   auto pOutX = std::make_unique<double>(xsEvt);
   iEvent.put(std::move(pOutX), "xsec");

   auto pOutN = std::make_unique<double>(_NumberEvents);
   iEvent.put(std::move(pOutN), "nevents");
}

// Get weight factor dependent on true number of
// added PU interactions
// --------------------------------------------------
double WeightProducer::getPUWeight(double trueint, TH1* pu) const {
  double w = 1.;
  
  if(!pu) return w;

  if (trueint < pu->GetBinLowEdge(pu->GetNbinsX()+1)) {
        w = pu->GetBinContent(pu->GetXaxis()->FindBin(trueint));
  } else {
    edm::LogWarning("TreeMaker") << "WARNING in WeightProducer::getPUWeight: Number of interactions = " << trueint << " out of histogram binning.";
    w = pu->GetBinContent(pu->GetNbinsX());
  }

   return w;
}

//define this as a plug-in
DEFINE_FWK_MODULE( WeightProducer);
