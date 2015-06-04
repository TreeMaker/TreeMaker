// -*- C++ -*-
//
// Package:    AllHadronicSUSY/TruthNoiseFilter
// Class:      TruthNoiseFilter
//
/**\class TruthNoiseFilter TruthNoiseFilter.cc AllHadronicSUSY/TruthNoiseFilter/plugins/TruthNoiseFilter.cc
 
 Description: [one line class summary]
 
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Christian Sander
//         Created:  Thu, 12 Mar 2015 19:24:31 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

//
// class declaration
//

class TruthNoiseFilter : public edm::EDFilter {
public:
   explicit TruthNoiseFilter(const edm::ParameterSet&);
   ~TruthNoiseFilter();
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   virtual void beginJob() override;
   virtual bool filter(edm::Event&, const edm::EventSetup&) override;
   virtual void endJob() override;
   
   //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
   //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
   //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
   //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
   
   // ----------member data ---------------------------
   edm::InputTag genjets_;
   edm::InputTag jets_;
   double recoJetPt_;
   double genJetPt_;
   double dRmax_;
   
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
TruthNoiseFilter::TruthNoiseFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
   genjets_ = iConfig.getParameter<edm::InputTag> ("genjetCollection");
   jets_ = iConfig.getParameter<edm::InputTag> ("jetCollection");
   recoJetPt_ = iConfig.getParameter<double> ("recoJetPt");
   genJetPt_ = iConfig.getParameter<double> ("genJetPt");
   dRmax_ = iConfig.getParameter<double> ("dRmax");
}


TruthNoiseFilter::~TruthNoiseFilter()
{
   
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
   
}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
TruthNoiseFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   
   //GenJets
   edm::Handle<edm::View<reco::GenJet> > Jets_gen;
   iEvent.getByLabel(genjets_, Jets_gen);
   
   //RecoJets
   edm::Handle<edm::View<pat::Jet> > Jets_rec;
   iEvent.getByLabel(jets_, Jets_rec);
   
   for (edm::View<pat::Jet>::const_iterator jt = Jets_rec->begin(); jt != Jets_rec->end(); ++jt) {
      double dRbest = 0;
      if (jt->pt() < recoJetPt_) continue;
      dRbest = 100;
      for (edm::View<reco::GenJet>::const_iterator it = Jets_gen->begin(); it != Jets_gen->end(); ++it) {
         if (it->pt() < jt->pt()/2.) continue;
         double dR = deltaR(*jt, *it);
         if (dR < dRbest) {
            dRbest = dR;
         }
      }
      if (dRbest > dRmax_) {
         //std::cout << "reject" << std::endl;
         return false;
      }
   }
   //std::cout << "accept" << std::endl;
   return true;
}

// ------------ method called once each job just before starting event loop  ------------
void
TruthNoiseFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TruthNoiseFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
 void
 TruthNoiseFilter::beginRun(edm::Run const&, edm::EventSetup const&)
 {
 }
 */

// ------------ method called when ending the processing of a run  ------------
/*
 void
 TruthNoiseFilter::endRun(edm::Run const&, edm::EventSetup const&)
 {
 }
 */

// ------------ method called when starting to processes a luminosity block  ------------
/*
 void
 TruthNoiseFilter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
 {
 }
 */

// ------------ method called when ending the processing of a luminosity block  ------------
/*
 void
 TruthNoiseFilter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
 {
 }
 */

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TruthNoiseFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(TruthNoiseFilter);
