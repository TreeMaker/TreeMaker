//
//  BinPrediction.h
//  
//
//  Created by Christian Sander on 15/06/15.
//
//

#ifndef ____BinPrediction__
#define ____BinPrediction__

#include <stdio.h>

#include <TROOT.h>
#include <TTree.h>
#include <TChain.h>

#include <memory>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <iostream>

using namespace std;

class BinPrediction {
   
public:
   BinPrediction(TChain&, TChain&, TString&);
   ~BinPrediction();
   
private:
   // tree with prediction
   TTree* QCDPrediction;
   UShort_t vtxN;
   UShort_t NJets;
   UShort_t BTags;
   UShort_t NSmear;
   Float_t weight;
   Float_t HT;
   Float_t MHT;
   Float_t HT_seed;
   Float_t Jet1Pt;
   Float_t Jet2Pt;
   Float_t Jet3Pt;
   Float_t Jet4Pt;
   Float_t Jet1Eta;
   Float_t Jet2Eta;
   Float_t Jet3Eta;
   Float_t Jet4Eta;
   Float_t DeltaPhi1;
   Float_t DeltaPhi2;
   Float_t DeltaPhi3;
   Float_t minDeltaPhiN;

   // tree with selection
   TTree* RA2PreSelection;
   UShort_t vtxN_RA2;
   UShort_t NLeptons_RA2;
   UShort_t NJets_RA2;
   UShort_t BTags_RA2;
   Int_t EvtNum_RA2;
   Float_t weight_RA2;
   Float_t HT_RA2;
   Float_t MHT_RA2;
   Float_t Jet1Pt_RA2;
   Float_t Jet2Pt_RA2;
   Float_t Jet3Pt_RA2;
   Float_t Jet4Pt_RA2;
   Float_t Jet1Eta_RA2;
   Float_t Jet2Eta_RA2;
   Float_t Jet3Eta_RA2;
   Float_t Jet4Eta_RA2;
   Float_t DeltaPhi1_RA2;
   Float_t DeltaPhi2_RA2;
   Float_t DeltaPhi3_RA2;
   Float_t minDeltaPhiN_RA2;
   
   // store deltaPhi cut
   vector<bool> MinDeltaPhiCut;
   
   bool DeltaPhiCut_selection();
   bool DeltaPhiCut_prediction();
};

#endif /* defined(____BinPrediction__) */

