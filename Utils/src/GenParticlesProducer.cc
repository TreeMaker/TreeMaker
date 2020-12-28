// -*- C++ -*-
// Package:    TreeMaker
// Class:      GenParticlesProducer
// Authors:  Andrew Whitbeck, Sam Bein 
//         Created:  Wed March 7, 2014
//         Modified: Thurs March 3, 2016

#include <algorithm>
#include <memory>
#include <numeric>
#include <iostream>
#include <unordered_set>
#include <vector>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/Point3D.h"

//
// class declarations
//
class GenPartInfos {
public:
    GenPartInfos() {
        genParticle_vec = std::make_unique<std::vector<math::PtEtaPhiELorentzVector>>();
        Charge_vec      = std::make_unique<std::vector<int>>();
        PdgId_vec       = std::make_unique<std::vector<int>>();
        Status_vec      = std::make_unique<std::vector<int>>();
        Parent_vec      = std::make_unique<std::vector<int>>();
        ParentId_vec    = std::make_unique<std::vector<int>>();
        VtxIdx_vec      = std::make_unique<std::vector<int>>();
        GenVtx_vec      = std::make_unique<std::vector<math::XYZPoint>>();
        TTFlag_vec      = std::make_unique<std::vector<bool>>();
    }

    void put(edm::Event & iEvent, bool keepMinimal, bool saveVtx) {
        iEvent.put(std::move(genParticle_vec));
        iEvent.put(std::move(Charge_vec     ), "Charge");
        iEvent.put(std::move(PdgId_vec      ), "PdgId");
        iEvent.put(std::move(Status_vec     ), "Status");
        iEvent.put(std::move(ParentId_vec   ), "ParentId");
        iEvent.put(std::move(Parent_vec     ), "Parent");
        if(saveVtx) {
            iEvent.put(std::move(VtxIdx_vec     ), "VtxIdx");
            iEvent.put(std::move(GenVtx_vec     ), "GenVtx");
        }
        if(!keepMinimal) {
            iEvent.put(std::move(TTFlag_vec     ), "TTFlag");
        }
    }

    void setVtxInfo(const math::XYZPoint& vtx) {
        auto it = std::find(GenVtx_vec->begin(), GenVtx_vec->end(), vtx);
        if (it == GenVtx_vec->end()) {
            GenVtx_vec->push_back(vtx);
            it = std::prev(GenVtx_vec->end());
        }
        VtxIdx_vec->push_back(std::distance(GenVtx_vec->begin(),it));
    }

    // ----------member data ---------------------------
    std::unique_ptr<std::vector<math::PtEtaPhiELorentzVector>> genParticle_vec;
    std::unique_ptr<std::vector<int>> Charge_vec, PdgId_vec, Status_vec, Parent_vec, ParentId_vec, VtxIdx_vec;
    std::unique_ptr<std::vector<math::XYZPoint>> GenVtx_vec;
    std::unique_ptr<std::vector<bool>> TTFlag_vec;
};

class GenParticlesProducer : public edm::global::EDProducer<> {

public:
    explicit GenParticlesProducer(const edm::ParameterSet&);
    ~GenParticlesProducer() override;

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
    const reco::GenParticle* findLast(const reco::GenParticle& particle) const;
    void saveChain(int depth, int parentId, int parent_idx, const reco::GenParticle& particle,
                   GenPartInfos& genPartInfos,
                   std::unordered_set<const reco::Candidate *>& stored_particles_ref,
                   std::vector<const reco::Candidate *>& stored_particles_list,
                   std::vector<const reco::Candidate *>& parents_list) const;
    void storeMinimal(const edm::Handle< edm::View<reco::GenParticle> >& genPartCands, GenPartInfos& genPartInfos) const;
    void storeStandard(const edm::Handle< edm::View<reco::GenParticle> >& genPartCands, GenPartInfos& genPartInfos) const;

    // ----------member data ---------------------------

    edm::InputTag genCollection;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> genCollectionTok;
    bool        debug;
    std::unordered_set<int> typicalChildIds, typicalParentIds, keepAllTheseIds;
    bool        keepFirstDecayProducts;
    bool        keepMinimal, saveVtx;
    const std::vector<int> proton_status_codes, initial_parton_status_codes, quark_status_codes, lepton_status_codes, top_status_codes, boson_status_codes;
};


GenParticlesProducer::GenParticlesProducer(const edm::ParameterSet& iConfig):
genCollection(iConfig.getParameter<edm::InputTag>("genCollection")),
genCollectionTok(consumes<edm::View<reco::GenParticle>>(genCollection)),
debug(iConfig.getParameter<bool>("debug")),
// Final copy status codes
proton_status_codes{4},
initial_parton_status_codes{21},
quark_status_codes{23,51,52,71,72,73,91},
lepton_status_codes{1,2},
top_status_codes{22,51,52,62},
boson_status_codes{22,51,52,62}
{
    const auto& cids = iConfig.getParameter<std::vector<int>>("childIds");
    typicalChildIds.insert(cids.begin(),cids.end());

    const auto& pids = iConfig.getParameter<std::vector<int>>("parentIds");
    typicalParentIds.insert(pids.begin(),pids.end());

    const auto& ids = iConfig.getParameter<std::vector<int>>("keepIds");
    keepAllTheseIds.insert(ids.begin(),ids.end());

    keepFirstDecayProducts = iConfig.getParameter<bool>("keepFirst");

    keepMinimal = iConfig.getParameter<bool>("keepMinimal");

    saveVtx = iConfig.getParameter<bool>("saveVtx");

    produces< std::vector< math::PtEtaPhiELorentzVector > >("");
    produces< std::vector< int > >("Charge");
    produces< std::vector< int > >("PdgId");
    produces< std::vector< int > >("Status");
    produces< std::vector< int > >("Parent");
    produces< std::vector< int > >("ParentId");
    produces< std::vector< int > >("VtxIdx");
    produces< std::vector< math::XYZPoint > >("GenVtx");
    if(!keepMinimal)
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

    GenPartInfos genPartInfos;

    edm::Handle< View<reco::GenParticle> > genPartCands;
    iEvent.getByToken(genCollectionTok, genPartCands);

    //Filter out unwanted gen particles and store 4-vector, pdgid, status, and parentID:
    if (debug) {
        edm::LogInfo("TreeMaker")<< "======new event============"<<"\n"
        <<"idx\t"<<"pdgId\t"<<"status\t"<<"parId\t"<<"parIdx\t";
    }

    if (keepMinimal) storeMinimal(genPartCands, genPartInfos);
    else             storeStandard(genPartCands, genPartInfos);

    genPartInfos.put(iEvent,keepMinimal,saveVtx);
}

// Based on http://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf
enum particle_type
{
    //SM particles
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
    Higgs=25,
    proton=2212,
    //SUSY particles
    sdownL=1000001,
    supL=1000002,
    sstrangeL=1000003,
    scharmL=1000004,
    sbottom1=1000005,
    stop1=1000006,
    gluino=1000021,
    neutralino1=1000022,
    neutralino2=1000023,
    chargino1=1000024,
    neutralino3=1000025,
    neutralino4=1000035,
    chargino2=1000037,
    gravitino=1000039,
    sdownR=2000001,
    supR=2000002,
    sstrangeR=2000003,
    scharmR=2000004,
    sbottom2=2000005,
    stop2=2000006,
    //HV particles
    hvscalar=4900001,
    hvgluon=4900021,
    zprime=4900023,
    hvquark1=4900101,
    hvquark2=4900102,
    hvpion1=4900111,
    hvrho1=4900113,
    hvpion2=4900211,
    hvrho2=4900213,
    //DM particles
    dm1=51,
    dm2=52,
    dm3=53,
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
    unsigned int lastPdgId = abs(last->pdgId());
    int lastStatus = last->status();
    if(((lastPdgId >= down && lastPdgId <= bottom) && !std::binary_search(quark_status_codes.begin(), quark_status_codes.end(), lastStatus)) ||
       (lastPdgId == top && !std::binary_search(top_status_codes.begin(), top_status_codes.end(), lastStatus)) ||
       (lastPdgId == W && !std::binary_search(boson_status_codes.begin(), boson_status_codes.end(), lastStatus)) ||
       ((lastPdgId >= electron && lastPdgId <= tau_neutrino) && !std::binary_search(lepton_status_codes.begin(), lepton_status_codes.end(), lastStatus))) {
        edm::LogInfo("TreeMaker") << "WARNING The last particle in the chain (" << lastPdgId << ") does not have a status that corresponds to its type (status=" << lastStatus << ")";
    }

    return last;
}

void GenParticlesProducer::saveChain(int depth, int parentId, int parent_idx, const reco::GenParticle& particle,
                                     GenPartInfos& genPartInfos,
                                     std::unordered_set<const reco::Candidate *>& stored_particles_ref,
                                     std::vector<const reco::Candidate *>& stored_particles_list,
                                     std::vector<const reco::Candidate *>& parents_list) const {
    // Set a minimal depth of particles to save
    if(depth==0) return;
    auto lastParticle = findLast(particle);
    // Special hack to keep first copy of HV Zprime daughters
    if(parentId==zprime) lastParticle = &particle;
    // Skip particles which are already in the list of stored particles
    if(stored_particles_ref.find(lastParticle)!=stored_particles_ref.end()) {
       if(debug) edm::LogInfo("TreeMaker") << "   Skipping duplicate particle (pdgId=" << lastParticle->pdgId() << " status=" << lastParticle->status() << " pointer=" << lastParticle << ")";
       return;
    }
    if(debug) edm::LogInfo("TreeMaker") << "   Saving chain for a " << particle.pdgId() << " (status=" << particle.status() << " pointer=" << lastParticle << ")\n      Current depth is " << depth;

    // Save the gen particle information
    math::PtEtaPhiELorentzVector tmp(lastParticle->pt(), lastParticle->eta(), lastParticle->phi(), lastParticle->energy());
    genPartInfos.genParticle_vec->push_back(tmp);
    genPartInfos.Charge_vec->push_back(lastParticle->charge());
    genPartInfos.PdgId_vec->push_back(lastParticle->pdgId());
    genPartInfos.Status_vec->push_back(abs(lastParticle->status()));
    stored_particles_ref.insert(lastParticle);
    stored_particles_list.push_back(lastParticle);
    parents_list.push_back(lastParticle->mother());
    genPartInfos.ParentId_vec->push_back(parentId);
    genPartInfos.Parent_vec->push_back(parent_idx);
    genPartInfos.setVtxInfo(lastParticle->vertex());
    int current_parent_idx = genPartInfos.PdgId_vec->size()-1;
    int current_parent_id = genPartInfos.PdgId_vec->back();

    // Save the daughters
    // negative depth indicates signal
    if(lastParticle->numberOfDaughters()==2 || depth<0) {
        int nextDepth = --depth;
        for(unsigned int iDau=0; iDau<lastParticle->numberOfDaughters(); iDau++) {
            if(abs(lastParticle->pdgId())<=bottom) continue;
            const reco::GenParticle *daughter = static_cast<const reco::GenParticle *>(lastParticle->daughter(iDau));
            saveChain(nextDepth, current_parent_id, current_parent_idx, *daughter, genPartInfos, stored_particles_ref, stored_particles_list, parents_list);
        }
    }

    return;
}

void GenParticlesProducer::storeMinimal(const edm::Handle< edm::View<reco::GenParticle> >& genPartCands, GenPartInfos& genPartInfos) const {
    std::unordered_set<const reco::Candidate *> stored_particles_ref;
    std::vector<const reco::Candidate *> stored_particles_list, parents_list;
    std::array<const reco::Candidate*, 2> possible_mothers{ {&(*genPartCands->begin()), &(*(genPartCands->begin()+1))} };
    for(const auto& particle : *genPartCands) {
        // Skip particles which are already in the list of stored particles
        // This is to protect against parts of a chain which may be saved, but here we are looking at the first copy
        if(stored_particles_ref.find(&particle)!=stored_particles_ref.end()) continue;

        // Store the initial partons
        auto nmothers = particle.numberOfMothers();
        if(nmothers == 1) {
           auto mother = particle.mother(0);
           if(mother->pdgId() == proton &&
              mother->status() == proton_status_codes[0] &&
              (mother == possible_mothers[0] || mother == possible_mothers[1]) &&
              particle.status()==initial_parton_status_codes[0]) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving an initial parton " << particle.pdgId() << " ... ";
                math::PtEtaPhiELorentzVector tmp(particle.pt(), particle.eta(), particle.phi(), particle.energy());
                genPartInfos.genParticle_vec->push_back(tmp);
                genPartInfos.Charge_vec->push_back(particle.charge());
                genPartInfos.PdgId_vec->push_back(particle.pdgId());
                genPartInfos.Status_vec->push_back(abs(particle.status()));
                stored_particles_ref.insert(&particle);
                stored_particles_list.push_back(&particle);
                parents_list.push_back(mother);
                genPartInfos.ParentId_vec->push_back(mother->pdgId());
                genPartInfos.Parent_vec->push_back(-1);
                genPartInfos.setVtxInfo(particle.vertex());
           }
        }

        // Skip starting particles which are not from the hard process
        if(!particle.isHardProcess() && !particle.fromHardProcessBeforeFSR()) continue;

        // Only store particles in the list of acceptable parent pdgids
        auto absPdgId = abs(particle.pdgId());
        if(typicalParentIds.find(absPdgId)!=typicalParentIds.end()) {
            if (absPdgId==top) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving a top chain ... ";
                saveChain(3, particle.mother()->pdgId(), -1, particle, genPartInfos, stored_particles_ref, stored_particles_list, parents_list);
            }
            else if(absPdgId>=photon && absPdgId<=Higgs) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving a boson chain ... ";
                saveChain(2, particle.mother()->pdgId(), -1, particle, genPartInfos, stored_particles_ref, stored_particles_list, parents_list);
            }
            else if(absPdgId>=sdownL && absPdgId<=stop2) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving a SUSY chain ... ";
                saveChain(-1, particle.mother()->pdgId(), -1, particle, genPartInfos, stored_particles_ref, stored_particles_list, parents_list);
            }
            else if(absPdgId>=hvscalar && absPdgId<=hvrho2) {
                if(debug) edm::LogInfo("TreeMaker") << "Saving a Hidden Valley chain ... ";
                saveChain(-1, particle.mother()->pdgId(), -1, particle, genPartInfos, stored_particles_ref, stored_particles_list, parents_list);
            }
            else {
                if(debug) edm::LogInfo("TreeMaker") << "Saving an individual particle " << particle.pdgId() << " ... ";
                math::PtEtaPhiELorentzVector tmp(particle.pt(), particle.eta(), particle.phi(), particle.energy());
                genPartInfos.genParticle_vec->push_back(tmp);
                genPartInfos.Charge_vec->push_back(particle.charge());
                genPartInfos.PdgId_vec->push_back(particle.pdgId());
                genPartInfos.Status_vec->push_back(abs(particle.status()));
                stored_particles_ref.insert(&particle);
                stored_particles_list.push_back(&particle);
                parents_list.push_back(particle.mother());
                genPartInfos.ParentId_vec->push_back(particle.mother()->pdgId());
                genPartInfos.Parent_vec->push_back(-1);
                genPartInfos.setVtxInfo(particle.vertex());
            }
        }
    }

    //fill in the parents
    for(unsigned g = 0; g < stored_particles_list.size(); ++g){
        //some already have parent indices
        if(genPartInfos.Parent_vec->at(g)!=-1) continue;
        auto it = std::find(stored_particles_list.begin(),stored_particles_list.end(),parents_list[g]);
        if(it!=stored_particles_list.end()){
            genPartInfos.Parent_vec->at(g) = std::distance(stored_particles_list.begin(),it);
        }
    }
}

void GenParticlesProducer::storeStandard(const edm::Handle< edm::View<reco::GenParticle> >& genPartCands, GenPartInfos& genPartInfos) const {

    auto parents = std::make_unique<std::vector<math::PtEtaPhiELorentzVector>>();

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

        math::PtEtaPhiELorentzVector temp(iPart.pt(), iPart.eta(), iPart.phi(), iPart.energy());
        genPartInfos.genParticle_vec->push_back(temp);
        genPartInfos.Charge_vec->push_back(iPart.charge());
        genPartInfos.PdgId_vec->push_back(iPart.pdgId());
        genPartInfos.Status_vec->push_back(status);
        genPartInfos.TTFlag_vec->push_back(!(acceptableChild || acceptableParent) && (keepAllThese || firstDecayProducts));
        math::PtEtaPhiELorentzVector parent(0,0,0,0);
        int parentid = 0;
        const reco::GenParticle *Parent;
        Parent = static_cast<const reco::GenParticle *>(iPart.mother());
        while (true) {
            if (!(Parent)) break;
            if (debug) {
                if (abs(genPartInfos.PdgId_vec->back())==24) {
                    edm::LogInfo("TreeMaker") << "W parent Id, status ="<< Parent->pdgId()<<", "<<Parent->status()<<",px="<<Parent->px()<<",py="<<Parent->py()<<",phi="<<Parent->phi();
                }
            }
            if (Parent->isLastCopy() || Parent->status()==21) {
                parentid = Parent->pdgId();
                parent.SetCoordinates(Parent->pt(), Parent->eta(), Parent->phi(), Parent->energy());
                if (debug) {
                    if (abs(genPartInfos.PdgId_vec->back())==24) {
                        edm::LogInfo("TreeMaker") << "planning to keep this mother";
                    }
                }
                break;
            }
            Parent = static_cast<const reco::GenParticle *>(Parent->mother());
        }
        parents->push_back(parent);
        genPartInfos.ParentId_vec->push_back(parentid);
        genPartInfos.setVtxInfo(iPart.vertex());
    }

    //Identify each gp's parent within the vector of stored gp's and store parentIdx:
    std::vector<math::PtEtaPhiELorentzVector>::iterator itlv;
    for (unsigned int g = 0; g < genPartInfos.genParticle_vec->size(); g++) {
        itlv = std::find(genPartInfos.genParticle_vec->begin(), genPartInfos.genParticle_vec->end(), parents->at(g));
        auto index = std::distance(genPartInfos.genParticle_vec->begin(), itlv);
        int parentIndex = index;
        if (itlv == genPartInfos.genParticle_vec->end()) parentIndex = -1;
        genPartInfos.Parent_vec->push_back(parentIndex);
        if (debug) {
          edm::LogInfo("TreeMaker")<<g<<"\t"<<genPartInfos.PdgId_vec->at(g)<<"\t"<<genPartInfos.Status_vec->at(g)<<"\t"<<genPartInfos.ParentId_vec->at(g)
          <<"\t"<<genPartInfos.Parent_vec->at(g)<<"\n" //<<", eta="<<  parents->at(g).Eta() <<"phi="<< parents->at(g).Phi() <<"\n"
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
