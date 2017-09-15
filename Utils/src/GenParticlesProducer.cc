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
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TLorentzVector.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <DataFormats/PatCandidates/interface/Photon.h>

#include <vector>

class GenParticlesProducer : public edm::global::EDProducer<> {

public:
  explicit GenParticlesProducer(const edm::ParameterSet&);
  ~GenParticlesProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

  // ----------member data ---------------------------

  edm::InputTag genCollection;
  edm::EDGetTokenT<edm::View<reco::GenParticle>> genCollectionTok;
  bool        debug;
  std::unordered_set<int> typicalChildIds, typicalParentIds;

};


GenParticlesProducer::GenParticlesProducer(const edm::ParameterSet& iConfig):
  genCollection(iConfig.getParameter<edm::InputTag>("genCollection")),
  genCollectionTok(consumes<edm::View<reco::GenParticle>>(genCollection)),
  debug(iConfig.getParameter<bool>("debug"))
{
  const auto& cids = iConfig.getParameter<std::vector<int>>("childIds");
  typicalChildIds.insert(cids.begin(),cids.end());

  const auto& pids = iConfig.getParameter<std::vector<int>>("parentIds");
  typicalParentIds.insert(pids.begin(),pids.end());

  produces< std::vector< TLorentzVector > >(""); 
  produces< std::vector< int > >("PdgId");
  produces< std::vector< int > >("Status");
  produces< std::vector< int > >("Parent");
  produces< std::vector< int > >("ParentId");
  
}

GenParticlesProducer::~GenParticlesProducer()
{
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenParticlesProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{

  using namespace edm;

  auto genParticle_vec = std::make_unique<std::vector<TLorentzVector>>();
  auto PdgId_vec = std::make_unique<std::vector<int>>();
  auto Status_vec = std::make_unique<std::vector<int>>();
  auto Parent_vec = std::make_unique<std::vector<int>>();
  auto ParentId_vec = std::make_unique<std::vector<int>>();
  auto parents = std::make_unique<std::vector<TLorentzVector>>();

  edm::Handle< View<reco::GenParticle> > genPartCands;
  iEvent.getByToken(genCollectionTok, genPartCands);

  //Filter out unwanted gen particles and store 4-vector, pdgid, status, and parentID:
  if( debug ){
    edm::LogInfo("TreeMaker")<< "======new event============"<<"\n"
      <<"idx\t"<<"pdgId\t"<<"status\t"<<"parId\t"<<"parIdx\t";
  }
  for(View<reco::GenParticle>::const_iterator iPart = genPartCands->begin(); iPart != genPartCands->end(); ++iPart)
    {
      bool typicalChild=(typicalChildIds.find(abs(iPart->pdgId()))!=typicalChildIds.end());
      bool typicalParent=(typicalParentIds.find(abs(iPart->pdgId()))!=typicalParentIds.end());
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
              edm::LogInfo("TreeMaker") << "W parent Id, status ="<< Parent->pdgId()<<", "<<Parent->status()<<",px="<<Parent->px()<<",py="<<Parent->py()<<",phi="<<Parent->phi();
          }
          if(Parent->isLastCopy() || Parent->status()==21)
            {
              parentid = Parent->pdgId();
              parent.SetPxPyPzE(Parent->px(), Parent->py(), Parent->pz(), Parent->energy());
              if( debug ){
                if(abs(PdgId_vec->back())==24) edm::LogInfo("TreeMaker") << "planning to keep this mother";
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
        edm::LogInfo("TreeMaker")<<g<<"\t"<<PdgId_vec->at(g)<<"\t"<<Status_vec->at(g)<<"\t"<<ParentId_vec->at(g)<<"\t"<<Parent_vec->at(g)<<"\n" //<<", eta="<<  parents->at(g).Eta() <<"phi="<< parents->at(g).Phi() <<"\n"
          << "eta="<< parents->at(g).Eta();
      }
    }

  iEvent.put(std::move(genParticle_vec)); 
  iEvent.put(std::move(PdgId_vec  ), "PdgId" );
  iEvent.put(std::move(Status_vec ), "Status" );
  iEvent.put(std::move(ParentId_vec ), "ParentId" );
  iEvent.put(std::move(Parent_vec ), "Parent" );
 
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
