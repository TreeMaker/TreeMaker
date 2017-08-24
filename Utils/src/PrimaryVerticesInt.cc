// -*- C++ -*-
//
// Package:    PrimaryVerticesInt
// Class:      PrimaryVerticesInt
// 
/**\class PrimaryVerticesInt PrimaryVerticesInt.cc RA2Classic/PrimaryVerticesInt/src/PrimaryVerticesInt.cc
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
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

//
// class declaration
//

class PrimaryVerticesInt : public edm::global::EDProducer<> {
public:
	explicit PrimaryVerticesInt(const edm::ParameterSet&);
	~PrimaryVerticesInt();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

	// ----------member data ---------------------------
	edm::InputTag vertexCollectionTag_;
	edm::EDGetTokenT<reco::VertexCollection> vertexCollectionTok_;
};

//
// constructors and destructor
//
PrimaryVerticesInt::PrimaryVerticesInt(const edm::ParameterSet& iConfig)
{
	//register your products
	vertexCollectionTag_ = iConfig.getParameter<edm::InputTag>("VertexCollection");
	vertexCollectionTok_ = consumes<reco::VertexCollection>(vertexCollectionTag_);
	
	produces<int>("");
}


PrimaryVerticesInt::~PrimaryVerticesInt()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PrimaryVerticesInt::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	using namespace edm;
	int nVertices=0;
	edm::Handle<reco::VertexCollection> vertices;
	iEvent.getByToken(vertexCollectionTok_,vertices);
	if( vertices.isValid() ) {
		nVertices = vertices->size();
	}
	else edm::LogWarning("TreeMaker")<<"Warning VertexCollection Tag not valid: "<<vertexCollectionTag_.label();
	auto htp = std::make_unique<int>(nVertices);
	iEvent.put(std::move(htp));
	
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PrimaryVerticesInt::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PrimaryVerticesInt);
