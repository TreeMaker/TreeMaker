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

  edm::InputTag pfCandidatesTag_;
  edm::InputTag vertexInputTag_;
  edm::InputTag MetInputTag_;
  edm::EDGetTokenT<edm::View<pat::PackedCandidate>> pfCandidatesTok_;
  edm::EDGetTokenT<edm::View<reco::Vertex>> vertexInputTok_;
  edm::EDGetTokenT<edm::View<pat::MET>> MetInputTok_;

  void GetTrkIso(edm::Handle<edm::View<pat::PackedCandidate> > pfcands, const unsigned tkInd, float& trkiso, float& activity) const;

};

//
// constructors and destructor
//

TrackIsolationFilter::TrackIsolationFilter(const edm::ParameterSet& iConfig) {

	pfCandidatesTag_		= iConfig.getParameter<InputTag>("pfCandidatesTag");
	vertexInputTag_               = iConfig.getParameter<InputTag>("vertexInputTag");
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
	vertexInputTok_ = consumes<edm::View<reco::Vertex>>(vertexInputTag_);
	MetInputTok_ = consumes<edm::View<pat::MET>>(MetInputTag_);
	
	produces<std::vector<pat::PackedCandidate> >(""); 
	produces<vector<TLorentzVector> >("pfcands");
	produces<vector<double> >("pfcandsactivity");
	produces<vector<double> >("pfcandstrkiso");
	produces<vector<double> >("pfcandsdzpv"  );
	produces<vector<double> >("pfcandsmT"    );
	produces<vector<int>   >("pfcandschg"    );
	produces<vector<int>   >("pfcandsid"     );
	produces<int>("isoTracks");

}

TrackIsolationFilter::~TrackIsolationFilter() {

}

// ------------ method called to produce the data  ------------
bool TrackIsolationFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {

	auto pfcands = std::make_unique<vector<TLorentzVector>>();
	auto  pfcands_activity = std::make_unique<vector<double>>();
	auto  pfcands_trkiso = std::make_unique<vector<double>>();
	auto  pfcands_dzpv   = std::make_unique<vector<double>>();
	auto  pfcands_mT     = std::make_unique<vector<double>>();
	auto  pfcands_chg     = std::make_unique<vector<int>>();
	auto  pfcands_id      = std::make_unique<vector<int>>();
	
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
	// get Vertex Collection
	//---------------------------------
	
	edm::Handle<edm::View<reco::Vertex> > vertices;
	iEvent.getByToken(vertexInputTok_, vertices);
	bool hasGoodVtx = false;
	if(!vertices->empty()) hasGoodVtx = true;
	
	//-------------------------------------------------------------------------------------------------
	// loop over PFCandidates and calculate the trackIsolation and dz w.r.t. 1st good PV for each one
	// for neutral PFCandidates, store trkiso = 999 and dzpv = 999
	//-------------------------------------------------------------------------------------------------
	
	auto prodminiAOD = std::make_unique<std::vector<pat::PackedCandidate>>();
   
    // miniAOD
    for(size_t i=0; i<pfCandidates->size();i++)
    {
		const pat::PackedCandidate pfCand = (*pfCandidates)[i];
		
		//calculated mT value
		double dphiMET = fabs(pfCand.phi()-metLorentz.phi());
		double mT = sqrt(2 *metLorentz.pt() * pfCand.pt() * (1 - cos(dphiMET)));
		
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
		
		//store candidate values
		//(all values stored in debug case, otherwise just good candidates are stored)
		TLorentzVector p4(pfCand.px(),pfCand.py(),pfCand.pz(),pfCand.energy());
		pfcands->push_back(p4);
		pfcands_chg->push_back(pfCand.charge());
		pfcands_id->push_back(pfCand.pdgId());
		pfcands_mT->push_back(mT);	
		pfcands_trkiso->push_back(trkiso);
		pfcands_activity->push_back(activity);
		pfcands_dzpv->push_back(dz_it);

		if( debug_ && !goodCand) continue;
		prodminiAOD->push_back( pfCand );
	}

	bool result = (doTrkIsoVeto_ ? (prodminiAOD->empty()) : true);
	
	int isoTracks=prodminiAOD->size();
	auto htp = std::make_unique<int>(isoTracks);
	iEvent.put(std::move(htp),"isoTracks" );
	
	// put candidate values back into event
	iEvent.put(std::move(pfcands       ),"pfcands"      );
	iEvent.put(std::move(pfcands_trkiso),"pfcandstrkiso");
	iEvent.put(std::move(pfcands_activity),"pfcandsactivity");
	iEvent.put(std::move(pfcands_dzpv  ),"pfcandsdzpv"  );
	iEvent.put(std::move(pfcands_mT    ),"pfcandsmT"    );
	iEvent.put(std::move(pfcands_chg   ),"pfcandschg"   );
	iEvent.put(std::move(pfcands_id    ),"pfcandsid"    );
	
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
  for (unsigned int iPF(0); iPF<pfcands->size(); iPF++) {
    const pat::PackedCandidate &pfc = pfcands->at(iPF);
    if (pfc.charge()==0) continue;
    if (iPF==tkInd) continue; // don't count track in its own sum
    float dz_other = pfc.dz();
    if( fabs(dz_other) > 0.1 ) continue;
    double dr = deltaR(pfc, pfcands->at(tkInd));
    // activity annulus
    if (dr >= r_iso && dr <= 0.4) activity += pfc.pt();
    // mini iso cone
    if (dr <= r_iso) trkiso += pfc.pt();
  }
  trkiso = trkiso/pfcands->at(tkInd).pt();
  activity = activity/pfcands->at(tkInd).pt();
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackIsolationFilter);

