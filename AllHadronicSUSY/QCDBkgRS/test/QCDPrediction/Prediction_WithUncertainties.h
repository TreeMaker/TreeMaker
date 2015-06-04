#include <TROOT.h>
#include <TF1.h>
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include <TCanvas.h>
#include <TChain.h>
#include <TPad.h>
#include <TLegend.h>
#include <TMath.h>
#include <TArrayF.h>
#include <TLine.h>
#include <TPaveText.h>
#include <TTree.h>

#include <memory>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <iostream>

using namespace std;

class Prediction_WithUncertainties {

public:
   Prediction_WithUncertainties (TChain&, TChain&, TString&);
   ~Prediction_WithUncertainties();

   TH1F* GetSelectionHisto(TString type);
   TH1F* GetPredictionHisto(TString type);
   double GetResultValue(TH1F* histo, double MHTlow, double MHTup);
   double GetResultError(TH1F* histo, double MHTlow, double MHTup);

private:
   // tree with prediction
   TTree* QCDPrediction; 
   UShort_t vtxN;
   UShort_t NJets;
   UShort_t NSmear;
   Float_t weight;
   Float_t DeltaPhi1;
   Float_t DeltaPhi2;
   Float_t DeltaPhi3;
 
   // tree with selection
   TTree* RA2PreSelection; 
   Int_t EvtNum_RA2;
   UShort_t vtxN_RA2;
   UShort_t NJets_RA2;
   Float_t weight_RA2;
   Float_t DeltaPhi1_RA2;
   Float_t DeltaPhi2_RA2;
   Float_t DeltaPhi3_RA2;

   // store deltaPhi cut
   vector<bool> MinDeltaPhiCut;

   // cut variables for search bins
   double HTlow;
   double HTmedium;
   double HThigh;
   double HTveryhigh;
   double HTextremehigh;
   double MHTlow;
   double MHTmedium;
   double MHThigh;
   double MHTveryhigh;
   double MHTextremehigh;

   //----------------------------------------------------------//
   // raw prediction histograms preselection 
   TH2F* HT_presel_pred_raw;
   TH2F* MHT_presel_pred_raw;
   TH2F* NJets_presel_pred_raw;
   TH2F* Jet1Pt_presel_pred_raw;
   TH2F* Jet2Pt_presel_pred_raw;
   TH2F* Jet3Pt_presel_pred_raw;
   TH2F* Jet1Eta_presel_pred_raw;
   TH2F* Jet2Eta_presel_pred_raw;
   TH2F* Jet3Eta_presel_pred_raw;
   TH2F* DeltaPhi1_presel_pred_raw;
   TH2F* DeltaPhi2_presel_pred_raw;
   TH2F* DeltaPhi3_presel_pred_raw;

   // raw prediction histograms preselection - high HT
   TH2F* HT_presel_HThigh_pred_raw;
   TH2F* MHT_presel_HThigh_pred_raw;
   TH2F* NJets_presel_HThigh_pred_raw;
   TH2F* Jet1Pt_presel_HThigh_pred_raw;
   TH2F* Jet2Pt_presel_HThigh_pred_raw;
   TH2F* Jet3Pt_presel_HThigh_pred_raw;
   TH2F* Jet1Eta_presel_HThigh_pred_raw;
   TH2F* Jet2Eta_presel_HThigh_pred_raw;
   TH2F* Jet3Eta_presel_HThigh_pred_raw;
   TH2F* DeltaPhi1_presel_HThigh_pred_raw;
   TH2F* DeltaPhi2_presel_HThigh_pred_raw;
   TH2F* DeltaPhi3_presel_HThigh_pred_raw;

   // raw prediction histograms 2 jets, HT 500-750 
   TH2F* MHT_JetBin1_HTlow_pred_raw;
   // raw prediction histograms 2 jets, HT 750-1000
   TH2F* MHT_JetBin1_HTmedium_pred_raw;
   // raw prediction histograms 2 jets, HT 1000-1250
   TH2F* MHT_JetBin1_HThigh_pred_raw;
   // raw prediction histograms 2 jets, HT 1250-1500
   TH2F* MHT_JetBin1_HTveryhigh_pred_raw;
   // raw prediction histograms 2 jets, HT >=1500
   TH2F* MHT_JetBin1_HTextremehigh_pred_raw;

   // raw prediction histograms 3-5 jets, HT 500-750 
   TH2F* MHT_JetBin2_HTlow_pred_raw;
   // raw prediction histograms 3-5 jets, HT 750-1000
   TH2F* MHT_JetBin2_HTmedium_pred_raw;
   // raw prediction histograms 3-5 jets, HT 1000-1250
   TH2F* MHT_JetBin2_HThigh_pred_raw;
   // raw prediction histograms 3-5 jets, HT 1250-1500
   TH2F* MHT_JetBin2_HTveryhigh_pred_raw;
   // raw prediction histograms 3-5 jets, HT >=1500
   TH2F* MHT_JetBin2_HTextremehigh_pred_raw;

   // raw prediction histograms 6-7 jets, HT 500-750 
   TH2F* MHT_JetBin3_HTlow_pred_raw;
   // raw prediction histograms 6-7 jets, HT 750-1000
   TH2F* MHT_JetBin3_HTmedium_pred_raw;
   // raw prediction histograms 6-7 jets, HT 1000-1250
   TH2F* MHT_JetBin3_HThigh_pred_raw;
   // raw prediction histograms 6-7 jets, HT 1250-1500
   TH2F* MHT_JetBin3_HTveryhigh_pred_raw;
   // raw prediction histograms 6-7 jets, HT >=1500
   TH2F* MHT_JetBin3_HTextremehigh_pred_raw;

   // raw prediction histograms >=8 jets, HT 500-750 
   TH2F* MHT_JetBin4_HTlow_pred_raw;
   // raw prediction histograms >=8 jets, HT 750-1000
   TH2F* MHT_JetBin4_HTmedium_pred_raw;
   // raw prediction histograms >=8 jets, HT 1000-1250
   TH2F* MHT_JetBin4_HThigh_pred_raw;
   // raw prediction histograms >=8 jets, HT 1250-1500
   TH2F* MHT_JetBin4_HTveryhigh_pred_raw;
   // raw prediction histograms >=8 jets, HT >=1500
   TH2F* MHT_JetBin4_HTextremehigh_pred_raw;

   //----------------------------------------------------------//

   //----------------------------------------------------------//
   // prediction histograms preselection
   TH1F* HT_presel_pred;
   TH1F* MHT_presel_pred;
   TH1F* NJets_presel_pred;
   TH1F* Jet1Pt_presel_pred;
   TH1F* Jet2Pt_presel_pred;
   TH1F* Jet3Pt_presel_pred;
   TH1F* Jet1Eta_presel_pred;
   TH1F* Jet2Eta_presel_pred;
   TH1F* Jet3Eta_presel_pred;
   TH1F* DeltaPhi1_presel_pred;
   TH1F* DeltaPhi2_presel_pred;
   TH1F* DeltaPhi3_presel_pred;

   // prediction histograms preselection - high HT
   TH1F* HT_presel_HThigh_pred;
   TH1F* MHT_presel_HThigh_pred;
   TH1F* NJets_presel_HThigh_pred;
   TH1F* Jet1Pt_presel_HThigh_pred;
   TH1F* Jet2Pt_presel_HThigh_pred;
   TH1F* Jet3Pt_presel_HThigh_pred;
   TH1F* Jet1Eta_presel_HThigh_pred;
   TH1F* Jet2Eta_presel_HThigh_pred;
   TH1F* Jet3Eta_presel_HThigh_pred;
   TH1F* DeltaPhi1_presel_HThigh_pred;
   TH1F* DeltaPhi2_presel_HThigh_pred;
   TH1F* DeltaPhi3_presel_HThigh_pred;

   // prediction histograms 2 jets, HT 500-750 
   TH1F* MHT_JetBin1_HTlow_pred;
   // prediction histograms 2 jets, HT 750-1000
   TH1F* MHT_JetBin1_HTmedium_pred;
   // prediction histograms 2 jets, HT 1000-1250
   TH1F* MHT_JetBin1_HThigh_pred;
   // prediction histograms 2 jets, HT 1250-1500
   TH1F* MHT_JetBin1_HTveryhigh_pred;
   // prediction histograms 2 jets, HT >=1500
   TH1F* MHT_JetBin1_HTextremehigh_pred;

   // prediction histograms 3-5 jets, HT 500-750 
   TH1F* MHT_JetBin2_HTlow_pred;
   // prediction histograms 3-5 jets, HT 750-1000
   TH1F* MHT_JetBin2_HTmedium_pred;
   // prediction histograms 3-5 jets, HT 1000-1250
   TH1F* MHT_JetBin2_HThigh_pred;
   // prediction histograms 3-5 jets, HT 1250-1500
   TH1F* MHT_JetBin2_HTveryhigh_pred;
   // prediction histograms 3-5 jets, HT >=1500
   TH1F* MHT_JetBin2_HTextremehigh_pred;

   // prediction histograms 6-7 jets, HT 500-750 
   TH1F* MHT_JetBin3_HTlow_pred;
   // prediction histograms 6-7 jets, HT 750-1000
   TH1F* MHT_JetBin3_HTmedium_pred;
   // prediction histograms 6-7 jets, HT 1000-1250
   TH1F* MHT_JetBin3_HThigh_pred;
   // prediction histograms 6-7 jets, HT 1250-1500
   TH1F* MHT_JetBin3_HTveryhigh_pred;
   // prediction histograms 6-7 jets, HT >=1500
   TH1F* MHT_JetBin3_HTextremehigh_pred;

   // prediction histograms >=8 jets, HT 500-750 
   TH1F* MHT_JetBin4_HTlow_pred;
   // prediction histograms >=8 jets, HT 750-1000
   TH1F* MHT_JetBin4_HTmedium_pred;
   // prediction histograms >=8 jets, HT 1000-1250
   TH1F* MHT_JetBin4_HThigh_pred;
   // prediction histograms >=8 jets, HT 1250-1500
   TH1F* MHT_JetBin4_HTveryhigh_pred;
   // prediction histograms >=8 jets, HT >=1500
   TH1F* MHT_JetBin4_HTextremehigh_pred;

   //----------------------------------------------------------//

   //----------------------------------------------------------//
   // selection histograms preselection
   TH1F* HT_presel_sel;
   TH1F* MHT_presel_sel;
   TH1F* NJets_presel_sel;
   TH1F* Jet1Pt_presel_sel;
   TH1F* Jet2Pt_presel_sel;
   TH1F* Jet3Pt_presel_sel;
   TH1F* Jet1Eta_presel_sel;
   TH1F* Jet2Eta_presel_sel;
   TH1F* Jet3Eta_presel_sel;
   TH1F* DeltaPhi1_presel_sel;
   TH1F* DeltaPhi2_presel_sel;
   TH1F* DeltaPhi3_presel_sel;

   // selection histograms preselection - HT high
   TH1F* HT_presel_HThigh_sel;
   TH1F* MHT_presel_HThigh_sel;
   TH1F* NJets_presel_HThigh_sel;
   TH1F* Jet1Pt_presel_HThigh_sel;
   TH1F* Jet2Pt_presel_HThigh_sel;
   TH1F* Jet3Pt_presel_HThigh_sel;
   TH1F* Jet1Eta_presel_HThigh_sel;
   TH1F* Jet2Eta_presel_HThigh_sel;
   TH1F* Jet3Eta_presel_HThigh_sel;
   TH1F* DeltaPhi1_presel_HThigh_sel;
   TH1F* DeltaPhi2_presel_HThigh_sel;
   TH1F* DeltaPhi3_presel_HThigh_sel;

   // selection histograms 2 jets, HT 500-750 
   TH1F* MHT_JetBin1_HTlow_sel;
   // selection histograms 2 jets, HT 750-1000
   TH1F* MHT_JetBin1_HTmedium_sel;
   // selection histograms 2 jets, HT 1000-1250
   TH1F* MHT_JetBin1_HThigh_sel;
   // selection histograms 2 jets, HT 1250-1500
   TH1F* MHT_JetBin1_HTveryhigh_sel;
   // selection histograms 2 jets, HT >=1500
   TH1F* MHT_JetBin1_HTextremehigh_sel;

   // selection histograms 3-5 jets, HT 500-750 
   TH1F* MHT_JetBin2_HTlow_sel;
   // selection histograms 3-5 jets, HT 750-1000
   TH1F* MHT_JetBin2_HTmedium_sel;
   // selection histograms 3-5 jets, HT 1000-1250
   TH1F* MHT_JetBin2_HThigh_sel;
   // selection histograms 3-5 jets, HT 1250-1500
   TH1F* MHT_JetBin2_HTveryhigh_sel;
   // selection histograms 3-5 jets, HT >=1500
   TH1F* MHT_JetBin2_HTextremehigh_sel;

   // selection histograms 6-7 jets, HT 500-750 
   TH1F* MHT_JetBin3_HTlow_sel;
   // selection histograms 6-7 jets, HT 750-1000
   TH1F* MHT_JetBin3_HTmedium_sel;
   // selection histograms 6-7 jets, HT 1000-1250
   TH1F* MHT_JetBin3_HThigh_sel;
   // selection histograms 6-7 jets, HT 1250-1500
   TH1F* MHT_JetBin3_HTveryhigh_sel;
   // selection histograms 6-7 jets, HT >=1500
   TH1F* MHT_JetBin3_HTextremehigh_sel;

   // selection histograms >=8 jets, HT 500-750 
   TH1F* MHT_JetBin4_HTlow_sel;
   // selection histograms >=8 jets, HT 750-1000
   TH1F* MHT_JetBin4_HTmedium_sel;
   // selection histograms >=8 jets, HT 1000-1250
   TH1F* MHT_JetBin4_HThigh_sel;
   // selection histograms >=8 jets, HT 1250-1500
   TH1F* MHT_JetBin4_HTveryhigh_sel;
   // selection histograms >=8 jets, HT >=1500
   TH1F* MHT_JetBin4_HTextremehigh_sel;

   //----------------------------------------------------------//

   // dummy histo
   TH1F* dummy;

   bool DeltaPhiCut_selection();
   bool DeltaPhiCut_prediction();
   void DoRebinning(TH2F* prediction_raw, TH1F* selection_raw, int Nbins);
   TH1F* CalcPrediction(TH2F* prediction_raw);
 
};


