#ifndef iso_act_h
#define iso_act_h

// adapted from https://github.com/ald77/cmssw/blob/TnP_v3/RecoEgamma/EgammaIsolationAlgos/plugins/isolation_cones/ElectronMiniIsolationWithConeVeto.cc

#include <cmath>
#include <algorithm>
#include <vector>

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


class SUSYIsolation {
public:
  enum iso_types { electron = 0, muon = 1, other = 2 };

  std::vector<double> electronEAValues;
  std::vector<double> muonEAValues;

  void SetEAVectors(const std::vector<double> & electronValues, const std::vector<double> muonValues) {
    electronEAValues = electronValues;
    muonEAValues = muonValues;
  }

  // Effective areas from https://twiki.cern.ch/twiki/bin/view/CMS/SUSLeptonSF
  double GetMuonEA(double eta) const {
    if (muonEAValues.size()!=5)
      throw cms::Exception("The muon effective area vector does not have the proper size (5).");

    double abseta = fabs(eta);
    if (abseta < 0.8) return muonEAValues[0];
    else if (abseta < 1.3) return muonEAValues[1];
    else if (abseta < 2.0) return muonEAValues[2];
    else if (abseta < 2.2) return muonEAValues[3];
    else if (abseta < 2.5) return muonEAValues[4];
    else return 0;
  }

  double GetElectronEA(double eta) const {
    if (electronEAValues.size()!=7)
      throw cms::Exception("The electron effective area vector does not have the proper size (7).");

    double abseta = fabs(eta);
    if (abseta < 1) return electronEAValues[0];
    else if (abseta < 1.479) return electronEAValues[1];
    else if (abseta < 2.0) return electronEAValues[2];
    else if (abseta < 2.2) return electronEAValues[3];
    else if (abseta < 2.3) return electronEAValues[4];
    else if (abseta < 2.4) return electronEAValues[5];
    else if (abseta < 2.5) return electronEAValues[6];
    else return 0;
  }

  void GetCandIso(bool computeMT2Activity, const pat::PackedCandidate &pfc, double dr, double ptThresh, std::vector<double>& iso_x, const std::vector<double>& deadcones) const {
    //setup variables
    double& iso_nh = iso_x[0]; double& iso_ch = iso_x[1]; double& iso_ph = iso_x[2]; double& iso_pu = iso_x[3];
    const double& deadcone_nh = deadcones[0]; const double& deadcone_ch = deadcones[1]; const double& deadcone_ph = deadcones[2]; const double& deadcone_pu = deadcones[3];
    
    //////////////////  NEUTRALS  /////////////////////////
    if (pfc.charge()==0){
      if (pfc.pt()>ptThresh) {
        /////////// PHOTONS ////////////
        if (abs(pfc.pdgId())==22) {
          if(!computeMT2Activity && dr < deadcone_ph) return;
          iso_ph += pfc.pt();
          /////////// NEUTRAL HADRONS ////////////
        } else if (abs(pfc.pdgId())==130) {
          if(!computeMT2Activity && dr < deadcone_nh) return;
          iso_nh += pfc.pt();
        }
      }
      //////////////////  CHARGED from PV  /////////////////////////
    } else if (pfc.fromPV()>1 || std::abs(pfc.dz()) < 0.1){
      if (abs(pfc.pdgId())==211) {
        if(!computeMT2Activity && dr < deadcone_ch) return;
        iso_ch += pfc.pt();
      }
      //////////////////  CHARGED from PU  /////////////////////////
    } else {
      if (pfc.pt()>ptThresh){
        if(!computeMT2Activity && dr < deadcone_pu) return;
        iso_pu += pfc.pt();
      }
    }
  }
  
  double GetFinalIso(const reco::Candidate* ptcl, iso_types type, double r_iso, double rho, const std::vector<double>& iso_x, bool useEAcorr=true, bool charged_only=false) const {
    //setup variables
    const double& iso_nh = iso_x[0]; const double& iso_ch = iso_x[1]; const double& iso_ph = iso_x[2]; const double& iso_pu = iso_x[3];

    double iso(0.);
    if (charged_only){
      iso = iso_ch;
    } else {
      iso = iso_ph + iso_nh;
      if (useEAcorr) {
        double eta = ptcl->eta();
        double EA;
        if(type==electron) {
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

  void GetPFIsolation(edm::Handle<edm::View<pat::PackedCandidate> > pfcands, const unsigned pfcand_idx,
                      double& pf_iso_all, double& pf_iso_chg, //return values
                      double r_pfiso=0.3, double ptThresh=0.0) const
  {
    pf_iso_all = 0.0;
    pf_iso_chg = 0.0;
    const auto& ptcl = pfcands->at(pfcand_idx);
    if (ptcl.p4().Pt()<5.) {
      pf_iso_all = 99999.;
      pf_iso_chg = 99999.;
      return;
  }

    //nh, ch, ph, pu
    std::vector<double> iso_pf(4, 0.);
    std::vector<double> deadcones(4,0.);
    for (unsigned int iPF(0); iPF<pfcands->size(); iPF++) {
      const pat::PackedCandidate &pfc = pfcands->at(iPF);
      if (abs(pfc.pdgId())<7) continue;
      if (iPF==pfcand_idx) continue; // don't count track in its own sum
      double dr = deltaR(pfc, ptcl);
      // rel-iso cone
      if (dr < r_pfiso) GetCandIso(false,pfc,dr,ptThresh,iso_pf,deadcones);
    }

    pf_iso_all = GetFinalIso(&ptcl, iso_types::other, 0.0, 0.0, iso_pf, false, false);
    pf_iso_chg = GetFinalIso(&ptcl, iso_types::other, 0.0, 0.0, iso_pf, false, true);
  }

  void GetMiniIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
                        const reco::Candidate* ptcl, iso_types type, double rho,
                        double& mini_iso, double& mt2_activity, //return values
                        double r_iso_min=0.05, double r_iso_max=0.2, double kt_scale=10.,
                        bool useEAcorr=true, bool charged_only=false) const
  {
    mini_iso = 0.0;
    mt2_activity = 0.0;
    if (ptcl->pt()<5.) {
		mini_iso = 99999.;
		mt2_activity = 99999.;
		return;
	}

    //nh, ch, ph, pu
    std::vector<double> deadcones(4,0.);
    if(type==electron) {
      if (fabs(ptcl->eta())>1.479) {deadcones[1] = 0.015; deadcones[2] = 0.08; deadcones[3] = 0.015;}
    } else if(type==muon) {
      deadcones[0] = 0.01; deadcones[1] = 0.0001; deadcones[2] = 0.01; deadcones[3] = 0.01;  
    } else {
      deadcones[0] = 0.01; deadcones[1] = 0.0001; deadcones[2] = 0.01; deadcones[3] = 0.01; // maybe use muon cones??
    }

    //nh, ch, ph, pu
    std::vector<double> iso_mini(4,0.);
    std::vector<double> iso_mt2(4, 0.);
    double ptThresh(0.5);
    if(type==electron) ptThresh = 0;
    double r_iso = std::max(r_iso_min, std::min(r_iso_max, kt_scale/ptcl->pt()));

    for (const pat::PackedCandidate &pfc : *pfcands) {
      if (abs(pfc.pdgId())<7) continue;

      double dr = deltaR(pfc, *ptcl);
      // MT2 activity annulus
      if (dr >= r_iso && dr <= 0.4) GetCandIso(true,pfc,dr,ptThresh,iso_mt2,deadcones);
      // mini-iso cone
      if (dr <= r_iso) GetCandIso(false,pfc,dr,ptThresh,iso_mini,deadcones);

    }
    
    mt2_activity = GetFinalIso(ptcl,type,r_iso,rho,iso_mt2,useEAcorr,charged_only);
    mini_iso = GetFinalIso(ptcl,type,r_iso,rho,iso_mini,useEAcorr,charged_only);

  }
  
  double GetRA2Activity(edm::Handle<pat::JetCollection> jets, const reco::Candidate* ptcl, const bool useEME=true) const {

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
  
};

#endif

