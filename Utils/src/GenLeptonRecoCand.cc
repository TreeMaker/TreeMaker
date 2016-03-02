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
#include "FWCore/Framework/interface/EDProducer.h"

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

class GenLeptonRecoCand : public edm::EDProducer {
public:
  explicit GenLeptonRecoCand(const edm::ParameterSet&);
  ~GenLeptonRecoCand();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag PrunedGenParticleTag_;
  edm::InputTag pfCandsTag_;
  edm::EDGetTokenT<edm::View<reco::GenParticle>> PrunedGenParticleTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> pfCandsTok_;
  int pdgID_;
	
  const reco::GenParticle* BosonFound(const reco::GenParticle * particle);
  const reco::GenParticle* TauFound(const reco::GenParticle * particle);

  void GetTrkIso(edm::Handle<pat::PackedCandidateCollection> pfcands, const unsigned tkInd, float& trkiso, float& activity);
  const int MatchToPFCand(edm::Handle<pat::PackedCandidateCollection> pfcands, const reco::GenParticle* gen_track);
  const double GetGenRecoD3(edm::Handle<pat::PackedCandidateCollection> pfcands, const int tkInd, const reco::GenParticle* gen_track);
	
	
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
  
  const std::string string1("Boson");
  const std::string string1t("BosonPDGId");
  const std::string string2("Muon");
  const std::string string2t("MuonTauDecay");
  const std::string string2tt("MuonGenRecoD3");
  const std::string string2ttt("MuonTrkIso");
  const std::string string2tttt("MuonTrkAct");
  const std::string string3("Electron");
  const std::string string3t("ElectronTauDecay");
  const std::string string3tt("ElectronGenRecoD3");
  const std::string string3ttt("ElectronTrkIso");
  const std::string string3tttt("ElectronTrkAct");
  const std::string string4("Tau");
  const std::string string4t("TauHadronic");
  const std::string string4tt("TauDecayCands");
  const std::string string4tt2("TauDecayCandspdgID");
  const std::string string4tt3("TauDecayCandsmomInd");
  const std::string string4tt4("TauLeadTrk");
  const std::string string4tt5("TauLeadTrkGenRecoD3");
  const std::string string4tt6("TauLeadTrkIso");
  const std::string string4tt7("TauLeadTrkAct");
  const std::string string4ttt("TauNProngs");
  const std::string string4ttt2("TauNNHads");
  const std::string string5("TauNu");
  const std::string string6("TauNuMomPt");

  produces<std::vector<reco::GenParticle> > (string1).setBranchAlias(string1);
  produces<std::vector<int> > (string1t).setBranchAlias(string1t);
  produces<std::vector<reco::GenParticle> > (string2).setBranchAlias(string2);
  produces<std::vector<int> > (string2t).setBranchAlias(string2t);
  produces<std::vector<double> > (string2tt).setBranchAlias(string2tt);
  produces<std::vector<double> > (string2ttt).setBranchAlias(string2ttt);
  produces<std::vector<double> > (string2tttt).setBranchAlias(string2ttt);
  produces<std::vector<reco::GenParticle> > (string3).setBranchAlias(string3);
  produces<std::vector<int> > (string3t).setBranchAlias(string3t);
  produces<std::vector<double> > (string3tt).setBranchAlias(string3tt);
  produces<std::vector<double> > (string3ttt).setBranchAlias(string3ttt);
  produces<std::vector<double> > (string3tttt).setBranchAlias(string3ttt);
  produces<std::vector<reco::GenParticle> > (string4).setBranchAlias(string4);
  produces<std::vector<int> > (string4t).setBranchAlias(string4t);
  produces<std::vector<reco::GenParticle> > (string4tt).setBranchAlias(string4tt);
  produces<std::vector<int> > (string4tt2).setBranchAlias(string4tt2);
  produces<std::vector<int> > (string4tt3).setBranchAlias(string4tt3);
  produces<std::vector<TLorentzVector> > (string4tt4).setBranchAlias(string4tt4);
  produces<std::vector<double> > (string4tt5).setBranchAlias(string4tt5);
  produces<std::vector<double> > (string4tt6).setBranchAlias(string4tt6);
  produces<std::vector<double> > (string4tt7).setBranchAlias(string4tt7);
  produces<std::vector<int> > (string4ttt).setBranchAlias(string4ttt);
  produces<std::vector<int> > (string4ttt2).setBranchAlias(string4ttt2);
  produces<std::vector<reco::GenParticle> > (string5).setBranchAlias(string5);
  produces<std::vector<double> > (string6).setBranchAlias(string6);
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
GenLeptonRecoCand::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //  std::cout<<"Running GenLeptonRecoCand"<<std::endl;

  using namespace edm;	
  std::auto_ptr< std::vector<reco::GenParticle> > selectedBoson(new std::vector<reco::GenParticle>);
  std::auto_ptr< std::vector<int> > selectedBosonPDGId(new std::vector<int>);
  std::auto_ptr< std::vector<reco::GenParticle> > selectedMuon(new std::vector<reco::GenParticle>);
  std::auto_ptr< std::vector<int> > selectedMuonTauDecay(new std::vector<int>);
  std::auto_ptr< std::vector<double> > selectedMuonGenRecoD3(new std::vector<double>);
  std::auto_ptr< std::vector<double> > selectedMuonTrkIso(new std::vector<double>);
  std::auto_ptr< std::vector<double> > selectedMuonTrkAct(new std::vector<double>);
  std::auto_ptr< std::vector<reco::GenParticle> > selectedElectron(new std::vector<reco::GenParticle>);
  std::auto_ptr< std::vector<int> > selectedElectronTauDecay(new std::vector<int>);
  std::auto_ptr< std::vector<double> > selectedElectronGenRecoD3(new std::vector<double>);
  std::auto_ptr< std::vector<double> > selectedElectronTrkIso(new std::vector<double>);
  std::auto_ptr< std::vector<double> > selectedElectronTrkAct(new std::vector<double>);
  std::auto_ptr< std::vector<reco::GenParticle> > selectedTau(new std::vector<reco::GenParticle>);
  std::auto_ptr< std::vector<int> > selectedTauHadTronic(new std::vector<int>);
  std::auto_ptr< std::vector<reco::GenParticle> > selectedTauDecayCands(new std::vector<reco::GenParticle>);
  std::auto_ptr< std::vector<int> > selectedTauDecayCandspdgID(new std::vector<int>);
  std::auto_ptr< std::vector<int> > selectedTauDecayCandsmomInd(new std::vector<int>);
  std::auto_ptr< std::vector<TLorentzVector> > selectedTauLeadTrk(new std::vector<TLorentzVector>);
  std::auto_ptr< std::vector<double> > selectedTauLeadTrkd3(new std::vector<double>);
  std::auto_ptr< std::vector<double> > selectedTauLeadTrkIso(new std::vector<double>);
  std::auto_ptr< std::vector<double> > selectedTauLeadTrkAct(new std::vector<double>);
  std::auto_ptr< std::vector<int> > selectedTauNProngs(new std::vector<int>);
  std::auto_ptr< std::vector<int> > selectedTauNNHads(new std::vector<int>);

  std::auto_ptr< std::vector<reco::GenParticle> > selectedTauNu(new std::vector<reco::GenParticle>);
  Handle<edm::View<reco::GenParticle> > pruned;
  iEvent.getByToken(PrunedGenParticleTok_,pruned);

  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(pfCandsTok_, pfcands);

  for(size_t i=0; i<pruned->size();i++)
    {
      if( (abs((*pruned)[i].pdgId() ) == 24 || abs((*pruned)[i].pdgId() ) == 23 ) && (*pruned)[i].status()==22) // needs to be checked if this workes for Z 23 as well
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

		  // 					selectedTauHadTronic->push_back(0);
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

		  int hadTauDecay=1;
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

						
		      // 						else std::cout<<"No lep decay tau with daughters["<<iii<<"]: "<<FinalTauDecay->daughter(iii)->pdgId()<<std::endl;
		    }
		  selectedTauHadTronic->push_back(hadTauDecay);
		}
	    }

	}
	  
    }

  if (selectedTauNu->size()!=selectedTau->size()) printf("WARNING: number of tau neutrino stored and number of taus do not matched %6d %6d\n",int(selectedTauNu->size()),int(selectedTau->size()));

  // Now get properties of leading track from tau
  for (unsigned int itau(0); itau<selectedTauHadTronic->size(); itau++) {
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
  
  //  std::cout<<"Putting stuff back into event"<<std::endl;

  const std::string string1("Boson");
  const std::string string1t("BosonPDGId");
  const std::string string2("Muon");
  const std::string string2t("MuonTauDecay");
  const std::string string2tt("MuonGenRecoD3");
  const std::string string2ttt("MuonTrkIso");
  const std::string string2tttt("MuonTrkAct");
  const std::string string3("Electron");
  const std::string string3t("ElectronTauDecay");
  const std::string string3tt("ElectronGenRecoD3");
  const std::string string3ttt("ElectronTrkIso");
  const std::string string3tttt("ElectronTrkAct");
  const std::string string4("Tau");
  const std::string string4t("TauHadronic");
  const std::string string4tt("TauDecayCands");
  const std::string string4tt2("TauDecayCandspdgID");
  const std::string string4tt3("TauDecayCandsmomInd");
  const std::string string4tt4("TauLeadTrk");
  const std::string string4tt5("TauLeadTrkGenRecoD3");
  const std::string string4tt6("TauLeadTrkIso");
  const std::string string4tt7("TauLeadTrkAct");
  const std::string string4ttt("TauNProngs");
  const std::string string4ttt2("TauNNHads");
  const std::string string5("TauNu");
  iEvent.put(selectedBoson,string1);
  iEvent.put(selectedBosonPDGId,string1t);
  iEvent.put(selectedMuon,string2);
  iEvent.put(selectedMuonTauDecay,string2t);
  iEvent.put(selectedMuonGenRecoD3,string2tt);
  iEvent.put(selectedMuonTrkIso,string2ttt);
  iEvent.put(selectedMuonTrkAct,string2tttt);
  iEvent.put(selectedElectron,string3);
  iEvent.put(selectedElectronTauDecay,string3t);
  iEvent.put(selectedElectronGenRecoD3,string3tt);
  iEvent.put(selectedElectronTrkIso,string3ttt);
  iEvent.put(selectedElectronTrkAct,string3tttt);
  iEvent.put(selectedTau,string4);
  iEvent.put(selectedTauHadTronic,string4t);
  iEvent.put(selectedTauDecayCands,string4tt);
  iEvent.put(selectedTauDecayCandspdgID,string4tt2);
  iEvent.put(selectedTauDecayCandsmomInd,string4tt3);
  iEvent.put(selectedTauLeadTrk,string4tt4);
  iEvent.put(selectedTauLeadTrkd3,string4tt5);
  iEvent.put(selectedTauLeadTrkIso,string4tt6);
  iEvent.put(selectedTauLeadTrkAct,string4tt7);
  iEvent.put(selectedTauNProngs,string4ttt);
  iEvent.put(selectedTauNNHads,string4ttt2);
  iEvent.put(selectedTauNu,string5);

  //  std::cout<<"DONE!"<<std::endl;
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
GenLeptonRecoCand::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenLeptonRecoCand::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
GenLeptonRecoCand::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GenLeptonRecoCand::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GenLeptonRecoCand::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GenLeptonRecoCand::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
const reco::GenParticle* GenLeptonRecoCand::BosonFound(const reco::GenParticle * particle)
{
  for(size_t i=0;i< particle->numberOfDaughters();i++)
    {
      if(abs(particle->daughter(i)->pdgId() )== 24 || abs(particle->daughter(i)->pdgId() ) == 23 ) return BosonFound((reco::GenParticle*)particle->daughter(i));
    }
  return particle;
	
}

const reco::GenParticle* GenLeptonRecoCand::TauFound(const reco::GenParticle * particle)
{
  for(size_t i=0;i< particle->numberOfDaughters();i++)
    {
      if(abs(particle->daughter(i)->pdgId()) == 15) return TauFound((reco::GenParticle*)particle->daughter(i));
    }
  return particle;
	
}


void GenLeptonRecoCand::GetTrkIso(edm::Handle<pat::PackedCandidateCollection> pfcands, const unsigned tkInd, float& trkiso, float& activity) {
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

const int GenLeptonRecoCand::MatchToPFCand(edm::Handle<pat::PackedCandidateCollection> pfcands, const reco::GenParticle* gen_track) {
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

const double GenLeptonRecoCand::GetGenRecoD3(edm::Handle<pat::PackedCandidateCollection> pfcands, const int tkInd, const reco::GenParticle* gen_track) {
  if (tkInd<0||tkInd>(int)pfcands->size()) return -999.;
  const pat::PackedCandidate &pfc = pfcands->at(tkInd);
  TVector3 genTrk3(gen_track->px(), gen_track->py(), gen_track->pz());
  TVector3 pf3(pfc.px(), pfc.py(), pfc.pz());
  double d3 = (genTrk3-pf3).Mag();
  return d3;
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenLeptonRecoCand);
