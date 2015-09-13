#ifndef iso_act_h
#define iso_act_h

// adapted from https://github.com/ald77/cmssw/blob/TnP_v3/RecoEgamma/EgammaIsolationAlgos/plugins/isolation_cones/ElectronMiniIsolationWithConeVeto.cc

#include <cmath>
#include <algorithm>

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Utilities/interface/Exception.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

#include "DataFormats/Common/interface/ConditionsInEdm.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

#include "DataFormats/Math/interface/deltaR.h"


namespace SUSYIsolation {

  inline double GetMuonEA(double eta) {
    double ea = 0.;
    if      (fabs(eta)<=0.800) ea = 0.0913;
    else if (fabs(eta)<=1.300) ea = 0.0765;
    else if (fabs(eta)<=2.000) ea = 0.0546;
    else if (fabs(eta)<=2.200) ea = 0.0728;
    else if (fabs(eta)<=2.500) ea = 0.1177;
    return ea;
  }

  inline double GetElectronEA(double eta) {
    double ea = 0.;
    if      (fabs(eta)<=0.800) ea = 0.1013;
    else if (fabs(eta)<=1.300) ea = 0.0988;
    else if (fabs(eta)<=2.000) ea = 0.0572;
    else if (fabs(eta)<=2.200) ea = 0.0842;
    else if (fabs(eta)<=2.500) ea = 0.1530;
    return ea;
  }
  
  inline double GetMiniIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
				 const reco::Candidate* ptcl, std::string type, 
				 double rho, bool computeMT2Activity=false,
				 double r_iso_min=0.05, double r_iso_max=0.2, double kt_scale=10.,
				 bool useEAcorr=true, bool charged_only=false) {
    
    if (ptcl->pt()<5.) return 99999.;

    double deadcone_nh(0.), deadcone_ch(0.), deadcone_ph(0.), deadcone_pu(0.);
    if(type=="electron") {
      if (fabs(ptcl->eta())>1.479) {deadcone_ch = 0.015; deadcone_pu = 0.015; deadcone_ph = 0.08;}
    } else if(type=="muon") {
      deadcone_ch = 0.0001; deadcone_pu = 0.01; deadcone_ph = 0.01;deadcone_nh = 0.01;  
    } else {
      deadcone_ch = 0.0001; deadcone_pu = 0.01; deadcone_ph = 0.01;deadcone_nh = 0.01; // maybe use muon cones??
    }

    double iso_nh(0.); double iso_ch(0.); 
    double iso_ph(0.); double iso_pu(0.);
    double ptThresh(0.5);
    if(type=="electron") ptThresh = 0;
    double r_iso = std::max(r_iso_min, std::min(r_iso_max, kt_scale/ptcl->pt()));
    
    for (const pat::PackedCandidate &pfc : *pfcands) {
      if (abs(pfc.pdgId())<7) continue;

      double dr = deltaR(pfc, *ptcl);
      if (computeMT2Activity) {
	if (dr < r_iso || dr > 0.4) continue; // activity annulus
      }
      else if (dr > r_iso) continue;
      
      //////////////////  NEUTRALS  /////////////////////////
      if (pfc.charge()==0){
        if (pfc.pt()>ptThresh) {
          /////////// PHOTONS ////////////
          if (abs(pfc.pdgId())==22) {
            if(!computeMT2Activity && dr < deadcone_ph) continue;
            iso_ph += pfc.pt();
	    /////////// NEUTRAL HADRONS ////////////
          } else if (abs(pfc.pdgId())==130) {
            if(!computeMT2Activity && dr < deadcone_nh) continue;
            iso_nh += pfc.pt();
          }
        }
        //////////////////  CHARGED from PV  /////////////////////////
      } else if (pfc.fromPV()>1){
        if (abs(pfc.pdgId())==211) {
          if(!computeMT2Activity && dr < deadcone_ch) continue;
          iso_ch += pfc.pt();
        }
        //////////////////  CHARGED from PU  /////////////////////////
      } else {
	if (pfc.pt()>ptThresh){
          if(!computeMT2Activity && dr < deadcone_pu) continue;
          iso_pu += pfc.pt();
        }
      }
    }
    double iso(0.);
    if (charged_only){
      iso = iso_ch;
    } else {
      iso = iso_ph + iso_nh;
      if (useEAcorr) {
	double eta = ptcl->eta();
	double EA;
	if(type=="electron") {
	  EA = GetElectronEA(eta);
	} else EA = GetMuonEA(eta);
	double correction = rho * EA * (r_iso/0.3) * (r_iso/0.3);
	iso -= correction;
      }
      else iso -= 0.5*iso_pu; // DB correction
      if (iso>0) iso += iso_ch;
      else iso = iso_ch;
    }
    iso = iso/ptcl->pt();

    return iso;
  }

  
  inline double GetRA2Activity(edm::Handle<pat::JetCollection> jets, const reco::Candidate* ptcl, const bool useEME=true) {

    double activity=0;
    for (unsigned int ijet(0); ijet < jets->size(); ijet++) 
      {
	const pat::Jet &thisJet = (*jets)[ijet];
	if(deltaR(ptcl->eta(),ptcl->phi(),thisJet.eta(),thisJet.phi())>1.0) continue;
	double chFrac = thisJet.chargedHadronEnergy()/thisJet.energy();
	if (useEME) chFrac+=thisJet.chargedEmEnergy()/thisJet.energy();
	activity+=thisJet.pt() * chFrac;
      }
    return activity;
  }
  
}

#endif

