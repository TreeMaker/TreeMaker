#ifndef SMEAR_FUNCTION_H
#define SMEAR_FUNCTION_H

#include "TF1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include "TTree.h"
#include "TKey.h"
#include "TFile.h"
#include "TMath.h"
#include "TArray.h"
#include "TPostScript.h"
#include "TCanvas.h"
#include "TStyle.h"

#include <memory>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <iostream>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
//#include "Utilities/Parang/interface/Paramatrix.h"

using namespace std;

//typedef Paramatrix<PopulationF> ParamatrixF;
//typedef Paramatrix<PopulationD> ParamatrixD;

class SmearFunction {

public:
   SmearFunction( const edm::ParameterSet& );
   ~SmearFunction();

   TF1* getSigmaPtForRebalancing(int i_jet, int i_eta) const;
   TF1* getSigmaPtScaledForRebalancing(int i_jet, int i_eta) const;
   TH1F* getSmearFunc(int i_flav, int i_jet, int i_eta, int i_Pt) const;
  
private:
   typedef std::vector<std::string>::const_iterator StrIter;

   void FillSigmaHistsForRebalancing();
   void ResizeSmearFunctions();
   void CalculateSmearFunctions();
   double GetAdditionalSmearing(const double&, const double&);
   double GetLowerTailScaling(const double&, const double&);
   double GetUpperTailScaling(const double&, const double&);
   void FoldWithGaussian(const TH1&, TH1&, const double&);
   void StretchHisto(const TH1&, TH1&, const double&);
   int GetIndex(const double&, const std::vector<double>*);
  
   std::vector<double> PtBinEdges_scaling_;
   std::vector<double> EtaBinEdges_scaling_;
   std::vector<double> AdditionalSmearing_;
   std::vector<double> LowerTailScaling_;
   std::vector<double> UpperTailScaling_;
   double AdditionalSmearing_variation_;
   double LowerTailScaling_variation_;
   double UpperTailScaling_variation_;

   std::string inputhist1HF_;
   std::string inputhist2HF_;
   std::string inputhist3pHF_;
   std::string inputhist1NoHF_;
   std::string inputhist2NoHF_;
   std::string inputhist3pNoHF_;
   std::string smearingfile_;
   std::string bprobabilityfile_;
   std::string outputfile_;

   int NRebin_;
   bool absoluteTailScaling_;
   double A0RMS_;
   double A1RMS_;
   double probExtreme_;

   std::string uncertaintyName_;

   std::vector<double> PtBinEdges_;
   std::vector<double> EtaBinEdges_;

   //// vectors of response functions
   std::vector<std::vector<std::vector<std::vector<TH1F*> > > >smearFunc;
   std::vector<std::vector<std::vector<std::vector<TH1F*> > > >smearFunc_Core;
   std::vector<std::vector<std::vector<std::vector<TH1F*> > > >smearFunc_LowerTail;
   std::vector<std::vector<std::vector<std::vector<TH1F*> > > >smearFunc_UpperTail;
   std::vector<std::vector<std::vector<std::vector<TH1F*> > > >smearFunc_scaled;
   std::vector<std::vector<std::vector<TH1F*> > >SigmaPtHist;
   std::vector<std::vector<std::vector<TF1*> > >SigmaPt;
   std::vector<std::vector<std::vector<TH1F*> > >SigmaPtHist_scaled;
   std::vector<std::vector<std::vector<TF1*> > >SigmaPt_scaled;

   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_total;
   std::vector<std::vector<TH1F*> > SigmaPtHist_total;
   std::vector<std::vector<TF1*> > SigmaPt_total;
   std::vector<std::vector<TH1F*> > SigmaPtHist_scaled_total;
   std::vector<std::vector<TF1*> > SigmaPt_scaled_total;
};

#endif
