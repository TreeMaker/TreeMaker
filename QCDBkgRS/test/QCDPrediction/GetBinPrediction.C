//
//  GetBinPrediction.c
//  
//
//  Created by Christian Sander on 15/06/15.
//
//

#include <TROOT.h>
#include <TSystem.h>
#include <TFile.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "BinPrediction.h"

using namespace std;

int main()
{
   
   string root_file;
   TChain* prediction = new TChain("QCDfromSmearing/QCDPrediction");
   TChain* prediction_CoreUP = new TChain("QCDfromSmearingCoreUP/QCDPrediction");
   //TChain* prediction_CoreDN = new TChain("QCDfromSmearingCoreDN/QCDPrediction");
   TChain* prediction_TailUP = new TChain("QCDfromSmearingTailUP/QCDPrediction");
   //TChain* prediction_TailDN = new TChain("QCDfromSmearingTailDN/QCDPrediction");
   TChain* selection = new TChain("RA2TreeMaker/PreSelection");
   
   // open files for MC --- madgraph QCD ---- //
   //ifstream myfile1 ("filelists_phys14/filelist_madgraph.txt");
   //ifstream myfile1 ("filelists_phys14/filelist_pythia.txt");
   ifstream myfile1 ("filelists_phys14/filelist_pythia_large.txt");
   //ifstream myfile1 ("filelists_phys14/test.txt");
   if (myfile1.is_open()) {
      while( myfile1.good() ) {
         getline (myfile1,root_file);
         cout << root_file << endl;
         
         TString path = root_file;
         prediction->Add(path);
         prediction_CoreUP->Add(path);
         //prediction_CoreDN->Add(path);
         prediction_TailUP->Add(path);
         //prediction_TailDN->Add(path);
         selection->Add(path);
         
      }
      myfile1.close();
   }
   
   // ------------------------------------------------------------------- //
   
   // initialize new Prediction object
  
   TString uncertainty;
   uncertainty = "_nominal";
   BinPrediction* pred_ = new BinPrediction(*prediction, *selection, uncertainty);
   uncertainty = "_CoreUP";
   BinPrediction* pred_CoreUP_ = new BinPrediction(*prediction_CoreUP, *selection, uncertainty);
   //uncertainty = "_CoreDN";
   //BinPrediction* pred_CoreDN_ = new BinPrediction(*prediction_CoreDN, *selection, uncertainty);
   uncertainty = "_TailUP";
   BinPrediction* pred_TailUP_ = new BinPrediction(*prediction_TailUP, *selection, uncertainty);
   //uncertainty = "_TailDN";
   //BinPrediction* pred_TailDN_ = new BinPrediction(*prediction_TailDN, *selection, uncertainty);
   
   return 1;
}
