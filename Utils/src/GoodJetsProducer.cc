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
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
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

class GoodJetsProducer : public edm::EDFilter {
public:
   explicit GoodJetsProducer(const edm::ParameterSet&);
   ~GoodJetsProducer();
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   virtual void beginJob() override;
   virtual bool filter(edm::Event&, const edm::EventSetup&) override;
   virtual void endJob() override;
   
   virtual void beginRun(edm::Run&, edm::EventSetup const&);
   virtual void endRun(edm::Run&, edm::EventSetup const&);
   virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   edm::InputTag JetTag_;
   std::vector<edm::InputTag> SkipTag_;
   edm::InputTag MetTag_;
   edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
   std::vector<edm::EDGetTokenT<edm::View<reco::Candidate>>> SkipTok_;
   edm::EDGetTokenT<edm::View<pat::MET> > MetTok_;
   double maxEta_;
   double maxNeutralFraction_, maxPhotonFraction_, minChargedFraction_, maxChargedEMFraction_, maxPhotonFractionHF_;
   int minNconstituents_, minNneutrals_, minNcharged_;
   double jetPtFilter_;
   bool saveAll_, ExcludeLeptonIsoTrackPhotons_, TagMode_;
   double JetConeSize_;
   double deltaR(double eta1, double phi1, double eta2, double phi2);

   
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
   minNneutrals_ = iConfig.getParameter <int> ("minNneutrals");
   minNcharged_ = iConfig.getParameter <int> ("minNcharged");
   maxNeutralFraction_ = iConfig.getParameter <double> ("maxNeutralFraction");
   maxPhotonFraction_ = iConfig.getParameter <double> ("maxPhotonFraction");
   maxPhotonFractionHF_ = iConfig.getParameter <double> ("maxPhotonFractionHF");
   minChargedFraction_ = iConfig.getParameter <double> ("minChargedFraction");
   maxChargedEMFraction_ = iConfig.getParameter <double> ("maxChargedEMFraction");
   jetPtFilter_ = iConfig.getParameter <double> ("jetPtFilter");
   saveAll_ = iConfig.getParameter <bool> ("SaveAllJets");  
   
   ExcludeLeptonIsoTrackPhotons_ = iConfig.getParameter <bool> ("ExcludeLepIsoTrackPhotons");
   SkipTag_  = iConfig.getParameter<std::vector<edm::InputTag>>("SkipTag");
   JetConeSize_ = iConfig.getParameter <double> ("JetConeSize");
   
   JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
   for(auto& tag: SkipTag_) SkipTok_.push_back(consumes<edm::View<reco::Candidate>>(tag));

   MetTag_ = iConfig.getParameter<edm::InputTag>("METTag");
   MetTok_ = consumes<edm::View<pat::MET>>(MetTag_);

   
   produces<std::vector<Jet> >();
   produces<bool>("JetID");
   produces<std::vector<bool> >("JetIDMask");
   produces<bool>("MuonJetFilter");
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
GoodJetsProducer::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   // load to be excluded leptons, isotracks and photons
   std::vector<edm::Handle<edm::View<reco::Candidate>>> excludeHandles;
   excludeHandles.reserve(SkipTag_.size());
   if(ExcludeLeptonIsoTrackPhotons_ && SkipTag_.size()){
      // loop over each edm::InputTag
      for (unsigned iC = 0; iC < SkipTag_.size(); ++iC) {
         // get each collection the edm::InputTag corresponds to
         edm::Handle<edm::View<reco::Candidate>> cleanCands;
         iEvent.getByToken(SkipTok_[iC], cleanCands);
         if (cleanCands.isValid()) {
            excludeHandles.push_back(cleanCands);
         }
         else {
             std::cout<<"Warning: skip tag not valid in GoodJetsProducer: "<<SkipTag_[iC]<<std::endl;
         }
      }
   }

   edm::Handle< edm::View<pat::MET> > MET;
   iEvent.getByToken(MetTok_,MET); 
   double met_phi(-99.);
   if(MET.isValid()) {
     met_phi=MET->at(0).phi();
   } else std::cout<<"GoodJetsProducer::METTag Invalid Tag: "<<MetTag_.label()<<std::endl;
   
   
   std::auto_ptr<std::vector<Jet> > prodJets(new std::vector<Jet>());
   std::auto_ptr<std::vector<bool> > jetsMask(new std::vector<bool>());
   bool result=true;
   bool noMuonJet=true;
   edm::Handle< edm::View<Jet> > Jets;
   iEvent.getByToken(JetTok_,Jets);
   if(Jets.isValid())
   {
      for(unsigned int i=0; i<Jets->size();i++)
      {
         if (std::abs(Jets->at(i).eta())>maxEta_) continue;
         float neufrac=Jets->at(i).neutralHadronEnergyFraction();//gives raw energy in the denominator
         float phofrac=Jets->at(i).neutralEmEnergyFraction();//gives raw energy in the denominator
         float chgfrac=Jets->at(i).chargedHadronEnergyFraction();
         float chgEMfrac=Jets->at(i).chargedEmEnergyFraction();
         int chgmulti=Jets->at(i).chargedMultiplicity();
         int neumulti=Jets->at(i).neutralMultiplicity();
         int nconstit=chgmulti+neumulti;
         bool skip=false;
         if(ExcludeLeptonIsoTrackPhotons_ && excludeHandles.size())
         {
            for(unsigned h=0; h<excludeHandles.size(); ++h){
                for(unsigned ih=0; ih<excludeHandles[h]->size(); ++ih){
                    if(std::abs(Jets->at(i).pt() - excludeHandles[h]->at(ih).pt() ) / excludeHandles[h]->at(ih).pt() < 1 && 
                       deltaR(Jets->at(i).eta(),Jets->at(i).phi(),excludeHandles[h]->at(ih).eta(),excludeHandles[h]->at(ih).phi()) < JetConeSize_ )
                    {
                       skip=true;
                       break;
                    }
                    if(skip) break; //no need to keep checking
                }
            }
            if(skip)
            {
               prodJets->push_back(Jet(Jets->at(i)));
               jetsMask->push_back(true);
               continue;
            }
         }
         bool good = true;
         if (std::abs(Jets->at(i).eta()) < 3.0){
            good = neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ && nconstit>minNconstituents_;
            if(std::abs(Jets->at(i).eta()) < 2.4) good &= chgfrac>minChargedFraction_ && chgmulti>minNcharged_ && chgEMfrac<maxChargedEMFraction_;
         } else {
            good = phofrac<maxPhotonFractionHF_ && neumulti>minNneutrals_;
         }

        //save all good jets regardless of pt
        if (good || saveAll_) {
           prodJets->push_back(Jet(Jets->at(i)));
           jetsMask->push_back(good);
        } 
        //calculate event filter only for jets that pass pT cut
        if (Jets->at(i).pt() > jetPtFilter_) {
           //std::cout << "Filtered jet pT, eta: " << Jets->at(i).pt() << ", " << Jets->at(i).eta() << std::endl;
           if(!good && !TagMode_) return false;
           result &= good;
        }
	//calculate event filter for bad muon jets
        if (Jets->at(i).pt() > 200. && Jets->at(i).muonEnergyFraction()>0.5) {
	  if(std::abs(reco::deltaPhi(Jets->at(i).phi(), met_phi)) > (TMath::Pi()-0.4)) noMuonJet = false;
        }
      }
   }
   // put in the event
   iEvent.put(prodJets);
   iEvent.put(jetsMask,"JetIDMask");
   std::auto_ptr<bool> passing(new bool(result));
   iEvent.put(passing,"JetID");
   std::auto_ptr<bool> muJet(new bool(noMuonJet));
   iEvent.put(muJet,"MuonJetFilter");
   return true;
   
}

// ------------ method called once each job just before starting event loop  ------------
void
GoodJetsProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
GoodJetsProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
GoodJetsProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
GoodJetsProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
GoodJetsProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
GoodJetsProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
double GoodJetsProducer::deltaR(double eta1, double phi1, double eta2, double phi2)
{
   double deta = eta1-eta2;
   double dphi = TVector2::Phi_mpi_pi(phi1-phi2);
   return sqrt(deta * deta + dphi *dphi); 
}

//define this as a plug-in
DEFINE_FWK_MODULE(GoodJetsProducer);
