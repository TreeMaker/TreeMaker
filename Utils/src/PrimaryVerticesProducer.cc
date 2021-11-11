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
#include "DataFormats/Math/interface/Point3D.h"

//
// class declaration
//
class VertexInfos {
public:
	VertexInfos() {
		vtx_ref      = std::make_unique<std::vector<reco::VertexRef>>();
		vtx_position = std::make_unique<std::vector<math::XYZPoint>>();
		vtx_time     = std::make_unique<std::vector<double>>();
		vtx_isValid  = std::make_unique<std::vector<bool>>();
		vtx_isFake   = std::make_unique<std::vector<bool>>();
		vtx_isGood   = std::make_unique<std::vector<bool>>();
		vtx_ndof     = std::make_unique<std::vector<double>>();
		vtx_chi2     = std::make_unique<std::vector<double>>();
		vtx_xError   = std::make_unique<std::vector<double>>();
		vtx_yError   = std::make_unique<std::vector<double>>();
		vtx_zError   = std::make_unique<std::vector<double>>();
		vtx_tError   = std::make_unique<std::vector<double>>();
		vtx_ntracks  = std::make_unique<std::vector<int>>();
	}

	void fill(const reco::Vertex & vertex, bool good) {
		vtx_position->push_back(vertex.position());
		vtx_time->push_back(vertex.t());
		vtx_isValid->push_back(vertex.isValid());
		vtx_isFake->push_back(vertex.isFake());
		vtx_isGood->push_back(good);
		vtx_ndof->push_back(vertex.ndof());
		vtx_chi2->push_back(vertex.chi2());
		vtx_xError->push_back(vertex.xError());
		vtx_yError->push_back(vertex.yError());
		vtx_zError->push_back(vertex.zError());
		vtx_tError->push_back(vertex.tError());
		vtx_ntracks->push_back(vertex.nTracks());
	}

	void fillRef(const edm::Handle<reco::VertexCollection> & vertices, size_t i) {
		vtx_ref->push_back(reco::VertexRef(vertices, i));
	}

	void put(edm::Event & iEvent) {
		iEvent.put(std::move(vtx_ref),      "vtxref");
		iEvent.put(std::move(vtx_position), "vtxposition");
		iEvent.put(std::move(vtx_time),     "vtxtime");
		iEvent.put(std::move(vtx_isValid),  "vtxisValid");
		iEvent.put(std::move(vtx_isFake),   "vtxisFake");
		iEvent.put(std::move(vtx_isGood),   "vtxisGood");
		iEvent.put(std::move(vtx_ndof),     "vtxndof");
		iEvent.put(std::move(vtx_chi2),     "vtxchi2");
		iEvent.put(std::move(vtx_xError),   "vtxxError");
		iEvent.put(std::move(vtx_yError),   "vtxyError");
		iEvent.put(std::move(vtx_zError),   "vtxzError");
		iEvent.put(std::move(vtx_tError),   "vtxtError");
		iEvent.put(std::move(vtx_ntracks),  "vtxntracks");
	}

// ----------member data ---------------------------
	std::unique_ptr<std::vector<reco::VertexRef>> vtx_ref;
	std::unique_ptr<std::vector<math::XYZPoint>> vtx_position;
	std::unique_ptr<std::vector<bool>> vtx_isValid, vtx_isFake, vtx_isGood;
	std::unique_ptr<std::vector<double>> vtx_time, vtx_ndof, vtx_chi2, vtx_xError, vtx_yError, vtx_zError, vtx_tError;
	std::unique_ptr<std::vector<int>> vtx_ntracks;
};

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
	bool saveVertices_;
};

//
// constructors and destructor
//
PrimaryVerticesProducer::PrimaryVerticesProducer(const edm::ParameterSet& iConfig) :
vertexCollectionTag_(iConfig.getParameter<edm::InputTag>("VertexCollection")),
goodVertexCollectionTag_(iConfig.getParameter<edm::InputTag>("GoodVertexCollection")),
vertexCollectionTok_(consumes<reco::VertexCollection>(vertexCollectionTag_)),
goodVertexCollectionTok_(consumes<reco::VertexCollection>(goodVertexCollectionTag_)),
saveVertices_(iConfig.getParameter<bool>("saveVertices"))
{	
	produces<int>("NVtx");
	produces<int>("nAllVertices");
	if (saveVertices_) {
		produces<std::vector<reco::VertexRef> >("vtxref");
		produces<std::vector<math::XYZPoint> > ("vtxposition");
		produces<std::vector<double> >         ("vtxtime");
		produces<std::vector<bool> >           ("vtxisValid");
		produces<std::vector<bool> >           ("vtxisFake");
		produces<std::vector<bool> >           ("vtxisGood");
		produces<std::vector<double> >         ("vtxndof");
		produces<std::vector<double> >         ("vtxchi2");
		produces<std::vector<double> >         ("vtxxError");
		produces<std::vector<double> >         ("vtxyError");
		produces<std::vector<double> >         ("vtxzError");
		produces<std::vector<double> >         ("vtxtError");
		produces<std::vector<int> >            ("vtxntracks");
	}
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
	edm::Handle<reco::VertexCollection> vertices, goodVertices;
	int nVertices=0, nGoodVertices=0;

	iEvent.getByToken(vertexCollectionTok_,vertices);
	if( vertices.isValid() ) {
		nVertices = vertices->size();
	}
	else edm::LogWarning("TreeMaker")<<"Warning VertexCollection Tag not valid: "<<vertexCollectionTag_;
	auto nVerticesPtr     = std::make_unique<int>(nVertices);

	iEvent.getByToken(goodVertexCollectionTok_,goodVertices);
	if( goodVertices.isValid() ) {
		nGoodVertices = goodVertices->size();
	}
	else edm::LogWarning("TreeMaker")<<"Warning VertexCollection Tag not valid: "<<goodVertexCollectionTag_;
	auto nGoodVerticesPtr = std::make_unique<int>(nGoodVertices);

	VertexInfos infos;
	if (saveVertices_){
		for (size_t i=0; i<vertices->size();i++) {
			const reco::Vertex& vertex = (*vertices)[i];

			reco::VertexCollection::const_iterator it;
			it = std::find_if(goodVertices->begin(), goodVertices->end(), [&vertex](reco::Vertex const& obj){
					return obj.position() == vertex.position();
				} );

			infos.fill(vertex,it!=goodVertices->end());
			infos.fillRef(vertices,i);
		}
		infos.put(iEvent);
	}

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
