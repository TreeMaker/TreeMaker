// -*- C++ -*-
//
// Package:    PuppiJetsAK8Producer
// Class:      PuppiJetsAK8Producer
// 
/**\class PuppiJetsAK8Producer PuppiJetsAK8Producer.cc RA2Classic/PuppiJetsAK8Producer/src/PuppiJetsAK8Producer.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Andrew Whitbeck
//         Created:  January 19, 2017
// $Id$
//
//

// root include files
#include "TLorentzVector.h"

// system include files
#include <memory>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

class PuppiJetsAK8Producer : public edm::EDProducer {
public:
	explicit PuppiJetsAK8Producer(const edm::ParameterSet&);
	~PuppiJetsAK8Producer();
	
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
	edm::InputTag SubJetTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
	edm::EDGetTokenT<edm::View<pat::Jet>> SubJetTok_;
	bool debug;
};

//
// constructors and destructor
//
PuppiJetsAK8Producer::PuppiJetsAK8Producer(const edm::ParameterSet& iConfig)
{
    
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
	SubJetTag_ = iConfig.getParameter<edm::InputTag>("SubJetTag");
	SubJetTok_ = consumes<edm::View<pat::Jet>>(SubJetTag_);
	debug = iConfig.getParameter<bool>("debug");

    produces< std::vector< TLorentzVector > >();
    produces< std::vector< double > >("softDropMass");
    
}

PuppiJetsAK8Producer::~PuppiJetsAK8Producer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PuppiJetsAK8Producer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    auto puppiJets = std::make_unique<std::vector<TLorentzVector> >();
    auto puppiSoftDropMass = std::make_unique<std::vector<double> >();

    TLorentzVector tempJet(0.,0.,0.,0.);
	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);

	if( Jets.isValid() ) {
		for(auto Jet = Jets->begin();  Jet != Jets->end(); ++Jet){
            tempJet.SetPtEtaPhiE(Jet->userFloat("ak8PFJetsPuppiValueMap:pt"),
                                 Jet->userFloat("ak8PFJetsPuppiValueMap:eta"),
                                 Jet->userFloat("ak8PFJetsPuppiValueMap:phi"),
                                 Jet->userFloat("ak8PFJetsPuppiValueMap:mass")
                                 );
            
            puppiJets->push_back(tempJet);

            TLorentzVector puppi_softdrop, puppi_softdrop_subjet;
            auto const & sdSubjetsPuppi = Jet->subjets("SoftDropPuppi");
            for ( auto const & it : sdSubjetsPuppi ) {
                puppi_softdrop_subjet.SetPtEtaPhiM(it->pt(),it->eta(),it->phi(),it->mass());
                puppi_softdrop+=puppi_softdrop_subjet;
            }
            puppiSoftDropMass->push_back(puppi_softdrop.M());
		}
	}

    iEvent.put(std::move(puppiJets));
    iEvent.put(std::move(puppiSoftDropMass),"softDropMass");
}

// ------------ method called once each job just before starting event loop  ------------
void 
PuppiJetsAK8Producer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PuppiJetsAK8Producer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
PuppiJetsAK8Producer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PuppiJetsAK8Producer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PuppiJetsAK8Producer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PuppiJetsAK8Producer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PuppiJetsAK8Producer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PuppiJetsAK8Producer);
