// -*- C++ -*-
//
// Package:    DeltaPhiDouble
// Class:      DeltaPhiDouble
//
/**\class DeltaPhiDouble DeltaPhiDouble.cc RA2Classic/DeltaPhiDouble/src/DeltaPhiDouble.cc
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
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "TreeMaker/Utils/interface/mht.h"

//
// class declaration
//

class DeltaPhiDouble : public edm::global::EDProducer<> {
public:
   explicit DeltaPhiDouble(const edm::ParameterSet&);
   ~DeltaPhiDouble() override;
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   
   edm::InputTag MHTPhiTag_, MHTJetTag_, DeltaPhiJetTag_;
   edm::EDGetTokenT<edm::View<reco::Candidate>> MHTJetTok_, DeltaPhiJetTok_;
   edm::EDGetTokenT<double> MHTPhiTok_;
   bool usePhi;
   
   
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
DeltaPhiDouble::DeltaPhiDouble(const edm::ParameterSet& iConfig) :
   MHTPhiTag_(iConfig.getParameter<edm::InputTag>("MHTPhi")),
   MHTJetTag_(iConfig.getParameter<edm::InputTag>("MHTJets")),
   DeltaPhiJetTag_(iConfig.getParameter<edm::InputTag>("DeltaPhiJets")),
   usePhi(!MHTPhiTag_.label().empty())
{
   //register your products
   if(usePhi) MHTPhiTok_ = consumes<double>(MHTPhiTag_);
   else MHTJetTok_ = consumes<edm::View<reco::Candidate> >(MHTJetTag_);
   DeltaPhiJetTok_ = consumes<edm::View<reco::Candidate> >(DeltaPhiJetTag_);
   
   produces<double>("DeltaPhi1");
   produces<double>("DeltaPhi2");
   produces<double>("DeltaPhi3");
   produces<double>("DeltaPhi4");
   produces<double>("minDeltaPhi");
}


DeltaPhiDouble::~DeltaPhiDouble()
{
   
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
   
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
DeltaPhiDouble::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;
   std::vector<double> deltaphi(4,10.);
   double mhtLorentzPhi = -1;
   if(usePhi){
      edm::Handle<double> MHTPhi;
      iEvent.getByToken(MHTPhiTok_,MHTPhi);
      if(MHTPhi.isValid()) mhtLorentzPhi = *(MHTPhi.product());
      else edm::LogWarning("TreeMaker")<<"DeltaPhiDouble::Invalid MHT Phi Tag: "<<MHTPhiTag_;
   }
   else {
      edm::Handle< edm::View<reco::Candidate> > MHTJets;
      iEvent.getByToken(MHTJetTok_,MHTJets);
      if( MHTJets.isValid() ) {
         reco::MET::LorentzVector mhtLorentz = utils::calculateMHT(MHTJets.product());
         mhtLorentzPhi = mhtLorentz.phi();
      }
      else edm::LogWarning("TreeMaker")<<"DeltaPhiDouble::Invalid MHT Jet Tag: "<<MHTJetTag_;
   }
   edm::Handle< edm::View<reco::Candidate> > DeltaPhiJets;
   iEvent.getByToken(DeltaPhiJetTok_,DeltaPhiJets);
   float minDeltaPhi=99;
   if( DeltaPhiJets.isValid() ) {
      for (unsigned int i=0; i<DeltaPhiJets->size();i++)
      {
         deltaphi[i] = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentzPhi));
         if (minDeltaPhi>deltaphi[i]) minDeltaPhi = deltaphi[i];

         if(i==3) break;
      }
   }
   else edm::LogWarning("TreeMaker")<<"DeltaPhiDouble::Invalid DeltaPhiJets Jet Tag: "<<DeltaPhiJetTag_;
   
   auto htp1c = std::make_unique<double>(deltaphi[0]);
   iEvent.put(std::move(htp1c),"DeltaPhi1");
   auto htp2c = std::make_unique<double>(deltaphi[1]);
   iEvent.put(std::move(htp2c),"DeltaPhi2");
   auto htp3c = std::make_unique<double>(deltaphi[2]);
   iEvent.put(std::move(htp3c),"DeltaPhi3");
   auto htp4d = std::make_unique<double>(deltaphi[3]);
   iEvent.put(std::move(htp4d),"DeltaPhi4");   
   auto htp4c = std::make_unique<double>(minDeltaPhi);
   iEvent.put(std::move(htp4c),"minDeltaPhi");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DeltaPhiDouble::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DeltaPhiDouble);
