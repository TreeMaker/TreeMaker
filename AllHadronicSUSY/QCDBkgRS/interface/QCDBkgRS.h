#ifndef QCDBkgRS_H
#define QCDBkgRS_H
// -*- C++ -*-
//
// Package:    QCDBkgRS
// Class:      QCDBkgRS
//
//**\class QCDBkgRS QCDBkgRS.h RA2Classic/QCDBkgRS/interface/QCDBkgRS.h

// system include files
#include <memory>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "PhysicsTools/KinFitter/interface/TKinFitter.h"
#include "PhysicsTools/KinFitter/interface/TFitParticleEtEtaPhi.h"
#include "PhysicsTools/KinFitter/interface/TFitConstraintEp.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "CommonTools/Utils/interface/PtComparator.h"

#include "TRandom3.h"
#include "TF1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include "TTree.h"
#include "TKey.h"
#include "TFile.h"
#include "TMath.h"
#include "TArray.h"

//#include "Utilities/Parang/interface/Paramatrix.h"
#include "SmearFunction.h"

using namespace std;

//typedef Paramatrix<PopulationF> ParamatrixF;
//typedef Paramatrix<PopulationD> ParamatrixD;

class QCDBkgRS: public edm::EDAnalyzer {
public:
   explicit QCDBkgRS(const edm::ParameterSet&);
   ~QCDBkgRS();
   
private:
   virtual void beginJob();
   virtual void analyze(const edm::Event&, const edm::EventSetup&);
   virtual void endJob();
   
   typedef math::XYZTLorentzVector LorentzVector;
   typedef std::vector<std::string>::const_iterator StrIter;

   SmearFunction *smearFunc_;        // Object of class SmearFunction
   
   double rebalancedJetPt_;
   std::string rebalanceMode_; // "MHTall", "MHThigh" or "MET" only for smearCollection = "Reco"
   
   int nSmearedJets_;
   double smearedJetPt_;
   std::vector<double> PtBinEdges_scaling_;
   std::vector<double> EtaBinEdges_scaling_;
   std::vector<double> AdditionalSmearing_;
   std::vector<double> LowerTailScaling_;
   std::vector<double> UpperTailScaling_;
   double AdditionalSmearing_variation_;
   double LowerTailScaling_variation_;
   double UpperTailScaling_variation_;
   std::string smearCollection_; // "Gen" or "Reco"
   
   edm::InputTag vertices_;
   edm::InputTag genjets_;
   edm::InputTag jets_;
   edm::InputTag weightName_;
   std::string jets_reb_;
   std::string met_reb_;
   std::string jets_smeared_;
   std::string genjets_smeared_;
   
   //// vector of response function
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_Core;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_LowerTail;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_UpperTail;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_scaled;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_HF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_Core_HF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_LowerTail_HF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_UpperTail_HF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_scaled_HF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_NoHF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_Core_NoHF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_LowerTail_NoHF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_UpperTail_NoHF;
   std::vector<std::vector<std::vector<TH1F*> > > smearFunc_scaled_NoHF;
   std::vector<std::vector<TH1F*> > SigmaPtHist;
   std::vector<std::vector<TF1*> > SigmaPt;
   std::vector<std::vector<TH1F*> > SigmaPtHist_scaled;
   std::vector<std::vector<TF1*> > SigmaPt_scaled;
   std::vector<double> PtBinEdges_;
   std::vector<double> EtaBinEdges_;
   std::string inputhist1HF_;
   std::string inputhist2HF_;
   std::string inputhist3pHF_;
   std::string inputhist1NoHF_;
   std::string inputhist2NoHF_;
   std::string inputhist3pNoHF_;
   std::string smearingfile_;
   std::string bprobabilityfile_;
   std::string outputfile_;
   std::string RebalanceCorrectionFile_;
   int NRebin_;
   bool controlPlots_;
   bool isData_;
   bool isMadgraph_;
   bool absoluteTailScaling_;
   bool cleverPrescaleTreating_;
   bool useRebalanceCorrectionFactors_;
   double A0RMS_;
   double A1RMS_;
   double probExtreme_;
   double MHTmin_;
   double MHTmax_;
   double HTmin_;
   double HTmax_;
   int NbinsMHT_;
   int NbinsHT_;
   int Ntries_;
   int NJets_;
   double JetsHTPt_;
   double JetsHTEta_;
   double JetsMHTPt_;
   double JetsMHTEta_;
   vector<double> JetDeltaMin_;
   double MHTcut_low_;
   double MHTcut_medium_;
   double MHTcut_high_;
   double HTcut_low_;
   double HTcut_medium_;
   double HTcut_high_;
   double HTcut_veryhigh_;
   double HTcut_extremehigh_;
   
   std::string uncertaintyName_;
   
   int plotindex_;
   TRandom3 *rand_;
   
   double JetResolution_Pt2(const double&, const double&, const int&);
   double JetResolution_Ptrel(const double&, const double&, const int&);
   double JetResolution_Eta2(const double&, const double&);
   double JetResolution_Phi2(const double&, const double&);
   double JetResolutionHist_Pt_Smear(const double&, const double&, const int&,const double&, const int&);
   double GetHFProb(const int&, const double&, const int&);
   int GetIndex(const double&, const std::vector<double>*);
   void FillPredictions(const std::vector<pat::Jet>&, const int&, const double&);
   void FillPredictions_gen(const std::vector<reco::GenJet>&, const int&, const double&);
   double calcHT(const std::vector<pat::Jet>&);
   double calcHT_gen(const std::vector<reco::GenJet>&);
   math::PtEtaPhiMLorentzVector calcMHT(const std::vector<pat::Jet>&);
   math::PtEtaPhiMLorentzVector calcMHT_gen(const std::vector<reco::GenJet>&);
   int calcNJets(const std::vector<pat::Jet>&);
   int calcNJets_gen(const std::vector<reco::GenJet>&);
   bool calcMinDeltaPhi(const std::vector<pat::Jet>&, math::PtEtaPhiMLorentzVector&);
   bool calcMinDeltaPhi_gen(const std::vector<reco::GenJet>&, math::PtEtaPhiMLorentzVector&);
   void FillLeadingJetPredictions(const std::vector<pat::Jet>&); 
   void FillDeltaPhiPredictions(const std::vector<pat::Jet>&, math::PtEtaPhiMLorentzVector&); 
   void FillLeadingJetPredictions_gen(const std::vector<reco::GenJet>&); 
   void FillDeltaPhiPredictions_gen(const std::vector<reco::GenJet>&, math::PtEtaPhiMLorentzVector&); 
   double GetRebalanceCorrection(double jet_pt);

   
   bool RebalanceJets_KinFitter(edm::View<pat::Jet>*, std::vector<pat::Jet> &);
   void SmearingJets(const std::vector<pat::Jet>&, std::vector<pat::Jet> &);
   void SmearingGenJets(edm::View<reco::GenJet>*, std::vector<reco::GenJet> &);
   
   std::string GetName(const std::string plot, const std::string uncert = "", const std::string ptbin = "") const;
   
   TH2F* h_RecJetRes_Pt;
   TH2F* h_RecJetRes_Eta;
   TH2F* h_RebJetRes_Pt;
   TH2F* h_RebJetRes_Eta;
   TH2F* h_SmearedJetRes_Pt;
   TH2F* h_SmearedJetRes_Eta;

   TH2F* h_RebCorrection_vsReco;  
   TH1F* h_RebCorrectionFactor;
  
   // TH2F* h_bProb_NJets1;
   TH2F* h_bProb_NJets2;
   TH2F* h_bProb_NJets3;
   TH2F* h_bProb_NJets4;
   TH2F* h_bProb_NJets5p6;
   TH2F* h_bProb_NJets7p;

   TH1F* h_nJets_gen;
   TH1F* h_nJets_reco;
   TH1F* h_nJets_reb;
   TH1F* h_nJets_smear;
   TH1F* h_JetPt_gen;
   TH1F* h_JetPt_reco;
   TH1F* h_JetPt_reb;
   TH1F* h_JetPt_smear;
   
   TH1F *h_HT_gen, *h_HT_rec, *h_HT_smeared, *h_HT_reb;
   TH1F *h_deltaPhiJet1Jet2_gen, *h_deltaPhiJet1Jet2_rec, *h_deltaPhiJet1Jet2_smeared, *h_deltaPhiJet1Jet2_reb;
   TH1F *h_HT_JetBin1_gen, *h_HT_JetBin1_rec, *h_HT_JetBin1_smeared, *h_HT_JetBin1_reb;
   TH1F *h_HT_JetBin2_gen, *h_HT_JetBin2_rec, *h_HT_JetBin2_smeared, *h_HT_JetBin2_reb;
   TH1F *h_HT_JetBin3_gen, *h_HT_JetBin3_rec, *h_HT_JetBin3_smeared, *h_HT_JetBin3_reb;
   TH1F *h_HT_JetBin4_gen, *h_HT_JetBin4_rec, *h_HT_JetBin4_smeared, *h_HT_JetBin4_reb;
   TH1F *h_HTall_gen, *h_HTall_rec, *h_HTall_smeared, *h_HTall_reb;
   TH1F *h_HThigh_gen, *h_HThigh_rec, *h_HThigh_smeared, *h_HThigh_reb;
   TH1F *h_MHTall_gen, *h_MHTall_rec, *h_MHTall_smeared, *h_MHTall_reb;
   TH1F *h_MHThigh_gen, *h_MHThigh_rec, *h_MHThigh_smeared, *h_MHThigh_reb;
   
   TH1F *h_RecJetMatched_Pt, *h_RecJetNotMatched_Pt;
   TH1F *h_RecJetMatched_JetBin1_Pt, *h_RecJetNotMatched_JetBin1_Pt;
   TH1F *h_RecJetMatched_JetBin2_Pt, *h_RecJetNotMatched_JetBin2_Pt;
   TH1F *h_RecJetMatched_JetBin3_Pt, *h_RecJetNotMatched_JetBin3_Pt;
   TH1F *h_RecJetMatched_JetBin4_Pt, *h_RecJetNotMatched_JetBin4_Pt;
       
   TH1F *h_fitProb;
   TH1F *h_weight;
   TH1F *h_weightedWeight;

   TH1F *h_deltaR_rebCorr;

   TH2F *h_SeedEvents_HT_NJet2;
   TH2F *h_SeedEvents_HT_NJet3;
   TH2F *h_SeedEvents_HT_NJet4;
   TH2F *h_SeedEvents_HT_NJet5;
   TH2F *h_SeedEvents_HT_NJet6;
   TH2F *h_SeedEvents_HT_NJet7;
   TH2F *h_SeedEvents_HT_NJet8;
      
   double weight_;

   TTree *PredictionTree;
   UShort_t vtxN;
   UShort_t Njets_pred;
   UShort_t Ntries_pred;
   Float_t HT_seed;
   Float_t HT_pred;
   Float_t MHT_pred;
   Float_t weight;
   Float_t Jet1Pt_pred;
   Float_t Jet2Pt_pred;
   Float_t Jet3Pt_pred;
   Float_t Jet1Eta_pred;
   Float_t Jet2Eta_pred;
   Float_t Jet3Eta_pred;
   Float_t DeltaPhi1_pred;
   Float_t DeltaPhi2_pred;
   Float_t DeltaPhi3_pred;
};

#endif
