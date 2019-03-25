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
#include "DataFormats/Candidate/interface/Candidate.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <DataFormats/PatCandidates/interface/Photon.h>

#include <vector>

class GenParticlesProducer : public edm::global::EDProducer<> {

public:
    explicit GenParticlesProducer(const edm::ParameterSet&);
    ~GenParticlesProducer() override;

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
    //bool isAncestor(const reco::Candidate* ancestor, const reco::Candidate * particle) const;
    //void saveChain(int depth, int maxDepth, const reco::GenParticle&, std::unique_ptr<std::vector<TLorentzVector>>&,
    //               std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<int>>&,
    //               std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<int>>&,
    //               std::unordered_set<const reco::Candidate *>&) const;
    const reco::GenParticle* findLast(const reco::GenParticle& particle) const;
    void saveChain(int depth, int parentId, int parent_idx, const reco::GenParticle& particle, std::unique_ptr<std::vector<TLorentzVector>>& genParticle_vec,
                   std::unique_ptr<std::vector<int>>& PdgId_vec, std::unique_ptr<std::vector<int>>& Status_vec,
                   std::unique_ptr<std::vector<int>>& Parent_vec, std::unique_ptr<std::vector<int>>& ParentId_vec,
                   std::unordered_set<const reco::Candidate *>& stored_particles_ref) const;
    void storeMinimal(const edm::Handle< edm::View<reco::GenParticle> >&, std::unique_ptr<std::vector<TLorentzVector>>&,
                      std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<int>>&,
                      std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<int>>&) const;
    void storeStandard(const edm::Handle< edm::View<reco::GenParticle> >&, std::unique_ptr<std::vector<TLorentzVector>>&,
                      std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<int>>&,
                      std::unique_ptr<std::vector<int>>&, std::unique_ptr<std::vector<bool>>&) const;

    // ----------member data ---------------------------

    edm::InputTag genCollection;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> genCollectionTok;
    bool        debug;
    std::unordered_set<int> typicalChildIds, typicalParentIds, keepAllTheseIds;
    bool        keepFirstDecayProducts;
    bool        keepMinimal;

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

    const auto& ids = iConfig.getParameter<std::vector<int>>("keepIds");
    keepAllTheseIds.insert(ids.begin(),ids.end());

    keepFirstDecayProducts = iConfig.getParameter<bool>("keepFirst");

    keepMinimal = iConfig.getParameter<bool>("keepMinimal");

    produces< std::vector< TLorentzVector > >(""); 
    produces< std::vector< int > >("PdgId");
    produces< std::vector< int > >("Status");
    produces< std::vector< int > >("Parent");
    produces< std::vector< int > >("ParentId");
    produces< std::vector< bool > >("TTFlag");
}

GenParticlesProducer::~GenParticlesProducer() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called for each event  ------------
void GenParticlesProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
    using namespace edm;

    auto genParticle_vec = std::make_unique<std::vector<TLorentzVector>>();
    auto PdgId_vec = std::make_unique<std::vector<int>>();
    auto Status_vec = std::make_unique<std::vector<int>>();
    auto Parent_vec = std::make_unique<std::vector<int>>();
    auto ParentId_vec = std::make_unique<std::vector<int>>();
    auto TTFlag_vec = std::make_unique<std::vector<bool>>();

    edm::Handle< View<reco::GenParticle> > genPartCands;
    iEvent.getByToken(genCollectionTok, genPartCands);

    //Filter out unwanted gen particles and store 4-vector, pdgid, status, and parentID:
    if (debug) {
        edm::LogInfo("TreeMaker")<< "======new event============"<<"\n"
        <<"idx\t"<<"pdgId\t"<<"status\t"<<"parId\t"<<"parIdx\t";
    }

    if (keepMinimal) storeMinimal(genPartCands, genParticle_vec,PdgId_vec,Status_vec,Parent_vec,ParentId_vec);
    else             storeStandard(genPartCands,genParticle_vec,PdgId_vec,Status_vec,Parent_vec,ParentId_vec,TTFlag_vec);

    iEvent.put(std::move(genParticle_vec)); 
    iEvent.put(std::move(PdgId_vec      ), "PdgId");
    iEvent.put(std::move(Status_vec     ), "Status");
    iEvent.put(std::move(ParentId_vec   ), "ParentId");
    iEvent.put(std::move(Parent_vec     ), "Parent");
    iEvent.put(std::move(TTFlag_vec     ), "TTFlag");
}

// Based on http://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf
enum particle_type
{
    down=1,
    up=2,
    strange=3,
    charm=4,
    bottom=5,
    top=6,
    electron=11,
    electron_neutrino=12,
    muon=13,
    muon_neutrino=14,
    tau=15,
    tau_neutrino=16,
    photon=22,
    Z=23,
    W=24,
    Higgs=25
};

// Referenced:
//   https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017
//   https://github.com/cms-sw/cmssw/blob/master/DataFormats/HepMCCandidate/interface/GenParticle.h
//   https://github.com/cms-sw/cmssw/blob/master/DataFormats/Candidate/interface/CompositeRefCandidateT.h
//   https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCandidateModules#ParticleTreeDrawer_Utility
//   https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATMCMatchingExercise
const reco::GenParticle* GenParticlesProducer::findLast(const reco::GenParticle& particle) const {
    const reco::GenParticle* last = &particle;
    bool resetLast = false;
    const reco::GenParticle *daughter;
    if(debug) edm::LogInfo("TreeMaker") << "   Found a " << last->pdgId() << " (status=" << last->status() << ", ndaughters=" << last->numberOfDaughters() << "):";

    while (true) {
        resetLast=false;
        for(unsigned int iDau=0; iDau<last->numberOfDaughters(); iDau++) {
            daughter = static_cast<const reco::GenParticle *>(last->daughter(iDau));
            if(daughter->pdgId()==last->pdgId()) {
                last = daughter;
                resetLast = true;
                if(debug) edm::LogInfo("TreeMaker") << "      reset to " << last->pdgId() << "(status=" << last->status() << ")";
            }
        }
        if(!resetLast) break;
    }

    /*
    Empirical rules for particle status codes:
    ==========================================
    From a semi-leptonic TTJets sample:
    -----------------------------------
    1. tops start with status 22 and end with 62
        any time there is one daughter it is simply radiating. when there are two daughters that should be the final top
    2. b start with status 23 and end with 71/72 (ignore any gluon radiation)
    3. W start with status 22, can immediately decay or go to status 51/52
        immediately decays to status 23 which then decay to status 1/2 (leptonic) or 71 (hadronic)
    */
    if(((last->pdgId() >= down && last->pdgId() <= bottom) && (last->status()!=51 && last->status()!=52 && last->status()!=71 && last->status()!=72)) ||
       (last->pdgId() == top && last->status()!=62) ||
       (last->pdgId() == W && (last->status()!=22 && last->status()!=51 && last->status()!=52)) ||
       ((last->pdgId() >= electron && last->pdgId() <= tau_neutrino) && (last->status() != 1 && last->status() != 2))) {
        edm::LogInfo("TreeMaker") << "WARNING The last particle in the chain (" << last->pdgId() << ") does not have a status that corresponds to its type (status=" << last->status() << ")";
    }

    return last;
}

void GenParticlesProducer::saveChain(int depth, int parentId, int parent_idx, const reco::GenParticle& particle, std::unique_ptr<std::vector<TLorentzVector>>& genParticle_vec,
                                     std::unique_ptr<std::vector<int>>& PdgId_vec, std::unique_ptr<std::vector<int>>& Status_vec,
                                     std::unique_ptr<std::vector<int>>& Parent_vec, std::unique_ptr<std::vector<int>>& ParentId_vec,
                                     std::unordered_set<const reco::Candidate *>& stored_particles_ref) const {
    // Set a minimal depth of particles to save
    if(depth==0) return;
    auto lastParticle = findLast(particle);
    // Skip particles which are already in the list of stored particles
    if(stored_particles_ref.find(lastParticle)!=stored_particles_ref.end()) return;
    if(debug) edm::LogInfo("TreeMaker") << "   Saving chain for a " << particle.pdgId() << " (status=" << particle.status() << ")\n      Current depth is " << depth;

    // Save the gen particle information
    TLorentzVector temp;
    temp.SetPxPyPzE(lastParticle->px(), lastParticle->py(), lastParticle->pz(), lastParticle->energy());
    genParticle_vec->push_back(temp);
    PdgId_vec->push_back(lastParticle->pdgId());
    Status_vec->push_back(abs(lastParticle->status()));
    stored_particles_ref.insert(lastParticle);
    ParentId_vec->push_back(parentId);
    Parent_vec->push_back(parent_idx);
    int current_parent_idx = PdgId_vec->size()-1;
    int current_parent_id = PdgId_vec->back();

    // Save the daughters
    if(lastParticle->numberOfDaughters()==2) {
        int nextDepth = --depth;
        for(unsigned int iDau=0; iDau<lastParticle->numberOfDaughters(); iDau++) {
            if(abs(lastParticle->pdgId())<=bottom) continue;
            const reco::GenParticle *daughter = static_cast<const reco::GenParticle *>(lastParticle->daughter(iDau));
            saveChain(nextDepth, current_parent_id, current_parent_idx, *daughter, genParticle_vec, PdgId_vec, Status_vec, Parent_vec, ParentId_vec, stored_particles_ref);
        }
    }

    return;
}

void GenParticlesProducer::storeMinimal(const edm::Handle< edm::View<reco::GenParticle> >& genPartCands, std::unique_ptr<std::vector<TLorentzVector>>& genParticle_vec, 
                                        std::unique_ptr<std::vector<int>>& PdgId_vec, std::unique_ptr<std::vector<int>>& Status_vec, std::unique_ptr<std::vector<int>>& Parent_vec,
                                        std::unique_ptr<std::vector<int>>& ParentId_vec) const {
    std::unordered_set<const reco::Candidate *> stored_particles_ref;
    for(const auto& iPart : *genPartCands) {
        // Skip particles which are already in the list of stored particles
        // This is to protect against parts of a chain which may be saved, but here we are looking at the first copy
        if(stored_particles_ref.find(&iPart)!=stored_particles_ref.end()) continue;
        // Skip starting particles which are not from the hard process
        if(!iPart.isHardProcess() && !iPart.fromHardProcessBeforeFSR()) continue;
        // Only store particles in the list of acceptable parent pdgids
        if(typicalParentIds.find(abs(iPart.pdgId()))!=typicalParentIds.end()) {
            if (abs(iPart.pdgId())==top) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving a top chain ... ";
                saveChain(3, iPart.mother()->pdgId(), -1, iPart, genParticle_vec, PdgId_vec, Status_vec, Parent_vec, ParentId_vec, stored_particles_ref);
            }
            else if(abs(iPart.pdgId())>=photon && abs(iPart.pdgId())<=Higgs) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving a boson chain ... ";
                saveChain(2, iPart.mother()->pdgId(), -1, iPart, genParticle_vec, PdgId_vec, Status_vec, Parent_vec, ParentId_vec, stored_particles_ref);
            }
            else {
                if(debug) edm::LogInfo("TreeMaker") << "Saving an individual particle ... ";
                TLorentzVector temp;
                temp.SetPxPyPzE(iPart.px(), iPart.py(), iPart.pz(), iPart.energy());
                genParticle_vec->push_back(temp);
                PdgId_vec->push_back(iPart.pdgId());
                Status_vec->push_back(abs(iPart.status()));
                stored_particles_ref.insert(&iPart);
                ParentId_vec->push_back(iPart.mother()->pdgId());
                Parent_vec->push_back(-1);
            }
        }
    }
}

void GenParticlesProducer::storeStandard(const edm::Handle< edm::View<reco::GenParticle> >& genPartCands, std::unique_ptr<std::vector<TLorentzVector>>& genParticle_vec,
                                         std::unique_ptr<std::vector<int>>& PdgId_vec, std::unique_ptr<std::vector<int>>& Status_vec, std::unique_ptr<std::vector<int>>& Parent_vec,
                                         std::unique_ptr<std::vector<int>>& ParentId_vec, std::unique_ptr<std::vector<bool>>& TTFlag_vec) const {

    auto parents = std::make_unique<std::vector<TLorentzVector>>();

    for(const auto& iPart : *genPartCands) {

        bool keepAllThese = (keepAllTheseIds.find(abs(iPart.pdgId()))!=keepAllTheseIds.end());
        bool firstDecayProducts = false;
        if (keepFirstDecayProducts) firstDecayProducts = (abs(iPart.status())==23);

        bool typicalChild=(typicalChildIds.find(abs(iPart.pdgId()))!=typicalChildIds.end());
        bool typicalParent=(typicalParentIds.find(abs(iPart.pdgId()))!=typicalParentIds.end());
        if (!(typicalChild || typicalParent || keepAllThese || firstDecayProducts)) continue;

        int status = abs(iPart.status());
        bool acceptableParent = typicalParent && (iPart.isLastCopy() || status==21);
        //bool acceptableChild = typicalChild && (status==1 || status==2 || (status>20 && status<30));
        bool acceptableChild = typicalChild && iPart.isLastCopy();
        if (!(acceptableChild || acceptableParent || keepAllThese || firstDecayProducts)) continue;

        TLorentzVector temp;
        temp.SetPxPyPzE(iPart.px(), iPart.py(), iPart.pz(), iPart.energy());
        genParticle_vec->push_back(temp);
        PdgId_vec->push_back(iPart.pdgId());
        Status_vec->push_back(status);
        TTFlag_vec->push_back(!(acceptableChild || acceptableParent) && (keepAllThese || firstDecayProducts));
        TLorentzVector parent; parent.SetPxPyPzE(0,0,0,0);
        int parentid = 0;
        const reco::GenParticle *Parent;
        Parent = static_cast<const reco::GenParticle *>(iPart.mother());
        while (true) {
            if (!(Parent)) break;
            if (debug) {
                if (abs(PdgId_vec->back())==24) {
                    edm::LogInfo("TreeMaker") << "W parent Id, status ="<< Parent->pdgId()<<", "<<Parent->status()<<",px="<<Parent->px()<<",py="<<Parent->py()<<",phi="<<Parent->phi();
                }
            }
            if (Parent->isLastCopy() || Parent->status()==21) {
                parentid = Parent->pdgId();
                parent.SetPxPyPzE(Parent->px(), Parent->py(), Parent->pz(), Parent->energy());
                if (debug) {
                    if (abs(PdgId_vec->back())==24) {
                        edm::LogInfo("TreeMaker") << "planning to keep this mother";
                    }
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
    for (unsigned int g = 0; g < genParticle_vec->size(); g++) {
        itlv = std::find(genParticle_vec->begin(), genParticle_vec->end(), parents->at(g));
        auto index = std::distance(genParticle_vec->begin(), itlv);
        int parentIndex = index;
        if (itlv == genParticle_vec->end()) parentIndex = -1;
        Parent_vec->push_back(parentIndex);
        if (debug) {
          edm::LogInfo("TreeMaker")<<g<<"\t"<<PdgId_vec->at(g)<<"\t"<<Status_vec->at(g)<<"\t"<<ParentId_vec->at(g)<<"\t"<<Parent_vec->at(g)<<"\n" //<<", eta="<<  parents->at(g).Eta() <<"phi="<< parents->at(g).Phi() <<"\n"
          << "eta="<< parents->at(g).Eta();
        }
    }
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void GenParticlesProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  /*
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  */
}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(GenParticlesProducer);
