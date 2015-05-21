#include <TROOT.h>
#include <TSystem.h>
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include <TCanvas.h>
#include <TPad.h>
#include <TStyle.h>
#include <TFile.h>
#include <TPostScript.h>
#include <TLegend.h>
#include <TMath.h>
#include <TString.h>
#include <iostream>
#include <vector>
#include <string>

#include "Prediction.h"

using namespace std;

Prediction::Prediction(TChain& QCDPrediction, TChain& RA2PreSelection)
{
   gROOT->ProcessLine("#include <vector>");
   
   // ------------- define all histos needed -------//
   // set histogram attributes
   int Ntries = 100;
   int NbinsMHT = 150;
   int NbinsHT = 100;
   int NbinsJetPt = 250;
   int NbinsJetEta = 100;
   double MHTmin = 0.;
   double MHTmax = 1500.;
   double HTmin = 0.;
   double HTmax = 5000.;
   double JetPtmin = 0.;
   double JetPtmax = 2500.;
   double JetEtamin = -5.;
   double JetEtamax = 5.;
   
   // define prediction histograms
   // preselection
   HT_presel_pred_raw = new TH2F("presel_HT_prediction", "presel_HT_prediction", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_presel_pred_raw = new TH2F("presel_MHT_prediction", "presel_MHT_prediction", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Pt_presel_pred_raw = new TH2F("presel_Jet1_Pt_prediction", "presel_Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_presel_pred_raw = new TH2F("presel_Jet2_Pt_prediction", "presel_Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_presel_pred_raw = new TH2F("presel_Jet3_Pt_prediction", "presel_Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_presel_pred_raw = new TH2F("presel_Jet1_Eta_prediction", "presel_Jet1_Eta", NbinsJetEta,  JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_presel_pred_raw = new TH2F("presel_Jet2_Eta_prediction", "presel_Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_presel_pred_raw = new TH2F("presel_Jet3_Eta_prediction", "presel_Jet3_Eta", NbinsJetEta,  JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_presel_pred_raw = new TH2F("presel_DeltaPhi1_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_presel_pred_raw = new TH2F("presel_DeltaPhi2_prediction", "DeltaPhi2", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_presel_pred_raw = new TH2F("presel_DeltaPhi3_prediction", "DeltaPhi3", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // preselection + delta Phi
   HT_deltaPhi_pred_raw = new TH2F("deltaPhi_HT_prediction", "deltaPhi_HT_prediction", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_deltaPhi_pred_raw = new TH2F("deltaPhi_MHT_prediction", "deltaPhi_MHT_prediction", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Pt_deltaPhi_pred_raw = new TH2F("deltaPhi_Jet1_Pt_prediction", "deltaPhi_Jet1_Pt", NbinsJetPt,  JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_deltaPhi_pred_raw = new TH2F("deltaPhi_Jet2_Pt_prediction", "deltaPhi_Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_deltaPhi_pred_raw = new TH2F("deltaPhi_Jet3_Pt_prediction", "deltaPhi_Jet3_Pt", NbinsJetPt,  JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_deltaPhi_pred_raw = new TH2F("deltaPhi_Jet1_Eta_prediction", "deltaPhi_Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_deltaPhi_pred_raw = new TH2F("deltaPhi_Jet2_Eta_prediction", "deltaPhi_Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_deltaPhi_pred_raw = new TH2F("deltaPhi_Jet3_Eta_prediction", "deltaPhi_Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   
   // HT inclusive, baseline
   MHT_JetBin1_HTinclusive_pred_raw = new TH2F("MHT_JetBin1_HTinclusive_pred", "MHT_JetBin1_HTinclusive_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin2_HTinclusive_pred_raw = new TH2F("MHT_JetBin2_HTinclusive_pred", "MHT_JetBin2_HTinclusive_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin3_HTinclusive_pred_raw = new TH2F("MHT_JetBin3_HTinclusive_pred", "MHT_JetBin3_HTinclusive_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin4_HTinclusive_pred_raw = new TH2F("MHT_JetBin4_HTinclusive_pred", "MHT_JetBin4_HTinclusive_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   
   // baseline
   HT_baseline_pred_raw = new TH2F("HT_baseline_pred", "HT baseline", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_baseline_pred_raw = new TH2F("MHT_baseline_pred", "MHT baseline", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   
   // baseline jet bin 1
   Jet1Pt_JetBin1_baseline_pred_raw = new TH2F("baseline_Jet1_Pt_JetBin1_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin1_baseline_pred_raw = new TH2F("baseline_Jet2_Pt_JetBin1_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin1_baseline_pred_raw = new TH2F("baseline_Jet1_Eta_JetBin1_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin1_baseline_pred_raw = new TH2F("baseline_Jet2_Eta_JetBin1_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin1_baseline_pred_raw = new TH2F("baseline_DeltaPhi1_JetBin1_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin1_baseline_pred_raw = new TH2F("baseline_DeltaPhi2_JetBin1_prediction", "DeltaPhi2", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // baseline jet bin 2
   Jet1Pt_JetBin2_baseline_pred_raw = new TH2F("baseline_Jet1_Pt_JetBin2_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin2_baseline_pred_raw = new TH2F("baseline_Jet2_Pt_JetBin2_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_JetBin2_baseline_pred_raw = new TH2F("baseline_Jet3_Pt_JetBin2_prediction", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin2_baseline_pred_raw = new TH2F("baseline_Jet1_Eta_JetBin2_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin2_baseline_pred_raw = new TH2F("baseline_Jet2_Eta_JetBin2_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_JetBin2_baseline_pred_raw = new TH2F("baseline_Jet3_Eta_JetBin2_prediction", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin2_baseline_pred_raw = new TH2F("baseline_DeltaPhi1_JetBin2_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin2_baseline_pred_raw = new TH2F("baseline_DeltaPhi2_JetBin2_prediction", "DeltaPhi2", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_JetBin2_baseline_pred_raw = new TH2F("baseline_DeltaPhi3_JetBin2_prediction", "DeltaPhi3", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // baseline jet bin 3
   Jet1Pt_JetBin3_baseline_pred_raw = new TH2F("baseline_Jet1_Pt_JetBin3_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin3_baseline_pred_raw = new TH2F("baseline_Jet2_Pt_JetBin3_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_JetBin3_baseline_pred_raw = new TH2F("baseline_Jet3_Pt_JetBin3_prediction", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin3_baseline_pred_raw = new TH2F("baseline_Jet1_Eta_JetBin3_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin3_baseline_pred_raw = new TH2F("baseline_Jet2_Eta_JetBin3_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_JetBin3_baseline_pred_raw = new TH2F("baseline_Jet3_Eta_JetBin3_prediction", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin3_baseline_pred_raw = new TH2F("baseline_DeltaPhi1_JetBin3_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin3_baseline_pred_raw = new TH2F("baseline_DeltaPhi2_JetBin3_prediction", "DeltaPhi2", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_JetBin3_baseline_pred_raw = new TH2F("baseline_DeltaPhi3_JetBin3_prediction", "DeltaPhi3", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // baseline jet bin 4
   Jet1Pt_JetBin4_baseline_pred_raw = new TH2F("baseline_Jet1_Pt_JetBin4_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin4_baseline_pred_raw = new TH2F("baseline_Jet2_Pt_JetBin4_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_JetBin4_baseline_pred_raw = new TH2F("baseline_Jet3_Pt_JetBin4_prediction", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin4_baseline_pred_raw = new TH2F("baseline_Jet1_Eta_JetBin4_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin4_baseline_pred_raw = new TH2F("baseline_Jet2_Eta_JetBin4_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_JetBin4_baseline_pred_raw = new TH2F("baseline_Jet3_Eta_JetBin4_prediction", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin4_baseline_pred_raw = new TH2F("baseline_DeltaPhi1_JetBin4_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin4_baseline_pred_raw = new TH2F("baseline_DeltaPhi2_JetBin4_prediction", "DeltaPhi2", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_JetBin4_baseline_pred_raw = new TH2F("baseline_DeltaPhi3_JetBin4_prediction", "DeltaPhi3", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   
   // baseline without delta Phi jet bin 1
   HT_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_HT_JetBin1_prediction", "HT_prediction", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_MHT_JetBin1_prediction", "MHT_prediction", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin1_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin1_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin1_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin1_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin1_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin1_prediction", "DeltaPhi2", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // baseline without delta Phi jet bin 2
   HT_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_HT_JetBin2_prediction", "HT_prediction", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_MHT_JetBin2_prediction", "MHT_prediction", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin2_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin2_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet3_Pt_JetBin2_prediction", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin2_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin2_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet3_Eta_JetBin2_prediction", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin2_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin2_prediction", "DeltaPhi2", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi3_JetBin2_prediction", "DeltaPhi3", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // baseline without delta Phi jet bin 3
   HT_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_HT_JetBin3_prediction", "HT_prediction", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_MHT_JetBin3_prediction", "MHT_prediction", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin3_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin3_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet3_Pt_JetBin3_prediction", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin3_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin3_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet3_Eta_JetBin3_prediction", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin3_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin3_prediction", "DeltaPhi2", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi3_JetBin3_prediction", "DeltaPhi3", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // baseline without delta Phi jet bin 4
   HT_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_HT_JetBin4_prediction", "HT_prediction", NbinsHT, HTmin, HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_MHT_JetBin4_prediction", "MHT_prediction", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin4_prediction", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin4_prediction", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet3_Pt_JetBin4_prediction", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin4_prediction", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin4_prediction", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_Jet3_Eta_JetBin4_prediction", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin4_prediction", "DeltaPhi1", 100, 0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin4_prediction", "DeltaPhi2", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred_raw = new TH2F("baseline_withoutDeltaPhi_DeltaPhi3_JetBin4_prediction", "DeltaPhi3", 100,  0., TMath::Pi(), Ntries, 0.5, Ntries + 0.5);
   
   // NJets
   NJets_baseline_withoutMHT_pred_raw = new TH2F("NJets_baseline_withoutMHT_pred", "NJets baseline", 15, 0, 15, Ntries, 0.5, Ntries + 0.5);
   NJets_baseline_pred_raw = new TH2F("NJets_baseline_pred", "NJets baseline", 15, 0, 15, Ntries, 0.5, Ntries + 0.5);
   NJets_baseline_withoutDeltaPhi_withoutMHT_pred_raw = new TH2F("NJets_baseline_withoutDeltaPhi_withoutMHT_pred", "NJets baseline", 15, 0, 15, Ntries, 0.5, Ntries + 0.5);
   NJets_baseline_withoutDeltaPhi_pred_raw = new TH2F("NJets_baseline_withoutDeltaPhi_pred", "NJets baseline", 15, 0, 15, Ntries, 0.5, Ntries + 0.5);
   NJets_presel_pred_raw = new TH2F("NJets_presel_pred_raw", "NJets presel", 15, 0, 15, Ntries, 0.5, Ntries + 0.5);
   
   // ------------------------------------------------------------------------------ //
   
   // define selection histograms
   // preselection
   HT_presel_sel = new TH1F("presel_HT_selection", "presel_HT_selection", NbinsHT, HTmin, HTmax);
   MHT_presel_sel = new TH1F("presel_MHT_selection", "presel_MHT_selection", NbinsMHT, MHTmin, MHTmax);
   Jet1Pt_presel_sel = new TH1F("presel_Jet1_Pt_selection", "presel_Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_presel_sel = new TH1F("presel_Jet2_Pt_selection", "presel_Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_presel_sel = new TH1F("presel_Jet3_Pt_selection", "presel_Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_presel_sel = new TH1F("presel_Jet1_Eta_selection", "presel_Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_presel_sel = new TH1F("presel_Jet2_Eta_selection", "presel_Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_presel_sel = new TH1F("presel_Jet3_Eta_selection", "presel_Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   DeltaPhi1_presel_sel = new TH1F("presel_DeltaPhi1_selection", "DeltaPhi1", 100, 0., TMath::Pi());
   DeltaPhi2_presel_sel = new TH1F("presel_DeltaPhi2_selection", "DeltaPhi2", 100, 0., TMath::Pi());
   DeltaPhi3_presel_sel = new TH1F("presel_DeltaPhi3_selection", "DeltaPhi3", 100, 0., TMath::Pi());
   
   // preselection + delta Phi
   HT_deltaPhi_sel = new TH1F("deltaPhi_HT_selection", "deltaPhi_HT_selection", NbinsHT, HTmin, HTmax);
   MHT_deltaPhi_sel = new TH1F("deltaPhi_MHT_selection", "deltaPhi_MHT_selection", NbinsMHT, MHTmin, MHTmax);
   Jet1Pt_deltaPhi_sel = new TH1F("deltaPhi_Jet1_Pt_selection", "deltaPhi_Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_deltaPhi_sel = new TH1F("deltaPhi_Jet2_Pt_selection", "deltaPhi_Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_deltaPhi_sel = new TH1F("deltaPhi_Jet3_Pt_selection", "deltaPhi_Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_deltaPhi_sel = new TH1F("deltaPhi_Jet1_Eta_selection", "deltaPhi_Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_deltaPhi_sel = new TH1F("deltaPhi_Jet2_Eta_selection", "deltaPhi_Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_deltaPhi_sel = new TH1F("deltaPhi_Jet3_Eta_selection", "deltaPhi_Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   
   // HT inclusive, baseline
   MHT_JetBin1_HTinclusive_sel = new TH1F("MHT_JetBin1_HTinclusive_sel", "MHT_JetBin1_HTinclusive_sel", NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin2_HTinclusive_sel = new TH1F("MHT_JetBin2_HTinclusive_sel", "MHT_JetBin2_HTinclusive_sel", NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin3_HTinclusive_sel = new TH1F("MHT_JetBin3_HTinclusive_sel", "MHT_JetBin3_HTinclusive_sel", NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin4_HTinclusive_sel = new TH1F("MHT_JetBin4_HTinclusive_sel", "MHT_JetBin4_HTinclusive_sel", NbinsMHT, MHTmin, MHTmax);
   
   //baseline
   HT_baseline_sel = new TH1F("HT_baseline_sel", "HT baseline", NbinsHT, HTmin, HTmax);
   MHT_baseline_sel = new TH1F("MHT_baseline_sel", "MHT baseline", NbinsMHT, MHTmin, MHTmax);
   
   // baseline jet bin 1
   Jet1Pt_JetBin1_baseline_sel = new TH1F("baseline_Jet1_Pt_JetBin1_selection", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_JetBin1_baseline_sel = new TH1F("baseline_Jet2_Pt_JetBin1_selection", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_JetBin1_baseline_sel = new TH1F("baseline_Jet1_Eta_JetBin1_selection", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_JetBin1_baseline_sel = new TH1F("baseline_Jet2_Eta_JetBin1_selection", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   DeltaPhi1_JetBin1_baseline_sel = new TH1F("baseline_DeltaPhi1_JetBin1_selection", "DeltaPhi1", 100, 0., TMath::Pi());
   DeltaPhi2_JetBin1_baseline_sel = new TH1F("baseline_DeltaPhi2_JetBin1_selection", "DeltaPhi2", 100, 0., TMath::Pi());
   
   // baseline jet bin 2
   Jet1Pt_JetBin2_baseline_sel = new TH1F("baseline_Jet1_Pt_JetBin2_selection", "Jet1_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet2Pt_JetBin2_baseline_sel = new TH1F("baseline_Jet2_Pt_JetBin2_selection", "Jet2_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet3Pt_JetBin2_baseline_sel = new TH1F("baseline_Jet3_Pt_JetBin2_selection", "Jet3_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet1Eta_JetBin2_baseline_sel = new TH1F("baseline_Jet1_Eta_JetBin2_selection", "Jet1_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   Jet2Eta_JetBin2_baseline_sel = new TH1F("baseline_Jet2_Eta_JetBin2_selection", "Jet2_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   Jet3Eta_JetBin2_baseline_sel = new TH1F("baseline_Jet3_Eta_JetBin2_selection", "Jet3_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   DeltaPhi1_JetBin2_baseline_sel = new TH1F("baseline_DeltaPhi1_JetBin2_selection", "DeltaPhi1", 100,0., TMath::Pi());
   DeltaPhi2_JetBin2_baseline_sel = new TH1F("baseline_DeltaPhi2_JetBin2_selection", "DeltaPhi2", 100,0., TMath::Pi());
   DeltaPhi3_JetBin2_baseline_sel = new TH1F("baseline_DeltaPhi3_JetBin2_selection", "DeltaPhi3", 100,0., TMath::Pi());
   
   // baseline jet bin 3
   Jet1Pt_JetBin3_baseline_sel = new TH1F("baseline_Jet1_Pt_JetBin3_selection", "Jet1_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet2Pt_JetBin3_baseline_sel = new TH1F("baseline_Jet2_Pt_JetBin3_selection", "Jet2_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet3Pt_JetBin3_baseline_sel = new TH1F("baseline_Jet3_Pt_JetBin3_selection", "Jet3_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet1Eta_JetBin3_baseline_sel = new TH1F("baseline_Jet1_Eta_JetBin3_selection", "Jet1_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   Jet2Eta_JetBin3_baseline_sel = new TH1F("baseline_Jet2_Eta_JetBin3_selection", "Jet2_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   Jet3Eta_JetBin3_baseline_sel = new TH1F("baseline_Jet3_Eta_JetBin3_selection", "Jet3_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   DeltaPhi1_JetBin3_baseline_sel = new TH1F("baseline_DeltaPhi1_JetBin3_selection", "DeltaPhi1", 100,0., TMath::Pi());
   DeltaPhi2_JetBin3_baseline_sel = new TH1F("baseline_DeltaPhi2_JetBin3_selection", "DeltaPhi2", 100,0., TMath::Pi());
   DeltaPhi3_JetBin3_baseline_sel = new TH1F("baseline_DeltaPhi3_JetBin3_selection", "DeltaPhi3", 100,0., TMath::Pi());
   
   // baseline jet bin 4
   Jet1Pt_JetBin4_baseline_sel = new TH1F("baseline_Jet1_Pt_JetBin4_selection", "Jet1_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet2Pt_JetBin4_baseline_sel = new TH1F("baseline_Jet2_Pt_JetBin4_selection", "Jet2_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet3Pt_JetBin4_baseline_sel = new TH1F("baseline_Jet3_Pt_JetBin4_selection", "Jet3_Pt", NbinsJetPt,JetPtmin, JetPtmax);
   Jet1Eta_JetBin4_baseline_sel = new TH1F("baseline_Jet1_Eta_JetBin4_selection", "Jet1_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   Jet2Eta_JetBin4_baseline_sel = new TH1F("baseline_Jet2_Eta_JetBin4_selection", "Jet2_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   Jet3Eta_JetBin4_baseline_sel = new TH1F("baseline_Jet3_Eta_JetBin4_selection", "Jet3_Eta", NbinsJetEta,JetEtamin, JetEtamax);
   DeltaPhi1_JetBin4_baseline_sel = new TH1F("baseline_DeltaPhi1_JetBin4_selection", "DeltaPhi1", 100,0., TMath::Pi());
   DeltaPhi2_JetBin4_baseline_sel = new TH1F("baseline_DeltaPhi2_JetBin4_selection", "DeltaPhi2", 100,0., TMath::Pi());
   DeltaPhi3_JetBin4_baseline_sel = new TH1F("baseline_DeltaPhi3_JetBin4_selection", "DeltaPhi3", 100,0., TMath::Pi());
   
   // baseline without delta Phi jet bin 1
   HT_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_HT_JetBin1_selection", "HT_selection", NbinsHT, HTmin, HTmax);
   MHT_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_MHT_JetBin1_selection", "MHT_selection", NbinsMHT, MHTmin, MHTmax);
   Jet1Pt_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin1_selection", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin1_selection", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin1_selection", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin1_selection", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin1_selection", "DeltaPhi1", 100, 0., TMath::Pi());
   DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin1_selection", "DeltaPhi2", 100, 0., TMath::Pi());
   
   // baseline without delta Phi jet bin 2
   HT_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_HT_JetBin2_selection", "HT_selection", NbinsHT, HTmin, HTmax);
   MHT_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_MHT_JetBin2_selection", "MHT_selection", NbinsMHT, MHTmin, MHTmax);
   Jet1Pt_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin2_selection", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin2_selection", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet3_Pt_JetBin2_selection", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin2_selection", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin2_selection", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet3_Eta_JetBin2_selection", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin2_selection", "DeltaPhi1", 100, 0., TMath::Pi());
   DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin2_selection", "DeltaPhi2", 100, 0., TMath::Pi());
   DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi3_JetBin2_selection", "DeltaPhi3", 100, 0., TMath::Pi());
   
   // baseline without delta Phi jet bin 3
   HT_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_HT_JetBin3_selection", "HT_selection", NbinsHT, HTmin, HTmax);
   MHT_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_MHT_JetBin3_selection", "MHT_selection", NbinsMHT, MHTmin, MHTmax);
   Jet1Pt_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin3_selection", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin3_selection", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet3_Pt_JetBin3_selection", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin3_selection", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin3_selection", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet3_Eta_JetBin3_selection", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin3_selection", "DeltaPhi1", 100, 0., TMath::Pi());
   DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin3_selection", "DeltaPhi2", 100, 0., TMath::Pi());
   DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi3_JetBin3_selection", "DeltaPhi3", 100, 0., TMath::Pi());
   
   // baseline without delta Phi jet bin 4
   HT_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_HT_JetBin4_selection", "HT_selection", NbinsHT, HTmin, HTmax);
   MHT_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_MHT_JetBin4_selection", "MHT_selection", NbinsMHT, MHTmin, MHTmax);
   Jet1Pt_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Pt_JetBin4_selection", "Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Pt_JetBin4_selection", "Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet3_Pt_JetBin4_selection", "Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet1_Eta_JetBin4_selection", "Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet2_Eta_JetBin4_selection", "Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_Jet3_Eta_JetBin4_selection", "Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi1_JetBin4_selection", "DeltaPhi1", 100, 0., TMath::Pi());
   DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi2_JetBin4_selection", "DeltaPhi2", 100, 0., TMath::Pi());
   DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_sel = new TH1F("baseline_withoutDeltaPhi_DeltaPhi3_JetBin4_selection", "DeltaPhi3", 100, 0., TMath::Pi());
   
   // NJets
   NJets_baseline_withoutMHT_sel = new TH1F("NJets_baseline_withoutMHT_sel", "NJets baseline", 15, 0, 15);
   NJets_baseline_sel = new TH1F("NJets_baseline_sel", "NJets baseline", 15, 0, 15);
   NJets_baseline_withoutDeltaPhi_withoutMHT_sel = new TH1F("NJets_baseline_withoutDeltaPhi_withoutMHT_sel", "NJets baseline", 15, 0, 15);
   NJets_baseline_withoutDeltaPhi_sel = new TH1F("NJets_baseline_withoutDeltaPhi_sel", "NJets baseline", 15, 0, 15);
   NJets_presel_sel = new TH1F("NJets_presel_sel", "NJets presel", 15, 0, 15);
   
   // ------------------------------------------------------------------------------ //
   
   // get tree with predictions
   cout << "entries prediction tree:" << QCDPrediction.GetEntries() << endl;
   
   // variables from prediction tree
   Float_t HT_seed = 0;
   Float_t HT = 0;
   Float_t MHT = 0;
   Float_t Jet1Pt = 0;
   Float_t Jet2Pt = 0;
   Float_t Jet3Pt = 0;
   Float_t Jet1Eta = 0;
   Float_t Jet2Eta = 0;
   Float_t Jet3Eta = 0;
   
   NJets = 0;
   NSmear = 0;
   weight = 0;
   DeltaPhi1 = 0;
   DeltaPhi2 = 0;
   DeltaPhi3 = 0;
   
   cout << "Before: SetBranchAddress (prediction)" << endl;
   
   QCDPrediction.SetBranchAddress("NVtx",&vtxN);
   QCDPrediction.SetBranchAddress("NJets",&NJets);
   QCDPrediction.SetBranchAddress("BTags",&BTags);
   QCDPrediction.SetBranchAddress("Ntries",&NSmear);
   QCDPrediction.SetBranchAddress("Weight",&weight);
   QCDPrediction.SetBranchAddress("HT",&HT);
   QCDPrediction.SetBranchAddress("MHT",&MHT);
   QCDPrediction.SetBranchAddress("HT_seed",&HT_seed);
   QCDPrediction.SetBranchAddress("Jet1Pt",&Jet1Pt);
   QCDPrediction.SetBranchAddress("Jet2Pt",&Jet2Pt);
   QCDPrediction.SetBranchAddress("Jet3Pt",&Jet3Pt);
   QCDPrediction.SetBranchAddress("Jet1Eta",&Jet1Eta);
   QCDPrediction.SetBranchAddress("Jet2Eta",&Jet2Eta);
   QCDPrediction.SetBranchAddress("Jet3Eta",&Jet3Eta);
   QCDPrediction.SetBranchAddress("DeltaPhi1",&DeltaPhi1);
   QCDPrediction.SetBranchAddress("DeltaPhi2",&DeltaPhi2);
   QCDPrediction.SetBranchAddress("DeltaPhi3",&DeltaPhi3);
   
   cout << "After: SetBranchAddress (prediction)" << endl;

   int Prediction_entries = 0;
   float smear_rep = 0;
   
   // loop over entries and fill prediction histos
   ULong_t nentries = QCDPrediction.GetEntries();
   //Int_t nentries = 10000000;
   for ( ULong_t i = 0 ; i<nentries ; i++) {
      QCDPrediction.GetEntry(i);
      
      if( i%1000000 == 0 ) std::cout << "event (prediction): " << i << '\n';
      
      // select reasonable event weights
      if( weight < 30000. ) {
         
         // apply same HT cut as on selection
         if( HT > 500. ) {
            
            // ------------------------------------------------------------- //
            // fill preselection histos
            // ------------------------------------------------------------- //
            
            if( NJets > 2 ) {
               HT_presel_pred_raw->Fill(HT, NSmear, weight);
               MHT_presel_pred_raw->Fill(MHT, NSmear, weight);
               NJets_presel_pred_raw->Fill(NJets, NSmear, weight);
               Jet1Pt_presel_pred_raw->Fill(Jet1Pt, NSmear, weight);
               Jet2Pt_presel_pred_raw->Fill(Jet2Pt, NSmear, weight);
               Jet3Pt_presel_pred_raw->Fill(Jet3Pt, NSmear, weight);
               Jet1Eta_presel_pred_raw->Fill(Jet1Eta, NSmear, weight);
               Jet2Eta_presel_pred_raw->Fill(Jet2Eta, NSmear, weight);
               Jet3Eta_presel_pred_raw->Fill(Jet3Eta, NSmear, weight);
               DeltaPhi1_presel_pred_raw->Fill(DeltaPhi1, NSmear, weight);
               DeltaPhi2_presel_pred_raw->Fill(DeltaPhi2, NSmear, weight);
               DeltaPhi3_presel_pred_raw->Fill(DeltaPhi3, NSmear, weight);
            }
            
            // ------------------------------------------------------------- //
            // baseline closure without deltaPhi
            // ------------------------------------------------------------- //
            // HT baseline cut
            if( HT > 500. ) {
               if( NJets > 2 ) {
                  NJets_baseline_withoutDeltaPhi_withoutMHT_pred_raw->Fill(NJets, NSmear, weight);
               }
               if( NJets == 2 ) {
                  MHT_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(MHT, NSmear, weight);
               }
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  MHT_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(MHT, NSmear, weight);
               }
               else if(  NJets == 6  ||  NJets == 7 ) {
                  MHT_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(MHT, NSmear, weight);
               }
               else if(  NJets >= 8 ) {
                  MHT_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(MHT, NSmear, weight);
               }
               
               // MHT baseline cut
               if( MHT > 200. ) {
                  if( NJets > 2 ) {
                     NJets_baseline_withoutDeltaPhi_pred_raw->Fill(NJets, NSmear, weight);
                  }
                  // jet bin 1
                  if( NJets == 2 ) {
                     Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                  }
                  // jet bin 2
                  else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                     Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(Jet3Pt, NSmear, weight);
                     Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(Jet3Eta, NSmear, weight);
                     DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                     DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi3, NSmear, weight);
                  }
                  // jet bin 3
                  else if( NJets == 6  ||  NJets == 7 ) {
                     Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(Jet3Pt, NSmear, weight);
                     Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(Jet3Eta, NSmear, weight);
                     DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                     DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi3, NSmear, weight);
                     
                  }
                  // jet bin 4
                  else if( NJets >= 8 ) {
                     Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(Jet3Pt, NSmear, weight);
                     Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(Jet3Eta, NSmear, weight);
                     DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                     DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(DeltaPhi3, NSmear, weight);
                  }
               }
            }
            
            // MHT baseline cut
            if( MHT > 200. ) {
               if( NJets == 2 ) {
                  HT_JetBin1_baseline_withoutDeltaPhi_pred_raw->Fill(HT, NSmear, weight);
               }
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  HT_JetBin2_baseline_withoutDeltaPhi_pred_raw->Fill(HT, NSmear, weight);
               }
               else if(  NJets == 6  ||  NJets == 7 ) {
                  HT_JetBin3_baseline_withoutDeltaPhi_pred_raw->Fill(HT, NSmear, weight);
               }
               else if(  NJets >= 8 ) {
                  HT_JetBin4_baseline_withoutDeltaPhi_pred_raw->Fill(HT, NSmear, weight);
               }
            }
            
            
            // ------------------------------------------------------------- //
            // check deltaPhi cut
            if( DeltaPhiCut_prediction() ) {
               
               // ------------------------------------------------------------- //
               // fill histos after deltaPhi cut
               // ------------------------------------------------------------- //
               if( NJets > 2 ) {
                  HT_deltaPhi_pred_raw->Fill(HT, NSmear, weight);
                  MHT_deltaPhi_pred_raw->Fill(MHT, NSmear, weight);
                  Jet1Pt_deltaPhi_pred_raw->Fill(Jet1Pt, NSmear, weight);
                  Jet2Pt_deltaPhi_pred_raw->Fill(Jet2Pt, NSmear, weight);
                  Jet3Pt_deltaPhi_pred_raw->Fill(Jet3Pt, NSmear, weight);
                  Jet1Eta_deltaPhi_pred_raw->Fill(Jet1Eta, NSmear, weight);
                  Jet2Eta_deltaPhi_pred_raw->Fill(Jet2Eta, NSmear, weight);
                  Jet3Eta_deltaPhi_pred_raw->Fill(Jet3Eta, NSmear, weight);
                  
                  // ------------------------------------------------------------- //
                  // fill baseline histos
                  // ------------------------------------------------------------- //
                  if( HT > 500. ) {
                     MHT_baseline_pred_raw->Fill(MHT, NSmear, weight);
                     NJets_baseline_withoutMHT_pred_raw->Fill(NJets, NSmear, weight);
                     if( MHT > 200. ) {
                        NJets_baseline_pred_raw->Fill(NJets, NSmear, weight);
                     }
                  }
                  if( MHT > 200. ) {
                     HT_baseline_pred_raw->Fill(HT, NSmear, weight);
                  }
               }
               
               // ------------------------------------------------------------- //
               //  fill different jet multiplicity bins
               // ------------------------------------------------------------- //
               // jet bin 1
               if( NJets == 2 ) {
                  MHT_JetBin1_HTinclusive_pred_raw->Fill(MHT, NSmear, weight);
                  
                  if( MHT > 200. ) {
                     Jet1Pt_JetBin1_baseline_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin1_baseline_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet1Eta_JetBin1_baseline_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin1_baseline_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     DeltaPhi1_JetBin1_baseline_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin1_baseline_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                  }
                  
               }
               // jet bin 2
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  MHT_JetBin2_HTinclusive_pred_raw->Fill(MHT, NSmear, weight);
                  
                  if( MHT > 200. ) {
                     Jet1Pt_JetBin2_baseline_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin2_baseline_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet3Pt_JetBin2_baseline_pred_raw->Fill(Jet3Pt, NSmear, weight);
                     Jet1Eta_JetBin2_baseline_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin2_baseline_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     Jet3Eta_JetBin2_baseline_pred_raw->Fill(Jet3Eta, NSmear, weight);
                     DeltaPhi1_JetBin2_baseline_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin2_baseline_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                     DeltaPhi3_JetBin2_baseline_pred_raw->Fill(DeltaPhi3, NSmear, weight);
                  }
                  
               }
               // jet bin 3
               else if(  NJets == 6  ||  NJets == 7 ) {
                  MHT_JetBin3_HTinclusive_pred_raw->Fill(MHT, NSmear, weight);
                  
                  if( MHT > 200. ) {
                     Jet1Pt_JetBin3_baseline_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin3_baseline_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet3Pt_JetBin3_baseline_pred_raw->Fill(Jet3Pt, NSmear, weight);
                     Jet1Eta_JetBin3_baseline_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin3_baseline_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     Jet3Eta_JetBin3_baseline_pred_raw->Fill(Jet3Eta, NSmear, weight);
                     DeltaPhi1_JetBin3_baseline_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin3_baseline_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                     DeltaPhi3_JetBin3_baseline_pred_raw->Fill(DeltaPhi3, NSmear, weight);
                  }
                  
               }
               // jet bin 4
               else if(  NJets >= 8 ) {
                  MHT_JetBin4_HTinclusive_pred_raw->Fill(MHT, NSmear, weight);
                  
                  if( MHT > 200. ) {
                     Jet1Pt_JetBin4_baseline_pred_raw->Fill(Jet1Pt, NSmear, weight);
                     Jet2Pt_JetBin4_baseline_pred_raw->Fill(Jet2Pt, NSmear, weight);
                     Jet3Pt_JetBin4_baseline_pred_raw->Fill(Jet3Pt, NSmear, weight);
                     Jet1Eta_JetBin4_baseline_pred_raw->Fill(Jet1Eta, NSmear, weight);
                     Jet2Eta_JetBin4_baseline_pred_raw->Fill(Jet2Eta, NSmear, weight);
                     Jet3Eta_JetBin4_baseline_pred_raw->Fill(Jet3Eta, NSmear, weight);
                     DeltaPhi1_JetBin4_baseline_pred_raw->Fill(DeltaPhi1, NSmear, weight);
                     DeltaPhi2_JetBin4_baseline_pred_raw->Fill(DeltaPhi2, NSmear, weight);
                     DeltaPhi3_JetBin4_baseline_pred_raw->Fill(DeltaPhi3, NSmear, weight);
                  }
               }
               
            }
         }
      }
   }
   
   cout << "Prediction entries final: " <<  Prediction_entries << endl;
   
   // ------------------------------------------------------------- //
   
   ///////////////////////////////////////////////////////////////////////
   // get event selections
   cout << "entries selection tree:" << RA2PreSelection.GetEntries() << endl;
   
   // variables from selection tree
   Float_t HT_RA2 = 0;
   Float_t MHT_RA2 = 0;
   Float_t Jet1Pt_RA2 = 0;
   Float_t Jet2Pt_RA2 = 0;
   Float_t Jet3Pt_RA2 = 0;
   Float_t Jet1Eta_RA2 = 0;
   Float_t Jet2Eta_RA2 = 0;
   Float_t Jet3Eta_RA2 = 0;
   
   EvtNum_RA2 = 0;
   vtxN_RA2 = 0;
   NJets_RA2 = 0;
   BTags_RA2 = 0;
   weight_RA2 = 0;
   DeltaPhi1_RA2 = 0;
   DeltaPhi2_RA2 = 0;
   DeltaPhi3_RA2 = 0;
   
   cout << "Before: SetBranchAddress (expectation)" << endl;

   RA2PreSelection.SetBranchAddress("NVtx",&vtxN_RA2);
   RA2PreSelection.SetBranchAddress("NJets",&NJets_RA2);
   RA2PreSelection.SetBranchAddress("BTags",&BTags_RA2);
   RA2PreSelection.SetBranchAddress("Weight",&weight_RA2);
   RA2PreSelection.SetBranchAddress("EvtNum",&EvtNum_RA2);
   RA2PreSelection.SetBranchAddress("HT",&HT_RA2);
   RA2PreSelection.SetBranchAddress("MHT",&MHT_RA2);
   RA2PreSelection.SetBranchAddress("Jet1Pt",&Jet1Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet2Pt",&Jet2Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet3Pt",&Jet3Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet1Eta",&Jet1Eta_RA2);
   RA2PreSelection.SetBranchAddress("Jet2Eta",&Jet2Eta_RA2);
   RA2PreSelection.SetBranchAddress("Jet3Eta",&Jet3Eta_RA2);
   RA2PreSelection.SetBranchAddress("DeltaPhi1",&DeltaPhi1_RA2);
   RA2PreSelection.SetBranchAddress("DeltaPhi2",&DeltaPhi2_RA2);
   RA2PreSelection.SetBranchAddress("DeltaPhi3",&DeltaPhi3_RA2);
   
   cout << "After: SetBranchAddress (expectation)" << endl;

   // loop over entries and fill selection histos
   Int_t nentries2 = RA2PreSelection.GetEntries();
   //Int_t nentries2 = 500000;
   for ( Int_t i = 0 ; i<nentries2 ; i++) {
      RA2PreSelection.GetEntry(i);
      
      if( i%100000 == 0 ) std::cout << "event (selection): " << i << '\n';
      
      if( weight_RA2 > 30000. ) {
         
         cout << "------------------------------" << endl;
         cout << "Event: " << EvtNum_RA2 << endl;
         cout << "Weight: " << weight_RA2 << endl;
         cout << "NVtx: " << vtxN_RA2 << endl;
         cout << "HT: " << HT_RA2 << endl;
         cout << "MHT: " << MHT_RA2 << endl;
         cout << "NJets: " << NJets_RA2 << endl;
         cout << "------------------------------" << endl;
      }
      
      // select reasonable event weights
      if( weight_RA2 < 30000. ) {
         
         if( NJets_RA2 >= 2 ) {
            
            // ------------------------------------------------------------- //
            // fill preselection histos
            // ------------------------------------------------------------- //
            
            if( NJets_RA2 > 2 ) {
               HT_presel_sel->Fill(HT_RA2, weight_RA2);
               MHT_presel_sel->Fill(MHT_RA2, weight_RA2);
               NJets_presel_sel->Fill(NJets_RA2, weight_RA2);
               Jet1Pt_presel_sel->Fill(Jet1Pt_RA2, weight_RA2);
               Jet2Pt_presel_sel->Fill(Jet2Pt_RA2, weight_RA2);
               Jet3Pt_presel_sel->Fill(Jet3Pt_RA2, weight_RA2);
               Jet1Eta_presel_sel->Fill(Jet1Eta_RA2, weight_RA2);
               Jet2Eta_presel_sel->Fill(Jet2Eta_RA2, weight_RA2);
               Jet3Eta_presel_sel->Fill(Jet3Eta_RA2, weight_RA2);
               DeltaPhi1_presel_sel->Fill(DeltaPhi1_RA2, weight_RA2);
               DeltaPhi2_presel_sel->Fill(DeltaPhi2_RA2, weight_RA2);
               DeltaPhi3_presel_sel->Fill(DeltaPhi3_RA2, weight_RA2);
            }
            
            // ------------------------------------------------------------- //
            // baseline closure without deltaPhi
            // ------------------------------------------------------------- //
            // HT baseline cut
            if( HT_RA2 > 500. ) {
               if( NJets_RA2 > 2 ) {
                  NJets_baseline_withoutDeltaPhi_withoutMHT_sel->Fill(NJets_RA2, weight_RA2);
               }
               if( NJets_RA2 == 2 ) {
                  MHT_JetBin1_baseline_withoutDeltaPhi_sel->Fill(MHT_RA2, weight_RA2);
               }
               else if( NJets_RA2 == 3 || NJets_RA2 == 4 ||  NJets_RA2 == 5 ) {
                  MHT_JetBin2_baseline_withoutDeltaPhi_sel->Fill(MHT_RA2, weight_RA2);
               }
               else if(  NJets_RA2 == 6  ||  NJets_RA2 == 7 ) {
                  MHT_JetBin3_baseline_withoutDeltaPhi_sel->Fill(MHT_RA2, weight_RA2);
               }
               else if(  NJets_RA2 >= 8 ) {
                  MHT_JetBin4_baseline_withoutDeltaPhi_sel->Fill(MHT_RA2, weight_RA2);
               }
               
               // MHT baseline cut
               if( MHT_RA2 > 200. ) {
                  if( NJets_RA2 > 2 ) {
                     NJets_baseline_withoutDeltaPhi_sel->Fill(NJets_RA2, weight_RA2);
                  }
                  // jet bin 1
                  if( NJets_RA2 == 2 ) {
                     Jet1Pt_JetBin1_baseline_withoutDeltaPhi_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin1_baseline_withoutDeltaPhi_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin1_baseline_withoutDeltaPhi_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin1_baseline_withoutDeltaPhi_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                  }
                  // jet bin 2
                  else if( NJets_RA2 == 3 || NJets_RA2 == 4 ||  NJets_RA2 == 5 ) {
                     Jet1Pt_JetBin2_baseline_withoutDeltaPhi_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin2_baseline_withoutDeltaPhi_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet3Pt_JetBin2_baseline_withoutDeltaPhi_sel->Fill(Jet3Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin2_baseline_withoutDeltaPhi_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin2_baseline_withoutDeltaPhi_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     Jet3Eta_JetBin2_baseline_withoutDeltaPhi_sel->Fill(Jet3Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                     DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi3_RA2, weight_RA2);
                  }
                  // jet bin 3
                  else if( NJets_RA2 == 6  ||  NJets_RA2 == 7 ) {
                     Jet1Pt_JetBin3_baseline_withoutDeltaPhi_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin3_baseline_withoutDeltaPhi_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet3Pt_JetBin3_baseline_withoutDeltaPhi_sel->Fill(Jet3Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin3_baseline_withoutDeltaPhi_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin3_baseline_withoutDeltaPhi_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     Jet3Eta_JetBin3_baseline_withoutDeltaPhi_sel->Fill(Jet3Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                     DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi3_RA2, weight_RA2);
                     
                  }
                  // jet bin 4
                  else if( NJets_RA2 >= 8 ) {
                     Jet1Pt_JetBin4_baseline_withoutDeltaPhi_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin4_baseline_withoutDeltaPhi_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet3Pt_JetBin4_baseline_withoutDeltaPhi_sel->Fill(Jet3Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin4_baseline_withoutDeltaPhi_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin4_baseline_withoutDeltaPhi_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     Jet3Eta_JetBin4_baseline_withoutDeltaPhi_sel->Fill(Jet3Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                     DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_sel->Fill(DeltaPhi3_RA2, weight_RA2);
                  }
               }
            }
            
            // MHT baseline cut
            if( MHT_RA2 > 200. ) {
               if( NJets_RA2 == 2 ) {
                  HT_JetBin1_baseline_withoutDeltaPhi_sel->Fill(HT_RA2, weight_RA2);
               }
               else if( NJets_RA2 == 3 || NJets_RA2 == 4 ||  NJets_RA2 == 5 ) {
                  HT_JetBin2_baseline_withoutDeltaPhi_sel->Fill(HT_RA2, weight_RA2);
               }
               else if(  NJets_RA2 == 6  ||  NJets_RA2 == 7 ) {
                  HT_JetBin3_baseline_withoutDeltaPhi_sel->Fill(HT_RA2, weight_RA2);
               }
               else if(  NJets_RA2 >= 8 ) {
                  HT_JetBin4_baseline_withoutDeltaPhi_sel->Fill(HT_RA2, weight_RA2);
               }
            }
            
            // ------------------------------------------------------------- //
            // check deltaPhi Cut
            if( DeltaPhiCut_selection() ) {
               
               // ------------------------------------------------------------- //
               // fill histos after deltaPhi cut
               // ------------------------------------------------------------- //
               if( NJets_RA2 > 2 ) {
                  HT_deltaPhi_sel->Fill(HT_RA2, weight_RA2);
                  MHT_deltaPhi_sel->Fill(MHT_RA2, weight_RA2);
                  Jet1Pt_deltaPhi_sel->Fill(Jet1Pt_RA2, weight_RA2);
                  Jet2Pt_deltaPhi_sel->Fill(Jet2Pt_RA2, weight_RA2);
                  Jet3Pt_deltaPhi_sel->Fill(Jet3Pt_RA2, weight_RA2);
                  Jet1Eta_deltaPhi_sel->Fill(Jet1Eta_RA2, weight_RA2);
                  Jet2Eta_deltaPhi_sel->Fill(Jet2Eta_RA2, weight_RA2);
                  Jet3Eta_deltaPhi_sel->Fill(Jet3Eta_RA2, weight_RA2);
                  
                  // ------------------------------------------------------------- //
                  // fill baseline histos
                  // ------------------------------------------------------------- //
                  if( HT_RA2 > 500. ) {
                     MHT_baseline_sel->Fill(MHT_RA2, weight_RA2);
                     NJets_baseline_withoutMHT_sel->Fill(NJets_RA2, weight_RA2);
                     if( MHT_RA2 > 200. ) {
                        NJets_baseline_sel->Fill(NJets_RA2, weight_RA2);
                     }
                  }
                  if( MHT_RA2 > 200. ) {
                     HT_baseline_sel->Fill(HT_RA2, weight_RA2);
                  }
               }
               
               // ------------------------------------------------------------- //
               //  fill different jet multiplicity bins
               // ------------------------------------------------------------- //
               // jet bin 1
               if( NJets_RA2 == 2 ) {
                  MHT_JetBin1_HTinclusive_sel->Fill(MHT_RA2, weight_RA2);
                  
                  if( MHT_RA2 > 200. ) {
                     Jet1Pt_JetBin1_baseline_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin1_baseline_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin1_baseline_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin1_baseline_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin1_baseline_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin1_baseline_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                  }
                  
               }
               // jet bin 2
               else if( NJets_RA2 == 3 || NJets_RA2 == 4 ||  NJets_RA2 == 5 ) {
                  MHT_JetBin2_HTinclusive_sel->Fill(MHT_RA2, weight_RA2);
                  
                  if( MHT_RA2 > 200. ) {
                     Jet1Pt_JetBin2_baseline_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin2_baseline_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet3Pt_JetBin2_baseline_sel->Fill(Jet3Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin2_baseline_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin2_baseline_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     Jet3Eta_JetBin2_baseline_sel->Fill(Jet3Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin2_baseline_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin2_baseline_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                     DeltaPhi3_JetBin2_baseline_sel->Fill(DeltaPhi3_RA2, weight_RA2);
                  }
                  
               }
               // jet bin 3
               else if(  NJets_RA2 == 6  ||  NJets_RA2 == 7 ) {
                  MHT_JetBin3_HTinclusive_sel->Fill(MHT_RA2, weight_RA2);
                  
                  if( MHT_RA2 > 200. ) {
                     Jet1Pt_JetBin3_baseline_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin3_baseline_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet3Pt_JetBin3_baseline_sel->Fill(Jet3Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin3_baseline_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin3_baseline_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     Jet3Eta_JetBin3_baseline_sel->Fill(Jet3Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin3_baseline_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin3_baseline_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                     DeltaPhi3_JetBin3_baseline_sel->Fill(DeltaPhi3_RA2, weight_RA2);
                  }
               }
               // jet bin 4
               else if(  NJets_RA2 >= 8 ) {
                  MHT_JetBin4_HTinclusive_sel->Fill(MHT_RA2, weight_RA2);
                  
                  if( MHT_RA2 > 200. ) {
                     Jet1Pt_JetBin4_baseline_sel->Fill(Jet1Pt_RA2, weight_RA2);
                     Jet2Pt_JetBin4_baseline_sel->Fill(Jet2Pt_RA2, weight_RA2);
                     Jet3Pt_JetBin4_baseline_sel->Fill(Jet3Pt_RA2, weight_RA2);
                     Jet1Eta_JetBin4_baseline_sel->Fill(Jet1Eta_RA2, weight_RA2);
                     Jet2Eta_JetBin4_baseline_sel->Fill(Jet2Eta_RA2, weight_RA2);
                     Jet3Eta_JetBin4_baseline_sel->Fill(Jet3Eta_RA2, weight_RA2);
                     DeltaPhi1_JetBin4_baseline_sel->Fill(DeltaPhi1_RA2, weight_RA2);
                     DeltaPhi2_JetBin4_baseline_sel->Fill(DeltaPhi2_RA2, weight_RA2);
                     DeltaPhi3_JetBin4_baseline_sel->Fill(DeltaPhi3_RA2, weight_RA2);
                  }
               }
            }
         }
      }
   }
   
   //----------------------------------------------------------//
   
   //----------------------------------------------------------//
   // rebin histos
   // ------------------------------------------------------------- //
   DoRebinning(HT_presel_pred_raw, HT_presel_sel , -1);
   DoRebinning(MHT_presel_pred_raw, MHT_presel_sel , -2);
   DoRebinning(Jet1Pt_presel_pred_raw, Jet1Pt_presel_sel , 10);
   DoRebinning(Jet2Pt_presel_pred_raw, Jet2Pt_presel_sel , 10);
   DoRebinning(Jet3Pt_presel_pred_raw, Jet3Pt_presel_sel , 10);
   DoRebinning(Jet1Eta_presel_pred_raw, Jet1Eta_presel_sel , 2);
   DoRebinning(Jet2Eta_presel_pred_raw, Jet2Eta_presel_sel , 2);
   DoRebinning(Jet3Eta_presel_pred_raw, Jet3Eta_presel_sel , 2);
   DoRebinning(DeltaPhi1_presel_pred_raw, DeltaPhi1_presel_sel , 5);
   DoRebinning(DeltaPhi2_presel_pred_raw, DeltaPhi2_presel_sel , 5);
   DoRebinning(DeltaPhi3_presel_pred_raw, DeltaPhi3_presel_sel , 5);
   
   DoRebinning(HT_deltaPhi_pred_raw, HT_deltaPhi_sel , -1);
   DoRebinning(MHT_deltaPhi_pred_raw, MHT_deltaPhi_sel , -2);
   DoRebinning(Jet1Pt_deltaPhi_pred_raw, Jet1Pt_deltaPhi_sel , 10);
   DoRebinning(Jet2Pt_deltaPhi_pred_raw, Jet2Pt_deltaPhi_sel , 10);
   DoRebinning(Jet3Pt_deltaPhi_pred_raw, Jet3Pt_deltaPhi_sel , 10);
   DoRebinning(Jet1Eta_deltaPhi_pred_raw, Jet1Eta_deltaPhi_sel , 2);
   DoRebinning(Jet2Eta_deltaPhi_pred_raw, Jet2Eta_deltaPhi_sel , 2);
   DoRebinning(Jet3Eta_deltaPhi_pred_raw, Jet3Eta_deltaPhi_sel , 2);
   
   DoRebinning(MHT_JetBin1_HTinclusive_pred_raw, MHT_JetBin1_HTinclusive_sel , -2);
   DoRebinning(MHT_JetBin2_HTinclusive_pred_raw, MHT_JetBin2_HTinclusive_sel , -2);
   DoRebinning(MHT_JetBin3_HTinclusive_pred_raw, MHT_JetBin3_HTinclusive_sel , -2);
   DoRebinning(MHT_JetBin4_HTinclusive_pred_raw, MHT_JetBin4_HTinclusive_sel , -2);
   
   DoRebinning(HT_baseline_pred_raw, HT_baseline_sel , -1);
   DoRebinning(MHT_baseline_pred_raw, MHT_baseline_sel , -2);
   
   DoRebinning(Jet1Pt_JetBin1_baseline_pred_raw, Jet1Pt_JetBin1_baseline_sel, 10);
   DoRebinning(Jet2Pt_JetBin1_baseline_pred_raw, Jet2Pt_JetBin1_baseline_sel, 10);
   DoRebinning(Jet1Eta_JetBin1_baseline_pred_raw, Jet1Eta_JetBin1_baseline_sel, 2);
   DoRebinning(Jet2Eta_JetBin1_baseline_pred_raw, Jet2Eta_JetBin1_baseline_sel, 2);
   DoRebinning(DeltaPhi1_JetBin1_baseline_pred_raw, DeltaPhi1_JetBin1_baseline_sel, 5);
   DoRebinning(DeltaPhi2_JetBin1_baseline_pred_raw, DeltaPhi2_JetBin1_baseline_sel, 5);
   
   DoRebinning(Jet1Pt_JetBin2_baseline_pred_raw, Jet1Pt_JetBin2_baseline_sel, 10);
   DoRebinning(Jet2Pt_JetBin2_baseline_pred_raw, Jet2Pt_JetBin2_baseline_sel, 10);
   DoRebinning(Jet3Pt_JetBin2_baseline_pred_raw, Jet3Pt_JetBin2_baseline_sel, 10);
   DoRebinning(Jet1Eta_JetBin2_baseline_pred_raw, Jet1Eta_JetBin2_baseline_sel, 2);
   DoRebinning(Jet2Eta_JetBin2_baseline_pred_raw, Jet2Eta_JetBin2_baseline_sel, 2);
   DoRebinning(Jet3Eta_JetBin2_baseline_pred_raw, Jet3Eta_JetBin2_baseline_sel, 2);
   DoRebinning(DeltaPhi1_JetBin2_baseline_pred_raw, DeltaPhi1_JetBin2_baseline_sel, 5);
   DoRebinning(DeltaPhi2_JetBin2_baseline_pred_raw, DeltaPhi2_JetBin2_baseline_sel, 5);
   DoRebinning(DeltaPhi3_JetBin2_baseline_pred_raw, DeltaPhi3_JetBin2_baseline_sel, 5);
   
   DoRebinning(Jet1Pt_JetBin3_baseline_pred_raw, Jet1Pt_JetBin3_baseline_sel, 10);
   DoRebinning(Jet2Pt_JetBin3_baseline_pred_raw, Jet2Pt_JetBin3_baseline_sel, 10);
   DoRebinning(Jet3Pt_JetBin3_baseline_pred_raw, Jet3Pt_JetBin3_baseline_sel, 10);
   DoRebinning(Jet1Eta_JetBin3_baseline_pred_raw, Jet1Eta_JetBin3_baseline_sel, 2);
   DoRebinning(Jet2Eta_JetBin3_baseline_pred_raw, Jet2Eta_JetBin3_baseline_sel, 2);
   DoRebinning(Jet3Eta_JetBin3_baseline_pred_raw, Jet3Eta_JetBin3_baseline_sel, 2);
   DoRebinning(DeltaPhi1_JetBin3_baseline_pred_raw, DeltaPhi1_JetBin3_baseline_sel, 5);
   DoRebinning(DeltaPhi2_JetBin3_baseline_pred_raw, DeltaPhi2_JetBin3_baseline_sel, 5);
   DoRebinning(DeltaPhi3_JetBin3_baseline_pred_raw, DeltaPhi3_JetBin3_baseline_sel, 5);
   
   DoRebinning(Jet1Pt_JetBin4_baseline_pred_raw, Jet1Pt_JetBin4_baseline_sel, 10);
   DoRebinning(Jet2Pt_JetBin4_baseline_pred_raw, Jet2Pt_JetBin4_baseline_sel, 10);
   DoRebinning(Jet3Pt_JetBin4_baseline_pred_raw, Jet3Pt_JetBin4_baseline_sel, 10);
   DoRebinning(Jet1Eta_JetBin4_baseline_pred_raw, Jet1Eta_JetBin4_baseline_sel, 2);
   DoRebinning(Jet2Eta_JetBin4_baseline_pred_raw, Jet2Eta_JetBin4_baseline_sel, 2);
   DoRebinning(Jet3Eta_JetBin4_baseline_pred_raw, Jet3Eta_JetBin4_baseline_sel, 2);
   DoRebinning(DeltaPhi1_JetBin4_baseline_pred_raw, DeltaPhi1_JetBin4_baseline_sel, 5);
   DoRebinning(DeltaPhi2_JetBin4_baseline_pred_raw, DeltaPhi2_JetBin4_baseline_sel, 5);
   DoRebinning(DeltaPhi3_JetBin4_baseline_pred_raw, DeltaPhi3_JetBin4_baseline_sel, 5);
   
   DoRebinning(HT_JetBin1_baseline_withoutDeltaPhi_pred_raw, HT_JetBin1_baseline_withoutDeltaPhi_sel, -1);
   DoRebinning(MHT_JetBin1_baseline_withoutDeltaPhi_pred_raw, MHT_JetBin1_baseline_withoutDeltaPhi_sel, -2);
   DoRebinning(Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw, Jet1Pt_JetBin1_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw, Jet2Pt_JetBin1_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw, Jet1Eta_JetBin1_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw, Jet2Eta_JetBin1_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred_raw, DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred_raw, DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_sel, 5);
   
   DoRebinning(HT_JetBin2_baseline_withoutDeltaPhi_pred_raw, HT_JetBin2_baseline_withoutDeltaPhi_sel, -1);
   DoRebinning(MHT_JetBin2_baseline_withoutDeltaPhi_pred_raw, MHT_JetBin2_baseline_withoutDeltaPhi_sel, -2);
   DoRebinning(Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw, Jet1Pt_JetBin2_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw, Jet2Pt_JetBin2_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw, Jet3Pt_JetBin2_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw, Jet1Eta_JetBin2_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw, Jet2Eta_JetBin2_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw, Jet3Eta_JetBin2_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred_raw, DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred_raw, DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred_raw, DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_sel, 5);
   
   DoRebinning(HT_JetBin3_baseline_withoutDeltaPhi_pred_raw, HT_JetBin3_baseline_withoutDeltaPhi_sel, -1);
   DoRebinning(MHT_JetBin3_baseline_withoutDeltaPhi_pred_raw, MHT_JetBin3_baseline_withoutDeltaPhi_sel, -2);
   DoRebinning(Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw, Jet1Pt_JetBin3_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw, Jet2Pt_JetBin3_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw, Jet3Pt_JetBin3_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw, Jet1Eta_JetBin3_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw, Jet2Eta_JetBin3_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw, Jet3Eta_JetBin3_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred_raw, DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred_raw, DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred_raw, DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_sel, 5);
   
   DoRebinning(HT_JetBin4_baseline_withoutDeltaPhi_pred_raw, HT_JetBin4_baseline_withoutDeltaPhi_sel, -1);
   DoRebinning(MHT_JetBin4_baseline_withoutDeltaPhi_pred_raw, MHT_JetBin4_baseline_withoutDeltaPhi_sel, -2);
   DoRebinning(Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw, Jet1Pt_JetBin4_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw, Jet2Pt_JetBin4_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw, Jet3Pt_JetBin4_baseline_withoutDeltaPhi_sel, 10);
   DoRebinning(Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw, Jet1Eta_JetBin4_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw, Jet2Eta_JetBin4_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw, Jet3Eta_JetBin4_baseline_withoutDeltaPhi_sel, 2);
   DoRebinning(DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred_raw, DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred_raw, DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_sel, 5);
   DoRebinning(DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred_raw, DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_sel, 5);
   
   //----------------------------------------------------------//
   
   //----------------------------------------------------------//
   // fill prediction histos
   HT_presel_pred = CalcPrediction(HT_presel_pred_raw);
   MHT_presel_pred = CalcPrediction(MHT_presel_pred_raw);
   NJets_presel_pred = CalcPrediction(NJets_presel_pred_raw);
   Jet1Pt_presel_pred = CalcPrediction(Jet1Pt_presel_pred_raw);
   Jet2Pt_presel_pred = CalcPrediction(Jet2Pt_presel_pred_raw);
   Jet3Pt_presel_pred = CalcPrediction(Jet3Pt_presel_pred_raw);
   Jet1Eta_presel_pred = CalcPrediction(Jet1Eta_presel_pred_raw);
   Jet2Eta_presel_pred = CalcPrediction(Jet2Eta_presel_pred_raw);
   Jet3Eta_presel_pred = CalcPrediction(Jet3Eta_presel_pred_raw);
   DeltaPhi1_presel_pred = CalcPrediction(DeltaPhi1_presel_pred_raw);
   DeltaPhi2_presel_pred = CalcPrediction(DeltaPhi2_presel_pred_raw);
   DeltaPhi3_presel_pred = CalcPrediction(DeltaPhi3_presel_pred_raw);
   
   HT_deltaPhi_pred = CalcPrediction(HT_deltaPhi_pred_raw);
   MHT_deltaPhi_pred = CalcPrediction(MHT_deltaPhi_pred_raw);
   Jet1Pt_deltaPhi_pred = CalcPrediction(Jet1Pt_deltaPhi_pred_raw);
   Jet2Pt_deltaPhi_pred = CalcPrediction(Jet2Pt_deltaPhi_pred_raw);
   Jet3Pt_deltaPhi_pred = CalcPrediction(Jet3Pt_deltaPhi_pred_raw);
   Jet1Eta_deltaPhi_pred = CalcPrediction(Jet1Eta_deltaPhi_pred_raw);
   Jet2Eta_deltaPhi_pred = CalcPrediction(Jet2Eta_deltaPhi_pred_raw);
   Jet3Eta_deltaPhi_pred = CalcPrediction(Jet3Eta_deltaPhi_pred_raw);
   
   MHT_JetBin1_HTinclusive_pred = CalcPrediction(MHT_JetBin1_HTinclusive_pred_raw);
   MHT_JetBin2_HTinclusive_pred = CalcPrediction(MHT_JetBin2_HTinclusive_pred_raw);
   MHT_JetBin3_HTinclusive_pred = CalcPrediction(MHT_JetBin3_HTinclusive_pred_raw);
   MHT_JetBin4_HTinclusive_pred = CalcPrediction(MHT_JetBin4_HTinclusive_pred_raw);
   
   HT_baseline_pred = CalcPrediction( HT_baseline_pred_raw);
   MHT_baseline_pred = CalcPrediction( MHT_baseline_pred_raw);
   
   Jet1Pt_JetBin1_baseline_pred = CalcPrediction(Jet1Pt_JetBin1_baseline_pred_raw);
   Jet2Pt_JetBin1_baseline_pred = CalcPrediction(Jet2Pt_JetBin1_baseline_pred_raw);
   Jet1Eta_JetBin1_baseline_pred = CalcPrediction(Jet1Eta_JetBin1_baseline_pred_raw);
   Jet2Eta_JetBin1_baseline_pred = CalcPrediction(Jet2Eta_JetBin1_baseline_pred_raw);
   DeltaPhi1_JetBin1_baseline_pred = CalcPrediction(DeltaPhi1_JetBin1_baseline_pred_raw);
   DeltaPhi2_JetBin1_baseline_pred = CalcPrediction(DeltaPhi2_JetBin1_baseline_pred_raw);
   
   Jet1Pt_JetBin2_baseline_pred = CalcPrediction(Jet1Pt_JetBin2_baseline_pred_raw);
   Jet2Pt_JetBin2_baseline_pred = CalcPrediction(Jet2Pt_JetBin2_baseline_pred_raw);
   Jet3Pt_JetBin2_baseline_pred = CalcPrediction(Jet3Pt_JetBin2_baseline_pred_raw);
   Jet1Eta_JetBin2_baseline_pred = CalcPrediction(Jet1Eta_JetBin2_baseline_pred_raw);
   Jet2Eta_JetBin2_baseline_pred = CalcPrediction(Jet2Eta_JetBin2_baseline_pred_raw);
   Jet3Eta_JetBin2_baseline_pred = CalcPrediction(Jet3Eta_JetBin2_baseline_pred_raw);
   DeltaPhi1_JetBin2_baseline_pred = CalcPrediction(DeltaPhi1_JetBin2_baseline_pred_raw);
   DeltaPhi2_JetBin2_baseline_pred = CalcPrediction(DeltaPhi2_JetBin2_baseline_pred_raw);
   DeltaPhi3_JetBin2_baseline_pred = CalcPrediction(DeltaPhi3_JetBin2_baseline_pred_raw);
   
   Jet1Pt_JetBin3_baseline_pred = CalcPrediction(Jet1Pt_JetBin3_baseline_pred_raw);
   Jet2Pt_JetBin3_baseline_pred = CalcPrediction(Jet2Pt_JetBin3_baseline_pred_raw);
   Jet3Pt_JetBin3_baseline_pred = CalcPrediction(Jet3Pt_JetBin3_baseline_pred_raw);
   Jet1Eta_JetBin3_baseline_pred = CalcPrediction(Jet1Eta_JetBin3_baseline_pred_raw);
   Jet2Eta_JetBin3_baseline_pred = CalcPrediction(Jet2Eta_JetBin3_baseline_pred_raw);
   Jet3Eta_JetBin3_baseline_pred = CalcPrediction(Jet3Eta_JetBin3_baseline_pred_raw);
   DeltaPhi1_JetBin3_baseline_pred = CalcPrediction(DeltaPhi1_JetBin3_baseline_pred_raw);
   DeltaPhi2_JetBin3_baseline_pred = CalcPrediction(DeltaPhi2_JetBin3_baseline_pred_raw);
   DeltaPhi3_JetBin3_baseline_pred = CalcPrediction(DeltaPhi3_JetBin3_baseline_pred_raw);
   
   Jet1Pt_JetBin4_baseline_pred = CalcPrediction(Jet1Pt_JetBin4_baseline_pred_raw);
   Jet2Pt_JetBin4_baseline_pred = CalcPrediction(Jet2Pt_JetBin4_baseline_pred_raw);
   Jet3Pt_JetBin4_baseline_pred = CalcPrediction(Jet3Pt_JetBin4_baseline_pred_raw);
   Jet1Eta_JetBin4_baseline_pred = CalcPrediction(Jet1Eta_JetBin4_baseline_pred_raw);
   Jet2Eta_JetBin4_baseline_pred = CalcPrediction(Jet2Eta_JetBin4_baseline_pred_raw);
   Jet3Eta_JetBin4_baseline_pred = CalcPrediction(Jet3Eta_JetBin4_baseline_pred_raw);
   DeltaPhi1_JetBin4_baseline_pred = CalcPrediction(DeltaPhi1_JetBin4_baseline_pred_raw);
   DeltaPhi2_JetBin4_baseline_pred = CalcPrediction(DeltaPhi2_JetBin4_baseline_pred_raw);
   DeltaPhi3_JetBin4_baseline_pred = CalcPrediction(DeltaPhi3_JetBin4_baseline_pred_raw);
   
   HT_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(HT_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   MHT_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(MHT_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred_raw);
   
   HT_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(HT_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   MHT_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(MHT_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred_raw);
   
   HT_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(HT_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   MHT_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(MHT_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred_raw);
   
   HT_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(HT_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   MHT_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(MHT_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred = CalcPrediction(DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred_raw);
   
   NJets_baseline_withoutMHT_pred = CalcPrediction( NJets_baseline_withoutMHT_pred_raw);
   NJets_baseline_pred = CalcPrediction( NJets_baseline_pred_raw);
   NJets_baseline_withoutDeltaPhi_withoutMHT_pred = CalcPrediction(NJets_baseline_withoutDeltaPhi_withoutMHT_pred_raw);
   NJets_baseline_withoutDeltaPhi_pred = CalcPrediction(NJets_baseline_withoutDeltaPhi_pred_raw);
   //----------------------------------------------------------//
   
   //----------------------------------------------------------//
   // write histos to file
   TFile* prediction_histos = new TFile("output_GetPrediction/prediction_histos.root", "RECREATE");
   
   // Save histograms: prediction
   
   HT_presel_pred->Write();
   MHT_presel_pred->Write();
   NJets_presel_pred->Write();
   Jet1Pt_presel_pred->Write();
   Jet2Pt_presel_pred->Write();
   Jet3Pt_presel_pred->Write();
   Jet1Eta_presel_pred->Write();
   Jet2Eta_presel_pred->Write();
   Jet3Eta_presel_pred->Write();
   
   HT_deltaPhi_pred->Write();
   MHT_deltaPhi_pred->Write();
   Jet1Pt_deltaPhi_pred->Write();
   Jet2Pt_deltaPhi_pred->Write();
   Jet3Pt_deltaPhi_pred->Write();
   Jet1Eta_deltaPhi_pred->Write();
   Jet2Eta_deltaPhi_pred->Write();
   Jet3Eta_deltaPhi_pred->Write();
   
   NJets_baseline_withoutMHT_pred->Write();
   NJets_baseline_pred->Write();
   NJets_baseline_withoutDeltaPhi_withoutMHT_pred->Write();
   NJets_baseline_withoutDeltaPhi_pred ->Write();
   
   HT_baseline_pred->Write();
   MHT_baseline_pred->Write();
   MHT_JetBin1_HTinclusive_pred->Write();
   MHT_JetBin2_HTinclusive_pred->Write();
   MHT_JetBin3_HTinclusive_pred->Write();
   MHT_JetBin4_HTinclusive_pred->Write();
   
   Jet1Pt_JetBin1_baseline_pred->Write();
   Jet2Pt_JetBin1_baseline_pred->Write();
   Jet1Eta_JetBin1_baseline_pred->Write();
   Jet2Eta_JetBin1_baseline_pred->Write();
   DeltaPhi1_JetBin1_baseline_pred->Write();
   DeltaPhi2_JetBin1_baseline_pred->Write();
   
   Jet1Pt_JetBin2_baseline_pred->Write();
   Jet2Pt_JetBin2_baseline_pred->Write();
   Jet3Pt_JetBin2_baseline_pred->Write();
   Jet1Eta_JetBin2_baseline_pred->Write();
   Jet2Eta_JetBin2_baseline_pred->Write();
   Jet3Eta_JetBin2_baseline_pred->Write();
   DeltaPhi1_JetBin2_baseline_pred->Write();
   DeltaPhi2_JetBin2_baseline_pred->Write();
   DeltaPhi3_JetBin2_baseline_pred->Write();
   
   Jet1Pt_JetBin3_baseline_pred->Write();
   Jet2Pt_JetBin3_baseline_pred->Write();
   Jet3Pt_JetBin3_baseline_pred->Write();
   Jet1Eta_JetBin3_baseline_pred->Write();
   Jet2Eta_JetBin3_baseline_pred->Write();
   Jet3Eta_JetBin3_baseline_pred->Write();
   DeltaPhi1_JetBin3_baseline_pred->Write();
   DeltaPhi2_JetBin3_baseline_pred->Write();
   DeltaPhi3_JetBin3_baseline_pred->Write();
   
   Jet1Pt_JetBin4_baseline_pred->Write();
   Jet2Pt_JetBin4_baseline_pred->Write();
   Jet3Pt_JetBin4_baseline_pred->Write();
   Jet1Eta_JetBin4_baseline_pred->Write();
   Jet2Eta_JetBin4_baseline_pred->Write();
   Jet3Eta_JetBin4_baseline_pred->Write();
   DeltaPhi1_JetBin4_baseline_pred->Write();
   DeltaPhi2_JetBin4_baseline_pred->Write();
   DeltaPhi3_JetBin4_baseline_pred->Write();
   
   HT_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   MHT_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred->Write();
   
   HT_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   MHT_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred->Write();
   
   HT_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   MHT_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred->Write();
   
   HT_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   MHT_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred->Write();
   
   // Save histograms: expectation
   
   HT_presel_sel->Write();
   MHT_presel_sel->Write();
   NJets_presel_sel->Write();
   Jet1Pt_presel_sel->Write();
   Jet2Pt_presel_sel->Write();
   Jet3Pt_presel_sel->Write();
   Jet1Eta_presel_sel->Write();
   Jet2Eta_presel_sel->Write();
   Jet3Eta_presel_sel->Write();
   HT_deltaPhi_sel->Write();
   MHT_deltaPhi_sel->Write();
   Jet1Pt_deltaPhi_sel->Write();
   Jet2Pt_deltaPhi_sel->Write();
   Jet3Pt_deltaPhi_sel->Write();
   Jet1Eta_deltaPhi_sel->Write();
   Jet2Eta_deltaPhi_sel->Write();
   Jet3Eta_deltaPhi_sel->Write();
   NJets_baseline_withoutMHT_sel->Write();
   NJets_baseline_sel->Write();
   NJets_baseline_withoutDeltaPhi_withoutMHT_sel->Write();
   NJets_baseline_withoutDeltaPhi_sel ->Write();
   
   HT_baseline_sel->Write();
   MHT_baseline_sel->Write();
   MHT_JetBin1_HTinclusive_sel->Write();
   MHT_JetBin2_HTinclusive_sel->Write();
   MHT_JetBin3_HTinclusive_sel->Write();
   MHT_JetBin4_HTinclusive_sel->Write();
   
   Jet1Pt_JetBin1_baseline_sel->Write();
   Jet2Pt_JetBin1_baseline_sel->Write();
   Jet1Eta_JetBin1_baseline_sel->Write();
   Jet2Eta_JetBin1_baseline_sel->Write();
   DeltaPhi1_JetBin1_baseline_sel->Write();
   DeltaPhi2_JetBin1_baseline_sel->Write();
   
   Jet1Pt_JetBin2_baseline_sel->Write();
   Jet2Pt_JetBin2_baseline_sel->Write();
   Jet3Pt_JetBin2_baseline_sel->Write();
   Jet1Eta_JetBin2_baseline_sel->Write();
   Jet2Eta_JetBin2_baseline_sel->Write();
   Jet3Eta_JetBin2_baseline_sel->Write();
   DeltaPhi1_JetBin2_baseline_sel->Write();
   DeltaPhi2_JetBin2_baseline_sel->Write();
   DeltaPhi3_JetBin2_baseline_sel->Write();
   
   Jet1Pt_JetBin3_baseline_sel->Write();
   Jet2Pt_JetBin3_baseline_sel->Write();
   Jet3Pt_JetBin3_baseline_sel->Write();
   Jet1Eta_JetBin3_baseline_sel->Write();
   Jet2Eta_JetBin3_baseline_sel->Write();
   Jet3Eta_JetBin3_baseline_sel->Write();
   DeltaPhi1_JetBin3_baseline_sel->Write();
   DeltaPhi2_JetBin3_baseline_sel->Write();
   DeltaPhi3_JetBin3_baseline_sel->Write();
   
   Jet1Pt_JetBin4_baseline_sel->Write();
   Jet2Pt_JetBin4_baseline_sel->Write();
   Jet3Pt_JetBin4_baseline_sel->Write();
   Jet1Eta_JetBin4_baseline_sel->Write();
   Jet2Eta_JetBin4_baseline_sel->Write();
   Jet3Eta_JetBin4_baseline_sel->Write();
   DeltaPhi1_JetBin4_baseline_sel->Write();
   DeltaPhi2_JetBin4_baseline_sel->Write();
   DeltaPhi3_JetBin4_baseline_sel->Write();
   
   HT_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   MHT_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   Jet1Pt_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   Jet2Pt_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   Jet1Eta_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   Jet2Eta_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_sel->Write();
   
   HT_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   MHT_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   Jet1Pt_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   Jet2Pt_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   Jet3Pt_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   Jet1Eta_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   Jet2Eta_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   Jet3Eta_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_sel->Write();
   
   HT_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   MHT_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   Jet1Pt_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   Jet2Pt_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   Jet3Pt_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   Jet1Eta_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   Jet2Eta_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   Jet3Eta_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_sel->Write();
   
   HT_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   MHT_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   Jet1Pt_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   Jet2Pt_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   Jet3Pt_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   Jet1Eta_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   Jet2Eta_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   Jet3Eta_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_sel->Write();
   
   prediction_histos->Write();
   //----------------------------------------------------------//
}

////////////////////////////////////////////////////////////////////////////////////////
bool Prediction::DeltaPhiCut_prediction()
{
   bool deltaPhiCut = true;
   if( NJets == 2 ) {
      if( DeltaPhi1 < 0.5 ||
         DeltaPhi2 < 0.5 ) deltaPhiCut = false;
   }
   if( NJets >= 3 ) {
      if( DeltaPhi1 < 0.5 ||
         DeltaPhi2 < 0.5 ||
         DeltaPhi3 < 0.3 ) deltaPhiCut = false;
   }
   
   return deltaPhiCut;
}
////////////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////
bool Prediction::DeltaPhiCut_selection()
{
   bool deltaPhiCut = true;
   if( NJets_RA2 == 2 ) {
      if( DeltaPhi1_RA2 < 0.5 ||
         DeltaPhi2_RA2 < 0.5 ) deltaPhiCut = false;
   }
   if( NJets_RA2 >= 3 ) {
      if( DeltaPhi1_RA2 < 0.5 ||
         DeltaPhi2_RA2 < 0.5 ||
         DeltaPhi3_RA2 < 0.3 ) deltaPhiCut = false;
   }
   
   return deltaPhiCut;
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
void Prediction::DoRebinning(TH2F* prediction_raw, TH1F* selection_raw, int Nbins)
{
   //do some non-equidistant binning
   if (Nbins < 0) {
      int nbins = 19;
      // HT binning
      double vbins[20] = {0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1300, 1500, 1700, 2000, 2500, 3000, 4000, 5000};
      
      // MHT binning
      if (Nbins == -2) {
         vbins[1]  = 0.;
         vbins[2]  = 10.;
         vbins[3]  = 20.;
         vbins[4]  = 30.;
         vbins[5]  = 40.;
         vbins[6]  = 50.;
         vbins[7]  = 60.;
         vbins[8]  = 70.;
         vbins[9]  = 80.;
         vbins[10] = 90.;
         vbins[11] = 100.;
         vbins[12] = 110.;
         vbins[13] = 120.;
         vbins[14] = 150.;
         vbins[15] = 200.;
         vbins[16] = 350.;
         vbins[17] = 500.;
         vbins[18] = 600.;
         vbins[19] = 700.;
         vbins[20] = 800.;
      }
      
      TH2F* temp = (TH2F*) prediction_raw->Clone();
      prediction_raw->GetXaxis()->Set(nbins, &vbins[0]);
      for (int j = 0; j <= prediction_raw->GetYaxis()->GetNbins() + 1; ++j) {
         for (int i = 0; i <= prediction_raw->GetXaxis()->GetNbins() + 1; ++i) {
            prediction_raw->SetBinContent(i, j, 0);
            prediction_raw->SetBinError(i, j, 0);
         }
      }
      
      //loop over y-axis
      for (int j = 1; j < temp->GetYaxis()->GetNbins() + 1; ++j) {
         int bin = 0;
         double sum2 = 0., content = 0.;
         for (int i = 0; i <= temp->GetXaxis()->GetNbins() + 1; ++i) {
            int this_bin = prediction_raw->GetXaxis()->FindBin(temp->GetXaxis()->GetBinCenter(i));
            if (this_bin > bin) {
               double binWidth = prediction_raw->GetXaxis()->GetBinWidth(bin);
               prediction_raw->SetBinContent(bin, j, content/binWidth);
               prediction_raw->SetBinError(bin, j, sqrt(sum2)/binWidth);
               bin = this_bin;
               sum2 = content = 0.;
            }
            sum2 += pow(temp->GetBinError(i, j), 2);
            content += temp->GetBinContent(i, j);
         }
         
      }
      
      TH1F* temp2 = (TH1F*) selection_raw->Clone();
      selection_raw->GetXaxis()->Set(nbins, &vbins[0]);
      for (int i = 0; i <= selection_raw->GetXaxis()->GetNbins() + 1; ++i) {
         selection_raw->SetBinContent(i, 0);
         selection_raw->SetBinError(i, 0);
      }
      
      int bin = 0;
      double sum2 = 0., content = 0.;
      for (int i = 0; i <= temp2->GetXaxis()->GetNbins() + 1; ++i) {
         int this_bin = selection_raw->GetXaxis()->FindBin(temp->GetXaxis()->GetBinCenter(i));
         if (this_bin > bin) {
            double binWidth = selection_raw->GetXaxis()->GetBinWidth(bin);
            selection_raw->SetBinContent(bin, content/binWidth);
            selection_raw->SetBinError(bin, sqrt(sum2)/binWidth);
            bin = this_bin;
            sum2 = content = 0.;
         }
         sum2 += pow(temp2->GetBinError(i), 2);
         content += temp2->GetBinContent(i);
      }
      
   } else {
      prediction_raw->Rebin2D(Nbins, 1);
      selection_raw->Rebin(Nbins);
   }
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
TH1F* Prediction::CalcPrediction(TH2F* prediction_raw) {
   TH1F* prediction = new TH1F();
   prediction = (TH1F*) prediction_raw->ProjectionX();
   prediction->Reset();
   for (int i = 0; i <= prediction_raw->GetXaxis()->GetNbins() + 1; ++i) {
      TH1F h = *((TH1F*) prediction_raw->ProjectionY("py", i, i));
      
      double summ = 0;
      double sumv = 0;
      int N = 0;
      
      //// Calculate mean
      for (int j = 1; j <= h.GetNbinsX(); ++j) {
         //for (int j = 501; j <= 1000; ++j) {
         summ += h.GetBinContent(j);
         ++N;
      }
      double mean = summ / N;
      
      //// Calculated variance
      for (int j = 1; j <= h.GetNbinsX(); ++j) {
         //for (int j = 501; j <= 1000; ++j) {
         sumv += pow(mean - h.GetBinContent(j), 2);
      }
      double variance = sqrt(sumv / N);
      //cout << "i, mean, variance: " << i << " " << mean << " " << variance << endl;
      
      prediction->SetBinContent(i, mean);
      prediction->SetBinError(i, variance);
   }
   
   return prediction;
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
TH1F* Prediction::GetSelectionHisto(TString type) {
   
   if ( type == "HT_presel") return HT_presel_sel;
   if ( type == "MHT_presel") return MHT_presel_sel;
   if ( type == "NJets_presel") return NJets_presel_sel;
   if ( type == "Jet1Pt_presel") return Jet1Pt_presel_sel;
   if ( type == "Jet2Pt_presel") return Jet2Pt_presel_sel;
   if ( type == "Jet3Pt_presel") return Jet3Pt_presel_sel;
   if ( type == "Jet1Eta_presel") return Jet1Eta_presel_sel;
   if ( type == "Jet2Eta_presel") return Jet2Eta_presel_sel;
   if ( type == "Jet3Eta_presel") return Jet3Eta_presel_sel;
   if ( type == "DeltaPhi1_presel") return DeltaPhi1_presel_sel;
   if ( type == "DeltaPhi2_presel") return DeltaPhi2_presel_sel;
   if ( type == "DeltaPhi3_presel") return DeltaPhi3_presel_sel;
   
   if ( type == "HT_deltaPhi") return HT_deltaPhi_sel;
   if ( type == "MHT_deltaPhi") return MHT_deltaPhi_sel;
   if ( type == "Jet1Pt_deltaPhi") return Jet1Pt_deltaPhi_sel;
   if ( type == "Jet2Pt_deltaPhi") return Jet2Pt_deltaPhi_sel;
   if ( type == "Jet3Pt_deltaPhi") return Jet3Pt_deltaPhi_sel;
   if ( type == "Jet1Eta_deltaPhi") return Jet1Eta_deltaPhi_sel;
   if ( type == "Jet2Eta_deltaPhi") return Jet2Eta_deltaPhi_sel;
   if ( type == "Jet3Eta_deltaPhi") return Jet3Eta_deltaPhi_sel;
   
   if ( type == "MHT_JetBin1_HTinclusive") return MHT_JetBin1_HTinclusive_sel;
   if ( type == "MHT_JetBin2_HTinclusive") return MHT_JetBin2_HTinclusive_sel;
   if ( type == "MHT_JetBin3_HTinclusive") return MHT_JetBin3_HTinclusive_sel;
   if ( type == "MHT_JetBin4_HTinclusive") return MHT_JetBin4_HTinclusive_sel;
   
   if ( type == "HT_baseline") return HT_baseline_sel;
   if ( type == "MHT_baseline") return MHT_baseline_sel;
   
   if( type == "Jet1Pt_JetBin1_baseline" ) return Jet1Pt_JetBin1_baseline_sel;
   if( type == "Jet2Pt_JetBin1_baseline" ) return Jet2Pt_JetBin1_baseline_sel;
   if( type == "Jet1Eta_JetBin1_baseline" ) return Jet1Eta_JetBin1_baseline_sel;
   if( type == "Jet2Eta_JetBin1_baseline" ) return Jet2Eta_JetBin1_baseline_sel;
   if( type == "DeltaPhi1_JetBin1_baseline") return DeltaPhi1_JetBin1_baseline_sel;
   if( type == "DeltaPhi2_JetBin1_baseline") return DeltaPhi2_JetBin1_baseline_sel;
   
   if( type == "Jet1Pt_JetBin2_baseline" ) return Jet1Pt_JetBin2_baseline_sel;
   if( type == "Jet2Pt_JetBin2_baseline" ) return Jet2Pt_JetBin2_baseline_sel;
   if( type == "Jet3Pt_JetBin2_baseline" ) return Jet3Pt_JetBin2_baseline_sel;
   if( type == "Jet1Eta_JetBin2_baseline" ) return Jet1Eta_JetBin2_baseline_sel;
   if( type == "Jet2Eta_JetBin2_baseline" ) return Jet2Eta_JetBin2_baseline_sel;
   if( type == "Jet3Eta_JetBin2_baseline" ) return Jet3Eta_JetBin2_baseline_sel;
   if( type == "DeltaPhi1_JetBin2_baseline") return DeltaPhi1_JetBin2_baseline_sel;
   if( type == "DeltaPhi2_JetBin2_baseline") return DeltaPhi2_JetBin2_baseline_sel;
   if( type == "DeltaPhi3_JetBin2_baseline") return DeltaPhi3_JetBin2_baseline_sel;
   
   if( type == "Jet1Pt_JetBin3_baseline" ) return Jet1Pt_JetBin3_baseline_sel;
   if( type == "Jet2Pt_JetBin3_baseline" ) return Jet2Pt_JetBin3_baseline_sel;
   if( type == "Jet3Pt_JetBin3_baseline" ) return Jet3Pt_JetBin3_baseline_sel;
   if( type == "Jet1Eta_JetBin3_baseline" ) return Jet1Eta_JetBin3_baseline_sel;
   if( type == "Jet2Eta_JetBin3_baseline" ) return Jet2Eta_JetBin3_baseline_sel;
   if( type == "Jet3Eta_JetBin3_baseline" ) return Jet3Eta_JetBin3_baseline_sel;
   if( type == "DeltaPhi1_JetBin3_baseline") return DeltaPhi1_JetBin3_baseline_sel;
   if( type == "DeltaPhi2_JetBin3_baseline") return DeltaPhi2_JetBin3_baseline_sel;
   if( type == "DeltaPhi3_JetBin3_baseline") return DeltaPhi3_JetBin3_baseline_sel;
   
   if( type == "Jet1Pt_JetBin4_baseline" ) return Jet1Pt_JetBin4_baseline_sel;
   if( type == "Jet2Pt_JetBin4_baseline" ) return Jet2Pt_JetBin4_baseline_sel;
   if( type == "Jet3Pt_JetBin4_baseline" ) return Jet3Pt_JetBin4_baseline_sel;
   if( type == "Jet1Eta_JetBin4_baseline" ) return Jet1Eta_JetBin4_baseline_sel;
   if( type == "Jet2Eta_JetBin4_baseline" ) return Jet2Eta_JetBin4_baseline_sel;
   if( type == "Jet3Eta_JetBin4_baseline" ) return Jet3Eta_JetBin4_baseline_sel;
   if( type == "DeltaPhi1_JetBin4_baseline") return DeltaPhi1_JetBin4_baseline_sel;
   if( type == "DeltaPhi2_JetBin4_baseline") return DeltaPhi2_JetBin4_baseline_sel;
   if( type == "DeltaPhi3_JetBin4_baseline") return DeltaPhi3_JetBin4_baseline_sel;
   
   if( type == "HT_JetBin1_baseline_withoutDeltaPhi") return HT_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "MHT_JetBin1_baseline_withoutDeltaPhi") return MHT_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Pt_JetBin1_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Pt_JetBin1_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Eta_JetBin1_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Eta_JetBin1_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi1_JetBin1_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi2_JetBin1_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_sel;
   
   if( type == "HT_JetBin2_baseline_withoutDeltaPhi") return HT_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "MHT_JetBin2_baseline_withoutDeltaPhi") return MHT_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Pt_JetBin2_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Pt_JetBin2_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "Jet3Pt_JetBin2_baseline_withoutDeltaPhi" ) return Jet3Pt_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Eta_JetBin2_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Eta_JetBin2_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "Jet3Eta_JetBin2_baseline_withoutDeltaPhi" ) return Jet3Eta_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi1_JetBin2_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi2_JetBin2_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi3_JetBin2_baseline_withoutDeltaPhi") return DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_sel;
   
   if( type == "HT_JetBin3_baseline_withoutDeltaPhi") return HT_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "MHT_JetBin3_baseline_withoutDeltaPhi") return MHT_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Pt_JetBin3_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Pt_JetBin3_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "Jet3Pt_JetBin3_baseline_withoutDeltaPhi" ) return Jet3Pt_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Eta_JetBin3_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Eta_JetBin3_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "Jet3Eta_JetBin3_baseline_withoutDeltaPhi" ) return Jet3Eta_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi1_JetBin3_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi2_JetBin3_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi3_JetBin3_baseline_withoutDeltaPhi") return DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_sel;
   
   if( type == "HT_JetBin4_baseline_withoutDeltaPhi") return HT_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "MHT_JetBin4_baseline_withoutDeltaPhi") return MHT_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Pt_JetBin4_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Pt_JetBin4_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "Jet3Pt_JetBin4_baseline_withoutDeltaPhi" ) return Jet3Pt_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "Jet1Eta_JetBin4_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "Jet2Eta_JetBin4_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "Jet3Eta_JetBin4_baseline_withoutDeltaPhi" ) return Jet3Eta_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi1_JetBin4_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi2_JetBin4_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_sel;
   if( type == "DeltaPhi3_JetBin4_baseline_withoutDeltaPhi") return DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_sel;
   
   if ( type == "NJets_baseline_withoutMHT") return NJets_baseline_withoutMHT_sel;
   if ( type == "NJets_baseline")         return NJets_baseline_sel;
   if ( type == "NJets_baseline_withoutDeltaPhi_withoutMHT") return NJets_baseline_withoutDeltaPhi_withoutMHT_sel;
   if ( type == "NJets_baseline_withoutDeltaPhi") return NJets_baseline_withoutDeltaPhi_sel;
   
   else { cout << "Error: No valid hist type" << endl;
      return dummy;
   }
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
TH1F* Prediction::GetPredictionHisto(TString type) {
   
   if ( type == "HT_presel") return HT_presel_pred;
   if ( type == "MHT_presel") return MHT_presel_pred;
   if ( type == "NJets_presel") return NJets_presel_pred;
   if ( type == "Jet1Pt_presel") return Jet1Pt_presel_pred;
   if ( type == "Jet2Pt_presel") return Jet2Pt_presel_pred;
   if ( type == "Jet3Pt_presel") return Jet3Pt_presel_pred;
   if ( type == "Jet1Eta_presel") return Jet1Eta_presel_pred;
   if ( type == "Jet2Eta_presel") return Jet2Eta_presel_pred;
   if ( type == "Jet3Eta_presel") return Jet3Eta_presel_pred;
   if ( type == "DeltaPhi1_presel") return DeltaPhi1_presel_pred;
   if ( type == "DeltaPhi2_presel") return DeltaPhi2_presel_pred;
   if ( type == "DeltaPhi3_presel") return DeltaPhi3_presel_pred;
   
   if ( type == "HT_deltaPhi") return HT_deltaPhi_pred;
   if ( type == "MHT_deltaPhi") return MHT_deltaPhi_pred;
   if ( type == "Jet1Pt_deltaPhi") return Jet1Pt_deltaPhi_pred;
   if ( type == "Jet2Pt_deltaPhi") return Jet2Pt_deltaPhi_pred;
   if ( type == "Jet3Pt_deltaPhi") return Jet3Pt_deltaPhi_pred;
   if ( type == "Jet1Eta_deltaPhi") return Jet1Eta_deltaPhi_pred;
   if ( type == "Jet2Eta_deltaPhi") return Jet2Eta_deltaPhi_pred;
   if ( type == "Jet3Eta_deltaPhi") return Jet3Eta_deltaPhi_pred;
   
   if ( type == "MHT_JetBin1_HTinclusive") return MHT_JetBin1_HTinclusive_pred;
   if ( type == "MHT_JetBin2_HTinclusive") return MHT_JetBin2_HTinclusive_pred;
   if ( type == "MHT_JetBin3_HTinclusive") return MHT_JetBin3_HTinclusive_pred;
   if ( type == "MHT_JetBin4_HTinclusive") return MHT_JetBin4_HTinclusive_pred;
   
   if ( type == "HT_baseline") return HT_baseline_pred;
   if ( type == "MHT_baseline") return MHT_baseline_pred;
   
   if( type == "Jet1Pt_JetBin1_baseline" ) return Jet1Pt_JetBin1_baseline_pred;
   if( type == "Jet2Pt_JetBin1_baseline" ) return Jet2Pt_JetBin1_baseline_pred;
   if( type == "Jet1Eta_JetBin1_baseline" ) return Jet1Eta_JetBin1_baseline_pred;
   if( type == "Jet2Eta_JetBin1_baseline" ) return Jet2Eta_JetBin1_baseline_pred;
   if( type == "DeltaPhi1_JetBin1_baseline") return DeltaPhi1_JetBin1_baseline_pred;
   if( type == "DeltaPhi2_JetBin1_baseline") return DeltaPhi2_JetBin1_baseline_pred;
   
   if( type == "Jet1Pt_JetBin2_baseline" ) return Jet1Pt_JetBin2_baseline_pred;
   if( type == "Jet2Pt_JetBin2_baseline" ) return Jet2Pt_JetBin2_baseline_pred;
   if( type == "Jet3Pt_JetBin2_baseline" ) return Jet3Pt_JetBin2_baseline_pred;
   if( type == "Jet1Eta_JetBin2_baseline" ) return Jet1Eta_JetBin2_baseline_pred;
   if( type == "Jet2Eta_JetBin2_baseline" ) return Jet2Eta_JetBin2_baseline_pred;
   if( type == "Jet3Eta_JetBin2_baseline" ) return Jet3Eta_JetBin2_baseline_pred;
   if( type == "DeltaPhi1_JetBin2_baseline") return DeltaPhi1_JetBin2_baseline_pred;
   if( type == "DeltaPhi2_JetBin2_baseline") return DeltaPhi2_JetBin2_baseline_pred;
   if( type == "DeltaPhi3_JetBin2_baseline") return DeltaPhi3_JetBin2_baseline_pred;
   
   if( type == "Jet1Pt_JetBin3_baseline" ) return Jet1Pt_JetBin3_baseline_pred;
   if( type == "Jet2Pt_JetBin3_baseline" ) return Jet2Pt_JetBin3_baseline_pred;
   if( type == "Jet3Pt_JetBin3_baseline" ) return Jet3Pt_JetBin3_baseline_pred;
   if( type == "Jet1Eta_JetBin3_baseline" ) return Jet1Eta_JetBin3_baseline_pred;
   if( type == "Jet2Eta_JetBin3_baseline" ) return Jet2Eta_JetBin3_baseline_pred;
   if( type == "Jet3Eta_JetBin3_baseline" ) return Jet3Eta_JetBin3_baseline_pred;
   if( type == "DeltaPhi1_JetBin3_baseline") return DeltaPhi1_JetBin3_baseline_pred;
   if( type == "DeltaPhi2_JetBin3_baseline") return DeltaPhi2_JetBin3_baseline_pred;
   if( type == "DeltaPhi3_JetBin3_baseline") return DeltaPhi3_JetBin3_baseline_pred;
   
   if( type == "Jet1Pt_JetBin4_baseline" ) return Jet1Pt_JetBin4_baseline_pred;
   if( type == "Jet2Pt_JetBin4_baseline" ) return Jet2Pt_JetBin4_baseline_pred;
   if( type == "Jet3Pt_JetBin4_baseline" ) return Jet3Pt_JetBin4_baseline_pred;
   if( type == "Jet1Eta_JetBin4_baseline" ) return Jet1Eta_JetBin4_baseline_pred;
   if( type == "Jet2Eta_JetBin4_baseline" ) return Jet2Eta_JetBin4_baseline_pred;
   if( type == "Jet3Eta_JetBin4_baseline" ) return Jet3Eta_JetBin4_baseline_pred;
   if( type == "DeltaPhi1_JetBin4_baseline") return DeltaPhi1_JetBin4_baseline_pred;
   if( type == "DeltaPhi2_JetBin4_baseline") return DeltaPhi2_JetBin4_baseline_pred;
   if( type == "DeltaPhi3_JetBin4_baseline") return DeltaPhi3_JetBin4_baseline_pred;
   
   if( type == "HT_JetBin1_baseline_withoutDeltaPhi") return HT_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "MHT_JetBin1_baseline_withoutDeltaPhi") return MHT_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Pt_JetBin1_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Pt_JetBin1_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Eta_JetBin1_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Eta_JetBin1_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi1_JetBin1_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin1_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi2_JetBin1_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin1_baseline_withoutDeltaPhi_pred;
   
   if( type == "HT_JetBin2_baseline_withoutDeltaPhi") return HT_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "MHT_JetBin2_baseline_withoutDeltaPhi") return MHT_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Pt_JetBin2_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Pt_JetBin2_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "Jet3Pt_JetBin2_baseline_withoutDeltaPhi" ) return Jet3Pt_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Eta_JetBin2_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Eta_JetBin2_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "Jet3Eta_JetBin2_baseline_withoutDeltaPhi" ) return Jet3Eta_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi1_JetBin2_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi2_JetBin2_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin2_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi3_JetBin2_baseline_withoutDeltaPhi") return DeltaPhi3_JetBin2_baseline_withoutDeltaPhi_pred;
   
   if( type == "HT_JetBin3_baseline_withoutDeltaPhi") return HT_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "MHT_JetBin3_baseline_withoutDeltaPhi") return MHT_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Pt_JetBin3_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Pt_JetBin3_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "Jet3Pt_JetBin3_baseline_withoutDeltaPhi" ) return Jet3Pt_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Eta_JetBin3_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Eta_JetBin3_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "Jet3Eta_JetBin3_baseline_withoutDeltaPhi" ) return Jet3Eta_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi1_JetBin3_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi2_JetBin3_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin3_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi3_JetBin3_baseline_withoutDeltaPhi") return DeltaPhi3_JetBin3_baseline_withoutDeltaPhi_pred;
   
   if( type == "HT_JetBin4_baseline_withoutDeltaPhi") return HT_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "MHT_JetBin4_baseline_withoutDeltaPhi") return MHT_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Pt_JetBin4_baseline_withoutDeltaPhi" ) return Jet1Pt_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Pt_JetBin4_baseline_withoutDeltaPhi" ) return Jet2Pt_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "Jet3Pt_JetBin4_baseline_withoutDeltaPhi" ) return Jet3Pt_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "Jet1Eta_JetBin4_baseline_withoutDeltaPhi" ) return Jet1Eta_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "Jet2Eta_JetBin4_baseline_withoutDeltaPhi" ) return Jet2Eta_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "Jet3Eta_JetBin4_baseline_withoutDeltaPhi" ) return Jet3Eta_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi1_JetBin4_baseline_withoutDeltaPhi") return DeltaPhi1_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi2_JetBin4_baseline_withoutDeltaPhi") return DeltaPhi2_JetBin4_baseline_withoutDeltaPhi_pred;
   if( type == "DeltaPhi3_JetBin4_baseline_withoutDeltaPhi") return DeltaPhi3_JetBin4_baseline_withoutDeltaPhi_pred;
   
   if ( type == "NJets_baseline_withoutMHT") return NJets_baseline_withoutMHT_pred;
   if ( type == "NJets_baseline") return NJets_baseline_pred;
   if ( type == "NJets_baseline_withoutDeltaPhi_withoutMHT") return NJets_baseline_withoutDeltaPhi_withoutMHT_pred;
   if ( type == "NJets_baseline_withoutDeltaPhi") return NJets_baseline_withoutDeltaPhi_pred;
   
   else { cout << "Error: No valid hist type" << endl;
      return dummy;
   }
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
double Prediction::GetResultValue(TH1F* histo, double MHTlow, double MHTup)
{
   double result_value;
   if( MHTlow == MHTup ) {
      result_value = histo->Integral(histo->FindBin(MHTlow),histo->GetNbinsX());
   }
   else result_value = histo->Integral(histo->FindBin(MHTlow), histo->FindBin(MHTup)-1);
   
   return result_value;
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
double Prediction::GetResultError(TH1F* histo, double MHTlow, double MHTup)
{
   double result_error;
   if( MHTlow == MHTup ) {
      histo->IntegralAndError(histo->FindBin(MHTlow),histo->GetNbinsX(), result_error);
   }
   else histo->IntegralAndError(histo->FindBin(MHTlow), histo->FindBin(MHTup)-1, result_error);
   
   return result_error;
}
////////////////////////////////////////////////////////////////////////////////////////


