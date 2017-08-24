// -*- C++ -*-
//
// Package:    NJetInt
// Class:      NJetInt
// 
/**\class NJetInt NJetInt.cc RA2Classic/NJetInt/src/NJetInt.cc
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
#include "DataFormats/PatCandidates/interface/Jet.h"
//
// class declaration
//

class NJetInt : public edm::global::EDProducer<> {
public:
	explicit NJetInt(const edm::ParameterSet&);
	~NJetInt();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
	// ----------member data ---------------------------
	edm::InputTag JetTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
};

//
// constructors and destructor
//
NJetInt::NJetInt(const edm::ParameterSet& iConfig)
{
	//register your product
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
	
	produces<int>("");
}


NJetInt::~NJetInt()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
NJetInt::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	using namespace edm;
	int NJets=0;
	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);
	if( Jets.isValid() ) {
	  	     	
		//NJets=Jets->size();
		for(unsigned int j=0; j<Jets->size(); ++j){
			++NJets;
		}
	}
	else edm::LogWarning("TreeMaker")<<"NJetInt::Invalid Tag: "<<JetTag_.label();
	auto htp = std::make_unique<int>(NJets);
	iEvent.put(std::move(htp));
	
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
NJetInt::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NJetInt);
