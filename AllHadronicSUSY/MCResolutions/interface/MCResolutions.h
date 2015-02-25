#ifndef MCResolutions_H
#define MCResolutions_H

// system include files
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TMath.h"
#include "TFile.h"

// b-Tagging
#include "DataFormats/BTauReco/interface/JetTag.h"

//
// class declaration
//

class MCResolutions: public edm::EDAnalyzer {
   public:
   explicit MCResolutions(const edm::ParameterSet&);
   ~MCResolutions();

   private:
   virtual void beginJob();
   virtual void analyze(const edm::Event&, const edm::EventSetup&);
   virtual void endJob();

   // ----------member data ---------------------------
   edm::InputTag _jetTag;
   edm::InputTag _leptonTag;
   std::string _btagTag;
   edm::InputTag _genJetTag;
   edm::InputTag _weightName;

   double _btagCut;
   double _jetMultPtCut;
   double _jetMultEtaCut;
   double _deltaPhiDiJet;
   double _absCut3rdJet;
   double _relCut3rdJet;
   double _deltaRMatch;
   double _deltaRMatchVeto;
   double _absPtVeto;
   double _relPtVeto;
   double _GenJetPtCut;
   std::string _fileName;

   double weight;

   // JetResponse in Pt and eta bins
   int PtBin(const double& pt);
   int EtaBin(const double& eta);

   // Resize histo vectors
   void ResizeHistoVector(std::vector<std::vector<TH1F*> > &histoVector);

   // total
   std::vector<std::vector<TH1F*> > h_tot_DiJet_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_tot_JetAll_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_tot_Jet1_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_tot_Jet2_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_tot_Jet3_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_tot_Jet4_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_tot_Jet5p_JetResPt_Pt;
   // with btag
   std::vector<std::vector<TH1F*> > h_b_DiJet_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_b_JetAll_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_b_Jet1_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_b_Jet2_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_b_Jet3_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_b_Jet4_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_b_Jet5p_JetResPt_Pt;
   // without btag
   std::vector<std::vector<TH1F*> > h_nob_DiJet_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_nob_JetAll_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_nob_Jet1_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_nob_Jet2_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_nob_Jet3_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_nob_Jet4_JetResPt_Pt;
   std::vector<std::vector<TH1F*> > h_nob_Jet5p_JetResPt_Pt;

   std::vector<double> PtBinEdges;
   std::vector<double> EtaBinEdges;

   TFile* hfile;

};

#endif
