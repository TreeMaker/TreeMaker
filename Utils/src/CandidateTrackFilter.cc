// system include files
#include <memory>

// CMSSW include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/Point3D.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"

#include "Math/VectorUtil.h"
#include "TMath.h"

using namespace std;

//
// class declarations
//
class TrackInfos {
public:
	TrackInfos() {
		trks                         = std::make_unique<vector<math::XYZVector>>();
		trks_referencepoint          = std::make_unique<vector<math::XYZPoint>>();
		trks_chg                     = std::make_unique<vector<int>>();
		trks_dzpv                    = std::make_unique<vector<double>>();
		trks_dzerrorpv               = std::make_unique<vector<double>>();
		trks_dxypv                   = std::make_unique<vector<double>>();
		trks_dxyerrorpv              = std::make_unique<vector<double>>();
		trks_normalizedchi2          = std::make_unique<vector<double>>();
		trks_pterror                 = std::make_unique<vector<double>>();
		trks_etaerror                = std::make_unique<vector<double>>();
		trks_phierror                = std::make_unique<vector<double>>();
		trks_qoverperror             = std::make_unique<vector<double>>();
		trks_ip2d                    = std::make_unique<vector<double>>();
		trks_ip2dsig                 = std::make_unique<vector<double>>();
		trks_ip3d                    = std::make_unique<vector<double>>();
		trks_ip3dsig                 = std::make_unique<vector<double>>();
		trks_found                   = std::make_unique<vector<int>>();
		trks_lost                    = std::make_unique<vector<int>>();
		trks_quality                 = std::make_unique<vector<int>>();
		trks_hitpattern              = std::make_unique<vector<vector<int>>>();
		trks_matchedtopfcand         = std::make_unique<vector<bool>>();
		pfcands_numberofhits         = std::make_unique<vector<int>>();
		pfcands_numberofpixelhits    = std::make_unique<vector<int>>();
		pfcands_firsthit             = std::make_unique<vector<int>>();
		pfcands_frompv               = std::make_unique<vector<int>>();
		pfcands_pvassociationquality = std::make_unique<vector<int>>();
		pfcands_dzassociatedpv       = std::make_unique<vector<double>>();
		pfcands_vtxidx               = std::make_unique<vector<int>>();
	}

	void fill(const reco::Vertex & primaryVertex, const pat::PackedCandidate & pfCand,
	          const reco::Track & track, const reco::TransientTrack & transientTrack,
	          bool trackMatch, int vtxIdx) {
		// basic information from the reco::Track
		//   Reference: https://github.com/cms-sw/cmssw/blob/master/DataFormats/TrackReco/interface/Track.h
		trks->push_back(track.momentum());
		trks_referencepoint->push_back(track.referencePoint());
		trks_chg->push_back(track.charge());
		trks_dzpv->push_back(track.dz()); //returns the ip wrt PV[0] 
		trks_dzerrorpv->push_back(track.dzError());
		trks_dxypv->push_back(track.dxy());
		trks_dxyerrorpv->push_back(track.dxyError());
		trks_normalizedchi2->push_back(track.normalizedChi2());
		trks_pterror->push_back(track.ptError());
		trks_etaerror->push_back(track.etaError());
		trks_phierror->push_back(track.phiError());
		trks_qoverperror->push_back(track.qoverpError());
		trks_found->push_back(track.found());
		trks_lost->push_back(track.lost());
		// track quality enum:
		//    Reference: https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_11_patch1/DataFormats/TrackReco/interface/TrackBase.h#L151-L162
		//      undefQuality = -1,
		//      loose = 0,
		//      tight = 1,
		//      highPurity = 2,
		//      confirmed = 3,  // means found by more than one iteration
		//      goodIterative = 4,  // meaningless
		//      looseSetWithPV = 5,
		//      highPuritySetWithPV = 6,
		//      discarded = 7, // because a better track found. kept in the collection for reference....
		//      qualitySize = 8
		trks_quality->push_back(track.qualityMask());
		// impact parameter variables
		std::pair<bool,Measurement1D> ip2d = IPTools::absoluteTransverseImpactParameter(transientTrack, primaryVertex);
		std::pair<bool,Measurement1D> ip3d = IPTools::absoluteImpactParameter3D(transientTrack, primaryVertex);
		trks_ip2d->push_back(ip2d.second.value());
		trks_ip2dsig->push_back(ip2d.second.significance());
		trks_ip3d->push_back(ip3d.second.value());
		trks_ip3dsig->push_back(ip3d.second.significance());
		// hit pattern of the track:
		//   Reference: https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_11_patch1/DataFormats/TrackReco/interface/HitPattern.h
		const reco::HitPattern &hp = track.hitPattern();
		auto nhits = hp.numberOfAllHits(reco::HitPattern::TRACK_HITS);
		auto hits = vector<int>(nhits,0);
		for (auto ih=0; ih<nhits; ih++) {
			hits[ih] = hp.getHitPattern(reco::HitPattern::TRACK_HITS, ih);
		} // for(track hits)
		trks_hitpattern->push_back(hits);
		trks_matchedtopfcand->push_back(trackMatch);

		// information from the pat::PackedCandidate
		//   Reference: https://github.com/cms-sw/cmssw/blob/master/DataFormats/ParticleFlowCandidate/interface/PFCandidate.h
		pfcands_numberofhits->push_back(pfCand.numberOfHits());
		pfcands_numberofpixelhits->push_back(pfCand.numberOfPixelHits());
		pfcands_firsthit->push_back(pfCand.firstHit());
		pfcands_frompv->push_back(pfCand.fromPV()); //fromPV() returns a number between 3 and 0 to define how tight the association with the PV is
		pfcands_pvassociationquality->push_back(pfCand.pvAssociationQuality());
		pfcands_dzassociatedpv->push_back(pfCand.dzAssociatedPV()); //returns the ip wrt the PV associated to this candidate
		pfcands_vtxidx->push_back(vtxIdx);
	}

	void put(edm::Event & iEvent) {
		iEvent.put(std::move(trks                        ), "trks");
		iEvent.put(std::move(trks_referencepoint         ), "trksreferencepoint");
		iEvent.put(std::move(trks_chg                    ), "trkschg");
		iEvent.put(std::move(trks_dzpv                   ), "trksdzpv");
		iEvent.put(std::move(trks_dzerrorpv              ), "trksdzerrorpv");
		iEvent.put(std::move(trks_dxypv                  ), "trksdxypv");
		iEvent.put(std::move(trks_dxyerrorpv             ), "trksdxyerrorpv");
		iEvent.put(std::move(trks_normalizedchi2         ), "trksnormalizedchi2");
		iEvent.put(std::move(trks_pterror                ), "trkspterror");
		iEvent.put(std::move(trks_etaerror               ), "trksetaerror");
		iEvent.put(std::move(trks_phierror               ), "trksphierror");
		iEvent.put(std::move(trks_qoverperror            ), "trksqoverperror");
		iEvent.put(std::move(trks_ip2d                   ), "trksip2d");
		iEvent.put(std::move(trks_ip2dsig                ), "trksip2dsig");
		iEvent.put(std::move(trks_ip3d                   ), "trksip3d");
		iEvent.put(std::move(trks_ip3dsig                ), "trksip3dsig");
		iEvent.put(std::move(trks_found                  ), "trksfound");
		iEvent.put(std::move(trks_lost                   ), "trkslost");
		iEvent.put(std::move(trks_quality                ), "trksquality");
		iEvent.put(std::move(trks_hitpattern             ), "trkshitpattern");
		iEvent.put(std::move(trks_matchedtopfcand        ), "trksmatchedtopfcand");
		iEvent.put(std::move(pfcands_numberofhits        ), "pfcandsnumberofhits");
		iEvent.put(std::move(pfcands_numberofpixelhits   ), "pfcandsnumberofpixelhits");
		iEvent.put(std::move(pfcands_firsthit            ), "pfcandsfirsthit");
		iEvent.put(std::move(pfcands_frompv              ), "pfcandsfrompv");
		iEvent.put(std::move(pfcands_pvassociationquality), "pfcandspvassociationquality");
		iEvent.put(std::move(pfcands_dzassociatedpv      ), "pfcandsdzassociatedpv");
		iEvent.put(std::move(pfcands_vtxidx              ), "pfcandsvtxidx");
	}

	// ----------member data ---------------------------
	std::unique_ptr<vector<math::XYZVector>> trks;
	std::unique_ptr<vector<math::XYZPoint>> trks_referencepoint;
	std::unique_ptr<vector<bool>> trks_matchedtopfcand;
	std::unique_ptr<vector<double>> trks_dzpv,trks_dzerrorpv,trks_dxypv,trks_dxyerrorpv,trks_normalizedchi2,trks_pterror,trks_etaerror,
									trks_phierror,trks_qoverperror,trks_ip2d,trks_ip2dsig,trks_ip3d,trks_ip3dsig, pfcands_dzassociatedpv;
	std::unique_ptr<vector<int>> trks_chg, trks_found, trks_lost, trks_quality, pfcands_numberofhits, pfcands_numberofpixelhits,
								 pfcands_firsthit, pfcands_frompv, pfcands_pvassociationquality, pfcands_vtxidx;
	std::unique_ptr<vector<vector<int>>> trks_hitpattern;
};

class CandidateTrackFilter : public edm::global::EDFilter<> {
public:
	explicit CandidateTrackFilter (const edm::ParameterSet&);
	~CandidateTrackFilter() override;

private:
	bool filter(edm::StreamID, edm::Event & iEvent, const edm::EventSetup & iSetup) const override;
	bool filterOnTrack(const pat::PackedCandidate & pfCand, const reco::Track & track) const;
	int  getVertexIndex(const pat::PackedCandidate & pfCand, const edm::Handle<edm::View<reco::VertexRef> > & goodVertices) const;
	void loopOverCollection(TrackInfos & infos, const edm::Handle<edm::View<pat::PackedCandidate> > & collection,
							const edm::ESHandle<TransientTrackBuilder> & ttBuilder,
							const reco::Vertex & primaryVertex, const edm::Handle<edm::View<reco::VertexRef> > & goodVertices,
							bool trackMatch) const;

	// ----------member data ---------------------------
	edm::InputTag pfCandidatesTag_;
	edm::InputTag lostTracksTag_;
	edm::InputTag lostEleTracksTag_;
	edm::InputTag displacedStandAloneMuonsTag_;
	edm::InputTag vertexInputTag_;
	edm::InputTag storedVerticesTag_;
	edm::EDGetTokenT<edm::View<pat::PackedCandidate>> pfCandidatesTok_;
	edm::EDGetTokenT<edm::View<pat::PackedCandidate>> lostTracksTok_;
	edm::EDGetTokenT<edm::View<pat::PackedCandidate>> lostEleTracksTok_;
	edm::EDGetTokenT<edm::View<pat::PackedCandidate>> displacedStandAloneMuonsTok_;
	edm::EDGetTokenT<edm::View<reco::Vertex>> vertexInputTok_;
	edm::EDGetTokenT<edm::View<reco::VertexRef>> storedVerticesTok_;

	double minPt_, maxEta_, maxdz_, maxdxy_, maxnormchi2_;
	bool debug_, doFilter_, doDisplacedMuons_;
};

//
// constructors and destructor
//
CandidateTrackFilter::CandidateTrackFilter(const edm::ParameterSet& iConfig) : 
	pfCandidatesTag_            (iConfig.getParameter<edm::InputTag>("pfCandidatesTag")),
	lostTracksTag_              (iConfig.getParameter<edm::InputTag>("lostTracksTag")),
	lostEleTracksTag_           (iConfig.getParameter<edm::InputTag>("lostEleTracksTag")),
	vertexInputTag_             (iConfig.getParameter<edm::InputTag>("vertexInputTag")),
	storedVerticesTag_          (iConfig.getParameter<edm::InputTag>("storedVerticesTag")),
	minPt_                      (iConfig.getParameter<double>       ("minPt")),
	maxEta_                     (iConfig.getParameter<double>       ("maxEta")),
	maxdz_                      (iConfig.getParameter<double>       ("maxdz")),
	maxdxy_                     (iConfig.getParameter<double>       ("maxdxy")),
	maxnormchi2_                (iConfig.getParameter<double>       ("maxnormchi2")),
	debug_                      (iConfig.getParameter<bool>         ("debug")),
	doFilter_                   (iConfig.getParameter<bool>         ("doFilter")),
	doDisplacedMuons_           (false)
{	
	pfCandidatesTok_             = consumes<edm::View<pat::PackedCandidate>>(pfCandidatesTag_);
	lostTracksTok_               = consumes<edm::View<pat::PackedCandidate>>(lostTracksTag_);
	lostEleTracksTok_            = consumes<edm::View<pat::PackedCandidate>>(lostEleTracksTag_);
	vertexInputTok_              = consumes<edm::View<reco::Vertex>>(vertexInputTag_);
	storedVerticesTok_           = consumes<edm::View<reco::VertexRef>>(storedVerticesTag_);

	if (iConfig.exists("displacedStandAloneMuonsTag")) {
		displacedStandAloneMuonsTag_ = iConfig.getParameter<edm::InputTag>("displacedStandAloneMuonsTag"),
		displacedStandAloneMuonsTok_ = consumes<edm::View<pat::PackedCandidate>>(displacedStandAloneMuonsTag_);
		doDisplacedMuons_ = true;
	}

	produces<std::vector<pat::PackedCandidate> >(""); 
	produces<vector<math::XYZVector> >          ("trks");
	produces<vector<math::XYZPoint> >           ("trksreferencepoint");
	produces<vector<int> >                      ("trkschg");
	produces<vector<double> >                   ("trksdzpv");
	produces<vector<double> >                   ("trksdzerrorpv");
	produces<vector<double> >                   ("trksdxypv");
	produces<vector<double> >                   ("trksdxyerrorpv");
	produces<vector<double> >                   ("trksnormalizedchi2");
	produces<vector<double> >                   ("trkspterror");
	produces<vector<double> >                   ("trksetaerror");
	produces<vector<double> >                   ("trksphierror");
	produces<vector<double> >                   ("trksqoverperror");
	produces<vector<double> >                   ("trksip2d");
	produces<vector<double> >                   ("trksip2dsig");
	produces<vector<double> >                   ("trksip3d");
	produces<vector<double> >                   ("trksip3dsig");
	produces<vector<int> >                      ("trksfound");
	produces<vector<int> >                      ("trkslost");
	produces<vector<int> >                      ("trksquality");
	produces<vector<vector<int>> >              ("trkshitpattern");
	produces<vector<bool> >                     ("trksmatchedtopfcand");
	produces<vector<int> >                      ("pfcandsnumberofhits");
	produces<vector<int> >                      ("pfcandsnumberofpixelhits");
	produces<vector<int> >                      ("pfcandsfirsthit");
	produces<vector<int> >                      ("pfcandsfrompv");
	produces<vector<int> >                      ("pfcandspvassociationquality");
	produces<vector<double> >                   ("pfcandsdzassociatedpv");
	produces<vector<int> >                      ("pfcandsvtxidx");
}

CandidateTrackFilter::~CandidateTrackFilter() {

}

// ------------ method called to produce the data  ------------
bool CandidateTrackFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
	TrackInfos infos;

	//-------------------------------------------------------------------------------------------------
	// get Vertex Collection
	//-------------------------------------------------------------------------------------------------
	edm::Handle<edm::View<reco::Vertex> > vertices;
	iEvent.getByToken(vertexInputTok_, vertices);
	bool hasGoodVtx = false;
	if (!vertices->empty()) hasGoodVtx = true;
	auto primaryVertex = vertices->at(0); //IS THIS THE PRIMARY VERTEX?

	//-------------------------------------------------------------------------------------------------
	// skip events with no good vertices
	//-------------------------------------------------------------------------------------------------
	if(!hasGoodVtx) return false;

	//-------------------------------------------------------------------------------------------------
	// get the Good Vertices Collection
	//-------------------------------------------------------------------------------------------------
	edm::Handle<edm::View<reco::VertexRef> > storedVertices;
	iEvent.getByToken(storedVerticesTok_, storedVertices);

	//-------------------------------------------------------------------------------------------------
	// get TransientTrackBuilder from the EventSetup
	//-------------------------------------------------------------------------------------------------
	// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideTransientTracks
	edm::ESHandle<TransientTrackBuilder> ttBuilder;
	iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",ttBuilder);

	//-------------------------------------------------------------------------------------------------
	// get the various track containing collections
	//-------------------------------------------------------------------------------------------------
	edm::Handle<edm::View<pat::PackedCandidate> > pfCandidates;
	edm::Handle<edm::View<pat::PackedCandidate> > lostTracks;
	edm::Handle<edm::View<pat::PackedCandidate> > lostEleTracks;
	iEvent.getByToken(pfCandidatesTok_, pfCandidates);
	iEvent.getByToken(lostTracksTok_, lostTracks);
	iEvent.getByToken(lostEleTracksTok_, lostEleTracks);

	//-------------------------------------------------------------------------------------------------
	// loop over the various track containing collections
	//-------------------------------------------------------------------------------------------------
	if( pfCandidates.isValid() ){
		loopOverCollection(infos,pfCandidates,ttBuilder,primaryVertex,storedVertices,true);
	} else {
		edm::LogWarning("TreeMaker")<<"CandidateTrackFilter: Collection "<<pfCandidatesTag_<<" not found!";
	}

	if( lostTracks.isValid() ){
		loopOverCollection(infos,lostTracks,ttBuilder,primaryVertex,storedVertices,false);
	} else {
		edm::LogWarning("TreeMaker")<<"CandidateTrackFilter: Collection "<<lostTracksTag_<<" not found!";
	}

	if( lostEleTracks.isValid() ){
		loopOverCollection(infos,lostEleTracks,ttBuilder,primaryVertex,storedVertices,false);
	} else {
		edm::LogWarning("TreeMaker")<<"CandidateTrackFilter: Collection "<<lostEleTracksTag_<<" not found!";
	}

	if (doDisplacedMuons_) {
		//-------------------------------------------------------------------------------------------------
		// get displacedStandAloneMuons collection
		//-------------------------------------------------------------------------------------------------
		edm::Handle<edm::View<pat::PackedCandidate> > displacedStandAloneMuons;
		iEvent.getByToken(displacedStandAloneMuonsTok_, displacedStandAloneMuons);

		//-------------------------------------------------------------------------------------------------
		// loop over displacedStandAloneMuons
		//-------------------------------------------------------------------------------------------------
		loopOverCollection(infos,displacedStandAloneMuons,ttBuilder,primaryVertex,storedVertices,false); //Do these overlap with the packedPFCandidate collection? Are they matched?
	}

	//-------------------------------------------------------------------------------------------------
	// put track/PFCandidate values back into event
	//-------------------------------------------------------------------------------------------------
	bool result = (doFilter_) ? !infos.trks->empty() : true;
	infos.put(iEvent);
	return result;
}

// ------------ other methods  ------------
bool CandidateTrackFilter::filterOnTrack(const pat::PackedCandidate & pfCand, const reco::Track & track) const {
	return (track.pt() >= minPt_) && (std::abs(track.eta()) < maxEta_) && // cut on track pT and eta
		   (std::abs(track.dz()) <= maxdz_) && (std::abs(track.dxy()) <= maxdxy_) && // cut on impact parameter quantities
		   (std::abs(track.normalizedChi2()) <= maxnormchi2_); // cut on chi2
}

int CandidateTrackFilter::getVertexIndex(const pat::PackedCandidate & pfCand, const edm::Handle<edm::View<reco::VertexRef> > & storedVertices) const {
	auto it = std::find_if(storedVertices->begin(), storedVertices->end(), [&pfCand](reco::VertexRef const& obj){
					return obj == pfCand.vertexRef();
				} );
	if(it!=storedVertices->end()) return std::distance(storedVertices->begin(),it);
	else return -1;
}

void CandidateTrackFilter::loopOverCollection(TrackInfos & infos, const edm::Handle<edm::View<pat::PackedCandidate> > & collection,
											  const edm::ESHandle<TransientTrackBuilder> & ttBuilder,
											  const reco::Vertex & primaryVertex, const edm::Handle<edm::View<reco::VertexRef> > & storedVertices,
											  bool trackMatch) const {
	//-------------------------------------------------------------------------------------------------
	// loop over PFCandidates
	//-------------------------------------------------------------------------------------------------
	for (size_t i=0; i<collection->size();i++) {
		const pat::PackedCandidate pfCand = (*collection)[i];

		//-------------------------------------------------------------------------------------------------
		// pull the track details, if available
		//-------------------------------------------------------------------------------------------------
		if (!pfCand.hasTrackDetails()) continue;
		auto track = pfCand.pseudoTrack();

		//-------------------------------------------------------------------------------------------------
		// place some minimal cuts on the tracks
		//-------------------------------------------------------------------------------------------------
		if (!filterOnTrack(pfCand,track)) continue;

		//-------------------------------------------------------------------------------------------------
		// find the index of the associated vertex in the good vertices collection
		//-------------------------------------------------------------------------------------------------
		int vtxIdx = getVertexIndex(pfCand,storedVertices);

		//-------------------------------------------------------------------------------------------------
		// fill the track values and PFCandidate values we'd like to save
		//-------------------------------------------------------------------------------------------------
		auto transientTrack = ttBuilder->build(track);
		infos.fill(primaryVertex,pfCand,track,transientTrack,trackMatch,vtxIdx);
	}
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateTrackFilter);
