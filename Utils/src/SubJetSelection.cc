// -*- C++ -*-
//
// Package:    SubJetSelectionT
// Class:      SubJetSelectionT
//
/**\class SubJetSelectionT SubJetSelectionT.cc RA2Classic/SubJetSelectionT/src/SubJetSelectionT.cc
 *
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Thu Apr 17 10:49:52 CEST 2014
// $Id$
//
//


// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
//
// class declaration
//

template <class T>
class SubJetSelectionT : public edm::global::EDProducer<> {
public:
   explicit SubJetSelectionT(const edm::ParameterSet&);
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   double getRawPt(const T& Jet) const { return Jet.pt(); }

   // ----------member data ---------------------------
   edm::InputTag JetTag_;
   edm::EDGetTokenT<edm::View<T>> JetTok_;
   double MinPt_, MaxEta_;
   double VetoMaxPt_, VetoMinEta_, VetoMaxEta_;
   bool VetoRawPt_, veto_;
};

//
// constructors and destructor
//
using namespace pat;

template <class T>
SubJetSelectionT<T>::SubJetSelectionT(const edm::ParameterSet& iConfig) :
   JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
   JetTok_(consumes<edm::View<T>>(JetTag_)),
   MinPt_(iConfig.getParameter<double>("MinPt")),
   MaxEta_(iConfig.getParameter<double>("MaxEta")),
   VetoMaxPt_(iConfig.getParameter<double>("VetoMaxPt")),
   VetoMinEta_(iConfig.getParameter<double>("VetoMinEta")),
   VetoMaxEta_(iConfig.getParameter<double>("VetoMaxEta")),
   VetoRawPt_(iConfig.getParameter<bool>("VetoRawPt")),
   veto_(iConfig.getParameter<bool>("veto"))
{
   //register your products
   produces<std::vector<T> >();
   produces<std::vector<bool> >("SubJetMask");
}

// ------------ method called to produce the data  ------------
template <class T>
void SubJetSelectionT<T>::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;
   auto prodJets = std::make_unique<std::vector<T>>();
   auto mask = std::make_unique<std::vector<bool>>();

   edm::Handle< edm::View<T> > Jets;
   iEvent.getByToken(JetTok_,Jets);
   if(Jets.isValid()) {
      mask->resize(Jets->size(),false);
      for(unsigned int i=0; i<Jets->size();i++) {
         const auto& Jet = Jets->at(i);
         double pt = Jet.pt();
         double eta = std::abs(Jet.eta());
         bool pass = (pt>MinPt_ and eta<MaxEta_);
         if(veto_){
            if(VetoRawPt_) pt = getRawPt(Jet);
            pass &= (pt>VetoMaxPt_ or eta<VetoMinEta_ or eta>VetoMaxEta_);
         }
         if(pass) {
            prodJets->push_back(T(Jet));
            mask->at(i) = true;
         }
      }
   }
   // put in the event
   iEvent.put(std::move(prodJets));
   iEvent.put(std::move(mask),"SubJetMask");
}

template <>
double SubJetSelectionT<pat::Jet>::getRawPt(const pat::Jet& Jet) const {
   double pt = Jet.pt();
   if(Jet.jecSetsAvailable()) pt *= Jet.jecFactor(0);
   if(Jet.hasUserFloat("jerFactor")) pt /= Jet.userFloat("jerFactor");
   return pt;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template <class T>
void SubJetSelectionT<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}

//typedefs
typedef SubJetSelectionT<pat::Jet> SubJetSelection;
typedef SubJetSelectionT<reco::GenJet> SubGenJetSelection;

//define this as a plug-in
DEFINE_FWK_MODULE(SubJetSelection);
DEFINE_FWK_MODULE(SubGenJetSelection);
