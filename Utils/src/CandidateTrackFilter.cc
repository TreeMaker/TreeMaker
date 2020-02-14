//-----------------------------------------------------------------------------------------
//
// Computation of the trackIsolation, for use with the isolated track veto 
// used for the stop quark search in the single lepton channel
// Author: Ben Hooberman
//
// For each PFCandidate above threshold minPt_PFCandidate store 4 quantities:
// pT of PFCandidate
// charge of PFCandidate
// dz of PFCandidate w.r.t. the 1st good vertex
// the trackIsolation value
//
// In the analysis, we veto any event containing IN ADDITION TO the selected lepton a charged PFCandidate with:
// pT > 10 GeV, dz < 0.05 cm, and trackIso/pT < 0.1
//
//-----------------------------------------------------------------------------------------

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
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "Math/VectorUtil.h"
#include "TMath.h"
#include "TLorentzVector.h"

//using namespace reco;
//using namespace edm;
using namespace std;

//
// class declaration
//
class CandidateTrackFilter : public edm::global::EDFilter<> {
public:
	explicit CandidateTrackFilter (const edm::ParameterSet&);
	~CandidateTrackFilter() override;

private:
	bool filter(edm::StreamID, edm::Event & iEvent, const edm::EventSetup & iSetup) const override;

	// ----------member data ---------------------------
	edm::InputTag pfCandidatesTag_;
	edm::InputTag vertexInputTag_;
	edm::EDGetTokenT<edm::View<pat::PackedCandidate>> pfCandidatesTok_;
	edm::EDGetTokenT<edm::View<reco::Vertex>> vertexInputTok_;

	double minPt_;
	double maxEta_;
	double maxdz_;
	double maxdxy_;
	double maxnormchi2_;
	bool debug_;
};

//
// constructors and destructor
//
CandidateTrackFilter::CandidateTrackFilter(const edm::ParameterSet& iConfig) : 
	pfCandidatesTag_(iConfig.getParameter<edm::InputTag>("pfCandidatesTag")),
	vertexInputTag_ (iConfig.getParameter<edm::InputTag>("vertexInputTag")),
	minPt_          (iConfig.getParameter<double>       ("minPt")),
	maxEta_         (iConfig.getParameter<double>       ("maxEta")),
	maxdz_          (iConfig.getParameter<double>       ("maxdz")),
	maxdxy_         (iConfig.getParameter<double>       ("maxdxy")),
	maxnormchi2_    (iConfig.getParameter<double>       ("maxnormchi2")),
	debug_          (iConfig.getParameter<bool>         ("debug"))
{	
	pfCandidatesTok_ = consumes<edm::View<pat::PackedCandidate>>(pfCandidatesTag_);
	vertexInputTok_ = consumes<edm::View<reco::Vertex>>(vertexInputTag_);
	
	produces<std::vector<pat::PackedCandidate> >(""); 
	produces<vector<TLorentzVector> >("trks");
	produces<vector<int> >   ("trkschg");
	produces<vector<double> >("trksdzpv");
	produces<vector<double> >("trksdzerrorpv");
	produces<vector<double> >("trksdxypv");
	produces<vector<double> >("trksdxyerrorpv");
	produces<vector<int> >   ("trksnormalizedchi2");
	produces<vector<int> >   ("trksfound");
	produces<vector<int> >   ("trkslost");
	//produces<vector<bool> >  ("trksquality");
	produces<vector<int> >   ("pfcandsnumberofhits");
	produces<vector<int> >   ("pfcandsnumberofpixelhits");

	/*
	For charged packed PF candidates with pT > 0.5 GeV, additional information is stored with different precision (high precision for pt > 0.95 GeV, low precision for 0.5 GeV < pt < 0.95 GeV )

    the uncertainty on the impact parameter dzError(), dxyError()
    the number of hits and pixel hits on the track (numberOfHits(), numberOfPixelHits())
    the number of layers with hits on the track
    the sub/det and layer of first hit of the track
    the reco::Track of the candidate is provided by the pseudoTrack() method, with:
        the pt,eta and phi of the original track (if those are different from the one of the original PFCandidate)
        an approximate covariance matrix of the track state at the vertex
        approximate hitPattern() and trackerExpectedHitsInner() that yield the correct number of hits, pixel hits, layers and the information returned by lostInnerHits()
        (but nothing more, so e.g. you cannot access expected outer hits, or lost hits within the track)
        the track normalized chisquare (truncated to an integer)
        the highPurity quality flag set, if the original track had it. 
*/


}

CandidateTrackFilter::~CandidateTrackFilter() {

}

// ------------ method called to produce the data  ------------
bool CandidateTrackFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
	auto trks                      = std::make_unique<vector<TLorentzVector>>();
	auto trks_chg                  = std::make_unique<vector<int>>();
	auto trks_dzpv                 = std::make_unique<vector<double>>();
	auto trks_dzerrorpv            = std::make_unique<vector<double>>();
	auto trks_dxypv                = std::make_unique<vector<double>>();
	auto trks_dxyerrorpv           = std::make_unique<vector<double>>();
	auto trks_normalizedchi2       = std::make_unique<vector<int>>();
	auto trks_found                = std::make_unique<vector<int>>();
	auto trks_lost                 = std::make_unique<vector<int>>();
	//auto trks_quality              = std::make_unique<vector<bool>>(); 
	auto pfcands_numberofhits      = std::make_unique<vector<int>>();
	auto pfcands_numberofpixelhits = std::make_unique<vector<int>>();
	
	//---------------------------------
	// get PFCandidate collection
	//---------------------------------
  
	edm::Handle<edm::View<pat::PackedCandidate> > pfCandidates;
	iEvent.getByToken(pfCandidatesTok_, pfCandidates);

	//---------------------------------
	// get Vertex Collection
	//---------------------------------
	
	edm::Handle<edm::View<reco::Vertex> > vertices;
	iEvent.getByToken(vertexInputTok_, vertices);
	bool hasGoodVtx = false;
	if (!vertices->empty()) hasGoodVtx = true;

	//-------------------------------------------------------------------------------------------------
	// loop over PFCandidates
	//-------------------------------------------------------------------------------------------------

    for (size_t i=0; i<pfCandidates->size();i++) {
		const pat::PackedCandidate pfCand = (*pfCandidates)[i];

		//-------------------------------------------------------------------------------------
		// skip events with no good vertices
		//-------------------------------------------------------------------------------------
		if(!hasGoodVtx) continue;

		//-------------------------------------------------------------------------------------
		// only store PFCandidate values if pt > minPt and |eta| < maxEta_
		//-------------------------------------------------------------------------------------
		if ( (pfCand.pt() < minPt_) || (fabs(pfCand.eta()) > maxEta_) ) continue;

		//-------------------------------------------------------------------------------------
		// pull the track details, if available
		//-------------------------------------------------------------------------------------
		if (!pfCand.hasTrackDetails()) continue;
		const reco::Track track = pfCand.pseudoTrack();

		//-------------------------------------------------------------------------------------
		// cut on impact parameter quantities
		//-------------------------------------------------------------------------------------
		if ( (std::abs(track.dz()) > maxdz_) || (std::abs(track.dxy()) > maxdxy_) ) continue;

		//-------------------------------------------------------------------------------------
		// cut on chi2
		//-------------------------------------------------------------------------------------
		if ( (std::abs(track.normalizedChi2()) > maxnormchi2_) ) continue;

	    //-------------------------------------------------------------------------------------
		// store values
		//-------------------------------------------------------------------------------------

		TLorentzVector p4(track.px(),track.py(),track.pz(),pfCand.energy());
		trks->push_back(p4);
		trks_chg->push_back(track.charge());
		trks_dzpv->push_back(track.dz());
		trks_dzerrorpv->push_back(track.dzError());
		trks_dxypv->push_back(track.dxy());
		trks_dxyerrorpv->push_back(track.dxyError());
		trks_normalizedchi2->push_back(track.normalizedChi2());
		trks_found->push_back(track.found());
		trks_lost->push_back(track.lost());
		//trks_quality->push_back(track.quality());
		pfcands_numberofhits->push_back(pfCand.numberOfHits());
		pfcands_numberofpixelhits->push_back(pfCand.numberOfPixelHits());
	}

	bool result = trks->empty();

	// put candidate values back into event
	iEvent.put(std::move(trks                     ), "trks");
	iEvent.put(std::move(trks_chg                 ), "trkschg");
	iEvent.put(std::move(trks_dzpv                ), "trksdzpv");
	iEvent.put(std::move(trks_dzerrorpv           ), "trksdzerrorpv");
	iEvent.put(std::move(trks_dxypv               ), "trksdxypv");
	iEvent.put(std::move(trks_dxyerrorpv          ), "trksdxyerrorpv");
	iEvent.put(std::move(trks_normalizedchi2      ), "trksnormalizedchi2");
	iEvent.put(std::move(trks_found               ), "trksfound");
	iEvent.put(std::move(trks_lost                ), "trkslost");
	//iEvent.put(std::move(trks_quality             ), "trksquality");
	iEvent.put(std::move(pfcands_numberofhits     ), "pfcandsnumberofhits");
	iEvent.put(std::move(pfcands_numberofpixelhits), "pfcandsnumberofpixelhits");

	return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateTrackFilter);