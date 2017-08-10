// -*- C++ -*-
//
// Package:    GenLeptonRecoCand
// Class:      GenLeptonRecoCand
// 
/**\class GenLeptonRecoCand GenLeptonRecoCand.cc RA2Classic/GenLeptonRecoCand/src/GenLeptonRecoCand.cc
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

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "DataFormats/Math/interface/deltaR.h"

#include <TLorentzVector.h>
#include <TVector3.h>

//
// class declaration
//

class GenLeptonRecoCand : public edm::global::EDProducer<> {
public:
  explicit GenLeptonRecoCand(const edm::ParameterSet&);
  ~GenLeptonRecoCand();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  edm::InputTag PrunedGenParticleTag_;
  edm::InputTag pfCandsTag_;
  edm::EDGetTokenT<edm::View<reco::GenParticle>> PrunedGenParticleTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> pfCandsTok_;
	
  const reco::GenParticle* BosonFound(const reco::GenParticle * particle) const;
  const reco::GenParticle* TauFound(const reco::GenParticle * particle) const;

  void GetTrkIso(edm::Handle<pat::PackedCandidateCollection> pfcands, const unsigned tkInd, float& trkiso, float& activity) const;
  const int MatchToPFCand(edm::Handle<pat::PackedCandidateCollection> pfcands, const reco::GenParticle* gen_track) const;
  const double GetGenRecoD3(edm::Handle<pat::PackedCandidateCollection> pfcands, const int tkInd, const reco::GenParticle* gen_track) const;
	
	
  // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
GenLeptonRecoCand::GenLeptonRecoCand(const edm::ParameterSet& iConfig)
{
  //register your product
  PrunedGenParticleTag_ 				= 	iConfig.getParameter<edm::InputTag >("PrunedGenParticleTag");
  pfCandsTag_ = 	iConfig.getParameter<edm::InputTag >("pfCandsTag");
  PrunedGenParticleTok_ = consumes<edm::View<reco::GenParticle>>(PrunedGenParticleTag_);
  pfCandsTok_ = consumes<pat::PackedCandidateCollection>(pfCandsTag_);
  

  produces<std::vector<reco::GenParticle>>("Boson");
  produces<std::vector<int>>("BosonPDGId");
  produces<std::vector<reco::GenParticle>>("Muon");
  produces<std::vector<bool>>("MuonTauDecay");
  produces<std::vector<double>>("MuonGenRecoD3");
  produces<std::vector<double>>("MuonTrkIso");
  produces<std::vector<double>>("MuonTrkAct");
  produces<std::vector<reco::GenParticle>>("Electron");
  produces<std::vector<bool>>("ElectronTauDecay");
  produces<std::vector<double>>("ElectronGenRecoD3");
  produces<std::vector<double>>("ElectronTrkIso");
  produces<std::vector<double>>("ElectronTrkAct");
  produces<std::vector<reco::GenParticle>>("Tau");
  produces<std::vector<bool>>("TauHadronic");
  produces<std::vector<reco::GenParticle>>("TauDecayCands");
  produces<std::vector<int>>("TauDecayCandspdgID");
  produces<std::vector<int>>("TauDecayCandsmomInd");
  produces<std::vector<TLorentzVector>>("TauLeadTrk");
  produces<std::vector<double>>("TauLeadTrkGenRecoD3");
  produces<std::vector<double>>("TauLeadTrkIso");
  produces<std::vector<double>>("TauLeadTrkAct");
  produces<std::vector<int>>("TauNProngs");
  produces<std::vector<int>>("TauNNHads");
  produces<std::vector<reco::GenParticle>>("TauNu");
  produces<std::vector<double>>("TauNuMomPt");
  /* Examples
   *   produces<ExampleData2>();
   * 
   *   //if do put with a label
   *   produces<ExampleData2>("label");
   * 
   *   //if you want to put into the Run
   *   produces<ExampleData2,InRun>();
   */
  //now do what ever other initialization is needed
	
}


GenLeptonRecoCand::~GenLeptonRecoCand()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
GenLeptonRecoCand::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;	
  auto selectedBoson = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedBosonPDGId = std::make_unique<std::vector<int>>();
  auto selectedMuon = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedMuonTauDecay = std::make_unique<std::vector<bool>>();
  auto selectedMuonGenRecoD3 = std::make_unique<std::vector<double>>();
  auto selectedMuonTrkIso = std::make_unique<std::vector<double>>();
  auto selectedMuonTrkAct = std::make_unique<std::vector<double>>();
  auto selectedElectron = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedElectronTauDecay = std::make_unique<std::vector<bool>>();
  auto selectedElectronGenRecoD3 = std::make_unique<std::vector<double>>();
  auto selectedElectronTrkIso = std::make_unique<std::vector<double>>();
  auto selectedElectronTrkAct = std::make_unique<std::vector<double>>();
  auto selectedTau = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedTauHadronic = std::make_unique<std::vector<bool>>();
  auto selectedTauDecayCands = std::make_unique<std::vector<reco::GenParticle>>();
  auto selectedTauDecayCandspdgID = std::make_unique<std::vector<int>>();
  auto selectedTauDecayCandsmomInd = std::make_unique<std::vector<int>>();
  auto selectedTauLeadTrk = std::make_unique<std::vector<TLorentzVector>>();
  auto selectedTauLeadTrkd3 = std::make_unique<std::vector<double>>();
  auto selectedTauLeadTrkIso = std::make_unique<std::vector<double>>();
  auto selectedTauLeadTrkAct = std::make_unique<std::vector<double>>();
  auto selectedTauNProngs = std::make_unique<std::vector<int>>();
  auto selectedTauNNHads = std::make_unique<std::vector<int>>();

  auto selectedTauNu = std::make_unique<std::vector<reco::GenParticle>>();
  Handle<edm::View<reco::GenParticle> > pruned;
  iEvent.getByToken(PrunedGenParticleTok_,pruned);

  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(pfCandsTok_, pfcands);

  for(size_t i=0; i<pruned->size();i++)
    {
      if( (abs((*pruned)[i].pdgId() ) == 24 || abs((*pruned)[i].pdgId() ) == 23 || abs((*pruned)[i].pdgId() ) == 1000024 ) && (*pruned)[i].status()==22) // needs to be checked if this workes for Z 23 as well
	{
	  const reco::GenParticle * FinalBoson = BosonFound(&(*pruned)[i]);
	  size_t bosonDaugthers = FinalBoson->numberOfDaughters();
	  selectedBoson->push_back(*FinalBoson);
	  selectedBosonPDGId->push_back(FinalBoson->pdgId());
	  for(size_t ii=0;ii< bosonDaugthers; ii++)
	    {
	      if(abs(FinalBoson->daughter(ii)->pdgId())== 11) 
		{
		  selectedElectron->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));
		  selectedElectronTauDecay->push_back(0);
		  int matchedPFCand(MatchToPFCand(pfcands, &selectedElectron->back()));
		  selectedElectronGenRecoD3->push_back(GetGenRecoD3(pfcands, matchedPFCand, &selectedElectron->back()));
		  float trkiso = 0.;
		  float activity = 0.;
		  GetTrkIso(pfcands, matchedPFCand, trkiso, activity);
		  selectedElectronTrkIso->push_back(trkiso);
		  selectedElectronTrkAct->push_back(activity);
		}
	      if(abs(FinalBoson->daughter(ii)->pdgId())== 13) 
		{
		  selectedMuon->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));
		  selectedMuonTauDecay->push_back(0);
		  int matchedPFCand(MatchToPFCand(pfcands, &selectedMuon->back()));
		  selectedMuonGenRecoD3->push_back(GetGenRecoD3(pfcands, matchedPFCand, &selectedMuon->back()));
		  float trkiso = 0.;
		  float activity = 0.;
		  GetTrkIso(pfcands, matchedPFCand, trkiso, activity);
		  selectedMuonTrkIso->push_back(trkiso);
		  selectedMuonTrkAct->push_back(activity);
		}
	      if(abs(FinalBoson->daughter(ii)->pdgId())== 15) 
		{
		  selectedTau->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));

		  // 					selectedTauHadronic->push_back(0);
		  const reco::GenParticle * FinalTauDecay = TauFound((reco::GenParticle*)FinalBoson->daughter(ii));

		  for(size_t iii=0; iii<FinalTauDecay->numberOfDaughters();iii++)
		    {
		      // daughters of "final" taus before decaying
		      if (FinalTauDecay->daughter(iii)->status()==1 
			  || FinalTauDecay->daughter(iii)->pdgId()==111 ){                 // Stable particle or pi0
			selectedTauDecayCandsmomInd->push_back(selectedTau->size()-1); // index to connect it to mom tau
			selectedTauDecayCands->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
			selectedTauDecayCandspdgID->push_back(FinalTauDecay->daughter(iii)->pdgId());
			if (abs(FinalTauDecay->daughter(iii)->pdgId())==16) 
			  selectedTauNu->push_back( *((reco::GenParticle*) FinalTauDecay->daughter(iii)) );
		      } else {                                                             // Neither stable particle nor pi0 (e.g. rho+-, a+-, K*+-, W+-)
			for(size_t iiii=0; iiii<FinalTauDecay->daughter(iii)->numberOfDaughters();iiii++){
			  // granddaughters of "final" taus before decaying
			  if (FinalTauDecay->daughter(iii)->daughter(iiii)->status()==1 
			      || FinalTauDecay->daughter(iii)->daughter(iiii)->pdgId()==111){ // Stable particle or pi0
			    selectedTauDecayCandsmomInd->push_back(selectedTau->size()-1); // index to connect it to mom tau
			    selectedTauDecayCands->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii)->daughter(iiii) ));
			    selectedTauDecayCandspdgID->push_back(FinalTauDecay->daughter(iii)->daughter(iiii)->pdgId());
			  } else {                                                            // Neither stable particle nor pi0 (e.g. eta, K0S)
			    for(size_t iiiii=0; iiiii<FinalTauDecay->daughter(iii)->daughter(iiii)->numberOfDaughters();iiiii++){
			      // greatgranddaughters of "final" taus before decaying
			      selectedTauDecayCandsmomInd->push_back(selectedTau->size()-1); // index to connect it to mom tau
			      selectedTauDecayCands->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii)->daughter(iiii)->daughter(iiiii) ));
			      selectedTauDecayCandspdgID->push_back(FinalTauDecay->daughter(iii)->daughter(iiii)->daughter(iiiii)->pdgId());
			      if (FinalTauDecay->daughter(iii)->daughter(iiii)->daughter(iiiii)->status()!=1 
				  && FinalTauDecay->daughter(iii)->daughter(iiii)->daughter(iiiii)->pdgId()!=111){ // Stable particle or pi0
				printf("WARNING: This is a tau's greatgranddaughter, but it's still neither stable nor pi0/eta/K0S. pdgId=%d. stauts=%d\n",
				       FinalTauDecay->daughter(iii)->daughter(iiii)->daughter(iiiii)->pdgId(),
				       FinalTauDecay->daughter(iii)->daughter(iiii)->daughter(iiiii)->status());						    
			      }
			    }
			  }
			}
		      }
		    }

		  bool hadTauDecay=1;
		  for(size_t iii=0; iii<FinalTauDecay->numberOfDaughters();iii++)
		    {
		      if(abs(FinalTauDecay->daughter(iii)->pdgId())== 11) 
			{
			  selectedElectron->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
			  selectedElectronTauDecay->push_back(1);
			  int matchedPFCand(MatchToPFCand(pfcands, &selectedElectron->back()));
			  selectedElectronGenRecoD3->push_back(GetGenRecoD3(pfcands, matchedPFCand, &selectedElectron->back()));
			  float trkiso = 0.;
			  float activity = 0.;
			  GetTrkIso(pfcands, matchedPFCand, trkiso, activity);
			  selectedElectronTrkIso->push_back(trkiso);
			  selectedElectronTrkAct->push_back(activity);
			  hadTauDecay=0;
			}
		      else if(abs(FinalTauDecay->daughter(iii)->pdgId())== 13) 
			{
			  selectedMuon->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
			  selectedMuonTauDecay->push_back(1);
			  int matchedPFCand(MatchToPFCand(pfcands, &selectedMuon->back()));
			  selectedMuonGenRecoD3->push_back(GetGenRecoD3(pfcands, matchedPFCand, &selectedMuon->back()));
			  float trkiso = 0.;
			  float activity = 0.;
			  GetTrkIso(pfcands, matchedPFCand, trkiso, activity);
			  selectedMuonTrkIso->push_back(trkiso);
			  selectedMuonTrkAct->push_back(activity);
			  hadTauDecay=0;
			}
		      // store all decay productes of the tau in a new colleciton
          }
		  selectedTauHadronic->push_back(hadTauDecay);
		}
	    }

	}
	  
    }

  if (selectedTauNu->size()!=selectedTau->size()) printf("WARNING: number of tau neutrino stored and number of taus do not matched %6d %6d\n",int(selectedTauNu->size()),int(selectedTau->size()));

  // Now get properties of leading track from tau
  for (unsigned int itau(0); itau<selectedTauHadronic->size(); itau++) {
    unsigned int nNHad(0), nTrk(0);
    std::vector<int> tau_trks;
    for (unsigned int icand(0); icand<selectedTauDecayCands->size(); icand++) {
      unsigned int pdgID = abs(selectedTauDecayCandspdgID->at(icand));
      if ((unsigned)abs(selectedTauDecayCandsmomInd->at(icand)) != itau) continue;
      if (pdgID<100) continue;
      if (pdgID==211 || pdgID==321) {
  	nTrk++;
  	tau_trks.push_back(icand);
     }
      else {
  	nNHad++;
     }
    }
    selectedTauNProngs->push_back(nTrk);
    selectedTauNNHads->push_back(nNHad);
    if (nTrk>0) {
      // find the leading track
      double maxPt(0.);
      int leadTrk(0);
      for (unsigned int itk(0); itk<tau_trks.size(); itk++) {
  	if (selectedTauDecayCands->at(tau_trks[itk]).pt()>maxPt) {
  	  maxPt=tau_trks[itk];
  	  leadTrk=tau_trks[itk];
  	}
      }
      TLorentzVector p4(selectedTauDecayCands->at(leadTrk).px(),selectedTauDecayCands->at(leadTrk).py(),selectedTauDecayCands->at(leadTrk).pz(),selectedTauDecayCands->at(leadTrk).energy());
      selectedTauLeadTrk->push_back(p4);
      // now get iso and act from matched PF track
      int matched_track = MatchToPFCand(pfcands, &selectedTauDecayCands->at(leadTrk));
      if (matched_track>=0) {
  	//	printf("Matched gen pion to iso track: ptg = %3.3f, pttk = %3.3f --> d3 = %3.3f\n", selectedTauLeadTrkPT[icand], TAPPionTracks->at(matched_TAP_track).Pt(), mind3);
	float trkiso = 0.;
	float activity = 0.;
	GetTrkIso(pfcands, matched_track, trkiso, activity);
	selectedTauLeadTrkIso->push_back(trkiso);
	selectedTauLeadTrkAct->push_back(activity);	
  	selectedTauLeadTrkd3->push_back(GetGenRecoD3(pfcands, matched_track, &selectedTauDecayCands->at(leadTrk)));
      } else {
  	selectedTauLeadTrkIso->push_back(-999.);
  	selectedTauLeadTrkAct->push_back(-999.);
  	selectedTauLeadTrkd3->push_back(-999.);
     }
    } else {
      //      printf("No hadronic tracks!\n");
      selectedTauLeadTrkIso->push_back(-999.);
      selectedTauLeadTrkAct->push_back(-999.);
      selectedTauLeadTrk->push_back(TLorentzVector(0,0,0,0));
      selectedTauLeadTrkd3->push_back(-999.);
    }
  }
  
  iEvent.put(std::move(selectedBoson),"Boson");
  iEvent.put(std::move(selectedBosonPDGId),"BosonPDGId");
  iEvent.put(std::move(selectedMuon),"Muon");
  iEvent.put(std::move(selectedMuonTauDecay),"MuonTauDecay");
  iEvent.put(std::move(selectedMuonGenRecoD3),"MuonGenRecoD3");
  iEvent.put(std::move(selectedMuonTrkIso),"MuonTrkIso");
  iEvent.put(std::move(selectedMuonTrkAct),"MuonTrkAct");
  iEvent.put(std::move(selectedElectron),"Electron");
  iEvent.put(std::move(selectedElectronTauDecay),"ElectronTauDecay");
  iEvent.put(std::move(selectedElectronGenRecoD3),"ElectronGenRecoD3");
  iEvent.put(std::move(selectedElectronTrkIso),"ElectronTrkIso");
  iEvent.put(std::move(selectedElectronTrkAct),"ElectronTrkAct");
  iEvent.put(std::move(selectedTau),"Tau");
  iEvent.put(std::move(selectedTauHadronic),"TauHadronic");
  iEvent.put(std::move(selectedTauDecayCands),"TauDecayCands");
  iEvent.put(std::move(selectedTauDecayCandspdgID),"TauDecayCandspdgID");
  iEvent.put(std::move(selectedTauDecayCandsmomInd),"TauDecayCandsmomInd");
  iEvent.put(std::move(selectedTauLeadTrk),"TauLeadTrk");
  iEvent.put(std::move(selectedTauLeadTrkd3),"TauLeadTrkGenRecoD3");
  iEvent.put(std::move(selectedTauLeadTrkIso),"TauLeadTrkIso");
  iEvent.put(std::move(selectedTauLeadTrkAct),"TauLeadTrkAct");
  iEvent.put(std::move(selectedTauNProngs),"TauNProngs");
  iEvent.put(std::move(selectedTauNNHads),"TauNNHads");
  iEvent.put(std::move(selectedTauNu),"TauNu");

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenLeptonRecoCand::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

const reco::GenParticle* GenLeptonRecoCand::BosonFound(const reco::GenParticle * particle) const
{
  for(size_t i=0;i< particle->numberOfDaughters();i++)
    {
      if(abs(particle->daughter(i)->pdgId() )== 24 || abs(particle->daughter(i)->pdgId() ) == 23 || abs(particle->daughter(i)->pdgId() ) == 1000024) return BosonFound((reco::GenParticle*)particle->daughter(i));
    }
  return particle;
	
}

const reco::GenParticle* GenLeptonRecoCand::TauFound(const reco::GenParticle * particle) const
{
  for(size_t i=0;i< particle->numberOfDaughters();i++)
    {
      if(abs(particle->daughter(i)->pdgId()) == 15) return TauFound((reco::GenParticle*)particle->daughter(i));
    }
  return particle;
	
}


void GenLeptonRecoCand::GetTrkIso(edm::Handle<pat::PackedCandidateCollection> pfcands, const unsigned tkInd, float& trkiso, float& activity) const {
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

const int GenLeptonRecoCand::MatchToPFCand(edm::Handle<pat::PackedCandidateCollection> pfcands, const reco::GenParticle* gen_track) const {
  int pdgId=abs(gen_track->pdgId());
  if (pdgId!=11&&pdgId!=13) pdgId=211;
  double mind3=99999.;
  int matched_track=-1;
  for (unsigned int iPF(0); iPF<pfcands->size(); iPF++) {
    const pat::PackedCandidate &pfc = pfcands->at(iPF);
    if (pfc.charge()==0) continue;
    if (abs(pfc.pdgId())!=pdgId) continue;
    TVector3 genTrk3(gen_track->px(), gen_track->py(), gen_track->pz());
    TVector3 pf3(pfc.px(), pfc.py(), pfc.pz());
    double d3 = (genTrk3-pf3).Mag();
    if (d3<mind3) {
      mind3=d3;
      matched_track=iPF;
    }
  }
  return matched_track;
}

const double GenLeptonRecoCand::GetGenRecoD3(edm::Handle<pat::PackedCandidateCollection> pfcands, const int tkInd, const reco::GenParticle* gen_track) const {
  if (tkInd<0||tkInd>(int)pfcands->size()) return -999.;
  const pat::PackedCandidate &pfc = pfcands->at(tkInd);
  TVector3 genTrk3(gen_track->px(), gen_track->py(), gen_track->pz());
  TVector3 pf3(pfc.px(), pfc.py(), pfc.pz());
  double d3 = (genTrk3-pf3).Mag();
  return d3;
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenLeptonRecoCand);
