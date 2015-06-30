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

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
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

#include "AllHadronicSUSY/Utils/interface/TrackIsolationFilter.h"
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
 // produces<std::vector<reco::PFCandidate> >(""); 
  produces<std::vector<pat::PackedCandidate> >(""); 
  produces<vector<float> >("pfcandstrkiso").setBranchAlias("pfcands_trkiso");
  produces<vector<float> >("pfcandsdzpv"  ).setBranchAlias("pfcands_dzpv");
  produces<vector<float> >("pfcandspt"    ).setBranchAlias("pfcands_pt");
  const std::string string1("MT");
  produces<std::vector<double> > (string1).setBranchAlias(string1);
  produces<vector<int>   >("pfcandschg"   ).setBranchAlias("pfcands_chg");
  produces<int>("isoTracks").setBranchAlias("isoTracks");

}

TrackIsolationFilter::~TrackIsolationFilter() {

}

// ------------ method called to produce the data  ------------

bool TrackIsolationFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  auto_ptr<vector<float> >  pfcands_trkiso(new vector<float>);
  auto_ptr<vector<float> >  pfcands_dzpv  (new vector<float>);
  auto_ptr<vector<float> >  pfcands_pt    (new vector<float>);
  std::auto_ptr< std::vector<double> > mt_(new std::vector<double>);
  auto_ptr<vector<int>   >  pfcands_chg   (new vector<int>  );

  edm::Handle< edm::View<pat::MET> > MET;
  iEvent.getByLabel(MetInputTag_,MET);
  reco::MET::LorentzVector metLorentz(0,0,0,0);
  if(MET.isValid() ){
        metLorentz=MET->at(0).p4();
  }

  //---------------------------------
  // get PFCandidate collection
  //---------------------------------
  
  edm::Handle<PFCandidateCollection> pfCandidatesHandle;
//  edm::Handle<edm::View< pat::PackedCandidate> >pfCandidatesHandle;
  iEvent.getByLabel(pfCandidatesTag_, pfCandidatesHandle);
  
  edm::Handle<edm::View< pat::PackedCandidate> >pfCandidates;
  iEvent.getByLabel(pfCandidatesTag_, pfCandidates);

  //---------------------------------
  // get Vertex Collection
  //---------------------------------

  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexInputTag_, vertices);
  reco::Vertex::Point vtxpos = (vertices->size() > 0 ? (*vertices)[0].position() : reco::Vertex::Point());
int firstGoodVertexIdx = -1;
  vtxSize = vertices->size();
for(int v=0; v<vtxSize;++v){
        if ( !(*vertices)[v].isFake() && (*vertices)[v].ndof()>=4. && (*vertices)[v].position().Rho()<=2.0 && fabs((*vertices)[v].position().Z())<=24.0) {
        firstGoodVertexIdx=v;
// 				std::cout<<"GoodVertexIdV found: "<<firstGoodVertexIdx<<std::endl;
        break;
        }
}  
  //-------------------------------------------------------------------------------------------------
  // loop over PFCandidates and calculate the trackIsolation and dz w.r.t. 1st good PV for each one
  // for neutral PFCandidates, store trkiso = 999 and dzpv = 999
  //-------------------------------------------------------------------------------------------------

  std::auto_ptr<std::vector<reco::PFCandidate> > prod(new std::vector<reco::PFCandidate>());
  std::auto_ptr<std::vector<pat::PackedCandidate> > prodminiAOD(new std::vector<pat::PackedCandidate>());
   if( vertices->size() > 0 && firstGoodVertexIdx>=0) {
// 	if( vertices->size() > 0) {
    /* for( PFCandidateCollection::const_iterator pf_it = pfCandidatesHandle->begin(); pf_it != pfCandidatesHandle->end(); pf_it++ ) {

        //-------------------------------------------------------------------------------------
        // only store PFCandidate values if pt > minPt
        //-------------------------------------------------------------------------------------

        if( pf_it->pt() < minPt_ ) continue;

        //-------------------------------------------------------------------------------------
        // store pt and charge of PFCandidate
        //-------------------------------------------------------------------------------------

        pfcands_pt->push_back(pf_it->pt());
        pfcands_chg->push_back(pf_it->charge());

        //-------------------------------------------------------------------------------------
        // if there's no good vertex in the event, we can't calculate anything so store 999999
        //-------------------------------------------------------------------------------------
    
        //-------------------------------------------------------
        // require PFCandidate is charged, otherwise store 999 
        //-------------------------------------------------------

        if( pf_it->charge() != 0 ){

           //----------------------------------------------------------------------------
           // now loop over other PFCandidates in the event to calculate trackIsolation
           //----------------------------------------------------------------------------

           float trkiso = 0.0;

           for( PFCandidateCollection::const_iterator pf_other = pfCandidatesHandle->begin(); pf_other != pfCandidatesHandle->end(); pf_other++ ) {

              // don't count the PFCandidate in its own isolation sum
              if( pf_it == pf_other       ) continue;

	      // require the PFCandidate to be charged
	      if( pf_other->charge() == 0 ) continue;

              // cut on dR between the PFCandidates
              float dR = deltaR(pf_it->eta(), pf_it->phi(), pf_other->eta(), pf_other->phi());
              if( dR > dR_ ) continue;

	      // cut on the PFCandidate dz
	      float dz_other = 100;

	      if ( pf_other->trackRef().isNonnull()) {
	         dz_other = pf_other->trackRef()->dz(vtxpos);
	      }

	      if( fabs(dz_other) > dzcut_ ) continue;

	      trkiso += pf_other->pt();
           }

           // calculate the dz of this candidate
           float dz_it = 100; //

           if ( pf_it->trackRef().isNonnull()) {
              dz_it = pf_it->trackRef()->dz(vtxpos);
           }

           // store trkiso and dz values
           pfcands_trkiso->push_back(trkiso);
           pfcands_dzpv->push_back(dz_it);

           if( trkiso/pf_it->pt() > isoCut_ ) continue;
           if( std::abs(dz_it) > dzcut_ ) continue;

           prod->push_back( (*pf_it) );

        }else{
           //neutral particle, set trkiso and dzpv to 9999
           pfcands_trkiso->push_back(9999);
           pfcands_dzpv->push_back(9999);
        }

     }*/
      // miniAOD
      for(size_t i=0; i<pfCandidates->size();i++)
      {
	//-------------------------------------------------------------------------------------
	// only store PFCandidate values if PFCandidate.pdgId() == pdgId_
	//-------------------------------------------------------------------------------------
	if( abs( (*pfCandidates)[i].pdgId() ) != pdgId_ && pdgId_ != 0 ) continue;
	//-------------------------------------------------------------------------------------
	// only store PFCandidate values if pt > minPt
	//-------------------------------------------------------------------------------------
	if((*pfCandidates)[i].pt() <minPt_) continue;
	if(fabs((*pfCandidates)[i].eta()) >maxEta_) continue;
	//-------------------------------------------------------------------------------------
	// store pt and charge of PFCandidate
	//-------------------------------------------------------------------------------------
	double dphiMET=fabs((*pfCandidates)[i].phi()-metLorentz.phi());
        double mT=sqrt(2 *metLorentz.pt() * (*pfCandidates)[i].pt() * (1 - cos(dphiMET)));
        if(mTCut_>0.01 && mT>mTCut_)continue;
	mt_->push_back(mT);
	pfcands_pt->push_back((*pfCandidates)[i].pt());
	pfcands_chg->push_back((*pfCandidates)[i].charge());
	//----------------------------------------------------------------------------
	// now loop over other PFCandidates in the event to calculate trackIsolation
	//----------------------------------------------------------------------------
	
	if( (*pfCandidates)[i].charge() != 0 )
	{
	  float trkiso = 0.0;
	  for(size_t ii=0; ii<pfCandidates->size();ii++)
	  {
	    // don't count the PFCandidate in its own isolation sum
	    if(i==ii) continue;
	    // require the PFCandidate to be charged
	    if( (*pfCandidates)[ii].charge() == 0 ) continue;
	    // cut on dR between the PFCandidates
	    float dR = deltaR((*pfCandidates)[i].eta(), (*pfCandidates)[i].phi(), (*pfCandidates)[ii].eta(), (*pfCandidates)[ii].phi());
	    if( dR > dR_ ) continue;
	    // cut on the PFCandidate dz
	    float dz_other = 100;
	    // was
	    //if ((*pfCandidates)[ii].trackRef().isNonnull()) 
	    //{
	    //  dz_other = (*pfCandidates)[ii].trackRef()->dz(vtxpos);
	    //}
	    // check if this workes fine!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	    
	      dz_other = (*pfCandidates)[ii].dz(vtxpos);
	    if( fabs(dz_other) > dzcut_ ) continue;
	    trkiso += (*pfCandidates)[ii].pt();
	  }
	  float dz_it = 100; //
	  dz_it = (*pfCandidates)[i].dz(vtxpos);
	  pfcands_trkiso->push_back(trkiso);
	  pfcands_dzpv->push_back(dz_it);
	  if( trkiso/(*pfCandidates)[i].pt() > isoCut_ ) continue;
	  if( std::abs(dz_it) > dzcut_ ) continue;
	  prodminiAOD->push_back( (*pfCandidates)[i] );
	  
	}
	else //neutral particle, set trkiso and dzpv to 9999
	{
	  pfcands_trkiso->push_back(9999);
	  pfcands_dzpv->push_back(9999);
	}
	
      }
  }

  bool result = (doTrkIsoVeto_ ? (prod->size() == 0) : true);

  int isoTracks=prodminiAOD->size();
  std::auto_ptr<int> htp(new int(isoTracks));
  iEvent.put(htp,"isoTracks" );

  // put trkiso and dz values back into event
  iEvent.put(pfcands_trkiso,"pfcandstrkiso");
  iEvent.put(pfcands_dzpv  ,"pfcandsdzpv"  );
  iEvent.put(pfcands_pt    ,"pfcandspt"    );
  const std::string string0("MT");
  iEvent.put(mt_,string0);
  iEvent.put(pfcands_chg   ,"pfcandschg"   );

  iEvent.put(prodminiAOD); 
  return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackIsolationFilter);

