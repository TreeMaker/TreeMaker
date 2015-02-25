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
#include <TArrayF.h>
#include <TLine.h>
#include <TPaveText.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

//#include "/afs/naf.desy.de/user/k/kriheine/macros/PlottingUtils.C"

using namespace std;

void GetRebalanceCorrectionFactor()
{
   gROOT->ProcessLine(".L PlottingUtils.C+");

   PlottingUtils::SetPlotStyle();

   // --- define output file for ps ---//
   TString pt = "pt10";
   double x_min = 10.;

   TString outfile = "RebalanceCorrectionFactor/RebalanceCorrectionFactors_DR53X_chsJets_TuneZ2star_withoutPUReweighting_" + pt;

   TH2F* RebCorrection_vsReco = new TH2F("RebCorrection_vsReco", "Jet pt", 1000, 0., 1000., 100, 0., 3.);
   TH2F* RebCorrection_vsReco_madgraph = new TH2F("RebCorrection_vsReco_madgraph", "Jet pt", 1000, 0., 1000., 100, 0., 3.);
   TH2F* RebCorrection_vsReco_NVtx0_10 = new TH2F("RebCorrection_vsReco_NVtx0_10", "Jet pt", 1000, 0., 1000., 100, 0., 3.);
   TH2F* RebCorrection_vsReco_NVtx11_20 = new TH2F("RebCorrection_vsReco_NVtx11_20", "Jet pt", 1000, 0., 1000., 100, 0., 3.);
   TH2F* RebCorrection_vsReco_NVtx21_Inf = new TH2F("RebCorrection_vsReco_NVtx21_Inf", "Jet pt", 1000, 0., 1000., 100, 0., 3.);
   
   string root_file;

   // pythia
   ifstream myfile ("filelists_53X/filelist_pythia_DR53X_chs_TuneZ2star_" + pt + "_withoutPUReweighting_RebControlPlots_v1_mc.txt");
   if (myfile.is_open()) {
      while( myfile.good() ) {
         getline (myfile,root_file);
         cout << root_file << endl;
                     
         TH2F* RebCorrection_vsReco_temp; 
               
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_temp);
         RebCorrection_vsReco->Add(RebCorrection_vsReco_temp);

         input_file->Close();
         
      }
      myfile.close();
   }

   // madgraph 1 HT=100-250
   ifstream myfile2 ("filelists_53X/filelist_madgraph_DR53X_chs_" + pt + "_withoutPUReweighting_HT100-250_RebControlPlots_v1_mc.txt");
   if (myfile2.is_open()) {
      while( myfile2.good() ) {
         getline (myfile2,root_file);
         cout << root_file << endl;
               
         TH2F* RebCorrection_vsReco_madgraph_temp; 
                
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_madgraph_temp);
         RebCorrection_vsReco_madgraph->Add(RebCorrection_vsReco_madgraph_temp);

         input_file->Close();
         
      }
      myfile2.close();
   }

   // madgraph 2 HT=250-500
   ifstream myfile3 ("filelists_53X/filelist_madgraph_DR53X_chs_" + pt + "_withoutPUReweighting_HT250-500_RebControlPlots_v1_mc.txt");
   if (myfile3.is_open()) {
      while( myfile3.good() ) {
         getline (myfile3,root_file);
         cout << root_file << endl;
               
         TH2F* RebCorrection_vsReco_madgraph_temp; 
                
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_madgraph_temp);
         RebCorrection_vsReco_madgraph->Add(RebCorrection_vsReco_madgraph_temp);

         input_file->Close();
         
      }
      myfile3.close();
   }

   // madgraph 3 HT=500-1000
   ifstream myfile4 ("filelists_53X/filelist_madgraph_DR53X_chs_" + pt + "_withoutPUReweighting_HT500-1000_RebControlPlots_v1_mc.txt");
   if (myfile4.is_open()) {
      while( myfile4.good() ) {
         getline (myfile4,root_file);
         cout << root_file << endl;
               
         TH2F* RebCorrection_vsReco_madgraph_temp; 
                
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_madgraph_temp);
         RebCorrection_vsReco_madgraph->Add(RebCorrection_vsReco_madgraph_temp);

         input_file->Close();
         
      }
      myfile4.close();
   }

   // madgraph 4 HT=1000-Inf
   ifstream myfile5 ("filelists_53X/filelist_madgraph_DR53X_chs_" + pt + "_withoutPUReweighting_HT1000-Inf_RebControlPlots_v1_mc.txt");
   if (myfile5.is_open()) {
      while( myfile5.good() ) {
         getline (myfile5,root_file);
         cout << root_file << endl;
               
         TH2F* RebCorrection_vsReco_madgraph_temp; 
                
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_madgraph_temp);
         RebCorrection_vsReco_madgraph->Add(RebCorrection_vsReco_madgraph_temp);

         input_file->Close();
         
      }
      myfile5.close();
   }

   // pythia - nVtx 0-10
   ifstream myfile6 ("filelists_53X/filelist_pythia_DR53X_chs_TuneZ2star_" + pt + "_withoutPUReweighting_RebControlPlots_NVtx0-10_v1_mc.txt");
   if (myfile6.is_open()) {
      while( myfile6.good() ) {
         getline (myfile6,root_file);
         cout << root_file << endl;
                     
         TH2F* RebCorrection_vsReco_NVtx0_10_temp; 
               
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_NVtx0_10_temp);
         RebCorrection_vsReco_NVtx0_10->Add(RebCorrection_vsReco_NVtx0_10_temp);

         input_file->Close();
         
      }
      myfile6.close();
   }

   // pythia - nVtx 11-20
   ifstream myfile7 ("filelists_53X/filelist_pythia_DR53X_chs_TuneZ2star_" + pt + "_withoutPUReweighting_RebControlPlots_NVtx11-20_v1_mc.txt");
   if (myfile7.is_open()) {
      while( myfile7.good() ) {
         getline (myfile7,root_file);
         cout << root_file << endl;
                     
         TH2F* RebCorrection_vsReco_NVtx11_20_temp; 
               
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_NVtx11_20_temp);
         RebCorrection_vsReco_NVtx11_20->Add(RebCorrection_vsReco_NVtx11_20_temp);

         input_file->Close();
         
      }
      myfile7.close();
   }

   // pythia - nVtx 21-Inf
   ifstream myfile8 ("filelists_53X/filelist_pythia_DR53X_chs_TuneZ2star_" + pt + "_withoutPUReweighting_RebControlPlots_NVtx21-Inf_v1_mc.txt");
   if (myfile8.is_open()) {
      while( myfile8.good() ) {
         getline (myfile8,root_file);
         cout << root_file << endl;
                     
         TH2F* RebCorrection_vsReco_NVtx21_Inf_temp; 
               
         TString path = root_file;

         TFile* input_file = TFile::Open(path, "READ");
         input_file->cd("QCDfromSmearing");

         gDirectory->GetObject("RebCorrection_vsReco;1", RebCorrection_vsReco_NVtx21_Inf_temp);
         RebCorrection_vsReco_NVtx21_Inf->Add(RebCorrection_vsReco_NVtx21_Inf_temp);

         input_file->Close();
         
      }
      myfile8.close();
   }

//    RebCorrection_vsReco_NVtx0_10->Rebin2D(2, 1);
//    RebCorrection_vsReco_NVtx11_20->Rebin2D(2, 1);
//    RebCorrection_vsReco_NVtx21_Inf->Rebin2D(2, 1);

   // ---------------------------------------------------- //
   // pythia
   TH1F* correction_vsReco = new TH1F();
   correction_vsReco = (TH1F*) RebCorrection_vsReco->ProjectionX();
   correction_vsReco->Reset();
   for (int i = 0; i <= RebCorrection_vsReco->GetXaxis()->GetNbins(); ++i) {
      TH1F h = *((TH1F*) RebCorrection_vsReco->ProjectionY("py", i, i));
            
      double mean = h.GetMean();
      double error = h.GetMeanError();

      cout << "i: " << i << " " << "mean: " << mean << " " << "error: " << error << endl;
            
      correction_vsReco->SetBinContent(i, mean);
      correction_vsReco->SetBinError(i, error);
   }

   // madgraph
   TH1F* correction_vsReco_madgraph = new TH1F();
   correction_vsReco_madgraph = (TH1F*) RebCorrection_vsReco_madgraph->ProjectionX();
   correction_vsReco_madgraph->Reset();
   for (int i = 0; i <= RebCorrection_vsReco_madgraph->GetXaxis()->GetNbins(); ++i) {
      TH1F h = *((TH1F*) RebCorrection_vsReco_madgraph->ProjectionY("py", i, i));
            
      double mean = h.GetMean();
      double error = h.GetMeanError();

      cout << "i: " << i << " " << "mean: " << mean << " " << "error: " << error << endl;
            
      correction_vsReco_madgraph->SetBinContent(i, mean);
      correction_vsReco_madgraph->SetBinError(i, error);
   }

   // pythia NVtx 0-10
   TH1F* correction_vsReco_NVtx0_10 = new TH1F();
   correction_vsReco_NVtx0_10 = (TH1F*) RebCorrection_vsReco_NVtx0_10->ProjectionX();
   correction_vsReco_NVtx0_10->Reset();
   for (int i = 0; i <= RebCorrection_vsReco_NVtx0_10->GetXaxis()->GetNbins(); ++i) {
      TH1F h = *((TH1F*) RebCorrection_vsReco_NVtx0_10->ProjectionY("py", i, i));
            
      double mean = h.GetMean();
      double error = h.GetMeanError();

      cout << "i: " << i << " " << "mean: " << mean << " " << "error: " << error << endl;
            
      correction_vsReco_NVtx0_10->SetBinContent(i, mean);
      correction_vsReco_NVtx0_10->SetBinError(i, error);
   }

   // pythia NVtx 11-20
   TH1F* correction_vsReco_NVtx11_20 = new TH1F();
   correction_vsReco_NVtx11_20 = (TH1F*) RebCorrection_vsReco_NVtx11_20->ProjectionX();
   correction_vsReco_NVtx11_20->Reset();
   for (int i = 0; i <= RebCorrection_vsReco_NVtx11_20->GetXaxis()->GetNbins(); ++i) {
      TH1F h = *((TH1F*) RebCorrection_vsReco_NVtx11_20->ProjectionY("py", i, i));
            
      double mean = h.GetMean();
      double error = h.GetMeanError();

      cout << "i: " << i << " " << "mean: " << mean << " " << "error: " << error << endl;
            
      correction_vsReco_NVtx11_20->SetBinContent(i, mean);
      correction_vsReco_NVtx11_20->SetBinError(i, error);
   }

   // pythia NVtx 21-Inf
   TH1F* correction_vsReco_NVtx21_Inf = new TH1F();
   correction_vsReco_NVtx21_Inf = (TH1F*) RebCorrection_vsReco_NVtx21_Inf->ProjectionX();
   correction_vsReco_NVtx21_Inf->Reset();
   for (int i = 0; i <= RebCorrection_vsReco_NVtx21_Inf->GetXaxis()->GetNbins(); ++i) {
      TH1F h = *((TH1F*) RebCorrection_vsReco_NVtx21_Inf->ProjectionY("py", i, i));
            
      double mean = h.GetMean();
      double error = h.GetMeanError();

      cout << "i: " << i << " " << "mean: " << mean << " " << "error: " << error << endl;
            
      correction_vsReco_NVtx21_Inf->SetBinContent(i, mean);
      correction_vsReco_NVtx21_Inf->SetBinError(i, error);
   }

   // ---------------------------------------------------- //

   TCanvas *c = new TCanvas("c", "", PlottingUtils::CanvasPlot[2], PlottingUtils::CanvasPlot[3]);
   correction_vsReco->SetAxisRange(x_min, correction_vsReco->GetXaxis()->GetXmax());
   correction_vsReco->SetXTitle("reco jet p_{T} [GeV]");
   correction_vsReco->SetYTitle("reb jet p_{T} / gen jet p_{T} ");
   correction_vsReco->Draw();

   TPaveText* pt1 =  PlottingUtils::CMSLabelMC("19.47");
   pt1->Draw();

   c->Print(outfile + "_vsReco.ps");  
   c->Print(outfile + "_vsReco.png"); 

   // ---------------------------------------------------- //

   correction_vsReco_madgraph->SetAxisRange(x_min, correction_vsReco_madgraph->GetXaxis()->GetXmax());
   correction_vsReco_madgraph->SetXTitle("reco jet p_{T} [GeV]");
   correction_vsReco_madgraph->SetYTitle("reb jet p_{T} / gen jet p_{T} ");
   correction_vsReco_madgraph->Draw();

   pt1->Draw();

   c->Print(outfile + "_vsRecoMadgraph.ps");  
   c->Print(outfile + "_vsRecoMadgraph.png"); 

   // ---------------------------------------------------- //

   // ---------------------------------------------------- //

   correction_vsReco_NVtx0_10->SetAxisRange(x_min, correction_vsReco_madgraph->GetXaxis()->GetXmax());
   correction_vsReco_NVtx0_10->SetXTitle("reco jet p_{T} [GeV]");
   correction_vsReco_NVtx0_10->SetYTitle("reb jet p_{T} / gen jet p_{T} ");
   correction_vsReco_NVtx0_10->Draw();
   correction_vsReco_NVtx11_20->SetMarkerStyle(PlottingUtils::c_MarkerStyle[1]);
   correction_vsReco_NVtx11_20->SetLineColor(PlottingUtils::c_LineColor[1]);
   correction_vsReco_NVtx11_20->SetMarkerColor(PlottingUtils::c_MarkerColor[1]);
   correction_vsReco_NVtx11_20->Draw("same");
   correction_vsReco_NVtx21_Inf->SetMarkerStyle(PlottingUtils::c_MarkerStyle[2]);
   correction_vsReco_NVtx21_Inf->SetLineColor(PlottingUtils::c_LineColor[2]);
   correction_vsReco_NVtx21_Inf->SetMarkerColor(PlottingUtils::c_MarkerColor[2]);
   correction_vsReco_NVtx21_Inf->Draw("same");

   TLegend* leg = PlottingUtils::Legend3Entries(correction_vsReco_NVtx0_10, correction_vsReco_NVtx11_20,
                                                correction_vsReco_NVtx21_Inf,
                                                " 0 - 10 Vertices", " 11 - 20 Vertices", " > 20 Vertices");
   leg->Draw("same");

   pt1->Draw();

   c->Print(outfile + "_vsRecoNVtxSplit.ps");  
   c->Print(outfile + "_vsRecoNVtxSplit.png"); 

   // ---------------------------------------------------- //

   c = PlottingUtils::Draw2CurvesWithRatio(correction_vsReco, correction_vsReco_madgraph, 
                                           "reco jet p_{T} [GeV]", "f = reb jet p_{T} / gen jet p_{T} ", 
                                           "", "CMS Simulation,  L = 19.47 fb^{  -1}, #sqrt{s} = 8 TeV", "QCD pythia",
                                           "QCD madgraph", "#Delta f");

   c->Print(outfile + "_vsRecoWithMadgraphComp.ps");  
   c->Print(outfile + "_vsRecoWithMadgraphComp.png"); 

   // ---------------------------------------------------- //

   TFile* RebalanceCorrection = new TFile("RebalanceCorrectionFactor/RebalanceCorrection_DR53X_withoutPUReweighting_" + pt + ".root", "RECREATE");
   correction_vsReco->Write();
   correction_vsReco_madgraph->Write();

   RebalanceCorrection->Write();
}


