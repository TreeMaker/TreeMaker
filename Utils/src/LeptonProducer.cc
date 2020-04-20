// -*- C++ -*-
//
// Package:    LeptonProducer
// Class:      LeptonProducer
//
/**\class LeptonProducer LeptonProducer.cc RA2Classic/LeptonProducer/src/LeptonProducer.cc
 * 
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files

#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TVector2.h"

#include "TreeMaker/Utils/interface/get_isolation_activity.h"
//
// class declaration
//

class LeptonProducer : public edm::global::EDProducer<> {
  enum elecIDLevel {VETO, LOOSE, MEDIUM, TIGHT};
public:
  explicit LeptonProducer(const edm::ParameterSet&);
  ~LeptonProducer() override;
        
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  float MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi) const;
  bool MuonIDloose(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool MuonIDmedium(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool MuonIDtight(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level, const double rho = 0.0) const;
        
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
        
  // ----------member data ---------------------------
  edm::InputTag MuonTag_, ElecTag_, PrimVtxTag_, metTag_, PFCandTag_, RhoTag_;
  edm::EDGetTokenT<edm::View<pat::Muon>> MuonTok_;
  edm::EDGetTokenT<edm::View<pat::Electron>> ElecTok_;
  edm::EDGetTokenT<reco::VertexCollection> PrimVtxTok_;
  edm::EDGetTokenT<edm::View<pat::MET>> metTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> PFCandTok_;
  edm::EDGetTokenT<double> RhoTok_;
  double minElecPt_, maxElecEta_, elecIsoValue_;
  std::vector<double> eb_ieta_cut_, eb_deta_cut_, eb_dphi_cut_, eb_hovere_cut_, eb_hovere_cut2_, eb_hovere_cut3_, eb_ooeminusoop_cut_, eb_d0_cut_, eb_dz_cut_;
  std::vector<int> eb_misshits_cut_;
  std::vector<double> ee_ieta_cut_, ee_deta_cut_, ee_dphi_cut_, ee_hovere_cut_, ee_hovere_cut2_, ee_hovere_cut3_, ee_ooeminusoop_cut_, ee_d0_cut_, ee_dz_cut_;
  std::vector<int> ee_misshits_cut_;
  bool hovere_constant_;
  double minMuPt_, maxMuEta_, muIsoValue_;
  double muNormalizedChi2Max_, muChi2LocalPositionMax_, muTrkKink_, muValidFractionMin_;
  std::vector<double> muSegmentCompatibilityMin_;
  double mudBMax_, mudZMax_;
  double tightMuNormalizedChi2Max_;
  int tightMuNumberOfValidMuonHitsMin_, tightMuNumberOfMatchedStationsMin_;
  double tightMudBMax_, tightMudZMax_;
  int tightMuNumberOfValidPixelHitsMin_, tightMuTrackerLayersWithMeasurementMin_;
  bool useMiniIsolation_;
  std::vector<double> electronEAValues_, muonEAValues_;
  SUSYIsolation SUSYIsolationHelper;
  bool debug_;
};

//
// constructors and destructor
//
LeptonProducer::LeptonProducer(const edm::ParameterSet& iConfig):
  //register your products
  MuonTag_                               (iConfig.getParameter<edm::InputTag>("MuonTag")),
  ElecTag_                               (iConfig.getParameter<edm::InputTag>("ElectronTag")),
  PrimVtxTag_                            (iConfig.getParameter<edm::InputTag>("PrimaryVertex")),
  metTag_                                (iConfig.getParameter<edm::InputTag> ("METTag")),
  PFCandTag_                             (edm::InputTag("packedPFCandidates")),
  RhoTag_                                (iConfig.getParameter<edm::InputTag> ("rhoCollection")),
  MuonTok_                               (consumes<edm::View<pat::Muon>>(MuonTag_)),
  ElecTok_                               (consumes<edm::View<pat::Electron>>(ElecTag_)),
  PrimVtxTok_                            (consumes<reco::VertexCollection>(PrimVtxTag_)),
  metTok_                                (consumes<edm::View<pat::MET>>(metTag_)),
  PFCandTok_                             (consumes<pat::PackedCandidateCollection>(PFCandTag_)),
  RhoTok_                                (consumes<double>(RhoTag_)),
  minElecPt_                             (iConfig.getParameter<double>("minElecPt")),
  maxElecEta_                            (iConfig.getParameter<double>("maxElecEta")),
  elecIsoValue_                          (iConfig.getParameter<double>("elecIsoValue")),
  eb_ieta_cut_                           (iConfig.getParameter<std::vector<double>>("eb_ieta_cut")),
  eb_deta_cut_                           (iConfig.getParameter<std::vector<double>>("eb_deta_cut")),
  eb_dphi_cut_                           (iConfig.getParameter<std::vector<double>>("eb_dphi_cut")),
  eb_hovere_cut_                         (iConfig.getParameter<std::vector<double>>("eb_hovere_cut")),
  eb_ooeminusoop_cut_                    (iConfig.getParameter<std::vector<double>>("eb_ooeminusoop_cut")),
  eb_d0_cut_                             (iConfig.getParameter<std::vector<double>>("eb_d0_cut")),
  eb_dz_cut_                             (iConfig.getParameter<std::vector<double>>("eb_dz_cut")),
  eb_misshits_cut_                       (iConfig.getParameter<std::vector<int>>("eb_misshits_cut")),
  ee_ieta_cut_                           (iConfig.getParameter<std::vector<double>>("ee_ieta_cut")),
  ee_deta_cut_                           (iConfig.getParameter<std::vector<double>>("ee_deta_cut")),
  ee_dphi_cut_                           (iConfig.getParameter<std::vector<double>>("ee_dphi_cut")),
  ee_hovere_cut_                         (iConfig.getParameter<std::vector<double>>("ee_hovere_cut")),
  ee_ooeminusoop_cut_                    (iConfig.getParameter<std::vector<double>>("ee_ooeminusoop_cut")),
  ee_d0_cut_                             (iConfig.getParameter<std::vector<double>>("ee_d0_cut")),
  ee_dz_cut_                             (iConfig.getParameter<std::vector<double>>("ee_dz_cut")),
  ee_misshits_cut_                       (iConfig.getParameter<std::vector<int>>("ee_misshits_cut")),
  hovere_constant_                       (iConfig.getParameter<bool>("hovere_constant")),
  minMuPt_                               (iConfig.getParameter<double>("minMuPt")),
  maxMuEta_                              (iConfig.getParameter<double>("maxMuEta")),
  muIsoValue_                            (iConfig.getParameter<double>("muIsoValue")),
  muNormalizedChi2Max_                   (iConfig.getParameter<double>("muNormalizedChi2Max")),
  muChi2LocalPositionMax_                (iConfig.getParameter<double>("muChi2LocalPositionMax")),
  muTrkKink_                             (iConfig.getParameter<double>("muTrkKink")),
  muValidFractionMin_                    (iConfig.getParameter<double>("muValidFractionMin")),
  muSegmentCompatibilityMin_             (iConfig.getParameter<std::vector<double>>("muSegmentCompatibilityMin")),
  mudBMax_                               (iConfig.getParameter<double>("mudBMax")),
  mudZMax_                               (iConfig.getParameter<double>("mudZMax")),
  tightMuNormalizedChi2Max_              (iConfig.getParameter<double>("tightMuNormalizedChi2Max")),
  tightMuNumberOfValidMuonHitsMin_       (iConfig.getParameter<int>("tightMuNumberOfValidMuonHitsMin")),
  tightMuNumberOfMatchedStationsMin_     (iConfig.getParameter<int>("tightMuNumberOfMatchedStationsMin")),
  tightMudBMax_                          (iConfig.getParameter<double>("tightMudBMax")),
  tightMudZMax_                          (iConfig.getParameter<double>("tightMudZMax")),
  tightMuNumberOfValidPixelHitsMin_      (iConfig.getParameter<int>("tightMuNumberOfValidPixelHitsMin")),
  tightMuTrackerLayersWithMeasurementMin_(iConfig.getParameter<int>("tightMuTrackerLayersWithMeasurementMin")),
  useMiniIsolation_                      (iConfig.getParameter<bool>("UseMiniIsolation")),
  electronEAValues_                      (iConfig.getParameter<std::vector<double>>("electronEAValues")),
  muonEAValues_                          (iConfig.getParameter<std::vector<double>>("muonEAValues")),
  debug_                                 (iConfig.getParameter<bool>("debug"))
{

  if(!hovere_constant_){
    eb_hovere_cut2_ = iConfig.getParameter<std::vector<double>>("eb_hovere_cut2");
    eb_hovere_cut3_ = iConfig.getParameter<std::vector<double>>("eb_hovere_cut3");
    ee_hovere_cut2_ = iConfig.getParameter<std::vector<double>>("ee_hovere_cut2");
    ee_hovere_cut3_ = iConfig.getParameter<std::vector<double>>("ee_hovere_cut3");
  }

  SUSYIsolationHelper.SetEAVectors(electronEAValues_, muonEAValues_);

  produces<std::vector<pat::Muon>>("IdMuon");
  produces<std::vector<bool>>("IdMuonMediumID");
  produces<std::vector<bool>>("IdMuonTightID");
  produces<std::vector<int>>("IdMuonCharge");
  produces<std::vector<double>>("IdMuonMTW");
  produces<std::vector<bool>>("IdMuonPassIso");
  produces<std::vector<pat::Muon>>("IdIsoMuon");
  produces<int>("IdIsoMuonNum");

  produces<std::vector<pat::Electron>>("IdElectron");
  produces<std::vector<bool>>("IdElectronMediumID");
  produces<std::vector<bool>>("IdElectronTightID");
  produces<std::vector<int>>("IdElectronCharge");
  produces<std::vector<double>>("IdElectronEnergyCorr");
  produces<std::vector<double>>("IdElectronTrkEnergyCorr");
  produces<std::vector<double>>("IdElectronMTW");
  produces<std::vector<bool>>("IdElectronPassIso");
  produces<std::vector<pat::Electron>>("IdIsoElectron");
  produces<int>("IdIsoElectronNum");
  
  produces<int>("");        
}


LeptonProducer::~LeptonProducer()
{
        
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
        
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void LeptonProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;

  if (debug_) edm::LogInfo("TreeMaker") << "LeptonProducer: Doing " << iEvent.eventAuxiliary().run() << ":" << iEvent.eventAuxiliary().luminosityBlock() 
                                        << ":" << iEvent.eventAuxiliary().event() << " ... ";

  auto isoElectrons = std::make_unique<std::vector<pat::Electron>>();
  auto idElectrons = std::make_unique<std::vector<pat::Electron>>();
  auto isoMuons = std::make_unique<std::vector<pat::Muon>>();
  auto idMuons = std::make_unique<std::vector<pat::Muon>>();
  
  auto MuonCharge = std::make_unique<std::vector<int>>();
  auto ElectronCharge = std::make_unique<std::vector<int>>();

  auto muIDMTW = std::make_unique<std::vector<double>>();
  auto muIDMedium = std::make_unique<std::vector<bool>>();
  auto muIDTight = std::make_unique<std::vector<bool>>();
  auto muIDPassIso = std::make_unique<std::vector<bool>>();
  auto elecIDEnergyCorr = std::make_unique<std::vector<double>>();
  auto elecIDTrkEnergyCorr = std::make_unique<std::vector<double>>();
  auto elecIDMTW = std::make_unique<std::vector<double>>();
  auto elecIDMedium = std::make_unique<std::vector<bool>>();
  auto elecIDTight = std::make_unique<std::vector<bool>>();
  auto elecIDPassIso = std::make_unique<std::vector<bool>>();

  int nmuons = 0;
  int nelectrons = 0;

  edm::Handle< edm::View<pat::MET> > MET;
  iEvent.getByToken(metTok_,MET); 
  reco::MET::LorentzVector metLorentz(0,0,0,0);
  if(MET.isValid() )
    {
      metLorentz=MET->at(0).p4();
    } else edm::LogWarning("TreeMaker")<<"LeptonProducer::MetTag Invalid Tag: "<<metTag_;

  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(PFCandTok_, pfcands);

  edm::Handle< double > rho_;
  iEvent.getByToken(RhoTok_, rho_); // Central rho recommended for SUSY
  double rho = rho_.isValid() ? (double)(*rho_) : 0;

  edm::Handle<reco::VertexCollection> vtx_h;
  iEvent.getByToken(PrimVtxTok_, vtx_h);
  edm::Handle<edm::View<pat::Muon> > muonHandle;
  iEvent.getByToken(MuonTok_, muonHandle);
  if(muonHandle.isValid())
    {
      for(const auto & aMu : *muonHandle)
        {
          if(aMu.pt()<minMuPt_ || std::abs(aMu.eta())>maxMuEta_) continue;

          if(MuonIDloose(aMu,vtx_h->at(0)))
            {
              idMuons->push_back(aMu);
              muIDMedium->push_back(MuonIDmedium(aMu,vtx_h->at(0)));
              muIDTight->push_back(MuonIDtight(aMu,vtx_h->at(0)));
              muIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),aMu.pt(),aMu.phi()));
              MuonCharge->push_back(aMu.charge());
              float ChgIso=aMu.pfIsolationR04().sumChargedHadronPt;
              float ChgPU=aMu.pfIsolationR04().sumPUPt;
              float NeuIso=aMu.pfIsolationR04().sumNeutralHadronEt+aMu.pfIsolationR04().sumPhotonEt;
              double dBIsoMu= (ChgIso+std::max(0., NeuIso-0.5*ChgPU))/aMu.pt();
              if(useMiniIsolation_) {
                double mt2_act = 0.0;
                SUSYIsolationHelper.GetMiniIsolation(pfcands, &aMu, SUSYIsolation::muon, rho, dBIsoMu, mt2_act);
              }
              muIDPassIso->push_back(dBIsoMu<muIsoValue_);
              if(muIDPassIso->back() and muIDMedium->back())
                {
                  nmuons++;
                  isoMuons->push_back(aMu);
                }
            }
        }
    }
    else edm::LogWarning("TreeMaker")<<"LeptonProducer::MuonTag Invalid Tag: "<<MuonTag_;


  edm::Handle<edm::View<pat::Electron> > eleHandle;
  iEvent.getByToken(ElecTok_, eleHandle);
  if(eleHandle.isValid())
    {
      for(const auto & aEle : *eleHandle)
        {
          if(std::abs(aEle.superCluster()->eta())>maxElecEta_ || aEle.pt()<minElecPt_) continue;
          const reco::Vertex vtx = vtx_h->at(0);

          double miniIso = 0.0;
          double mt2_act = 0.0;
          SUSYIsolationHelper.GetMiniIsolation(pfcands, &aEle, SUSYIsolation::electron, rho, miniIso, mt2_act);

          if(ElectronID(aEle, vtx, VETO, rho)) // check VETO id
            {
              // id passed
              idElectrons->push_back(aEle);
              elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),aEle.pt(),aEle.phi()));
              elecIDMedium->push_back(ElectronID(aEle, vtx, MEDIUM, rho));
              elecIDTight->push_back(ElectronID(aEle, vtx, TIGHT, rho));
              ElectronCharge->push_back(aEle.charge());
              elecIDEnergyCorr->push_back(aEle.hasUserFloat("ecalEnergyPostCorr") ? aEle.userFloat("ecalEnergyPostCorr") : -1);
              elecIDTrkEnergyCorr->push_back(aEle.hasUserFloat("ecalTrkEnergyPostCorr") ? aEle.userFloat("ecalTrkEnergyPostCorr") : -1);
              elecIDPassIso->push_back(miniIso<elecIsoValue_);
              if(elecIDPassIso->back())
                {
                  // iso passed
                  isoElectrons->push_back(aEle);
                  nelectrons++;
                }
            }
        }
    }
    else edm::LogWarning("TreeMaker")<<"LeptonProducer::ElectronTag Invalid Tag: "<<ElecTag_;

  auto htp1 = std::make_unique<int>(nmuons+nelectrons);
  auto htp2 = std::make_unique<int>(nmuons);
  auto htp3 = std::make_unique<int>(nelectrons);
  iEvent.put(std::move(htp1));
  iEvent.put(std::move(htp2),"IdIsoMuonNum");
  iEvent.put(std::move(htp3),"IdIsoElectronNum");
  iEvent.put(std::move(idMuons),"IdMuon");
  iEvent.put(std::move(isoMuons),"IdIsoMuon");

  iEvent.put(std::move(idElectrons),"IdElectron");
  iEvent.put(std::move(isoElectrons),"IdIsoElectron");

  iEvent.put(std::move(ElectronCharge),"IdElectronCharge");
  iEvent.put(std::move(MuonCharge),"IdMuonCharge");

  iEvent.put(std::move(muIDMTW),"IdMuonMTW");
  iEvent.put(std::move(muIDMedium),"IdMuonMediumID");
  iEvent.put(std::move(muIDTight),"IdMuonTightID");
  iEvent.put(std::move(muIDPassIso),"IdMuonPassIso");
  iEvent.put(std::move(elecIDMTW),"IdElectronMTW");
  iEvent.put(std::move(elecIDEnergyCorr),"IdElectronEnergyCorr");
  iEvent.put(std::move(elecIDTrkEnergyCorr),"IdElectronTrkEnergyCorr");
  iEvent.put(std::move(elecIDMedium),"IdElectronMediumID");
  iEvent.put(std::move(elecIDTight),"IdElectronTightID");
  iEvent.put(std::move(elecIDPassIso),"IdElectronPassIso");

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

float LeptonProducer::MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi) const
{
  if(std::isnan(lepPhi) || std::isnan(metPhi)) return 0.;
  float deltaPhi =TVector2::Phi_mpi_pi(lepPhi-metPhi);
  return sqrt(2*lepPt*metPt*(1-cos(deltaPhi)) );
}

bool LeptonProducer::MuonIDloose(const pat::Muon & muon, const reco::Vertex& vtx) const {
  return muon.isLooseMuon();
}

bool LeptonProducer::MuonIDmedium(const pat::Muon & muon, const reco::Vertex& vtx) const {
  //medium WP + dz/dxy cuts
  bool goodGlob      = muon.isGlobalMuon() && 
                       muon.globalTrack()->normalizedChi2() < muNormalizedChi2Max_ && 
                       muon.combinedQuality().chi2LocalPosition < muChi2LocalPositionMax_ && 
                       muon.combinedQuality().trkKink < muTrkKink_; 
  bool isMedium      = muon.isLooseMuon() && 
                       muon.innerTrack()->validFraction() > muValidFractionMin_ && 
                       muon.segmentCompatibility() > (goodGlob ? muSegmentCompatibilityMin_[0] : muSegmentCompatibilityMin_[1]);
  bool susyIP2DLoose = muon.dB() < mudBMax_ && std::abs(muon.muonBestTrack()->dz(vtx.position())) < mudZMax_;
  bool isMediumPlus  = isMedium && susyIP2DLoose;
  return isMediumPlus; 
}

bool LeptonProducer::MuonIDtight(const pat::Muon & muon, const reco::Vertex& vtx) const {
  //tight WP
  bool isTight = muon.isGlobalMuon() &&
                 muon.isPFMuon() &&
                 muon.globalTrack()->normalizedChi2() < tightMuNormalizedChi2Max_ &&
                 muon.globalTrack()->hitPattern().numberOfValidMuonHits() > tightMuNumberOfValidMuonHitsMin_ &&
                 muon.numberOfMatchedStations() > tightMuNumberOfMatchedStationsMin_ &&
                 muon.dB() < tightMudBMax_ &&
                 std::abs(muon.muonBestTrack()->dz(vtx.position())) < tightMudZMax_ &&
                 muon.innerTrack()->hitPattern().numberOfValidPixelHits() > tightMuNumberOfValidPixelHitsMin_ &&
                 muon.innerTrack()->hitPattern().trackerLayersWithMeasurement() > tightMuTrackerLayersWithMeasurementMin_;

  return isTight;
}

bool LeptonProducer::ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level, const double rho) const {
  // electron ID cuts
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
  double sieie = electron.full5x5_sigmaIetaIeta();
  bool convVeto = electron.passConversionVeto();
  int mhits = electron.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);
  double dEtaIn = (electron.superCluster().isNonnull() && electron.superCluster()->seed().isNonnull())
                  ? electron.deltaEtaSuperClusterTrackAtVtx() - electron.superCluster()->eta() + electron.superCluster()->seed()->eta()
                  : std::numeric_limits<double>::max();
  double dPhiIn  = electron.deltaPhiSuperClusterTrackAtVtx();
  double hoe   = electron.hadronicOverEm();
  double ooemoop = std::abs(1.0/electron.ecalEnergy() - electron.eSuperClusterOverP()/electron.ecalEnergy());
  double d0vtx = electron.gsfTrack()->dxy(vtx.position());
  double dzvtx = electron.gsfTrack()->dz(vtx.position());
  double scEnergy = electron.superCluster()->energy();
  bool hovere_pass = false;
  bool reqConvVeto[4] = {true, true, true, true};

  if (electron.isEB()) {
    hovere_pass = (hovere_constant_) ? eb_hovere_cut_[level] > hoe : (eb_hovere_cut_[level] + (eb_hovere_cut2_[level]/scEnergy) + (eb_hovere_cut3_[level]*rho/scEnergy)) > hoe;

    if (debug_) {
      edm::LogInfo("TreeMaker") << "LeptonProducer: (pt,eta,phi): (" << electron.pt() << "," << electron.eta() << "," << electron.phi() << ")\n"
                                << "\teb_deta_cut_[level] > std::abs(dEtaIn): " << (eb_deta_cut_[level] > std::abs(dEtaIn)) << "\n"
                                << "\teb_dphi_cut_[level] > std::abs(dPhiIn): " << (eb_dphi_cut_[level] > std::abs(dPhiIn)) << "\n"
                                << "\teb_ieta_cut_[level] > sieie: " << (eb_ieta_cut_[level] > sieie) << "\n"
                                << "\thovere_pass: " << hovere_pass << " = (" << hovere_constant_ << ") ? " << eb_hovere_cut_[level] << " > " << hoe << " : " << eb_hovere_cut_[level] << " + ("
                                << eb_hovere_cut2_[level] << "/" << scEnergy << ") + (" << eb_hovere_cut3_[level] <<"*" << rho << "/" << scEnergy << ") > " << hoe << "\n"
                                << "\teb_d0_cut_[level] > std::abs(d0vtx): " << (eb_d0_cut_[level] > std::abs(d0vtx)) << "\n"
                                << "\teb_dz_cut_[level] > std::abs(dzvtx): " << (eb_dz_cut_[level] > std::abs(dzvtx)) << "\n"
                                << "\teb_ooeminusoop_cut_[level] > std::abs(ooemoop): " << (eb_ooeminusoop_cut_[level] > std::abs(ooemoop)) << "\n"
                                << "\t(!reqConvVeto[level] || convVeto): " << (!reqConvVeto[level] || convVeto) << "\n"
                                << "\t(eb_misshits_cut_[level] >= mhits): " << (eb_misshits_cut_[level] >= mhits);
    }

    return eb_deta_cut_[level] > std::abs(dEtaIn)
      && eb_dphi_cut_[level] > std::abs(dPhiIn)
      && eb_ieta_cut_[level] > sieie
      && hovere_pass
      && eb_d0_cut_[level] > std::abs(d0vtx)
      && eb_dz_cut_[level] > std::abs(dzvtx)
      && eb_ooeminusoop_cut_[level] > std::abs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (eb_misshits_cut_[level] >= mhits);
  } else if (electron.isEE()) {
    hovere_pass = (hovere_constant_) ? ee_hovere_cut_[level] > hoe : (ee_hovere_cut_[level] + (ee_hovere_cut2_[level]/scEnergy) + (ee_hovere_cut3_[level]*rho/scEnergy)) > hoe;

    if (debug_) {
      edm::LogInfo("TreeMaker") << "LeptonProducer: (pt,eta,phi): (" << electron.pt() << "," << electron.eta() << "," << electron.phi() << ")\n"
                                << "\tee_deta_cut_[level] > std::abs(dEtaIn): " << (ee_deta_cut_[level] > std::abs(dEtaIn)) << "\n"
                                << "\tee_dphi_cut_[level] > std::abs(dPhiIn): " << (ee_dphi_cut_[level] > std::abs(dPhiIn)) << "\n"
                                << "\tee_ieta_cut_[level] > sieie: " << (ee_ieta_cut_[level] > sieie) << "\n"
                                << "\thovere_pass: " << hovere_pass << " = (" << hovere_constant_ << ") ? " << ee_hovere_cut_[level] << " > " << hoe << " : " << ee_hovere_cut_[level] << " + ("
                                << ee_hovere_cut2_[level] << "/" << scEnergy << ") + (" << ee_hovere_cut3_[level] <<"*" << rho << "/" << scEnergy << ") > " << hoe << "\n"
                                << "\tee_d0_cut_[level] > std::abs(d0vtx): " << (ee_d0_cut_[level] > std::abs(d0vtx)) << "\n"
                                << "\tee_dz_cut_[level] > std::abs(dzvtx): " << (ee_dz_cut_[level] > std::abs(dzvtx)) << "\n"
                                << "\tee_ooeminusoop_cut_[level] > std::abs(ooemoop): " << (ee_ooeminusoop_cut_[level] > std::abs(ooemoop)) << "\n"
                                << "\t(!reqConvVeto[level] || convVeto): " << (!reqConvVeto[level] || convVeto) << "\n"
                                << "\t(ee_misshits_cut_[level] >= mhits): " << (ee_misshits_cut_[level] >= mhits);
    }

    return ee_deta_cut_[level] > std::abs(dEtaIn)
      && ee_dphi_cut_[level] > std::abs(dPhiIn)
      && ee_ieta_cut_[level] > sieie
      && hovere_pass
      && ee_d0_cut_[level] > std::abs(d0vtx)
      && ee_dz_cut_[level] > std::abs(dzvtx)
      && ee_ooeminusoop_cut_[level] > std::abs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (ee_misshits_cut_[level] >= mhits);
  } else return false;

}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonProducer);
