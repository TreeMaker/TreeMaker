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
  produces< std::vector< TLorentzVector > >(""); 
  produces< std::vector< double > >("isEB").setBranchAlias( photonCollection.label()+"isEB" );; 
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

  std::auto_ptr< std::vector< TLorentzVector > > photon ( new std::vector< TLorentzVector > () );
  
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

  effArea* effAreas = new effArea();
  effAreas->addEffA( 0.0,   1.0,   0.012, 0.030, 0.148 );
  effAreas->addEffA( 1.0,   1.479, 0.010, 0.057, 0.130 );
  effAreas->addEffA( 1.479, 2.0,   0.014, 0.039, 0.112 );
  effAreas->addEffA( 2.0,   2.2,   0.012, 0.015, 0.216 );
  effAreas->addEffA( 2.2,   2.3,   0.016, 0.024, 0.262 );
  effAreas->addEffA( 2.3,   2.4,   0.020, 0.039, 0.260 );
  effAreas->addEffA( 2.4,   99.,   0.012, 0.072, 0.266 );

  for( View< pat::Photon >::const_iterator iPhoton = photonCands->begin();
        iPhoton != photonCands->end();
        ++iPhoton){

    if( debug ) {
      std::cout << "photon pt: " << iPhoton->pt() << std::endl;
      std::cout << "photon eta: " << iPhoton->eta() << std::endl;
      std::cout << "photon phi: " << iPhoton->phi() << std::endl;
    }

    TLorentzVector temp;
    temp.SetPtEtaPhiE(iPhoton->pt(),
		      iPhoton->eta(),
		      iPhoton->phi(),
		      iPhoton->energy());
    photon->push_back( temp );

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

  }

  iEvent.put(photon); 
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
