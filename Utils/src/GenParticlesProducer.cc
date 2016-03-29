// -*- C++ -*-
// Package:    TreeMaker
// Class:      GenParticlesProducer
// Authors:  Andrew Whitbeck, Sam Bein 
//         Created:  Wed March 7, 2014
//         Modified: Thurs March 3, 2016

#include <memory>
#include <iostream>
#include <unordered_set>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TreeMaker/Utils/interface/GenParticlesProducer.h"
#include "TLorentzVector.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <vector>


GenParticlesProducer::GenParticlesProducer(const edm::ParameterSet& iConfig):
  genCollection(iConfig.getUntrackedParameter<edm::InputTag>("genCollection")),
  genCollectionTok(consumes<edm::View<reco::GenParticle>>(genCollection)),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< std::vector< TLorentzVector > >(""); 
  produces< std::vector< int > >("PdgId");
  produces< std::vector< int > >("Status");
  produces< std::vector< int > >("Parent");
  produces< std::vector< int > >("ParentId");
  
}

GenParticlesProducer::~GenParticlesProducer()
{
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenParticlesProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;

  std::auto_ptr< std::vector< TLorentzVector > > genParticle_vec( new std::vector< TLorentzVector > () );
  std::auto_ptr< std::vector< int > > PdgId_vec( new std::vector< int > () );
  std::auto_ptr< std::vector< int > > Status_vec( new std::vector< int > () );
  std::auto_ptr< std::vector< int > > Parent_vec( new std::vector< int > () );
  std::auto_ptr< std::vector< int > > ParentId_vec( new std::vector< int > () );
  std::auto_ptr< std::vector< TLorentzVector > > parents( new std::vector< TLorentzVector > () );//not stored

  std::unordered_set<int> typicalChildIds({1,2,3,4,5,11,12,13,14,15,16,22});
  std::unordered_set<int> typicalParentIds(
                                           {1,2,1000021,1000022,1000023,1000024,1000025,1000035,1000037,1000039,
                                            1000001,1000002,1000003,1000004,1000005,1000006,
                                            2000001,2000002,2000003,2000004,2000005,2000006,
                                            6, 23, 24, 25}
                                        );
  
  edm::Handle< View<reco::GenParticle> > genPartCands;
  iEvent.getByToken(genCollectionTok, genPartCands);

  //Filter out unwanted gen particles and store 4-vector, pdgid, status, and parentID:
  if( debug ){
    std::cout<< "======new event============"<<std::endl;
    std::cout<<"idx\t"<<"pdgId\t"<<"status\t"<<"parId\t"<<"parIdx\t"<<std::endl;
  }
  for(View<reco::GenParticle>::const_iterator iPart = genPartCands->begin(); iPart != genPartCands->end(); ++iPart)
    {
      bool typicalChild=!(std::find(typicalChildIds.begin(),typicalChildIds.end(),abs(iPart->pdgId()))==typicalChildIds.end());
      bool typicalParent=!(std::find(typicalParentIds.begin(),typicalParentIds.end(),abs(iPart->pdgId()))==typicalParentIds.end());
      if (!(typicalChild || typicalParent)) continue;

      int status = abs(iPart->status());
      bool acceptableParent = typicalParent && (iPart->isLastCopy() || status==21);
      //bool acceptableChild = typicalChild && (status==1 || status==2 || (status>20 && status<30));
      bool acceptableChild = typicalChild && iPart->isLastCopy();
      if (!(acceptableChild || acceptableParent)) continue;

      TLorentzVector temp;
      temp.SetPxPyPzE(iPart->px(), iPart->py(), iPart->pz(), iPart->energy());
      genParticle_vec->push_back(temp);
      PdgId_vec->push_back(iPart->pdgId());
      Status_vec->push_back(status);
      TLorentzVector parent; parent.SetPxPyPzE(0,0,0,0);
      int parentid = 0;
      const reco::GenParticle *Parent;
      Parent = static_cast<const reco::GenParticle *>(iPart->mother());
      while(true)
        {
          if(!(Parent)) break;
          if( debug ){
            if(abs(PdgId_vec->back())==24) 
              std::cout << "W parent Id, status ="<< Parent->pdgId()<<", "<<Parent->status()<<",px="<<Parent->px()<<",py="<<Parent->py()<<",phi="<<Parent->phi()<<std::endl;
          }
          if(Parent->isLastCopy() || Parent->status()==21)
            {
              parentid = Parent->pdgId();
              parent.SetPxPyPzE(Parent->px(), Parent->py(), Parent->pz(), Parent->energy());
              if( debug ){
                if(abs(PdgId_vec->back())==24) std:: cout << "planning to keep this mother"<<std::endl;
              }
              break;
            }
          Parent = static_cast<const reco::GenParticle *>(Parent->mother());
        }
      parents->push_back(parent);
      ParentId_vec->push_back(parentid);

    }

  //Identify each gp's parent within the vector of stored gp's and store parentIdx:
  std::vector<TLorentzVector>::iterator itlv;
  for (unsigned int g = 0; g < genParticle_vec->size(); g++)
    {
      itlv = std::find(genParticle_vec->begin(), genParticle_vec->end(), parents->at(g));
      auto index = std::distance(genParticle_vec->begin(), itlv);
      int parentIndex = index;
      if (itlv == genParticle_vec->end()) parentIndex = -1;
      Parent_vec->push_back(parentIndex);
      if( debug ){
        std::cout<<g<<"\t"<<PdgId_vec->at(g)<<"\t"<<Status_vec->at(g)<<"\t"<<ParentId_vec->at(g)<<"\t"<<Parent_vec->at(g)<<std::endl;//", eta="<<  parents->at(g).Eta() <<"phi="<< parents->at(g).Phi() <<std::endl;
        std::cout<< "eta="<< parents->at(g).Eta() << std::endl;
      }
    }

  iEvent.put(genParticle_vec); 
  iEvent.put(PdgId_vec  , "PdgId" );
  iEvent.put(Status_vec , "Status" );
  iEvent.put(ParentId_vec , "ParentId" );
  iEvent.put(Parent_vec , "Parent" );
 
}


// ------------ method called once each job just before starting event loop  ------------
void 

GenParticlesProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenParticlesProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
GenParticlesProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GenParticlesProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GenParticlesProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GenParticlesProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenParticlesProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(GenParticlesProducer);
