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
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>

//
// class declaration
//

class DeltaPhiDouble : public edm::EDProducer {
public:
   explicit DeltaPhiDouble(const edm::ParameterSet&);
   ~DeltaPhiDouble();
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   virtual void beginJob() ;
   virtual void produce(edm::Event&, const edm::EventSetup&);
   virtual void endJob() ;
   
   virtual void beginRun(edm::Run&, edm::EventSetup const&);
   virtual void endRun(edm::Run&, edm::EventSetup const&);
   virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   edm::InputTag MHTJetTag_, DeltaPhiJetTag_;
   edm::EDGetTokenT<edm::View<reco::Candidate>> MHTJetTok_, DeltaPhiJetTok_;
   
   
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
DeltaPhiDouble::DeltaPhiDouble(const edm::ParameterSet& iConfig)
{
   //register your product
   MHTJetTag_ = iConfig.getParameter<edm::InputTag> ("MHTJets");
   DeltaPhiJetTag_ = iConfig.getParameter<edm::InputTag> ("DeltaPhiJets");
   MHTJetTok_ = consumes<edm::View<reco::Candidate> >(MHTJetTag_);
   DeltaPhiJetTok_ = consumes<edm::View<reco::Candidate> >(DeltaPhiJetTag_);
   
   produces<double>("Jet1Pt");
   produces<double>("Jet2Pt");
   produces<double>("Jet3Pt");
   produces<double>("Jet4Pt");
   produces<double>("Jet1Eta");
   produces<double>("Jet2Eta");
   produces<double>("Jet3Eta");
   produces<double>("Jet4Eta");
   produces<double>("DeltaPhi1");
   produces<double>("DeltaPhi2");
   produces<double>("DeltaPhi3");
   produces<double>("DeltaPhi4");
   produces<double>("minDeltaPhi");
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
DeltaPhiDouble::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   double jet1pt=0;
   double jet2pt=0;
   double jet3pt=0;
   double jet4pt=0;
   double jet1eta=0;
   double jet2eta=0;
   double jet3eta=0;
   double jet4eta=0;
   double deltaphi1=10;
   double deltaphi2=10;
   double deltaphi3=10;
   double deltaphi4=10;
   edm::Handle< edm::View<reco::Candidate> > MHTJets;
   iEvent.getByToken(MHTJetTok_,MHTJets);
   reco::MET::LorentzVector mhtLorentz(0,0,0,0);
   if( MHTJets.isValid() ) {
      for(unsigned int i=0; i<MHTJets->size();i++)
      {
         mhtLorentz -=MHTJets->at(i).p4();
      }
   }
   else edm::LogWarning("TreeMaker")<<"DeltaPhiDouble::Invalid MHT Jet Tag: "<<MHTJetTag_.label();
   edm::Handle< edm::View<reco::Candidate> > DeltaPhiJets;
   iEvent.getByToken(DeltaPhiJetTok_,DeltaPhiJets);
   float minDeltaPhi=99;
   if( DeltaPhiJets.isValid() ) {
      int count=0;
      for (unsigned int i=0; i<DeltaPhiJets->size();i++)
      {
         if (count==0){
            jet1pt = DeltaPhiJets->at(i).pt();
            jet1eta = DeltaPhiJets->at(i).eta();
            deltaphi1 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if (count==1){
            jet2pt = DeltaPhiJets->at(i).pt();
            jet2eta = DeltaPhiJets->at(i).eta();
            deltaphi2 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if (count==2){
            jet3pt = DeltaPhiJets->at(i).pt();
            jet3eta = DeltaPhiJets->at(i).eta();
            deltaphi3 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if (count==3){
            jet4pt = DeltaPhiJets->at(i).pt();
            jet4eta = DeltaPhiJets->at(i).eta();
            deltaphi4 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if (minDeltaPhi>std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi())))
            minDeltaPhi=std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));;

         count++;
         if(count==4) break;
      }
   }
   else edm::LogWarning("TreeMaker")<<"DeltaPhiDouble::Invalid DeltaPhiJets Jet Tag: "<<DeltaPhiJetTag_.label();
   
   auto htp1a = std::make_unique<double>(jet1pt);
   iEvent.put(std::move(htp1a),"Jet1Pt");
   auto htp1b = std::make_unique<double>(jet1eta);
   iEvent.put(std::move(htp1b),"Jet1Eta");
   auto htp1c = std::make_unique<double>(deltaphi1);
   iEvent.put(std::move(htp1c),"DeltaPhi1");
   auto htp2a = std::make_unique<double>(jet2pt);
   iEvent.put(std::move(htp2a),"Jet2Pt");
   auto htp2b = std::make_unique<double>(jet2eta);
   iEvent.put(std::move(htp2b),"Jet2Eta");
   auto htp2c = std::make_unique<double>(deltaphi2);
   iEvent.put(std::move(htp2c),"DeltaPhi2");
   auto htp3a = std::make_unique<double>(jet3pt);
   iEvent.put(std::move(htp3a),"Jet3Pt");
   auto htp3b = std::make_unique<double>(jet3eta);
   iEvent.put(std::move(htp3b),"Jet3Eta");
   auto htp3c = std::make_unique<double>(deltaphi3);
   iEvent.put(std::move(htp3c),"DeltaPhi3");
   auto htp4a = std::make_unique<double>(jet4pt);
   iEvent.put(std::move(htp4a),"Jet4Pt");
   auto htp4b = std::make_unique<double>(jet4eta);
   iEvent.put(std::move(htp4b),"Jet4Eta");
   auto htp4d = std::make_unique<double>(deltaphi4);
   iEvent.put(std::move(htp4d),"DeltaPhi4");   
   auto htp4c = std::make_unique<double>(minDeltaPhi);
   iEvent.put(std::move(htp4c),"minDeltaPhi");
}

// ------------ method called once each job just before starting event loop  ------------
void
DeltaPhiDouble::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
DeltaPhiDouble::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
DeltaPhiDouble::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
DeltaPhiDouble::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
DeltaPhiDouble::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
DeltaPhiDouble::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
