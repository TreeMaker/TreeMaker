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
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
//
// class declaration
//

class GoodJetsProducer : public edm::EDProducer {
public:
   explicit GoodJetsProducer(const edm::ParameterSet&);
   ~GoodJetsProducer();
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   virtual void beginJob() ;
   virtual void produce(edm::Event&, const edm::EventSetup&);
   virtual void endJob() ;
   
   virtual void beginRun(edm::Run&, edm::EventSetup const&);
   virtual void endRun(edm::Run&, edm::EventSetup const&);
   virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   edm::InputTag JetTag_;
   double maxEta_;
   double maxMuFraction_, minNConstituents_, maxNeutralFraction_, maxPhotonFraction_, minChargedMultiplicity_, minChargedFraction_, maxChargedEMFraction_;
   
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
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   maxEta_ = iConfig.getParameter <double> ("maxJetEta");
   maxMuFraction_ = iConfig.getParameter <double> ("maxMuFraction");
   minNConstituents_ = iConfig.getParameter <double> ("minNConstituents");
   maxNeutralFraction_ = iConfig.getParameter <double> ("maxNeutralFraction");
   maxPhotonFraction_ = iConfig.getParameter <double> ("maxPhotonFraction");
   minChargedMultiplicity_ = iConfig.getParameter <double> ("minChargedMultiplicity");
   minChargedFraction_ = iConfig.getParameter <double> ("minChargedFraction");
   maxChargedEMFraction_ = iConfig.getParameter <double> ("maxChargedEMFraction");
   produces<std::vector<Jet> >();
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
void
GoodJetsProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   std::auto_ptr<std::vector<Jet> > prodJets(new std::vector<Jet>());
   edm::Handle< edm::View<Jet> > Jets;
   iEvent.getByLabel(JetTag_,Jets);
   if(Jets.isValid())
   {
      for(unsigned int i=0; i<Jets->size();i++)
      {
         if (std::abs(Jets->at(i).eta())>maxEta_) continue;
         float neufrac=Jets->at(i).neutralHadronEnergyFraction();//gives raw energy in the denominator
         float phofrac=Jets->at(i).neutralEmEnergyFraction();//gives raw energy in the denominator
         float chgfrac=Jets->at(i).chargedHadronEnergyFraction();
         float chgEMfrac=Jets->at(i).chargedEmEnergyFraction();
         float muFrac=Jets->at(i).muonEnergyFraction();
         unsigned int nconstit=Jets->at(i).nConstituents();
         int chgmulti=Jets->at(i).chargedHadronMultiplicity();
         if (muFrac<maxMuFraction_ && nconstit>=minNConstituents_ && neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ &&chgmulti>=minChargedMultiplicity_ && chgfrac>minChargedFraction_ && chgEMfrac<maxChargedEMFraction_)
            prodJets->push_back(Jet(Jets->at(i)));
      }
   }
   // put in the event
   const std::string string1("");
   iEvent.put(prodJets );
   
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

//define this as a plug-in
DEFINE_FWK_MODULE(GoodJetsProducer);
