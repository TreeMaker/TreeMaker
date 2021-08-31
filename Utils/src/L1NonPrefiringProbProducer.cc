// system include files
#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "TFile.h"
#include "TH2.h"
#include "TF1.h"

#include "TreeMaker/Utils/interface/EnergyFractionCalculator.h"

#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <cmath>

//based on: https://github.com/lathomas/cmssw/blob/L1Prefiring_9_4_9/L1Prefiring/EventWeightProducer/plugins/L1NonPrefiringProbProducer.cc

namespace {
   void dot(std::array<double,3>& a1, const std::array<double,3>& a2){
      for(unsigned i = 0; i < a1.size(); ++i){
         a1[i] *= a2[i];
      }
   }
}

class L1NonPrefiringProbProducer : public edm::global::EDProducer<> {
public:
  explicit L1NonPrefiringProbProducer(const edm::ParameterSet&);
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  std::array<double,3> getNonPrefiringRateECAL( double eta, double pt, TH2F * h_prefmap) const;
  std::array<double,3> getNonPrefiringRateMuon( double eta, double phi, double pt) const;
 
  edm::EDGetTokenT<std::vector< pat::Photon> > photons_token_; 
  edm::EDGetTokenT<std::vector< pat::Jet> > jets_token_;
  edm::EDGetTokenT<std::vector< pat::Muon> > muons_token_;

  TH2F* h_prefmap_photon; 
  TH2F* h_prefmap_jet;
  TF1* h_prefparam_muon_0p00to0p20;
  TF1* h_prefparam_muon_0p20to0p30;
  TF1* h_prefparam_muon_0p30to0p55;
  TF1* h_prefparam_muon_0p55to0p83;
  TF1* h_prefparam_muon_0p83to1p24;
  TF1* h_prefparam_muon_1p24to1p40;
  TF1* h_prefparam_muon_1p40to1p60;
  TF1* h_prefparam_muon_1p60to1p80;
  TF1* h_prefparam_muon_1p80to2p10;
  TF1* h_prefparam_muon_2p10to2p25;
  TF1* h_prefparam_muon_2p25to2p40;
  TF1* h_prefparam_muon_hotspot;
  std::string dataeraecal_;
  std::string dataeramuon_;
  bool useEMpt_;
  double prefiringRateSystUncECAL_;
  double prefiringRateSystUncMuon_;
  double jet_max_muon_fraction_;

};

L1NonPrefiringProbProducer::L1NonPrefiringProbProducer(const edm::ParameterSet& iConfig) :
  photons_token_(consumes<std::vector<pat::Photon>>(iConfig.getParameter<edm::InputTag>("ThePhotons"))),
  jets_token_(consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("TheJets"))),
  muons_token_(consumes<std::vector<pat::Muon>>(iConfig.getParameter<edm::InputTag>("TheMuons"))),
  dataeraecal_(iConfig.getParameter<std::string>("DataEraECAL")),
  dataeramuon_(iConfig.getParameter<std::string>("DataEraMuon")),
  useEMpt_(iConfig.getParameter<bool>("UseJetEMPt")),
  prefiringRateSystUncECAL_(iConfig.getParameter<double>("PrefiringRateSystematicUnctyECAL")),
  prefiringRateSystUncMuon_(iConfig.getParameter<double>("PrefiringRateSystematicUnctyMuon")),
  jet_max_muon_fraction_(iConfig.getParameter<double>("JetMaxMuonFraction"))
{
  std::string fnameecal =  iConfig.getParameter<std::string>("L1MapsECAL");
  TFile* file_ecalprefiringmaps = TFile::Open(fnameecal.c_str(),"read");

  std::string mapphotonfullname = "L1prefiring_photonptvseta_"+ dataeraecal_; 
  file_ecalprefiringmaps->ls();
  h_prefmap_photon = (TH2F*)file_ecalprefiringmaps->Get(mapphotonfullname.c_str());
  h_prefmap_photon->SetDirectory(0);

  std::string mapjetfullname = "L1prefiring_jet";
  mapjetfullname += (useEMpt_ ? "empt" : "pt");
  mapjetfullname += "vseta_" + dataeraecal_;
  h_prefmap_jet = (TH2F*)file_ecalprefiringmaps->Get(mapjetfullname.c_str());
  h_prefmap_jet->SetDirectory(0);
  file_ecalprefiringmaps->Close();

  std::string fnamemuon =  iConfig.getParameter<std::string>("L1ParamsMuon");
  TFile* file_muonprefiringparams = TFile::Open(fnamemuon.c_str(), "read");

  std::string mapmuonfullname = "L1prefiring_muonparam_HotSpot_" + dataeramuon_;
  h_prefparam_muon_hotspot = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_0.0To0.2_" + dataeramuon_;
  h_prefparam_muon_0p00to0p20 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_0.2To0.3_" + dataeramuon_;
  h_prefparam_muon_0p20to0p30 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_0.3To0.55_" + dataeramuon_;
  h_prefparam_muon_0p30to0p55 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_0.55To0.83_" + dataeramuon_;
  h_prefparam_muon_0p55to0p83 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_0.83To1.24_" + dataeramuon_;
  h_prefparam_muon_0p83to1p24 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_1.24To1.4_" + dataeramuon_;
  h_prefparam_muon_1p24to1p40 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_1.4To1.6_" + dataeramuon_;
  h_prefparam_muon_1p40to1p60 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_1.6To1.8_" + dataeramuon_;
  h_prefparam_muon_1p60to1p80 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_1.8To2.1_" + dataeramuon_;
  h_prefparam_muon_1p80to2p10 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_2.1To2.25_" + dataeramuon_;
  h_prefparam_muon_2p10to2p25 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  mapmuonfullname = "L1prefiring_muonparam_2.25To2.4_" + dataeramuon_;
  h_prefparam_muon_2p25to2p40 = (TF1*)file_muonprefiringparams->Get(mapmuonfullname.c_str());

  file_muonprefiringparams->Close();

  produces<double>( "NonPrefiringProb" );
  produces<double>( "NonPrefiringProbUp" );
  produces<double>( "NonPrefiringProbDown" );
  produces<double>( "NonPrefiringProbECAL" );
  produces<double>( "NonPrefiringProbECALUp" );
  produces<double>( "NonPrefiringProbECALDown" );
  produces<double>( "NonPrefiringProbMuon" );
  produces<double>( "NonPrefiringProbMuonUp" );
  produces<double>( "NonPrefiringProbMuonDown" );

}

void
L1NonPrefiringProbProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;

   //Photons
   edm::Handle< std::vector<pat::Photon> > thePhotons;
   iEvent.getByToken(photons_token_,thePhotons);
   
   //Jets
   edm::Handle< std::vector< pat::Jet> > theJets;
   iEvent.getByToken(jets_token_,theJets );
   
   //Muons
   edm::Handle< std::vector< pat::Muon> > theMuons;
   iEvent.getByToken(muons_token_,theMuons );

   //Probability for the event NOT to prefire, computed with the prefiring maps per object. 
   //Up and down values correspond to the resulting value when shifting up/down all prefiring rates in prefiring maps.
   std::array<double,3> NonPrefiringProbs = {{1.,1.,1.}}; //0: central, 1: up, 2: down
   std::array<double,3> NonPrefiringProbsECAL = {{1.,1.,1.}}; //0: central, 1: up, 2: down
   std::array<double,3> NonPrefiringProbsMuon = {{1.,1.,1.}}; //0: central, 1: up, 2: down

   //Start by applying the prefiring maps to photons in the affected regions.
   std::vector<pat::Photon> affectedphotons;
   for(const auto& photon : *(thePhotons.product())){
      double pt = photon.pt();
      double eta = photon.eta();
      if(pt < 20.0 or abs(eta) < 2. or abs(eta) > 3.) continue;
      affectedphotons.push_back(photon);
      const auto& nonprefiringprob_gam = getNonPrefiringRateECAL(eta, pt, h_prefmap_photon);
      dot(NonPrefiringProbs,nonprefiringprob_gam);
   }

   //Now apply the prefiring maps to jets in the affected regions. 
   for(const auto& jet : *(theJets.product())){
      double pt = jet.pt();
      double eta = jet.eta();
      if(pt < 20.0 or abs(eta) < 2. or abs(eta) > 3.) continue;
      
      //Loop over photons to remove overlap
      std::array<double,3> NonPrefiringProbOverlap = {{1.,1.,1.}};
      bool overlap = false;
      for(const auto& photon: affectedphotons){
         double dR = reco::deltaR(jet,photon);
         if(dR > 0.4) continue;
         overlap = true;
         const auto& nonprefiringprob_gam = getNonPrefiringRateECAL(photon.eta(), photon.pt(), h_prefmap_photon);
         dot(NonPrefiringProbOverlap,nonprefiringprob_gam);
      }

      EnergyFractionCalculator efc(jet);
      double ptem = pt*(efc.neutralEmEnergyFraction() + efc.chargedEmEnergyFraction());
      const auto& nonprefiringprob_jet = getNonPrefiringRateECAL(eta, useEMpt_ ? ptem : pt, h_prefmap_jet);
      
      //If there are no overlapping photons, just multiply by the jet non prefiring rate
      if(!overlap) dot(NonPrefiringProbs,nonprefiringprob_jet);
      else {
         for(unsigned i = 0; i < NonPrefiringProbs.size(); ++i){
            //If overlapping photons have a non prefiring rate larger than the jet, then replace these weights by the jet one
            if(NonPrefiringProbOverlap[i] > nonprefiringprob_jet[i]){
               if(NonPrefiringProbOverlap[i] > 0.) NonPrefiringProbs[i] *= nonprefiringprob_jet[i]/NonPrefiringProbOverlap[i];
               else NonPrefiringProbs[i] = 0.;
            }
            //If overlapping photons have a non prefiring rate smaller than the jet, don't consider the jet in the event weight
         }
      }
   }

   for(const auto& muon : *(theMuons.product())){
      double pt = muon.pt();
      double phi = muon.phi();
      double eta = muon.eta();
 
      // remove low quality muons that would not prefire the L1 trigger
      if (pt < 5 || !muon.isLooseMuon())
         continue;

      const auto& nonprefiringprob_mu = getNonPrefiringRateMuon(eta, phi, pt);

      dot(NonPrefiringProbsMuon, nonprefiringprob_mu);
      dot(NonPrefiringProbs, nonprefiringprob_mu);
   }

   auto NonPrefiringProb = std::make_unique <double> ( NonPrefiringProbs[0]);
   auto NonPrefiringProbUp = std::make_unique <double> ( NonPrefiringProbs[1]);
   auto NonPrefiringProbDown = std::make_unique <double> ( NonPrefiringProbs[2]);
   auto NonPrefiringProbECAL = std::make_unique <double> ( NonPrefiringProbsECAL[0]);
   auto NonPrefiringProbECALUp = std::make_unique <double> ( NonPrefiringProbsECAL[1]);
   auto NonPrefiringProbECALDown = std::make_unique <double> ( NonPrefiringProbsECAL[2]);
   auto NonPrefiringProbMuon = std::make_unique <double> ( NonPrefiringProbsMuon[0]);
   auto NonPrefiringProbMuonUp = std::make_unique <double> ( NonPrefiringProbsMuon[1]);
   auto NonPrefiringProbMuonDown = std::make_unique <double> ( NonPrefiringProbsMuon[2]);

   iEvent.put( std::move(NonPrefiringProb), "NonPrefiringProb" );
   iEvent.put( std::move(NonPrefiringProbUp), "NonPrefiringProbUp" );
   iEvent.put( std::move(NonPrefiringProbDown), "NonPrefiringProbDown" );
   iEvent.put( std::move(NonPrefiringProbECAL), "NonPrefiringProbECAL" );
   iEvent.put( std::move(NonPrefiringProbECALUp), "NonPrefiringProbECALUp" );
   iEvent.put( std::move(NonPrefiringProbECALDown), "NonPrefiringProbECALDown" );
   iEvent.put( std::move(NonPrefiringProbMuon), "NonPrefiringProbMuon" );
   iEvent.put( std::move(NonPrefiringProbMuonUp), "NonPrefiringProbMuonUp" );
   iEvent.put( std::move(NonPrefiringProbMuonDown), "NonPrefiringProbMuonDown" );
}

std::array<double,3> L1NonPrefiringProbProducer::getNonPrefiringRateECAL( double eta, double pt, TH2F * h_prefmap) const {
   if(h_prefmap==0) return {{0.,0.,0.}};
   
   //Check pt is not above map overflow
   int nbinsy = h_prefmap->GetNbinsY();
   double maxy = h_prefmap->GetYaxis()->GetBinLowEdge(nbinsy+1);
   if(pt>=maxy) pt = maxy-0.01;
   int thebin = h_prefmap->FindBin(eta,pt);
   
   double prefrate = h_prefmap->GetBinContent(thebin);
   double preferr = h_prefmap->GetBinError(thebin);
   double prefrate_up = std::min(std::max(prefrate + preferr, (1. + prefiringRateSystUncECAL_)*prefrate),1.);
   double prefrate_dn = std::max(std::min(prefrate - preferr, (1. - prefiringRateSystUncECAL_)*prefrate),0.);
   
   return {{1.-prefrate, 1.-prefrate_up, 1.-prefrate_dn}};
}

std::array<double,3> L1NonPrefiringProbProducer::getNonPrefiringRateMuon( double eta, double phi, double pt) const {

   double abseta = abs(eta);
   double prefrate = 0.0; double preferr = 0.0;
   if ((dataeramuon_.find("2016") != std::string::npos) && (eta > 1.24 && eta < 1.6) && (phi > 2.44346 && phi < 2.79253)){
      prefrate = h_prefparam_muon_hotspot->Eval(pt);
      preferr = h_prefparam_muon_hotspot->GetParError(2); 
   } else if (abseta < 0.2) {
      prefrate = h_prefparam_muon_0p00to0p20->Eval(pt);
      preferr = h_prefparam_muon_0p00to0p20->GetParError(2);
   } else if (abseta < 0.3) {
      prefrate = h_prefparam_muon_0p20to0p30->Eval(pt);
      preferr = h_prefparam_muon_0p20to0p30->GetParError(2);
   } else if (abseta < 0.55) {
      prefrate = h_prefparam_muon_0p30to0p55->Eval(pt);
      preferr = h_prefparam_muon_0p30to0p55->GetParError(2);
   } else if (abseta < 0.83) {
      prefrate = h_prefparam_muon_0p55to0p83->Eval(pt);
      preferr = h_prefparam_muon_0p55to0p83->GetParError(2);
   } else if (abseta < 1.24) {
      prefrate = h_prefparam_muon_0p83to1p24->Eval(pt);
      preferr = h_prefparam_muon_0p83to1p24->GetParError(2);
   } else if (abseta < 1.4) {
      prefrate = h_prefparam_muon_1p24to1p40->Eval(pt);
      preferr = h_prefparam_muon_1p24to1p40->GetParError(2);
   } else if (abseta < 1.6) {
      prefrate = h_prefparam_muon_1p40to1p60->Eval(pt);
      preferr = h_prefparam_muon_1p40to1p60->GetParError(2);
   } else if (abseta < 1.8) {
      prefrate = h_prefparam_muon_1p60to1p80->Eval(pt);
      preferr = h_prefparam_muon_1p60to1p80->GetParError(2);
   } else if (abseta < 2.1) {
      prefrate = h_prefparam_muon_1p80to2p10->Eval(pt);
      preferr = h_prefparam_muon_1p80to2p10->GetParError(2);
   } else if (abseta < 2.25) {
      prefrate = h_prefparam_muon_2p10to2p25->Eval(pt);
      preferr = h_prefparam_muon_2p10to2p25->GetParError(2);
   } else if (abseta < 2.4) {
      prefrate = h_prefparam_muon_2p25to2p40->Eval(pt);
      preferr = h_prefparam_muon_2p25to2p40->GetParError(2);
   } else {
      return {{0.,0.,0.}};
   }

   double prefrate_up = std::min(std::max(prefrate + preferr, (1. + prefiringRateSystUncMuon_)*prefrate),1.);
   double prefrate_dn = std::max(std::min(prefrate - preferr, (1. - prefiringRateSystUncMuon_)*prefrate),0.);
   
   return {{1.-prefrate, 1.-prefrate_up, 1.-prefrate_dn}};
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
L1NonPrefiringProbProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  
  desc.add<edm::InputTag>("ThePhotons", edm::InputTag("slimmedPhotons"));
  desc.add<edm::InputTag>("TheJets", edm::InputTag("slimmedJets"));
  desc.add<edm::InputTag>("TheMuons", edm::InputTag("slimmedMuons"));
  desc.add<double>("JetMaxMuonFraction", 0.5);
  desc.add<std::string>("L1MapsECAL", "L1PrefiringMaps.root");
  desc.add<std::string>("L1ParamsMuon", "L1MuonPrefiringParameterizations.root");
  desc.add<std::string>("DataEraECAL", "UL2017BtoF");
  desc.add<std::string>("DataEraMuon", "20172018");
  desc.add<bool>("UseJetEMPt", true);
  desc.add<double>("PrefiringRateSystematicUnctyECAL",0.2);
  desc.add<double>("PrefiringRateSystematicUnctyMuon",0.2);
  descriptions.add("L1NonPrefiringProbProducer",desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(L1NonPrefiringProbProducer);
