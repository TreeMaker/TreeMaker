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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "AllHadronicSUSY/Utils/interface/genParticlesProducer.h"

#include "TLorentzVector.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

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

  std::vector<int> pdgIdOfInterest;
  pdgIdOfInterest.push_back(21);
  pdgIdOfInterest.push_back(22);
  pdgIdOfInterest.push_back(23);
  pdgIdOfInterest.push_back(24);
  pdgIdOfInterest.push_back(25);

  pdgIdOfInterest.push_back(1);
  pdgIdOfInterest.push_back(2);
  pdgIdOfInterest.push_back(3);
  pdgIdOfInterest.push_back(4);
  pdgIdOfInterest.push_back(5);
  pdgIdOfInterest.push_back(6);

  pdgIdOfInterest.push_back(11);
  pdgIdOfInterest.push_back(12);
  pdgIdOfInterest.push_back(13);
  pdgIdOfInterest.push_back(14);
  pdgIdOfInterest.push_back(15);
  pdgIdOfInterest.push_back(16);

  pdgIdOfInterest.push_back(1000021);
  pdgIdOfInterest.push_back(1000022);
  pdgIdOfInterest.push_back(1000023);
  pdgIdOfInterest.push_back(1000025);
  pdgIdOfInterest.push_back(1000035);

  pdgIdOfInterest.push_back(1000001);
  pdgIdOfInterest.push_back(1000002);
  pdgIdOfInterest.push_back(1000003);
  pdgIdOfInterest.push_back(1000004);
  pdgIdOfInterest.push_back(1000005);
  pdgIdOfInterest.push_back(1000006);

  pdgIdOfInterest.push_back(2000001);
  pdgIdOfInterest.push_back(2000002);
  pdgIdOfInterest.push_back(2000003);
  pdgIdOfInterest.push_back(2000004);
  pdgIdOfInterest.push_back(2000005);
  pdgIdOfInterest.push_back(2000006);

  edm::Handle< View<reco::Candidate> > genPartCands;
  iEvent.getByLabel( "prunedGenParticles" ,genPartCands);
  
  for(View<reco::Candidate>::const_iterator iPart = genPartCands->begin();
      iPart != genPartCands->end();
      ++iPart){
    
    if( std::find( pdgIdOfInterest.begin(), pdgIdOfInterest.end(), abs(iPart->pdgId()) ) != pdgIdOfInterest.end() && abs( iPart->status() ) >20 && abs( iPart->status() ) <30 ){
      
      TLorentzVector temp;
      temp.SetPtEtaPhiE( iPart->pt() ,
			 iPart->eta() ,
			 iPart->phi() ,
			 iPart->energy() 
			 );

      genParticle->push_back( temp );     
      PDGid->push_back( iPart->pdgId() );

      int parentIndex = 0;

      for(View<reco::Candidate>::const_iterator jPart = genPartCands->begin();
	  jPart != genPartCands->end();
	  ++jPart){

	if( pow( pow( iPart->phi() - jPart->phi() , 2 ) + pow( iPart->eta() - jPart->eta() , 2 ) , .5 ) < 0.01 ) 
	  break;
	
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
