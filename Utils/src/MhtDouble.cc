// -*- C++ -*-
//
// Package:    MhtDouble
// Class:      MhtDouble
// 
/**\class MhtDouble MhtDouble.cc RA2Classic/MhtDouble/src/MhtDouble.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
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
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
//
// class declaration
//

class MhtDouble : public edm::global::EDProducer<> {
   public:
      explicit MhtDouble(const edm::ParameterSet&);
      ~MhtDouble();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
      
      // ----------member data ---------------------------
      edm::InputTag JetTag_;
	  edm::EDGetTokenT<reco::CandidateView> JetTok_;
};

//
// constructors and destructor
//
MhtDouble::MhtDouble(const edm::ParameterSet& iConfig)
{
   //register your product
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   JetTok_ = consumes<reco::CandidateView>(JetTag_);

	 produces<double>("Pt");
	 produces<double>("Phi");
}


MhtDouble::~MhtDouble()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
MhtDouble::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;
  edm::Handle< reco::CandidateView > Jets;
	iEvent.getByToken(JetTok_,Jets);
	reco::MET::LorentzVector mhtLorentz(0,0,0,0);
	if( Jets.isValid() ) {
		for(unsigned int i=0; i<Jets->size();i++)
		{
		mhtLorentz -=Jets->at(i).p4();
		}
  }
  else edm::LogWarning("TreeMaker")<<"MHTDouble::Invalid Tag: "<<JetTag_.label();
	auto Pt = std::make_unique<double>(mhtLorentz.pt());
	auto Phi = std::make_unique<double>(mhtLorentz.phi());
	iEvent.put(std::move(Pt),"Pt");
	iEvent.put(std::move(Phi),"Phi");
 
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MhtDouble::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MhtDouble);
