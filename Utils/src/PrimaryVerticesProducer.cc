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

class PrimaryVerticesProducer : public edm::global::EDProducer<> {
public:
	explicit PrimaryVerticesProducer(const edm::ParameterSet&);
	~PrimaryVerticesProducer() override;
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

	// ----------member data ---------------------------
	edm::InputTag vertexCollectionTag_, goodVertexCollectionTag_;
	edm::EDGetTokenT<reco::VertexCollection> vertexCollectionTok_, goodVertexCollectionTok_;
};

//
// constructors and destructor
//
PrimaryVerticesProducer::PrimaryVerticesProducer(const edm::ParameterSet& iConfig) :
vertexCollectionTag_(iConfig.getParameter<edm::InputTag>("VertexCollection")),
goodVertexCollectionTag_(iConfig.getParameter<edm::InputTag>("GoodVertexCollection")),
vertexCollectionTok_(consumes<reco::VertexCollection>(vertexCollectionTag_)),
goodVertexCollectionTok_(consumes<reco::VertexCollection>(goodVertexCollectionTag_))
{	
	produces<int>("NVtx");
	produces<int>("nAllVertices");
}


PrimaryVerticesProducer::~PrimaryVerticesProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PrimaryVerticesProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	edm::Handle<reco::VertexCollection> vertices;
	int nVertices=0, nGoodVertices=0;

	iEvent.getByToken(vertexCollectionTok_,vertices);
	if( vertices.isValid() ) {
		nVertices = vertices->size();
	}
	else edm::LogWarning("TreeMaker")<<"Warning VertexCollection Tag not valid: "<<vertexCollectionTag_;

	iEvent.getByToken(goodVertexCollectionTok_,vertices);
	if( vertices.isValid() ) {
		nGoodVertices = vertices->size();
	}
	else edm::LogWarning("TreeMaker")<<"Warning VertexCollection Tag not valid: "<<goodVertexCollectionTag_;

	auto nVerticesPtr     = std::make_unique<int>(nVertices);
	auto nGoodVerticesPtr = std::make_unique<int>(nGoodVertices);
	iEvent.put(std::move(nVerticesPtr    ), "nAllVertices");
	iEvent.put(std::move(nGoodVerticesPtr), "NVtx");
	
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PrimaryVerticesProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PrimaryVerticesProducer);
