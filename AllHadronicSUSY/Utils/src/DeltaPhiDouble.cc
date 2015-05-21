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
   //register your produc
   MHTJetTag_ = iConfig.getParameter<edm::InputTag> ("MHTJets");
   DeltaPhiJetTag_ = iConfig.getParameter<edm::InputTag> ("DeltaPhiJets");
   
   produces<double>("Jet1Pt");
   produces<double>("Jet2Pt");
   produces<double>("Jet3Pt");
   produces<double>("Jet1Eta");
   produces<double>("Jet2Eta");
   produces<double>("Jet3Eta");
   produces<double>("DeltaPhi1");
   produces<double>("DeltaPhi2");
   produces<double>("DeltaPhi3");
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
   double jet1eta=0;
   double jet2eta=0;
   double jet3eta=0;
   double deltaphi1=10;
   double deltaphi2=10;
   double deltaphi3=10;
   edm::Handle< edm::View<reco::Candidate> > MHTJets;
   iEvent.getByLabel(MHTJetTag_,MHTJets);
   reco::MET::LorentzVector mhtLorentz(0,0,0,0);
   if( MHTJets.isValid() ) {
      for(unsigned int i=0; i<MHTJets->size();i++)
      {
         mhtLorentz -=MHTJets->at(i).p4();
      }
   }
   else std::cout<<"DeltaPhiDouble::Invlide MHT Jet Tag: "<<MHTJetTag_.label()<<std::endl;
   edm::Handle< edm::View<reco::Candidate> > DeltaPhiJets;
   iEvent.getByLabel(DeltaPhiJetTag_,DeltaPhiJets);
   float minDeltaPhi=99;
   if( DeltaPhiJets.isValid() ) {
      int count=0;
      for(unsigned int i=0; i<DeltaPhiJets->size();i++)
      {
         if(count==0){
            jet1pt = DeltaPhiJets->at(i).pt();
            jet1eta = DeltaPhiJets->at(i).eta();
            deltaphi1 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if(count==1){
            jet2pt = DeltaPhiJets->at(i).pt();
            jet2eta = DeltaPhiJets->at(i).eta();
            deltaphi2 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if(count==2){
            jet3pt = DeltaPhiJets->at(i).pt();
            jet3eta = DeltaPhiJets->at(i).eta();
            deltaphi3 = std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));
         }
         if(minDeltaPhi>std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi())))minDeltaPhi=std::abs(reco::deltaPhi(DeltaPhiJets->at(i).phi(),mhtLorentz.phi()));;
         count++;
         if(count==3) break;
      }
   }
   else std::cout<<"DeltaPhiDouble::Invlide DeltaPhiJets Jet Tag: "<<DeltaPhiJetTag_.label()<<std::endl;
   
   std::auto_ptr<double> htp1a(new double(jet1pt));
   iEvent.put(htp1a,"Jet1Pt");
   std::auto_ptr<double> htp1b(new double(jet1eta));
   iEvent.put(htp1b,"Jet1Eta");
   std::auto_ptr<double> htp1c(new double(deltaphi1));
   iEvent.put(htp1c,"DeltaPhi1");
   std::auto_ptr<double> htp2a(new double(jet2pt));
   iEvent.put(htp2a,"Jet2Pt");
   std::auto_ptr<double> htp2b(new double(jet2eta));
   iEvent.put(htp2b,"Jet2Eta");
   std::auto_ptr<double> htp2c(new double(deltaphi2));
   iEvent.put(htp2c,"DeltaPhi2");
   std::auto_ptr<double> htp3a(new double(jet3pt));
   iEvent.put(htp3a,"Jet3Pt");
   std::auto_ptr<double> htp3b(new double(jet3eta));
   iEvent.put(htp3b,"Jet3Eta");
   std::auto_ptr<double> htp3c(new double(deltaphi3));
   iEvent.put(htp3c,"DeltaPhi3");
   std::auto_ptr<double> htp4c(new double(minDeltaPhi));
   iEvent.put(htp4c,"minDeltaPhi");
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
