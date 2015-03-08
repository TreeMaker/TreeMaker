// -*- C++ -*-
//
// Package:    AllHadronicSUSY/Utils
// Class:      CleanPATJetProducer
// 
/*

 Description: Takes photons and jet collections
 from cfg and removes all jets which match photon
 (currently matching is done with dR<0.4 criteria) 
 A collection of pat::Jet is saved to the event.

*/
//
// Original Author: Bibhuprasad Mahakud 
//         Created: 5th March 2015
// 
// 

// system include files
#include <memory>
#include <DataFormats/PatCandidates/interface/Jet.h>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "AllHadronicSUSY/Utils/interface/CleanPATJetProducer.h"
#include "AllHadronicSUSY/Utils/src/effArea.cc"
#include "TLorentzVector.h"

#include <vector>

CleanPATJetProducer::CleanPATJetProducer(const edm::ParameterSet& iConfig):
  jetCollection(iConfig.getUntrackedParameter<std::string>("jetCollection")),
  photonCollection(iConfig.getUntrackedParameter<edm::InputTag>("photonCollection")),
  rhoCollection(iConfig.getUntrackedParameter<edm::InputTag>("rhoCollection")),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< std::vector< pat::Jet > >("");
}


CleanPATJetProducer::~CleanPATJetProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
CleanPATJetProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  //initialize 'collection' to be saved in event
  std::auto_ptr< std::vector< pat::Jet > >  patJet4Vec( new std::vector< pat::Jet > () );
  vector< TLorentzVector > *purePhoton = 0;

  using namespace edm;
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
  effAreas->addEffA( 0.0,   1.0,   0.012, 0.030, 0.148 );
  effAreas->addEffA( 1.0,   1.479, 0.010, 0.057, 0.130 );
  effAreas->addEffA( 1.479, 2.0,   0.014, 0.039, 0.112 );
  effAreas->addEffA( 2.0,   2.2,   0.012, 0.015, 0.216 );
  effAreas->addEffA( 2.2,   2.3,   0.016, 0.024, 0.262 );
  effAreas->addEffA( 2.3,   2.4,   0.020, 0.039, 0.260 );
  effAreas->addEffA( 2.4,   99.,   0.012, 0.072, 0.266 );
  double PhotonPt=0;
  
  // - - - - - - - - - - - - - - - - - - - - 
  // loop over all photons to find the best photon
  // 'pure' photon.  This is defined to be the 
  // highest pt photon that passes all the iso
  // and id cuts.  
  // - - - - - - - - - - - - - - - - - - - - 
  for( View< pat::Photon >::const_iterator iPhoton = photonCands->begin();
       iPhoton != photonCands->end();
       ++iPhoton){//photon loop starts
 
    isBarrelPhoton=false;
    isEndcapPhoton=false;
    isGenMatched=false;
    passID=false;
    passIso=false;
    passAcc=false;

 
 
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
  
    // bool genPhoton,isgenMatched;
    isGenMatched=iPhoton->genPhoton() != NULL;
  
    // apply id cuts
    if(isBarrelPhoton){
  
      if(iPhoton->hadTowOverEm() < 0.05 && iPhoton->hasPixelSeed()==false && iPhoton->sigmaIetaIeta() < 0.011){//id criterias barrel
	passID=true;

      }//id criterias

    } 
    else if(isEndcapPhoton){
      if(iPhoton->hadTowOverEm() < 0.05 && iPhoton->hasPixelSeed()==false && iPhoton->sigmaIetaIeta() < 0.031){//id criteria endcap
	passID=true;

      }//id criterias endcap

    }
    else {
      passID=false;
    }
 
    // compute the rho corrected isolation variable using
    // the effective areas defined above
    chIso = effAreas->rhoCorrectedIso(  pfCh  , iPhoton->chargedHadronIso() , iPhoton->eta() , rho );
    nuIso = effAreas->rhoCorrectedIso(  pfNu  , iPhoton->neutralHadronIso() , iPhoton->eta() , rho );
    gamIso = effAreas->rhoCorrectedIso( pfGam , iPhoton->photonIso()        , iPhoton->eta() , rho );
   
    // apply isolation cuts
    if(isBarrelPhoton){
      if(chIso <0.7 && nuIso <  (0.4 + 0.04*(iPhoton->pt()))  && gamIso < ( 0.5 + 0.005*(iPhoton->pt())) ){
	passIso=true;      
      }
     
    }
    else if(isEndcapPhoton){
      if(chIso <0.5 && nuIso <  (1.5 + 0.04*(iPhoton->pt()))  && gamIso < ( 1.0 + 0.005*(iPhoton->pt())) ){
	passIso=true;
      }

    }
    else{
      passIso=false;
    }

    // check if photons is a good photon
    if( passAcc && passID && passIso && iPhoton->pt() > 100.0){//pure photons
      // make sure only the highest pt photon is used
      if(iPhoton->pt() > PhotonPt){ 
	purePhoton->clear();
	TLorentzVector temp;
	temp.SetPtEtaPhiE(iPhoton->pt(),
			  iPhoton->eta(),
			  iPhoton->phi(),
			  iPhoton->energy());
	purePhoton->push_back( temp );
	PhotonPt=iPhoton->pt();

      }
    
    }//pure photons    

  }//photon loop

  if( debug ) cout<<"number of photons = "<<purePhoton->size()<<endl;
  
  // get jet collection
  Handle< View<pat::Jet> > jetCands;
  iEvent.getByLabel(jetCollection,jetCands);

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  }

  // - - - - - - - - - - - - - - - - - - - - 
  // loop over jet collection and match jets
  // with the 'pure' photon selected above
  // - - - - - - - - - - - - - - - - - - - -   
  for(View<pat::Jet>::const_iterator iPart = jetCands->begin(); iPart != jetCands->end(); ++iPart){//loop over ak4Jets
      
    if( debug ) {
      std::cout << "input  p_{mu}: " 
		<< iPart->px() << " " 
		<< iPart->py() << " " 
		<< iPart->pz() << " " 
		<< iPart->energy() << std::endl;
    }// end debug

    if(purePhoton->size()==1){
      double PhEta=purePhoton->at(0).Eta();  
      double PhPhi=purePhoton->at(0).Phi();
  
      double jetEta=iPart->eta();
      double jetPhi=iPart->phi();

      double dEta=PhEta-jetEta;
      double dPhi=PhPhi-jetPhi;
      if (fabs(PhPhi-jetPhi) > 3.14159){
	dPhi= 2*3.14159-(PhPhi-jetPhi );
      }

      double dR=sqrt((dEta*dEta)+(dPhi*dPhi)); 
      if(dR > 0.4 ){//deltaR cut photon and jet

        patJet4Vec->push_back(*iPart);

      }//photon and jet

    }else if(purePhoton->size()==0){

      patJet4Vec->push_back(*iPart);

    }

  }// end loop over ak4Jets 

 
  iEvent.put(patJet4Vec); 
}


// ------------ method called once each job just before starting event loop  ------------
void 

CleanPATJetProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CleanPATJetProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
CleanPATJetProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
CleanPATJetProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
CleanPATJetProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
CleanPATJetProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CleanPATJetProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(CleanPATJetProducer);
