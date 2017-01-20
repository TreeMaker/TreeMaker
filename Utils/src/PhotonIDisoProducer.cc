// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      PhotonIDisoProducer
// 
/*

  Description: Takes as cfg input a photon collection
  recomputes sigmaIetaIeta, applies loose EGamma WP cuts,
  fills 4-vector information for the best photon, ID & ISO
  variables for all photons, and counts the number of good
  photons.
  
*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed March 7, 2014
// 

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "../interface/PhotonIDisoProducer.h"
#include "effArea.cc"

#include "TLorentzVector.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <vector>

PhotonIDisoProducer::PhotonIDisoProducer(const edm::ParameterSet& iConfig):
  photonCollection(iConfig.getUntrackedParameter<edm::InputTag>("photonCollection")),
  electronCollection(iConfig.getUntrackedParameter<edm::InputTag>("electronCollection")),
  conversionCollection(iConfig.getUntrackedParameter<edm::InputTag>("conversionCollection")),
  beamspotCollection(iConfig.getUntrackedParameter<edm::InputTag>("beamspotCollection")),
  ecalRecHitsInputTag_EE_(iConfig.getParameter<edm::InputTag>("ecalRecHitsInputTag_EE")),
  ecalRecHitsInputTag_EB_(iConfig.getParameter<edm::InputTag>("ecalRecHitsInputTag_EB")),
  rhoCollection(iConfig.getUntrackedParameter<edm::InputTag>("rhoCollection")),
  genParCollection(iConfig.getUntrackedParameter<edm::InputTag>("genParCollection")),
  photonTok_(consumes<edm::View<pat::Photon>>(photonCollection)),
  electronTok_(consumes<pat::ElectronCollection>(electronCollection)),
  conversionTok_(consumes<std::vector<reco::Conversion>>(conversionCollection)),
  beamspotTok_(consumes<reco::BeamSpot>(beamspotCollection)),
  ecalRecHitsInputTag_EE_Token_(consumes<EcalRecHitCollection>(ecalRecHitsInputTag_EE_)),
  ecalRecHitsInputTag_EB_Token_(consumes<EcalRecHitCollection>(ecalRecHitsInputTag_EB_)),
  rhoTok_(consumes<double>(rhoCollection)),
  genParTok_(consumes<edm::View<reco::GenParticle>>(genParCollection)),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{

  ecalRecHitsInputTag_EE_Token_ = consumes<EcalRecHitCollection>(ecalRecHitsInputTag_EE_);
  ecalRecHitsInputTag_EB_Token_ = consumes<EcalRecHitCollection>(ecalRecHitsInputTag_EB_);

  produces< std::vector< pat::Photon > >(); 
  produces< std::vector< double > >("isEB");
  produces< std::vector< double > >("genMatched"); 
  produces< std::vector< double > >("hadTowOverEM"); 
  produces< std::vector< double > >("sigmaIetaIeta"); 
  produces< std::vector< double > >("pfChargedIso"); 
  produces< std::vector< double > >("pfNeutralIso"); 
  produces< std::vector< double > >("pfGammaIso"); 
  produces< std::vector< double > >("pfChargedIsoRhoCorr"); 
  produces< std::vector< double > >("pfNeutralIsoRhoCorr"); 
  produces< std::vector< double > >("pfGammaIsoRhoCorr"); 
  produces< std::vector< double > >("hasPixelSeed"); 
  produces< std::vector< double > >("passElectronVeto"); 
  produces< std::vector< bool > >("hadronization");
  produces< std::vector< bool > >("nonPrompt");
  produces< std::vector< bool > >("fullID");
  produces< std::vector< bool > >("electronFakes");
  produces< bool >("hasGenPromptPhoton");
}


PhotonIDisoProducer::~PhotonIDisoProducer()
{
 
   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PhotonIDisoProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  
  auto goodPhotons  = std::make_unique<std::vector<pat::Photon>>();
  auto photon_isEB = std::make_unique<std::vector<double>>();
  auto photon_genMatched = std::make_unique<std::vector<double>>();
  auto photon_hadTowOverEM = std::make_unique<std::vector<double>>();
  auto photon_sigmaIetaIeta = std::make_unique<std::vector<double>>();
  auto photon_pfGammaIso = std::make_unique<std::vector<double>>();
  auto photon_pfChargedIso = std::make_unique<std::vector<double>>();
  auto photon_pfNeutralIso = std::make_unique<std::vector<double>>();
  auto photon_pfGammaIsoRhoCorr = std::make_unique<std::vector<double>>();
  auto photon_pfChargedIsoRhoCorr = std::make_unique<std::vector<double>>();
  auto photon_pfNeutralIsoRhoCorr = std::make_unique<std::vector<double>>();
  auto photon_hasPixelSeed = std::make_unique<std::vector<double>>();
  auto photon_passElectronVeto = std::make_unique<std::vector<double>>();
  auto   photon_hadronization = std::make_unique<std::vector<bool>>();
  auto   photon_nonPrompt  = std::make_unique<std::vector<bool>>();
  auto   photon_fullID  = std::make_unique<std::vector<bool>>();
  auto   photon_electronFakes  = std::make_unique<std::vector<bool>>();

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  }
  
  Handle< View< pat::Photon> > photonCands;
  iEvent.getByToken( photonTok_,photonCands);
  Handle<pat::ElectronCollection> electrons;
  iEvent.getByToken(electronTok_, electrons);
  Handle<vector<reco::Conversion> > conversions;
  iEvent.getByToken(conversionTok_,conversions);
  Handle<reco::BeamSpot> beamSpot;
  iEvent.getByToken(beamspotTok_,beamSpot);
  edm::Handle< View<reco::GenParticle> > genParticles;
  iEvent.getByToken( genParTok_,genParticles);
  edm::Handle< double > rho_;
  iEvent.getByToken(rhoTok_,rho_);
  double rho = *rho_;

  if( debug ) std::cout << "got photon collection" << std::endl;


  // - - - - - - - - - - - - - - - - - - - - 
  // Initializing effective area to be used 
  // for rho corrections to the photon isolation
  // variables. 
  // - - - - - - - - - - - - - - - - - - - - 
  //addEffA(etaLow_, etaHigh_, effA_pfCh_, effA_pfNu_, effA_pfGa_); 
  effArea effAreas;
  effAreas.addEffA(0.,    1.0,   0.0, 0.0599, 0.1271);
  effAreas.addEffA(1.0,   1.479, 0.0, 0.0819, 0.1101);
  effAreas.addEffA(1.479, 2.0,   0.0, 0.0696, 0.0756);
  effAreas.addEffA(2.0,   2.2,   0.0, 0.0360, 0.1175);
  effAreas.addEffA(2.2,   2.3,   0.0, 0.0360, 0.1498);
  effAreas.addEffA(2.3,   2.4,   0.0, 0.0462, 0.1857);
  effAreas.addEffA(2.4,   99.,   0.0, 0.0656, 0.2183);

  /// setup cluster tools
  noZS::EcalClusterLazyTools clusterTools_(iEvent, iSetup, ecalRecHitsInputTag_EB_Token_, ecalRecHitsInputTag_EE_Token_);
        
  for( View< pat::Photon >::const_iterator iPhoton = photonCands->begin(); iPhoton != photonCands->end(); ++iPhoton){

    if( debug ) {
      std::cout << "photon pt: " << iPhoton->pt() << std::endl;
      std::cout << "photon eta: " << iPhoton->eta() << std::endl;
      std::cout << "photon phi: " << iPhoton->phi() << std::endl;
    }

    std::vector<float> vCov = clusterTools_.localCovariances( *(iPhoton->superCluster()->seed()) ); 
    const float sieie = (isnan(vCov[0]) ? 0. : sqrt(vCov[0])); 
    
    double chIso = effAreas.rhoCorrectedIso(  pfCh  , iPhoton->chargedHadronIso() , iPhoton->eta() , rho ); 
    double nuIso = effAreas.rhoCorrectedIso(  pfNu  , iPhoton->neutralHadronIso() , iPhoton->eta() , rho ); 
    double gamIso = effAreas.rhoCorrectedIso( pfGam , iPhoton->photonIso()        , iPhoton->eta() , rho ); 

    // apply photon selection -- all good photons will be saved
    // use loose selection with no sieie or chiso cuts
    bool isBarrelPhoton=false;
    bool isEndcapPhoton=false;
    bool passID=false;
    bool passIDLoose=false;
    bool passIso=false;
    bool passIsoLoose=false;
    bool passAcc=false;

    double PhEta=iPhoton->eta();

    if(fabs(PhEta) < 1.4442  ){
      isBarrelPhoton=true;
    }
    else if(fabs(PhEta)>1.566 && fabs(PhEta)<2.5){
      isEndcapPhoton=true;
    }
    else {
      isBarrelPhoton=false;
      isEndcapPhoton=false;
    }

    if(isBarrelPhoton || isEndcapPhoton){
      passAcc=true;
    }
    
    // apply id cuts
    if (isBarrelPhoton) {
      if (iPhoton->hadTowOverEm() < 0.05 && !hasMatchedPromptElectron(iPhoton->superCluster(), electrons, conversions, beamSpot->position())) {
         passIDLoose = true;
         if (sieie < 0.0102) {
            passID = true;
         }
      }
    } else if (isEndcapPhoton) {
      if (iPhoton->hadTowOverEm() < 0.05 && !hasMatchedPromptElectron(iPhoton->superCluster(), electrons, conversions, beamSpot->position())) {
         passIDLoose = true;
         if (sieie < 0.0274) {
            passID = true;
         }
      }
    }
 
    // apply isolation cuts
    if (isBarrelPhoton) {
      if (nuIso < (1.92 + 0.014*iPhoton->pt() + 0.000019*iPhoton->pt()*iPhoton->pt()) && gamIso < (0.81 + 0.0053*iPhoton->pt())) {
        passIsoLoose = true;
        if (chIso < 3.32) {
           passIso = true;
        }
      }
    } else if (isEndcapPhoton) {
      if (nuIso < (11.86 + 0.0139*iPhoton->pt() + 0.000025*iPhoton->pt()*iPhoton->pt())  && gamIso < (0.83 + 0.0034*iPhoton->pt())) {
        passIsoLoose = true;
        if (chIso < 1.97) {
          passIso = true;
        }
      }
    }

    // check if photon is a good loose photon
    if( passAcc && passIDLoose && passIsoLoose && iPhoton->pt() > 100.0){//pure photons
      goodPhotons->push_back( *iPhoton );
      photon_isEB->push_back( iPhoton->isEB() );
      photon_genMatched->push_back( iPhoton->genPhoton() != NULL );
      photon_hadTowOverEM->push_back( iPhoton->hadTowOverEm() ) ;
      photon_sigmaIetaIeta->push_back( sieie );
      photon_pfChargedIso->push_back(      iPhoton->chargedHadronIso() );
      photon_pfGammaIso->push_back(        iPhoton->photonIso() );
      photon_pfNeutralIso->push_back(      iPhoton->neutralHadronIso() );
      photon_pfChargedIsoRhoCorr->push_back( chIso  );
      photon_pfGammaIsoRhoCorr->push_back(   gamIso  );
      photon_pfNeutralIsoRhoCorr->push_back( nuIso );
      photon_hasPixelSeed->push_back( iPhoton->hasPixelSeed() );
      photon_passElectronVeto->push_back( !hasMatchedPromptElectron(iPhoton->superCluster(),electrons, conversions, beamSpot->position()) );
      photon_fullID->push_back(passID&&passIso);

      if (genParticles.isValid()){//genLevel Stuff
        // loop over gen particles and find nonprompt and hadronization photons
        int matchedGenPrompt = 0;
        int matchedGenNonPrompt = 0 ;
	bool photonMatchGenE = false;        
        for( View<reco::GenParticle>::const_iterator iGen = genParticles->begin();
             iGen != genParticles->end();
             ++iGen){
	  
          // check for non-prompt photons ----------------------
          if( iGen->pdgId() == 22 && ( ( iGen->status() / 10 ) == 2 || iGen->status() == 1 || iGen->status() == 2 ) ){
	    
            TLorentzVector gen( iGen->px() , iGen->py() , iGen->pz() , iGen->energy() );
            TLorentzVector photon( iPhoton->px() , iPhoton->py() , iPhoton->pz() , iPhoton->energy() );
        
            if( gen.DeltaR(photon) < 0.2 ){ /// I LEFT OFF HERE!!!!!!
              if( abs(iGen->mother()->pdgId()) > 100 && abs(iGen->mother()->pdgId()) < 1000000 && abs(iGen->mother()->pdgId()) != 2212 ) matchedGenNonPrompt++ ;
              if( abs(iGen->mother()->pdgId()) <= 100 || abs(iGen->mother()->pdgId()) == 2212 ){
		if( gen.Pt()/photon.Pt() > 0.5 && gen.Pt()/photon.Pt() < 1.5 )
		  matchedGenPrompt++ ;
	      }//for prmopt photons
            }//gen matching
          }
	  //check wheather photon has matched to a gen electron or not
	  if( abs(iGen->pdgId()) == 11 && iGen->status() == 1 ){
	    if( (deltaR(iGen->p4(), iPhoton->p4())) < 0.2)
	      photonMatchGenE = true;
	  }
        
          // ----------------------------------------------------
        
          // check for hadronization photons --------------------
        //  if( abs(iGen->pdgId()) < 6 && ( iGen->status() / 10 ) == 2){
        
            //TLorentzVector gen2( iGen->px() , iGen->py() , iGen->pz() , iGen->energy() );
            //TLorentzVector photon2( iPhoton->px() , iPhoton->py() , iPhoton->pz() , iPhoton->energy() );
        
            //if( gen2.DeltaR(photon2) < 0.4 ) isHadronization = true;
        
         // }
          // ----------------------------------------------------
        
        }// end loop over gen particles

        if( matchedGenPrompt > 0 || matchedGenNonPrompt == 0 ) photon_nonPrompt->push_back(false);
        else if( matchedGenNonPrompt > 0 ) photon_nonPrompt->push_back(true);
        else photon_nonPrompt->push_back(false);
	//check if photon is fake or not.
	if( matchedGenPrompt == 0 && photonMatchGenE )//make sure that photon is matched to gen electron and not matched to any gen prompt photon
	  photon_electronFakes->push_back(true);
	else
	  photon_electronFakes->push_back(false);
      }//gen level stuff
    //photon_hadronization->push_back( isHadronization );

    }//pure photons

  }// end loop over candidate photons
  bool foundGenPrompt = false;
  if (genParticles.isValid()){
    for( View<reco::GenParticle>::const_iterator iGen = genParticles->begin();
	 iGen != genParticles->end();
	 ++iGen){  
      if( iGen->pdgId() == 22 && ( ( iGen->status() / 10 ) == 2 || iGen->status() == 1 || iGen->status() == 2 ) ){
	TLorentzVector gen( iGen->px() , iGen->py() , iGen->pz() , iGen->energy() );
	if( gen.Pt() > 40.0 && (abs(iGen->mother()->pdgId()) <= 100 || abs(iGen->mother()->pdgId()) == 2212 ) ){
	  foundGenPrompt = true;
	  //	  cout<<gen.Pt()<<" "<<abs(iGen->mother()->pdgId())<<" pdg: "<<iGen->pdgId()<<endl;
	  break;
	}//if there is a photon with pt > 10 and its parent PdgID <=100, then consider the event as having a hard scattered photon.
      }
    }// end of loop over gen particles
  }
  
  iEvent.put(std::move(goodPhotons)); 
  iEvent.put(std::move(photon_isEB ), "isEB" );
  iEvent.put(std::move(photon_genMatched ), "genMatched" );
  iEvent.put(std::move(photon_hadTowOverEM ), "hadTowOverEM" );
  iEvent.put(std::move(photon_sigmaIetaIeta ), "sigmaIetaIeta" );
  iEvent.put(std::move(photon_pfChargedIso ), "pfChargedIso" );
  iEvent.put(std::move(photon_pfNeutralIso ), "pfNeutralIso" );
  iEvent.put(std::move(photon_pfGammaIso ), "pfGammaIso" );
  iEvent.put(std::move(photon_pfChargedIsoRhoCorr ), "pfChargedIsoRhoCorr" );
  iEvent.put(std::move(photon_pfNeutralIsoRhoCorr ), "pfNeutralIsoRhoCorr" );
  iEvent.put(std::move(photon_pfGammaIsoRhoCorr ), "pfGammaIsoRhoCorr" );
  iEvent.put(std::move(photon_hasPixelSeed ), "hasPixelSeed" );
  iEvent.put(std::move(photon_passElectronVeto ), "passElectronVeto" );
  iEvent.put(std::move(photon_nonPrompt ), "nonPrompt" );
  iEvent.put(std::move(photon_fullID ), "fullID" );
  iEvent.put(std::move(photon_electronFakes ), "electronFakes" );
  auto hasGenPromptPhoton = std::make_unique<bool>(foundGenPrompt);  
  iEvent.put(std::move(hasGenPromptPhoton ), "hasGenPromptPhoton" );
 
}

// copied from https://github.com/RazorCMS/SUSYBSMAnalysis-RazorTuplizer/blob/6072ffb43bbeb3f6b34cf8a96426c7f104c5b902/plugins/RazorAux.cc#L127
//check if a given SuperCluster matches to at least one GsfElectron having zero expected inner hits
//and not matching any conversion in the collection passing the quality cuts
bool PhotonIDisoProducer::hasMatchedPromptElectron(const reco::SuperClusterRef &sc, const edm::Handle<std::vector<pat::Electron> > &eleCol,
                                                   const edm::Handle<reco::ConversionCollection> &convCol, const math::XYZPoint &beamspot,
                                                   float lxyMin, float probMin, unsigned int nHitsBeforeVtxMax)
{
  if (sc.isNull()) return false;
  for (std::vector<pat::Electron>::const_iterator it = eleCol->begin(); it!=eleCol->end(); ++it) {
    //match electron to supercluster
    if (it->superCluster()!=sc) continue;
    //check expected inner hits
    if (it->gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) > 0) continue;
    //check if electron is matching to a conversion
    if (ConversionTools::hasMatchedConversion(*it,convCol,beamspot,lxyMin,probMin,nHitsBeforeVtxMax)) continue;
    return true;
  }
  return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 

PhotonIDisoProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PhotonIDisoProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
PhotonIDisoProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PhotonIDisoProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PhotonIDisoProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PhotonIDisoProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PhotonIDisoProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(PhotonIDisoProducer);
