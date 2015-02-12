#include <TROOT.h>
#include <TSystem.h>
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include <TCanvas.h>
#include <TColor.h>
#include <TChain.h>
#include <TPad.h>
#include <TStyle.h>
#include <TFile.h>
#include <TPostScript.h>
#include <TLegend.h>
#include <TMath.h>
#include <TString.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "Prediction.h"
#include "../../../AdditionalInputFiles/RA2PlottingStyle.h" 

using namespace std;

TCanvas* DrawComparison(TH1F* prediction, TH1F* selection, TString Title, TString LumiTitle, TString xTitle, TString yTitle, bool isData)
{
   double MinX = selection->GetXaxis()->GetXmin();
   double MaxX = selection->GetXaxis()->GetXmax();
   double MaxY = selection->GetMaximum();
   double YRangeMax = 120.*MaxY;
   TString titlePrediction;
   TString titleSelection;
   TString RatioTitle;
   
   if( isData ){
      titlePrediction = "Pred. from Data";
      titleSelection = "Data";
      RatioTitle = "(Pred-Data)/Data";
   }
   else {
      titlePrediction = "Data-driven Pred. from MC";
      //titlePrediction = "Smeared Generator Jets";
      titleSelection = "MC Expectation";
      RatioTitle = "(Pred-MC)/MC";
      //RatioTitle = "(Gen-MC)/MC";
   }

   static Int_t c_LightBrown   = TColor::GetColor( "#D9D9CC" );
   static Int_t c_LightGray    = TColor::GetColor( "#DDDDDD" );

   prediction->SetAxisRange(MinX, MaxX, "X");
   prediction->GetYaxis()->SetRangeUser(0.005, YRangeMax);
   prediction->SetMarkerStyle(20);
   prediction->SetMarkerSize(0.9);
   prediction->SetMarkerColor(kBlack);
   prediction->SetXTitle(xTitle);
   prediction->SetYTitle(yTitle);
   selection->SetAxisRange(MinX, MaxX, "X");
   selection->GetYaxis()->SetRangeUser(0.05, YRangeMax);
   // selection->SetFillColor(c_LightBrown);
   selection->SetFillColor(c_LightGray);
   selection->SetTitle("");
   selection->SetXTitle(xTitle);
   selection->SetYTitle(yTitle);

   TCanvas *c = new TCanvas("ca", "Comparison and ratio of two histos", 700, 700);

   TPad *pad1 = new TPad("pad1a", "pad1a", 0, 0.35, 1, 1);
   pad1->SetLogy();
   pad1->SetBottomMargin(0);
   pad1->Draw();
   pad1->cd();
  
   selection->DrawCopy("hist");
   prediction->Draw("same");
   selection->SetFillColor(kAzure-3);
   selection->SetFillStyle(3354);
   selection->DrawCopy("e2same");

   selection->SetFillStyle(1001);
   //  selection->SetFillColor(c_LightBrown);
   selection->SetFillColor(c_LightGray);

   //  TLegend* leg1 = new TLegend(0.48, 0.63, 0.95, 0.83);
   TLegend* leg1 = new TLegend(0.44, 0.63, 0.91, 0.83);
   leg1->SetFillStyle(0);
   leg1->SetLineStyle(1);
   leg1->SetTextFont(42);
   // leg1->SetTextSize(0.04);
   leg1->SetTextSize(0.045);
   leg1->AddEntry(selection, titleSelection, "lf");
   leg1->AddEntry(prediction, titlePrediction, "lep");
   leg1->Draw("same");
 
   TPaveText* pt = new TPaveText(0.11, 0.98, 0.95, 0.86, "NDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextAlign(12);
   pt->SetTextSize(0.045);
   pt->AddText(Title);
   pt->AddText(LumiTitle);
   pt->Draw();

   c->cd();
   TPad *pad2 = new TPad("pad2a", "pad2a", 0, 0, 1, 0.35);
   pad2->SetTopMargin(0);
   pad2->Draw();
   pad2->cd();
   TH1F* r = new TH1F(*selection);
   r->SetTitle("");
   r->SetLabelSize(0.08, "XYZ");
   r->SetLabelOffset(0.01, "XYZ");
   // r->SetTitleSize(0.09, "XYZ");
   r->SetTitleSize(0.125, "XYZ");
   r->SetTitleOffset(0.95, "X");
   r->SetTitleOffset(0.53, "Y");
   // r->SetTitleOffset(0.65, "Y");
   r->SetTickLength(0.05);
   r->SetYTitle(RatioTitle);
   r->SetStats(0);
   r->SetMarkerStyle(20);
   r->SetMarkerSize(0.9);
   r->SetMarkerColor(kBlack);
   r->Reset();
   r->Add(prediction, 1);
   r->Add(selection, -1);
   r->Divide(selection);
   r->SetMaximum(1.2);
   r->SetMinimum(-1.2);
   r->Draw("ep");
   TLine l;
   l.DrawLine(MinX, 0., MaxX, 0.);
   c->cd();
   return c;
}

int main()
{

   gROOT->Reset();
   gROOT->SetStyle("Plain");
   //gStyle->SetPalette(51, 0);

   //  gStyle->SetHatchesLineWidth(1.2);

   // For the canvas:
   gStyle->SetCanvasColor(0);
   //gStyle->SetCanvasBorderMode(0);

   // For the Pad:
   gStyle->SetPadColor(0);  
   gStyle->SetPadTickX(1);
   gStyle->SetPadTickY(1);
   gStyle->SetPadBorderSize(2);
   //gStyle->SetPadBorderMode(0);
  
   // For the frame:
   gStyle->SetFrameBorderMode(0);

   // For the histo:
   // gStyle->SetMarkerSize(0.7);
   // gStyle->SetMarkerStyle(20);
   // gStyle->SetMarkerColor(1);
  
   // For the statistics box:
   gStyle->SetOptStat(0);
   //gStyle->SetOptFit(1011);
  
   // Margins:
   gStyle->SetPadBottomMargin(0.25);
   gStyle->SetPadTopMargin(0.15);
   gStyle->SetPadLeftMargin(0.15);
   gStyle->SetPadRightMargin(0.1);
      
   // For the Global title:
   gStyle->SetOptTitle(0);
   gStyle->SetTitleColor(1);
   gStyle->SetTitleFillColor(10);
   gStyle->SetTitleTextColor(1); 
   gStyle->SetTitleFont(42);
   gStyle->SetTitleFontSize(0.05);
   gStyle->SetTitleBorderSize(0);

   // For the axis
   gStyle->SetNdivisions(510, "X");
   gStyle->SetNdivisions(510, "Y");
   gStyle->SetTickLength(0.03);

   // For the axis titles:
   gStyle->SetTitleOffset(1.4, "X");
   //gStyle->SetTitleOffset(1.25, "Y");
   gStyle->SetTitleOffset(1.2, "Y");
   gStyle->SetTitleOffset(0.5, "Z");
   // gStyle->SetTitleSize(0.05, "XYZ");
   gStyle->SetTitleSize(0.061, "XYZ");
   gStyle->SetTitleFont(42, "XYZ");
   //gStyle->SetTitleX(0.15);
   //gStyle->SetTitleY(0.99);

   // For the axis labels:
   gStyle->SetLabelSize(0.04, "XYZ");
   gStyle->SetLabelOffset(0.01, "XYZ");
   gStyle->SetLabelFont(42, "XYZ");

   // For the legend
   gStyle->SetLegendBorderSize(0);
  
   gROOT->ForceStyle();

   ////////////////////////////////////////   
  
   string root_file;
   TChain* prediction = new TChain("QCDfromSmearing/QCDPrediction");
   TChain* selection = new TChain("RA2TreeMaker/RA2PreSelection");

   // open files for MC --- pythia QCD ---- //
   /*ifstream myfile ("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_UseRebCorrection_v1_mc.txt");
   // ifstream myfile ("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_DoNotUseRebCorrection_v1_mc.txt");
   // ifstream myfile ("filelist_pythia_DR53X_chs_TuneZ2star_SmearedGenJets_withoutPUReweighting_v1_mc.txt");
   if (myfile.is_open()) {
      while( myfile.good() ) {
         getline (myfile,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         selection->Add(path);

      }
      myfile.close();
      }*/

   // open files for MC --- madgraph QCD ---- //
   //ifstream myfile1 ("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT100-250_SmearedGenJets_v1_mc.txt");
   //ifstream myfile1 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT100-250_UseRebCorrection_v1_mc.txt");
   ifstream myfile1 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT100-250_DoNotUseRebCorrection_v1_mc.txt");
   if (myfile1.is_open()) {
      while( myfile1.good() ) {
         getline (myfile1,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         selection->Add(path);

      }
      myfile1.close();
   }

   //ifstream myfile2 ("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT250-500_SmearedGenJets_v1_mc.txt");
   //ifstream myfile2 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT250-500_UseRebCorrection_v1_mc.txt");
   ifstream myfile2 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT250-500_DoNotUseRebCorrection_v1_mc.txt");
   if (myfile2.is_open()) {
      while( myfile2.good() ) {
         getline (myfile2,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         selection->Add(path);

      }
      myfile2.close();
   }

   // ifstream myfile3 ("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT500-1000_SmearedGenJets_v1_mc.txt");
   //ifstream myfile3 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT500-1000_UseRebCorrection_v1_mc.txt");
   ifstream myfile3 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT500-1000_DoNotUseRebCorrection_v1_mc.txt");
   if (myfile3.is_open()) {
      while( myfile3.good() ) {
         getline (myfile3,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         selection->Add(path);

      }
      myfile3.close();
   }

   //ifstream myfile4 ("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT1000-Inf_SmearedGenJets_v1_mc.txt");
   //ifstream myfile4 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT1000-Inf_UseRebCorrection_v1_mc.txt");
   ifstream myfile4 ("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT1000-Inf_DoNotUseRebCorrection_v1_mc.txt");
   if (myfile4.is_open()) {
      while( myfile4.good() ) {
         getline (myfile4,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         selection->Add(path);

      }
      myfile4.close();
   }


   // files for data prediction
   /*  ifstream myfile1 ("filelist_prediction_535_Resolutions525_Run2012A-13Jul2012-v1_pt15_withUncertainties_data.txt");
   if (myfile1.is_open()) {
      while( myfile1.good() ) {
         getline (myfile1,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
      }
      myfile1.close();
   }

   ifstream myfile2 ("filelist_prediction_535_Resolutions525_Run2012A-recover-06Aug2012-v1_pt15_withUncertainties_data.txt");
   if (myfile2.is_open()) {
      while( myfile2.good() ) {
         getline (myfile2,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
      }
      myfile2.close();
   }

   ifstream myfile3 ("filelist_prediction_535_Resolutions525_Run2012B-13Jul2012-v1_pt15_withUncertainties_data.txt");
   if (myfile3.is_open()) {
      while( myfile3.good() ) {
         getline (myfile3,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
      }
      myfile3.close();
   }

   ifstream myfile4 ("filelist_selection_535_Resolutions525_Run2012A-13Jul2012-v1_data.txt");
   if (myfile4.is_open()) {
      while( myfile4.good() ) {
         getline (myfile4,root_file);
         cout << root_file << endl;

         TString path = root_file;
         selection->Add(path);
      }
      myfile4.close();
   }

   ifstream myfile5 ("filelist_selection_535_Resolutions525_Run2012A-recover-06Aug2012-v1_data.txt");
   if (myfile5.is_open()) {
      while( myfile5.good() ) {
         getline (myfile5,root_file);
         cout << root_file << endl;

         TString path = root_file;
         selection->Add(path);
      }
      myfile5.close();
   }

   ifstream myfile6 ("filelist_selection_535_Resolutions525_Run2012B-13Jul2012-v1_data.txt");
   if (myfile6.is_open()) {
      while( myfile6.good() ) {
         getline (myfile6,root_file);
         cout << root_file << endl;

         TString path = root_file;
         selection->Add(path);
      }
      myfile6.close();
      }*/

   // ------------------------------------------------------------------- //
     
   // initialize new Prediction object
   Prediction *pred_;
   bool isData = false;
   pred_ = new Prediction(*prediction, *selection);
  
   TString LumiTitle;
   if( isData ) LumiTitle = "CMS preliminary, L = 19.466 fb^{  -1}, #sqrt{s} = 8 TeV";
   else LumiTitle = "CMS Simulation, #sqrt{s} = 8 TeV";
   //else LumiTitle = "CMS work in progress, #sqrt{s} = 8 TeV";

   //TString postfix = "_test";
 
   //TString postfix = "_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_UseRebCorrection_v1";
   // TString postfix = "_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_DoNotUseRebCorrection_v1";
   // TString postfix = "_pythia_DR53X_chs_TuneZ2star_SmearedGenJets_withoutPUReweighting_v1";
  
   //TString postfix = "_madgraph_DR53X_chs_TuneZ2star_SmearedGenJets_withoutPUReweighting_v1";
   //TString postfix = "_madgraph_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_UseRebCorrection_deltaPhiInverted_v1";
   // TString postfix = "_madgraph_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_UseRebCorrection_v1";
   TString postfix = "_madgraph_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_DoNotUseRebCorrection_v1";


   vector<TString> xTitle_presel;
   xTitle_presel.push_back("H_{T} (GeV)");
   xTitle_presel.push_back("#slash{H}_{T} (GeV)");
   xTitle_presel.push_back("N_{Jets}");
   xTitle_presel.push_back("Jet1 p_{T} (GeV)");
   xTitle_presel.push_back("Jet2 p_{T} (GeV)");
   xTitle_presel.push_back("Jet1 #eta");
   xTitle_presel.push_back("Jet2 #eta");

   vector<TString> xTitle_deltaPhi;
   xTitle_deltaPhi.push_back("H_{T} (GeV)");
   xTitle_deltaPhi.push_back("#slash{H}_{T} (GeV)");
   xTitle_deltaPhi.push_back("Jet1 p_{T} (GeV)");
   xTitle_deltaPhi.push_back("Jet2 p_{T} (GeV)");
   xTitle_deltaPhi.push_back("Jet1 #eta");
   xTitle_deltaPhi.push_back("Jet2 #eta");

   vector<TString> xTitle_searchBins;
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");
   xTitle_searchBins.push_back("#slash{H}_{T} (GeV)");

   vector<TString> xTitle_baseline_Bin1;
   xTitle_baseline_Bin1.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_Bin1.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_Bin1.push_back("Jet1 #eta");
   xTitle_baseline_Bin1.push_back("Jet2 #eta");
   xTitle_baseline_Bin1.push_back("#Delta#phi 1");
   xTitle_baseline_Bin1.push_back("#Delta#phi 2");
    
   vector<TString> xTitle_baseline_Bin2;
   xTitle_baseline_Bin2.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_Bin2.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_Bin2.push_back("Jet3 p_{T} (GeV)");
   xTitle_baseline_Bin2.push_back("Jet1 #eta");
   xTitle_baseline_Bin2.push_back("Jet2 #eta");
   xTitle_baseline_Bin2.push_back("Jet3 #eta");
   xTitle_baseline_Bin2.push_back("#Delta#phi 1");
   xTitle_baseline_Bin2.push_back("#Delta#phi 2");
   xTitle_baseline_Bin2.push_back("#Delta#phi 3");

   vector<TString> xTitle_baseline_Bin3;
   xTitle_baseline_Bin3.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_Bin3.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_Bin3.push_back("Jet3 p_{T} (GeV)");
   xTitle_baseline_Bin3.push_back("Jet1 #eta");
   xTitle_baseline_Bin3.push_back("Jet2 #eta");
   xTitle_baseline_Bin3.push_back("Jet3 #eta");
   xTitle_baseline_Bin3.push_back("#Delta#phi 1");
   xTitle_baseline_Bin3.push_back("#Delta#phi 2");
   xTitle_baseline_Bin3.push_back("#Delta#phi 3");
  
   vector<TString> xTitle_baseline_Bin4;
   xTitle_baseline_Bin4.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_Bin4.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_Bin4.push_back("Jet3 p_{T} (GeV)");
   xTitle_baseline_Bin4.push_back("Jet1 #eta");
   xTitle_baseline_Bin4.push_back("Jet2 #eta");
   xTitle_baseline_Bin4.push_back("Jet3 #eta");
   xTitle_baseline_Bin4.push_back("#Delta#phi 1");
   xTitle_baseline_Bin4.push_back("#Delta#phi 2");
   xTitle_baseline_Bin4.push_back("#Delta#phi 3");

   vector<TString> xTitle_baseline_withoutDeltaPhi_Bin1;
   xTitle_baseline_withoutDeltaPhi_Bin1.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin1.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin1.push_back("Jet1 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin1.push_back("Jet2 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin1.push_back("#Delta#phi 1");
   xTitle_baseline_withoutDeltaPhi_Bin1.push_back("#Delta#phi 2");

   vector<TString> xTitle_baseline_withoutDeltaPhi_Bin2;
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("Jet3 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("Jet1 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("Jet2 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("Jet3 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("#Delta#phi 1");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("#Delta#phi 2");
   xTitle_baseline_withoutDeltaPhi_Bin2.push_back("#Delta#phi 3");

   vector<TString> xTitle_baseline_withoutDeltaPhi_Bin3;
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("Jet3 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("Jet1 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("Jet2 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("Jet3 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("#Delta#phi 1");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("#Delta#phi 2");
   xTitle_baseline_withoutDeltaPhi_Bin3.push_back("#Delta#phi 3");

   vector<TString> xTitle_baseline_withoutDeltaPhi_Bin4;
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("Jet1 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("Jet2 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("Jet3 p_{T} (GeV)");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("Jet1 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("Jet2 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("Jet3 #eta");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("#Delta#phi 1");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("#Delta#phi 2");
   xTitle_baseline_withoutDeltaPhi_Bin4.push_back("#Delta#phi 3");
  
   vector<TString> hist_type_presel;
   hist_type_presel.push_back("HT_presel");
   hist_type_presel.push_back("MHT_presel");
   hist_type_presel.push_back("NJets_presel"); 
   hist_type_presel.push_back("Jet1Pt_presel");
   hist_type_presel.push_back("Jet2Pt_presel");
   hist_type_presel.push_back("Jet1Eta_presel");
   hist_type_presel.push_back("Jet2Eta_presel");

   vector<TString> hist_type_deltaPhi;
   hist_type_deltaPhi.push_back("HT_deltaPhi");
   hist_type_deltaPhi.push_back("MHT_deltaPhi");    
   hist_type_deltaPhi.push_back("Jet1Pt_deltaPhi"); 
   hist_type_deltaPhi.push_back("Jet2Pt_deltaPhi"); 
   hist_type_deltaPhi.push_back("Jet1Eta_deltaPhi");
   hist_type_deltaPhi.push_back("Jet2Eta_deltaPhi");
  
   vector<TString> hist_type_searchBins;
   hist_type_searchBins.push_back("MHT_JetBin1_HTlow");    
   hist_type_searchBins.push_back("MHT_JetBin1_HTmedium"); 
   hist_type_searchBins.push_back("MHT_JetBin1_HThigh");   
   hist_type_searchBins.push_back("MHT_JetBin2_HTlow");    
   hist_type_searchBins.push_back("MHT_JetBin2_HTmedium"); 
   hist_type_searchBins.push_back("MHT_JetBin2_HThigh");   
   hist_type_searchBins.push_back("MHT_JetBin3_HTlow");    
   hist_type_searchBins.push_back("MHT_JetBin3_HTmedium"); 
   hist_type_searchBins.push_back("MHT_JetBin3_HThigh");   
   hist_type_searchBins.push_back("MHT_JetBin4_HTlow");    
   hist_type_searchBins.push_back("MHT_JetBin4_HTmedium"); 
   hist_type_searchBins.push_back("MHT_JetBin4_HThigh");  

   vector<TString> hist_type_baseline_Bin1;
   hist_type_baseline_Bin1.push_back("Jet1Pt_JetBin1_baseline");
   hist_type_baseline_Bin1.push_back("Jet2Pt_JetBin1_baseline");
   hist_type_baseline_Bin1.push_back("Jet1Eta_JetBin1_baseline");
   hist_type_baseline_Bin1.push_back("Jet2Eta_JetBin1_baseline");
   hist_type_baseline_Bin1.push_back("DeltaPhi1_JetBin1_baseline");
   hist_type_baseline_Bin1.push_back("DeltaPhi2_JetBin1_baseline");

   vector<TString> hist_type_baseline_Bin2;
   hist_type_baseline_Bin2.push_back("Jet1Pt_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("Jet2Pt_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("Jet3Pt_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("Jet1Eta_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("Jet2Eta_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("Jet3Eta_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("DeltaPhi1_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("DeltaPhi2_JetBin2_baseline");
   hist_type_baseline_Bin2.push_back("DeltaPhi3_JetBin2_baseline");

   vector<TString> hist_type_baseline_Bin3;
   hist_type_baseline_Bin3.push_back("Jet1Pt_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("Jet2Pt_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("Jet3Pt_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("Jet1Eta_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("Jet2Eta_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("Jet3Eta_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("DeltaPhi1_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("DeltaPhi2_JetBin3_baseline");
   hist_type_baseline_Bin3.push_back("DeltaPhi3_JetBin3_baseline");

   vector<TString> hist_type_baseline_Bin4;
   hist_type_baseline_Bin4.push_back("Jet1Pt_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("Jet2Pt_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("Jet3Pt_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("Jet1Eta_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("Jet2Eta_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("Jet3Eta_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("DeltaPhi1_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("DeltaPhi2_JetBin4_baseline");
   hist_type_baseline_Bin4.push_back("DeltaPhi3_JetBin4_baseline");

   vector<TString> hist_type_baseline_withoutDeltaPhi_Bin1;
   hist_type_baseline_withoutDeltaPhi_Bin1.push_back("Jet1Pt_JetBin1_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin1.push_back("Jet2Pt_JetBin1_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin1.push_back("Jet1Eta_JetBin1_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin1.push_back("Jet2Eta_JetBin1_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin1.push_back("DeltaPhi1_JetBin1_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin1.push_back("DeltaPhi2_JetBin1_baseline_withoutDeltaPhi");

   vector<TString> hist_type_baseline_withoutDeltaPhi_Bin2;
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("Jet1Pt_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("Jet2Pt_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("Jet3Pt_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("Jet1Eta_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("Jet2Eta_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("Jet3Eta_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("DeltaPhi1_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("DeltaPhi2_JetBin2_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin2.push_back("DeltaPhi3_JetBin2_baseline_withoutDeltaPhi");

   vector<TString> hist_type_baseline_withoutDeltaPhi_Bin3;
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("Jet1Pt_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("Jet2Pt_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("Jet3Pt_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("Jet1Eta_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("Jet2Eta_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("Jet3Eta_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("DeltaPhi1_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("DeltaPhi2_JetBin3_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin3.push_back("DeltaPhi3_JetBin3_baseline_withoutDeltaPhi");

   vector<TString> hist_type_baseline_withoutDeltaPhi_Bin4;
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("Jet1Pt_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("Jet2Pt_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("Jet3Pt_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("Jet1Eta_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("Jet2Eta_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("Jet3Eta_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("DeltaPhi1_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("DeltaPhi2_JetBin4_baseline_withoutDeltaPhi");
   hist_type_baseline_withoutDeltaPhi_Bin4.push_back("DeltaPhi3_JetBin4_baseline_withoutDeltaPhi");

   // --------------------------------------------------------------------------------------------- //
   // plots for preselection (2 jets)
   TString Title;
   TString yTitle = "Events";
   Title = ">= 3 jets";

   if( hist_type_presel.size() != xTitle_presel.size() ) cout << "Error: Missing xTitles preselection!!" << endl;

   for(int i = 0; i < hist_type_presel.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_presel.at(i)), pred_->GetSelectionHisto(hist_type_presel.at(i)), Title, LumiTitle, xTitle_presel.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_presel" + postfix + ".ps(");
      else if ( i == hist_type_presel.size()-1 ) c->Print("outpout_GetPrediction/QCD_presel" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_presel" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_presel.at(i) + postfix + ".png");
   }

   // --------------------------------------------------------------------------------------------- //
   // deltaPhi after preselection
   Title = ">= 3 jets";
   TCanvas *c =  DrawComparison( pred_->GetPredictionHisto("DeltaPhi1_presel"), pred_->GetSelectionHisto("DeltaPhi1_presel"), Title, LumiTitle,"#Delta#phi (jet1, MHT)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_DeltaPhiPlots_presel" + postfix + ".ps(");
   c->Print("outpout_GetPrediction/DeltaPhi1_presel" + postfix + ".png");

   Title = ">= 3 jets";
   c =  DrawComparison( pred_->GetPredictionHisto("DeltaPhi2_presel"), pred_->GetSelectionHisto("DeltaPhi2_presel"), Title, LumiTitle,"#Delta#phi (jet2, MHT)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_DeltaPhiPlots_presel" + postfix + ".ps");
   c->Print("outpout_GetPrediction/DeltaPhi2_presel" + postfix + ".png");

   Title = ">= 3 jets";
   c =  DrawComparison( pred_->GetPredictionHisto("DeltaPhi3_presel"), pred_->GetSelectionHisto("DeltaPhi3_presel"), Title, LumiTitle,"#Delta#phi (jet3, MHT)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_DeltaPhiPlots_presel" + postfix + ".ps)");
   c->Print("outpout_GetPrediction/DeltaPhi3_presel" + postfix + ".png");
  
   // --------------------------------------------------------------------------------------------- //
   // plots for preselection + deltaPhi cut
   Title = ">= 3 jets, #Delta#phi(#slash{H}_{T}, jet1-2,3)";

   if( hist_type_deltaPhi.size() != xTitle_deltaPhi.size() ) cout << "Error: Missing xTitles preselection!!" << endl;

   for(int i = 0; i < hist_type_deltaPhi.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_deltaPhi.at(i)), pred_->GetSelectionHisto(hist_type_deltaPhi.at(i)), Title, LumiTitle, xTitle_deltaPhi.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_deltaPhi" + postfix + ".ps(");
      else if ( i == hist_type_deltaPhi.size()-1 ) c->Print("outpout_GetPrediction/QCD_deltaPhi" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_deltaPhi" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_deltaPhi.at(i) + postfix + ".png");
   }

   // --------------------------------------------------------------------------------------------- //
   // plots for baseline
   Title = "2 jets, #Delta#phi, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_Bin1.size() != xTitle_baseline_Bin1.size() ) cout << "Error: Missing xTitles baseline Bin1!!" << endl;

   for(int i = 0; i < hist_type_baseline_Bin1.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_Bin1.at(i)), pred_->GetSelectionHisto(hist_type_baseline_Bin1.at(i)), Title, LumiTitle, xTitle_baseline_Bin1.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_Bin1" + postfix + ".ps(");
      else if ( i == hist_type_baseline_Bin1.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_Bin1" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_Bin1" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_Bin1.at(i) + postfix + ".png");
   }

   ////////////////////////////////////////////////////////////////
   Title = "3-5 jets, #Delta#phi, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_Bin2.size() != xTitle_baseline_Bin2.size() ) cout << "Error: Missing xTitles baseline Bin2!!" << endl;

   for(int i = 0; i < hist_type_baseline_Bin2.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_Bin2.at(i)), pred_->GetSelectionHisto(hist_type_baseline_Bin2.at(i)), Title, LumiTitle, xTitle_baseline_Bin2.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_Bin2" + postfix + ".ps(");
      else if ( i == hist_type_baseline_Bin2.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_Bin2" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_Bin2" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_Bin2.at(i) + postfix + ".png");
   }

   ////////////////////////////////////////////////////////////////
   Title = "6+7 jets, #Delta#phi, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_Bin3.size() != xTitle_baseline_Bin3.size() ) cout << "Error: Missing xTitles baseline Bin3!!" << endl;

   for(int i = 0; i < hist_type_baseline_Bin3.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_Bin3.at(i)), pred_->GetSelectionHisto(hist_type_baseline_Bin3.at(i)), Title, LumiTitle, xTitle_baseline_Bin3.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_Bin3" + postfix + ".ps(");
      else if ( i == hist_type_baseline_Bin3.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_Bin3" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_Bin3" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_Bin3.at(i) + postfix + ".png");
   }

   ////////////////////////////////////////////////////////////////
   Title = ">=8 jets, #Delta#phi, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_Bin4.size() != xTitle_baseline_Bin4.size() ) cout << "Error: Missing xTitles baseline Bin4!!" << endl;

   for(int i = 0; i < hist_type_baseline_Bin4.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_Bin4.at(i)), pred_->GetSelectionHisto(hist_type_baseline_Bin4.at(i)), Title, LumiTitle, xTitle_baseline_Bin4.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_Bin4" + postfix + ".ps(");
      else if ( i == hist_type_baseline_Bin4.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_Bin4" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_Bin4" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_Bin4.at(i) + postfix + ".png");
   }

   // --------------------------------------------------------------------------------------------- //
   // plots for baseline without deltaPhi
   Title = "2 jets, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_withoutDeltaPhi_Bin1.size() != xTitle_baseline_withoutDeltaPhi_Bin1.size() ) cout << "Error: Missing xTitles baseline_withoutDeltaPhi Bin1!!" << endl;

   for(int i = 0; i < hist_type_baseline_withoutDeltaPhi_Bin1.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_withoutDeltaPhi_Bin1.at(i)), pred_->GetSelectionHisto(hist_type_baseline_withoutDeltaPhi_Bin1.at(i)), Title, LumiTitle, xTitle_baseline_withoutDeltaPhi_Bin1.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin1" + postfix + ".ps(");
      else if ( i == hist_type_baseline_withoutDeltaPhi_Bin1.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin1" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin1" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_withoutDeltaPhi_Bin1.at(i) + postfix + ".png");
   }

   ////////////////////////////////////////////////////////////////
   Title = "3-5 jets, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_withoutDeltaPhi_Bin2.size() != xTitle_baseline_withoutDeltaPhi_Bin2.size() ) cout << "Error: Missing xTitles baseline_withoutDeltaPhi Bin2!!" << endl;

   for(int i = 0; i < hist_type_baseline_withoutDeltaPhi_Bin2.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_withoutDeltaPhi_Bin2.at(i)), pred_->GetSelectionHisto(hist_type_baseline_withoutDeltaPhi_Bin2.at(i)), Title, LumiTitle, xTitle_baseline_withoutDeltaPhi_Bin2.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin2" + postfix + ".ps(");
      else if ( i == hist_type_baseline_withoutDeltaPhi_Bin2.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin2" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin2" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_withoutDeltaPhi_Bin2.at(i) + postfix + ".png");
   }

   ////////////////////////////////////////////////////////////////
   Title = "6+7 jets, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_withoutDeltaPhi_Bin3.size() != xTitle_baseline_withoutDeltaPhi_Bin3.size() ) cout << "Error: Missing xTitles baseline_withoutDeltaPhi Bin3!!" << endl;

   for(int i = 0; i < hist_type_baseline_withoutDeltaPhi_Bin3.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_withoutDeltaPhi_Bin3.at(i)), pred_->GetSelectionHisto(hist_type_baseline_withoutDeltaPhi_Bin3.at(i)), Title, LumiTitle, xTitle_baseline_withoutDeltaPhi_Bin3.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin3" + postfix + ".ps(");
      else if ( i == hist_type_baseline_withoutDeltaPhi_Bin3.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin3" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin3" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_withoutDeltaPhi_Bin3.at(i) + postfix + ".png");
   }

   ////////////////////////////////////////////////////////////////
   Title = ">=8 jets, HT > 500 GeV, MHT > 200 GeV";

   if( hist_type_baseline_withoutDeltaPhi_Bin4.size() != xTitle_baseline_withoutDeltaPhi_Bin4.size() ) cout << "Error: Missing xTitles baseline_withoutDeltaPhi Bin4!!" << endl;

   for(int i = 0; i < hist_type_baseline_withoutDeltaPhi_Bin4.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_baseline_withoutDeltaPhi_Bin4.at(i)), pred_->GetSelectionHisto(hist_type_baseline_withoutDeltaPhi_Bin4.at(i)), Title, LumiTitle, xTitle_baseline_withoutDeltaPhi_Bin4.at(i), yTitle, isData); 

      if      ( i == 0) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin4" + postfix + ".ps(");
      else if ( i == hist_type_baseline_withoutDeltaPhi_Bin4.size()-1 ) c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin4" + postfix + ".ps)");
      else c->Print("outpout_GetPrediction/QCD_baseline_withoutDeltaPhi_Bin4" + postfix + ".ps");

      c->Print("outpout_GetPrediction/" + hist_type_baseline_withoutDeltaPhi_Bin4.at(i) + postfix + ".png");
   }

   // --------------------------------------------------------------------------------------------- //
   // plots for non-closure uncertainty 
   //jet Bin 1
   Title = "2 jets, #Delta#phi cut, HT = 500 - 1000 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps(");
   c->Print("outpout_GetPrediction/MHT_JetBin1_HTlow" + postfix + ".png");

   Title = "2 jets, #Delta#phi cut, HT >= 1000 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin1_HThigh" + postfix + ".png");

   // jet Bin2
   Title = "3 - 5 jets, #Delta#phi cut, HT = 500 - 1000 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin2_HTlow" + postfix + ".png");

   Title = "3 - 5 jets, #Delta#phi cut, HT >= 1000 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin2_HThigh" + postfix + ".png");

   // jet Bin3
   Title = "6 - 7 jets, #Delta#phi cut, HT = 500 - 1000 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin3_HTlow" + postfix + ".png");

   Title = "6 - 7 jets, #Delta#phi cut, HT >= 1000 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin3_HThigh" + postfix + ".png");

   // jet Bin 4
   Title = ">= 8 jets, #Delta#phi cut, HT = 500 - 1000 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin4_HTlow" + postfix + ".png");
  
   Title = ">= 8 jets, #Delta#phi cut, HT >= 1000 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_searchBins" + postfix + ".ps)");
   c->Print("outpout_GetPrediction/MHT_JetBin4_HThigh" + postfix + ".png");

   // --------------------------------------------------------------------------------------------- //
   // plots for HT inclusive
   //jet Bin 1
   Title = "2 jets, #Delta#phi cut, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin1_HTinclusive"), pred_->GetSelectionHisto("MHT_JetBin1_HTinclusive"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HTinclusiveNJetBins" + postfix + ".ps(");
   c->Print("outpout_GetPrediction/MHT_JetBin1_HTinclusive" + postfix + ".png");

   // jet Bin2
   Title = "3 - 5 jets, #Delta#phi cut, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin2_HTinclusive"), pred_->GetSelectionHisto("MHT_JetBin2_HTinclusive"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HTinclusiveNJetBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin2_HTinclusive" + postfix + ".png");

   // jet Bin3
   Title = "6 - 7 jets, #Delta#phi cut, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin3_HTinclusive"), pred_->GetSelectionHisto("MHT_JetBin3_HTinclusive"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HTinclusiveNJetBins" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin3_HTinclusive" + postfix + ".png");

   // jet Bin 4
   Title = ">= 8 jets, #Delta#phi cut, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin4_HTinclusive"), pred_->GetSelectionHisto("MHT_JetBin4_HTinclusive"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HTinclusiveNJetBins" + postfix + ".ps)");
   c->Print("outpout_GetPrediction/MHT_JetBin4_HTinclusive" + postfix + ".png");

   // --------------------------------------------------------------------------------------------- //
   // baseline without deltaPhi (HT + MHT)
   //jet Bin 1
   Title = "2 jets, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin1_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("MHT_JetBin1_baseline_withoutDeltaPhi"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_MHT_baseline_withoutDeltaPhi" + postfix + ".ps(");
   c->Print("outpout_GetPrediction/MHT_JetBin1_baseline_withoutDeltaPhi" + postfix + ".png");

   // jet Bin2
   Title = "3 - 5 jets, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin2_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("MHT_JetBin2_baseline_withoutDeltaPhi"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_MHT_baseline_withoutDeltaPhi" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin2_baseline_withoutDeltaPhi" + postfix + ".png");

   // jet Bin3
   Title = "6 - 7 jets, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin3_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("MHT_JetBin3_baseline_withoutDeltaPhi"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_MHT_baseline_withoutDeltaPhi" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_JetBin3_baseline_withoutDeltaPhi" + postfix + ".png");

   // jet Bin 4
   Title = ">= 8 jets, HT > 500 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("MHT_JetBin4_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("MHT_JetBin4_baseline_withoutDeltaPhi"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_MHT_baseline_withoutDeltaPhi" + postfix + ".ps)");
   c->Print("outpout_GetPrediction/MHT_JetBin4_baseline_withoutDeltaPhi" + postfix + ".png");

   //jet Bin 1
   Title = "2 jets, MHT > 200 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("HT_JetBin1_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("HT_JetBin1_baseline_withoutDeltaPhi"), Title, LumiTitle,"H_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HT_baseline_withoutDeltaPhi" + postfix + ".ps(");
   c->Print("outpout_GetPrediction/HT_JetBin1_baseline_withoutDeltaPhi" + postfix + ".png");

   // jet Bin2
   Title = "3 - 5 jets, MHT > 200 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("HT_JetBin2_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("HT_JetBin2_baseline_withoutDeltaPhi"), Title, LumiTitle,"H_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HT_baseline_withoutDeltaPhi" + postfix + ".ps");
   c->Print("outpout_GetPrediction/HT_JetBin2_baseline_withoutDeltaPhi" + postfix + ".png");

   // jet Bin3
   Title = "6 - 7 jets, MHT > 200 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("HT_JetBin3_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("HT_JetBin3_baseline_withoutDeltaPhi"), Title, LumiTitle,"H_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HT_baseline_withoutDeltaPhi" + postfix + ".ps");
   c->Print("outpout_GetPrediction/HT_JetBin3_baseline_withoutDeltaPhi" + postfix + ".png");

   // jet Bin 4
   Title = ">= 8 jets, MHT > 200 GeV";
   c = DrawComparison( pred_->GetPredictionHisto("HT_JetBin4_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("HT_JetBin4_baseline_withoutDeltaPhi"), Title, LumiTitle,"H_{T} (GeV)", yTitle, isData); 
   c->Print("outpout_GetPrediction/QCD_HT_baseline_withoutDeltaPhi" + postfix + ".ps)");
   c->Print("outpout_GetPrediction/HT_JetBin4_baseline_withoutDeltaPhi" + postfix + ".png");

   // --------------------------------------------------------------------------------------------- //
   // baseline plots
   Title = "#Delta#phi cut, HT > 500 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("NJets_baseline_withoutMHT"), pred_->GetSelectionHisto("NJets_baseline_withoutMHT"), Title, LumiTitle,"N_{Jets}", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_NJets_withoutMHT" + postfix + ".ps");
   c->Print("outpout_GetPrediction/NJets_baseline_withoutMHT" + postfix + ".png");

   Title = "#Delta#phi cut, HT > 500 GeV, MHT > 200 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("NJets_baseline"), pred_->GetSelectionHisto("NJets_baseline"), Title, LumiTitle,"N_{Jets}", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_NJets" + postfix + ".ps");
   c->Print("outpout_GetPrediction/NJets_baseline" + postfix + ".png");

   Title = "HT > 500 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("NJets_baseline_withoutDeltaPhi_withoutMHT"), pred_->GetSelectionHisto("NJets_baseline_withoutDeltaPhi_withoutMHT"), Title, LumiTitle,"N_{Jets}", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_NJets_withoutDeltaPhi_withoutMHT" + postfix + ".ps");
   c->Print("outpout_GetPrediction/NJets_baseline_withoutDeltaPhi_withoutMHT" + postfix + ".png");

   Title = "HT > 500 GeV, MHT > 200 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("NJets_baseline_withoutDeltaPhi"), pred_->GetSelectionHisto("NJets_baseline_withoutDeltaPhi"), Title, LumiTitle,"N_{Jets}", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_NJets_withoutDeltaPhi" + postfix + ".ps");
   c->Print("outpout_GetPrediction/NJets_baseline_withoutDeltaPhi" + postfix + ".png");

   Title = ">= 3 jets, #Delta#phi cut, HT > 500 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("MHT_baseline"), pred_->GetSelectionHisto("MHT_baseline"), Title, LumiTitle,"#slash{H}_{T} (GeV)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_MHT_baseline" + postfix + ".ps");
   c->Print("outpout_GetPrediction/MHT_baseline" + postfix + ".png");

   Title = ">= 3 jets, #Delta#phi cut, MHT > 200 GeV";
   c =  DrawComparison( pred_->GetPredictionHisto("HT_baseline"), pred_->GetSelectionHisto("HT_baseline"), Title, LumiTitle,"H_{T} (GeV)", yTitle, isData);
   c->Print("outpout_GetPrediction/QCD_HT_baseline" + postfix + ".ps");
   c->Print("outpout_GetPrediction/HT_baseline" + postfix + ".png");
   // --------------------------------------------------------------------------------------------- //
  
   // set search bin cut values for HT and MHT (check with Prediction.C)
   double HTlow = 500;
   double HThigh = 1000;
   double MHTlow = 100;
   double MHTmedium = 200;
   int SmearRep = 100;
  
   // determine non-closure bias for MC
   if( !isData ) {
 
      ofstream prediction_outfile;
      prediction_outfile.open("outpout_GetPrediction/NonClosureBias" + postfix + ".txt");
    
      // first jet multiplicity bin
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "CMS preliminary, Non-closure uncertainty, #sqrt{s} = 8 TeV" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "NJets = 2 " << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTlow, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
  

      // second jet multiplicity bin
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "NJets = 3 - 5" << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium) ) 
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTlow, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium) ) 
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHTmedium), 2) ) << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) /  pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium) /  pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;


      // third jet multiplicity bin
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "NJets = 6 or 7" << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTlow, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;


      // fourth jet multiplicity bin
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "NJets >= 8" << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTlow, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT = " << HTlow << "-" << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium), 2) ) << endl; 

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << MHTlow << " < MHT < " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;

      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "HT >= " << HThigh << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "MHT >= " << MHTmedium << endl;
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "Integral Selection:  " << pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Integral Prediction: " << pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) 
                         << " +- " << pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium)
                         << endl;
      prediction_outfile << "Non-closure:  1 - Pred/Selection: " << 1 - (pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) / pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) )
                         << " +- " << TMath::Sqrt( pow(1/pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium), 2) * pow(pred_->GetResultError( pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium), 2) + pow(pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium)/pow(pred_->GetResultValue(pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium), 2), 2) * pow(pred_->GetResultError( pred_->GetSelectionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium), 2) ) << endl; 
      prediction_outfile << "----------------------" << endl;
      prediction_outfile << "----------------------" << endl;
   
      prediction_outfile.close();
   }

   return 1;
}




