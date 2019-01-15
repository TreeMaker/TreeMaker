// -*- C++ -*-
//
// Package:    HTDouble
// Class:      HTDouble
// 
/**\class HTDouble HTDouble.cc RA2Classic/HTDouble/src/HTDouble.cc
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
#include "DataFormats/PatCandidates/interface/Jet.h"
//
// class declaration
//

class HTDouble : public edm::global::EDProducer<> {
public:
	explicit HTDouble(const edm::ParameterSet&);
	~HTDouble() override;
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
	// ----------member data ---------------------------
	edm::InputTag JetTag_;
	edm::EDGetTokenT<reco::CandidateView> JetTok_;
};

//
// constructors and destructor
//
HTDouble::HTDouble(const edm::ParameterSet& iConfig)
{
	//register your products
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	JetTok_ = consumes<reco::CandidateView>(JetTag_);
	
	produces<double>("");
	
}


HTDouble::~HTDouble()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
HTDouble::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	using namespace edm;
	double ht_=0;
	edm::Handle< reco::CandidateView > Jets;
	iEvent.getByToken(JetTok_,Jets);
	if( Jets.isValid() ) {
		for(const auto & iJet : *Jets)
		{
			ht_ += iJet.pt();
		}
	}
	else edm::LogWarning("TreeMaker")<<"HTDouble::Invalid Tag: "<<JetTag_;
	auto htp = std::make_unique<double>(ht_);
	iEvent.put(std::move(htp));
	
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HTDouble::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HTDouble);
