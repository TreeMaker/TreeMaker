// -*- C++ -*-
//
// Package:    NtupleMaker
// Class:      NtupleMaker
// 
/**\class NtupleMaker NtupleMaker.cc CMS2/NtupleMaker/src/NtupleMaker.cc

   Description: <one line class summary>

   Implementation:
   <Notes on implementation>
*/
#ifndef NTUPLEFILTER_TRACKISOLATIONFILTER_H
#define NTUPLEFILTER_TRACKISOLATIONFILTER_H

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/ParticleFlow/interface/PFPileUpAlgo.h"
#include "Math/VectorUtil.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "TLorentzVector.h"
#include "TTree.h"

//
// class decleration
//

class TrackIsolationFilter : public edm::EDFilter {
public:
     explicit TrackIsolationFilter (const edm::ParameterSet&);
     ~TrackIsolationFilter();

private:
  virtual bool filter(edm::Event & iEvent, const edm::EventSetup & iSetup);

  // ----------member data ---------------------------
  double dR_;
  double dzcut_;
  double minPt_;
  double maxEta_;
  double isoCut_;
  double mTCut_;
  bool doTrkIsoVeto_;
  int pdgId_;
  bool debug_;

  edm::InputTag pfCandidatesTag_;
  edm::InputTag vertexInputTag_;
  edm::InputTag MetInputTag_;

  int vtxSize;

  const double GetTrkIso(edm::Handle<edm::View<pat::PackedCandidate> > pfcands, const int tkInd, bool doActivity=false);

};

#endif

