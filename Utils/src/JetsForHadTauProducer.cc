// -*- C++ -*-
//
// Package:    JetsForHadTauProducer
// Class:      JetsForHadTauProducer
// 
/**\class JetsForHadTauProducer JetsForHadTauProducer.cc 
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Thu Apr 17 10:49:52 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"

//
// class declaration
//

class JetsForHadTauProducer : public edm::global::EDProducer<> {
public:
    explicit JetsForHadTauProducer(const edm::ParameterSet&);
    ~JetsForHadTauProducer();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
private:
    virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

    const reco::GenParticle* TauFound(const reco::GenParticle * particle) const;
    bool matchJetLepton(const pat::Jet* otjet, const edm::Handle<edm::View<reco::GenParticle> >& pruned,
                        const edm::Handle<edm::View<pat::Muon> >& muon, const edm::Handle<edm::View<pat::Electron> >& electron) const;

    // ----------member data ---------------------------
    edm::InputTag JetTag_, reclusJetTag_, MuonTag_, ElecTag_, GenPartTag_;
    edm::EDGetTokenT<edm::View<pat::Muon>> MuonTok_;
    edm::EDGetTokenT<edm::View<pat::Electron>> ElecTok_;
    edm::EDGetTokenT<std::vector<pat::Jet>> JetTok_, reclusJetTok_;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> GenPartTok_;
    double jetPtCut_miniAOD_, genMatch_dR_;
    double relPt_for_xCheck_, dR_for_xCheck_;
    bool debug_;
    bool MCflag_;
    bool useReclusteredJets_;
    bool requireLeptonMatch_;
};

//
// constructors and destructor
//
using namespace pat;
JetsForHadTauProducer::JetsForHadTauProducer(const edm::ParameterSet& iConfig)
{
    JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
    reclusJetTag_ = iConfig.getParameter<edm::InputTag>("reclusJetTag");
    jetPtCut_miniAOD_ = iConfig.getParameter<double>("jetPtCut_miniAOD");
    genMatch_dR_ = iConfig.getParameter<double>("genMatch_dR");
    dR_for_xCheck_ = iConfig.getParameter<double>("dR_for_xCheck");
    relPt_for_xCheck_ = iConfig.getParameter<double>("relPt_for_xCheck");
    MCflag_ = iConfig.getParameter<bool>("MCflag");
    useReclusteredJets_ = iConfig.getParameter<bool>("useReclusteredJets");
    requireLeptonMatch_ = iConfig.getParameter<bool>("requireLeptonMatch");
    debug_ = iConfig.getParameter<bool>("debug");
    MuonTag_ = edm::InputTag("slimmedMuons");
    ElecTag_ = edm::InputTag("slimmedElectrons");
    GenPartTag_ = edm::InputTag("prunedGenParticles");
    
    MuonTok_ = consumes<edm::View<pat::Muon>>(MuonTag_);
    ElecTok_ = consumes<edm::View<pat::Electron>>(ElecTag_);
    JetTok_ = consumes<std::vector<pat::Jet>>(JetTag_);
    reclusJetTok_ = consumes<std::vector<pat::Jet>>(reclusJetTag_);
    GenPartTok_ = consumes<edm::View<reco::GenParticle>>(GenPartTag_);

    produces<std::vector<Jet> >();
}


JetsForHadTauProducer::~JetsForHadTauProducer()
{
	
	// do anything here that needs to be done at destruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetsForHadTauProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;
  edm::Handle<std::vector<pat::Jet> > Jets,reclusJets; 
  edm::Handle<edm::View<reco::GenParticle> > pruned;
  edm::Handle<edm::View<pat::Muon> > muon;
  edm::Handle<edm::View<pat::Electron> > electron;  

  iEvent.getByToken(JetTok_,Jets);
  if (useReclusteredJets_) iEvent.getByToken(reclusJetTok_,reclusJets);
  iEvent.getByToken(MuonTok_, muon);
  iEvent.getByToken(ElecTok_, electron);
  if (MCflag_) iEvent.getByToken(GenPartTok_,pruned);

  auto finalJets = std::make_unique<std::vector<Jet>>();
  
  // finalJets should contain all jets (high-pt duplicates will be discarded after JER smearing)
  // use lepton matching to save space
  if(Jets.isValid()){
    for(unsigned int ij=0; ij< Jets->size(); ij++){
      if(!requireLeptonMatch_ || matchJetLepton(&(Jets->at(ij)),pruned,muon,electron)) finalJets->push_back(Jets->at(ij));
    }
  }
  
  if (useReclusteredJets_){
  if (debug_) edm::LogWarning("TreeMaker") << "Jets and reclusJets isValid:" << Jets.isValid() << " " << reclusJets.isValid();
  if(Jets.isValid() && reclusJets.isValid() )
  {

//.................................////.................................//
    
    // Check which ones to keep
    if (debug_) edm::LogWarning("TreeMaker") << "Jets and reclusJets size:" << Jets->size() << " " << reclusJets->size();
    for(unsigned int io=0; io < reclusJets->size(); io++){
       const double otjet_pt = reclusJets->at(io).pt(), otjet_eta = reclusJets->at(io).eta(), otjet_phi = reclusJets->at(io).phi();
       int cntFound = 0, matchedIdx = -1;
       double minDR = 999.0;
       for(unsigned int ij=0; ij< Jets->size(); ij++){
          const double dR = deltaR(reclusJets->at(io).p4(),Jets->at(ij).p4());
          if( minDR > dR ){
             minDR = dR; matchedIdx = ij;
          }
       }
       if( matchedIdx != -1 ){
          if( minDR < dR_for_xCheck_ && std::abs(otjet_pt - Jets->at(matchedIdx).pt())/Jets->at(matchedIdx).pt() < relPt_for_xCheck_ ){
             cntFound ++;
          }
       }
       if( otjet_pt > jetPtCut_miniAOD_ ){
          if( cntFound != 1 && debug_ ){
            std::stringstream stmp;
            if( matchedIdx != -1 ) stmp <<"\n  jet_pt : "<<Jets->at(matchedIdx).pt()<<"    jet_eta : "<<Jets->at(matchedIdx).eta()<<"    jet_phi : "<<Jets->at(matchedIdx).phi();
            edm::LogWarning("TreeMaker")<<"WARNING ... jet mis-matching between reclusJets and jets for pt > "<<jetPtCut_miniAOD_<<"  matchedIdx: "<<matchedIdx<<"  cntFound: "<<cntFound<<"\n"
              <<"otjet_pt : "<<otjet_pt<<"  otjet_eta : "<<otjet_eta<<"  otjet_phi : "<<otjet_phi
              << stmp.str();
          }
       }else{
          if( cntFound && debug_ ){
             edm::LogWarning("TreeMaker")<<"WARNING ... otjet with pt : "<<otjet_pt<<"  matching to one of the jets for pt > "<<jetPtCut_miniAOD_<<" ?!"<<"\n"
               <<"otjet_pt : "<<otjet_pt<<"  otjet_eta : "<<otjet_eta<<"  otjet_phi : "<<otjet_phi<<"\n"
               <<"  jet_pt : "<<Jets->at(matchedIdx).pt()<<"    jet_eta : "<<Jets->at(matchedIdx).eta()<<"    jet_phi : "<<Jets->at(matchedIdx).phi();
          }else{
             if( otjet_pt>0 && otjet_pt <= jetPtCut_miniAOD_ && matchJetLepton(&(reclusJets->at(io)),pruned,muon,electron) ){
              finalJets->push_back(reclusJets->at(io));
             }
          }
       } // above or below jetPtCut_miniAOD_
    } // reclusJets loop
  } // Jets.isValid() and reclusJets.isValid()
  } // useReclusteredJets_

  // put in the event
  iEvent.put(std::move(finalJets));
  
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetsForHadTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

const reco::GenParticle* JetsForHadTauProducer::TauFound(const reco::GenParticle * particle) const
{
        for(size_t i=0;i< particle->numberOfDaughters();i++)
        {
          if(abs(particle->daughter(i)->pdgId()) == 15) return TauFound((reco::GenParticle*)particle->daughter(i));
        }
        return particle;
        
}

bool JetsForHadTauProducer::matchJetLepton(const pat::Jet* otjet, const edm::Handle<edm::View<reco::GenParticle> >& pruned,
                                           const edm::Handle<edm::View<pat::Muon> >& muon, const edm::Handle<edm::View<pat::Electron> >& electron) const
{
    int cntgenMatch = 0;
    //
    // Check gen leptons
    //
    if (MCflag_ && pruned.isValid()) { // this matching check is done only if pruned particle collection exists
        for(unsigned int ig=0; ig<pruned->size(); ig++){
          // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
          const reco::GenParticle* genPart = &(*pruned)[ig];
          if(  abs(genPart->pdgId())==11 || abs(genPart->pdgId())==13 || abs(genPart->pdgId())==15  ){
             double perdeltaR = deltaR(otjet->p4(),genPart->p4());
             if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
          
             // Sometimes the nutrinos of tau are so energetic that gen. tau and it hadronic daughter are 
             // in two different directions. We would like to store those type of jets as well.
             if(abs(genPart->pdgId())==15){
               const reco::GenParticle* FinalTauDecay = TauFound(genPart);
               for(unsigned int igg=0; igg<FinalTauDecay->numberOfDaughters(); igg++){
                 if( abs( FinalTauDecay->daughter(igg)->pdgId() )==16 ){
                   auto TauMinusNuLVec = genPart->p4() - FinalTauDecay->daughter(igg)->p4();
                   perdeltaR = deltaR(otjet->p4(),TauMinusNuLVec);
                   if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
                 }  
               }
             }
           }
        }
    } // MC flag
    //
    // Check reco muons
    //
    if (muon.isValid()){
        for(unsigned int ig=0; ig<muon->size(); ig++){
          // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
           double perdeltaR = deltaR(otjet->p4(),(*muon)[ig].p4());
           if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
        }
    }
    //
    // Check reco electrons
    //
    if (electron.isValid()){
        for(unsigned int ig=0; ig<electron->size(); ig++){
          // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
           double perdeltaR = deltaR(otjet->p4(),(*electron)[ig].p4());
           if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
        }
    }
    //
    //
    //
	return cntgenMatch;
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetsForHadTauProducer);
