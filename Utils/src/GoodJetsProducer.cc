// -*- C++ -*-
//
// Package:    GoodJetsProducer
// Class:      GoodJetsProducer
//
/**\class GoodJetsProducer GoodJetsProducer.cc RA2Classic/GoodJetsProducer/src/GoodJetsProducer.cc
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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
#include <DataFormats/PatCandidates/interface/Photon.h>
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include <TVector2.h>
//
// class declaration
//

class GoodJetsProducer : public edm::global::EDFilter<> {
public:
   explicit GoodJetsProducer(const edm::ParameterSet&);
   ~GoodJetsProducer() override;
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   bool filter(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   
   edm::InputTag JetTag_;
   std::vector<edm::InputTag> SkipTag_;
   edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
   std::vector<edm::EDGetTokenT<edm::View<reco::Candidate>>> SkipTok_;
   double maxEta_;
   double maxNeutralFraction_, maxNeutralFractionHE_, minNeutralFractionHF_, maxPhotonFraction_, minPhotonFractionHE_, maxPhotonFractionHE_, maxPhotonFractionHF_, minChargedFraction_, maxChargedEMFraction_;
   int minNconstituents_, minNneutralsHE_, minNneutralsHF_, minNcharged_;
   double jetPtFilter_;
   bool saveAllId_, saveAllPt_, ExcludeLeptonIsoTrackPhotons_, TagMode_, invertJetPtFilter_;
   double JetConeSize_;

   
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
using namespace pat;
GoodJetsProducer::GoodJetsProducer(const edm::ParameterSet& iConfig)
{
   TagMode_ = iConfig.getParameter<bool> ("TagMode");
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   maxEta_ = iConfig.getParameter <double> ("maxJetEta");
   minNconstituents_ = iConfig.getParameter <int> ("minNconstituents");
   minNneutralsHE_ = iConfig.getParameter <int> ("minNneutralsHE");
   minNneutralsHF_ = iConfig.getParameter <int> ("minNneutralsHF");
   minNcharged_ = iConfig.getParameter <int> ("minNcharged");
   maxNeutralFraction_ = iConfig.getParameter <double> ("maxNeutralFraction");
   maxNeutralFractionHE_ = iConfig.getParameter <double> ("maxNeutralFractionHE");
   minNeutralFractionHF_ = iConfig.getParameter <double> ("minNeutralFractionHF");
   maxPhotonFraction_ = iConfig.getParameter <double> ("maxPhotonFraction");
   minPhotonFractionHE_ = iConfig.getParameter <double> ("minPhotonFractionHE");
   maxPhotonFractionHE_ = iConfig.getParameter <double> ("maxPhotonFractionHE");
   maxPhotonFractionHF_ = iConfig.getParameter <double> ("maxPhotonFractionHF");
   minChargedFraction_ = iConfig.getParameter <double> ("minChargedFraction");
   maxChargedEMFraction_ = iConfig.getParameter <double> ("maxChargedEMFraction");
   jetPtFilter_ = iConfig.getParameter <double> ("jetPtFilter");
   invertJetPtFilter_ = iConfig.getParameter <bool> ("invertJetPtFilter");
   saveAllId_ = iConfig.getParameter <bool> ("SaveAllJetsId");
   saveAllPt_ = iConfig.getParameter <bool> ("SaveAllJetsPt");
   
   ExcludeLeptonIsoTrackPhotons_ = iConfig.getParameter <bool> ("ExcludeLepIsoTrackPhotons");
   SkipTag_  = iConfig.getParameter<std::vector<edm::InputTag>>("SkipTag");
   JetConeSize_ = iConfig.getParameter <double> ("JetConeSize");
   
   JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
   for(auto& tag: SkipTag_) SkipTok_.push_back(consumes<edm::View<reco::Candidate>>(tag));
   
   produces<std::vector<Jet> >();
   produces<bool>("JetID");
   produces<std::vector<bool> >("JetIDMask");
   produces<std::vector<bool> >("JetLeptonMask");
}


GoodJetsProducer::~GoodJetsProducer()
{
   
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
   
}


//
// member functions
//

// ------------ method called to produce the data  ------------
bool
GoodJetsProducer::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;
   // load to be excluded leptons, isotracks and photons
   std::vector<edm::Handle<edm::View<reco::Candidate>>> excludeHandles;
   excludeHandles.reserve(SkipTag_.size());
   if(ExcludeLeptonIsoTrackPhotons_ && !SkipTag_.empty()){
      // loop over each edm::InputTag
      for (unsigned iC = 0; iC < SkipTag_.size(); ++iC) {
         // get each collection the edm::InputTag corresponds to
         edm::Handle<edm::View<reco::Candidate>> cleanCands;
         iEvent.getByToken(SkipTok_[iC], cleanCands);
         if (cleanCands.isValid()) {
            excludeHandles.push_back(cleanCands);
         }
         else {
             edm::LogWarning("TreeMaker")<<"Warning: skip tag not valid in GoodJetsProducer: "<<SkipTag_[iC];
         }
      }
   }
   
   auto prodJets = std::make_unique<std::vector<Jet>>();
   auto jetsMask = std::make_unique<std::vector<bool>>();
   auto leptonMask = std::make_unique<std::vector<bool>>();
   bool result=true;
   edm::Handle< edm::View<Jet> > Jets;
   iEvent.getByToken(JetTok_,Jets);
   if(Jets.isValid())
   {
      prodJets->reserve(Jets->size());
      jetsMask->reserve(Jets->size());
      leptonMask->reserve(Jets->size());
      for(const auto & iJet : *Jets)
      {
         if (std::abs(iJet.eta())>maxEta_) continue;
         if (!saveAllPt_ &&
              ( (!invertJetPtFilter_ && iJet.pt() <= jetPtFilter_) ||
                (invertJetPtFilter_ && iJet.pt() > jetPtFilter_) ) ) continue;
         float neufrac=iJet.neutralHadronEnergyFraction();//gives raw energy in the denominator
         float phofrac=iJet.neutralEmEnergyFraction();//gives raw energy in the denominator
         float chgfrac=iJet.chargedHadronEnergyFraction();
         float chgEMfrac=iJet.chargedEmEnergyFraction();
         int chgmulti=iJet.chargedMultiplicity();
         int neumulti=iJet.neutralMultiplicity();
         int nconstit=chgmulti+neumulti;
         bool skip=false;
         if(ExcludeLeptonIsoTrackPhotons_ && !excludeHandles.empty())
         {
            for(const auto & excludeHandle : excludeHandles){
                for(const auto & exclude : *excludeHandle){
                    if(std::abs(iJet.pt() - exclude.pt() ) / exclude.pt() < 1 && 
                       deltaR(iJet.p4(),exclude.p4()) < JetConeSize_ )
                    {
                       skip=true;
                       break;
                    }
                    if(skip) break; //no need to keep checking
                }
            }
            if(skip)
            {
               prodJets->push_back(Jet(iJet));
               jetsMask->push_back(true);
               leptonMask->push_back(true);
               continue;
            }
            else leptonMask->push_back(false);
         }
         else leptonMask->push_back(false);
         bool good = true;
         if (std::abs(iJet.eta()) <= 2.7){
            good = neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ && nconstit>minNconstituents_;
            if(std::abs(iJet.eta()) < 2.4) good &= chgfrac>minChargedFraction_ && chgmulti>minNcharged_ && chgEMfrac<maxChargedEMFraction_;
         }
         else if(std::abs(iJet.eta()) <= 3.0){
            good = phofrac>minPhotonFractionHE_ && phofrac<maxPhotonFractionHE_ && neufrac<maxNeutralFractionHE_ && neumulti>minNneutralsHE_;
         }
         else {
            good = phofrac<maxPhotonFractionHF_ && neufrac>minNeutralFractionHF_ && neumulti>minNneutralsHF_;
         }
        //save good jets, potentially regardless of id or pt
        if (good || saveAllId_) {
           prodJets->push_back(Jet(iJet));
           jetsMask->push_back(good);
        } 
        //calculate event filter only for jets that pass pT cut
        if ( (!invertJetPtFilter_ && iJet.pt() > jetPtFilter_) ||
                (invertJetPtFilter_ && iJet.pt() <= jetPtFilter_) ) {
           if(!good && !TagMode_) return false;
           result &= good;
        }
      }
   }
   // put in the event
   iEvent.put(std::move(prodJets));
   iEvent.put(std::move(jetsMask),"JetIDMask");
   iEvent.put(std::move(leptonMask),"JetLeptonMask");
   auto passing = std::make_unique<bool>(result);
   iEvent.put(std::move(passing),"JetID");
   return true;
   
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GoodJetsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GoodJetsProducer);
