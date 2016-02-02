// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      genParticlesProducer
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
#include <iostream>
#include <unordered_set>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TreeMaker/Utils/interface/genParticlesProducer.h"

#include "TLorentzVector.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>

#include <vector>

genParticlesProducer::genParticlesProducer(const edm::ParameterSet& iConfig):
  genCollection(iConfig.getUntrackedParameter<edm::InputTag>("genCollection")),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< std::vector< TLorentzVector > >(""); 
  produces< std::vector< int > >("PDGid");
  produces< std::vector< int > >("parent");
  
}


genParticlesProducer::~genParticlesProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
genParticlesProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;

  std::auto_ptr< std::vector< TLorentzVector > > genParticle( new std::vector< TLorentzVector > () );
  
  std::auto_ptr< std::vector< int > > PDGid( new std::vector< int > () );
  std::auto_ptr< std::vector< int > > parent( new std::vector< int > () );

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;  
  }

  std::unordered_set<int> pdgIdOfInterest(
    {21,22,23,24,25,
     1,2,3,4,5,6,
     11,12,13,14,15,16,
     1000021,1000022,1000023,1000025,1000035,
     1000001,1000002,1000003,1000004,1000005,1000006,
     2000001,2000002,2000003,2000004,2000005,2000006}
  );
  
  std::unordered_set<int> pdgIdLastCopy(
    {1000021,
     1000001,1000002,1000003,1000004,1000005,1000006,
     2000001,2000002,2000003,2000004}
  );

  edm::Handle< View<reco::GenParticle> > genPartCands;
  iEvent.getByLabel( "prunedGenParticles" ,genPartCands);
  
  for(View<reco::GenParticle>::const_iterator iPart = genPartCands->begin(); iPart != genPartCands->end(); ++iPart){
    if ( std::find( pdgIdOfInterest.begin(), pdgIdOfInterest.end(), abs(iPart->pdgId()) ) == pdgIdOfInterest.end() ) continue;
    
    bool checkLastCopy = ( std::find( pdgIdLastCopy.begin(), pdgIdLastCopy.end(), abs(iPart->pdgId()) ) != pdgIdLastCopy.end() );
    if( ( checkLastCopy && iPart->isLastCopy() ) 
        || ( !checkLastCopy && abs( iPart->status() ) > 20 && abs( iPart->status() ) < 30 ) )
    {
      TLorentzVector temp;
      temp.SetPtEtaPhiE( iPart->pt() ,
                         iPart->eta() ,
                         iPart->phi() ,
                         iPart->energy() 
                         );

      genParticle->push_back( temp );     
      PDGid->push_back( iPart->pdgId() );

      int parentIndex = 0;

      for(View<reco::GenParticle>::const_iterator jPart = genPartCands->begin(); jPart != genPartCands->end(); ++jPart){
        if( pow( pow( iPart->phi() - jPart->phi() , 2 ) + pow( iPart->eta() - jPart->eta() , 2 ) , .5 ) < 0.01 ) break;
        
        parentIndex++;
      }
      
      parent->push_back( parentIndex );

    }
  }// end of loop over gen-particles

  iEvent.put(genParticle); 
  iEvent.put(PDGid , "PDGid" );
  iEvent.put(parent , "parent" );
 
}


// ------------ method called once each job just before starting event loop  ------------
void 

genParticlesProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
genParticlesProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
genParticlesProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
genParticlesProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
genParticlesProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
genParticlesProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
genParticlesProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(genParticlesProducer);
