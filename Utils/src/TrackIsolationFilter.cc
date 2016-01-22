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
#include "FWCore/Framework/interface/EDProducer.h"
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

#include "TreeMaker/Utils/interface/TrackIsolationFilter.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"

#include "TMath.h"
#include "TLorentzVector.h"
#include "TTree.h"
// miniAOD
//#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

using namespace reco;
using namespace edm;
using namespace std;

//
// class decleration
//

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
	produces<vector<double> >("pfcandsactivity").setBranchAlias("pfcands_activity");
	produces<vector<double> >("pfcandstrkiso").setBranchAlias("pfcands_trkiso");
	produces<vector<double> >("pfcandsdzpv"  ).setBranchAlias("pfcands_dzpv");
	produces<vector<double> >("pfcandsmT"    ).setBranchAlias("pfcands_mT");
	produces<vector<int>   >("pfcandschg"    ).setBranchAlias("pfcands_chg");
	produces<vector<int>   >("pfcandsid"     ).setBranchAlias("pfcands_id");
	produces<int>("isoTracks").setBranchAlias("isoTracks");

}

TrackIsolationFilter::~TrackIsolationFilter() {

}

// ------------ method called to produce the data  ------------

bool TrackIsolationFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {


	auto_ptr<vector<TLorentzVector> > pfcands(new vector<TLorentzVector>);
	auto_ptr<vector<double> >  pfcands_activity(new vector<double>);
	auto_ptr<vector<double> >  pfcands_trkiso(new vector<double>);
	auto_ptr<vector<double> >  pfcands_dzpv  (new vector<double>);
	auto_ptr<vector<double> >  pfcands_mT    (new vector<double>);
	auto_ptr<vector<int>   >  pfcands_chg    (new vector<int>  );
	auto_ptr<vector<int>   >  pfcands_id     (new vector<int>  );
	
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
	vtxSize = vertices->size();
	bool hasGoodVtx = false;
	if(vertices->size() > 0) hasGoodVtx = true;
	
	//-------------------------------------------------------------------------------------------------
	// loop over PFCandidates and calculate the trackIsolation and dz w.r.t. 1st good PV for each one
	// for neutral PFCandidates, store trkiso = 999 and dzpv = 999
	//-------------------------------------------------------------------------------------------------
	
	std::auto_ptr<std::vector<pat::PackedCandidate> > prodminiAOD(new std::vector<pat::PackedCandidate>());
   
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
		if (pfCand.charge() == 0) continue;
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
		if( debug_ && !goodCand) continue;
		if( isoCut_>0 && trkiso > isoCut_ ) continue;
		if( std::abs(dz_it) > dzcut_ ) continue;
		
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
		prodminiAOD->push_back( pfCand );
		
		
	}

	bool result = (doTrkIsoVeto_ ? (prodminiAOD->size() == 0) : true);
	
	int isoTracks=prodminiAOD->size();
	std::auto_ptr<int> htp(new int(isoTracks));
	iEvent.put(htp,"isoTracks" );
	
	// put candidate values back into event
	iEvent.put(pfcands       ,"pfcands"      );
	iEvent.put(pfcands_trkiso,"pfcandstrkiso");
	iEvent.put(pfcands_activity,"pfcandsactivity");
	iEvent.put(pfcands_dzpv  ,"pfcandsdzpv"  );
	iEvent.put(pfcands_mT    ,"pfcandsmT"    );
	iEvent.put(pfcands_chg   ,"pfcandschg"   );
	iEvent.put(pfcands_id    ,"pfcandsid"    );
	
	iEvent.put(prodminiAOD); 
	return result;
}

void TrackIsolationFilter::GetTrkIso(edm::Handle<edm::View<pat::PackedCandidate> > pfcands, const unsigned tkInd, float& trkiso, float& activity) {
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

