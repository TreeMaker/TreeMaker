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
#include "TFile.h"
#include "TH2.h"

#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <cmath>

//based on: https://github.com/lathomas/cmssw/blob/L1Prefiring_9_4_9/L1Prefiring/EventWeightProducer/plugins/L1ECALNonPrefiringProbProducer.cc

namespace {
   void dot(std::array<double,3>& a1, const std::array<double,3>& a2){
      for(unsigned i = 0; i < a1.size(); ++i){
         a1[i] *= a2[i];
      }
   }
}

class L1ECALNonPrefiringProbProducer : public edm::global::EDProducer<> {
public:
  explicit L1ECALNonPrefiringProbProducer(const edm::ParameterSet&);
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  std::array<double,3> getNonPrefiringRate( double eta, double pt, TH2F * h_prefmap) const;
  
  edm::EDGetTokenT<std::vector< pat::Photon> >  photons_token_; 
  edm::EDGetTokenT<std::vector< pat::Jet> > jets_token_;

  TH2F* h_prefmap_photon; 
  TH2F* h_prefmap_jet;
  std::string dataera_;
  bool useEMpt_;
  double prefiringRateSystUnc_;
};

L1ECALNonPrefiringProbProducer::L1ECALNonPrefiringProbProducer(const edm::ParameterSet& iConfig) :
  photons_token_(consumes<std::vector<pat::Photon>>(iConfig.getParameter<edm::InputTag>("ThePhotons"))),
  jets_token_(consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("TheJets"))),
  dataera_(iConfig.getParameter<std::string>("DataEra")),
  useEMpt_(iConfig.getParameter<bool>("UseJetEMPt")),
  prefiringRateSystUnc_(iConfig.getParameter<double>("PrefiringRateSystematicUncty"))

{
  std::string fname =  iConfig.getParameter<std::string>("L1Maps");
  TFile* file_prefiringmaps = TFile::Open(fname.c_str(),"read");

  std::string mapphotonfullname = "L1prefiring_photonptvseta_"+ dataera_; 
  h_prefmap_photon = (TH2F*)file_prefiringmaps->Get(mapphotonfullname.c_str());
  h_prefmap_photon->SetDirectory(0);

  std::string mapjetfullname = "L1prefiring_jet";
  mapjetfullname += (useEMpt_ ? "empt" : "pt");
  mapjetfullname += "vseta_" + dataera_;
  h_prefmap_jet = (TH2F*)file_prefiringmaps->Get(mapjetfullname.c_str());
  h_prefmap_jet->SetDirectory(0);
  file_prefiringmaps->Close();
  
  produces<double>( "NonPrefiringProb" );
  produces<double>( "NonPrefiringProbUp" );
  produces<double>( "NonPrefiringProbDown" );
}

void
L1ECALNonPrefiringProbProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;

   //Photons
   edm::Handle< std::vector<pat::Photon> > thePhotons;
   iEvent.getByToken(photons_token_,thePhotons);
   
   //Jets
   edm::Handle< std::vector< pat::Jet> > theJets;
   iEvent.getByToken(jets_token_,theJets );
   
   //Probability for the event NOT to prefire, computed with the prefiring maps per object. 
   //Up and down values correspond to the resulting value when shifting up/down all prefiring rates in prefiring maps.
   std::array<double,3> NonPrefiringProbs = {{1.,1.,1.}}; //0: central, 1: up, 2: down

   //Start by applying the prefiring maps to photons in the affected regions.
   std::vector<pat::Photon> affectedphotons;
   for(const auto& photon : *(thePhotons.product())){
      double pt = photon.pt();
      double eta = photon.eta();
      if(pt < 2.0 or abs(eta) < 2. or abs(eta) > 3.) continue;
      affectedphotons.push_back(photon);
      const auto& nonprefiringprob_gam = getNonPrefiringRate(eta, pt, h_prefmap_photon);
      dot(NonPrefiringProbs,nonprefiringprob_gam);
   }

   //Now apply the prefiring maps to jets in the affected regions. 
   for(const auto& jet : *(theJets.product())){
      double pt = jet.pt();
      double eta = jet.eta();
      if(pt < 2.0 or abs(eta) < 2. or abs(eta) > 3.) continue;
      
      //Loop over photons to remove overlap
      std::array<double,3> NonPrefiringProbOverlap = {{1.,1.,1.}};
      bool overlap = false;
      for(const auto& photon: affectedphotons){
         double dR = reco::deltaR(jet,photon);
         if(dR > 0.4) continue;
         overlap = true;
         const auto& nonprefiringprob_gam = getNonPrefiringRate(photon.eta(), photon.pt(), h_prefmap_photon);
         dot(NonPrefiringProbOverlap,nonprefiringprob_gam);
      }
      
      double ptem = pt*(jet.neutralEmEnergyFraction() + jet.chargedEmEnergyFraction());
      const auto& nonprefiringprob_jet = getNonPrefiringRate(eta, useEMpt_ ? ptem : pt, h_prefmap_jet);
      
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

   auto NonPrefiringProb = std::make_unique <double> ( NonPrefiringProbs[0]);
   auto NonPrefiringProbUp = std::make_unique <double> ( NonPrefiringProbs[1]);
   auto NonPrefiringProbDown = std::make_unique <double> ( NonPrefiringProbs[2]);
   iEvent.put( std::move(NonPrefiringProb), "NonPrefiringProb" );
   iEvent.put( std::move(NonPrefiringProbUp), "NonPrefiringProbUp" );
   iEvent.put( std::move(NonPrefiringProbDown), "NonPrefiringProbDown" );
}

std::array<double,3> L1ECALNonPrefiringProbProducer::getNonPrefiringRate( double eta, double pt, TH2F * h_prefmap) const {
   if(h_prefmap==0) return {{0.,0.,0.}};
   
   //Check pt is not above map overflow
   int nbinsy = h_prefmap->GetNbinsY();
   double maxy = h_prefmap->GetYaxis()->GetBinLowEdge(nbinsy+1);
   if(pt>=maxy) pt = maxy-0.01;
   int thebin = h_prefmap->FindBin(eta,pt);
   
   double prefrate = h_prefmap->GetBinContent(thebin);
   double preferr = h_prefmap->GetBinError(thebin);
   double prefrate_up = std::min(std::max(prefrate + preferr, (1. + prefiringRateSystUnc_)*prefrate),1.);
   double prefrate_dn = std::max(std::min(prefrate - preferr, (1. - prefiringRateSystUnc_)*prefrate),0.);
   
   return {{1.-prefrate, 1.-prefrate_up, 1.-prefrate_dn}};
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
L1ECALNonPrefiringProbProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  
  desc.add<edm::InputTag>("ThePhotons", edm::InputTag("slimmedPhotons"));
  desc.add<edm::InputTag>("TheJets", edm::InputTag("slimmedJets"));
  desc.add<std::string>("L1Maps", "L1PrefiringMaps_new.root");
  desc.add<std::string>("DataEra", "2017BtoF");
  desc.add<bool>("UseJetEMPt", true);
  desc.add<double>("PrefiringRateSystematicUncty",0.2);

  descriptions.add("L1ECALNonPrefiringProbProducer",desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(L1ECALNonPrefiringProbProducer);
