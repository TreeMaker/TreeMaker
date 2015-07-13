//
//  BinPrediction.c
//
//
//  Created by Christian Sander on 15/06/15.
//
//

#include "BinPrediction.h"
#include "RA2bBin.h"

#include <TROOT.h>
#include <TSystem.h>
#include <TMath.h>
#include <TString.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

BinPrediction::BinPrediction(TChain& QCDPrediction, TChain& RA2PreSelection, TString& Uncertainty)
{
   gROOT->ProcessLine("#include <vector>");
   
   // ------------- define all histos needed -------//
   // set histogram attributes
   int Ntries = 100;
   
   //Define search bins
   //￼Njets bins: 4-6, 7-8, 9+
   //Nb bins: 0, 1, 2, 3+
   //MHT,HT = 200,500,500,800
   //MHT,HT = 200,500,800,1200
   //MHT,HT = 200,500,1200+
   //MHT,HT = 500,750,500,1200
   //MHT,HT = 500,750,1200+
   //MHT,HT = 750+,800+
   
   std::vector<RA2bBin*> SB;
   
   RA2bBin SB1("Njet456-Nb0-MHT1-HT1", Ntries, 4, 6, 0, 0, 200., 500., 500., 800., true);
   RA2bBin SB2("Njet456-Nb0-MHT1-HT2", Ntries, 4, 6, 0, 0, 200., 500., 800., 1200., true);
   RA2bBin SB3("Njet456-Nb0-MHT1-HT3", Ntries, 4, 6, 0, 0, 200., 500., 1200., 9999., true);
   RA2bBin SB4("Njet456-Nb0-MHT2-HT1", Ntries, 4, 6, 0, 0, 500., 750., 500., 1200., true);
   RA2bBin SB5("Njet456-Nb0-MHT2-HT23", Ntries, 4, 6, 0, 0, 500., 750., 1200., 9999., true);
   RA2bBin SB6("Njet456-Nb0-MHT2-HT123", Ntries, 4, 6, 0, 0, 750., 9999., 800., 9999., true);
   
   RA2bBin SB7("Njet456-Nb1-MHT1-HT1", Ntries, 4, 6, 1, 1, 200., 500., 500., 800., true);
   RA2bBin SB8("Njet456-Nb1-MHT1-HT2", Ntries, 4, 6, 1, 1, 200., 500., 800., 1200., true);
   RA2bBin SB9("Njet456-Nb1-MHT1-HT3", Ntries, 4, 6, 1, 1, 200., 500., 1200., 9999., true);
   RA2bBin SB10("Njet456-Nb1-MHT2-HT1", Ntries, 4, 6, 1, 1, 500., 750., 500., 1200., true);
   RA2bBin SB11("Njet456-Nb1-MHT2-HT23", Ntries, 4, 6, 1, 1, 500., 750., 1200., 9999., true);
   RA2bBin SB12("Njet456-Nb1-MHT2-HT123", Ntries, 4, 6, 1, 1, 750., 9999., 800., 9999., true);
   
   RA2bBin SB13("Njet456-Nb2-MHT1-HT1", Ntries, 4, 6, 2, 2, 200., 500., 500., 800., true);
   RA2bBin SB14("Njet456-Nb2-MHT1-HT2", Ntries, 4, 6, 2, 2, 200., 500., 800., 1200., true);
   RA2bBin SB15("Njet456-Nb2-MHT1-HT3", Ntries, 4, 6, 2, 2, 200., 500., 1200., 9999., true);
   RA2bBin SB16("Njet456-Nb2-MHT2-HT1", Ntries, 4, 6, 2, 2, 500., 750., 500., 1200., true);
   RA2bBin SB17("Njet456-Nb2-MHT2-HT23", Ntries, 4, 6, 2, 2, 500., 750., 1200., 9999., true);
   RA2bBin SB18("Njet456-Nb2-MHT2-HT123", Ntries, 4, 6, 2, 2, 750., 9999., 800., 9999., true);
   
   RA2bBin SB19("Njet456-Nb3+-MHT1-HT1", Ntries, 4, 6, 3, 9, 200., 500., 500., 800., true);
   RA2bBin SB20("Njet456-Nb3+-MHT1-HT2", Ntries, 4, 6, 3, 9, 200., 500., 800., 1200., true);
   RA2bBin SB21("Njet456-Nb3+-MHT1-HT3", Ntries, 4, 6, 3, 9, 200., 500., 1200., 9999., true);
   RA2bBin SB22("Njet456-Nb3+-MHT2-HT1", Ntries, 4, 6, 3, 9, 500., 750., 500., 1200., true);
   RA2bBin SB23("Njet456-Nb3+-MHT2-HT23", Ntries, 4, 6, 3, 9, 500., 750., 1200., 9999., true);
   RA2bBin SB24("Njet456-Nb3+-MHT2-HT123", Ntries, 4, 6, 3, 9, 750., 9999., 800., 9999., true);
   
   RA2bBin SB25("Njet78-Nb0-MHT1-HT1", Ntries, 7, 8, 0, 0, 200., 500., 500., 800., true);
   RA2bBin SB26("Njet78-Nb0-MHT1-HT2", Ntries, 7, 8, 0, 0, 200., 500., 800., 1200., true);
   RA2bBin SB27("Njet78-Nb0-MHT1-HT3", Ntries, 7, 8, 0, 0, 200., 500., 1200., 9999., true);
   RA2bBin SB28("Njet78-Nb0-MHT2-HT1", Ntries, 7, 8, 0, 0, 500., 750., 500., 1200., true);
   RA2bBin SB29("Njet78-Nb0-MHT2-HT23", Ntries, 7, 8, 0, 0, 500., 750., 1200., 9999., true);
   RA2bBin SB30("Njet78-Nb0-MHT2-HT123", Ntries, 7, 8, 0, 0, 750., 9999., 800., 9999., true);
   
   RA2bBin SB31("Njet78-Nb1-MHT1-HT1", Ntries, 7, 8, 1, 1, 200., 500., 500., 800., true);
   RA2bBin SB32("Njet78-Nb1-MHT1-HT2", Ntries, 7, 8, 1, 1, 200., 500., 800., 1200., true);
   RA2bBin SB33("Njet78-Nb1-MHT1-HT3", Ntries, 7, 8, 1, 1, 200., 500., 1200., 9999., true);
   RA2bBin SB34("Njet78-Nb1-MHT2-HT1", Ntries, 7, 8, 1, 1, 500., 750., 500., 1200., true);
   RA2bBin SB35("Njet78-Nb1-MHT2-HT23", Ntries, 7, 8, 1, 1, 500., 750., 1200., 9999., true);
   RA2bBin SB36("Njet78-Nb1-MHT2-HT123", Ntries, 7, 8, 1, 1, 750., 9999., 800., 9999., true);
   
   RA2bBin SB37("Njet78-Nb2-MHT1-HT1", Ntries, 7, 8, 2, 2, 200., 500., 500., 800., true);
   RA2bBin SB38("Njet78-Nb2-MHT1-HT2", Ntries, 7, 8, 2, 2, 200., 500., 800., 1200., true);
   RA2bBin SB39("Njet78-Nb2-MHT1-HT3", Ntries, 7, 8, 2, 2, 200., 500., 1200., 9999., true);
   RA2bBin SB40("Njet78-Nb2-MHT2-HT1", Ntries, 7, 8, 2, 2, 500., 750., 500., 1200., true);
   RA2bBin SB41("Njet78-Nb2-MHT2-HT23", Ntries, 7, 8, 2, 2, 500., 750., 1200., 9999., true);
   RA2bBin SB42("Njet78-Nb2-MHT2-HT123", Ntries, 7, 8, 2, 2, 750., 9999., 800., 9999., true);
   
   RA2bBin SB43("Njet78-Nb3+-MHT1-HT1", Ntries, 7, 8, 3, 9, 200., 500., 500., 800., true);
   RA2bBin SB44("Njet78-Nb3+-MHT1-HT2", Ntries, 7, 8, 3, 9, 200., 500., 800., 1200., true);
   RA2bBin SB45("Njet78-Nb3+-MHT1-HT3", Ntries, 7, 8, 3, 9, 200., 500., 1200., 9999., true);
   RA2bBin SB46("Njet78-Nb3+-MHT2-HT1", Ntries, 7, 8, 3, 9, 500., 750., 500., 1200., true);
   RA2bBin SB47("Njet78-Nb3+-MHT2-HT23", Ntries, 7, 8, 3, 9, 500., 750., 1200., 9999., true);
   RA2bBin SB48("Njet78-Nb3+-MHT2-HT123", Ntries, 7, 8, 3, 9, 750., 9999., 800., 9999., true);
   
   RA2bBin SB49("Njet9+-Nb0-MHT1-HT1", Ntries, 9, 99, 0, 0, 200., 500., 500., 800., true);
   RA2bBin SB50("Njet9+-Nb0-MHT1-HT2", Ntries, 9, 99, 0, 0, 200., 500., 800., 1200., true);
   RA2bBin SB51("Njet9+-Nb0-MHT1-HT3", Ntries, 9, 99, 0, 0, 200., 500., 1200., 9999., true);
   RA2bBin SB52("Njet9+-Nb0-MHT2-HT1", Ntries, 9, 99, 0, 0, 500., 750., 500., 1200., true);
   RA2bBin SB53("Njet9+-Nb0-MHT2-HT23", Ntries, 9, 99, 0, 0, 500., 750., 1200., 9999., true);
   RA2bBin SB54("Njet9+-Nb0-MHT2-HT123", Ntries, 9, 99, 0, 0, 750., 9999., 800., 9999., true);
   
   RA2bBin SB55("Njet9+-Nb1-MHT1-HT1", Ntries, 9, 99, 1, 1, 200., 500., 500., 800., true);
   RA2bBin SB56("Njet9+-Nb1-MHT1-HT2", Ntries, 9, 99, 1, 1, 200., 500., 800., 1200., true);
   RA2bBin SB57("Njet9+-Nb1-MHT1-HT3", Ntries, 9, 99, 1, 1, 200., 500., 1200., 9999., true);
   RA2bBin SB58("Njet9+-Nb1-MHT2-HT1", Ntries, 9, 99, 1, 1, 500., 750., 500., 1200., true);
   RA2bBin SB59("Njet9+-Nb1-MHT2-HT23", Ntries, 9, 99, 1, 1, 500., 750., 1200., 9999., true);
   RA2bBin SB60("Njet9+-Nb1-MHT2-HT123", Ntries, 9, 99, 1, 1, 750., 9999., 800., 9999., true);
   
   RA2bBin SB61("Njet9+-Nb2-MHT1-HT1", Ntries, 9, 99, 2, 2, 200., 500., 500., 800., true);
   RA2bBin SB62("Njet9+-Nb2-MHT1-HT2", Ntries, 9, 99, 2, 2, 200., 500., 800., 1200., true);
   RA2bBin SB63("Njet9+-Nb2-MHT1-HT3", Ntries, 9, 99, 2, 2, 200., 500., 1200., 9999., true);
   RA2bBin SB64("Njet9+-Nb2-MHT2-HT1", Ntries, 9, 99, 2, 2, 500., 750., 500., 1200., true);
   RA2bBin SB65("Njet9+-Nb2-MHT2-HT23", Ntries, 9, 99, 2, 2, 500., 750., 1200., 9999., true);
   RA2bBin SB66("Njet9+-Nb2-MHT2-HT123", Ntries, 9, 99, 2, 2, 750., 9999., 800., 9999., true);
   
   RA2bBin SB67("Njet9+-Nb3+-MHT1-HT1", Ntries, 9, 99, 3, 9, 200., 500., 500., 800., true);
   RA2bBin SB68("Njet9+-Nb3+-MHT1-HT2", Ntries, 9, 99, 3, 9, 200., 500., 800., 1200., true);
   RA2bBin SB69("Njet9+-Nb3+-MHT1-HT3", Ntries, 9, 99, 3, 9, 200., 500., 1200., 9999., true);
   RA2bBin SB70("Njet9+-Nb3+-MHT2-HT1", Ntries, 9, 99, 3, 9, 500., 750., 500., 1200., true);
   RA2bBin SB71("Njet9+-Nb3+-MHT2-HT23", Ntries, 9, 99, 3, 9, 500., 750., 1200., 9999., true);
   RA2bBin SB72("Njet9+-Nb3+-MHT2-HT123", Ntries, 9, 99, 3, 9, 750., 9999., 800., 9999., true);
   
   RA2bBin SB1a("Njet456-MHT1-HT1", Ntries, 4, 6, 0, 99, 200., 500., 500., 800., true);
   RA2bBin SB2a("Njet456-MHT1-HT2", Ntries, 4, 6, 0, 99, 200., 500., 800., 1200., true);
   RA2bBin SB3a("Njet456-MHT1-HT3", Ntries, 4, 6, 0, 99, 200., 500., 1200., 9999., true);
   RA2bBin SB4a("Njet456-MHT2-HT1", Ntries, 4, 6, 0, 99, 500., 750., 500., 1200., true);
   RA2bBin SB5a("Njet456-MHT2-HT23", Ntries, 4, 6, 0, 99, 500., 750., 1200., 9999., true);
   RA2bBin SB6a("Njet456-MHT2-HT123", Ntries, 4, 6, 0, 99, 750., 9999., 800., 9999., true);
   
   RA2bBin SB7a("Njet78-MHT1-HT1", Ntries, 7, 8, 0, 99, 200., 500., 500., 800., true);
   RA2bBin SB8a("Njet78-MHT1-HT2", Ntries, 7, 8, 0, 99, 200., 500., 800., 1200., true);
   RA2bBin SB9a("Njet78-MHT1-HT3", Ntries, 7, 8, 0, 99, 200., 500., 1200., 9999., true);
   RA2bBin SB10a("Njet78-MHT2-HT1", Ntries, 7, 8, 0, 99, 500., 750., 500., 1200., true);
   RA2bBin SB11a("Njet78-MHT2-HT23", Ntries, 7, 8, 0, 99, 500., 750., 1200., 9999., true);
   RA2bBin SB12a("Njet78-MHT2-HT123", Ntries, 7, 8, 0, 99, 750., 9999., 800., 9999., true);
   
   RA2bBin SB13a("Njet9+-MHT1-HT1", Ntries, 9, 99, 0, 99, 200., 500., 500., 800., true);
   RA2bBin SB14a("Njet9+-MHT1-HT2", Ntries, 9, 99, 0, 99, 200., 500., 800., 1200., true);
   RA2bBin SB15a("Njet9+-MHT1-HT3", Ntries, 9, 99, 0, 99, 200., 500., 1200., 9999., true);
   RA2bBin SB16a("Njet9+-MHT2-HT1", Ntries, 9, 99, 0, 99, 500., 750., 500., 1200., true);
   RA2bBin SB17a("Njet9+-MHT2-HT23", Ntries, 9, 99, 0, 99, 500., 750., 1200., 9999., true);
   RA2bBin SB18a("Njet9+-MHT2-HT123", Ntries, 9, 99, 0, 99, 750., 9999., 800., 9999., true);
   
   
   SB.push_back(&SB1);
   SB.push_back(&SB2);
   SB.push_back(&SB3);
   SB.push_back(&SB4);
   SB.push_back(&SB5);
   SB.push_back(&SB6);
   SB.push_back(&SB7);
   SB.push_back(&SB8);
   SB.push_back(&SB9);
   SB.push_back(&SB10);
   SB.push_back(&SB11);
   SB.push_back(&SB12);
   SB.push_back(&SB13);
   SB.push_back(&SB14);
   SB.push_back(&SB15);
   SB.push_back(&SB16);
   SB.push_back(&SB17);
   SB.push_back(&SB18);
   SB.push_back(&SB19);
   SB.push_back(&SB20);
   SB.push_back(&SB21);
   SB.push_back(&SB22);
   SB.push_back(&SB23);
   SB.push_back(&SB24);
   SB.push_back(&SB25);
   SB.push_back(&SB26);
   SB.push_back(&SB27);
   SB.push_back(&SB28);
   SB.push_back(&SB29);
   SB.push_back(&SB30);
   SB.push_back(&SB31);
   SB.push_back(&SB32);
   SB.push_back(&SB33);
   SB.push_back(&SB34);
   SB.push_back(&SB35);
   SB.push_back(&SB36);
   SB.push_back(&SB37);
   SB.push_back(&SB38);
   SB.push_back(&SB39);
   SB.push_back(&SB40);
   SB.push_back(&SB41);
   SB.push_back(&SB42);
   SB.push_back(&SB43);
   SB.push_back(&SB44);
   SB.push_back(&SB45);
   SB.push_back(&SB46);
   SB.push_back(&SB47);
   SB.push_back(&SB48);
   SB.push_back(&SB49);
   SB.push_back(&SB50);
   SB.push_back(&SB51);
   SB.push_back(&SB52);
   SB.push_back(&SB53);
   SB.push_back(&SB54);
   SB.push_back(&SB55);
   SB.push_back(&SB56);
   SB.push_back(&SB57);
   SB.push_back(&SB58);
   SB.push_back(&SB59);
   SB.push_back(&SB60);
   SB.push_back(&SB61);
   SB.push_back(&SB62);
   SB.push_back(&SB63);
   SB.push_back(&SB64);
   SB.push_back(&SB65);
   SB.push_back(&SB66);
   SB.push_back(&SB67);
   SB.push_back(&SB68);
   SB.push_back(&SB69);
   SB.push_back(&SB70);
   SB.push_back(&SB71);
   SB.push_back(&SB72);
   
   SB.push_back(&SB1a);
   SB.push_back(&SB2a);
   SB.push_back(&SB3a);
   SB.push_back(&SB4a);
   SB.push_back(&SB5a);
   SB.push_back(&SB6a);
   SB.push_back(&SB7a);
   SB.push_back(&SB8a);
   SB.push_back(&SB9a);
   SB.push_back(&SB10a);
   SB.push_back(&SB11a);
   SB.push_back(&SB12a);
   SB.push_back(&SB13a);
   SB.push_back(&SB14a);
   SB.push_back(&SB15a);
   SB.push_back(&SB16a);
   SB.push_back(&SB17a);
   SB.push_back(&SB18a);

   
   // ------------------------------------------------------------------------------ //
   
   // get tree with predictions
   cout << "entries prediction tree:" << QCDPrediction.GetEntries() << endl;
   
   // variables from prediction tree
   vtxN = 0;
   NJets = 0;
   BTags = 0;
   NSmear = 0;
   weight = 0;
   HT = 0;
   MHT = 0;
   HT_seed = 0;
   Jet1Pt = 0;
   Jet2Pt = 0;
   Jet3Pt = 0;
   Jet4Pt = 0;
   Jet1Eta = 0;
   Jet2Eta = 0;
   Jet3Eta = 0;
   Jet4Eta = 0;
   DeltaPhi1 = 0;
   DeltaPhi2 = 0;
   DeltaPhi3 = 0;
   minDeltaPhiN = 0;
   
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
   QCDPrediction.SetBranchAddress("Jet4Pt",&Jet4Pt);
   QCDPrediction.SetBranchAddress("Jet1Eta",&Jet1Eta);
   QCDPrediction.SetBranchAddress("Jet2Eta",&Jet2Eta);
   QCDPrediction.SetBranchAddress("Jet3Eta",&Jet3Eta);
   QCDPrediction.SetBranchAddress("Jet4Eta",&Jet4Eta);
   QCDPrediction.SetBranchAddress("DeltaPhi1",&DeltaPhi1);
   QCDPrediction.SetBranchAddress("DeltaPhi2",&DeltaPhi2);
   QCDPrediction.SetBranchAddress("DeltaPhi3",&DeltaPhi3);
   QCDPrediction.SetBranchAddress("minDeltaPhiN",&minDeltaPhiN);
   
   cout << "After: SetBranchAddress (prediction)" << endl;
   
   int Prediction_entries = 0;
   float smear_rep = 0;
   
   // loop over entries and fill prediction histos
   ULong_t nentries = QCDPrediction.GetEntries();
   
   for ( ULong_t i = 0 ; i<nentries ; i++) {
      
      QCDPrediction.GetEntry(i);
      
      if( i%1000000 == 0 ) std::cout << "event (prediction): " << i << '\n';
      
      bool mdp = DeltaPhiCut_prediction();

      if( HT > 500. && MHT > 200. && NJets >= 4 && vtxN >= 0 && mdp) {
         
         for (int it = 0; it < SB.size(); ++it){
            if (SB.at(it)->FillPred((int)(NSmear-1), (int)NJets, (int)BTags, (double)MHT, (double)HT, mdp, (double)weight)){
               //cout << "HT: " << HT;
               //cout << ", MHT: " << MHT;
               //cout << ", NJets: " << NJets;
               //cout << ", BTags: " << BTags;
               //cout << ", MDP: " << mdp;
               //cout << ", weight: " << weight << endl;
               //break;
            };
         }
         
      }
   }
   cout << "Prediction entries final: " <<  Prediction_entries << endl;
   
   // ------------------------------------------------------------- //
   
   ///////////////////////////////////////////////////////////////////////
   // get event selections
   cout << "entries selection tree:" << RA2PreSelection.GetEntries() << endl;
   
   // variables from selection tree
   vtxN_RA2 = 0;
   NLeptons_RA2 = 0;
   NJets_RA2 = 0;
   BTags_RA2 = 0;
   weight_RA2 = 0;
   EvtNum_RA2 = 0;
   HT_RA2 = 0;
   MHT_RA2 = 0;
   Jet1Pt_RA2 = 0;
   Jet2Pt_RA2 = 0;
   Jet3Pt_RA2 = 0;
   Jet4Pt_RA2 = 0;
   Jet1Eta_RA2 = 0;
   Jet2Eta_RA2 = 0;
   Jet3Eta_RA2 = 0;
   Jet4Eta_RA2 = 0;
   DeltaPhi1_RA2 = 0;
   DeltaPhi2_RA2 = 0;
   DeltaPhi3_RA2 = 0;
   minDeltaPhiN_RA2 = 0;
   
   cout << "Before: SetBranchAddress (expectation)" << endl;
   
   RA2PreSelection.SetBranchAddress("NVtx",&vtxN_RA2);
   RA2PreSelection.SetBranchAddress("GoodLeptons",&NLeptons_RA2);
   RA2PreSelection.SetBranchAddress("NJets",&NJets_RA2);
   RA2PreSelection.SetBranchAddress("BTags",&BTags_RA2);
   RA2PreSelection.SetBranchAddress("Weight",&weight_RA2);
   RA2PreSelection.SetBranchAddress("EvtNum",&EvtNum_RA2);
   RA2PreSelection.SetBranchAddress("HT",&HT_RA2);
   RA2PreSelection.SetBranchAddress("MHT",&MHT_RA2);
   RA2PreSelection.SetBranchAddress("Jet1Pt",&Jet1Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet2Pt",&Jet2Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet3Pt",&Jet3Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet4Pt",&Jet4Pt_RA2);
   RA2PreSelection.SetBranchAddress("Jet1Eta",&Jet1Eta_RA2);
   RA2PreSelection.SetBranchAddress("Jet2Eta",&Jet2Eta_RA2);
   RA2PreSelection.SetBranchAddress("Jet3Eta",&Jet3Eta_RA2);
   RA2PreSelection.SetBranchAddress("Jet4Eta",&Jet4Eta_RA2);
   RA2PreSelection.SetBranchAddress("DeltaPhi1",&DeltaPhi1_RA2);
   RA2PreSelection.SetBranchAddress("DeltaPhi2",&DeltaPhi2_RA2);
   RA2PreSelection.SetBranchAddress("DeltaPhi3",&DeltaPhi3_RA2);
   RA2PreSelection.SetBranchAddress("minDeltaPhiN",&minDeltaPhiN_RA2);
   
   cout << "After: SetBranchAddress (expectation)" << endl;
   
   // loop over entries and fill selection histos
   Int_t nentries2 = RA2PreSelection.GetEntries();
   
   for ( Int_t i = 0 ; i<nentries2 ; i++) {
      
      RA2PreSelection.GetEntry(i);
      
      if( i%100000 == 0 ) std::cout << "event (selection): " << i << '\n';
      
      bool mdp_RA2 = DeltaPhiCut_selection();
      if( HT_RA2 > 500. && MHT_RA2 > 200. && NJets_RA2 >= 4 && NLeptons_RA2 == 0 && vtxN_RA2 >= 0 && mdp_RA2) {
         
         for (int it = 0; it < SB.size(); ++it){
            if (SB.at(it)->FillExp((int) NJets_RA2, (int)BTags_RA2, (double)MHT_RA2, (double)HT_RA2, mdp_RA2, (double)weight_RA2));
         }
         
      }
   }
   
   //----------------------------------------------------------//
   
   cout << "Variation: " << Uncertainty << endl;
   cout << "No." << ", " << "BinName" << ", " << "mean_pred" << ", " << "var_pred"  << ", " << "mean_exp" << ", " << "var_exp" << endl;
   for (int it = 0; it < SB.size(); ++it){
      double mean_pred, mean_exp;
      double var_pred, var_exp;
      if ( SB.at(it)->GetPred(mean_pred, var_pred) ){
         cout << it << ", " << SB.at(it)->BinName << ", " << mean_pred << ", " << var_pred;
      }
      if ( SB.at(it)->GetExp(mean_exp, var_exp) ){
         cout << ", " << mean_exp << ", " << var_exp << endl;
      }
   }
   
}

////////////////////////////////////////////////////////////////////////////////////////
bool BinPrediction::DeltaPhiCut_prediction()
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
   //   if (minDeltaPhiN < 6) deltaPhiCut = false;
   
   return deltaPhiCut;
}
////////////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////
bool BinPrediction::DeltaPhiCut_selection()
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
   //   if (minDeltaPhiN_RA2 < 6) deltaPhiCut = false;
   
   return deltaPhiCut;
}
////////////////////////////////////////////////////////////////////////////////////////


