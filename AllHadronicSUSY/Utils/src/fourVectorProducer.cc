// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      fourVectorProducer
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

#include "AllHadronicSUSY/Utils/interface/fourVectorProducer.h"

#include "TLorentzVector.h"

#include <vector>

fourVectorProducer::fourVectorProducer(const edm::ParameterSet& iConfig):
  particleCollection(iConfig.getUntrackedParameter<edm::InputTag>("particleCollection")),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< std::vector< TLorentzVector > >(""); 
}


fourVectorProducer::~fourVectorProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
fourVectorProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  // get jet collection
  Handle< View<reco::Candidate> > partCands;
  iEvent.getByLabel(particleCollection,partCands);

  std::auto_ptr< std::vector< TLorentzVector > > part4Vec ( new std::vector< TLorentzVector > () );

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  }

  for(View<reco::Candidate>::const_iterator iPart = partCands->begin(); iPart != partCands->end(); ++iPart){
      
    if( debug ) {
	       std::cout << "input  p_{mu}: " 
		      << iPart->px() << " " 
		      << iPart->py() << " " 
		      << iPart->pz() << " " 
		      << iPart->energy() << std::endl;
    }// end debug
     
    TLorentzVector p4( iPart->px(), 
		       iPart->py(), 
		       iPart->pz(), 
		       iPart->energy() 
		       ) ;
    
    part4Vec->push_back( p4 ) ; 

  }// end loop over particles

  iEvent.put(part4Vec); 
 
}


// ------------ method called once each job just before starting event loop  ------------
void 

fourVectorProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
fourVectorProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
fourVectorProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
fourVectorProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
fourVectorProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
fourVectorProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
fourVectorProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(fourVectorProducer);
