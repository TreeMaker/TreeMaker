// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      PhotonIDisoProducer
// 
/*

 Description: Takes as cfg input a jet collection 
 and clusters the jets into large-R anti-kt jets.
 A collection of 4-vectors corresponding to these 
 jets is saved to the event.

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

#include "..//interface/PhotonIDisoProducer.h"
#include "effArea.cc"

#include "TLorentzVector.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <vector>

PhotonIDisoProducer::PhotonIDisoProducer(const edm::ParameterSet& iConfig):
  photonCollection(iConfig.getUntrackedParameter<edm::InputTag>("photonCollection")),
  rhoCollection(iConfig.getUntrackedParameter<edm::InputTag>("rhoCollection")),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< std::vector< pat::Photon > >(""); 
  produces< std::vector< pat::Photon > >("bestPhoton"); 
  produces< int >("NumPhotons");
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
}


PhotonIDisoProducer::~PhotonIDisoProducer()
{
 
   // do anything here that needs to be done at desctruction time
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

  std::auto_ptr< std::vector< pat::Photon > > photons ( new std::vector< pat::Photon >() );
  std::auto_ptr< std::vector< pat::Photon > > bestPhoton ( new std::vector< pat::Photon >() );

  std::auto_ptr< int > NumPhotons ( new int(0) );

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

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  
  }
  
  Handle< View< pat::Photon> > photonCands;
  iEvent.getByLabel( photonCollection ,photonCands);

  edm::Handle< double > rho_;
  iEvent.getByLabel(rhoCollection,rho_);
  double rho = *rho_;

  if( debug ) std::cout << "got photon collection" << std::endl;


  // - - - - - - - - - - - - - - - - - - - - 
  // Initializing effective area to be used 
  // for rho corrections to the photon isolation
  // variables.  -- currently these are taken from
  // the 2012 EGamma PAG recommendations and need 
  // to be updated
  // - - - - - - - - - - - - - - - - - - - - 
  effArea* effAreas = new effArea();
  effAreas->addEffA( 0.0, 1.0, 0.0234, 0.0053, 0.078 );
  effAreas->addEffA( 1.0, 1.479, 0.0189, 0.0130, 0.0629 );
  effAreas->addEffA( 1.479, 2.0, 0.0171, 0.0057, 0.0264 );
  effAreas->addEffA( 2.0, 2.2, 0.0129, 0.0070, 0.0462 );
  effAreas->addEffA( 2.2, 2.3, 0.0110, 0.0152, 0.0740 );
  effAreas->addEffA( 2.3, 2.4, 0.0074, 0.0232, 0.0924 );
  effAreas->addEffA( 2.4, 99., 0.0035, 0.1709, 0.1484 );

  double bestPhotonPt = 0. ; 
    
  for( View< pat::Photon >::const_iterator iPhoton = photonCands->begin();
        iPhoton != photonCands->end();
        ++iPhoton){

    if( debug ) {
      std::cout << "photon pt: " << iPhoton->pt() << std::endl;
      std::cout << "photon eta: " << iPhoton->eta() << std::endl;
      std::cout << "photon phi: " << iPhoton->phi() << std::endl;
    }

    photon_isEB->push_back( iPhoton->isEB() );
    photon_genMatched->push_back( iPhoton->genPhoton() != NULL );
    photon_hadTowOverEM->push_back( iPhoton->hadTowOverEm() ) ;
    photon_sigmaIetaIeta->push_back( iPhoton->sigmaIetaIeta() ) ;
    
    photon_pfChargedIso->push_back(      iPhoton->chargedHadronIso() );
    photon_pfGammaIso->push_back(        iPhoton->photonIso() );
    photon_pfNeutralIso->push_back(      iPhoton->neutralHadronIso() );

    double chIso = effAreas->rhoCorrectedIso(  pfCh  , iPhoton->chargedHadronIso() , iPhoton->eta() , rho ); 
    double nuIso = effAreas->rhoCorrectedIso(  pfNu  , iPhoton->neutralHadronIso() , iPhoton->eta() , rho ); 
    double gamIso = effAreas->rhoCorrectedIso( pfGam , iPhoton->photonIso()        , iPhoton->eta() , rho ); 

    photon_pfChargedIsoRhoCorr->push_back( chIso  );
    photon_pfGammaIsoRhoCorr->push_back(   nuIso  );
    photon_pfNeutralIsoRhoCorr->push_back( gamIso );

    photon_hasPixelSeed->push_back( iPhoton->hasPixelSeed() );

    // apply photon selection -- all good photons and the leading pt photon will be saved
    bool isBarrelPhoton=false;
    bool isEndcapPhoton=false;
    bool passID=false;
    bool passIso=false;
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
  
      if(iPhoton->hadTowOverEm() < 0.028 && iPhoton->hasPixelSeed()==false && iPhoton->sigmaIetaIeta() < 0.0107){//id criterias barrel
	passID=true;

      }//id criterias

    } 
    else if(isEndcapPhoton){
      if(iPhoton->hadTowOverEm() < 0.093 && iPhoton->hasPixelSeed()==false && iPhoton->sigmaIetaIeta() < 0.0272){//id criteria endcap
	passID=true;

      }//id criterias endcap

    }
    else {
      passID=false;
    }
 
    // apply isolation cuts
    if(isBarrelPhoton){
      if(chIso <2.67 && nuIso <  (7.23 + TMath::Exp(0.0028*(iPhoton->pt()+0.5408)))  && gamIso < ( 2.11 + 0.0014*(iPhoton->pt())) ){
	passIso=true;      
      }
     
    }
    else if(isEndcapPhoton){
      if(chIso <1.79 && nuIso <  (8.89 + 0.01725*(iPhoton->pt()))  && gamIso < ( 3.09 + 0.0091*(iPhoton->pt())) ){
	passIso=true;
      }

    }
    else{
      passIso=false;
    }

    // check if photons is a good photon
    if( passAcc && passID && passIso && iPhoton->pt() > 100.0){//pure photons
      (*NumPhotons)++;
      photons->push_back( *iPhoton );
      // make sure only the highest pt photon is used
      if(iPhoton->pt() > bestPhotonPt){ 

	bestPhoton->clear();
	bestPhoton->push_back( *iPhoton );
	bestPhotonPt=iPhoton->pt();

      }// done with best photon
    
    }//pure photons    

  }// end loop over candidate photons

  iEvent.put(photons); 
  iEvent.put(bestPhoton, "bestPhoton" ); 
  iEvent.put(NumPhotons, "NumPhotons" ); 
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
