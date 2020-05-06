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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "RecoParticleFlow/PFProducer/interface/PFMuonAlgo.h"
#include "DataFormats/ParticleFlowReco/interface/PFBlock.h"
#include "DataFormats/Common/interface/ValueMap.h"

#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"

#include "Math/VectorUtil.h"
#include "TMath.h"
#include "TLorentzVector.h"
#include "TTree.h"
// miniAOD
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/PFIsolation.h"

// TreeMaker
#include "TreeMaker/Utils/interface/get_isolation_activity.h"

using namespace reco;
using namespace edm;
using namespace std;

//
// class declaration
//

class TrackIsolationFilter : public edm::global::EDFilter<> {
public:
	explicit TrackIsolationFilter (const edm::ParameterSet&);
	~TrackIsolationFilter() override;

private:
	bool filter(edm::StreamID, edm::Event & iEvent, const edm::EventSetup & iSetup) const override;

	// ----------member data ---------------------------
	double dR_;
	double dzcut_;
	double minPt_;
	double maxEta_;
	double isoCut_;
	double mTCut_;
	bool doTrkIsoVeto_;
	int pdgId_;
	bool debug_;
	SUSYIsolation SUSYIsolationHelper;

	edm::InputTag pfCandidatesTag_;
	edm::InputTag vertexInputTag_;
	edm::InputTag ElectronInputTag_;
	edm::InputTag MuonInputTag_;
	edm::InputTag MetInputTag_;
	edm::EDGetTokenT<edm::View<pat::PackedCandidate>> pfCandidatesTok_;
	edm::EDGetTokenT<edm::View<reco::Candidate>> candTok_;
	edm::EDGetTokenT<edm::View<reco::Vertex>> vertexInputTok_;
	edm::EDGetTokenT<edm::View<reco::Candidate>> ElectronTok_;
	edm::EDGetTokenT<edm::View<reco::Candidate>> MuonTok_;
	edm::EDGetTokenT<edm::View<pat::MET>> MetInputTok_;
	std::vector<edm::EDGetTokenT<reco::CandidateView>> LeptonTok_;

	void GetTrkIso(edm::Handle<edm::View<pat::PackedCandidate> > pfcands, const unsigned tkInd, float& trkiso, float& activity) const;
	bool hasLeptonMatch(const std::vector<reco::CandidatePtr>& leptonPfCands, const reco::CandidatePtr&  candPtr) const;
};

//
// constructors and destructor
//

TrackIsolationFilter::TrackIsolationFilter(const edm::ParameterSet& iConfig) {

	pfCandidatesTag_		= iConfig.getParameter<InputTag>("pfCandidatesTag");
	vertexInputTag_               = iConfig.getParameter<InputTag>("vertexInputTag");
	ElectronInputTag_ = iConfig.getParameter<InputTag>("ElectronTag");
	MuonInputTag_     = iConfig.getParameter<InputTag>("MuonTag");
	MetInputTag_      = iConfig.getParameter<InputTag>("METTag");
	dR_               = iConfig.getParameter<double>          ("dR_ConeSize");       // dR value used to define the isolation cone                (default 0.3 )
	dzcut_            = iConfig.getParameter<double>          ("dz_CutValue");       // cut value for dz(trk,vtx) for track to include in iso sum (default 0.05)
	minPt_            = iConfig.getParameter<double>          ("minPt_PFCandidate"); // store PFCandidates with pt above this cut                 (default 0   )
	isoCut_           = iConfig.getParameter<double>          ("isoCut"); // isolation cut value
	doTrkIsoVeto_     = iConfig.getParameter<bool>            ("doTrkIsoVeto");
	pdgId_     = iConfig.getParameter<int>            ("pdgId");
	mTCut_=   iConfig.getParameter<double>   ("mTCut");
	maxEta_= iConfig.getParameter<double>("etaCut");
	debug_= iConfig.getParameter<bool>("debug");
	
	pfCandidatesTok_ = consumes<edm::View<pat::PackedCandidate>>(pfCandidatesTag_);
	candTok_ = consumes<edm::View<reco::Candidate> >(pfCandidatesTag_);
	vertexInputTok_ = consumes<edm::View<reco::Vertex>>(vertexInputTag_);
	ElectronTok_ = consumes<edm::View<reco::Candidate>>(ElectronInputTag_);
	MuonTok_ = consumes<edm::View<reco::Candidate>>(MuonInputTag_);
	MetInputTok_ = consumes<edm::View<pat::MET>>(MetInputTag_);
	LeptonTok_ = {ElectronTok_,MuonTok_};

	produces<std::vector<pat::PackedCandidate> >(""); 
	produces<vector<TLorentzVector> >("pfcands");
	produces<vector<double> >("pfcandsactivity");
	produces<vector<double> >("pfcandstrkiso");
	produces<vector<double> >("pfcandspfreliso03chg");
	produces<vector<double> >("pfcandspfreliso03all");
	produces<vector<double> >("pfcandsdzpv"  );
	produces<vector<double> >("pfcandsdxypv" );
	produces<vector<double> >("pfcandsmT"    );
	produces<vector<int>   >("pfcandschg"    );
	produces<vector<int>   >("pfcandsid"     );
	produces<vector<bool> >("pfcandsleptonmatch");
	produces<int>("isoTracks");

}

TrackIsolationFilter::~TrackIsolationFilter() {

}

// ------------ method called to produce the data  ------------
bool TrackIsolationFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {

	auto pfcands = std::make_unique<vector<TLorentzVector>>();
	auto pfcands_activity       = std::make_unique<vector<double>>();
	auto pfcands_trkiso         = std::make_unique<vector<double>>();
	auto pfcands_pfRelIso03_chg = std::make_unique<vector<double>>();
	auto pfcands_pfRelIso03_all = std::make_unique<vector<double>>();
	auto pfcands_dzpv           = std::make_unique<vector<double>>();
	auto pfcands_dxypv          = std::make_unique<vector<double>>();
	auto pfcands_mT             = std::make_unique<vector<double>>();
	auto pfcands_chg            = std::make_unique<vector<int>>();
	auto pfcands_id             = std::make_unique<vector<int>>();
	auto pfcands_leptonmatch    = std::make_unique<vector<bool>>();
	
	edm::Handle< edm::View<pat::MET> > MET;
	iEvent.getByToken(MetInputTok_,MET);
	reco::MET::LorentzVector metLorentz(0,0,0,0);
	if(MET.isValid() ){
		metLorentz=MET->at(0).p4();
	}

	//---------------------------------
	// get PFCandidate collection
	//---------------------------------

	edm::Handle<edm::View<pat::PackedCandidate> > pfCandidates;
	iEvent.getByToken(pfCandidatesTok_, pfCandidates);

	//---------------------------------
	// get Candidate collection
	//---------------------------------

	edm::Handle<edm::View<reco::Candidate> > cands;
	iEvent.getByToken(candTok_, cands);

	//---------------------------------
	// get Vertex collection
	//---------------------------------
	
	edm::Handle<edm::View<reco::Vertex> > vertices;
	iEvent.getByToken(vertexInputTok_, vertices);
	bool hasGoodVtx = false;
	if(!vertices->empty()) hasGoodVtx = true;

	//---------------------------------
	// get Lepton candidates
	//---------------------------------
	// Taken from: https://github.com/cms-sw/cmssw/blob/424ad43856c2c739d702c240187401b7b08566ea/PhysicsTools/PatAlgos/plugins/IsolatedTrackCleaner.cc#L28-L40
	std::vector<reco::CandidatePtr> leptonPfCands;
	edm::Handle<reco::CandidateView> leptons;
	for (const auto& token : LeptonTok_) {
		iEvent.getByToken(token, leptons);
		for (const auto& lep : *leptons) {
			for (unsigned int i = 0, n = lep.numberOfSourceCandidatePtrs(); i < n; ++i) {
				auto ptr = lep.sourceCandidatePtr(i);
				if (ptr.isNonnull()) leptonPfCands.push_back(ptr);
			}
		}
	}
	std::sort(leptonPfCands.begin(), leptonPfCands.end());

	//-------------------------------------------------------------------------------------------------
	// loop over PFCandidates and calculate the trackIsolation and dz w.r.t. 1st good PV for each one
	// for neutral PFCandidates, store trkiso = 999 and dzpv = 999
	//-------------------------------------------------------------------------------------------------
	
	auto prodminiAOD = std::make_unique<std::vector<pat::PackedCandidate>>();

	// miniAOD
	for(size_t i=0; i<pfCandidates->size();i++)
	{
		const pat::PackedCandidate pfCand = (*pfCandidates)[i];

		//to keep track of cuts in debug case (when continues are not used)
		bool goodCand = true;
		
		//-------------------------------------------------------------------------------------
		// skip events with no good vertices
		//-------------------------------------------------------------------------------------
		if(!hasGoodVtx) {
			if(debug_) goodCand &= false;
			else continue;
		}
		//-------------------------------------------------------------------------------------
		// only consider charged tracks
		//-------------------------------------------------------------------------------------
		if (pfCand.charge() == 0) {
			if(debug_) goodCand &= false;
			else continue;
		}
		//-------------------------------------------------------------------------------------
		// only store PFCandidate values if PFCandidate.pdgId() == pdgId_
		//-------------------------------------------------------------------------------------
		if( pdgId_ != 0 && abs( pfCand.pdgId() ) != pdgId_ ) {
			if(debug_) goodCand &= false;
			else continue;
		}
		//-------------------------------------------------------------------------------------
		// only store PFCandidate values if pt > minPt
		//-------------------------------------------------------------------------------------
		if(pfCand.pt() <minPt_) {
			if(debug_) goodCand &= false;
			else continue;
		}
		if(fabs(pfCand.eta()) >maxEta_) {
			if(debug_) goodCand &= false;
			else continue;
		}
		//-------------------------------------------------------------------------------------
		// cut on mT of track and MET
		//-------------------------------------------------------------------------------------
		//calculated mT value
		double dphiMET = fabs(pfCand.phi()-metLorentz.phi());
		double mT = sqrt(2 *metLorentz.pt() * pfCand.pt() * (1 - cos(dphiMET)));
		
		if(mTCut_>0.01 && mT>mTCut_) {
			if(debug_) goodCand &= false;
			else continue;
		}
		//----------------------------------------------------------------------------
		// now make cuts on isolation and dz
		//----------------------------------------------------------------------------
		float trkiso = 0.;
		float activity = 0.;
		GetTrkIso(pfCandidates, i, trkiso, activity);
		float dz_it = pfCand.dz();

		if( isoCut_>0 && trkiso > isoCut_ ) {
			if(debug_) goodCand &= false;
			else continue;
		}
		if( std::abs(dz_it) > dzcut_ ) {
			if(debug_) goodCand &= false;
			else continue;
		}

		double pfreliso03_chg = 0.;
		double pfreliso03_all = 0.;
		SUSYIsolationHelper.GetPFIsolation(pfCandidates, i, pfreliso03_all, pfreliso03_chg);
		
		//store candidate values
		//(all values stored in debug case, otherwise just good candidates are stored)
		TLorentzVector p4(pfCand.px(),pfCand.py(),pfCand.pz(),pfCand.energy());
		pfcands->push_back(p4);
		pfcands_chg->push_back(pfCand.charge());
		pfcands_id->push_back(pfCand.pdgId());
		pfcands_mT->push_back(mT);	
		pfcands_trkiso->push_back(trkiso);
		pfcands_activity->push_back(activity);
		pfcands_pfRelIso03_chg->push_back(pfreliso03_chg);
		pfcands_pfRelIso03_all->push_back(pfreliso03_all);
		pfcands_dzpv->push_back(dz_it);
		pfcands_dxypv->push_back(pfCand.dxy());
		pfcands_leptonmatch->push_back(hasLeptonMatch(leptonPfCands,cands->ptrAt(i)));

		if( debug_ && !goodCand) continue;
		prodminiAOD->push_back( pfCand );
	}

	bool result = (doTrkIsoVeto_ ? (prodminiAOD->empty()) : true);
	
	int isoTracks=prodminiAOD->size();
	auto htp = std::make_unique<int>(isoTracks);
	iEvent.put(std::move(htp),"isoTracks" );
	
	// put candidate values back into event
	iEvent.put(std::move(pfcands               ),"pfcands"      );
	iEvent.put(std::move(pfcands_trkiso        ),"pfcandstrkiso");
	iEvent.put(std::move(pfcands_activity      ),"pfcandsactivity");
	iEvent.put(std::move(pfcands_pfRelIso03_chg),"pfcandspfreliso03chg");
	iEvent.put(std::move(pfcands_pfRelIso03_all),"pfcandspfreliso03all");
	iEvent.put(std::move(pfcands_dzpv          ),"pfcandsdzpv"  );
	iEvent.put(std::move(pfcands_dxypv         ),"pfcandsdxypv" );
	iEvent.put(std::move(pfcands_mT            ),"pfcandsmT"    );
	iEvent.put(std::move(pfcands_chg           ),"pfcandschg"   );
	iEvent.put(std::move(pfcands_id            ),"pfcandsid"    );
	iEvent.put(std::move(pfcands_leptonmatch   ),"pfcandsleptonmatch");
	
	iEvent.put(std::move(prodminiAOD)); 
	return result;
}

void TrackIsolationFilter::GetTrkIso(edm::Handle<edm::View<pat::PackedCandidate> > pfcands, const unsigned tkInd, float& trkiso, float& activity) const {
	if (tkInd>pfcands->size()) {
		trkiso = -999.;
		activity = -999.;
		return;
	}
	trkiso = 0.;
	activity = 0.;
	double r_iso = 0.3;
	const auto& pfTkInd = pfcands->at(tkInd);
	for (unsigned int iPF(0); iPF<pfcands->size(); iPF++) {
		if (iPF==tkInd) continue; // don't count track in its own sum
		const pat::PackedCandidate &pfc = pfcands->at(iPF);
		if (pfc.charge()==0) continue;
		if( fabs(pfc.dz()) > 0.1 ) continue;
		double dr = deltaR(pfc, pfTkInd);
		// activity annulus
		if (dr >= r_iso && dr <= 0.4) activity += pfc.pt();
		// mini iso cone
		if (dr <= r_iso) trkiso += pfc.pt();
	}
	double invpt = 1.0/pfTkInd.pt();
	trkiso = trkiso*invpt;
	activity = activity*invpt;
}

bool TrackIsolationFilter::hasLeptonMatch(const std::vector<reco::CandidatePtr>& leptonPfCands, const reco::CandidatePtr&  candPtr) const {
	// Inspired by: https://github.com/cms-sw/cmssw/blob/424ad43856c2c739d702c240187401b7b08566ea/PhysicsTools/PatAlgos/plugins/IsolatedTrackCleaner.cc#L48-L49
	if (std::binary_search(leptonPfCands.begin(), leptonPfCands.end(), candPtr)) {
		return true;
	}
	return false;
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackIsolationFilter);

