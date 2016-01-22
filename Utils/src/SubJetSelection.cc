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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

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
class SubJetSelectionT : public edm::EDProducer {
public:
   explicit SubJetSelectionT(const edm::ParameterSet&);
   ~SubJetSelectionT();
   
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
   edm::EDGetTokenT<edm::View<T>> JetTok_;
   double MinPt_, MaxEta_;
   
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

template <class T>
SubJetSelectionT<T>::SubJetSelectionT(const edm::ParameterSet& iConfig)
{
   
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   MinPt_ = iConfig.getParameter <double> ("MinPt");
   MaxEta_ = iConfig.getParameter <double> ("MaxEta");
   
   JetTok_ = consumes<edm::View<T>>(JetTag_);

   //register your products
   produces<std::vector<T> >();
   produces<std::vector<bool> >("SubJetMask");
   
}

template <class T>
SubJetSelectionT<T>::~SubJetSelectionT()
{
   
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
   
}


//
// member functions
//

// ------------ method called to produce the data  ------------
template <class T>
void SubJetSelectionT<T>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   std::auto_ptr<std::vector<T> > prodJets(new std::vector<T>());
   std::auto_ptr<std::vector<bool> > mask(new std::vector<bool>());

   edm::Handle< edm::View<T> > Jets;
   iEvent.getByToken(JetTok_,Jets);
   if(Jets.isValid()) {
      mask->resize(Jets->size(),false);
      for(unsigned int i=0; i<Jets->size();i++) {
         if(Jets->at(i).pt()>MinPt_ && std::abs(Jets->at(i).eta() ) < MaxEta_) {
            prodJets->push_back(T(Jets->at(i)) );
            mask->at(i) = true;
         }
      }
   }
   // put in the event
   iEvent.put(prodJets);
   iEvent.put(mask,"SubJetMask");
   
}

// ------------ method called once each job just before starting event loop  ------------
template <class T>
void SubJetSelectionT<T>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template <class T>
void SubJetSelectionT<T>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template <class T>
void SubJetSelectionT<T>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template <class T>
void SubJetSelectionT<T>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template <class T>
void SubJetSelectionT<T>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template <class T>
void SubJetSelectionT<T>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
