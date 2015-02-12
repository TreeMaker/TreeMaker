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
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>

#include "Prediction_WithUncertainties.h"
#include "../../../AdditionalInputFiles/RA2PlottingStyle.h" 

using namespace std;

TCanvas* DrawComparison(TH1F* prediction, TH1F* selection, TString Title, TString LumiTitle, TString xTitle, bool isData)
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
      titleSelection = "MC Expectation";
      RatioTitle = "(Pred-MC)/MC";
   }

   static Int_t c_LightBrown   = TColor::GetColor( "#D9D9CC" );
   static Int_t c_LightGray    = TColor::GetColor( "#DDDDDD" );

   prediction->SetAxisRange(MinX, MaxX, "X");
   prediction->GetYaxis()->SetRangeUser(0.005, YRangeMax);
   prediction->SetMarkerStyle(20);
   prediction->SetMarkerSize(0.9);
   prediction->SetMarkerColor(kBlack);
   prediction->SetXTitle(xTitle);
   prediction->SetYTitle("Events");
   selection->SetAxisRange(MinX, MaxX, "X");
   selection->GetYaxis()->SetRangeUser(0.05, YRangeMax);
   // selection->SetFillColor(c_LightBrown);
   selection->SetFillColor(c_LightGray);
   selection->SetTitle("");
   selection->SetXTitle(xTitle);
   selection->SetYTitle("Events");

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

   // TLegend* leg1 = new TLegend(0.48, 0.63, 0.95, 0.83);
   TLegend* leg1 = new TLegend(0.44, 0.63, 0.91, 0.83);
   leg1->SetFillStyle(0);
   leg1->SetLineStyle(1);
   leg1->SetTextFont(42);
   //leg1->SetTextSize(0.04);
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
   // gStyle->SetTitleOffset(1.25, "Y");
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
   TChain* prediction_CoreUP = new TChain("QCDfromSmearingCoreUP/QCDPrediction");
   TChain* prediction_CoreDN = new TChain("QCDfromSmearingCoreDN/QCDPrediction");
   TChain* prediction_TailUP = new TChain("QCDfromSmearingTailUP/QCDPrediction");
   TChain* prediction_TailDN = new TChain("QCDfromSmearingTailDN/QCDPrediction");
   TChain* selection = new TChain("RA2TreeMaker/RA2PreSelection");

   // files for data 
   ifstream myfile1 ("filelist_prediction_535_Run2012A-13Jul2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile1.is_open()) {
      while( myfile1.good() ) {
         getline (myfile1,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         prediction_TailDN->Add(path);
         selection->Add(path);
      }
      myfile1.close();
   }

   ifstream myfile2 ("filelist_prediction_535_Run2012A-recover-06Aug2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile2.is_open()) {
      while( myfile2.good() ) {
         getline (myfile2,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         prediction_TailDN->Add(path);
         selection->Add(path);
      }
      myfile2.close();
   }

   ifstream myfile3 ("filelist_prediction_535_Run2012B-13Jul2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile3.is_open()) {
      while( myfile3.good() ) {
         getline (myfile3,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         prediction_TailDN->Add(path);
         selection->Add(path);
      }
      myfile3.close();
   }

   ifstream myfile4 ("filelist_prediction_535_Run2012C-24Aug2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile4.is_open()) {
      while( myfile4.good() ) {
         getline (myfile4,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         prediction_TailDN->Add(path);
         selection->Add(path);
      }
      myfile4.close();
   }

   ifstream myfile5 ("filelist_prediction_535_Run2012C-PromptReco-v2_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile5.is_open()) {
      while( myfile5.good() ) {
         getline (myfile5,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         prediction_TailDN->Add(path);
         selection->Add(path);
      }
      myfile5.close();
   }

   ifstream myfile6 ("filelist_prediction_535_Run2012D-PromptReco-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile6.is_open()) {
      while( myfile6.good() ) {
         getline (myfile6,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         prediction_TailDN->Add(path);
         selection->Add(path);
      }
      myfile6.close();
   }

   // ------------------------------------------------------------------- //
     
   // initialize new Prediction objects
   Prediction_WithUncertainties *pred_;
   Prediction_WithUncertainties *pred_CoreUP_;
   Prediction_WithUncertainties *pred_CoreDN_;
   Prediction_WithUncertainties *pred_TailUP_;
   Prediction_WithUncertainties *pred_TailDN_;

   TString uncertainty;
   uncertainty = "_nominal";
   pred_ = new Prediction_WithUncertainties(*prediction, *selection, uncertainty);
   uncertainty = "_CoreUP";
   pred_CoreUP_ = new Prediction_WithUncertainties(*prediction_CoreUP, *selection, uncertainty);
   uncertainty = "_CoreDN";
   pred_CoreDN_ = new Prediction_WithUncertainties(*prediction_CoreDN, *selection, uncertainty);
   uncertainty = "_TailUP";
   pred_TailUP_ = new Prediction_WithUncertainties(*prediction_TailUP, *selection, uncertainty);
   uncertainty = "_TailDN";
   pred_TailDN_ = new Prediction_WithUncertainties(*prediction_TailDN, *selection, uncertainty);

   bool isData = true;
   TString LumiTitle;
   LumiTitle = "CMS preliminary, L = 19.466 fb^{  -1}, #sqrt{s} = 8 TeV";
  
   TString postfix = "_chsJets_535_Run2012ABCD_data_pt10_withUncertainties_UseRebCorrection_v3";

   vector<TString> xTitle_presel_lowHT;
   xTitle_presel_lowHT.push_back("H_{T} (GeV)");
   xTitle_presel_lowHT.push_back("#slash{H}_{T} (GeV)");
   xTitle_presel_lowHT.push_back("N_{Jets}");
   xTitle_presel_lowHT.push_back("Jet1 p_{T} (GeV)");
   xTitle_presel_lowHT.push_back("Jet2 p_{T} (GeV)");
   xTitle_presel_lowHT.push_back("Jet1 #eta");
   xTitle_presel_lowHT.push_back("Jet2 #eta");

   vector<TString> xTitle_presel_highHT;
   xTitle_presel_highHT.push_back("H_{T} (GeV)");
   xTitle_presel_highHT.push_back("#slash{H}_{T} (GeV)");
   xTitle_presel_highHT.push_back("N_{Jets}");
   xTitle_presel_highHT.push_back("Jet1 p_{T} (GeV)");
   xTitle_presel_highHT.push_back("Jet2 p_{T} (GeV)");
   xTitle_presel_highHT.push_back("Jet1 #eta");
   xTitle_presel_highHT.push_back("Jet2 #eta");
  
   vector<TString> hist_type_presel_lowHT;
   hist_type_presel_lowHT.push_back("HT_presel");
   hist_type_presel_lowHT.push_back("MHT_presel");
   hist_type_presel_lowHT.push_back("NJets_presel"); 
   hist_type_presel_lowHT.push_back("Jet1Pt_presel");
   hist_type_presel_lowHT.push_back("Jet2Pt_presel");
   hist_type_presel_lowHT.push_back("Jet1Eta_presel");
   hist_type_presel_lowHT.push_back("Jet2Eta_presel");

   vector<TString> hist_type_presel_highHT;
   hist_type_presel_highHT.push_back("HT_presel_HThigh");
   hist_type_presel_highHT.push_back("MHT_presel_HThigh");
   hist_type_presel_highHT.push_back("NJets_presel_HThigh"); 
   hist_type_presel_highHT.push_back("Jet1Pt_presel_HThigh");
   hist_type_presel_highHT.push_back("Jet2Pt_presel_HThigh");
   hist_type_presel_highHT.push_back("Jet1Eta_presel_HThigh");
   hist_type_presel_highHT.push_back("Jet2Eta_presel_HThigh");
  
   // plots for preselection (2 jets)
   TString Title;
   Title = ">= 3 jets, #Delta#phi cut inverted, HT = 500 - 1000 GeV";

   if( hist_type_presel_lowHT.size() != xTitle_presel_lowHT.size() ) cout << "Error: Missing xTitles preselection!!" << endl;

   for(int i = 0; i < hist_type_presel_lowHT.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_presel_lowHT.at(i)), pred_->GetSelectionHisto(hist_type_presel_lowHT.at(i)), Title, LumiTitle, xTitle_presel_lowHT.at(i), isData); 

      if      ( i == 0) c->Print("output_GetPrediction_WithUncertainties/QCD_presel_lowHT" + postfix + ".ps(");
      else if ( i == hist_type_presel_lowHT.size()-1 ) c->Print("output_GetPrediction_WithUncertainties/QCD_presel_lowHT" + postfix + ".ps)");
      else c->Print("output_GetPrediction_WithUncertainties/QCD_presel_lowHT" + postfix + ".ps");

      c->Print("output_GetPrediction_WithUncertainties/" + hist_type_presel_lowHT.at(i) + postfix + ".png");
   }

   Title = ">= 3 jets, #Delta#phi cut inverted, HT > 1000 GeV";

   if( hist_type_presel_highHT.size() != xTitle_presel_highHT.size() ) cout << "Error: Missing xTitles preselection!!" << endl;

   for(int i = 0; i < hist_type_presel_highHT.size(); i++ ) {
      TCanvas *c = DrawComparison( pred_->GetPredictionHisto(hist_type_presel_highHT.at(i)), pred_->GetSelectionHisto(hist_type_presel_highHT.at(i)), Title, LumiTitle, xTitle_presel_highHT.at(i), isData); 

      if      ( i == 0) c->Print("output_GetPrediction_WithUncertainties/QCD_presel_highHT" + postfix + ".ps(");
      else if ( i == hist_type_presel_highHT.size()-1 ) c->Print("output_GetPrediction_WithUncertainties/QCD_presel_highHT" + postfix + ".ps)");
      else c->Print("output_GetPrediction_WithUncertainties/QCD_presel_highHT" + postfix + ".ps");

      c->Print("output_GetPrediction_WithUncertainties/" + hist_type_presel_highHT.at(i) + postfix + ".png");
   }

   // set search bin cut values for HT and MHT (check with Prediction.C)
   double HTlow = 500.;
   double HTmedium = 800.;
   double HThigh = 1000.;
   double HTveryhigh = 1250.;
   double HTextremehigh = 1500.;
   double MHTlow = 100.;
   double MHTmedium = 200.;
   double MHThigh = 300.;
   double MHTveryhigh = 450.;
   double MHTextremehigh = 600.;
   int SmearRep = 100;

   // ------------------------------------------------------------------------------ //
   // get prediction values - nominal -
   double JetBin1_HTlow_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),
                                                          MHTmedium, MHThigh); 
   double JetBin1_HTlow_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),
                                                          MHThigh, MHTveryhigh);
   double JetBin1_HTlow_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),
                                                          MHTveryhigh, MHTextremehigh);
   double JetBin1_HTlow_MHTextremehigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),                                                          MHTextremehigh, MHTextremehigh);
   double JetBin1_HTmedium_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),
                                                          MHTlow, MHTmedium);
   double JetBin1_HTmedium_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                         MHTmedium, MHThigh);
   double JetBin1_HTmedium_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),
                                                          MHThigh, MHTveryhigh);
   double JetBin1_HTmedium_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                       MHTveryhigh, MHTextremehigh);
   double JetBin1_HTmedium_MHTextremehigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                    MHTextremehigh, MHTextremehigh);
   double JetBin1_HThigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),
                                                          MHTlow, MHTmedium);
   double JetBin1_HThigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                             MHTmedium, MHThigh);
   double JetBin1_HThigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),
                                                          MHThigh, MHTveryhigh);
   double JetBin1_HThigh_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                           MHTveryhigh, MHTextremehigh);
   double JetBin1_HThigh_MHTextremehigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                        MHTextremehigh, MHTextremehigh);
   double JetBin1_HTveryhigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                                        MHTlow, MHTmedium);
   double JetBin1_HTveryhigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                                     MHTmedium, MHThigh);
   double JetBin1_HTveryhigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                                       MHThigh, MHTveryhigh);
   double JetBin1_HTveryhigh_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                                   MHTveryhigh, MHTveryhigh);
   double JetBin1_HTextremehigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"),                                                  MHTlow, MHTmedium);
   double JetBin1_HTextremehigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"),                                               MHTmedium, MHThigh);
   double JetBin1_HTextremehigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"),                                                 MHThigh, MHThigh);


   double JetBin2_HTlow_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),
                                                          MHTmedium, MHThigh); 
   double JetBin2_HTlow_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),
                                                          MHThigh, MHTveryhigh);
   double JetBin2_HTlow_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),
                                                          MHTveryhigh, MHTextremehigh);
   double JetBin2_HTlow_MHTextremehigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),                                                          MHTextremehigh, MHTextremehigh);
   double JetBin2_HTmedium_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),
                                                          MHTlow, MHTmedium);
   double JetBin2_HTmedium_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                         MHTmedium, MHThigh);
   double JetBin2_HTmedium_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),
                                                          MHThigh, MHTveryhigh);
   double JetBin2_HTmedium_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                       MHTveryhigh, MHTextremehigh);
   double JetBin2_HTmedium_MHTextremehigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                    MHTextremehigh, MHTextremehigh);
   double JetBin2_HThigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),
                                                          MHTlow, MHTmedium);
   double JetBin2_HThigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                             MHTmedium, MHThigh);
   double JetBin2_HThigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),
                                                          MHThigh, MHTveryhigh);
   double JetBin2_HThigh_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                           MHTveryhigh, MHTextremehigh);
   double JetBin2_HThigh_MHTextremehigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                        MHTextremehigh, MHTextremehigh);
   double JetBin2_HTveryhigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                                        MHTlow, MHTmedium);
   double JetBin2_HTveryhigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                                     MHTmedium, MHThigh);
   double JetBin2_HTveryhigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                                       MHThigh, MHTveryhigh);
   double JetBin2_HTveryhigh_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                                   MHTveryhigh, MHTveryhigh);
   double JetBin2_HTextremehigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"),                                                  MHTlow, MHTmedium);
   double JetBin2_HTextremehigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"),                                               MHTmedium, MHThigh);
   double JetBin2_HTextremehigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"),                                                 MHThigh, MHThigh);


   double JetBin3_HTlow_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"),
                                                          MHTmedium, MHThigh); 
   double JetBin3_HTlow_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"),
                                                          MHThigh, MHTveryhigh);
   double JetBin3_HTlow_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"),
                                                          MHTveryhigh, MHTveryhigh);
   double JetBin3_HTmedium_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),
                                                          MHTlow, MHTmedium);
   double JetBin3_HTmedium_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),                                                         MHTmedium, MHThigh);
   double JetBin3_HTmedium_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),
                                                          MHThigh, MHTveryhigh);
   double JetBin3_HTmedium_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),                                                       MHTveryhigh, MHTveryhigh);
   double JetBin3_HThigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),
                                                          MHTlow, MHTmedium);
   double JetBin3_HThigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),                                                             MHTmedium, MHThigh);
   double JetBin3_HThigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),
                                                          MHThigh, MHTveryhigh);
   double JetBin3_HThigh_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),                                                           MHTveryhigh, MHTveryhigh);
   double JetBin3_HTveryhigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                                        MHTlow, MHTmedium);
   double JetBin3_HTveryhigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                                     MHTmedium, MHThigh);
   double JetBin3_HTveryhigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                                       MHThigh, MHTveryhigh);
   double JetBin3_HTveryhigh_MHTveryhigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                                   MHTveryhigh, MHTveryhigh);
   double JetBin3_HTextremehigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"),                                                  MHTlow, MHTmedium);
   double JetBin3_HTextremehigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"),                                               MHTmedium, MHThigh);
   double JetBin3_HTextremehigh_MHThigh = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"),                                                 MHThigh, MHThigh);


   double JetBin4_HTlow_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"),
                                                          MHTmedium, MHTmedium);                    
   double JetBin4_HTmedium_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTmedium"),
                                                          MHTlow, MHTmedium);
   double JetBin4_HTmedium_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTmedium"),                                                         MHTmedium, MHTmedium);  
   double JetBin4_HThigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"),
                                                          MHTlow, MHTmedium);
   double JetBin4_HThigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"),                                                             MHTmedium, MHTmedium); 
   double JetBin4_HTveryhigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"),                                                        MHTlow, MHTmedium);
   double JetBin4_HTveryhigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"),                                                     MHTmedium, MHTmedium);
   double JetBin4_HTextremehigh_MHTlow = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"),                                                  MHTlow, MHTmedium);
   double JetBin4_HTextremehigh_MHTmedium = pred_->GetResultValue(pred_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"),                                               MHTmedium, MHTmedium);
  

   // ------------------------------------------------------------------------------ //
   // get prediction uncertainties - statistical -
   double JetBin1_HTlow_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),                                                         MHTmedium, MHThigh); 
   double JetBin1_HTlow_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),
                                                          MHThigh, MHTveryhigh);
   double JetBin1_HTlow_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),                                                       MHTveryhigh, MHTextremehigh);
   double JetBin1_HTlow_MHTextremehigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTlow"),                                                    MHTextremehigh, MHTextremehigh);
   double JetBin1_HTmedium_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                      MHTlow, MHTmedium);
   double JetBin1_HTmedium_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                   MHTmedium, MHThigh);
   double JetBin1_HTmedium_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                     MHThigh, MHTveryhigh);
   double JetBin1_HTmedium_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                                 MHTveryhigh, MHTextremehigh);
   double JetBin1_HTmedium_MHTextremehigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTmedium"),                                              MHTextremehigh, MHTextremehigh);
   double JetBin1_HThigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                          MHTlow, MHTmedium);
   double JetBin1_HThigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                       MHTmedium, MHThigh);
   double JetBin1_HThigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                         MHThigh, MHTveryhigh);
   double JetBin1_HThigh_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                     MHTveryhigh, MHTextremehigh);
   double JetBin1_HThigh_MHTextremehigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HThigh"),                                                  MHTextremehigh, MHTextremehigh);
   double JetBin1_HTveryhigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                                  MHTlow, MHTmedium);
   double JetBin1_HTveryhigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                               MHTmedium, MHThigh);
   double JetBin1_HTveryhigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                                 MHThigh, MHTveryhigh);
   double JetBin1_HTveryhigh_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"),                                             MHTveryhigh, MHTveryhigh);
   double JetBin1_HTextremehigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"),                                            MHTlow, MHTmedium);
   double JetBin1_HTextremehigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"),                                         MHTmedium, MHThigh);
   double JetBin1_HTextremehigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"),                                           MHThigh, MHThigh);


   double JetBin2_HTlow_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),                                                         MHTmedium, MHThigh); 
   double JetBin2_HTlow_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),
                                                          MHThigh, MHTveryhigh);
   double JetBin2_HTlow_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),                                                       MHTveryhigh, MHTextremehigh);
   double JetBin2_HTlow_MHTextremehigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTlow"),                                                    MHTextremehigh, MHTextremehigh);
   double JetBin2_HTmedium_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                      MHTlow, MHTmedium);
   double JetBin2_HTmedium_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                   MHTmedium, MHThigh);
   double JetBin2_HTmedium_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                     MHThigh, MHTveryhigh);
   double JetBin2_HTmedium_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                                 MHTveryhigh, MHTextremehigh);
   double JetBin2_HTmedium_MHTextremehigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTmedium"),                                              MHTextremehigh, MHTextremehigh);
   double JetBin2_HThigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                          MHTlow, MHTmedium);
   double JetBin2_HThigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                       MHTmedium, MHThigh);
   double JetBin2_HThigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                         MHThigh, MHTveryhigh);
   double JetBin2_HThigh_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                     MHTveryhigh, MHTextremehigh);
   double JetBin2_HThigh_MHTextremehigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HThigh"),                                                  MHTextremehigh, MHTextremehigh);
   double JetBin2_HTveryhigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                                  MHTlow, MHTmedium);
   double JetBin2_HTveryhigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                               MHTmedium, MHThigh);
   double JetBin2_HTveryhigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                                 MHThigh, MHTveryhigh);
   double JetBin2_HTveryhigh_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"),                                             MHTveryhigh, MHTveryhigh);
   double JetBin2_HTextremehigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"),                                            MHTlow, MHTmedium);
   double JetBin2_HTextremehigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"),                                         MHTmedium, MHThigh);
   double JetBin2_HTextremehigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"),                                           MHThigh, MHThigh);


   double JetBin3_HTlow_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"),
                                                        MHTmedium, MHThigh); 
   double JetBin3_HTlow_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"),
                                                        MHThigh, MHTveryhigh);
   double JetBin3_HTlow_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTlow"),                                                       MHTveryhigh, MHTveryhigh);
   double JetBin3_HTmedium_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),                                                      MHTlow, MHTmedium);
   double JetBin3_HTmedium_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),                                                   MHTmedium, MHThigh);
   double JetBin3_HTmedium_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),                                                     MHThigh, MHTveryhigh);
   double JetBin3_HTmedium_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTmedium"),                                                 MHTveryhigh, MHTveryhigh);
   double JetBin3_HThigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),
                                                        MHTlow, MHTmedium);
   double JetBin3_HThigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),                                                       MHTmedium, MHThigh);
   double JetBin3_HThigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),
                                                        MHThigh, MHTveryhigh);
   double JetBin3_HThigh_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HThigh"),                                                     MHTveryhigh, MHTveryhigh);
   double JetBin3_HTveryhigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                                  MHTlow, MHTmedium);
   double JetBin3_HTveryhigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                               MHTmedium, MHThigh);
   double JetBin3_HTveryhigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                                 MHThigh, MHTveryhigh);
   double JetBin3_HTveryhigh_MHTveryhigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"),                                             MHTveryhigh, MHTveryhigh);
   double JetBin3_HTextremehigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"),                                            MHTlow, MHTmedium);
   double JetBin3_HTextremehigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"),                                         MHTmedium, MHThigh);
   double JetBin3_HTextremehigh_MHThigh_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"),                                           MHThigh, MHThigh);


   double JetBin4_HTlow_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTlow"),
                                                        MHTmedium, MHTmedium);                    
   double JetBin4_HTmedium_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTmedium"),                                                      MHTlow, MHTmedium);
   double JetBin4_HTmedium_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTmedium"),                                                   MHTmedium, MHTmedium);  
   double JetBin4_HThigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"),
                                                        MHTlow, MHTmedium);
   double JetBin4_HThigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HThigh"),                                                       MHTmedium, MHTmedium); 
   double JetBin4_HTveryhigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"),                                                  MHTlow, MHTmedium);
   double JetBin4_HTveryhigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"),                                               MHTmedium, MHTmedium);
   double JetBin4_HTextremehigh_MHTlow_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"),                                            MHTlow, MHTmedium);
   double JetBin4_HTextremehigh_MHTmedium_error = pred_->GetResultError(pred_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"),                                         MHTmedium, MHTmedium);

   // ------------------------------------------------------------------------------ //
   // get prediction uncertainties - CoreUp -
   double JetBin1_HTlow_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHThigh) - JetBin1_HTlow_MHTmedium)/JetBin1_HTlow_MHTmedium; 
   double JetBin1_HTlow_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHThigh, MHTveryhigh) - JetBin1_HTlow_MHThigh)/JetBin1_HTlow_MHThigh;
   double JetBin1_HTlow_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin1_HTlow_MHTveryhigh)/JetBin1_HTlow_MHTveryhigh;
   double JetBin1_HTlow_MHTextremehigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin1_HTlow_MHTextremehigh)/JetBin1_HTlow_MHTextremehigh;
   double JetBin1_HTmedium_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTlow, MHTmedium) - JetBin1_HTmedium_MHTlow)/JetBin1_HTmedium_MHTlow;
   double JetBin1_HTmedium_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTmedium, MHThigh) - JetBin1_HTmedium_MHTmedium)/JetBin1_HTmedium_MHTmedium;
   double JetBin1_HTmedium_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHThigh, MHTveryhigh) - JetBin1_HTmedium_MHThigh)/JetBin1_HTmedium_MHThigh;
   double JetBin1_HTmedium_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin1_HTmedium_MHTveryhigh)/JetBin1_HTmedium_MHTveryhigh;
   double JetBin1_HTmedium_MHTextremehigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin1_HTmedium_MHTextremehigh)/JetBin1_HTmedium_MHTextremehigh;
   double JetBin1_HThigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) - JetBin1_HThigh_MHTlow)/JetBin1_HThigh_MHTlow;
   double JetBin1_HThigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHThigh) - JetBin1_HThigh_MHTmedium)/JetBin1_HThigh_MHTmedium;
   double JetBin1_HThigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHThigh, MHTveryhigh) - JetBin1_HThigh_MHThigh)/JetBin1_HThigh_MHThigh;
   double JetBin1_HThigh_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin1_HThigh_MHTveryhigh)/JetBin1_HThigh_MHTveryhigh;
   double JetBin1_HThigh_MHTextremehigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin1_HThigh_MHTextremehigh)/JetBin1_HThigh_MHTextremehigh;
   double JetBin1_HTveryhigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTlow, MHTmedium) - JetBin1_HTveryhigh_MHTlow)/JetBin1_HTveryhigh_MHTlow;
   double JetBin1_HTveryhigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTmedium, MHThigh) - JetBin1_HTveryhigh_MHTmedium)/JetBin1_HTveryhigh_MHTmedium;
   double JetBin1_HTveryhigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin1_HTveryhigh_MHThigh)/JetBin1_HTveryhigh_MHThigh;
   double JetBin1_HTveryhigh_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin1_HTveryhigh_MHTveryhigh)/JetBin1_HTveryhigh_MHTveryhigh;
   double JetBin1_HTextremehigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTlow, MHTmedium) - JetBin1_HTextremehigh_MHTlow)/JetBin1_HTextremehigh_MHTlow;
   double JetBin1_HTextremehigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTmedium, MHThigh) - JetBin1_HTextremehigh_MHTmedium)/JetBin1_HTextremehigh_MHTmedium;
   double JetBin1_HTextremehigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHThigh, MHThigh) - JetBin1_HTextremehigh_MHThigh)/JetBin1_HTextremehigh_MHThigh;


   double JetBin2_HTlow_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHThigh) - JetBin2_HTlow_MHTmedium)/JetBin2_HTlow_MHTmedium; 
   double JetBin2_HTlow_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHThigh, MHTveryhigh) - JetBin2_HTlow_MHThigh)/JetBin2_HTlow_MHThigh;
   double JetBin2_HTlow_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin2_HTlow_MHTveryhigh)/JetBin2_HTlow_MHTveryhigh;
   double JetBin2_HTlow_MHTextremehigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin2_HTlow_MHTextremehigh)/JetBin2_HTlow_MHTextremehigh;
   double JetBin2_HTmedium_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTlow, MHTmedium) - JetBin2_HTmedium_MHTlow)/JetBin2_HTmedium_MHTlow;
   double JetBin2_HTmedium_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTmedium, MHThigh) - JetBin2_HTmedium_MHTmedium)/JetBin2_HTmedium_MHTmedium;
   double JetBin2_HTmedium_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHThigh, MHTveryhigh) - JetBin2_HTmedium_MHThigh)/JetBin2_HTmedium_MHThigh;
   double JetBin2_HTmedium_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin2_HTmedium_MHTveryhigh)/JetBin2_HTmedium_MHTveryhigh;
   double JetBin2_HTmedium_MHTextremehigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin2_HTmedium_MHTextremehigh)/JetBin2_HTmedium_MHTextremehigh;
   double JetBin2_HThigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) - JetBin2_HThigh_MHTlow)/JetBin2_HThigh_MHTlow;
   double JetBin2_HThigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHThigh) - JetBin2_HThigh_MHTmedium)/JetBin2_HThigh_MHTmedium;
   double JetBin2_HThigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHThigh, MHTveryhigh) - JetBin2_HThigh_MHThigh)/JetBin2_HThigh_MHThigh;
   double JetBin2_HThigh_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin2_HThigh_MHTveryhigh)/JetBin2_HThigh_MHTveryhigh;
   double JetBin2_HThigh_MHTextremehigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin2_HThigh_MHTextremehigh)/JetBin2_HThigh_MHTextremehigh;
   double JetBin2_HTveryhigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTlow, MHTmedium) - JetBin2_HTveryhigh_MHTlow)/JetBin2_HTveryhigh_MHTlow;
   double JetBin2_HTveryhigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTmedium, MHThigh) - JetBin2_HTveryhigh_MHTmedium)/JetBin2_HTveryhigh_MHTmedium;
   double JetBin2_HTveryhigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin2_HTveryhigh_MHThigh)/JetBin2_HTveryhigh_MHThigh;
   double JetBin2_HTveryhigh_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin2_HTveryhigh_MHTveryhigh)/JetBin2_HTveryhigh_MHTveryhigh;
   double JetBin2_HTextremehigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTlow, MHTmedium) - JetBin2_HTextremehigh_MHTlow)/JetBin2_HTextremehigh_MHTlow;
   double JetBin2_HTextremehigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTmedium, MHThigh) - JetBin2_HTextremehigh_MHTmedium)/JetBin2_HTextremehigh_MHTmedium;
   double JetBin2_HTextremehigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHThigh, MHThigh) - JetBin2_HTextremehigh_MHThigh)/JetBin2_HTextremehigh_MHThigh;


   double JetBin3_HTlow_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHThigh) - JetBin3_HTlow_MHTmedium)/JetBin3_HTlow_MHTmedium; 
   double JetBin3_HTlow_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHThigh, MHTveryhigh) - JetBin3_HTlow_MHThigh)/JetBin3_HTlow_MHThigh;
   double JetBin3_HTlow_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTveryhigh, MHTveryhigh) - JetBin3_HTlow_MHTveryhigh)/JetBin3_HTlow_MHTveryhigh;
   double JetBin3_HTmedium_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTlow, MHTmedium) - JetBin3_HTmedium_MHTlow)/JetBin3_HTmedium_MHTlow;
   double JetBin3_HTmedium_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTmedium, MHThigh) - JetBin3_HTmedium_MHTmedium)/JetBin3_HTmedium_MHTmedium;
   double JetBin3_HTmedium_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHThigh, MHTveryhigh) - JetBin3_HTmedium_MHThigh)/JetBin3_HTmedium_MHThigh;
   double JetBin3_HTmedium_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTveryhigh, MHTveryhigh) - JetBin3_HTmedium_MHTveryhigh)/JetBin3_HTmedium_MHTveryhigh;
   double JetBin3_HThigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) - JetBin3_HThigh_MHTlow)/JetBin3_HThigh_MHTlow;
   double JetBin3_HThigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHThigh) - JetBin3_HThigh_MHTmedium)/JetBin3_HThigh_MHTmedium;
   double JetBin3_HThigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHThigh, MHTveryhigh) - JetBin3_HThigh_MHThigh)/JetBin3_HThigh_MHThigh;
   double JetBin3_HThigh_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HThigh_MHTveryhigh)/JetBin3_HThigh_MHTveryhigh;
   double JetBin3_HTveryhigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTlow, MHTmedium) - JetBin3_HTveryhigh_MHTlow)/JetBin3_HTveryhigh_MHTlow;
   double JetBin3_HTveryhigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTmedium, MHThigh) - JetBin3_HTveryhigh_MHTmedium)/JetBin3_HTveryhigh_MHTmedium;
   double JetBin3_HTveryhigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin3_HTveryhigh_MHThigh)/JetBin3_HTveryhigh_MHThigh;
   double JetBin3_HTveryhigh_MHTveryhigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HTveryhigh_MHTveryhigh)/JetBin3_HTveryhigh_MHTveryhigh;
   double JetBin3_HTextremehigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTlow, MHTmedium) - JetBin3_HTextremehigh_MHTlow)/JetBin3_HTextremehigh_MHTlow;
   double JetBin3_HTextremehigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTmedium, MHThigh) - JetBin3_HTextremehigh_MHTmedium)/JetBin3_HTextremehigh_MHTmedium;
   double JetBin3_HTextremehigh_MHThigh_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHThigh, MHThigh) - JetBin3_HTextremehigh_MHThigh)/JetBin3_HTextremehigh_MHThigh;
   
   
   double JetBin4_HTlow_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) - JetBin4_HTlow_MHTmedium)/JetBin4_HTlow_MHTmedium;                    
   double JetBin4_HTmedium_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTlow, MHTmedium) - JetBin4_HTmedium_MHTlow)/JetBin4_HTmedium_MHTlow;
   double JetBin4_HTmedium_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTmedium, MHTmedium) - JetBin4_HTmedium_MHTmedium)/JetBin4_HTmedium_MHTmedium;  
   double JetBin4_HThigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) - JetBin4_HThigh_MHTlow)/JetBin4_HThigh_MHTlow;
   double JetBin4_HThigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) - JetBin4_HThigh_MHTmedium)/JetBin4_HThigh_MHTmedium; 
   double JetBin4_HTveryhigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTlow, MHTmedium) - JetBin4_HTveryhigh_MHTlow)/JetBin4_HTveryhigh_MHTlow;
   double JetBin4_HTveryhigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTmedium, MHTmedium) - JetBin4_HTveryhigh_MHTmedium)/JetBin4_HTveryhigh_MHTmedium;
   double JetBin4_HTextremehigh_MHTlow_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTlow, MHTmedium) - JetBin4_HTextremehigh_MHTlow)/JetBin4_HTextremehigh_MHTlow;
   double JetBin4_HTextremehigh_MHTmedium_CoreUP = (pred_CoreUP_->GetResultValue(pred_CoreUP_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTmedium, MHTmedium) - JetBin4_HTextremehigh_MHTmedium)/JetBin4_HTextremehigh_MHTmedium;

   // ------------------------------------------------------------------------------ //
   // get prediction uncertainties - CoreDN -
   double JetBin1_HTlow_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHThigh) - JetBin1_HTlow_MHTmedium)/JetBin1_HTlow_MHTmedium; 
   double JetBin1_HTlow_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHThigh, MHTveryhigh) - JetBin1_HTlow_MHThigh)/JetBin1_HTlow_MHThigh;
   double JetBin1_HTlow_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin1_HTlow_MHTveryhigh)/JetBin1_HTlow_MHTveryhigh;
   double JetBin1_HTlow_MHTextremehigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin1_HTlow_MHTextremehigh)/JetBin1_HTlow_MHTextremehigh;
   double JetBin1_HTmedium_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTlow, MHTmedium) - JetBin1_HTmedium_MHTlow)/JetBin1_HTmedium_MHTlow;
   double JetBin1_HTmedium_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTmedium, MHThigh) - JetBin1_HTmedium_MHTmedium)/JetBin1_HTmedium_MHTmedium;
   double JetBin1_HTmedium_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHThigh, MHTveryhigh) - JetBin1_HTmedium_MHThigh)/JetBin1_HTmedium_MHThigh;
   double JetBin1_HTmedium_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin1_HTmedium_MHTveryhigh)/JetBin1_HTmedium_MHTveryhigh;
   double JetBin1_HTmedium_MHTextremehigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin1_HTmedium_MHTextremehigh)/JetBin1_HTmedium_MHTextremehigh;
   double JetBin1_HThigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) - JetBin1_HThigh_MHTlow)/JetBin1_HThigh_MHTlow;
   double JetBin1_HThigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHThigh) - JetBin1_HThigh_MHTmedium)/JetBin1_HThigh_MHTmedium;
   double JetBin1_HThigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHThigh, MHTveryhigh) - JetBin1_HThigh_MHThigh)/JetBin1_HThigh_MHThigh;
   double JetBin1_HThigh_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin1_HThigh_MHTveryhigh)/JetBin1_HThigh_MHTveryhigh;
   double JetBin1_HThigh_MHTextremehigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin1_HThigh_MHTextremehigh)/JetBin1_HThigh_MHTextremehigh;
   double JetBin1_HTveryhigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTlow, MHTmedium) - JetBin1_HTveryhigh_MHTlow)/JetBin1_HTveryhigh_MHTlow;
   double JetBin1_HTveryhigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTmedium, MHThigh) - JetBin1_HTveryhigh_MHTmedium)/JetBin1_HTveryhigh_MHTmedium;
   double JetBin1_HTveryhigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin1_HTveryhigh_MHThigh)/JetBin1_HTveryhigh_MHThigh;
   double JetBin1_HTveryhigh_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin1_HTveryhigh_MHTveryhigh)/JetBin1_HTveryhigh_MHTveryhigh;
   double JetBin1_HTextremehigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTlow, MHTmedium) - JetBin1_HTextremehigh_MHTlow)/JetBin1_HTextremehigh_MHTlow;
   double JetBin1_HTextremehigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTmedium, MHThigh) - JetBin1_HTextremehigh_MHTmedium)/JetBin1_HTextremehigh_MHTmedium;
   double JetBin1_HTextremehigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHThigh, MHThigh) - JetBin1_HTextremehigh_MHThigh)/JetBin1_HTextremehigh_MHThigh;


   double JetBin2_HTlow_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHThigh) - JetBin2_HTlow_MHTmedium)/JetBin2_HTlow_MHTmedium; 
   double JetBin2_HTlow_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHThigh, MHTveryhigh) - JetBin2_HTlow_MHThigh)/JetBin2_HTlow_MHThigh;
   double JetBin2_HTlow_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin2_HTlow_MHTveryhigh)/JetBin2_HTlow_MHTveryhigh;
   double JetBin2_HTlow_MHTextremehigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin2_HTlow_MHTextremehigh)/JetBin2_HTlow_MHTextremehigh;
   double JetBin2_HTmedium_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTlow, MHTmedium) - JetBin2_HTmedium_MHTlow)/JetBin2_HTmedium_MHTlow;
   double JetBin2_HTmedium_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTmedium, MHThigh) - JetBin2_HTmedium_MHTmedium)/JetBin2_HTmedium_MHTmedium;
   double JetBin2_HTmedium_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHThigh, MHTveryhigh) - JetBin2_HTmedium_MHThigh)/JetBin2_HTmedium_MHThigh;
   double JetBin2_HTmedium_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin2_HTmedium_MHTveryhigh)/JetBin2_HTmedium_MHTveryhigh;
   double JetBin2_HTmedium_MHTextremehigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin2_HTmedium_MHTextremehigh)/JetBin2_HTmedium_MHTextremehigh;
   double JetBin2_HThigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) - JetBin2_HThigh_MHTlow)/JetBin2_HThigh_MHTlow;
   double JetBin2_HThigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHThigh) - JetBin2_HThigh_MHTmedium)/JetBin2_HThigh_MHTmedium;
   double JetBin2_HThigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHThigh, MHTveryhigh) - JetBin2_HThigh_MHThigh)/JetBin2_HThigh_MHThigh;
   double JetBin2_HThigh_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin2_HThigh_MHTveryhigh)/JetBin2_HThigh_MHTveryhigh;
   double JetBin2_HThigh_MHTextremehigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin2_HThigh_MHTextremehigh)/JetBin2_HThigh_MHTextremehigh;
   double JetBin2_HTveryhigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTlow, MHTmedium) - JetBin2_HTveryhigh_MHTlow)/JetBin2_HTveryhigh_MHTlow;
   double JetBin2_HTveryhigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTmedium, MHThigh) - JetBin2_HTveryhigh_MHTmedium)/JetBin2_HTveryhigh_MHTmedium;
   double JetBin2_HTveryhigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin2_HTveryhigh_MHThigh)/JetBin2_HTveryhigh_MHThigh;
   double JetBin2_HTveryhigh_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin2_HTveryhigh_MHTveryhigh)/JetBin2_HTveryhigh_MHTveryhigh;
   double JetBin2_HTextremehigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTlow, MHTmedium) - JetBin2_HTextremehigh_MHTlow)/JetBin2_HTextremehigh_MHTlow;
   double JetBin2_HTextremehigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTmedium, MHThigh) - JetBin2_HTextremehigh_MHTmedium)/JetBin2_HTextremehigh_MHTmedium;
   double JetBin2_HTextremehigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHThigh, MHThigh) - JetBin2_HTextremehigh_MHThigh)/JetBin2_HTextremehigh_MHThigh;


   double JetBin3_HTlow_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHThigh) - JetBin3_HTlow_MHTmedium)/JetBin3_HTlow_MHTmedium; 
   double JetBin3_HTlow_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHThigh, MHTveryhigh) - JetBin3_HTlow_MHThigh)/JetBin3_HTlow_MHThigh;
   double JetBin3_HTlow_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTveryhigh, MHTveryhigh) - JetBin3_HTlow_MHTveryhigh)/JetBin3_HTlow_MHTveryhigh;
   double JetBin3_HTmedium_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTlow, MHTmedium) - JetBin3_HTmedium_MHTlow)/JetBin3_HTmedium_MHTlow;
   double JetBin3_HTmedium_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTmedium, MHThigh) - JetBin3_HTmedium_MHTmedium)/JetBin3_HTmedium_MHTmedium;
   double JetBin3_HTmedium_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHThigh, MHTveryhigh) - JetBin3_HTmedium_MHThigh)/JetBin3_HTmedium_MHThigh;
   double JetBin3_HTmedium_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTveryhigh, MHTveryhigh) - JetBin3_HTmedium_MHTveryhigh)/JetBin3_HTmedium_MHTveryhigh;
   double JetBin3_HThigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) - JetBin3_HThigh_MHTlow)/JetBin3_HThigh_MHTlow;
   double JetBin3_HThigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHThigh) - JetBin3_HThigh_MHTmedium)/JetBin3_HThigh_MHTmedium;
   double JetBin3_HThigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHThigh, MHTveryhigh) - JetBin3_HThigh_MHThigh)/JetBin3_HThigh_MHThigh;
   double JetBin3_HThigh_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HThigh_MHTveryhigh)/JetBin3_HThigh_MHTveryhigh;
   double JetBin3_HTveryhigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTlow, MHTmedium) - JetBin3_HTveryhigh_MHTlow)/JetBin3_HTveryhigh_MHTlow;
   double JetBin3_HTveryhigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTmedium, MHThigh) - JetBin3_HTveryhigh_MHTmedium)/JetBin3_HTveryhigh_MHTmedium;
   double JetBin3_HTveryhigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin3_HTveryhigh_MHThigh)/JetBin3_HTveryhigh_MHThigh;
   double JetBin3_HTveryhigh_MHTveryhigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HTveryhigh_MHTveryhigh)/JetBin3_HTveryhigh_MHTveryhigh;
   double JetBin3_HTextremehigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTlow, MHTmedium) - JetBin3_HTextremehigh_MHTlow)/JetBin3_HTextremehigh_MHTlow;
   double JetBin3_HTextremehigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTmedium, MHThigh) - JetBin3_HTextremehigh_MHTmedium)/JetBin3_HTextremehigh_MHTmedium;
   double JetBin3_HTextremehigh_MHThigh_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHThigh, MHThigh) - JetBin3_HTextremehigh_MHThigh)/JetBin3_HTextremehigh_MHThigh;
   
   
   double JetBin4_HTlow_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) - JetBin4_HTlow_MHTmedium)/JetBin4_HTlow_MHTmedium;                    
   double JetBin4_HTmedium_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTlow, MHTmedium) - JetBin4_HTmedium_MHTlow)/JetBin4_HTmedium_MHTlow;
   double JetBin4_HTmedium_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTmedium, MHTmedium) - JetBin4_HTmedium_MHTmedium)/JetBin4_HTmedium_MHTmedium;  
   double JetBin4_HThigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) - JetBin4_HThigh_MHTlow)/JetBin4_HThigh_MHTlow;
   double JetBin4_HThigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) - JetBin4_HThigh_MHTmedium)/JetBin4_HThigh_MHTmedium; 
   double JetBin4_HTveryhigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTlow, MHTmedium) - JetBin4_HTveryhigh_MHTlow)/JetBin4_HTveryhigh_MHTlow;
   double JetBin4_HTveryhigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTmedium, MHTmedium) - JetBin4_HTveryhigh_MHTmedium)/JetBin4_HTveryhigh_MHTmedium;
   double JetBin4_HTextremehigh_MHTlow_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTlow, MHTmedium) - JetBin4_HTextremehigh_MHTlow)/JetBin4_HTextremehigh_MHTlow;
   double JetBin4_HTextremehigh_MHTmedium_CoreDN = (pred_CoreDN_->GetResultValue(pred_CoreDN_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTmedium, MHTmedium) - JetBin4_HTextremehigh_MHTmedium)/JetBin4_HTextremehigh_MHTmedium;

   // ------------------------------------------------------------------------------ //
   // get prediction uncertainties - TailUp -
   double JetBin1_HTlow_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHThigh) - JetBin1_HTlow_MHTmedium)/JetBin1_HTlow_MHTmedium; 
   double JetBin1_HTlow_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHThigh, MHTveryhigh) - JetBin1_HTlow_MHThigh)/JetBin1_HTlow_MHThigh;
   double JetBin1_HTlow_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin1_HTlow_MHTveryhigh)/JetBin1_HTlow_MHTveryhigh;
   double JetBin1_HTlow_MHTextremehigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin1_HTlow_MHTextremehigh)/JetBin1_HTlow_MHTextremehigh;
   double JetBin1_HTmedium_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTlow, MHTmedium) - JetBin1_HTmedium_MHTlow)/JetBin1_HTmedium_MHTlow;
   double JetBin1_HTmedium_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTmedium, MHThigh) - JetBin1_HTmedium_MHTmedium)/JetBin1_HTmedium_MHTmedium;
   double JetBin1_HTmedium_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHThigh, MHTveryhigh) - JetBin1_HTmedium_MHThigh)/JetBin1_HTmedium_MHThigh;
   double JetBin1_HTmedium_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin1_HTmedium_MHTveryhigh)/JetBin1_HTmedium_MHTveryhigh;
   double JetBin1_HTmedium_MHTextremehigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin1_HTmedium_MHTextremehigh)/JetBin1_HTmedium_MHTextremehigh;
   double JetBin1_HThigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) - JetBin1_HThigh_MHTlow)/JetBin1_HThigh_MHTlow;
   double JetBin1_HThigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHThigh) - JetBin1_HThigh_MHTmedium)/JetBin1_HThigh_MHTmedium;
   double JetBin1_HThigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHThigh, MHTveryhigh) - JetBin1_HThigh_MHThigh)/JetBin1_HThigh_MHThigh;
   double JetBin1_HThigh_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin1_HThigh_MHTveryhigh)/JetBin1_HThigh_MHTveryhigh;
   double JetBin1_HThigh_MHTextremehigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin1_HThigh_MHTextremehigh)/JetBin1_HThigh_MHTextremehigh;
   double JetBin1_HTveryhigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTlow, MHTmedium) - JetBin1_HTveryhigh_MHTlow)/JetBin1_HTveryhigh_MHTlow;
   double JetBin1_HTveryhigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTmedium, MHThigh) - JetBin1_HTveryhigh_MHTmedium)/JetBin1_HTveryhigh_MHTmedium;
   double JetBin1_HTveryhigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin1_HTveryhigh_MHThigh)/JetBin1_HTveryhigh_MHThigh;
   double JetBin1_HTveryhigh_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin1_HTveryhigh_MHTveryhigh)/JetBin1_HTveryhigh_MHTveryhigh;
   double JetBin1_HTextremehigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTlow, MHTmedium) - JetBin1_HTextremehigh_MHTlow)/JetBin1_HTextremehigh_MHTlow;
   double JetBin1_HTextremehigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTmedium, MHThigh) - JetBin1_HTextremehigh_MHTmedium)/JetBin1_HTextremehigh_MHTmedium;
   double JetBin1_HTextremehigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHThigh, MHThigh) - JetBin1_HTextremehigh_MHThigh)/JetBin1_HTextremehigh_MHThigh;


   double JetBin2_HTlow_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHThigh) - JetBin2_HTlow_MHTmedium)/JetBin2_HTlow_MHTmedium; 
   double JetBin2_HTlow_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHThigh, MHTveryhigh) - JetBin2_HTlow_MHThigh)/JetBin2_HTlow_MHThigh;
   double JetBin2_HTlow_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin2_HTlow_MHTveryhigh)/JetBin2_HTlow_MHTveryhigh;
   double JetBin2_HTlow_MHTextremehigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin2_HTlow_MHTextremehigh)/JetBin2_HTlow_MHTextremehigh;
   double JetBin2_HTmedium_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTlow, MHTmedium) - JetBin2_HTmedium_MHTlow)/JetBin2_HTmedium_MHTlow;
   double JetBin2_HTmedium_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTmedium, MHThigh) - JetBin2_HTmedium_MHTmedium)/JetBin2_HTmedium_MHTmedium;
   double JetBin2_HTmedium_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHThigh, MHTveryhigh) - JetBin2_HTmedium_MHThigh)/JetBin2_HTmedium_MHThigh;
   double JetBin2_HTmedium_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin2_HTmedium_MHTveryhigh)/JetBin2_HTmedium_MHTveryhigh;
   double JetBin2_HTmedium_MHTextremehigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin2_HTmedium_MHTextremehigh)/JetBin2_HTmedium_MHTextremehigh;
   double JetBin2_HThigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) - JetBin2_HThigh_MHTlow)/JetBin2_HThigh_MHTlow;
   double JetBin2_HThigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHThigh) - JetBin2_HThigh_MHTmedium)/JetBin2_HThigh_MHTmedium;
   double JetBin2_HThigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHThigh, MHTveryhigh) - JetBin2_HThigh_MHThigh)/JetBin2_HThigh_MHThigh;
   double JetBin2_HThigh_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin2_HThigh_MHTveryhigh)/JetBin2_HThigh_MHTveryhigh;
   double JetBin2_HThigh_MHTextremehigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin2_HThigh_MHTextremehigh)/JetBin2_HThigh_MHTextremehigh;
   double JetBin2_HTveryhigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTlow, MHTmedium) - JetBin2_HTveryhigh_MHTlow)/JetBin2_HTveryhigh_MHTlow;
   double JetBin2_HTveryhigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTmedium, MHThigh) - JetBin2_HTveryhigh_MHTmedium)/JetBin2_HTveryhigh_MHTmedium;
   double JetBin2_HTveryhigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin2_HTveryhigh_MHThigh)/JetBin2_HTveryhigh_MHThigh;
   double JetBin2_HTveryhigh_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin2_HTveryhigh_MHTveryhigh)/JetBin2_HTveryhigh_MHTveryhigh;
   double JetBin2_HTextremehigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTlow, MHTmedium) - JetBin2_HTextremehigh_MHTlow)/JetBin2_HTextremehigh_MHTlow;
   double JetBin2_HTextremehigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTmedium, MHThigh) - JetBin2_HTextremehigh_MHTmedium)/JetBin2_HTextremehigh_MHTmedium;
   double JetBin2_HTextremehigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHThigh, MHThigh) - JetBin2_HTextremehigh_MHThigh)/JetBin2_HTextremehigh_MHThigh;


   double JetBin3_HTlow_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHThigh) - JetBin3_HTlow_MHTmedium)/JetBin3_HTlow_MHTmedium; 
   double JetBin3_HTlow_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHThigh, MHTveryhigh) - JetBin3_HTlow_MHThigh)/JetBin3_HTlow_MHThigh;
   double JetBin3_HTlow_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTveryhigh, MHTveryhigh) - JetBin3_HTlow_MHTveryhigh)/JetBin3_HTlow_MHTveryhigh;
   double JetBin3_HTmedium_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTlow, MHTmedium) - JetBin3_HTmedium_MHTlow)/JetBin3_HTmedium_MHTlow;
   double JetBin3_HTmedium_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTmedium, MHThigh) - JetBin3_HTmedium_MHTmedium)/JetBin3_HTmedium_MHTmedium;
   double JetBin3_HTmedium_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHThigh, MHTveryhigh) - JetBin3_HTmedium_MHThigh)/JetBin3_HTmedium_MHThigh;
   double JetBin3_HTmedium_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTveryhigh, MHTveryhigh) - JetBin3_HTmedium_MHTveryhigh)/JetBin3_HTmedium_MHTveryhigh;
   double JetBin3_HThigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) - JetBin3_HThigh_MHTlow)/JetBin3_HThigh_MHTlow;
   double JetBin3_HThigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHThigh) - JetBin3_HThigh_MHTmedium)/JetBin3_HThigh_MHTmedium;
   double JetBin3_HThigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHThigh, MHTveryhigh) - JetBin3_HThigh_MHThigh)/JetBin3_HThigh_MHThigh;
   double JetBin3_HThigh_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HThigh_MHTveryhigh)/JetBin3_HThigh_MHTveryhigh;
   double JetBin3_HTveryhigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTlow, MHTmedium) - JetBin3_HTveryhigh_MHTlow)/JetBin3_HTveryhigh_MHTlow;
   double JetBin3_HTveryhigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTmedium, MHThigh) - JetBin3_HTveryhigh_MHTmedium)/JetBin3_HTveryhigh_MHTmedium;
   double JetBin3_HTveryhigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin3_HTveryhigh_MHThigh)/JetBin3_HTveryhigh_MHThigh;
   double JetBin3_HTveryhigh_MHTveryhigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HTveryhigh_MHTveryhigh)/JetBin3_HTveryhigh_MHTveryhigh;
   double JetBin3_HTextremehigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTlow, MHTmedium) - JetBin3_HTextremehigh_MHTlow)/JetBin3_HTextremehigh_MHTlow;
   double JetBin3_HTextremehigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTmedium, MHThigh) - JetBin3_HTextremehigh_MHTmedium)/JetBin3_HTextremehigh_MHTmedium;
   double JetBin3_HTextremehigh_MHThigh_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHThigh, MHThigh) - JetBin3_HTextremehigh_MHThigh)/JetBin3_HTextremehigh_MHThigh;
   
   
   double JetBin4_HTlow_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) - JetBin4_HTlow_MHTmedium)/JetBin4_HTlow_MHTmedium;                    
   double JetBin4_HTmedium_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTlow, MHTmedium) - JetBin4_HTmedium_MHTlow)/JetBin4_HTmedium_MHTlow;
   double JetBin4_HTmedium_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTmedium, MHTmedium) - JetBin4_HTmedium_MHTmedium)/JetBin4_HTmedium_MHTmedium;  
   double JetBin4_HThigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) - JetBin4_HThigh_MHTlow)/JetBin4_HThigh_MHTlow;
   double JetBin4_HThigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) - JetBin4_HThigh_MHTmedium)/JetBin4_HThigh_MHTmedium; 
   double JetBin4_HTveryhigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTlow, MHTmedium) - JetBin4_HTveryhigh_MHTlow)/JetBin4_HTveryhigh_MHTlow;
   double JetBin4_HTveryhigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTmedium, MHTmedium) - JetBin4_HTveryhigh_MHTmedium)/JetBin4_HTveryhigh_MHTmedium;
   double JetBin4_HTextremehigh_MHTlow_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTlow, MHTmedium) - JetBin4_HTextremehigh_MHTlow)/JetBin4_HTextremehigh_MHTlow;
   double JetBin4_HTextremehigh_MHTmedium_TailUP = (pred_TailUP_->GetResultValue(pred_TailUP_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTmedium, MHTmedium) - JetBin4_HTextremehigh_MHTmedium)/JetBin4_HTextremehigh_MHTmedium;

   // ------------------------------------------------------------------------------ //
   // get prediction uncertainties - TailDN -
   double JetBin1_HTlow_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTmedium, MHThigh) - JetBin1_HTlow_MHTmedium)/JetBin1_HTlow_MHTmedium; 
   double JetBin1_HTlow_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHThigh, MHTveryhigh) - JetBin1_HTlow_MHThigh)/JetBin1_HTlow_MHThigh;
   double JetBin1_HTlow_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin1_HTlow_MHTveryhigh)/JetBin1_HTlow_MHTveryhigh;
   double JetBin1_HTlow_MHTextremehigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin1_HTlow_MHTextremehigh)/JetBin1_HTlow_MHTextremehigh;
   double JetBin1_HTmedium_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTlow, MHTmedium) - JetBin1_HTmedium_MHTlow)/JetBin1_HTmedium_MHTlow;
   double JetBin1_HTmedium_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTmedium, MHThigh) - JetBin1_HTmedium_MHTmedium)/JetBin1_HTmedium_MHTmedium;
   double JetBin1_HTmedium_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHThigh, MHTveryhigh) - JetBin1_HTmedium_MHThigh)/JetBin1_HTmedium_MHThigh;
   double JetBin1_HTmedium_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin1_HTmedium_MHTveryhigh)/JetBin1_HTmedium_MHTveryhigh;
   double JetBin1_HTmedium_MHTextremehigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin1_HTmedium_MHTextremehigh)/JetBin1_HTmedium_MHTextremehigh;
   double JetBin1_HThigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTlow, MHTmedium) - JetBin1_HThigh_MHTlow)/JetBin1_HThigh_MHTlow;
   double JetBin1_HThigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTmedium, MHThigh) - JetBin1_HThigh_MHTmedium)/JetBin1_HThigh_MHTmedium;
   double JetBin1_HThigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHThigh, MHTveryhigh) - JetBin1_HThigh_MHThigh)/JetBin1_HThigh_MHThigh;
   double JetBin1_HThigh_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin1_HThigh_MHTveryhigh)/JetBin1_HThigh_MHTveryhigh;
   double JetBin1_HThigh_MHTextremehigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin1_HThigh_MHTextremehigh)/JetBin1_HThigh_MHTextremehigh;
   double JetBin1_HTveryhigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTlow, MHTmedium) - JetBin1_HTveryhigh_MHTlow)/JetBin1_HTveryhigh_MHTlow;
   double JetBin1_HTveryhigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTmedium, MHThigh) - JetBin1_HTveryhigh_MHTmedium)/JetBin1_HTveryhigh_MHTmedium;
   double JetBin1_HTveryhigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin1_HTveryhigh_MHThigh)/JetBin1_HTveryhigh_MHThigh;
   double JetBin1_HTveryhigh_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin1_HTveryhigh_MHTveryhigh)/JetBin1_HTveryhigh_MHTveryhigh;
   double JetBin1_HTextremehigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTlow, MHTmedium) - JetBin1_HTextremehigh_MHTlow)/JetBin1_HTextremehigh_MHTlow;
   double JetBin1_HTextremehigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHTmedium, MHThigh) - JetBin1_HTextremehigh_MHTmedium)/JetBin1_HTextremehigh_MHTmedium;
   double JetBin1_HTextremehigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin1_HTextremehigh"), MHThigh, MHThigh) - JetBin1_HTextremehigh_MHThigh)/JetBin1_HTextremehigh_MHThigh;


   double JetBin2_HTlow_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTmedium, MHThigh) - JetBin2_HTlow_MHTmedium)/JetBin2_HTlow_MHTmedium; 
   double JetBin2_HTlow_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHThigh, MHTveryhigh) - JetBin2_HTlow_MHThigh)/JetBin2_HTlow_MHThigh;
   double JetBin2_HTlow_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTveryhigh, MHTextremehigh) - JetBin2_HTlow_MHTveryhigh)/JetBin2_HTlow_MHTveryhigh;
   double JetBin2_HTlow_MHTextremehigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTlow"), MHTextremehigh, MHTextremehigh) - JetBin2_HTlow_MHTextremehigh)/JetBin2_HTlow_MHTextremehigh;
   double JetBin2_HTmedium_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTlow, MHTmedium) - JetBin2_HTmedium_MHTlow)/JetBin2_HTmedium_MHTlow;
   double JetBin2_HTmedium_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTmedium, MHThigh) - JetBin2_HTmedium_MHTmedium)/JetBin2_HTmedium_MHTmedium;
   double JetBin2_HTmedium_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHThigh, MHTveryhigh) - JetBin2_HTmedium_MHThigh)/JetBin2_HTmedium_MHThigh;
   double JetBin2_HTmedium_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTveryhigh, MHTextremehigh) - JetBin2_HTmedium_MHTveryhigh)/JetBin2_HTmedium_MHTveryhigh;
   double JetBin2_HTmedium_MHTextremehigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTmedium"), MHTextremehigh, MHTextremehigh) - JetBin2_HTmedium_MHTextremehigh)/JetBin2_HTmedium_MHTextremehigh;
   double JetBin2_HThigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTlow, MHTmedium) - JetBin2_HThigh_MHTlow)/JetBin2_HThigh_MHTlow;
   double JetBin2_HThigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTmedium, MHThigh) - JetBin2_HThigh_MHTmedium)/JetBin2_HThigh_MHTmedium;
   double JetBin2_HThigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHThigh, MHTveryhigh) - JetBin2_HThigh_MHThigh)/JetBin2_HThigh_MHThigh;
   double JetBin2_HThigh_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTveryhigh, MHTextremehigh) - JetBin2_HThigh_MHTveryhigh)/JetBin2_HThigh_MHTveryhigh;
   double JetBin2_HThigh_MHTextremehigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HThigh"), MHTextremehigh, MHTextremehigh) - JetBin2_HThigh_MHTextremehigh)/JetBin2_HThigh_MHTextremehigh;
   double JetBin2_HTveryhigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTlow, MHTmedium) - JetBin2_HTveryhigh_MHTlow)/JetBin2_HTveryhigh_MHTlow;
   double JetBin2_HTveryhigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTmedium, MHThigh) - JetBin2_HTveryhigh_MHTmedium)/JetBin2_HTveryhigh_MHTmedium;
   double JetBin2_HTveryhigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin2_HTveryhigh_MHThigh)/JetBin2_HTveryhigh_MHThigh;
   double JetBin2_HTveryhigh_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin2_HTveryhigh_MHTveryhigh)/JetBin2_HTveryhigh_MHTveryhigh;
   double JetBin2_HTextremehigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTlow, MHTmedium) - JetBin2_HTextremehigh_MHTlow)/JetBin2_HTextremehigh_MHTlow;
   double JetBin2_HTextremehigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHTmedium, MHThigh) - JetBin2_HTextremehigh_MHTmedium)/JetBin2_HTextremehigh_MHTmedium;
   double JetBin2_HTextremehigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin2_HTextremehigh"), MHThigh, MHThigh) - JetBin2_HTextremehigh_MHThigh)/JetBin2_HTextremehigh_MHThigh;


   double JetBin3_HTlow_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTmedium, MHThigh) - JetBin3_HTlow_MHTmedium)/JetBin3_HTlow_MHTmedium; 
   double JetBin3_HTlow_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHThigh, MHTveryhigh) - JetBin3_HTlow_MHThigh)/JetBin3_HTlow_MHThigh;
   double JetBin3_HTlow_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTlow"), MHTveryhigh, MHTveryhigh) - JetBin3_HTlow_MHTveryhigh)/JetBin3_HTlow_MHTveryhigh;
   double JetBin3_HTmedium_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTlow, MHTmedium) - JetBin3_HTmedium_MHTlow)/JetBin3_HTmedium_MHTlow;
   double JetBin3_HTmedium_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTmedium, MHThigh) - JetBin3_HTmedium_MHTmedium)/JetBin3_HTmedium_MHTmedium;
   double JetBin3_HTmedium_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHThigh, MHTveryhigh) - JetBin3_HTmedium_MHThigh)/JetBin3_HTmedium_MHThigh;
   double JetBin3_HTmedium_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTmedium"), MHTveryhigh, MHTveryhigh) - JetBin3_HTmedium_MHTveryhigh)/JetBin3_HTmedium_MHTveryhigh;
   double JetBin3_HThigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTlow, MHTmedium) - JetBin3_HThigh_MHTlow)/JetBin3_HThigh_MHTlow;
   double JetBin3_HThigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTmedium, MHThigh) - JetBin3_HThigh_MHTmedium)/JetBin3_HThigh_MHTmedium;
   double JetBin3_HThigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHThigh, MHTveryhigh) - JetBin3_HThigh_MHThigh)/JetBin3_HThigh_MHThigh;
   double JetBin3_HThigh_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HThigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HThigh_MHTveryhigh)/JetBin3_HThigh_MHTveryhigh;
   double JetBin3_HTveryhigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTlow, MHTmedium) - JetBin3_HTveryhigh_MHTlow)/JetBin3_HTveryhigh_MHTlow;
   double JetBin3_HTveryhigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTmedium, MHThigh) - JetBin3_HTveryhigh_MHTmedium)/JetBin3_HTveryhigh_MHTmedium;
   double JetBin3_HTveryhigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHThigh, MHTveryhigh) - JetBin3_HTveryhigh_MHThigh)/JetBin3_HTveryhigh_MHThigh;
   double JetBin3_HTveryhigh_MHTveryhigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTveryhigh"), MHTveryhigh, MHTveryhigh) - JetBin3_HTveryhigh_MHTveryhigh)/JetBin3_HTveryhigh_MHTveryhigh;
   double JetBin3_HTextremehigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTlow, MHTmedium) - JetBin3_HTextremehigh_MHTlow)/JetBin3_HTextremehigh_MHTlow;
   double JetBin3_HTextremehigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHTmedium, MHThigh) - JetBin3_HTextremehigh_MHTmedium)/JetBin3_HTextremehigh_MHTmedium;
   double JetBin3_HTextremehigh_MHThigh_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin3_HTextremehigh"), MHThigh, MHThigh) - JetBin3_HTextremehigh_MHThigh)/JetBin3_HTextremehigh_MHThigh;
   
   
   double JetBin4_HTlow_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTlow"), MHTmedium, MHTmedium) - JetBin4_HTlow_MHTmedium)/JetBin4_HTlow_MHTmedium;                    
   double JetBin4_HTmedium_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTlow, MHTmedium) - JetBin4_HTmedium_MHTlow)/JetBin4_HTmedium_MHTlow;
   double JetBin4_HTmedium_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTmedium"), MHTmedium, MHTmedium) - JetBin4_HTmedium_MHTmedium)/JetBin4_HTmedium_MHTmedium;  
   double JetBin4_HThigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTlow, MHTmedium) - JetBin4_HThigh_MHTlow)/JetBin4_HThigh_MHTlow;
   double JetBin4_HThigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HThigh"), MHTmedium, MHTmedium) - JetBin4_HThigh_MHTmedium)/JetBin4_HThigh_MHTmedium; 
   double JetBin4_HTveryhigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTlow, MHTmedium) - JetBin4_HTveryhigh_MHTlow)/JetBin4_HTveryhigh_MHTlow;
   double JetBin4_HTveryhigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTveryhigh"), MHTmedium, MHTmedium) - JetBin4_HTveryhigh_MHTmedium)/JetBin4_HTveryhigh_MHTmedium;
   double JetBin4_HTextremehigh_MHTlow_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTlow, MHTmedium) - JetBin4_HTextremehigh_MHTlow)/JetBin4_HTextremehigh_MHTlow;
   double JetBin4_HTextremehigh_MHTmedium_TailDN = (pred_TailDN_->GetResultValue(pred_TailDN_->GetPredictionHisto("MHT_JetBin4_HTextremehigh"), MHTmedium, MHTmedium) - JetBin4_HTextremehigh_MHTmedium)/JetBin4_HTextremehigh_MHTmedium;
   // ------------------------------------------------------------------------------ //
    
   ////////////////////////////////////////////////////
   // set non-closure bias + PU uncertainty here
   // 52X
  //  double Bias_JetBin1_HTlow_MHTlow = 3.1;
//    double Bias_JetBin1_HTlow = 4.8;
//    double Bias_JetBin1_HThigh_MHTlow = 15.3;
//    double Bias_JetBin1_HThigh = 15.3;

//    double Bias_JetBin2_HTlow_MHTlow = 6.5;
//    double Bias_JetBin2_HTlow = 10.0;
//    double Bias_JetBin2_HThigh_MHTlow = 5.3;
//    double Bias_JetBin2_HThigh = 13.7;

//    double Bias_JetBin3_HTlow_MHTlow = 18.4;
//    double Bias_JetBin3_HTlow = 46.4;
//    double Bias_JetBin3_HThigh_MHTlow = 8.3;
//    double Bias_JetBin3_HThigh = 36.1;
//    double Bias_JetBin3_HThigh_lowerError = 36.1;

//    double Bias_JetBin4_HTlow_MHTlow = 85.1;
//    double Bias_JetBin4_HTlow = 113.;
//    double Bias_JetBin4_HTlow_lowerError = 100.;
//    double Bias_JetBin4_HThigh_MHTlow = 29.6;
//    double Bias_JetBin4_HThigh = 184.;
//    double Bias_JetBin4_HThigh_lowerError = 100.;

   // 53X
   double Bias_JetBin1_HTlow_MHTlow = 21.4;
   double Bias_JetBin1_HTlow = 66.9;
   double Bias_JetBin1_HThigh_MHTlow = 27.1;
   double Bias_JetBin1_HThigh = 77.7;

   double Bias_JetBin2_HTlow_MHTlow = 22.6;
   double Bias_JetBin2_HTlow = 60.4;
   double Bias_JetBin2_HThigh_MHTlow = 14.4;
   double Bias_JetBin2_HThigh = 14.4;

   double Bias_JetBin3_HTlow_MHTlow = 25.4;
   double Bias_JetBin3_HTlow = 25.4;
   double Bias_JetBin3_HThigh_MHTlow = 10.9;
   double Bias_JetBin3_HThigh = 10.9;
   double Bias_JetBin3_HThigh_lowerError = 10.9;

   double Bias_JetBin4_HTlow_MHTlow = 90.1;
   double Bias_JetBin4_HTlow = 90.1;
   double Bias_JetBin4_HTlow_lowerError = 90.1;
   double Bias_JetBin4_HThigh_MHTlow = 42.6;
   double Bias_JetBin4_HThigh = 42.6;
   double Bias_JetBin4_HThigh_lowerError = 42.6;

   // ------------------------------------------ //

   // 52X
  //  double PU_JetBin1 = 5.0;
//    double PU_JetBin2 = 3.2;
//    double PU_JetBin3 = 6.1;
//    double PU_JetBin4 = 17.5;

   // 53X
   double PU_JetBin1 = 3.9;
   double PU_JetBin2 = 2.9;
   double PU_JetBin3 = 8.0;
   double PU_JetBin4 = 33.4;
 
   ///////////////////////////////////////////////////
    
   ofstream prediction_outfile;
   prediction_outfile.open("output_GetPrediction_WithUncertainties/Prediction" + postfix + ".txt");
    
   // QCD predictions in search bins
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "CMS preliminary, L = 19.466 fb^{  -1}, #sqrt{s} = 8 TeV" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "NJets = 2 " << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
   // first jet multiplicity bin
   prediction_outfile << std::setprecision(4) << HTlow << " - " << HTmedium << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin1_HTlow_MHTmedium << " & " << JetBin1_HTlow_MHTmedium_error << " & " << JetBin1_HTlow_MHTmedium_CoreUP*100 << " & " << JetBin1_HTlow_MHTmedium_TailUP*100 << " & " << Bias_JetBin1_HTlow << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTlow_MHTmedium_CoreDN*100 << " & " <<  JetBin1_HTlow_MHTmedium_TailDN*100 << " & " << - Bias_JetBin1_HTlow << " & " << - PU_JetBin1 << "& \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin1_HTlow_MHThigh << " & " << JetBin1_HTlow_MHThigh_error << " & " << JetBin1_HTlow_MHThigh_CoreUP*100 << " & " << JetBin1_HTlow_MHThigh_TailUP*100 << " & " << Bias_JetBin1_HTlow << " & " << PU_JetBin1 << " &\\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTlow_MHThigh_CoreDN*100 << " & " <<  JetBin1_HTlow_MHThigh_TailDN*100 << " & " << - Bias_JetBin1_HTlow << " & " << - PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHTveryhigh << " - " << MHTextremehigh << " & " << JetBin1_HTlow_MHTveryhigh << " & " << JetBin1_HTlow_MHTveryhigh_error << " & " << JetBin1_HTlow_MHTveryhigh_CoreUP*100 << " & " << JetBin1_HTlow_MHTveryhigh_TailUP*100 << " & " << Bias_JetBin1_HTlow << " & " << PU_JetBin1 << "& \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTlow_MHTveryhigh_CoreDN*100 << " & " <<  JetBin1_HTlow_MHTveryhigh_TailDN*100 << " & " << - Bias_JetBin1_HTlow << " & " << - PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTextremehigh << " & " << JetBin1_HTlow_MHTextremehigh << " & " << JetBin1_HTlow_MHTextremehigh_error << " & " << JetBin1_HTlow_MHTextremehigh_CoreUP*100 << " & " << JetBin1_HTlow_MHTextremehigh_TailUP*100 << " & " << Bias_JetBin1_HTlow << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTlow_MHTextremehigh_CoreDN*100 << " & " <<  JetBin1_HTlow_MHTextremehigh_TailDN*100 << " & " << -Bias_JetBin1_HTlow << " & " << -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << HTmedium << " - " << HThigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin1_HTmedium_MHTlow << " & " << JetBin1_HTmedium_MHTlow_error << " & " << JetBin1_HTmedium_MHTlow_CoreUP*100 << " & " << JetBin1_HTmedium_MHTlow_TailUP*100 << " & " << Bias_JetBin1_HTlow_MHTlow << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTmedium_MHTlow_CoreDN*100 << " & " <<  JetBin1_HTmedium_MHTlow_TailDN*100 << " & "<< -Bias_JetBin1_HTlow_MHTlow << " & " << -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin1_HTmedium_MHTmedium << " & " << JetBin1_HTmedium_MHTmedium_error << " & " << JetBin1_HTmedium_MHTmedium_CoreUP*100 << " & " << JetBin1_HTmedium_MHTmedium_TailUP*100 << " & " << Bias_JetBin1_HTlow << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTmedium_MHTmedium_CoreDN*100 << " & " <<  JetBin1_HTmedium_MHTmedium_TailDN*100 << " & "<< - Bias_JetBin1_HTlow << " & "<< - PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin1_HTmedium_MHThigh << " & " << JetBin1_HTmedium_MHThigh_error << " & " << JetBin1_HTmedium_MHThigh_CoreUP*100 << " & " << JetBin1_HTmedium_MHThigh_TailUP*100 << " & " << Bias_JetBin1_HTlow << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTmedium_MHThigh_CoreDN*100 << " & " <<  JetBin1_HTmedium_MHThigh_TailDN*100 << " & "<< -Bias_JetBin1_HTlow << " & " << -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHTveryhigh << " - " << MHTextremehigh << " & " << JetBin1_HTmedium_MHTveryhigh << " & " << JetBin1_HTmedium_MHTveryhigh_error << " & " << JetBin1_HTmedium_MHTveryhigh_CoreUP*100 << " & " << JetBin1_HTmedium_MHTveryhigh_TailUP*100 << " & "<< Bias_JetBin1_HTlow << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTmedium_MHTveryhigh_CoreDN*100 << " & " <<  JetBin1_HTmedium_MHTveryhigh_TailDN*100 << " & "<< -Bias_JetBin1_HTlow << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTextremehigh << " & " << JetBin1_HTmedium_MHTextremehigh << " & " << JetBin1_HTmedium_MHTextremehigh_error << " & " << JetBin1_HTmedium_MHTextremehigh_CoreUP*100 << " & " << JetBin1_HTmedium_MHTextremehigh_TailUP*100 << " & "<< Bias_JetBin1_HTlow << " & " <<PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTmedium_MHTextremehigh_CoreDN*100 << " & " <<  JetBin1_HTmedium_MHTextremehigh_TailDN*100 << " & "<< -Bias_JetBin1_HTlow << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HThigh << " - " << HTveryhigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin1_HThigh_MHTlow << " & " << JetBin1_HThigh_MHTlow_error << " & " << JetBin1_HThigh_MHTlow_CoreUP*100 << " & " << JetBin1_HThigh_MHTlow_TailUP*100 << " & "<< Bias_JetBin1_HThigh_MHTlow << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HThigh_MHTlow_CoreDN*100 << " & " <<  JetBin1_HThigh_MHTlow_TailDN*100 << " & "<< -Bias_JetBin1_HThigh_MHTlow << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin1_HThigh_MHTmedium << " & " << JetBin1_HThigh_MHTmedium_error << " & " << JetBin1_HThigh_MHTmedium_CoreUP*100 << " & " << JetBin1_HThigh_MHTmedium_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HThigh_MHTmedium_CoreDN*100 << " & " <<  JetBin1_HThigh_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin1_HThigh_MHThigh << " & " << JetBin1_HThigh_MHThigh_error << " & " << JetBin1_HThigh_MHThigh_CoreUP*100 << " & " << JetBin1_HThigh_MHThigh_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HThigh_MHThigh_CoreDN*100 << " & " <<  JetBin1_HThigh_MHThigh_TailDN*100 << " & "<< -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHTveryhigh << " - " << MHTextremehigh << " & " << JetBin1_HThigh_MHTveryhigh << " & " << JetBin1_HThigh_MHTveryhigh_error << " & " << JetBin1_HThigh_MHTveryhigh_CoreUP*100 << " & " << JetBin1_HThigh_MHTveryhigh_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HThigh_MHTveryhigh_CoreDN*100 << " & " <<  JetBin1_HThigh_MHTveryhigh_TailDN*100 << " & "<< -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTextremehigh << " & " << JetBin1_HThigh_MHTextremehigh << " & " << JetBin1_HThigh_MHTextremehigh_error << " & " << JetBin1_HThigh_MHTextremehigh_CoreUP*100 << " & " << JetBin1_HThigh_MHTextremehigh_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HThigh_MHTextremehigh_CoreDN*100 << " & " <<  JetBin1_HThigh_MHTextremehigh_TailDN*100 << " & " << -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HTveryhigh << " - " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin1_HTveryhigh_MHTlow << " & " << JetBin1_HTveryhigh_MHTlow_error << " & " << JetBin1_HTveryhigh_MHTlow_CoreUP*100 << " & " << JetBin1_HTveryhigh_MHTlow_TailUP*100 << " & "<< Bias_JetBin1_HThigh_MHTlow << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTveryhigh_MHTlow_CoreDN*100 << " & " <<  JetBin1_HTveryhigh_MHTlow_TailDN*100 << " & "<< -Bias_JetBin1_HThigh_MHTlow << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin1_HTveryhigh_MHTmedium << " & " << JetBin1_HTveryhigh_MHTmedium_error << " & " << JetBin1_HTveryhigh_MHTmedium_CoreUP*100 << " & " << JetBin1_HTveryhigh_MHTmedium_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTveryhigh_MHTmedium_CoreDN*100 << " & " <<  JetBin1_HTveryhigh_MHTmedium_TailDN*100 << " & " << -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin1_HTveryhigh_MHThigh << " & " << JetBin1_HTveryhigh_MHThigh_error << " & " << JetBin1_HTveryhigh_MHThigh_CoreUP*100 << " & " << JetBin1_HTveryhigh_MHThigh_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTveryhigh_MHThigh_CoreDN*100 << " & " <<  JetBin1_HTveryhigh_MHThigh_TailDN*100 << " & "<< -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTveryhigh  << " & " << JetBin1_HTveryhigh_MHTveryhigh << " & " << JetBin1_HTveryhigh_MHTveryhigh_error << " & " << JetBin1_HTveryhigh_MHTveryhigh_CoreUP*100 << " & " << JetBin1_HTveryhigh_MHTveryhigh_TailUP*100 << " & "<< Bias_JetBin1_HThigh << " & "<< PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTveryhigh_MHTveryhigh_CoreDN*100 << " & " <<  JetBin1_HTveryhigh_MHTveryhigh_TailDN*100 << " & "<< -Bias_JetBin1_HThigh << " & "<< -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << " $>=$ " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin1_HTextremehigh_MHTlow << " & " << JetBin1_HTextremehigh_MHTlow_error << " & " << JetBin1_HTextremehigh_MHTlow_CoreUP*100 << " & " << JetBin1_HTextremehigh_MHTlow_TailUP*100 << " & " << Bias_JetBin1_HThigh_MHTlow << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTextremehigh_MHTlow_CoreDN*100 << " & " <<  JetBin1_HTextremehigh_MHTlow_TailDN*100 << " & " << - Bias_JetBin1_HThigh_MHTlow << " & " << -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin1_HTextremehigh_MHTmedium << " & " << JetBin1_HTextremehigh_MHTmedium_error << " & " << JetBin1_HTextremehigh_MHTmedium_CoreUP*100 << " & " << JetBin1_HTextremehigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin1_HThigh << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTextremehigh_MHTmedium_CoreDN*100 << " & " <<  JetBin1_HTextremehigh_MHTmedium_TailDN*100 << " & " << -Bias_JetBin1_HThigh << " &" << -PU_JetBin1 << "& \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " <<  MHThigh << " & " << JetBin1_HTextremehigh_MHThigh << " & " << JetBin1_HTextremehigh_MHThigh_error << " & " << JetBin1_HTextremehigh_MHThigh_CoreUP*100 << " & " << JetBin1_HTextremehigh_MHThigh_TailUP*100 << " & " << Bias_JetBin1_HThigh << " & " << PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin1_HTextremehigh_MHThigh_CoreDN*100 << " & " <<  JetBin1_HTextremehigh_MHThigh_TailDN*100 << " & " << -Bias_JetBin1_HThigh << " & " << -PU_JetBin1 << " & \\\\ " << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;

   // ------------------------------------------------------------------------------ //

   // second jet multiplicity bin
   prediction_outfile << "NJets = 3 - 5" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << std::setprecision(4) << HTlow << " - " << HTmedium << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin2_HTlow_MHTmedium << " & " << JetBin2_HTlow_MHTmedium_error << " & " << JetBin2_HTlow_MHTmedium_CoreUP*100 << " & " << JetBin2_HTlow_MHTmedium_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTlow_MHTmedium_CoreDN*100 << " & " <<  JetBin2_HTlow_MHTmedium_TailDN*100 << " & " << - Bias_JetBin2_HTlow <<  " & "<< - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin2_HTlow_MHThigh << " & " << JetBin2_HTlow_MHThigh_error << " & " << JetBin2_HTlow_MHThigh_CoreUP*100 << " & " << JetBin2_HTlow_MHThigh_TailUP*100 << " & " << Bias_JetBin2_HTlow <<  " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTlow_MHThigh_CoreDN*100 << " & " <<  JetBin2_HTlow_MHThigh_TailDN*100 << " & " << - Bias_JetBin2_HTlow<< " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHTveryhigh << " - " << MHTextremehigh << " & " << JetBin2_HTlow_MHTveryhigh << " & " << JetBin2_HTlow_MHTveryhigh_error << " & " << JetBin2_HTlow_MHTveryhigh_CoreUP*100 << " & " << JetBin2_HTlow_MHTveryhigh_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " <<  PU_JetBin2 <<" & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTlow_MHTveryhigh_CoreDN*100 << " & " <<  JetBin2_HTlow_MHTveryhigh_TailDN*100 << " & " << - Bias_JetBin2_HTlow<< " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTextremehigh << " & " << JetBin2_HTlow_MHTextremehigh << " & " << JetBin2_HTlow_MHTextremehigh_error << " & " << JetBin2_HTlow_MHTextremehigh_CoreUP*100 << " & " << JetBin2_HTlow_MHTextremehigh_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTlow_MHTextremehigh_CoreDN*100 << " & " <<  JetBin2_HTlow_MHTextremehigh_TailDN*100 << " & " << -Bias_JetBin2_HTlow << " & " << - PU_JetBin2 <<  " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << HTmedium << " - " << HThigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin2_HTmedium_MHTlow << " & " << JetBin2_HTmedium_MHTlow_error << " & " << JetBin2_HTmedium_MHTlow_CoreUP*100 << " & " << JetBin2_HTmedium_MHTlow_TailUP*100 << " & " << Bias_JetBin2_HTlow_MHTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTmedium_MHTlow_CoreDN*100 << " & " <<  JetBin2_HTmedium_MHTlow_TailDN*100 << " & " << -Bias_JetBin2_HTlow_MHTlow << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin2_HTmedium_MHTmedium << " & " << JetBin2_HTmedium_MHTmedium_error << " & " << JetBin2_HTmedium_MHTmedium_CoreUP*100 << " & " << JetBin2_HTmedium_MHTmedium_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTmedium_MHTmedium_CoreDN*100 << " & " <<  JetBin2_HTmedium_MHTmedium_TailDN*100 << " & " << - Bias_JetBin2_HTlow << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin2_HTmedium_MHThigh << " & " << JetBin2_HTmedium_MHThigh_error << " & " << JetBin2_HTmedium_MHThigh_CoreUP*100 << " & " << JetBin2_HTmedium_MHThigh_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTmedium_MHThigh_CoreDN*100 << " & " <<  JetBin2_HTmedium_MHThigh_TailDN*100 << " & " << - Bias_JetBin2_HTlow << " & " << - PU_JetBin2 <<" & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHTveryhigh << " - " << MHTextremehigh << " & " << JetBin2_HTmedium_MHTveryhigh << " & " << JetBin2_HTmedium_MHTveryhigh_error << " & " << JetBin2_HTmedium_MHTveryhigh_CoreUP*100 << " & " << JetBin2_HTmedium_MHTveryhigh_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTmedium_MHTveryhigh_CoreDN*100 << " & " <<  JetBin2_HTmedium_MHTveryhigh_TailDN*100 << " & " << - Bias_JetBin2_HTlow << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTextremehigh << " & " << JetBin2_HTmedium_MHTextremehigh << " & " << JetBin2_HTmedium_MHTextremehigh_error << " & " << JetBin2_HTmedium_MHTextremehigh_CoreUP*100 << " & " << JetBin2_HTmedium_MHTextremehigh_TailUP*100 << " & " << Bias_JetBin2_HTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTmedium_MHTextremehigh_CoreDN*100 << " & " <<  JetBin2_HTmedium_MHTextremehigh_TailDN*100 << " & " << - Bias_JetBin2_HTlow << " & " << - PU_JetBin2<< " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HThigh << " - " << HTveryhigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin2_HThigh_MHTlow << " & " << JetBin2_HThigh_MHTlow_error << " & " << JetBin2_HThigh_MHTlow_CoreUP*100 << " & " << JetBin2_HThigh_MHTlow_TailUP*100 << " & " << Bias_JetBin2_HThigh_MHTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HThigh_MHTlow_CoreDN*100 << " & " <<  JetBin2_HThigh_MHTlow_TailDN*100 << " & " << - Bias_JetBin2_HThigh_MHTlow << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin2_HThigh_MHTmedium << " & " << JetBin2_HThigh_MHTmedium_error << " & " << JetBin2_HThigh_MHTmedium_CoreUP*100 << " & " << JetBin2_HThigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HThigh_MHTmedium_CoreDN*100 << " & " <<  JetBin2_HThigh_MHTmedium_TailDN*100 << " & " << - Bias_JetBin2_HThigh << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin2_HThigh_MHThigh << " & " << JetBin2_HThigh_MHThigh_error << " & " << JetBin2_HThigh_MHThigh_CoreUP*100 << " & " << JetBin2_HThigh_MHThigh_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HThigh_MHThigh_CoreDN*100 << " & " <<  JetBin2_HThigh_MHThigh_TailDN*100 << " & " << - Bias_JetBin2_HThigh << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHTveryhigh << " - " << MHTextremehigh << " & " << JetBin2_HThigh_MHTveryhigh << " & " << JetBin2_HThigh_MHTveryhigh_error << " & " << JetBin2_HThigh_MHTveryhigh_CoreUP*100 << " & " << JetBin2_HThigh_MHTveryhigh_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HThigh_MHTveryhigh_CoreDN*100 << " & " <<  JetBin2_HThigh_MHTveryhigh_TailDN*100 << " & " << - Bias_JetBin2_HThigh << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTextremehigh << " & " << JetBin2_HThigh_MHTextremehigh << " & " << JetBin2_HThigh_MHTextremehigh_error << " & " << JetBin2_HThigh_MHTextremehigh_CoreUP*100 << " & " << JetBin2_HThigh_MHTextremehigh_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HThigh_MHTextremehigh_CoreDN*100 << " & " <<  JetBin2_HThigh_MHTextremehigh_TailDN*100 << " & " << -Bias_JetBin2_HThigh << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HTveryhigh << " - " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin2_HTveryhigh_MHTlow << " & " << JetBin2_HTveryhigh_MHTlow_error << " & " << JetBin2_HTveryhigh_MHTlow_CoreUP*100 << " & " << JetBin2_HTveryhigh_MHTlow_TailUP*100 << " & " << Bias_JetBin2_HThigh_MHTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTveryhigh_MHTlow_CoreDN*100 << " & " <<  JetBin2_HTveryhigh_MHTlow_TailDN*100 << " & " << - Bias_JetBin2_HThigh_MHTlow << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin2_HTveryhigh_MHTmedium << " & " << JetBin2_HTveryhigh_MHTmedium_error << " & " << JetBin2_HTveryhigh_MHTmedium_CoreUP*100 << " & " << JetBin2_HTveryhigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTveryhigh_MHTmedium_CoreDN*100 << " & " <<  JetBin2_HTveryhigh_MHTmedium_TailDN*100 << " & " << -Bias_JetBin2_HThigh << " & " << -PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin2_HTveryhigh_MHThigh << " & " << JetBin2_HTveryhigh_MHThigh_error << " & " << JetBin2_HTveryhigh_MHThigh_CoreUP*100 << " & " << JetBin2_HTveryhigh_MHThigh_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTveryhigh_MHThigh_CoreDN*100 << " & " <<  JetBin2_HTveryhigh_MHThigh_TailDN*100 << " & " << -Bias_JetBin2_HThigh << " & " << -PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTveryhigh  << " & " << JetBin2_HTveryhigh_MHTveryhigh << " & " << JetBin2_HTveryhigh_MHTveryhigh_error << " & " << JetBin2_HTveryhigh_MHTveryhigh_CoreUP*100 << " & " << JetBin2_HTveryhigh_MHTveryhigh_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTveryhigh_MHTveryhigh_CoreDN*100 << " & " <<  JetBin2_HTveryhigh_MHTveryhigh_TailDN*100 << " & " << - Bias_JetBin2_HThigh << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << " $>=$ " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin2_HTextremehigh_MHTlow << " & " << JetBin2_HTextremehigh_MHTlow_error << " & " << JetBin2_HTextremehigh_MHTlow_CoreUP*100 << " & " << JetBin2_HTextremehigh_MHTlow_TailUP*100 << " & " << Bias_JetBin2_HThigh_MHTlow << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTextremehigh_MHTlow_CoreDN*100 << " & " <<  JetBin2_HTextremehigh_MHTlow_TailDN*100 << " & " << - Bias_JetBin2_HThigh_MHTlow << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin2_HTextremehigh_MHTmedium << " & " << JetBin2_HTextremehigh_MHTmedium_error << " & " << JetBin2_HTextremehigh_MHTmedium_CoreUP*100 << " & " << JetBin2_HTextremehigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin2_HThigh << " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTextremehigh_MHTmedium_CoreDN*100 << " & " <<  JetBin2_HTextremehigh_MHTmedium_TailDN*100 << " & " << - Bias_JetBin2_HThigh << " & " << - PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " <<  MHThigh << " & " << JetBin2_HTextremehigh_MHThigh << " & " << JetBin2_HTextremehigh_MHThigh_error << " & " << JetBin2_HTextremehigh_MHThigh_CoreUP*100 << " & " << JetBin2_HTextremehigh_MHThigh_TailUP*100 << " & "<< Bias_JetBin2_HThigh <<  " & " << PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin2_HTextremehigh_MHThigh_CoreDN*100 << " & " <<  JetBin2_HTextremehigh_MHThigh_TailDN*100 << " & " << -Bias_JetBin2_HThigh << " & " << -PU_JetBin2 << " & \\\\ " << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;

   // ------------------------------------------------------------------------------ //
   // third jet multiplicity bin
   prediction_outfile << "NJets = 6 - 7" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << std::setprecision(4) << HTlow << " - " << HTmedium << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin3_HTlow_MHTmedium << " & " << JetBin3_HTlow_MHTmedium_error << " & " << JetBin3_HTlow_MHTmedium_CoreUP*100 << " & " << JetBin3_HTlow_MHTmedium_TailUP*100 << " & " << Bias_JetBin3_HTlow << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTlow_MHTmedium_CoreDN*100 << " & " <<  JetBin3_HTlow_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin3_HTlow<< " & "<< - PU_JetBin3 <<" & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin3_HTlow_MHThigh << " & " << JetBin3_HTlow_MHThigh_error << " & " << JetBin3_HTlow_MHThigh_CoreUP*100 << " & " << JetBin3_HTlow_MHThigh_TailUP*100 << " & "<< Bias_JetBin3_HTlow << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTlow_MHThigh_CoreDN*100 << " & " <<  JetBin3_HTlow_MHThigh_TailDN*100 << " & "<< -Bias_JetBin3_HTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " <<  MHTveryhigh << " & " << JetBin3_HTlow_MHTveryhigh << " & " << JetBin3_HTlow_MHTveryhigh_error << " & " << JetBin3_HTlow_MHTveryhigh_CoreUP*100 << " & " << JetBin3_HTlow_MHTveryhigh_TailUP*100 << " & "<< Bias_JetBin3_HTlow << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTlow_MHTveryhigh_CoreDN*100 << " & " <<  JetBin3_HTlow_MHTveryhigh_TailDN*100 << " & " << -Bias_JetBin3_HTlow << " & " << - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << HTmedium << " - " << HThigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin3_HTmedium_MHTlow << " & " << JetBin3_HTmedium_MHTlow_error << " & " << JetBin3_HTmedium_MHTlow_CoreUP*100 << " & " << JetBin3_HTmedium_MHTlow_TailUP*100 << " & "<< Bias_JetBin3_HTlow_MHTlow << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTmedium_MHTlow_CoreDN*100 << " & " <<  JetBin3_HTmedium_MHTlow_TailDN*100 << " & "<< -Bias_JetBin3_HTlow_MHTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin3_HTmedium_MHTmedium << " & " << JetBin3_HTmedium_MHTmedium_error << " & " << JetBin3_HTmedium_MHTmedium_CoreUP*100 << " & " << JetBin3_HTmedium_MHTmedium_TailUP*100 << " & " << Bias_JetBin3_HTlow << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTmedium_MHTmedium_CoreDN*100 << " & " <<  JetBin3_HTmedium_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin3_HTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin3_HTmedium_MHThigh << " & " << JetBin3_HTmedium_MHThigh_error << " & " << JetBin3_HTmedium_MHThigh_CoreUP*100 << " & " << JetBin3_HTmedium_MHThigh_TailUP*100 << " & " << Bias_JetBin3_HTlow << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTmedium_MHThigh_CoreDN*100 << " & " <<  JetBin3_HTmedium_MHThigh_TailDN*100 << " & "<< -Bias_JetBin3_HTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " <<  MHTveryhigh << " & " << JetBin3_HTmedium_MHTveryhigh << " & " << JetBin3_HTmedium_MHTveryhigh_error << " & " << JetBin3_HTmedium_MHTveryhigh_CoreUP*100 << " & " << JetBin3_HTmedium_MHTveryhigh_TailUP*100 << " & " << Bias_JetBin3_HTlow << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTmedium_MHTveryhigh_CoreDN*100 << " & " <<  JetBin3_HTmedium_MHTveryhigh_TailDN*100 << " & "<< -Bias_JetBin3_HTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HThigh << " - " << HTveryhigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin3_HThigh_MHTlow << " & " << JetBin3_HThigh_MHTlow_error << " & " << JetBin3_HThigh_MHTlow_CoreUP*100 << " & " << JetBin3_HThigh_MHTlow_TailUP*100 << " & " << Bias_JetBin3_HThigh_MHTlow << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HThigh_MHTlow_CoreDN*100 << " & " <<  JetBin3_HThigh_MHTlow_TailDN*100 << " & " << -Bias_JetBin3_HThigh_MHTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin3_HThigh_MHTmedium << " & " << JetBin3_HThigh_MHTmedium_error << " & " << JetBin3_HThigh_MHTmedium_CoreUP*100 << " & " << JetBin3_HThigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin3_HThigh << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HThigh_MHTmedium_CoreDN*100 << " & " <<  JetBin3_HThigh_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_lowerError << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin3_HThigh_MHThigh << " & " << JetBin3_HThigh_MHThigh_error << " & " << JetBin3_HThigh_MHThigh_CoreUP*100 << " & " << JetBin3_HThigh_MHThigh_TailUP*100 << " & "<< Bias_JetBin3_HThigh << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HThigh_MHThigh_CoreDN*100 << " & " <<  JetBin3_HThigh_MHThigh_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_lowerError << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  " $>=$ " << MHTveryhigh << " & " << JetBin3_HThigh_MHTveryhigh << " & " << JetBin3_HThigh_MHTveryhigh_error << " & " << JetBin3_HThigh_MHTveryhigh_CoreUP*100 << " & " << JetBin3_HThigh_MHTveryhigh_TailUP*100 << " & "<< Bias_JetBin3_HThigh << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HThigh_MHTveryhigh_CoreDN*100 << " & " <<  JetBin3_HThigh_MHTveryhigh_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_lowerError << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HTveryhigh << " - " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin3_HTveryhigh_MHTlow << " & " << JetBin3_HTveryhigh_MHTlow_error << " & " << JetBin3_HTveryhigh_MHTlow_CoreUP*100 << " & " << JetBin3_HTveryhigh_MHTlow_TailUP*100 << " & "<< Bias_JetBin3_HThigh_MHTlow << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTveryhigh_MHTlow_CoreDN*100 << " & " <<  JetBin3_HTveryhigh_MHTlow_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_MHTlow << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin3_HTveryhigh_MHTmedium << " & " << JetBin3_HTveryhigh_MHTmedium_error << " & " << JetBin3_HTveryhigh_MHTmedium_CoreUP*100 << " & " << JetBin3_HTveryhigh_MHTmedium_TailUP*100 << " & "<< Bias_JetBin3_HThigh << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTveryhigh_MHTmedium_CoreDN*100 << " & " <<  JetBin3_HTveryhigh_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_lowerError << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " <<  MHThigh << " - " << MHTveryhigh << " & " << JetBin3_HTveryhigh_MHThigh << " & " << JetBin3_HTveryhigh_MHThigh_error << " & " << JetBin3_HTveryhigh_MHThigh_CoreUP*100 << " & " << JetBin3_HTveryhigh_MHThigh_TailUP*100 << " & "<< Bias_JetBin3_HThigh << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTveryhigh_MHThigh_CoreDN*100 << " & " <<  JetBin3_HTveryhigh_MHThigh_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_lowerError <<  " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTveryhigh  << " & " << JetBin3_HTveryhigh_MHTveryhigh << " & " << JetBin3_HTveryhigh_MHTveryhigh_error << " & " << JetBin3_HTveryhigh_MHTveryhigh_CoreUP*100 << " & " << JetBin3_HTveryhigh_MHTveryhigh_TailUP*100 << " & "<< Bias_JetBin3_HThigh << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTveryhigh_MHTveryhigh_CoreDN*100 << " & " <<  JetBin3_HTveryhigh_MHTveryhigh_TailDN*100 << " & " << -Bias_JetBin3_HThigh_lowerError << " & " << - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << " $>=$ " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin3_HTextremehigh_MHTlow << " & " << JetBin3_HTextremehigh_MHTlow_error << " & " << JetBin3_HTextremehigh_MHTlow_CoreUP*100 << " & " << JetBin3_HTextremehigh_MHTlow_TailUP*100 << " & "<< Bias_JetBin3_HThigh_MHTlow << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTextremehigh_MHTlow_CoreDN*100 << " & " <<  JetBin3_HTextremehigh_MHTlow_TailDN*100 << " & " << -Bias_JetBin3_HThigh_MHTlow << " & " << - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << MHTmedium << " - " << MHThigh << " & " << JetBin3_HTextremehigh_MHTmedium << " & " << JetBin3_HTextremehigh_MHTmedium_error << " & " << JetBin3_HTextremehigh_MHTmedium_CoreUP*100 << " & " << JetBin3_HTextremehigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin3_HThigh << " & " << PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTextremehigh_MHTmedium_CoreDN*100 << " & " <<  JetBin3_HTextremehigh_MHTmedium_TailDN*100 << " & " << -Bias_JetBin3_HThigh_lowerError << " & " << - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " <<  MHThigh << " & " << JetBin3_HTextremehigh_MHThigh << " & " << JetBin3_HTextremehigh_MHThigh_error << " & " << JetBin3_HTextremehigh_MHThigh_CoreUP*100 << " & " << JetBin3_HTextremehigh_MHThigh_TailUP*100 << " & "<< Bias_JetBin3_HThigh << " & "<< PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin3_HTextremehigh_MHThigh_CoreDN*100 << " & " <<  JetBin3_HTextremehigh_MHThigh_TailDN*100 << " & "<< -Bias_JetBin3_HThigh_lowerError << " & "<< - PU_JetBin3 << " & \\\\ " << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;

   // ------------------------------------------------------------------------------ //
   // fourth jet multiplicity bin
   prediction_outfile << "NJets >= 8" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << std::setprecision(4) << HTlow << " - " << HTmedium << " & " << " $>=$ " << MHTmedium << " & " << JetBin4_HTlow_MHTmedium << " & " << JetBin4_HTlow_MHTmedium_error << " & " << JetBin4_HTlow_MHTmedium_CoreUP*100 << " & " << JetBin4_HTlow_MHTmedium_TailUP*100 << " & "<< Bias_JetBin4_HTlow << " & "<< PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTlow_MHTmedium_CoreDN*100 << " & " <<  JetBin4_HTlow_MHTmedium_TailDN*100 << " & "<< - Bias_JetBin4_HTlow_lowerError << " & "<< - PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << HTmedium << " - " << HThigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin4_HTmedium_MHTlow << " & " << JetBin4_HTmedium_MHTlow_error << " & " << JetBin4_HTmedium_MHTlow_CoreUP*100 << " & " << JetBin4_HTmedium_MHTlow_TailUP*100 << " & "<< Bias_JetBin4_HTlow_MHTlow << " & "<< PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTmedium_MHTlow_CoreDN*100 << " & " <<  JetBin4_HTmedium_MHTlow_TailDN*100 << " & "<< -Bias_JetBin4_HTlow_MHTlow << " & "<< -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTmedium << " & " << JetBin4_HTmedium_MHTmedium << " & " << JetBin4_HTmedium_MHTmedium_error << " & " << JetBin4_HTmedium_MHTmedium_CoreUP*100 << " & " << JetBin4_HTmedium_MHTmedium_TailUP*100 << " & " << Bias_JetBin4_HTlow << " & " << PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTmedium_MHTmedium_CoreDN*100 << " & " <<  JetBin4_HTmedium_MHTmedium_TailDN*100 << " & " << -Bias_JetBin4_HTlow_lowerError << " & " << -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HThigh << " - " << HTveryhigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin4_HThigh_MHTlow << " & " << JetBin4_HThigh_MHTlow_error << " & " << JetBin4_HThigh_MHTlow_CoreUP*100 << " & " << JetBin4_HThigh_MHTlow_TailUP*100 << " & " << Bias_JetBin4_HThigh_MHTlow << " & " << PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HThigh_MHTlow_CoreDN*100 << " & " <<  JetBin4_HThigh_MHTlow_TailDN*100 << " & "<< -Bias_JetBin4_HThigh_MHTlow << " & "<< -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTmedium << " & " << JetBin4_HThigh_MHTmedium << " & " << JetBin4_HThigh_MHTmedium_error << " & " << JetBin4_HThigh_MHTmedium_CoreUP*100 << " & " << JetBin4_HThigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin4_HThigh << " & " << PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HThigh_MHTmedium_CoreDN*100 << " & " <<  JetBin4_HThigh_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin4_HThigh_lowerError << " & "<< -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;
  
   prediction_outfile << std::setprecision(4) << HTveryhigh << " - " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin4_HTveryhigh_MHTlow << " & " << JetBin4_HTveryhigh_MHTlow_error << " & " << JetBin4_HTveryhigh_MHTlow_CoreUP*100 << " & " << JetBin4_HTveryhigh_MHTlow_TailUP*100 << " & " << Bias_JetBin4_HThigh_MHTlow << " & " << PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTveryhigh_MHTlow_CoreDN*100 << " & " <<  JetBin4_HTveryhigh_MHTlow_TailDN*100 << " & " << -Bias_JetBin4_HThigh_MHTlow << " & " << -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTmedium << " & " << JetBin4_HTveryhigh_MHTmedium << " & " << JetBin4_HTveryhigh_MHTmedium_error << " & " << JetBin4_HTveryhigh_MHTmedium_CoreUP*100 << " & " << JetBin4_HTveryhigh_MHTmedium_TailUP*100 << " & " << Bias_JetBin4_HThigh << " & "<< PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTveryhigh_MHTmedium_CoreDN*100 << " & " <<  JetBin4_HTveryhigh_MHTmedium_TailDN*100 << " & " << -Bias_JetBin4_HThigh_lowerError << " & " << -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << "\\midrule" << endl;

   prediction_outfile << std::setprecision(4) << " $>=$ " << HTextremehigh << " & " << MHTlow << " - " << MHTmedium << " & " << JetBin4_HTextremehigh_MHTlow << " & " << JetBin4_HTextremehigh_MHTlow_error << " & " << JetBin4_HTextremehigh_MHTlow_CoreUP*100 << " & " << JetBin4_HTextremehigh_MHTlow_TailUP*100 << " & "<< Bias_JetBin4_HThigh_MHTlow << " & "<< PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTextremehigh_MHTlow_CoreDN*100 << " & " <<  JetBin4_HTextremehigh_MHTlow_TailDN*100 << " & "<< -Bias_JetBin4_HThigh_MHTlow << " & "<< -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & " << " $>=$ " << MHTmedium << " & " << JetBin4_HTextremehigh_MHTmedium << " & " << JetBin4_HTextremehigh_MHTmedium_error << " & " << JetBin4_HTextremehigh_MHTmedium_CoreUP*100 << " & " << JetBin4_HTextremehigh_MHTmedium_TailUP*100 << " & "<< Bias_JetBin4_HThigh << " & "<< PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << std::setprecision(4) << " & & & & " << JetBin4_HTextremehigh_MHTmedium_CoreDN*100 << " & " <<  JetBin4_HTextremehigh_MHTmedium_TailDN*100 << " & "<< -Bias_JetBin4_HThigh_lowerError << " & " << -PU_JetBin4 << " & \\\\ " << endl;
   prediction_outfile << "----------------------" << endl;
   prediction_outfile << "----------------------" << endl;
    
   prediction_outfile.close();

   return 1;
}




