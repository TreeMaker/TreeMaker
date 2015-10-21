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
#include <iomanip>
#include <vector>
#include <string>

#include "Prediction_WithUncertainties.h"

using namespace std;

Prediction_WithUncertainties::Prediction_WithUncertainties(TChain& QCDPrediction, TChain& RA2PreSelection, TString& Uncertainty)
{
   gROOT->ProcessLine("#include <vector>");

   // set search bin cut values for HT and MHT
   HTlow = 500.;
   HTmedium = 800.;
   HThigh = 1000.;
   HTveryhigh = 1250.;
   HTextremehigh = 1500.;
   MHTlow = 100.;
   MHTmedium = 200.;
   MHThigh = 300.;
   MHTveryhigh = 450.;
   MHTextremehigh = 600.;

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
   HT_presel_pred_raw = new TH2F("presel_HT_prediction" + Uncertainty, "presel_HT_prediction", NbinsHT, HTmin,
                                 HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_presel_pred_raw = new TH2F("presel_MHT_prediction" + Uncertainty, "presel_MHT_prediction", NbinsMHT, MHTmin,
                                  MHTmax, Ntries, 0.5, Ntries + 0.5);
   NJets_presel_pred_raw = new TH2F("NJets_presel_pred_raw" + Uncertainty, "NJets presel", 15, 0, 15, Ntries, 
                                                 0.5, Ntries + 0.5);
   Jet1Pt_presel_pred_raw = new TH2F("presel_Jet1_Pt_prediction" + Uncertainty, "presel_Jet1_Pt", NbinsJetPt, JetPtmin,
                                     JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_presel_pred_raw = new TH2F("presel_Jet2_Pt_prediction" + Uncertainty, "presel_Jet2_Pt", NbinsJetPt, JetPtmin,
                                     JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_presel_pred_raw = new TH2F("presel_Jet3_Pt_prediction" + Uncertainty, "presel_Jet3_Pt", NbinsJetPt, JetPtmin,
                                     JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_presel_pred_raw = new TH2F("presel_Jet1_Eta_prediction" + Uncertainty, "presel_Jet1_Eta", NbinsJetEta, 
                                      JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_presel_pred_raw = new TH2F("presel_Jet2_Eta_prediction" + Uncertainty, "presel_Jet2_Eta", NbinsJetEta,
                                      JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_presel_pred_raw = new TH2F("presel_Jet3_Eta_prediction" + Uncertainty, "presel_Jet3_Eta", NbinsJetEta, 
                                      JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);


   HT_presel_HThigh_pred_raw = new TH2F("presel_HT_HThigh_prediction" + Uncertainty, "presel_HT_prediction", NbinsHT, HTmin,
                                 HTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_presel_HThigh_pred_raw = new TH2F("presel_MHT_HThigh_prediction" + Uncertainty, "presel_MHT_prediction", NbinsMHT, MHTmin,
                                  MHTmax, Ntries, 0.5, Ntries + 0.5);
   NJets_presel_HThigh_pred_raw = new TH2F("NJets_presel_HThigh_pred_raw" + Uncertainty, "NJets presel", 15, 0, 15, Ntries, 
                                                 0.5, Ntries + 0.5);
   Jet1Pt_presel_HThigh_pred_raw = new TH2F("presel_Jet1_Pt_HThigh_prediction" + Uncertainty, "presel_Jet1_Pt", NbinsJetPt, JetPtmin,
                                     JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet2Pt_presel_HThigh_pred_raw = new TH2F("presel_Jet2_Pt_HThigh_prediction" + Uncertainty, "presel_Jet2_Pt", NbinsJetPt, JetPtmin,
                                     JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet3Pt_presel_HThigh_pred_raw = new TH2F("presel_Jet3_Pt_HThigh_prediction" + Uncertainty, "presel_Jet3_Pt", NbinsJetPt, JetPtmin,
                                     JetPtmax, Ntries, 0.5, Ntries + 0.5);
   Jet1Eta_presel_HThigh_pred_raw = new TH2F("presel_Jet1_Eta_HThigh_prediction" + Uncertainty, "presel_Jet1_Eta", NbinsJetEta, 
                                      JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet2Eta_presel_HThigh_pred_raw = new TH2F("presel_Jet2_Eta_HThigh_prediction" + Uncertainty, "presel_Jet2_Eta", NbinsJetEta,
                                      JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);
   Jet3Eta_presel_HThigh_pred_raw = new TH2F("presel_Jet3_Eta_HThigh_prediction" + Uncertainty, "presel_Jet3_Eta", NbinsJetEta, 
                                      JetEtamin, JetEtamax, Ntries, 0.5, Ntries + 0.5);

  
   MHT_JetBin1_HTlow_pred_raw = new TH2F("MHT_JetBin1_HTlow_pred" + Uncertainty, "MHT_JetBin1_HTlow_pred", NbinsMHT, 
                                         MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin1_HTmedium_pred_raw = new TH2F("MHT_JetBin1_HTmedium_pred" + Uncertainty, "MHT_JetBin1_HTmedium_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin1_HThigh_pred_raw = new TH2F("MHT_JetBin1_HThigh_pred" + Uncertainty, "MHT_JetBin1_HThigh_pred", NbinsMHT, 
                                          MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin1_HTveryhigh_pred_raw = new TH2F("MHT_JetBin1_HTveryhigh_pred" + Uncertainty, "MHT_JetBin1_HTveryhigh_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin1_HTextremehigh_pred_raw = new TH2F("MHT_JetBin1_HTextremehigh_pred" + Uncertainty, "MHT_JetBin1_HTextremehigh_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);

   MHT_JetBin2_HTlow_pred_raw = new TH2F("MHT_JetBin2_HTlow_pred" + Uncertainty, "MHT_JetBin2_HTlow_pred", NbinsMHT, 
                                         MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin2_HTmedium_pred_raw = new TH2F("MHT_JetBin2_HTmedium_pred" + Uncertainty, "MHT_JetBin2_HTmedium_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin2_HThigh_pred_raw = new TH2F("MHT_JetBin2_HThigh_pred" + Uncertainty, "MHT_JetBin2_HThigh_pred", NbinsMHT, 
                                          MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin2_HTveryhigh_pred_raw = new TH2F("MHT_JetBin2_HTveryhigh_pred" + Uncertainty, "MHT_JetBin2_HTveryhigh_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin2_HTextremehigh_pred_raw = new TH2F("MHT_JetBin2_HTextremehigh_pred" + Uncertainty, "MHT_JetBin2_HTextremehigh_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);

   MHT_JetBin3_HTlow_pred_raw = new TH2F("MHT_JetBin3_HTlow_pred" + Uncertainty, "MHT_JetBin3_HTlow_pred", NbinsMHT, 
                                         MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin3_HTmedium_pred_raw = new TH2F("MHT_JetBin3_HTmedium_pred" + Uncertainty, "MHT_JetBin3_HTmedium_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin3_HThigh_pred_raw = new TH2F("MHT_JetBin3_HThigh_pred" + Uncertainty, "MHT_JetBin3_HThigh_pred", NbinsMHT, 
                                          MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin3_HTveryhigh_pred_raw = new TH2F("MHT_JetBin3_HTveryhigh_pred" + Uncertainty, "MHT_JetBin3_HTveryhigh_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin3_HTextremehigh_pred_raw = new TH2F("MHT_JetBin3_HTextremehigh_pred" + Uncertainty, "MHT_JetBin3_HTextremehigh_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);

   MHT_JetBin4_HTlow_pred_raw = new TH2F("MHT_JetBin4_HTlow_pred" + Uncertainty, "MHT_JetBin4_HTlow_pred", NbinsMHT, 
                                         MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin4_HTmedium_pred_raw = new TH2F("MHT_JetBin4_HTmedium_pred" + Uncertainty, "MHT_JetBin4_HTmedium_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin4_HThigh_pred_raw = new TH2F("MHT_JetBin4_HThigh_pred" + Uncertainty, "MHT_JetBin4_HThigh_pred", NbinsMHT, 
                                          MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin4_HTveryhigh_pred_raw = new TH2F("MHT_JetBin4_HTveryhigh_pred" + Uncertainty, "MHT_JetBin4_HTveryhigh_pred",
                                            NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);
   MHT_JetBin4_HTextremehigh_pred_raw = new TH2F("MHT_JetBin4_HTextremehigh_pred" + Uncertainty, "MHT_JetBin4_HTextremehigh_pred", NbinsMHT, MHTmin, MHTmax, Ntries, 0.5, Ntries + 0.5);

   // ------------------------------------------------------------------------------ //
   // define selection histograms
   HT_presel_sel = new TH1F("presel_HT_selection" + Uncertainty, "presel_HT_selection", NbinsHT, HTmin, HTmax);
   MHT_presel_sel = new TH1F("presel_MHT_selection" + Uncertainty, "presel_MHT_selection", NbinsMHT, MHTmin, MHTmax);
   NJets_presel_sel = new TH1F("NJets_presel_sel" + Uncertainty, "NJets presel", 15, 0, 15);
   Jet1Pt_presel_sel = new TH1F("presel_Jet1_Pt_selection" + Uncertainty, "presel_Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_presel_sel = new TH1F("presel_Jet2_Pt_selection" + Uncertainty, "presel_Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_presel_sel = new TH1F("presel_Jet3_Pt_selection" + Uncertainty, "presel_Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_presel_sel = new TH1F("presel_Jet1_Eta_selection" + Uncertainty, "presel_Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_presel_sel = new TH1F("presel_Jet2_Eta_selection" + Uncertainty, "presel_Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_presel_sel = new TH1F("presel_Jet3_Eta_selection" + Uncertainty, "presel_Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);

   HT_presel_HThigh_sel = new TH1F("presel_HT_HThigh_selection" + Uncertainty, "presel_HT_selection", NbinsHT, HTmin, HTmax);
   MHT_presel_HThigh_sel = new TH1F("presel_MHT_HThigh_selection" + Uncertainty, "presel_MHT_selection", NbinsMHT, MHTmin, MHTmax);
   NJets_presel_HThigh_sel = new TH1F("NJets_presel_HThigh_sel" + Uncertainty, "NJets presel", 15, 0, 15);
   Jet1Pt_presel_HThigh_sel = new TH1F("presel_Jet1_Pt_HThigh_selection" + Uncertainty, "presel_Jet1_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet2Pt_presel_HThigh_sel = new TH1F("presel_Jet2_Pt_HThigh_selection" + Uncertainty, "presel_Jet2_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet3Pt_presel_HThigh_sel = new TH1F("presel_Jet3_Pt_HThigh_selection" + Uncertainty, "presel_Jet3_Pt", NbinsJetPt, JetPtmin, JetPtmax);
   Jet1Eta_presel_HThigh_sel = new TH1F("presel_Jet1_Eta_HThigh_selection" + Uncertainty, "presel_Jet1_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet2Eta_presel_HThigh_sel = new TH1F("presel_Jet2_Eta_HThigh_selection" + Uncertainty, "presel_Jet2_Eta", NbinsJetEta, JetEtamin, JetEtamax);
   Jet3Eta_presel_HThigh_sel = new TH1F("presel_Jet3_Eta_HThigh_selection" + Uncertainty, "presel_Jet3_Eta", NbinsJetEta, JetEtamin, JetEtamax);

  
   MHT_JetBin1_HTlow_sel = new TH1F("MHT_JetBin1_HTlow_sel" + Uncertainty, "MHT_JetBin1_HTlow_sel", NbinsMHT,
                                    MHTmin, MHTmax);
   MHT_JetBin1_HTmedium_sel = new TH1F("MHT_JetBin1_HTmedium_sel" + Uncertainty, "MHT_JetBin1_HTmedium_sel",
                                       NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin1_HThigh_sel = new TH1F("MHT_JetBin1_HThigh_sel" + Uncertainty, "MHT_JetBin1_HThigh_sel", NbinsMHT, 
                                     MHTmin, MHTmax);
   MHT_JetBin1_HTveryhigh_sel = new TH1F("MHT_JetBin1_HTveryhigh_sel" + Uncertainty, "MHT_JetBin1_HTveryhigh_sel", 
                                         NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin1_HTextremehigh_sel = new TH1F("MHT_JetBin1_HTextremehigh_sel" + Uncertainty, "MHT_JetBin1_HTextremehigh_sel",
                                            NbinsMHT, MHTmin, MHTmax);

   MHT_JetBin2_HTlow_sel = new TH1F("MHT_JetBin2_HTlow_sel" + Uncertainty, "MHT_JetBin2_HTlow_sel", NbinsMHT, 
                                    MHTmin, MHTmax);
   MHT_JetBin2_HTmedium_sel = new TH1F("MHT_JetBin2_HTmedium_sel" + Uncertainty, "MHT_JetBin2_HTmedium_sel",
                                       NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin2_HThigh_sel = new TH1F("MHT_JetBin2_HThigh_sel" + Uncertainty, "MHT_JetBin2_HThigh_sel", NbinsMHT, 
                                     MHTmin, MHTmax);
   MHT_JetBin2_HTveryhigh_sel = new TH1F("MHT_JetBin2_HTveryhigh_sel" + Uncertainty, "MHT_JetBin2_HTveryhigh_sel", 
                                         NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin2_HTextremehigh_sel = new TH1F("MHT_JetBin2_HTextremehigh_sel" + Uncertainty, "MHT_JetBin2_HTextremehigh_sel",
                                            NbinsMHT, MHTmin, MHTmax);

   MHT_JetBin3_HTlow_sel = new TH1F("MHT_JetBin3_HTlow_sel" + Uncertainty, "MHT_JetBin3_HTlow_sel", NbinsMHT, 
                                    MHTmin, MHTmax);
   MHT_JetBin3_HTmedium_sel = new TH1F("MHT_JetBin3_HTmedium_sel" + Uncertainty, "MHT_JetBin3_HTmedium_sel",
                                       NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin3_HThigh_sel = new TH1F("MHT_JetBin3_HThigh_sel" + Uncertainty, "MHT_JetBin3_HThigh_sel", NbinsMHT, 
                                     MHTmin, MHTmax);
   MHT_JetBin3_HTveryhigh_sel = new TH1F("MHT_JetBin3_HTveryhigh_sel" + Uncertainty, "MHT_JetBin3_HTveryhigh_sel", 
                                         NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin3_HTextremehigh_sel = new TH1F("MHT_JetBin3_HTextremehigh_sel" + Uncertainty, "MHT_JetBin3_HTextremehigh_sel",
                                            NbinsMHT, MHTmin, MHTmax);

   MHT_JetBin4_HTlow_sel = new TH1F("MHT_JetBin4_HTlow_sel" + Uncertainty, "MHT_JetBin4_HTlow_sel", NbinsMHT, 
                                    MHTmin, MHTmax);
   MHT_JetBin4_HTmedium_sel = new TH1F("MHT_JetBin4_HTmedium_sel" + Uncertainty, "MHT_JetBin4_HTmedium_sel",
                                       NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin4_HThigh_sel = new TH1F("MHT_JetBin4_HThigh_sel" + Uncertainty, "MHT_JetBin4_HThigh_sel", NbinsMHT, 
                                     MHTmin, MHTmax);
   MHT_JetBin4_HTveryhigh_sel = new TH1F("MHT_JetBin4_HTveryhigh_sel" + Uncertainty, "MHT_JetBin4_HTveryhigh_sel", 
                                         NbinsMHT, MHTmin, MHTmax);
   MHT_JetBin4_HTextremehigh_sel = new TH1F("MHT_JetBin4_HTextremehigh_sel" + Uncertainty, "MHT_JetBin4_HTextremehigh_sel",
                                            NbinsMHT, MHTmin, MHTmax);

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
     
   QCDPrediction.SetBranchAddress("NVtx",&vtxN);
   QCDPrediction.SetBranchAddress("NJets",&NJets);
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

   // loop over entries and fill prediction histos
   ULong_t nentries = QCDPrediction.GetEntries();
   //Int_t nentries = 10000000;
   for ( ULong_t i = 0 ; i<nentries ; i++) {
      QCDPrediction.GetEntry(i);

      if( i%1000000 == 0 ) std::cout << "event (prediction): " << i << '\n';

      // select reasonable event weights
      if( weight < 30000. ) {
      
         // apply same HT cut as on selection
         if( HT > 350. ) {

            // ------------------------------------------------------------- //
            // fill data control plot histos
            if( !DeltaPhiCut_prediction() && NJets >= 3 ) {
               if( HT > 500 && HT < 1000) {
                  HT_presel_pred_raw->Fill(HT, NSmear, weight); 
                  MHT_presel_pred_raw->Fill(MHT, NSmear, weight); 
                  NJets_presel_pred_raw->Fill(NJets, NSmear, weight);
                  Jet1Pt_presel_pred_raw->Fill(Jet1Pt, NSmear, weight);
                  Jet2Pt_presel_pred_raw->Fill(Jet2Pt, NSmear, weight); 
                  Jet3Pt_presel_pred_raw->Fill(Jet3Pt, NSmear, weight); 
                  Jet1Eta_presel_pred_raw->Fill(Jet1Eta, NSmear, weight); 
                  Jet2Eta_presel_pred_raw->Fill(Jet2Eta, NSmear, weight); 
                  Jet3Eta_presel_pred_raw->Fill(Jet3Eta, NSmear, weight); 
               }
               if( HT >= 1000 ) {
                  HT_presel_HThigh_pred_raw->Fill(HT, NSmear, weight); 
                  MHT_presel_HThigh_pred_raw->Fill(MHT, NSmear, weight); 
                  NJets_presel_HThigh_pred_raw->Fill(NJets, NSmear, weight);
                  Jet1Pt_presel_HThigh_pred_raw->Fill(Jet1Pt, NSmear, weight);
                  Jet2Pt_presel_HThigh_pred_raw->Fill(Jet2Pt, NSmear, weight); 
                  Jet3Pt_presel_HThigh_pred_raw->Fill(Jet3Pt, NSmear, weight); 
                  Jet1Eta_presel_HThigh_pred_raw->Fill(Jet1Eta, NSmear, weight); 
                  Jet2Eta_presel_HThigh_pred_raw->Fill(Jet2Eta, NSmear, weight); 
                  Jet3Eta_presel_HThigh_pred_raw->Fill(Jet3Eta, NSmear, weight); 
               }
            }
             
            // ------------------------------------------------------------- //
            // check deltaPhi cut
            if( DeltaPhiCut_prediction() ) { 
         
               //  fill different jet multiplicity bins
               // jet bin 1
               if( NJets == 2 ) {
                  if( HTlow < HT && HT < HTmedium ) {
                     MHT_JetBin1_HTlow_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTmedium < HT && HT < HThigh ) {
                     MHT_JetBin1_HTmedium_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HThigh < HT && HT < HTveryhigh ) {
                     MHT_JetBin1_HThigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTveryhigh < HT && HT < HTextremehigh ) {
                     MHT_JetBin1_HTveryhigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTextremehigh <= HT ) {
                     MHT_JetBin1_HTextremehigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
               }

               // jet bin 2
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  if( HTlow < HT && HT < HTmedium ) {
                     MHT_JetBin2_HTlow_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTmedium < HT && HT < HThigh ) {
                     MHT_JetBin2_HTmedium_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HThigh < HT && HT < HTveryhigh ) {
                     MHT_JetBin2_HThigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTveryhigh < HT && HT < HTextremehigh ) {
                     MHT_JetBin2_HTveryhigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTextremehigh <= HT ) {
                     MHT_JetBin2_HTextremehigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
               }
               // jet bin 3            
               else if(  NJets == 6  ||  NJets == 7 ) {
                  if( HTlow < HT && HT < HTmedium ) {
                     MHT_JetBin3_HTlow_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTmedium < HT && HT < HThigh ) {
                     MHT_JetBin3_HTmedium_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HThigh < HT && HT < HTveryhigh ) {
                     MHT_JetBin3_HThigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTveryhigh < HT && HT < HTextremehigh ) {
                     MHT_JetBin3_HTveryhigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTextremehigh <= HT ) {
                     MHT_JetBin3_HTextremehigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
               }    
               // jet bin 4 
               else if(  NJets >= 8 ) {
                  if( HTlow < HT && HT < HTmedium ) {
                     MHT_JetBin4_HTlow_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTmedium < HT && HT < HThigh ) {
                     MHT_JetBin4_HTmedium_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HThigh < HT && HT < HTveryhigh ) {
                     MHT_JetBin4_HThigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTveryhigh < HT && HT < HTextremehigh ) {
                     MHT_JetBin4_HTveryhigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
                  else if( HTextremehigh <= HT ) {
                     MHT_JetBin4_HTextremehigh_pred_raw->Fill(MHT, NSmear, weight);
                  }
               }      
            }    
         }
      }
   } 
 
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
   weight_RA2 = 0;
   DeltaPhi1_RA2 = 0;
   DeltaPhi2_RA2 = 0;
   DeltaPhi3_RA2 = 0;
     
   RA2PreSelection.SetBranchAddress("NVtx",&vtxN_RA2);
   RA2PreSelection.SetBranchAddress("NJets",&NJets_RA2);
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
               // fill data control plot histos
               if( !DeltaPhiCut_selection() && NJets_RA2 >= 3 ) {
                  if( HT_RA2 > 500 && HT_RA2 < 1000 & MHT_RA2 > 100) {
                     HT_presel_sel->Fill(HT_RA2, weight_RA2); 
                     MHT_presel_sel->Fill(MHT_RA2, weight_RA2); 
                     NJets_presel_sel->Fill(NJets_RA2, weight_RA2);
                     Jet1Pt_presel_sel->Fill(Jet1Pt_RA2, weight_RA2); 
                     Jet2Pt_presel_sel->Fill(Jet2Pt_RA2, weight_RA2); 
                     Jet3Pt_presel_sel->Fill(Jet3Pt_RA2, weight_RA2); 
                     Jet1Eta_presel_sel->Fill(Jet1Eta_RA2, weight_RA2); 
                     Jet2Eta_presel_sel->Fill(Jet2Eta_RA2, weight_RA2); 
                     Jet3Eta_presel_sel->Fill(Jet3Eta_RA2, weight_RA2);
                  }
                  if( HT_RA2 >= 1000 & MHT_RA2 > 100) {
                     HT_presel_HThigh_sel->Fill(HT_RA2, weight_RA2); 
                     MHT_presel_HThigh_sel->Fill(MHT_RA2, weight_RA2); 
                     NJets_presel_HThigh_sel->Fill(NJets_RA2, weight_RA2);
                     Jet1Pt_presel_HThigh_sel->Fill(Jet1Pt_RA2, weight_RA2); 
                     Jet2Pt_presel_HThigh_sel->Fill(Jet2Pt_RA2, weight_RA2); 
                     Jet3Pt_presel_HThigh_sel->Fill(Jet3Pt_RA2, weight_RA2); 
                     Jet1Eta_presel_HThigh_sel->Fill(Jet1Eta_RA2, weight_RA2); 
                     Jet2Eta_presel_HThigh_sel->Fill(Jet2Eta_RA2, weight_RA2); 
                     Jet3Eta_presel_HThigh_sel->Fill(Jet3Eta_RA2, weight_RA2);
                  }

               } 
               // ------------------------------------------------------------- //

               // check deltaPhi Cut
               if( DeltaPhiCut_selection() ) {    
         
                  //  fill different jet multiplicity bins
                  // jet bin 1
                  if( NJets_RA2 == 2 ) {
                     if( HTlow < HT_RA2 && HT_RA2 < HTmedium ) {
                        MHT_JetBin1_HTlow_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTmedium < HT_RA2 && HT_RA2 < HThigh ) {
                        MHT_JetBin1_HTmedium_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HThigh < HT_RA2 && HT_RA2 < HTveryhigh ) {
                        MHT_JetBin1_HThigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTveryhigh < HT_RA2 && HT_RA2 < HTextremehigh ) {
                        MHT_JetBin1_HTveryhigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTextremehigh <= HT_RA2 ) {
                        MHT_JetBin1_HTextremehigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                  }
                  // jet bin 2
                  else if( NJets_RA2 == 3 || NJets_RA2 == 4 ||  NJets_RA2 == 5 ) {
                     if( HTlow < HT_RA2 && HT_RA2 < HTmedium ) {
                        MHT_JetBin2_HTlow_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTmedium < HT_RA2 && HT_RA2 < HThigh ) {
                        MHT_JetBin2_HTmedium_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HThigh < HT_RA2 && HT_RA2 < HTveryhigh ) {
                        MHT_JetBin2_HThigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTveryhigh < HT_RA2 && HT_RA2 < HTextremehigh ) {
                        MHT_JetBin2_HTveryhigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTextremehigh <= HT_RA2 ) {
                        MHT_JetBin2_HTextremehigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                  }
                  // jet bin 3            
                  else if(  NJets_RA2 == 6  ||  NJets_RA2 == 7 ) {
                     if( HTlow < HT_RA2 && HT_RA2 < HTmedium ) {
                        MHT_JetBin3_HTlow_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTmedium < HT_RA2 && HT_RA2 < HThigh ) {
                        MHT_JetBin3_HTmedium_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HThigh < HT_RA2 && HT_RA2 < HTveryhigh ) {
                        MHT_JetBin3_HThigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTveryhigh < HT_RA2 && HT_RA2 < HTextremehigh ) {
                        MHT_JetBin3_HTveryhigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTextremehigh <= HT_RA2 ) {
                        MHT_JetBin3_HTextremehigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                  }    
                  // jet bin 4 
                  else if(  NJets_RA2 >= 8 ) {
                     if( HTlow < HT_RA2 && HT_RA2 < HTmedium ) {
                        MHT_JetBin4_HTlow_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTmedium < HT_RA2 && HT_RA2 < HThigh ) {
                        MHT_JetBin4_HTmedium_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HThigh < HT_RA2 && HT_RA2 < HTveryhigh ) {
                        MHT_JetBin4_HThigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTveryhigh < HT_RA2 && HT_RA2 < HTextremehigh ) {
                        MHT_JetBin4_HTveryhigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                     else if( HTextremehigh <= HT_RA2 ) {
                        MHT_JetBin4_HTextremehigh_sel->Fill(MHT_RA2, weight_RA2);
                     }
                  }
               }    
            }
         }
      }
   //  }

   //----------------------------------------------------------//

   //----------------------------------------------------------//
   // rebin histos
   DoRebinning(HT_presel_pred_raw, HT_presel_sel , -1);
   DoRebinning(MHT_presel_pred_raw, MHT_presel_sel , -2);
   DoRebinning(Jet1Pt_presel_pred_raw, Jet1Pt_presel_sel , 10);
   DoRebinning(Jet2Pt_presel_pred_raw, Jet2Pt_presel_sel , 10);
   DoRebinning(Jet3Pt_presel_pred_raw, Jet3Pt_presel_sel , 10);
   DoRebinning(Jet1Eta_presel_pred_raw, Jet1Eta_presel_sel , 2);
   DoRebinning(Jet2Eta_presel_pred_raw, Jet2Eta_presel_sel , 2);
   DoRebinning(Jet3Eta_presel_pred_raw, Jet3Eta_presel_sel , 2);

   DoRebinning(HT_presel_HThigh_pred_raw, HT_presel_HThigh_sel , -1);
   DoRebinning(MHT_presel_HThigh_pred_raw, MHT_presel_HThigh_sel , -2);
   DoRebinning(Jet1Pt_presel_HThigh_pred_raw, Jet1Pt_presel_HThigh_sel , 10);
   DoRebinning(Jet2Pt_presel_HThigh_pred_raw, Jet2Pt_presel_HThigh_sel , 10);
   DoRebinning(Jet3Pt_presel_HThigh_pred_raw, Jet3Pt_presel_HThigh_sel , 10);
   DoRebinning(Jet1Eta_presel_HThigh_pred_raw, Jet1Eta_presel_HThigh_sel , 2);
   DoRebinning(Jet2Eta_presel_HThigh_pred_raw, Jet2Eta_presel_HThigh_sel , 2);
   DoRebinning(Jet3Eta_presel_HThigh_pred_raw, Jet3Eta_presel_HThigh_sel , 2);

   DoRebinning(MHT_JetBin1_HTlow_pred_raw, MHT_JetBin1_HTlow_sel , -2);
   DoRebinning(MHT_JetBin1_HTmedium_pred_raw, MHT_JetBin1_HTmedium_sel , -2);
   DoRebinning(MHT_JetBin1_HThigh_pred_raw, MHT_JetBin1_HThigh_sel , -2);
   DoRebinning(MHT_JetBin1_HTveryhigh_pred_raw, MHT_JetBin1_HTveryhigh_sel , -2);
   DoRebinning(MHT_JetBin1_HTextremehigh_pred_raw, MHT_JetBin1_HTextremehigh_sel , -2);

   DoRebinning(MHT_JetBin2_HTlow_pred_raw, MHT_JetBin2_HTlow_sel , -2);
   DoRebinning(MHT_JetBin2_HTmedium_pred_raw, MHT_JetBin2_HTmedium_sel , -2);
   DoRebinning(MHT_JetBin2_HThigh_pred_raw, MHT_JetBin2_HThigh_sel , -2);
   DoRebinning(MHT_JetBin2_HTveryhigh_pred_raw, MHT_JetBin2_HTveryhigh_sel , -2);
   DoRebinning(MHT_JetBin2_HTextremehigh_pred_raw, MHT_JetBin2_HTextremehigh_sel , -2);

   DoRebinning(MHT_JetBin3_HTlow_pred_raw, MHT_JetBin3_HTlow_sel , -2);
   DoRebinning(MHT_JetBin3_HTmedium_pred_raw, MHT_JetBin3_HTmedium_sel , -2);
   DoRebinning(MHT_JetBin3_HThigh_pred_raw, MHT_JetBin3_HThigh_sel , -2);
   DoRebinning(MHT_JetBin3_HTveryhigh_pred_raw, MHT_JetBin3_HTveryhigh_sel , -2);
   DoRebinning(MHT_JetBin3_HTextremehigh_pred_raw, MHT_JetBin3_HTextremehigh_sel , -2);

   DoRebinning(MHT_JetBin4_HTlow_pred_raw, MHT_JetBin4_HTlow_sel , -2);
   DoRebinning(MHT_JetBin4_HTmedium_pred_raw, MHT_JetBin4_HTmedium_sel , -2);
   DoRebinning(MHT_JetBin4_HThigh_pred_raw, MHT_JetBin4_HThigh_sel , -2);
   DoRebinning(MHT_JetBin4_HTveryhigh_pred_raw, MHT_JetBin4_HTveryhigh_sel , -2);
   DoRebinning(MHT_JetBin4_HTextremehigh_pred_raw, MHT_JetBin4_HTextremehigh_sel , -2);
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

   HT_presel_HThigh_pred = CalcPrediction(HT_presel_HThigh_pred_raw);
   MHT_presel_HThigh_pred = CalcPrediction(MHT_presel_HThigh_pred_raw);
   NJets_presel_HThigh_pred = CalcPrediction(NJets_presel_HThigh_pred_raw);
   Jet1Pt_presel_HThigh_pred = CalcPrediction(Jet1Pt_presel_HThigh_pred_raw);
   Jet2Pt_presel_HThigh_pred = CalcPrediction(Jet2Pt_presel_HThigh_pred_raw);
   Jet3Pt_presel_HThigh_pred = CalcPrediction(Jet3Pt_presel_HThigh_pred_raw);
   Jet1Eta_presel_HThigh_pred = CalcPrediction(Jet1Eta_presel_HThigh_pred_raw);
   Jet2Eta_presel_HThigh_pred = CalcPrediction(Jet2Eta_presel_HThigh_pred_raw);
   Jet3Eta_presel_HThigh_pred = CalcPrediction(Jet3Eta_presel_HThigh_pred_raw);

   MHT_JetBin1_HTlow_pred = CalcPrediction(MHT_JetBin1_HTlow_pred_raw);
   MHT_JetBin1_HTmedium_pred = CalcPrediction(MHT_JetBin1_HTmedium_pred_raw);
   MHT_JetBin1_HThigh_pred = CalcPrediction(MHT_JetBin1_HThigh_pred_raw);
   MHT_JetBin1_HTveryhigh_pred = CalcPrediction(MHT_JetBin1_HTveryhigh_pred_raw);
   MHT_JetBin1_HTextremehigh_pred = CalcPrediction(MHT_JetBin1_HTextremehigh_pred_raw);

   MHT_JetBin2_HTlow_pred = CalcPrediction(MHT_JetBin2_HTlow_pred_raw);
   MHT_JetBin2_HTmedium_pred = CalcPrediction(MHT_JetBin2_HTmedium_pred_raw);
   MHT_JetBin2_HThigh_pred = CalcPrediction(MHT_JetBin2_HThigh_pred_raw);
   MHT_JetBin2_HTveryhigh_pred = CalcPrediction(MHT_JetBin2_HTveryhigh_pred_raw);
   MHT_JetBin2_HTextremehigh_pred = CalcPrediction(MHT_JetBin2_HTextremehigh_pred_raw);

   MHT_JetBin3_HTlow_pred = CalcPrediction(MHT_JetBin3_HTlow_pred_raw);
   MHT_JetBin3_HTmedium_pred = CalcPrediction(MHT_JetBin3_HTmedium_pred_raw);
   MHT_JetBin3_HThigh_pred = CalcPrediction(MHT_JetBin3_HThigh_pred_raw);
   MHT_JetBin3_HTveryhigh_pred = CalcPrediction(MHT_JetBin3_HTveryhigh_pred_raw);
   MHT_JetBin3_HTextremehigh_pred = CalcPrediction(MHT_JetBin3_HTextremehigh_pred_raw);

   MHT_JetBin4_HTlow_pred = CalcPrediction(MHT_JetBin4_HTlow_pred_raw);
   MHT_JetBin4_HTmedium_pred = CalcPrediction(MHT_JetBin4_HTmedium_pred_raw);
   MHT_JetBin4_HThigh_pred = CalcPrediction(MHT_JetBin4_HThigh_pred_raw);
   MHT_JetBin4_HTveryhigh_pred = CalcPrediction(MHT_JetBin4_HTveryhigh_pred_raw);
   MHT_JetBin4_HTextremehigh_pred = CalcPrediction(MHT_JetBin4_HTextremehigh_pred_raw);
   //----------------------------------------------------------//

   //----------------------------------------------------------//
   // write histos to file
   TFile* prediction_histos = new TFile("output_GetPrediction_WithUncertainties/prediction_histos" + Uncertainty + ".root", "RECREATE");
   HT_presel_pred->Write();
   MHT_presel_pred->Write();
   NJets_presel_pred->Write();
   Jet1Pt_presel_pred->Write();
   Jet2Pt_presel_pred->Write();
   Jet3Pt_presel_pred->Write();
   Jet1Eta_presel_pred->Write();
   Jet2Eta_presel_pred->Write();
   Jet3Eta_presel_pred->Write();

   HT_presel_HThigh_pred->Write();
   MHT_presel_HThigh_pred->Write();
   NJets_presel_HThigh_pred->Write();
   Jet1Pt_presel_HThigh_pred->Write();
   Jet2Pt_presel_HThigh_pred->Write();
   Jet3Pt_presel_HThigh_pred->Write();
   Jet1Eta_presel_HThigh_pred->Write();
   Jet2Eta_presel_HThigh_pred->Write();
   Jet3Eta_presel_HThigh_pred->Write();
  
   MHT_JetBin1_HTlow_pred->Write();
   MHT_JetBin1_HTmedium_pred->Write();
   MHT_JetBin1_HThigh_pred->Write();
   MHT_JetBin1_HTveryhigh_pred->Write();
   MHT_JetBin1_HTextremehigh_pred->Write();
   MHT_JetBin2_HTlow_pred->Write();
   MHT_JetBin2_HTmedium_pred->Write();
   MHT_JetBin2_HThigh_pred->Write();
   MHT_JetBin2_HTveryhigh_pred->Write();
   MHT_JetBin2_HTextremehigh_pred->Write();
   MHT_JetBin3_HTlow_pred->Write();
   MHT_JetBin3_HTmedium_pred->Write();
   MHT_JetBin3_HThigh_pred->Write();
   MHT_JetBin3_HTveryhigh_pred->Write();
   MHT_JetBin3_HTextremehigh_pred->Write();
   MHT_JetBin4_HTlow_pred->Write();
   MHT_JetBin4_HTmedium_pred->Write();
   MHT_JetBin4_HThigh_pred->Write();
   MHT_JetBin4_HTveryhigh_pred->Write();
   MHT_JetBin4_HTextremehigh_pred->Write();
 
   HT_presel_sel->Write();
   MHT_presel_sel->Write();
   NJets_presel_sel->Write();
   Jet1Pt_presel_sel->Write();
   Jet2Pt_presel_sel->Write();
   Jet3Pt_presel_sel->Write();
   Jet1Eta_presel_sel->Write();
   Jet2Eta_presel_sel->Write();
   Jet3Eta_presel_sel->Write();

   HT_presel_HThigh_sel->Write();
   MHT_presel_HThigh_sel->Write();
   NJets_presel_HThigh_sel->Write();
   Jet1Pt_presel_HThigh_sel->Write();
   Jet2Pt_presel_HThigh_sel->Write();
   Jet3Pt_presel_HThigh_sel->Write();
   Jet1Eta_presel_HThigh_sel->Write();
   Jet2Eta_presel_HThigh_sel->Write();
   Jet3Eta_presel_HThigh_sel->Write();
 
   MHT_JetBin1_HTlow_sel->Write();
   MHT_JetBin1_HTmedium_sel->Write();
   MHT_JetBin1_HThigh_sel->Write();
   MHT_JetBin1_HTveryhigh_sel->Write();
   MHT_JetBin1_HTextremehigh_sel->Write();
   MHT_JetBin2_HTlow_sel->Write();
   MHT_JetBin2_HTmedium_sel->Write();
   MHT_JetBin2_HThigh_sel->Write();
   MHT_JetBin2_HTveryhigh_sel->Write();
   MHT_JetBin2_HTextremehigh_sel->Write();
   MHT_JetBin3_HTlow_sel->Write();
   MHT_JetBin3_HTmedium_sel->Write();
   MHT_JetBin3_HThigh_sel->Write();
   MHT_JetBin3_HTveryhigh_sel->Write();
   MHT_JetBin3_HTextremehigh_sel->Write();
   MHT_JetBin4_HTlow_sel->Write();
   MHT_JetBin4_HTmedium_sel->Write();
   MHT_JetBin4_HThigh_sel->Write();
   MHT_JetBin4_HTveryhigh_sel->Write();
   MHT_JetBin4_HTextremehigh_sel->Write();
  
   prediction_histos->Write();
   //----------------------------------------------------------//
}

////////////////////////////////////////////////////////////////////////////////////////
bool Prediction_WithUncertainties::DeltaPhiCut_prediction()
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

  //  if( DeltaPhi1 < 0.5 || 
//        DeltaPhi2 < 0.5 ||
//        DeltaPhi3 < 0.3 ) deltaPhiCut = false;  
   
   return deltaPhiCut;
}
////////////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////
bool Prediction_WithUncertainties::DeltaPhiCut_selection()
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

 //   if( DeltaPhi1_RA2 < 0.5 || 
//        DeltaPhi2_RA2 < 0.5 ||
//        DeltaPhi3_RA2 < 0.3 ) deltaPhiCut = false;

   return deltaPhiCut;
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
void Prediction_WithUncertainties::DoRebinning(TH2F* prediction_raw, TH1F* selection_raw, int Nbins) 
{
   //do some non-equidistant binning
   if (Nbins < 0) {
      int nbins = 19;
      // HT binning
      double vbins[20] =  {0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1300, 1500, 1700, 2000, 2500, 3000, 4000, 5000};

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
         vbins[16] = 300.;
         vbins[17] = 450.;
         vbins[18] = 600.;
         vbins[19] = 700.;
         vbins[20] = 800.;
      }
           
      // vbins[15] = 300.;
      //  vbins[16] = 400.;
      //}

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
               prediction_raw->SetBinContent(bin, j, content);
               prediction_raw->SetBinError(bin, j, sqrt(sum2));
               bin = this_bin;
               sum2 = content = 0.;
            }
            sum2 += pow(temp->GetBinError(i, j), 2);
            content += temp->GetBinContent(i, j);
         }
         prediction_raw->SetBinContent(bin, j, content);
         prediction_raw->SetBinError(bin, j, sqrt(sum2));
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
            selection_raw->SetBinContent(bin, content);
            selection_raw->SetBinError(bin, sqrt(sum2));
            bin = this_bin;
            sum2 = content = 0.;
         }
         sum2 += pow(temp2->GetBinError(i), 2);
         content += temp2->GetBinContent(i);
      }
      selection_raw->SetBinContent(bin, content);
      selection_raw->SetBinError(bin, sqrt(sum2));
         
   } else {
      prediction_raw->Rebin2D(Nbins, 1);
      selection_raw->Rebin(Nbins);
   }
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
TH1F* Prediction_WithUncertainties::CalcPrediction(TH2F* prediction_raw) {
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
TH1F* Prediction_WithUncertainties::GetSelectionHisto(TString type) {

   if ( type == "HT_presel")          return HT_presel_sel;
   if ( type == "MHT_presel")         return MHT_presel_sel;
   if ( type == "NJets_presel")       return NJets_presel_sel;
   if ( type == "Jet1Pt_presel")      return Jet1Pt_presel_sel;
   if ( type == "Jet2Pt_presel")      return Jet2Pt_presel_sel;
   if ( type == "Jet3Pt_presel")      return Jet3Pt_presel_sel;
   if ( type == "Jet1Eta_presel")     return Jet1Eta_presel_sel;
   if ( type == "Jet2Eta_presel")     return Jet2Eta_presel_sel;
   if ( type == "Jet3Eta_presel")     return Jet3Eta_presel_sel;
   if ( type == "DeltaPhi1_presel")   return DeltaPhi1_presel_sel;
   if ( type == "DeltaPhi2_presel")   return DeltaPhi2_presel_sel;
   if ( type == "DeltaPhi3_presel")   return DeltaPhi3_presel_sel;

   if ( type == "HT_presel_HThigh")          return HT_presel_HThigh_sel;
   if ( type == "MHT_presel_HThigh")         return MHT_presel_HThigh_sel;
   if ( type == "NJets_presel_HThigh")       return NJets_presel_HThigh_sel;
   if ( type == "Jet1Pt_presel_HThigh")      return Jet1Pt_presel_HThigh_sel;
   if ( type == "Jet2Pt_presel_HThigh")      return Jet2Pt_presel_HThigh_sel;
   if ( type == "Jet3Pt_presel_HThigh")      return Jet3Pt_presel_HThigh_sel;
   if ( type == "Jet1Eta_presel_HThigh")     return Jet1Eta_presel_HThigh_sel;
   if ( type == "Jet2Eta_presel_HThigh")     return Jet2Eta_presel_HThigh_sel;
   if ( type == "Jet3Eta_presel_HThigh")     return Jet3Eta_presel_HThigh_sel;
   if ( type == "DeltaPhi1_presel_HThigh")   return DeltaPhi1_presel_HThigh_sel;
   if ( type == "DeltaPhi2_presel_HThigh")   return DeltaPhi2_presel_HThigh_sel;
   if ( type == "DeltaPhi3_presel_HThigh")   return DeltaPhi3_presel_HThigh_sel;

   if ( type == "MHT_JetBin1_HTlow")      return MHT_JetBin1_HTlow_sel;
   if ( type == "MHT_JetBin1_HTmedium")   return MHT_JetBin1_HTmedium_sel;
   if ( type == "MHT_JetBin1_HThigh")     return MHT_JetBin1_HThigh_sel;
   if ( type == "MHT_JetBin1_HTveryhigh")    return MHT_JetBin1_HTveryhigh_sel;
   if ( type == "MHT_JetBin1_HTextremehigh") return MHT_JetBin1_HTextremehigh_sel;
   if ( type == "MHT_JetBin2_HTlow")      return MHT_JetBin2_HTlow_sel;
   if ( type == "MHT_JetBin2_HTmedium")   return MHT_JetBin2_HTmedium_sel;
   if ( type == "MHT_JetBin2_HThigh")     return MHT_JetBin2_HThigh_sel;
   if ( type == "MHT_JetBin2_HTveryhigh")    return MHT_JetBin2_HTveryhigh_sel;
   if ( type == "MHT_JetBin2_HTextremehigh") return MHT_JetBin2_HTextremehigh_sel;
   if ( type == "MHT_JetBin3_HTlow")      return MHT_JetBin3_HTlow_sel;
   if ( type == "MHT_JetBin3_HTmedium")   return MHT_JetBin3_HTmedium_sel;
   if ( type == "MHT_JetBin3_HThigh")     return MHT_JetBin3_HThigh_sel;
   if ( type == "MHT_JetBin3_HTveryhigh")    return MHT_JetBin3_HTveryhigh_sel;
   if ( type == "MHT_JetBin3_HTextremehigh") return MHT_JetBin3_HTextremehigh_sel;
   if ( type == "MHT_JetBin4_HTlow")      return MHT_JetBin4_HTlow_sel;
   if ( type == "MHT_JetBin4_HTmedium")   return MHT_JetBin4_HTmedium_sel;
   if ( type == "MHT_JetBin4_HThigh")     return MHT_JetBin4_HThigh_sel;
   if ( type == "MHT_JetBin4_HTveryhigh")    return MHT_JetBin4_HTveryhigh_sel;
   if ( type == "MHT_JetBin4_HTextremehigh") return MHT_JetBin4_HTextremehigh_sel;

   else { cout << "Error: No valid hist type" << endl;
      return dummy;
   }
}
////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
TH1F* Prediction_WithUncertainties::GetPredictionHisto(TString type) {

   if ( type == "HT_presel")          return HT_presel_pred;
   if ( type == "MHT_presel")         return MHT_presel_pred;
   if ( type == "NJets_presel")       return NJets_presel_pred;
   if ( type == "Jet1Pt_presel")      return Jet1Pt_presel_pred;
   if ( type == "Jet2Pt_presel")      return Jet2Pt_presel_pred;
   if ( type == "Jet3Pt_presel")      return Jet3Pt_presel_pred;
   if ( type == "Jet1Eta_presel")     return Jet1Eta_presel_pred;
   if ( type == "Jet2Eta_presel")     return Jet2Eta_presel_pred;
   if ( type == "Jet3Eta_presel")     return Jet3Eta_presel_pred;
   if ( type == "DeltaPhi1_presel")   return DeltaPhi1_presel_pred;
   if ( type == "DeltaPhi2_presel")   return DeltaPhi2_presel_pred;
   if ( type == "DeltaPhi3_presel")   return DeltaPhi3_presel_pred;

   if ( type == "HT_presel_HThigh")          return HT_presel_HThigh_pred;
   if ( type == "MHT_presel_HThigh")         return MHT_presel_HThigh_pred;
   if ( type == "NJets_presel_HThigh")       return NJets_presel_HThigh_pred;
   if ( type == "Jet1Pt_presel_HThigh")      return Jet1Pt_presel_HThigh_pred;
   if ( type == "Jet2Pt_presel_HThigh")      return Jet2Pt_presel_HThigh_pred;
   if ( type == "Jet3Pt_presel_HThigh")      return Jet3Pt_presel_HThigh_pred;
   if ( type == "Jet1Eta_presel_HThigh")     return Jet1Eta_presel_HThigh_pred;
   if ( type == "Jet2Eta_presel_HThigh")     return Jet2Eta_presel_HThigh_pred;
   if ( type == "Jet3Eta_presel_HThigh")     return Jet3Eta_presel_HThigh_pred;
   if ( type == "DeltaPhi1_presel_HThigh")   return DeltaPhi1_presel_HThigh_pred;
   if ( type == "DeltaPhi2_presel_HThigh")   return DeltaPhi2_presel_HThigh_pred;
   if ( type == "DeltaPhi3_presel_HThigh")   return DeltaPhi3_presel_HThigh_pred;

   if ( type == "MHT_JetBin1_HTlow")      return MHT_JetBin1_HTlow_pred;
   if ( type == "MHT_JetBin1_HTmedium")   return MHT_JetBin1_HTmedium_pred;
   if ( type == "MHT_JetBin1_HThigh")     return MHT_JetBin1_HThigh_pred;
   if ( type == "MHT_JetBin1_HTveryhigh")    return MHT_JetBin1_HTveryhigh_pred;
   if ( type == "MHT_JetBin1_HTextremehigh") return MHT_JetBin1_HTextremehigh_pred;
   if ( type == "MHT_JetBin2_HTlow")      return MHT_JetBin2_HTlow_pred;
   if ( type == "MHT_JetBin2_HTmedium")   return MHT_JetBin2_HTmedium_pred;
   if ( type == "MHT_JetBin2_HThigh")     return MHT_JetBin2_HThigh_pred;
   if ( type == "MHT_JetBin2_HTveryhigh")    return MHT_JetBin2_HTveryhigh_pred;
   if ( type == "MHT_JetBin2_HTextremehigh") return MHT_JetBin2_HTextremehigh_pred;
   if ( type == "MHT_JetBin3_HTlow")      return MHT_JetBin3_HTlow_pred;
   if ( type == "MHT_JetBin3_HTmedium")   return MHT_JetBin3_HTmedium_pred;
   if ( type == "MHT_JetBin3_HThigh")     return MHT_JetBin3_HThigh_pred;
   if ( type == "MHT_JetBin3_HTveryhigh")    return MHT_JetBin3_HTveryhigh_pred;
   if ( type == "MHT_JetBin3_HTextremehigh") return MHT_JetBin3_HTextremehigh_pred;
   if ( type == "MHT_JetBin4_HTlow")      return MHT_JetBin4_HTlow_pred;
   if ( type == "MHT_JetBin4_HTmedium")   return MHT_JetBin4_HTmedium_pred;
   if ( type == "MHT_JetBin4_HThigh")     return MHT_JetBin4_HThigh_pred;
   if ( type == "MHT_JetBin4_HTveryhigh")    return MHT_JetBin4_HTveryhigh_pred;
   if ( type == "MHT_JetBin4_HTextremehigh") return MHT_JetBin4_HTextremehigh_pred;

   else { cout << "Error: No valid hist type" << endl;
      return dummy;
   }
}
////////////////////////////////////////////////////////////////////////////////////////

      
////////////////////////////////////////////////////////////////////////////////////////
double Prediction_WithUncertainties::GetResultValue(TH1F* histo, double MHTlow, double MHTup)
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
double Prediction_WithUncertainties::GetResultError(TH1F* histo, double MHTlow, double MHTup)
{
   double result_error;
   if( MHTlow == MHTup ) {
      histo->IntegralAndError(histo->FindBin(MHTlow),histo->GetNbinsX(), result_error);
   }
   else histo->IntegralAndError(histo->FindBin(MHTlow), histo->FindBin(MHTup)-1, result_error);

   return result_error;
}
////////////////////////////////////////////////////////////////////////////////////////


