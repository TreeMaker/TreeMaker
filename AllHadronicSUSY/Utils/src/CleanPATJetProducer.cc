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

  using namespace edm;
  Handle< View< pat::Photon> > photonCands;
  iEvent.getByLabel( photonCollection ,photonCands);

  if( debug ) std::cout << "got photon collection" << std::endl;
  
  // get jet collection
  Handle< View<pat::Jet> > jetCands;
  iEvent.getByLabel(jetCollection,jetCands);

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  }

  // - - - - - - - - - - - - - - - - - - - - 
  // loop over jet collection and match jets
  // with the photons passed by user
  // - - - - - - - - - - - - - - - - - - - -   
  for(View<pat::Jet>::const_iterator iPart = jetCands->begin(); iPart != jetCands->end(); ++iPart){//loop over ak4Jets
    
    bool matchedToPhoton = false;

    for(View<pat::Photon>::const_iterator iPhot = photonCands->begin(); iPhot != photonCands->end(); ++iPhot){//loop over photons
      
      if( debug ) {
	std::cout << "input  p_{mu}: " 
		  << iPart->px() << " " 
		  << iPart->py() << " " 
		  << iPart->pz() << " " 
		  << iPart->energy() << std::endl;
      }// end debug

      double PhEta=iPhot->eta();  
      double PhPhi=iPhot->phi();
      
      double jetEta=iPart->eta();
      double jetPhi=iPart->phi();
      
      double dEta=PhEta-jetEta;
      double dPhi=PhPhi-jetPhi;
      if (fabs(PhPhi-jetPhi) > 3.14159){
	dPhi= 2*3.14159-(PhPhi-jetPhi );
      }

      double dR=sqrt((dEta*dEta)+(dPhi*dPhi)); 
      if(dR < 0.4 ) //deltaR cut photon and jet
	matchedToPhoton = true;

    }// end loop over photons
    
    if( ! matchedToPhoton ) patJet4Vec->push_back(*iPart);

  }// end loop over ak4Jets 
  
  iEvent.put(patJet4Vec ); 

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
