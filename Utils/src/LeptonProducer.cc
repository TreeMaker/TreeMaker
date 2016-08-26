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
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

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



class LeptonProducer : public edm::EDProducer {
  enum elecIDLevel {VETO, LOOSE, MEDIUM, TIGHT};
public:
  explicit LeptonProducer(const edm::ParameterSet&);
  ~LeptonProducer();
        
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  float MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi);
  bool MuonID(const pat::Muon & muon, const reco::Vertex& vtx);
  bool ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level);
        
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
        
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag MuonTag_, ElecTag_, PrimVtxTag_, metTag_, PFCandTag_, RhoTag_;
  edm::EDGetTokenT<edm::View<pat::Muon>> MuonTok_;
  edm::EDGetTokenT<edm::View<pat::Electron>> ElecTok_;
  edm::EDGetTokenT<reco::VertexCollection> PrimVtxTok_;
  edm::EDGetTokenT<edm::View<pat::MET>> metTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> PFCandTok_;
  edm::EDGetTokenT<double> RhoTok_;
  double minElecPt_, maxElecEta_, minMuPt_, maxMuEta_;
  bool useMiniIsolation_;
  double muIsoValue_, elecIsoValue_;
  SUSYIsolation SUSYIsolationHelper;
        
        
  // ----------member data ---------------------------


};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
LeptonProducer::LeptonProducer(const edm::ParameterSet& iConfig)
{
  //register your product
  MuonTag_                                 =         iConfig.getParameter<edm::InputTag >("MuonTag");
  ElecTag_                                 =         iConfig.getParameter<edm::InputTag >("ElectronTag");
  PrimVtxTag_=iConfig.getParameter<edm::InputTag>("PrimaryVertex");
  minElecPt_=iConfig.getParameter<double>          ("minElecPt");
  maxElecEta_=iConfig.getParameter<double>          ("maxElecEta");
  minMuPt_=iConfig.getParameter<double>          ("minMuPt");
  maxMuEta_=iConfig.getParameter<double>          ("maxMuEta");
  useMiniIsolation_ = iConfig.getParameter<bool>("UseMiniIsolation");
  muIsoValue_=iConfig.getParameter<double>          ("muIsoValue");
  elecIsoValue_=iConfig.getParameter<double>          ("elecIsoValue");
  metTag_   = iConfig.getParameter<edm::InputTag> ("METTag");
  RhoTag_ = edm::InputTag("fixedGridRhoFastjetCentralNeutral");
  PFCandTag_ = edm::InputTag("packedPFCandidates");
  
  MuonTok_ = consumes<edm::View<pat::Muon>>(MuonTag_);
  ElecTok_ = consumes<edm::View<pat::Electron>>(ElecTag_);
  PrimVtxTok_ = consumes<reco::VertexCollection>(PrimVtxTag_);
  metTok_ = consumes<edm::View<pat::MET>>(metTag_);
  PFCandTok_ = consumes<pat::PackedCandidateCollection>(PFCandTag_);
  RhoTok_ = consumes<double>(RhoTag_);
        
  const std::string string1("IdMuon");
  produces<std::vector<pat::Muon> > (string1).setBranchAlias(string1);
  const std::string string2("IdIsoMuon");
  produces<std::vector<pat::Muon> > (string2).setBranchAlias(string2);
  produces<std::vector<int> >("MuonCharge");
  //   const std::string string2b("IdIsoMuon_DeltaR");
  //   produces<std::vector<double> > (string2b).setBranchAlias(string2b);
  const std::string string3("IdElectron");
  produces<std::vector<pat::Electron> > (string3).setBranchAlias(string3);
  const std::string string4("IdIsoElectron");
  produces<std::vector<pat::Electron> > (string4).setBranchAlias(string4);
  produces<std::vector<int> >("ElectronCharge");
  //   const std::string string4b("IdIsoElectron_DeltaR");
  //   produces<std::vector<double> > (string4b).setBranchAlias(string4b);
  produces<std::vector<double> >("MuIDMTW");
  produces<std::vector<double> >("MuIDIsoMTW");
  produces<std::vector<double> >("ElecIDMTW");
  produces<std::vector<double> >("ElecIDIsoMTW");
  produces<std::vector<bool> >("ElecIDMedium");
  produces<std::vector<bool> >("ElecIDIsoMedium");
  
  // produces<std::vector<double> >("MuIDActRA2");
  // produces<std::vector<double> >("MuIDIsoActRA2");
  // produces<std::vector<double> >("MuIDActMT2");
  // produces<std::vector<double> >("MuIDIsoActMT2");

  // produces<std::vector<double> >("ElecIDActRA2");
  // produces<std::vector<double> >("ElecIDIsoActRA2");
  // produces<std::vector<double> >("ElecIDActMT2");
  // produces<std::vector<double> >("ElecIDIsoActMT2");
  
  produces<int>("");
  /* Examples
   *   produces<ExampleData2>();
   *
   *   //if do put with a label
   *   produces<ExampleData2>("label");
   *
   *   //if you want to put into the Run
   *   produces<ExampleData2,InRun>();
   */
  //now do what ever other initialization is needed
        
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
void LeptonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //  std::cout<<"Running LeptonProducer"<<std::endl;
 
  using namespace edm;
        
  auto MuonCharge = std::make_unique<std::vector<int>>();
  auto ElectronCharge = std::make_unique<std::vector<int>>();
        
  auto muIDMTW = std::make_unique<std::vector<double>>();
  auto muIDIsoMTW = std::make_unique<std::vector<double>>();
  auto elecIDMTW = std::make_unique<std::vector<double>>();
  auto elecIDIsoMTW = std::make_unique<std::vector<double>>();
  auto elecIDMedium = std::make_unique<std::vector<bool>>();
  auto elecIDIsoMedium = std::make_unique<std::vector<bool>>();
  // auto muIDActRA2 = std::make_unique<std::vector<double>>();
  // auto muIDIsoActRA2 = std::make_unique<std::vector<double>>();
  // auto muIDActMT2 = std::make_unique<std::vector<double>>();
  // auto muIDIsoActMT2 = std::make_unique<std::vector<double>>();

  // auto elecIDActRA2 = std::make_unique<std::vector<double>>();
  // auto elecIDIsoActRA2 = std::make_unique<std::vector<double>>();
  // auto elecIDActMT2 = std::make_unique<std::vector<double>>();
  // auto elecIDIsoActMT2 = std::make_unique<std::vector<double>>();

  edm::Handle< edm::View<pat::MET> > MET;
  iEvent.getByToken(metTok_,MET); 
  reco::MET::LorentzVector metLorentz(0,0,0,0);
  if(MET.isValid() )
    {
      metLorentz=MET->at(0).p4();
    } else std::cout<<"LeptonProducer::MetTag Invalid Tag: "<<metTag_.label()<<std::endl;


  int Leptons=0;
  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(PFCandTok_, pfcands);

  edm::Handle< double > rho_;
  iEvent.getByToken(RhoTok_, rho_); // Central rho recommended for SUSY
  double rho = *rho_;
        
  std::vector<pat::Electron> isoElectrons_, idElectrons_;
  std::vector<pat::Muon> isoMuons_, idMuons_;
  edm::Handle<reco::VertexCollection> vtx_h;
  iEvent.getByToken(PrimVtxTok_, vtx_h);
  edm::Handle<edm::View<pat::Muon> > muonHandle;
  iEvent.getByToken(MuonTok_, muonHandle);
  if(muonHandle.isValid())
    {
      for(unsigned int m=0; m<muonHandle->size(); ++m)
        {
          if(muonHandle->at(m).pt()<minMuPt_ || fabs(muonHandle->at(m).eta())>maxMuEta_) continue;
                        
          if(MuonID(muonHandle->at(m),vtx_h->at(0)))
            {
              idMuons_.push_back(muonHandle->at(m));
              muIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi()));
              float ChgIso=muonHandle->at(m).pfIsolationR04().sumChargedHadronPt;
              float ChgPU=muonHandle->at(m).pfIsolationR04().sumPUPt;
              float NeuIso=muonHandle->at(m).pfIsolationR04().sumNeutralHadronEt+muonHandle->at(m).pfIsolationR04().sumPhotonEt;
              double dBIsoMu= (ChgIso+std::max(0., NeuIso-0.5*ChgPU))/muonHandle->at(m).pt();
              if(useMiniIsolation_) {
                double mt2_act = 0.0;
                SUSYIsolationHelper.GetMiniIsolation(pfcands, &muonHandle->at(m), SUSYIsolation::muon, rho, dBIsoMu, mt2_act);
              }
              if(dBIsoMu<muIsoValue_)
                {
                  Leptons++;
                  isoMuons_.push_back(muonHandle->at(m));
                  muIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi()));
                  //        std::cout<<"muIDIsoMTW: "<<MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi())<<"\n";
                  MuonCharge->push_back(muonHandle->at(m).charge());
                }
            }
        }
    }


  edm::Handle<edm::View<pat::Electron> > eleHandle;
  iEvent.getByToken(ElecTok_, eleHandle);
  if(eleHandle.isValid())
    {
      for(unsigned int e=0; e<eleHandle->size(); ++e)
        {
          if(fabs(eleHandle->at(e).superCluster()->eta())>maxElecEta_ ||eleHandle->at(e).pt()<minElecPt_)continue;
          const pat::Electron aEle = eleHandle->at(e);
          const reco::Vertex vtx = vtx_h->at(0);

          double miniIso = 0.0;
          double mt2_act = 0.0;
          SUSYIsolationHelper.GetMiniIsolation(pfcands, &aEle, SUSYIsolation::electron, rho, miniIso, mt2_act);

          if(ElectronID(aEle, vtx, VETO)) // check VETO id
            {
              // id passed
              idElectrons_.push_back(eleHandle->at(e));
              elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
              elecIDMedium->push_back(ElectronID(aEle, vtx, MEDIUM));
              if(miniIso<elecIsoValue_)
                {
                  // iso passed
                  isoElectrons_.push_back(eleHandle->at(e));
                  elecIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
                  elecIDIsoMedium->push_back(ElectronID(aEle, vtx, MEDIUM));
                  Leptons++;
                  ElectronCharge->push_back(eleHandle->at(e).charge());
                }
            }
        }
    }
  const std::string string1("IdMuon");
  const std::string string2("IdIsoMuon");
  const std::string string3("IdElectron");
  const std::string string4("IdIsoElectron");
        
  auto htp = std::make_unique<int>(Leptons);
  iEvent.put(std::move(htp));
  auto htp1 = std::make_unique<std::vector<pat::Muon>>(idMuons_);
  iEvent.put(std::move(htp1),string1);
  auto htp2 = std::make_unique<std::vector<pat::Muon>>(isoMuons_);
  iEvent.put(std::move(htp2),string2);
        
  auto htp3 = std::make_unique<std::vector<pat::Electron>>(idElectrons_);
  iEvent.put(std::move(htp3),string3);
  auto htp4 = std::make_unique<std::vector<pat::Electron>>(isoElectrons_);
  iEvent.put(std::move(htp4),string4);
        
  iEvent.put(std::move(ElectronCharge),"ElectronCharge");
  iEvent.put(std::move(MuonCharge),"MuonCharge");
        
  iEvent.put(std::move(muIDMTW),"MuIDMTW");
  iEvent.put(std::move(muIDIsoMTW),"MuIDIsoMTW");
  iEvent.put(std::move(elecIDMTW),"ElecIDMTW");
  iEvent.put(std::move(elecIDIsoMTW),"ElecIDIsoMTW");
  iEvent.put(std::move(elecIDMedium),"ElecIDMedium");
  iEvent.put(std::move(elecIDIsoMedium),"ElecIDIsoMedium");
}

// ------------ method called once each job just before starting event loop  ------------
void
LeptonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LeptonProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
LeptonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
LeptonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
LeptonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
LeptonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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

float LeptonProducer::MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi)
{
  if(std::isnan(lepPhi) || std::isnan(metPhi)) return 0.;
  float deltaPhi =TVector2::Phi_mpi_pi(lepPhi-metPhi);
  return sqrt(2*lepPt*metPt*(1-cos(deltaPhi)) );
}

bool LeptonProducer::MuonID(const pat::Muon & muon, const reco::Vertex& vtx){
  //tight WP
  //return muon.isTightMuon(vtx);
        
  //medium WP + dz/dxy cuts
  bool goodGlob = muon.isGlobalMuon() && 
                  muon.globalTrack()->normalizedChi2() < 3 && 
                  muon.combinedQuality().chi2LocalPosition < 12 && 
                  muon.combinedQuality().trkKink < 20; 
  bool isMedium = muon.isLooseMuon() && 
                  muon.innerTrack()->validFraction() > 0.49 && 
                  muon.segmentCompatibility() > (goodGlob ? 0.303 : 0.451);
  bool isMediumPlus = isMedium && muon.dB() < 0.2 && fabs(muon.muonBestTrack()->dz(vtx.position())) < 0.5;
  return isMediumPlus; 
}

bool LeptonProducer::ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level) {
  // electron ID cuts, updated for Spring15 25ns MC and Run2015C-D data 
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2

  // barrel electrons
  double eb_ieta_cut[4] = {0.0114, 0.0103, 0.0101, 0.0101};
  double eb_deta_cut[4] = {0.0152, 0.0105, 0.0103, 0.00926};
  double eb_dphi_cut[4] = {0.216, 0.115, 0.0336, 0.0336};
  double eb_hovere_cut[4] = {0.181, 0.104, 0.0876, 0.0597};
  double eb_ooeminusoop_cut[4] = {0.207, 0.102, 0.0174, 0.012};
  double eb_d0_cut[4] = {0.0564, 0.0261, 0.0118, 0.0111};
  double eb_dz_cut[4] = {0.472, 0.41, 0.373, 0.0466};
  int eb_misshits_cut[4] = {2, 2, 2, 2};

  // endcap electrons
  double ee_ieta_cut[4] = {0.0352, 0.0301, 0.0283, 0.0279};
  double ee_deta_cut[4] = {0.0113, 0.00814, 0.00733, 0.00724};
  double ee_dphi_cut[4] = {0.237, 0.182, 0.114, 0.0918};
  double ee_hovere_cut[4] = {0.116, 0.0897, 0.0678, 0.0615};
  double ee_ooeminusoop_cut[4] = {0.174, 0.126, 0.0898, 0.00999};
  double ee_d0_cut[4] = {0.222, 0.118, 0.0739, 0.0351};
  double ee_dz_cut[4] = {0.921, 0.822, 0.602, 0.417};
  int ee_misshits_cut[4] = {3, 1, 1, 1};

  // common
  bool reqConvVeto[4] = {true, true, true, true};

  double sieie = electron.full5x5_sigmaIetaIeta();
  bool convVeto = electron.passConversionVeto();
  int mhits = electron.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);;
  double dEtaIn  = electron.deltaEtaSuperClusterTrackAtVtx();
  double dPhiIn  = electron.deltaPhiSuperClusterTrackAtVtx();
  double hoe   = electron.hadronicOverEm();
  double ooemoop = fabs(1.0/electron.ecalEnergy() - electron.eSuperClusterOverP()/electron.ecalEnergy());
  double d0vtx = electron.gsfTrack()->dxy(vtx.position());
  double dzvtx = electron.gsfTrack()->dz(vtx.position());

  if (electron.isEB()) {
    return eb_deta_cut[level] > fabs(dEtaIn)
      && eb_dphi_cut[level] > fabs(dPhiIn)
      && eb_ieta_cut[level] > sieie
      && eb_hovere_cut[level] > hoe
      && eb_d0_cut[level] > fabs(d0vtx)
      && eb_dz_cut[level] > fabs(dzvtx)
      && eb_ooeminusoop_cut[level] > fabs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (eb_misshits_cut[level] >= mhits);
  } else if (electron.isEE()) {
    return ee_deta_cut[level] > fabs(dEtaIn)
      && ee_dphi_cut[level] > fabs(dPhiIn)
      && ee_ieta_cut[level] > sieie
      && ee_hovere_cut[level] > hoe
      && ee_d0_cut[level] > fabs(d0vtx)
      && ee_dz_cut[level] > fabs(dzvtx)
      && ee_ooeminusoop_cut[level] > fabs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (ee_misshits_cut[level] >= mhits);
  } else return false;

}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonProducer);
