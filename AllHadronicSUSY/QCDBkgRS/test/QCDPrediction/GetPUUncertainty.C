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

using namespace std;

void GetPUUncertainty()
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
   gStyle->SetMarkerSize(0.75);
   gStyle->SetMarkerStyle(20);
   gStyle->SetMarkerColor(1);
  
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
   gStyle->SetTitleOffset(1.25, "Y");
   gStyle->SetTitleOffset(0.5, "Z");
   gStyle->SetTitleSize(0.05, "XYZ");
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

   string root_file;
   TChain* prediction_mc = new TChain("QCDfromSmearing/QCDPrediction");
   TChain* prediction_data = new TChain("QCDfromSmearing/QCDPrediction");

   int Ntries = 100;
   int NbinsHT_ = 100;
   double HTmin_ = 0.;
   double HTmax_ = 5000.;
	double MHTmin_ = 0.;
   double MHTmax_ = 1500.;
   
   // define PU bins
   double pubins_[4] = {0, 10, 20, 30};

   // histos for seed events data + mc
   TH2F* h_SeedEvents_HT_JetBin1_mc = new TH2F("SeedEvents_HT_JetBin1_mc", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin1_mc->Sumw2();
   TH2F* h_SeedEvents_HT_JetBin2_mc = new TH2F("SeedEvents_HT_JetBin2_mc", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin2_mc->Sumw2();
   TH2F* h_SeedEvents_HT_JetBin3_mc = new TH2F("SeedEvents_HT_JetBin3_mc", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin3_mc->Sumw2();
   TH2F* h_SeedEvents_HT_JetBin4_mc = new TH2F("SeedEvents_HT_JetBin4_mc", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin4_mc->Sumw2();
 
   TH2F* h_SeedEvents_HT_JetBin1_data = new TH2F("SeedEvents_HT_JetBin1_data", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin1_data->Sumw2();
   TH2F* h_SeedEvents_HT_JetBin2_data = new TH2F("SeedEvents_HT_JetBin2_data", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin2_data->Sumw2();
   TH2F* h_SeedEvents_HT_JetBin3_data = new TH2F("SeedEvents_HT_JetBin3_data", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin3_data->Sumw2();
   TH2F* h_SeedEvents_HT_JetBin4_data = new TH2F("SeedEvents_HT_JetBin4_data", "Seed Events", NbinsHT_, HTmin_, HTmax_, 60, 0, 60 );
   h_SeedEvents_HT_JetBin4_data->Sumw2();

   // open files for MC --- madgraph QCD ---- //
   ifstream myfile1_mc ("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT100-250_UseRebCorrection_v1_mc.txt");
   if (myfile1_mc.is_open()) {
      while( myfile1_mc.good() ) {
         getline (myfile1_mc,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_mc->Add(path);
       
         TH2F* h_SeedEvents_HT_NJet2_mc_temp;
         TH2F* h_SeedEvents_HT_NJet3_mc_temp;
         TH2F* h_SeedEvents_HT_NJet4_mc_temp;
         TH2F* h_SeedEvents_HT_NJet5_mc_temp; 
         TH2F* h_SeedEvents_HT_NJet6_mc_temp;
         TH2F* h_SeedEvents_HT_NJet7_mc_temp;
         TH2F* h_SeedEvents_HT_NJet8_mc_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_mc_temp);
         h_SeedEvents_HT_JetBin1_mc->Add(h_SeedEvents_HT_NJet2_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet3_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet4_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet5_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet6_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet7_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_mc_temp);
         h_SeedEvents_HT_JetBin4_mc->Add(h_SeedEvents_HT_NJet8_mc_temp);

         input_file->Close();
      }
      myfile1_mc.close();
   }

   ifstream myfile2_mc ("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT250-500_UseRebCorrection_v1_mc.txt");
   if (myfile2_mc.is_open()) {
      while( myfile2_mc.good() ) {
         getline (myfile2_mc,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_mc->Add(path);
       
         TH2F* h_SeedEvents_HT_NJet2_mc_temp;
         TH2F* h_SeedEvents_HT_NJet3_mc_temp;
         TH2F* h_SeedEvents_HT_NJet4_mc_temp;
         TH2F* h_SeedEvents_HT_NJet5_mc_temp; 
         TH2F* h_SeedEvents_HT_NJet6_mc_temp;
         TH2F* h_SeedEvents_HT_NJet7_mc_temp;
         TH2F* h_SeedEvents_HT_NJet8_mc_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_mc_temp);
         h_SeedEvents_HT_JetBin1_mc->Add(h_SeedEvents_HT_NJet2_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet3_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet4_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet5_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet6_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet7_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_mc_temp);
         h_SeedEvents_HT_JetBin4_mc->Add(h_SeedEvents_HT_NJet8_mc_temp);

         input_file->Close();
      }
      myfile2_mc.close();
   }

   ifstream myfile3_mc ("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT500-1000_UseRebCorrection_v1_mc.txt");
   if (myfile3_mc.is_open()) {
      while( myfile3_mc.good() ) {
         getline (myfile3_mc,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_mc->Add(path);
       
         TH2F* h_SeedEvents_HT_NJet2_mc_temp;
         TH2F* h_SeedEvents_HT_NJet3_mc_temp;
         TH2F* h_SeedEvents_HT_NJet4_mc_temp;
         TH2F* h_SeedEvents_HT_NJet5_mc_temp; 
         TH2F* h_SeedEvents_HT_NJet6_mc_temp;
         TH2F* h_SeedEvents_HT_NJet7_mc_temp;
         TH2F* h_SeedEvents_HT_NJet8_mc_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_mc_temp);
         h_SeedEvents_HT_JetBin1_mc->Add(h_SeedEvents_HT_NJet2_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet3_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet4_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet5_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet6_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet7_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_mc_temp);
         h_SeedEvents_HT_JetBin4_mc->Add(h_SeedEvents_HT_NJet8_mc_temp);

         input_file->Close();
      }
      myfile3_mc.close();
   }

   ifstream myfile4_mc ("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT1000-Inf_UseRebCorrection_v1_mc.txt");
   if (myfile4_mc.is_open()) {
      while( myfile4_mc.good() ) {
         getline (myfile4_mc,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_mc->Add(path);
       
         TH2F* h_SeedEvents_HT_NJet2_mc_temp;
         TH2F* h_SeedEvents_HT_NJet3_mc_temp;
         TH2F* h_SeedEvents_HT_NJet4_mc_temp;
         TH2F* h_SeedEvents_HT_NJet5_mc_temp; 
         TH2F* h_SeedEvents_HT_NJet6_mc_temp;
         TH2F* h_SeedEvents_HT_NJet7_mc_temp;
         TH2F* h_SeedEvents_HT_NJet8_mc_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_mc_temp);
         h_SeedEvents_HT_JetBin1_mc->Add(h_SeedEvents_HT_NJet2_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet3_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet4_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_mc_temp);
         h_SeedEvents_HT_JetBin2_mc->Add(h_SeedEvents_HT_NJet5_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet6_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_mc_temp);
         h_SeedEvents_HT_JetBin3_mc->Add(h_SeedEvents_HT_NJet7_mc_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_mc_temp);
         h_SeedEvents_HT_JetBin4_mc->Add(h_SeedEvents_HT_NJet8_mc_temp);

         input_file->Close();
      }
      myfile4_mc.close();
   }
  
   // files for data prediction
   ifstream myfile1_data ("filelist_prediction_535_Run2012A-13Jul2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile1_data.is_open()) {
      while( myfile1_data.good() ) {
         getline (myfile1_data,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_data->Add(path);

         TH2F* h_SeedEvents_HT_NJet2_data_temp;
         TH2F* h_SeedEvents_HT_NJet3_data_temp;
         TH2F* h_SeedEvents_HT_NJet4_data_temp;
         TH2F* h_SeedEvents_HT_NJet5_data_temp; 
         TH2F* h_SeedEvents_HT_NJet6_data_temp;
         TH2F* h_SeedEvents_HT_NJet7_data_temp;
         TH2F* h_SeedEvents_HT_NJet8_data_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_data_temp);
         h_SeedEvents_HT_JetBin1_data->Add(h_SeedEvents_HT_NJet2_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet3_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet4_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet5_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet6_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet7_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_data_temp);
         h_SeedEvents_HT_JetBin4_data->Add(h_SeedEvents_HT_NJet8_data_temp);

         input_file->Close();

      }
      myfile1_data.close();
   }

   ifstream myfile2_data ("filelist_prediction_535_Run2012A-recover-06Aug2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile2_data.is_open()) {
      while( myfile2_data.good() ) {
         getline (myfile2_data,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_data->Add(path);

         TH2F* h_SeedEvents_HT_NJet2_data_temp;
         TH2F* h_SeedEvents_HT_NJet3_data_temp;
         TH2F* h_SeedEvents_HT_NJet4_data_temp;
         TH2F* h_SeedEvents_HT_NJet5_data_temp; 
         TH2F* h_SeedEvents_HT_NJet6_data_temp;
         TH2F* h_SeedEvents_HT_NJet7_data_temp;
         TH2F* h_SeedEvents_HT_NJet8_data_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_data_temp);
         h_SeedEvents_HT_JetBin1_data->Add(h_SeedEvents_HT_NJet2_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet3_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet4_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet5_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet6_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet7_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_data_temp);
         h_SeedEvents_HT_JetBin4_data->Add(h_SeedEvents_HT_NJet8_data_temp);

         input_file->Close();
      }
      myfile2_data.close();
   }

   ifstream myfile3_data ("filelist_prediction_535_Run2012B-13Jul2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile3_data.is_open()) {
      while( myfile3_data.good() ) {
         getline (myfile3_data,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_data->Add(path);
         
         TH2F* h_SeedEvents_HT_NJet2_data_temp;
         TH2F* h_SeedEvents_HT_NJet3_data_temp;
         TH2F* h_SeedEvents_HT_NJet4_data_temp;
         TH2F* h_SeedEvents_HT_NJet5_data_temp; 
         TH2F* h_SeedEvents_HT_NJet6_data_temp;
         TH2F* h_SeedEvents_HT_NJet7_data_temp;
         TH2F* h_SeedEvents_HT_NJet8_data_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_data_temp);
         h_SeedEvents_HT_JetBin1_data->Add(h_SeedEvents_HT_NJet2_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet3_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet4_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet5_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet6_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet7_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_data_temp);
         h_SeedEvents_HT_JetBin4_data->Add(h_SeedEvents_HT_NJet8_data_temp);

         input_file->Close();
      }
      myfile3_data.close();
   }

   ifstream myfile4_data ("filelist_prediction_535_Run2012C-24Aug2012-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile4_data.is_open()) {
      while( myfile4_data.good() ) {
         getline (myfile4_data,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_data->Add(path);
         
         TH2F* h_SeedEvents_HT_NJet2_data_temp;
         TH2F* h_SeedEvents_HT_NJet3_data_temp;
         TH2F* h_SeedEvents_HT_NJet4_data_temp;
         TH2F* h_SeedEvents_HT_NJet5_data_temp; 
         TH2F* h_SeedEvents_HT_NJet6_data_temp;
         TH2F* h_SeedEvents_HT_NJet7_data_temp;
         TH2F* h_SeedEvents_HT_NJet8_data_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_data_temp);
         h_SeedEvents_HT_JetBin1_data->Add(h_SeedEvents_HT_NJet2_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet3_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet4_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet5_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet6_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet7_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_data_temp);
         h_SeedEvents_HT_JetBin4_data->Add(h_SeedEvents_HT_NJet8_data_temp);

         input_file->Close();
      }
      myfile4_data.close();
   }

   ifstream myfile5_data ("filelist_prediction_535_Run2012C-PromptReco-v2_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile5_data.is_open()) {
      while( myfile5_data.good() ) {
         getline (myfile5_data,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_data->Add(path);
         
         TH2F* h_SeedEvents_HT_NJet2_data_temp;
         TH2F* h_SeedEvents_HT_NJet3_data_temp;
         TH2F* h_SeedEvents_HT_NJet4_data_temp;
         TH2F* h_SeedEvents_HT_NJet5_data_temp; 
         TH2F* h_SeedEvents_HT_NJet6_data_temp;
         TH2F* h_SeedEvents_HT_NJet7_data_temp;
         TH2F* h_SeedEvents_HT_NJet8_data_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_data_temp);
         h_SeedEvents_HT_JetBin1_data->Add(h_SeedEvents_HT_NJet2_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet3_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet4_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet5_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet6_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet7_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_data_temp);
         h_SeedEvents_HT_JetBin4_data->Add(h_SeedEvents_HT_NJet8_data_temp);

         input_file->Close();
      }
      myfile5_data.close();
   }

   ifstream myfile6_data ("filelist_prediction_535_Run2012D-PromptReco-v1_pt10_withUncertainties_UseRebCorrection_data_v3.txt");
   if (myfile6_data.is_open()) {
      while( myfile6_data.good() ) {
         getline (myfile6_data,root_file);
         cout << root_file << endl;

         TString path = root_file;
         prediction_data->Add(path);
         
         TH2F* h_SeedEvents_HT_NJet2_data_temp;
         TH2F* h_SeedEvents_HT_NJet3_data_temp;
         TH2F* h_SeedEvents_HT_NJet4_data_temp;
         TH2F* h_SeedEvents_HT_NJet5_data_temp; 
         TH2F* h_SeedEvents_HT_NJet6_data_temp;
         TH2F* h_SeedEvents_HT_NJet7_data_temp;
         TH2F* h_SeedEvents_HT_NJet8_data_temp;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("SeedEvents_HT_NJet2;1", h_SeedEvents_HT_NJet2_data_temp);
         h_SeedEvents_HT_JetBin1_data->Add(h_SeedEvents_HT_NJet2_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet3;1", h_SeedEvents_HT_NJet3_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet3_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet4;1", h_SeedEvents_HT_NJet4_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet4_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet5;1", h_SeedEvents_HT_NJet5_data_temp);
         h_SeedEvents_HT_JetBin2_data->Add(h_SeedEvents_HT_NJet5_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet6;1", h_SeedEvents_HT_NJet6_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet6_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet7;1", h_SeedEvents_HT_NJet7_data_temp);
         h_SeedEvents_HT_JetBin3_data->Add(h_SeedEvents_HT_NJet7_data_temp);

         gDirectory->GetObject("SeedEvents_HT_NJet8;1", h_SeedEvents_HT_NJet8_data_temp);
         h_SeedEvents_HT_JetBin4_data->Add(h_SeedEvents_HT_NJet8_data_temp);

         input_file->Close();
      }
      myfile6_data.close();
   }

   // -------------------------------- //
   // plot vertex distribution in data + mc
   TH2F* h_NVtx_raw_data = new TH2F("NVtx_raw_data", "", NbinsHT_, HTmin_, HTmax_, 60, 0, 60);
   h_NVtx_raw_data->Add(h_SeedEvents_HT_JetBin1_data);
   h_NVtx_raw_data->Add(h_SeedEvents_HT_JetBin2_data);
   h_NVtx_raw_data->Add(h_SeedEvents_HT_JetBin3_data);
   h_NVtx_raw_data->Add(h_SeedEvents_HT_JetBin4_data);

   TH2F* h_NVtx_raw_mc = new TH2F("NVtx_raw_mc", "", NbinsHT_, HTmin_, HTmax_, 60, 0, 60);
   h_NVtx_raw_mc->Add(h_SeedEvents_HT_JetBin1_mc);
   h_NVtx_raw_mc->Add(h_SeedEvents_HT_JetBin2_mc);
   h_NVtx_raw_mc->Add(h_SeedEvents_HT_JetBin3_mc);
   h_NVtx_raw_mc->Add(h_SeedEvents_HT_JetBin4_mc);

   TH1F* h_NVtx_data = new TH1F();
   h_NVtx_data = (TH1F*) h_NVtx_raw_data->ProjectionY();
   double entries_data = h_NVtx_data->Integral();

   TH1F* h_NVtx_mc = new TH1F();
   h_NVtx_mc = (TH1F*) h_NVtx_raw_mc->ProjectionY();
   double entries_mc = h_NVtx_mc->Integral();

   h_NVtx_mc->Scale(entries_data/entries_mc); 
  
   TCanvas *c = new TCanvas("c", "", 700, 700);
   h_NVtx_data->Draw();
   h_NVtx_mc->SetMarkerColor(kRed);
   h_NVtx_mc->Draw("same");
   c->Print("NVtx_data_mc.ps");
   c->Print("NVtx_data_mc.png");
   // -------------------------------- //

   // define PU histos
   // data prediction
   TH1F* pile_up_histo_pred_data_Njet2 = new TH1F("pile_up_histo_pred_data_Njet2", "", 3, pubins_);
   TH1F* pile_up_histo_pred_data_Njet3_5 = new TH1F("pile_up_histo_pred_data_Njet3_5", "", 3, pubins_);
   TH1F* pile_up_histo_pred_data_Njet6_7 = new TH1F("pile_up_histo_pred_data_Njet6_7", "", 3, pubins_);
   TH1F* pile_up_histo_pred_data_Njet8 = new TH1F("pile_up_histo_pred_data_Njet8", "", 3, pubins_);

   // mc prediction
   TH1F* pile_up_histo_pred_mc_Njet2 = new TH1F("pile_up_histo_pred_mc_Njet2", "", 3, pubins_);
   TH1F* pile_up_histo_pred_mc_Njet3_5 = new TH1F("pile_up_histo_pred_mc_Njet3_5", "", 3, pubins_);
   TH1F* pile_up_histo_pred_mc_Njet6_7 = new TH1F("pile_up_histo_pred_mc_Njet6_7", "", 3, pubins_);
   TH1F* pile_up_histo_pred_mc_Njet8 = new TH1F("pile_up_histo_pred_mc_Njet8", "", 3, pubins_);

   // data seed events
   TH1F* pile_up_histo_seed_data_Njet2 = new TH1F("pile_up_histo_seed_data_Njet2", "", 3, pubins_);
   TH1F* pile_up_histo_seed_data_Njet3_5 = new TH1F("pile_up_histo_seed_data_Njet3_5", "", 3, pubins_);
   TH1F* pile_up_histo_seed_data_Njet6_7 = new TH1F("pile_up_histo_seed_data_Njet6_7", "", 3, pubins_);
   TH1F* pile_up_histo_seed_data_Njet8 = new TH1F("pile_up_histo_seed_data_Njet8", "", 3, pubins_);

   // mc seed events
   TH1F* pile_up_histo_seed_mc_Njet2 = new TH1F("pile_up_histo_seed_mc_Njet2", "", 3, pubins_);
   TH1F* pile_up_histo_seed_mc_Njet3_5 = new TH1F("pile_up_histo_seed_mc_Njet3_5", "", 3, pubins_);
   TH1F* pile_up_histo_seed_mc_Njet6_7 = new TH1F("pile_up_histo_seed_mc_Njet6_7", "", 3, pubins_);
   TH1F* pile_up_histo_seed_mc_Njet8 = new TH1F("pile_up_histo_seed_mc_Njet8", "", 3, pubins_);

   // define prediction histos
   // low bin
   MHT_JetBin1_HT_inclusive_pred_data_low = new TH2F("MHT_JetBin1_HT_inclusive_pred_data_low", "MHT_JetBin1_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
  
   MHT_JetBin2_HT_inclusive_pred_data_low = new TH2F("MHT_JetBin2_HT_inclusive_pred_data_low", "MHT_JetBin2_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
   
   MHT_JetBin3_HT_inclusive_pred_data_low = new TH2F("MHT_JetBin3_HT_inclusive_pred_data_low", "MHT_JetBin3_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
 
   MHT_JetBin4_HT_inclusive_pred_data_low = new TH2F("MHT_JetBin4_HT_inclusive_pred_data_low", "MHT_JetBin4_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);

   MHT_JetBin1_HT_inclusive_pred_mc_low = new TH2F("MHT_JetBin1_HT_inclusive_pred_mc_low", "MHT_JetBin1_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
  
   MHT_JetBin2_HT_inclusive_pred_mc_low = new TH2F("MHT_JetBin2_HT_inclusive_pred_mc_low", "MHT_JetBin2_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
   
   MHT_JetBin3_HT_inclusive_pred_mc_low = new TH2F("MHT_JetBin3_HT_inclusive_pred_mc_low", "MHT_JetBin3_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
 
   MHT_JetBin4_HT_inclusive_pred_mc_low = new TH2F("MHT_JetBin4_HT_inclusive_pred_mc_low", "MHT_JetBin4_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);

   // medium bin
   MHT_JetBin1_HT_inclusive_pred_data_medium = new TH2F("MHT_JetBin1_HT_inclusive_pred_data_medium", "MHT_JetBin1_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
  
   MHT_JetBin2_HT_inclusive_pred_data_medium = new TH2F("MHT_JetBin2_HT_inclusive_pred_data_medium", "MHT_JetBin2_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
   
   MHT_JetBin3_HT_inclusive_pred_data_medium = new TH2F("MHT_JetBin3_HT_inclusive_pred_data_medium", "MHT_JetBin3_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
 
   MHT_JetBin4_HT_inclusive_pred_data_medium = new TH2F("MHT_JetBin4_HT_inclusive_pred_data_medium", "MHT_JetBin4_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);

   MHT_JetBin1_HT_inclusive_pred_mc_medium = new TH2F("MHT_JetBin1_HT_inclusive_pred_mc_medium", "MHT_JetBin1_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
  
   MHT_JetBin2_HT_inclusive_pred_mc_medium = new TH2F("MHT_JetBin2_HT_inclusive_pred_mc_medium", "MHT_JetBin2_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
   
   MHT_JetBin3_HT_inclusive_pred_mc_medium = new TH2F("MHT_JetBin3_HT_inclusive_pred_mc_medium", "MHT_JetBin3_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
 
   MHT_JetBin4_HT_inclusive_pred_mc_medium = new TH2F("MHT_JetBin4_HT_inclusive_pred_mc_medium", "MHT_JetBin4_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);

   // high bin
   MHT_JetBin1_HT_inclusive_pred_data_high = new TH2F("MHT_JetBin1_HT_inclusive_pred_data_high", "MHT_JetBin1_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
  
   MHT_JetBin2_HT_inclusive_pred_data_high = new TH2F("MHT_JetBin2_HT_inclusive_pred_data_high", "MHT_JetBin2_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
   
   MHT_JetBin3_HT_inclusive_pred_data_high = new TH2F("MHT_JetBin3_HT_inclusive_pred_data_high", "MHT_JetBin3_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
 
   MHT_JetBin4_HT_inclusive_pred_data_high = new TH2F("MHT_JetBin4_HT_inclusive_pred_data_high", "MHT_JetBin4_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);

   MHT_JetBin1_HT_inclusive_pred_mc_high = new TH2F("MHT_JetBin1_HT_inclusive_pred_mc_high", "MHT_JetBin1_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
  
   MHT_JetBin2_HT_inclusive_pred_mc_high = new TH2F("MHT_JetBin2_HT_inclusive_pred_mc_high", "MHT_JetBin2_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
   
   MHT_JetBin3_HT_inclusive_pred_mc_high = new TH2F("MHT_JetBin3_HT_inclusive_pred_mc_high", "MHT_JetBin3_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);
 
   MHT_JetBin4_HT_inclusive_pred_mc_high = new TH2F("MHT_JetBin4_HT_inclusive_pred_mc_high", "MHT_JetBin4_HTinclusive_pred", 1, MHTmin_, MHTmax_, Ntries, 0.5, Ntries + 0.5);


   // get tree with predictions data
   cout << "entries prediction tree data:" << prediction_data->GetEntries() << endl;

   Float_t HT = 0;
   Float_t MHT = 0;
   UShort_t vtxN = 0;
   UShort_t NJets = 0;
   UShort_t NSmear = 0;
   Float_t weight = 0;
   Float_t DeltaPhi1 = 0;
   Float_t DeltaPhi2 = 0;
   Float_t DeltaPhi3 = 0;
   Float_t HT_seed = 0;

   prediction_data->SetBranchAddress("NVtx",&vtxN);
   prediction_data->SetBranchAddress("NJets",&NJets);
   prediction_data->SetBranchAddress("Ntries",&NSmear);
   prediction_data->SetBranchAddress("Weight",&weight);
   prediction_data->SetBranchAddress("HT",&HT);
   prediction_data->SetBranchAddress("MHT",&MHT);
   prediction_data->SetBranchAddress("DeltaPhi1",&DeltaPhi1);
   prediction_data->SetBranchAddress("DeltaPhi2",&DeltaPhi2);
   prediction_data->SetBranchAddress("DeltaPhi3",&DeltaPhi3);
   prediction_data->SetBranchAddress("HT_seed",&HT_seed);

   // used to count seed events
   // low PU
   double data_HT_JetBin1_lowPU_error = 0.;
   double data_HT_JetBin2_lowPU_error = 0.;
   double data_HT_JetBin3_lowPU_error = 0.;
   double data_HT_JetBin4_lowPU_error = 0.;
   double data_HT_JetBin1_lowPU = h_SeedEvents_HT_JetBin1_data->IntegralAndError(h_SeedEvents_HT_JetBin1_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin1_data->GetNbinsX(), 1, 11, data_HT_JetBin1_lowPU_error);
   double data_HT_JetBin2_lowPU = h_SeedEvents_HT_JetBin2_data->IntegralAndError(h_SeedEvents_HT_JetBin2_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin2_data->GetNbinsX(), 1, 11, data_HT_JetBin2_lowPU_error);
   double data_HT_JetBin3_lowPU = h_SeedEvents_HT_JetBin3_data->IntegralAndError(h_SeedEvents_HT_JetBin3_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin3_data->GetNbinsX(), 1, 11, data_HT_JetBin3_lowPU_error);
   double data_HT_JetBin4_lowPU = h_SeedEvents_HT_JetBin4_data->IntegralAndError(h_SeedEvents_HT_JetBin4_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin4_data->GetNbinsX(), 1, 11, data_HT_JetBin4_lowPU_error);

   // medium PU
   double data_HT_JetBin1_mediumPU_error = 0.;
   double data_HT_JetBin2_mediumPU_error = 0.;
   double data_HT_JetBin3_mediumPU_error = 0.;
   double data_HT_JetBin4_mediumPU_error = 0.;
   double data_HT_JetBin1_mediumPU = h_SeedEvents_HT_JetBin1_data->IntegralAndError(h_SeedEvents_HT_JetBin1_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin1_data->GetNbinsX(), 12, 21, data_HT_JetBin1_mediumPU_error);
   double data_HT_JetBin2_mediumPU = h_SeedEvents_HT_JetBin2_data->IntegralAndError(h_SeedEvents_HT_JetBin2_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin2_data->GetNbinsX(), 12, 21, data_HT_JetBin2_mediumPU_error); 
   double data_HT_JetBin3_mediumPU = h_SeedEvents_HT_JetBin3_data->IntegralAndError(h_SeedEvents_HT_JetBin3_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin3_data->GetNbinsX(), 12, 21, data_HT_JetBin3_mediumPU_error);
   double data_HT_JetBin4_mediumPU = h_SeedEvents_HT_JetBin4_data->IntegralAndError(h_SeedEvents_HT_JetBin4_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin4_data->GetNbinsX(), 12, 21, data_HT_JetBin4_mediumPU_error);

   // high PU
   double data_HT_JetBin1_highPU_error = 0.;
   double data_HT_JetBin2_highPU_error = 0.;
   double data_HT_JetBin3_highPU_error = 0.;
   double data_HT_JetBin4_highPU_error = 0.;
   double data_HT_JetBin1_highPU = h_SeedEvents_HT_JetBin1_data->IntegralAndError(h_SeedEvents_HT_JetBin1_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin1_data->GetNbinsX(), 22, h_SeedEvents_HT_JetBin1_data->GetNbinsY(), data_HT_JetBin1_highPU_error);
   double data_HT_JetBin2_highPU = h_SeedEvents_HT_JetBin2_data->IntegralAndError(h_SeedEvents_HT_JetBin2_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin2_data->GetNbinsX(), 22, h_SeedEvents_HT_JetBin2_data->GetNbinsY(), data_HT_JetBin2_highPU_error);
   double data_HT_JetBin3_highPU = h_SeedEvents_HT_JetBin3_data->IntegralAndError(h_SeedEvents_HT_JetBin3_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin3_data->GetNbinsX(), 22, h_SeedEvents_HT_JetBin3_data->GetNbinsY(), data_HT_JetBin3_highPU_error);
   double data_HT_JetBin4_highPU = h_SeedEvents_HT_JetBin4_data->IntegralAndError(h_SeedEvents_HT_JetBin4_data->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin4_data->GetNbinsX(), 22, h_SeedEvents_HT_JetBin4_data->GetNbinsY(), data_HT_JetBin4_highPU_error);

   // ------------------------------------------------------------- //
   // fill low PU bin data seed events
   pile_up_histo_seed_data_Njet2->SetBinContent(1, data_HT_JetBin1_lowPU);
   pile_up_histo_seed_data_Njet2->SetBinError(1, data_HT_JetBin1_lowPU_error);
   pile_up_histo_seed_data_Njet3_5->SetBinContent(1, data_HT_JetBin2_lowPU);
   pile_up_histo_seed_data_Njet3_5->SetBinError(1, data_HT_JetBin2_lowPU_error);
   pile_up_histo_seed_data_Njet6_7->SetBinContent(1, data_HT_JetBin3_lowPU);
   pile_up_histo_seed_data_Njet6_7->SetBinError(1, data_HT_JetBin3_lowPU_error);
   pile_up_histo_seed_data_Njet8->SetBinContent(1, data_HT_JetBin4_lowPU);
   pile_up_histo_seed_data_Njet8->SetBinError(1, data_HT_JetBin4_lowPU_error);

   // fill medium PU bin data seed events
   pile_up_histo_seed_data_Njet2->SetBinContent(2, data_HT_JetBin1_mediumPU);
   pile_up_histo_seed_data_Njet2->SetBinError(2, data_HT_JetBin1_mediumPU_error);
   pile_up_histo_seed_data_Njet3_5->SetBinContent(2, data_HT_JetBin2_mediumPU);
   pile_up_histo_seed_data_Njet3_5->SetBinError(2, data_HT_JetBin2_mediumPU_error);
   pile_up_histo_seed_data_Njet6_7->SetBinContent(2, data_HT_JetBin3_mediumPU);
   pile_up_histo_seed_data_Njet6_7->SetBinError(2, data_HT_JetBin3_mediumPU_error);
   pile_up_histo_seed_data_Njet8->SetBinContent(2, data_HT_JetBin4_mediumPU);
   pile_up_histo_seed_data_Njet8->SetBinError(2, data_HT_JetBin4_mediumPU_error);

   // fill medium PU bin data seed events
   pile_up_histo_seed_data_Njet2->SetBinContent(3, data_HT_JetBin1_highPU);
   pile_up_histo_seed_data_Njet2->SetBinError(3, data_HT_JetBin1_highPU_error);
   pile_up_histo_seed_data_Njet3_5->SetBinContent(3, data_HT_JetBin2_highPU);
   pile_up_histo_seed_data_Njet3_5->SetBinError(3, data_HT_JetBin2_highPU_error);
   pile_up_histo_seed_data_Njet6_7->SetBinContent(3, data_HT_JetBin3_highPU);
   pile_up_histo_seed_data_Njet6_7->SetBinError(3, data_HT_JetBin3_highPU_error);
   pile_up_histo_seed_data_Njet8->SetBinContent(3, data_HT_JetBin4_highPU);
   pile_up_histo_seed_data_Njet8->SetBinError(3, data_HT_JetBin4_highPU_error);
   // ------------------------------------------------------------- //

   // loop over entries and fill prediction histos
   ULong_t nentries = prediction_data->GetEntries();
   //Int_t nentries = 10000000;
   for ( ULong_t i = 0 ; i<nentries ; i++) {
      prediction_data->GetEntry(i);

      if( i%1000000 == 0 ) std::cout << "event prediction data: " << i << '\n';
            
      // ------------------------------------------------------------- //
      // check deltaPhi cut
      if( DeltaPhiCut(NJets, DeltaPhi1, DeltaPhi2, DeltaPhi3) ) {    
         
         //  fill different jet multiplicity bins
         //  if( 500. < HT  && 200. < MHT) {
         if( 500. < HT  && 100. < MHT ) {

            // cut on vertices
            // low PU
            if( vtxN <= pubins_[1] ){
               // jet bin 1
               if( NJets == 2 ) {
                  MHT_JetBin1_HT_inclusive_pred_data_low->Fill(MHT, NSmear, weight);
               }
               // jet bin 2
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  MHT_JetBin2_HT_inclusive_pred_data_low->Fill(MHT, NSmear, weight); 
               }
               // jet bin 3            
               else if(  NJets == 6  ||  NJets == 7 ) {
                  MHT_JetBin3_HT_inclusive_pred_data_low->Fill(MHT, NSmear, weight); 
               }
               // jet bin 4 
               else if(  NJets >= 8 ) {
                  MHT_JetBin4_HT_inclusive_pred_data_low->Fill(MHT, NSmear, weight);  
                  if( HT_seed != data_HT_JetBin4_lowPU ) {
                  }
               }
            }
            // medium PU
            if( vtxN > pubins_[1] && vtxN <= pubins_[2] ){
               // jet bin 1
               if( NJets == 2 ) {
                  MHT_JetBin1_HT_inclusive_pred_data_medium->Fill(MHT, NSmear, weight);
               }
               // jet bin 2
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  MHT_JetBin2_HT_inclusive_pred_data_medium->Fill(MHT, NSmear, weight); 
               }
               // jet bin 3            
               else if(  NJets == 6  ||  NJets == 7 ) {
                  MHT_JetBin3_HT_inclusive_pred_data_medium->Fill(MHT, NSmear, weight);
               }
               // jet bin 4 
               else if(  NJets >= 8 ) {
                  MHT_JetBin4_HT_inclusive_pred_data_medium->Fill(MHT, NSmear, weight);  
               }
            }
            
            // high PU
            if( vtxN > pubins_[2] ){
               // jet bin 1
               if( NJets == 2 ) {
                  MHT_JetBin1_HT_inclusive_pred_data_high->Fill(MHT, NSmear, weight);
               }
               // jet bin 2
               else if( NJets == 3 || NJets == 4 ||  NJets == 5 ) {
                  MHT_JetBin2_HT_inclusive_pred_data_high->Fill(MHT, NSmear, weight); 
               }
               // jet bin 3            
               else if(  NJets == 6  ||  NJets == 7 ) {
                  MHT_JetBin3_HT_inclusive_pred_data_high->Fill(MHT, NSmear, weight); 
               }
               // jet bin 4 
               else if(  NJets >= 8 ) {
                  MHT_JetBin4_HT_inclusive_pred_data_high->Fill(MHT, NSmear, weight); 
               }
            }
         }      
      }    
   } 

   // fill low PU bin data pred
   pile_up_histo_pred_data_Njet2->SetBinContent(1, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_data_low)->GetBinContent(1));
   pile_up_histo_pred_data_Njet2->SetBinError(1,CalcPrediction(MHT_JetBin1_HT_inclusive_pred_data_low)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet3_5->SetBinContent(1, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_data_low)->GetBinContent(1));
   pile_up_histo_pred_data_Njet3_5->SetBinError(1, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_data_low)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet6_7->SetBinContent(1, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_data_low)->GetBinContent(1));
   pile_up_histo_pred_data_Njet6_7->SetBinError(1, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_data_low)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet8->SetBinContent(1, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_data_low)->GetBinContent(1));
   pile_up_histo_pred_data_Njet8->SetBinError(1, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_data_low)->GetBinError(1)/10);

   // fill medium PU bin data pred
   pile_up_histo_pred_data_Njet2->SetBinContent(2, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_data_medium)->GetBinContent(1));
   pile_up_histo_pred_data_Njet2->SetBinError(2, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_data_medium)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet3_5->SetBinContent(2, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_data_medium)->GetBinContent(1));
   pile_up_histo_pred_data_Njet3_5->SetBinError(2, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_data_medium)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet6_7->SetBinContent(2, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_data_medium)->GetBinContent(1));
   pile_up_histo_pred_data_Njet6_7->SetBinError(2, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_data_medium)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet8->SetBinContent(2, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_data_medium)->GetBinContent(1));
   pile_up_histo_pred_data_Njet8->SetBinError(2, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_data_medium)->GetBinError(1)/10);
  
   // fill high PU bin data pred
   pile_up_histo_pred_data_Njet2->SetBinContent(3, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_data_high)->GetBinContent(1));
   pile_up_histo_pred_data_Njet2->SetBinError(3, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_data_high)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet3_5->SetBinContent(3, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_data_high)->GetBinContent(1));
   pile_up_histo_pred_data_Njet3_5->SetBinError(3, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_data_high)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet6_7->SetBinContent(3, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_data_high)->GetBinContent(1));
   pile_up_histo_pred_data_Njet6_7->SetBinError(3, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_data_high)->GetBinError(1)/10);
   pile_up_histo_pred_data_Njet8->SetBinContent(3, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_data_high)->GetBinContent(1));
   pile_up_histo_pred_data_Njet8->SetBinError(3, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_data_high)->GetBinError(1)/10);

   ///////////////////////////////////////////////////////////////////////////////////

   // get tree with predictions mc
   cout << "entries prediction tree mc:" << prediction_mc->GetEntries() << endl;

   Float_t HT_pred_mc = 0;
   Float_t MHT_pred_mc = 0;
   UShort_t vtxN_pred_mc = 0;
   UShort_t NJets_pred_mc = 0;
   UShort_t NSmear_pred_mc = 0;
   Float_t weight_pred_mc = 0;
   Float_t DeltaPhi1_pred_mc = 0;
   Float_t DeltaPhi2_pred_mc = 0;
   Float_t DeltaPhi3_pred_mc = 0;
   Float_t HT_seed_mc = 0;

   prediction_mc->SetBranchAddress("NVtx",&vtxN_pred_mc);
   prediction_mc->SetBranchAddress("NJets",&NJets_pred_mc);
   prediction_mc->SetBranchAddress("Ntries",&NSmear_pred_mc);
   prediction_mc->SetBranchAddress("Weight",&weight_pred_mc);
   prediction_mc->SetBranchAddress("HT",&HT_pred_mc);
   prediction_mc->SetBranchAddress("MHT",&MHT_pred_mc);
   prediction_mc->SetBranchAddress("DeltaPhi1",&DeltaPhi1_pred_mc);
   prediction_mc->SetBranchAddress("DeltaPhi2",&DeltaPhi2_pred_mc);
   prediction_mc->SetBranchAddress("DeltaPhi3",&DeltaPhi3_pred_mc);
   prediction_mc->SetBranchAddress("HT_seed",&HT_seed_mc);

   // used to count seed events
   // low PU
   double mc_HT_JetBin1_lowPU_error = 0.;
   double mc_HT_JetBin2_lowPU_error = 0.;
   double mc_HT_JetBin3_lowPU_error = 0.;
   double mc_HT_JetBin4_lowPU_error = 0.;
   double mc_HT_JetBin1_lowPU = h_SeedEvents_HT_JetBin1_mc->IntegralAndError(h_SeedEvents_HT_JetBin1_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin1_mc->GetNbinsX(), 1, 11, mc_HT_JetBin1_lowPU_error);
   double mc_HT_JetBin2_lowPU = h_SeedEvents_HT_JetBin2_mc->IntegralAndError(h_SeedEvents_HT_JetBin2_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin2_mc->GetNbinsX(), 1, 11, mc_HT_JetBin2_lowPU_error);
   double mc_HT_JetBin3_lowPU = h_SeedEvents_HT_JetBin3_mc->IntegralAndError(h_SeedEvents_HT_JetBin3_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin3_mc->GetNbinsX(), 1, 11, mc_HT_JetBin3_lowPU_error);
   double mc_HT_JetBin4_lowPU = h_SeedEvents_HT_JetBin4_mc->IntegralAndError(h_SeedEvents_HT_JetBin4_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin4_mc->GetNbinsX(), 1, 11, mc_HT_JetBin4_lowPU_error);

   // medium PU
   double mc_HT_JetBin1_mediumPU_error = 0.;
   double mc_HT_JetBin2_mediumPU_error = 0.;
   double mc_HT_JetBin3_mediumPU_error = 0.;
   double mc_HT_JetBin4_mediumPU_error = 0.;
   double mc_HT_JetBin1_mediumPU = h_SeedEvents_HT_JetBin1_mc->IntegralAndError(h_SeedEvents_HT_JetBin1_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin1_mc->GetNbinsX(), 12, 21, mc_HT_JetBin1_mediumPU_error);
   double mc_HT_JetBin2_mediumPU = h_SeedEvents_HT_JetBin2_mc->IntegralAndError(h_SeedEvents_HT_JetBin2_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin2_mc->GetNbinsX(), 12, 21, mc_HT_JetBin2_mediumPU_error); 
   double mc_HT_JetBin3_mediumPU = h_SeedEvents_HT_JetBin3_mc->IntegralAndError(h_SeedEvents_HT_JetBin3_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin3_mc->GetNbinsX(), 12, 21, mc_HT_JetBin3_mediumPU_error);
   double mc_HT_JetBin4_mediumPU = h_SeedEvents_HT_JetBin4_mc->IntegralAndError(h_SeedEvents_HT_JetBin4_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin4_mc->GetNbinsX(), 12, 21, mc_HT_JetBin4_mediumPU_error);

   // high PU
   double mc_HT_JetBin1_highPU_error = 0.;
   double mc_HT_JetBin2_highPU_error = 0.;
   double mc_HT_JetBin3_highPU_error = 0.;
   double mc_HT_JetBin4_highPU_error = 0.;
   double mc_HT_JetBin1_highPU = h_SeedEvents_HT_JetBin1_mc->IntegralAndError(h_SeedEvents_HT_JetBin1_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin1_mc->GetNbinsX(), 22, h_SeedEvents_HT_JetBin1_mc->GetNbinsY(), mc_HT_JetBin1_highPU_error);
   double mc_HT_JetBin2_highPU = h_SeedEvents_HT_JetBin2_mc->IntegralAndError(h_SeedEvents_HT_JetBin2_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin2_mc->GetNbinsX(), 22, h_SeedEvents_HT_JetBin2_mc->GetNbinsY(), mc_HT_JetBin2_highPU_error);
   double mc_HT_JetBin3_highPU = h_SeedEvents_HT_JetBin3_mc->IntegralAndError(h_SeedEvents_HT_JetBin3_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin3_mc->GetNbinsX(), 22, h_SeedEvents_HT_JetBin3_mc->GetNbinsY(), mc_HT_JetBin3_highPU_error);
   double mc_HT_JetBin4_highPU = h_SeedEvents_HT_JetBin4_mc->IntegralAndError(h_SeedEvents_HT_JetBin4_mc->ProjectionX()->FindBin(500.), h_SeedEvents_HT_JetBin4_mc->GetNbinsX(), 22, h_SeedEvents_HT_JetBin4_mc->GetNbinsY(), mc_HT_JetBin4_highPU_error);

   // ------------------------------------------------------------- //
   // fill low PU bin mc seed events
   pile_up_histo_seed_mc_Njet2->SetBinContent(1, mc_HT_JetBin1_lowPU);
   pile_up_histo_seed_mc_Njet2->SetBinError(1, mc_HT_JetBin1_lowPU_error);
   pile_up_histo_seed_mc_Njet3_5->SetBinContent(1, mc_HT_JetBin2_lowPU);
   pile_up_histo_seed_mc_Njet3_5->SetBinError(1, mc_HT_JetBin2_lowPU_error);
   pile_up_histo_seed_mc_Njet6_7->SetBinContent(1, mc_HT_JetBin3_lowPU);
   pile_up_histo_seed_mc_Njet6_7->SetBinError(1, mc_HT_JetBin3_lowPU_error);
   pile_up_histo_seed_mc_Njet8->SetBinContent(1, mc_HT_JetBin4_lowPU);
   pile_up_histo_seed_mc_Njet8->SetBinError(1, mc_HT_JetBin4_lowPU_error);

   // fill medium PU bin mc seed events
   pile_up_histo_seed_mc_Njet2->SetBinContent(2, mc_HT_JetBin1_mediumPU);
   pile_up_histo_seed_mc_Njet2->SetBinError(2, mc_HT_JetBin1_mediumPU_error);
   pile_up_histo_seed_mc_Njet3_5->SetBinContent(2, mc_HT_JetBin2_mediumPU);
   pile_up_histo_seed_mc_Njet3_5->SetBinError(2, mc_HT_JetBin2_mediumPU_error);
   pile_up_histo_seed_mc_Njet6_7->SetBinContent(2, mc_HT_JetBin3_mediumPU);
   pile_up_histo_seed_mc_Njet6_7->SetBinError(2, mc_HT_JetBin3_mediumPU_error);
   pile_up_histo_seed_mc_Njet8->SetBinContent(2, mc_HT_JetBin4_mediumPU);
   pile_up_histo_seed_mc_Njet8->SetBinError(2, mc_HT_JetBin4_mediumPU_error);

   // fill medium PU bin mc seed events
   pile_up_histo_seed_mc_Njet2->SetBinContent(3, mc_HT_JetBin1_highPU);
   pile_up_histo_seed_mc_Njet2->SetBinError(3, mc_HT_JetBin1_highPU_error);
   pile_up_histo_seed_mc_Njet3_5->SetBinContent(3, mc_HT_JetBin2_highPU);
   pile_up_histo_seed_mc_Njet3_5->SetBinError(3, mc_HT_JetBin2_highPU_error);
   pile_up_histo_seed_mc_Njet6_7->SetBinContent(3, mc_HT_JetBin3_highPU);
   pile_up_histo_seed_mc_Njet6_7->SetBinError(3, mc_HT_JetBin3_highPU_error);
   pile_up_histo_seed_mc_Njet8->SetBinContent(3, mc_HT_JetBin4_highPU);
   pile_up_histo_seed_mc_Njet8->SetBinError(3, mc_HT_JetBin4_highPU_error);
   // ------------------------------------------------------------- //

   // loop over entries and fill prediction histos
   ULong_t nentries2 = prediction_mc->GetEntries();
   //Int_t nentries2 = 10000000;
   for ( ULong_t i = 0 ; i<nentries2 ; i++) {
      prediction_mc->GetEntry(i);

      if( i%1000000 == 0 ) std::cout << "event prediction mc: " << i << '\n';

      // select reasonable event weights
      if( weight_pred_mc < 30000. ) {
                 
         // ------------------------------------------------------------- //
         // check deltaPhi cut
         if( DeltaPhiCut(NJets_pred_mc, DeltaPhi1_pred_mc, DeltaPhi2_pred_mc, DeltaPhi3_pred_mc) ) {    
         
            //  fill different jet multiplicity bins
            // if( 500. < HT_pred_mc && 200. < MHT_pred_mc) {
            if( 500. < HT_pred_mc  && 100. < MHT_pred_mc ) {

               // cut on vertices
               // low PU
               if( vtxN_pred_mc <= pubins_[1] ){
                  // jet bin 1
                  if( NJets_pred_mc == 2 ) {
                     MHT_JetBin1_HT_inclusive_pred_mc_low->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);
                  }
                  // jet bin 2
                  else if( NJets_pred_mc == 3 || NJets_pred_mc == 4 ||  NJets_pred_mc == 5 ) {
                     MHT_JetBin2_HT_inclusive_pred_mc_low->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);
                  }
                  // jet bin 3            
                  else if(  NJets_pred_mc == 6  ||  NJets_pred_mc == 7 ) {
                     MHT_JetBin3_HT_inclusive_pred_mc_low->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);
                  }
                  // jet bin 4 
                  else if(  NJets_pred_mc >= 8 ) {
                     MHT_JetBin4_HT_inclusive_pred_mc_low->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);
                  }
               }
               // medium PU
               if( vtxN_pred_mc > pubins_[1] && vtxN_pred_mc <= pubins_[2] ){
                  // jet bin 1
                  if( NJets_pred_mc == 2 ) {
                     MHT_JetBin1_HT_inclusive_pred_mc_medium->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);
                  }
                  // jet bin 2
                  else if( NJets_pred_mc == 3 || NJets_pred_mc == 4 ||  NJets_pred_mc == 5 ) {
                     MHT_JetBin2_HT_inclusive_pred_mc_medium->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc); 
                  }
                  // jet bin 3            
                  else if(  NJets_pred_mc == 6  ||  NJets_pred_mc == 7 ) {
                     MHT_JetBin3_HT_inclusive_pred_mc_medium->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);          
                  }
                  // jet bin 4 
                  else if(  NJets_pred_mc >= 8 ) {
                     MHT_JetBin4_HT_inclusive_pred_mc_medium->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);                    
                  }
               }
               // high PU
               if( vtxN_pred_mc > pubins_[2] ){
                  // jet bin 1
                  if( NJets_pred_mc == 2 ) {
                     MHT_JetBin1_HT_inclusive_pred_mc_high->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);
                  }
                  // jet bin 2
                  else if( NJets_pred_mc == 3 || NJets_pred_mc == 4 ||  NJets_pred_mc == 5 ) {
                     MHT_JetBin2_HT_inclusive_pred_mc_high->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc); 
                  }
                  // jet bin 3            
                  else if(  NJets_pred_mc == 6  ||  NJets_pred_mc == 7 ) {
                     MHT_JetBin3_HT_inclusive_pred_mc_high->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);                 
                  }
                  // jet bin 4 
                  else if(  NJets_pred_mc >= 8 ) {
                     MHT_JetBin4_HT_inclusive_pred_mc_high->Fill(MHT_pred_mc, NSmear_pred_mc, weight_pred_mc);                      
                  }
               }
            }      
         }    
      }
   }

   // fill low PU bin mc pred
   pile_up_histo_pred_mc_Njet2->SetBinContent(1, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_mc_low)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet2->SetBinError(1,CalcPrediction(MHT_JetBin1_HT_inclusive_pred_mc_low)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet3_5->SetBinContent(1, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_mc_low)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet3_5->SetBinError(1, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_mc_low)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet6_7->SetBinContent(1, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_mc_low)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet6_7->SetBinError(1, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_mc_low)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet8->SetBinContent(1, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_mc_low)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet8->SetBinError(1, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_mc_low)->GetBinError(1)/10);

   // fill medium PU bin mc pred
   pile_up_histo_pred_mc_Njet2->SetBinContent(2, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_mc_medium)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet2->SetBinError(2, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_mc_medium)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet3_5->SetBinContent(2, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_mc_medium)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet3_5->SetBinError(2, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_mc_medium)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet6_7->SetBinContent(2, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_mc_medium)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet6_7->SetBinError(2, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_mc_medium)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet8->SetBinContent(2, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_mc_medium)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet8->SetBinError(2, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_mc_medium)->GetBinError(1)/10);
  
   // fill high PU bin mc pred
   pile_up_histo_pred_mc_Njet2->SetBinContent(3, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_mc_high)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet2->SetBinError(3, CalcPrediction(MHT_JetBin1_HT_inclusive_pred_mc_high)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet3_5->SetBinContent(3, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_mc_high)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet3_5->SetBinError(3, CalcPrediction(MHT_JetBin2_HT_inclusive_pred_mc_high)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet6_7->SetBinContent(3, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_mc_high)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet6_7->SetBinError(3, CalcPrediction(MHT_JetBin3_HT_inclusive_pred_mc_high)->GetBinError(1)/10);
   pile_up_histo_pred_mc_Njet8->SetBinContent(3, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_mc_high)->GetBinContent(1));
   pile_up_histo_pred_mc_Njet8->SetBinError(3, CalcPrediction(MHT_JetBin4_HT_inclusive_pred_mc_high)->GetBinError(1)/10);

   /////////////////////////////////////////////////////////////////////////////////
  
   // divide prediction histos by seed event histos
   TH1F *pile_up_histo_data_Njet2 = new TH1F("pile_up_histo_data_Njet2", "", 3, pubins_);
   pile_up_histo_data_Njet2->Divide(pile_up_histo_pred_data_Njet2, pile_up_histo_seed_data_Njet2);
   TH1F *pile_up_histo_data_Njet3_5 = new TH1F("pile_up_histo_data_Njet3_5", "", 3, pubins_);
   pile_up_histo_data_Njet3_5->Divide(pile_up_histo_pred_data_Njet3_5, pile_up_histo_seed_data_Njet3_5);
   TH1F *pile_up_histo_data_Njet6_7 = new TH1F("pile_up_histo_data_Njet6_7", "", 3, pubins_);
   pile_up_histo_data_Njet6_7->Divide(pile_up_histo_pred_data_Njet6_7, pile_up_histo_seed_data_Njet6_7);
   TH1F *pile_up_histo_data_Njet8 = new TH1F("pile_up_histo_data_Njet8", "", 3, pubins_);
   pile_up_histo_data_Njet8->Divide(pile_up_histo_pred_data_Njet8, pile_up_histo_seed_data_Njet8);


   TH1F *pile_up_histo_mc_Njet2 = new TH1F("pile_up_histo_mc_Njet2", "", 3, pubins_);
   pile_up_histo_mc_Njet2->Divide(pile_up_histo_pred_mc_Njet2, pile_up_histo_seed_mc_Njet2);
   pile_up_histo_mc_Njet2->Scale(pile_up_histo_data_Njet2->GetBinContent(1)/pile_up_histo_mc_Njet2->GetBinContent(1));
   TH1F *pile_up_histo_mc_Njet3_5 = new TH1F("pile_up_histo_mc_Njet3_5", "", 3, pubins_);
   pile_up_histo_mc_Njet3_5->Divide(pile_up_histo_pred_mc_Njet3_5, pile_up_histo_seed_mc_Njet3_5);
   pile_up_histo_mc_Njet3_5->Scale(pile_up_histo_data_Njet3_5->GetBinContent(1)/pile_up_histo_mc_Njet3_5->GetBinContent(1));
   TH1F *pile_up_histo_mc_Njet6_7 = new TH1F("pile_up_histo_mc_Njet6_7", "", 3, pubins_);
   pile_up_histo_mc_Njet6_7->Divide(pile_up_histo_pred_mc_Njet6_7, pile_up_histo_seed_mc_Njet6_7);
   pile_up_histo_mc_Njet6_7->Scale(pile_up_histo_data_Njet6_7->GetBinContent(1)/pile_up_histo_mc_Njet6_7->GetBinContent(1));
   TH1F *pile_up_histo_mc_Njet8 = new TH1F("pile_up_histo_mc_Njet8", "", 3, pubins_);
   pile_up_histo_mc_Njet8->Divide(pile_up_histo_pred_mc_Njet8, pile_up_histo_seed_mc_Njet8);
   pile_up_histo_mc_Njet8->Scale(pile_up_histo_data_Njet8->GetBinContent(1)/pile_up_histo_mc_Njet8->GetBinContent(1));

   ////////////////////////////////////////////////////////////////////////
  
   // --------------------------------------------------------------- //
   // calc PU Uncertainty nominal from bins
   // --------------------------------------------------------------- //
   double x_NJet2_data = TMath::Abs(pile_up_histo_mc_Njet2->GetBinContent(2) - pile_up_histo_data_Njet2->GetBinContent(2)) * pile_up_histo_seed_data_Njet2->GetBinContent(2)
      + TMath::Abs(pile_up_histo_mc_Njet2->GetBinContent(3) - pile_up_histo_data_Njet2->GetBinContent(3)) * pile_up_histo_seed_data_Njet2->GetBinContent(3);
   double x_NJet3_5_data = TMath::Abs(pile_up_histo_mc_Njet3_5->GetBinContent(2) - pile_up_histo_data_Njet3_5->GetBinContent(2)) * pile_up_histo_seed_data_Njet3_5->GetBinContent(2)
      + TMath::Abs(pile_up_histo_mc_Njet3_5->GetBinContent(3) - pile_up_histo_data_Njet3_5->GetBinContent(3)) * pile_up_histo_seed_data_Njet3_5->GetBinContent(3);
   double x_NJet6_7_data = TMath::Abs(pile_up_histo_mc_Njet6_7->GetBinContent(2) - pile_up_histo_data_Njet6_7->GetBinContent(2)) * pile_up_histo_seed_data_Njet6_7->GetBinContent(2)
      + TMath::Abs(pile_up_histo_mc_Njet6_7->GetBinContent(3) - pile_up_histo_data_Njet6_7->GetBinContent(3)) * pile_up_histo_seed_data_Njet6_7->GetBinContent(3);
   double x_NJet8_data = TMath::Abs(pile_up_histo_mc_Njet8->GetBinContent(2) - pile_up_histo_data_Njet8->GetBinContent(2)) * pile_up_histo_seed_data_Njet8->GetBinContent(2)
      + TMath::Abs(pile_up_histo_mc_Njet8->GetBinContent(3) - pile_up_histo_data_Njet8->GetBinContent(3)) * pile_up_histo_seed_data_Njet8->GetBinContent(3);
   
   // --------------------------------------------------------------- //
   // calc prediction
   // --------------------------------------------------------------- //
   double pred_NJet2_data = (pile_up_histo_pred_data_Njet2->GetBinContent(1) + pile_up_histo_pred_data_Njet2->GetBinContent(2) + pile_up_histo_pred_data_Njet2->GetBinContent(3));
   double pred_NJet3_5_data = (pile_up_histo_pred_data_Njet3_5->GetBinContent(1) + pile_up_histo_pred_data_Njet3_5->GetBinContent(2) + pile_up_histo_pred_data_Njet3_5->GetBinContent(3));
   double pred_NJet6_7_data = (pile_up_histo_pred_data_Njet6_7->GetBinContent(1) + pile_up_histo_pred_data_Njet6_7->GetBinContent(2) + pile_up_histo_pred_data_Njet6_7->GetBinContent(3));
   double pred_NJet8_data = (pile_up_histo_pred_data_Njet8->GetBinContent(1) + pile_up_histo_pred_data_Njet8->GetBinContent(2) + pile_up_histo_pred_data_Njet8->GetBinContent(3));

   double sigma_pred_squared_NJet2 = pow(pile_up_histo_pred_data_Njet2->GetBinError(1), 2) + pow(pile_up_histo_pred_data_Njet2->GetBinError(2), 2) + pow(pile_up_histo_pred_data_Njet2->GetBinError(3), 2);
   double sigma_pred_squared_NJet3_5 = pow(pile_up_histo_pred_data_Njet3_5->GetBinError(1), 2) + pow(pile_up_histo_pred_data_Njet3_5->GetBinError(2), 2) + pow(pile_up_histo_pred_data_Njet3_5->GetBinError(3), 2);
   double sigma_pred_squared_NJet6_7 = pow(pile_up_histo_pred_data_Njet6_7->GetBinError(1), 2) + pow(pile_up_histo_pred_data_Njet6_7->GetBinError(2), 2) + pow(pile_up_histo_pred_data_Njet6_7->GetBinError(3), 2);
   double sigma_pred_squared_NJet8 = pow(pile_up_histo_pred_data_Njet8->GetBinError(1), 2) + pow(pile_up_histo_pred_data_Njet8->GetBinError(2), 2) + pow(pile_up_histo_pred_data_Njet8->GetBinError(3), 2);

   // --------------------------------------------------------------- //

   // --------------------------------------------------------------- //
   // calc uncertainty on uncertainty
   // --------------------------------------------------------------- //
   // NJet 2
   double c1_NJet2 = pow(pile_up_histo_seed_data_Njet2->GetBinContent(2) * pile_up_histo_mc_Njet2->GetBinError(2),2);

   double c4_NJet2 = pow(pile_up_histo_seed_data_Njet2->GetBinContent(2) * pile_up_histo_data_Njet2->GetBinError(2),2);

   double c5_NJet2 = pow((pile_up_histo_mc_Njet2->GetBinContent(2) - pile_up_histo_data_Njet2->GetBinContent(2)) * pile_up_histo_seed_data_Njet2->GetBinError(2),2);

   double c6_NJet2 = pow(pile_up_histo_seed_data_Njet2->GetBinContent(3) * pile_up_histo_mc_Njet2->GetBinError(3),2);

   double c7_NJet2 = pow(pile_up_histo_seed_data_Njet2->GetBinContent(3) * pile_up_histo_data_Njet2->GetBinError(3),2);

   double c8_NJet2 = pow((pile_up_histo_mc_Njet2->GetBinContent(3) - pile_up_histo_data_Njet2->GetBinContent(3)) * pile_up_histo_seed_data_Njet2->GetBinError(3),2);

   double sigma_x_squared_NJet2 = c1_NJet2 +/* c2_NJet2 + c3_NJet2 +*/ c4_NJet2 + c5_NJet2 + c6_NJet2 + c7_NJet2 + c8_NJet2;

   // --------------------------------------------------------------- //
   // NJet 3-5
   double c1_NJet3_5 = pow(pile_up_histo_seed_data_Njet3_5->GetBinContent(2) * pile_up_histo_mc_Njet3_5->GetBinError(2),2);

   double c4_NJet3_5 = pow(pile_up_histo_seed_data_Njet3_5->GetBinContent(2) * pile_up_histo_data_Njet3_5->GetBinError(2),2);

   double c5_NJet3_5 = pow((pile_up_histo_mc_Njet3_5->GetBinContent(2) - pile_up_histo_data_Njet3_5->GetBinContent(2)) * pile_up_histo_seed_data_Njet3_5->GetBinError(2),2);

   double c6_NJet3_5 = pow(pile_up_histo_seed_data_Njet3_5->GetBinContent(3) * pile_up_histo_mc_Njet3_5->GetBinError(3),2);

   double c7_NJet3_5 = pow(pile_up_histo_seed_data_Njet3_5->GetBinContent(3) * pile_up_histo_data_Njet3_5->GetBinError(3),2);

   double c8_NJet3_5 = pow((pile_up_histo_mc_Njet3_5->GetBinContent(3) - pile_up_histo_data_Njet3_5->GetBinContent(3)) * pile_up_histo_seed_data_Njet3_5->GetBinError(3),2);

   double sigma_x_squared_NJet3_5 = c1_NJet3_5 + /*c2_NJet3_5 + c3_NJet3_5 + */c4_NJet3_5 + c5_NJet3_5 + c6_NJet3_5 + c7_NJet3_5 + c8_NJet3_5;

   // --------------------------------------------------------------- //
   // NJet 6-7
   double c1_NJet6_7 = pow(pile_up_histo_seed_data_Njet6_7->GetBinContent(2) * pile_up_histo_mc_Njet6_7->GetBinError(2),2);

   double c4_NJet6_7 = pow(pile_up_histo_seed_data_Njet6_7->GetBinContent(2) * pile_up_histo_data_Njet6_7->GetBinError(2),2);

   double c5_NJet6_7 = pow((pile_up_histo_mc_Njet6_7->GetBinContent(2) - pile_up_histo_data_Njet6_7->GetBinContent(2)) * pile_up_histo_seed_data_Njet6_7->GetBinError(2),2);

   double c6_NJet6_7 = pow(pile_up_histo_seed_data_Njet6_7->GetBinContent(3) * pile_up_histo_mc_Njet6_7->GetBinError(3),2);

   double c7_NJet6_7 = pow(pile_up_histo_seed_data_Njet6_7->GetBinContent(3) * pile_up_histo_data_Njet6_7->GetBinError(3),2);

   double c8_NJet6_7 = pow((pile_up_histo_mc_Njet6_7->GetBinContent(3) - pile_up_histo_data_Njet6_7->GetBinContent(3)) * pile_up_histo_seed_data_Njet6_7->GetBinError(3),2);

   double sigma_x_squared_NJet6_7 = c1_NJet6_7 + /*c2_NJet6_7 + c3_NJet6_7 +*/ c4_NJet6_7 + c5_NJet6_7 + c6_NJet6_7 + c7_NJet6_7 + c8_NJet6_7;

   // --------------------------------------------------------------- //
   // NJet >=8
   double c1_NJet8 = pow(pile_up_histo_seed_data_Njet8->GetBinContent(2) * pile_up_histo_mc_Njet8->GetBinError(2),2);

   double c4_NJet8 = pow(pile_up_histo_seed_data_Njet8->GetBinContent(2) * pile_up_histo_data_Njet8->GetBinError(2),2);

   double c5_NJet8 = pow((pile_up_histo_mc_Njet8->GetBinContent(2) - pile_up_histo_data_Njet8->GetBinContent(2)) * pile_up_histo_seed_data_Njet8->GetBinError(2),2);

   double c6_NJet8 = pow(pile_up_histo_seed_data_Njet8->GetBinContent(3) * pile_up_histo_mc_Njet8->GetBinError(3),2);

   double c7_NJet8 = pow(pile_up_histo_seed_data_Njet8->GetBinContent(3) * pile_up_histo_data_Njet8->GetBinError(3),2);

   double c8_NJet8 = pow((pile_up_histo_mc_Njet8->GetBinContent(3) - pile_up_histo_data_Njet8->GetBinContent(3)) * pile_up_histo_seed_data_Njet8->GetBinError(3),2);

   double sigma_x_squared_NJet8 = c1_NJet8 + /*c2_NJet8 + c3_NJet8 + */c4_NJet8 + c5_NJet8 + c6_NJet8 + c7_NJet8 + c8_NJet8;

   // --------------------------------------------------------------- //
   
   ofstream PUUncertainty_outfile;
   PUUncertainty_outfile.open("PUUncertainty_DR53X_MHT100_v2.txt");
   // PUUncertainty_outfile.open("PUUncertainty_MHT100-200.txt");
   // PUUncertainty_outfile.open("PUUncertainty_MHT200.txt");
    
   // get PU uncertainty
   cout << "x 2 jets: " <<  x_NJet2_data << " +- " << TMath::Sqrt(sigma_x_squared_NJet2) << endl;
   cout << "pred 2: " << pred_NJet2_data << " +- " << TMath::Sqrt(sigma_pred_squared_NJet2)<< endl;
   cout << "x 3-5 jets: " <<  x_NJet3_5_data << " +- " << TMath::Sqrt(sigma_x_squared_NJet3_5)<<  endl;
   cout << "pred 3-5: " << pred_NJet3_5_data << " +- " << TMath::Sqrt(sigma_pred_squared_NJet3_5) << endl;
   cout << "x 6-7 jets: " <<  x_NJet6_7_data << " +- " << TMath::Sqrt(sigma_x_squared_NJet6_7) << endl;
   cout << "pred 6-7: " << pred_NJet6_7_data << " +- " << TMath::Sqrt(sigma_pred_squared_NJet6_7) << endl;
   cout << "x 8 jets: " <<  x_NJet8_data << " +- " << TMath::Sqrt(sigma_x_squared_NJet8) << endl;
   cout << "pred 8: " << pred_NJet8_data << " +- " << TMath::Sqrt(sigma_pred_squared_NJet8) << endl;

   PUUncertainty_outfile << "PU uncertainty NJet = 2: " << x_NJet2_data/pred_NJet2_data << " +- " << TMath::Sqrt(pow(1/pred_NJet2_data, 2) * sigma_x_squared_NJet2 + pow(x_NJet2_data/(pred_NJet2_data*pred_NJet2_data), 2) * sigma_pred_squared_NJet2) << endl;

   PUUncertainty_outfile << "PU uncertainty NJet = 3-5: " << x_NJet3_5_data/pred_NJet3_5_data << " +- " << TMath::Sqrt(pow(1/pred_NJet3_5_data, 2) * sigma_x_squared_NJet3_5 + pow(x_NJet3_5_data/(pred_NJet3_5_data*pred_NJet3_5_data), 2) * sigma_pred_squared_NJet3_5) << endl;

   PUUncertainty_outfile << "PU uncertainty NJet = 6-7: " << x_NJet6_7_data/pred_NJet6_7_data << " +- " << TMath::Sqrt(pow(1/pred_NJet6_7_data, 2) * sigma_x_squared_NJet6_7 + pow(x_NJet6_7_data/(pred_NJet6_7_data*pred_NJet6_7_data), 2) * sigma_pred_squared_NJet6_7) << endl;

   PUUncertainty_outfile << "PU uncertainty NJet >= 8: " << x_NJet8_data/pred_NJet8_data << " +- " << TMath::Sqrt(pow(1/pred_NJet8_data, 2) * sigma_x_squared_NJet8 + pow(x_NJet8_data/(pred_NJet8_data*pred_NJet8_data), 2) * sigma_pred_squared_NJet8) << endl;

   PUUncertainty_outfile.close();

   TFile* PUUncertainty = new TFile("PUUncertainty_DR53X_MHT100_v2.root", "RECREATE");
   // TFile* PUUncertainty = new TFile("PUUncertainty_MHT100-200.root", "RECREATE");
   // TFile* PUUncertainty = new TFile("PUUncertainty_MHT200.root", "RECREATE");
   pile_up_histo_pred_data_Njet2->Write();
   pile_up_histo_pred_data_Njet3_5->Write();
   pile_up_histo_pred_data_Njet6_7->Write();
   pile_up_histo_pred_data_Njet8->Write();
   pile_up_histo_pred_mc_Njet2->Write();
   pile_up_histo_pred_mc_Njet3_5->Write();
   pile_up_histo_pred_mc_Njet6_7->Write();
   pile_up_histo_pred_mc_Njet8->Write();
   pile_up_histo_seed_data_Njet2->Write();
   pile_up_histo_seed_data_Njet3_5->Write();
   pile_up_histo_seed_data_Njet6_7->Write();
   pile_up_histo_seed_data_Njet8->Write();
   pile_up_histo_seed_mc_Njet2->Write();
   pile_up_histo_seed_mc_Njet3_5->Write();
   pile_up_histo_seed_mc_Njet6_7->Write();
   pile_up_histo_seed_mc_Njet8->Write();
   pile_up_histo_data_Njet2->Write();
   pile_up_histo_data_Njet3_5->Write();
   pile_up_histo_data_Njet6_7->Write();
   pile_up_histo_data_Njet8->Write();
   pile_up_histo_mc_Njet2->Write();
   pile_up_histo_mc_Njet3_5->Write();
   pile_up_histo_mc_Njet6_7->Write();
   pile_up_histo_mc_Njet8->Write();
 
   PUUncertainty->Write();
}

////////////////////////////////////////////////////////////////////////////////////////
bool DeltaPhiCut( UShort_t NJets, Float_t DeltaPhi1, Float_t DeltaPhi2, Float_t DeltaPhi3 )
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
TH1F* CalcPrediction(TH2F* prediction_raw) {
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
