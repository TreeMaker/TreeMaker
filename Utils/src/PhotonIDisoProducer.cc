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
  
  std::auto_ptr< std::vector< pat::Photon > > goodPhotons ( new std::vector< pat::Photon >() );
  std::auto_ptr< std::vector< double > > photon_isEB( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_genMatched( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_hadTowOverEM( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_sigmaIetaIeta( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_pfGammaIso( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_pfChargedIso( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_pfNeutralIso( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_pfGammaIsoRhoCorr( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_pfChargedIsoRhoCorr( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_pfNeutralIsoRhoCorr( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_hasPixelSeed( new std::vector< double > () );
  std::auto_ptr< std::vector< double > > photon_passElectronVeto( new std::vector< double > () );
  std::auto_ptr< std::vector< bool > >   photon_hadronization( new std::vector< bool > () );
  std::auto_ptr< std::vector< bool > >   photon_nonPrompt ( new std::vector< bool > () );

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  
  }
  
  Handle< View< pat::Photon> > photonCands;
  iEvent.getByLabel( photonCollection ,photonCands);
  Handle<pat::ElectronCollection> electrons;
  iEvent.getByLabel(electronCollection, electrons);
  Handle<vector<reco::Conversion> > conversions;
  iEvent.getByLabel(conversionCollection,conversions);
  Handle<reco::BeamSpot> beamSpot;
  iEvent.getByLabel(beamspotCollection,beamSpot);
  edm::Handle< View<reco::GenParticle> > genParticles;
  iEvent.getByLabel( genParCollection ,genParticles);
  edm::Handle< double > rho_;
  iEvent.getByLabel(rhoCollection,rho_);
  double rho = *rho_;

  if( debug ) std::cout << "got photon collection" << std::endl;


  // - - - - - - - - - - - - - - - - - - - - 
  // Initializing effective area to be used 
  // for rho corrections to the photon isolation
  // variables. 
  // - - - - - - - - - - - - - - - - - - - - 
  effArea effAreas;
  effAreas.addEffA( 0.0, 1.0, 0.0234, 0.0053, 0.078 );
  effAreas.addEffA( 1.0, 1.479, 0.0189, 0.0130, 0.0629 );
  effAreas.addEffA( 1.479, 2.0, 0.0171, 0.0057, 0.0264 );
  effAreas.addEffA( 2.0, 2.2, 0.0129, 0.0070, 0.0462 );
  effAreas.addEffA( 2.2, 2.3, 0.0110, 0.0152, 0.0740 );
  effAreas.addEffA( 2.3, 2.4, 0.0074, 0.0232, 0.0924 );
  effAreas.addEffA( 2.4, 99., 0.0035, 0.1709, 0.1484 );

  /// setup cluster tools
  noZS::EcalClusterLazyTools clusterTools_(iEvent, iSetup, ecalRecHitsInputTag_EB_Token_, ecalRecHitsInputTag_EE_Token_);
        
  for( View< pat::Photon >::const_iterator iPhoton = photonCands->begin();
        iPhoton != photonCands->end();
        ++iPhoton){

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
    bool passIDLoose=false;
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
    if(isBarrelPhoton){
      //if(iPhoton->hadTowOverEm() < 0.028 && !hasMatchedPromptElectron(iPhoton->superCluster(),electrons, conversions, beamSpot->position()) && sieie < 0.0107){//id criterias barrel
      //  passID=true;
      //}//id criterias barrel
      if(iPhoton->hadTowOverEm() < 0.028 && !hasMatchedPromptElectron(iPhoton->superCluster(),electrons, conversions, beamSpot->position())){//id criterias barrel (loose, no sieie cut)
        passIDLoose=true;
      }//id criterias barrel (loose)
    } 
    else if(isEndcapPhoton){
      //if(iPhoton->hadTowOverEm() < 0.093 && !hasMatchedPromptElectron(iPhoton->superCluster(),electrons, conversions, beamSpot->position()) && sieie < 0.0272){//id criteria endcap
      //  passID=true;
      //}//id criterias endcap
      if(iPhoton->hadTowOverEm() < 0.093 && !hasMatchedPromptElectron(iPhoton->superCluster(),electrons, conversions, beamSpot->position())){//id criteria endcap (loose, no sieie cut)
        passIDLoose=true;
      }//id criterias endcap (loose)
    }
 
    // apply isolation cuts
    if(isBarrelPhoton){
      //if(chIso <2.67 && nuIso <  (7.23 + TMath::Exp(0.0028*(iPhoton->pt()+0.5408)))  && gamIso < ( 2.11 + 0.0014*(iPhoton->pt())) ){
      //  passIso=true;      
      //}
      if(nuIso <  (7.23 + TMath::Exp(0.0028*(iPhoton->pt()+0.5408)))  && gamIso < ( 2.11 + 0.0014*(iPhoton->pt())) ){//loose, no charged iso cut
        passIsoLoose=true;      
      }
    }
    else if(isEndcapPhoton){
      //if(chIso <1.79 && nuIso <  (8.89 + 0.01725*(iPhoton->pt()))  && gamIso < ( 3.09 + 0.0091*(iPhoton->pt())) ){
      //  passIso=true;
      //}
      if(nuIso <  (8.89 + 0.01725*(iPhoton->pt()))  && gamIso < ( 3.09 + 0.0091*(iPhoton->pt())) ){//loose, no charged iso cut
        passIsoLoose=true;
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


      if (genParticles.isValid()){//genLevel Stuff
        // loop over gen particles and find nonprompt and hadronization photons
        int matchedGenPrompt = 0;
        int matchedGenNonPrompt = 0 ;
        
        for( View<reco::GenParticle>::const_iterator iGen = genParticles->begin();
             iGen != genParticles->end();
             ++iGen){
        
          // check for non-prompt photons ----------------------
          if( iGen->pdgId() == 22 && ( ( iGen->status() / 10 ) == 2 || iGen->status() == 1 || iGen->status() == 2 ) ){
        
            TLorentzVector gen( iGen->px() , iGen->py() , iGen->pz() , iGen->energy() );
            TLorentzVector photon( iPhoton->px() , iPhoton->py() , iPhoton->pz() , iPhoton->energy() );
        
            if( gen.DeltaR(photon) < 0.2 ){ /// I LEFT OFF HERE!!!!!!
              if( abs(iGen->mother()->pdgId()) > 100 && abs(iGen->mother()->pdgId()) != 2212 ) matchedGenNonPrompt++ ;
              if( abs(iGen->mother()->pdgId()) <= 22 || abs(iGen->mother()->pdgId()) == 2212 ) matchedGenPrompt++ ;
            }
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
      }//gen level stuff
    //photon_hadronization->push_back( isHadronization );

    }//pure photons

  }// end loop over candidate photons
  iEvent.put(goodPhotons); 
  iEvent.put(photon_isEB , "isEB" );
  iEvent.put(photon_genMatched , "genMatched" );
  iEvent.put(photon_hadTowOverEM , "hadTowOverEM" );
  iEvent.put(photon_sigmaIetaIeta , "sigmaIetaIeta" );
  iEvent.put(photon_pfChargedIso , "pfChargedIso" );
  iEvent.put(photon_pfNeutralIso , "pfNeutralIso" );
  iEvent.put(photon_pfGammaIso , "pfGammaIso" );
  iEvent.put(photon_pfChargedIsoRhoCorr , "pfChargedIsoRhoCorr" );
  iEvent.put(photon_pfNeutralIsoRhoCorr , "pfNeutralIsoRhoCorr" );
  iEvent.put(photon_pfGammaIsoRhoCorr , "pfGammaIsoRhoCorr" );
  iEvent.put(photon_hasPixelSeed , "hasPixelSeed" );
  iEvent.put(photon_passElectronVeto , "passElectronVeto" );
  iEvent.put(photon_nonPrompt , "nonPrompt" );

 
}

// copied from https://github.com/RazorCMS/SUSYBSMAnalysis-RazorTuplizer/blob/6072ffb43bbeb3f6b34cf8a96426c7f104c5b902/plugins/RazorAux.cc#L127
//check if a given SuperCluster matches to at least one GsfElectron having zero expected inner hits
//and not matching any conversion in the collection passing the quality cuts
bool PhotonIDisoProducer::hasMatchedPromptElectron(const reco::SuperClusterRef &sc, const edm::Handle<std::vector<pat::Electron> > &eleCol,
						   const edm::Handle<reco::ConversionCollection> &convCol, const math::XYZPoint &beamspot,
						   float lxyMin, float probMin, unsigned int nHitsBeforeVtxMax) {

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
