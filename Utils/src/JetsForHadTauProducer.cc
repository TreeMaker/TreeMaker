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
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"

#include "TLorentzVector.h"
//
// class declaration
//

class JetsForHadTauProducer : public edm::EDProducer {
public:
	explicit JetsForHadTauProducer(const edm::ParameterSet&);
	~JetsForHadTauProducer();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

    const reco::GenParticle* TauFound(const reco::GenParticle * particle);

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
	// ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

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
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetsForHadTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  // finalJets should be equal to slimmedJets when pt>10. 
  // We just want to add low pT reclustered Jets to it. 
  std::auto_ptr<std::vector<Jet> > finalJets(new std::vector<Jet>(*Jets));

  if (useReclusteredJets_){
  if (debug_) std::cout << "Jets and reclusJets isValid:" << Jets.isValid() << " " << reclusJets.isValid() << std::endl;
  if(Jets.isValid() && reclusJets.isValid() )
  {

//.................................////.................................//
    
    // Check which ones to keep
    int cntJetPassPtCut = 0;
    if (debug_) std::cout << "Jets and reclusJets size:" << Jets->size() << " " << reclusJets->size() << std::endl;
    for(unsigned int io=0; io < reclusJets->size(); io++){
       const double otjet_pt = reclusJets->at(io).pt(), otjet_eta = reclusJets->at(io).eta(), otjet_phi = reclusJets->at(io).phi();
       TLorentzVector perLVec; perLVec.SetPtEtaPhiE(otjet_pt, otjet_eta, otjet_phi, reclusJets->at(io).energy());
       int cntFound = 0, matchedIdx = -1;
       double minDR = 999.0;
       for(unsigned int ij=0; ij< Jets->size(); ij++){
          const double jet_eta = Jets->at(ij).eta(), jet_phi = Jets->at(ij).phi();
          const double dR = reco::deltaR(otjet_eta, otjet_phi, jet_eta, jet_phi);
          if( minDR > dR ){
             minDR = dR; matchedIdx = ij;
          }
       }
       if( matchedIdx != -1 ){
          if( minDR < dR_for_xCheck_ && std::abs(otjet_pt - Jets->at(matchedIdx).pt())/Jets->at(matchedIdx).pt() < relPt_for_xCheck_ ){
             cntFound ++;
          }
       }
       if( otjet_pt >= jetPtCut_miniAOD_ ){

          cntJetPassPtCut ++;
          if( cntFound != 1 && debug_ ){
            std::cout<<"WARNING ... jet mis-matching between reclusJets and jets for pt > "<<jetPtCut_miniAOD_<<"  matchedIdx: "<<matchedIdx<<"  cntFound: "<<cntFound<<std::endl;
            std::cout<<"otjet_pt : "<<otjet_pt<<"  otjet_eta : "<<otjet_eta<<"  otjet_phi : "<<otjet_phi<<std::endl;
            if( matchedIdx != -1 ) std::cout<<"  jet_pt : "<<Jets->at(matchedIdx).pt()<<"    jet_eta : "<<Jets->at(matchedIdx).eta()<<"    jet_phi : "<<Jets->at(matchedIdx).phi()<<std::endl;
          }
       }else{
          if( cntFound && debug_ ){
             std::cout<<"WARNING ... otjet with pt : "<<otjet_pt<<"  matching to one of the jets for pt > "<<jetPtCut_miniAOD_<<" ?!"<<std::endl;
             std::cout<<"otjet_pt : "<<otjet_pt<<"  otjet_eta : "<<otjet_eta<<"  otjet_phi : "<<otjet_phi<<std::endl;
             std::cout<<"  jet_pt : "<<Jets->at(matchedIdx).pt()<<"    jet_eta : "<<Jets->at(matchedIdx).eta()<<"    jet_phi : "<<Jets->at(matchedIdx).phi()<<std::endl;
          }else{
             int cntgenMatch = 0;
	     //
	     // Check gen leptons
	     //
	     if (MCflag_){
	     if (pruned.isValid()) { // this matching check is done only if pruned particle collection exists
             for(unsigned int ig=0; ig<pruned->size(); ig++){
               // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
               if(  abs((*pruned)[ig].pdgId())==11 || abs((*pruned)[ig].pdgId())==13 || abs((*pruned)[ig].pdgId())==15  ){
                  TLorentzVector genLVec; genLVec.SetPtEtaPhiE((*pruned)[ig].pt(),(*pruned)[ig].eta(),(*pruned)[ig].phi(),(*pruned)[ig].energy());
                  double perdeltaR = perLVec.DeltaR(genLVec);
                  if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
               
                  // Sometimes the nutrinos of tau are so energetic that gen. tau and it hadronic daughter are 
                  // in two different directions. We would like to store those type of jets as well.
                  if(abs((*pruned)[ig].pdgId())==15){		    
		    const reco::GenParticle * FinalTauDecay = TauFound(&(*pruned)[ig]);
		    TLorentzVector genNuLVec,TauMinusNuLVec;
                    for(unsigned int igg=0; igg<FinalTauDecay->numberOfDaughters(); igg++){
                      if( abs( FinalTauDecay->daughter(igg)->pdgId() )==16 ){
                        genNuLVec.SetPtEtaPhiE(FinalTauDecay->daughter(igg)->pt(),FinalTauDecay->daughter(igg)->eta(),FinalTauDecay->daughter(igg)->phi(),FinalTauDecay->daughter(igg)->energy());
                        TauMinusNuLVec = genLVec - genNuLVec;
                        perdeltaR = perLVec.DeltaR(TauMinusNuLVec);
                        if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
                      }  
                    }
                  }
                }
             }
	     } // pruned.isValid()
	     } // MC flag
	     //
	     // Check reco muons
	     //
	     if (muon.isValid()){
             for(unsigned int ig=0; ig<muon->size(); ig++){
               // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
                TLorentzVector muLVec; muLVec.SetPtEtaPhiE((*muon)[ig].pt(),(*muon)[ig].eta(),(*muon)[ig].phi(),(*muon)[ig].energy());
                double perdeltaR = perLVec.DeltaR(muLVec);
                if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
             }
	     }
	     //
	     // Check reco electrons
	     //
	     if (electron.isValid()){
             for(unsigned int ig=0; ig<electron->size(); ig++){
               // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
                TLorentzVector muLVec; muLVec.SetPtEtaPhiE((*electron)[ig].pt(),(*electron)[ig].eta(),(*electron)[ig].phi(),(*electron)[ig].energy());
                double perdeltaR = perLVec.DeltaR(muLVec);
                if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
             }
	     }
	     //
	     //
	     //
             if( otjet_pt>0 && otjet_pt < 14000 &&  cntgenMatch ){
              finalJets->push_back(reclusJets->at(io));          
             }
          }
       } // above or below jetPtCut_miniAOD_
    } // reclusJets loop
  } // Jets.isValid() and reclusJets.isValid()
  } // useReclusteredJets_

  // put in the event
  iEvent.put(finalJets);
  
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetsForHadTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetsForHadTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
JetsForHadTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
JetsForHadTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
JetsForHadTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
JetsForHadTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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

const reco::GenParticle* JetsForHadTauProducer::TauFound(const reco::GenParticle * particle)
{
        for(size_t i=0;i< particle->numberOfDaughters();i++)
        {
          if(abs(particle->daughter(i)->pdgId()) == 15) return TauFound((reco::GenParticle*)particle->daughter(i));
        }
        return particle;
        
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetsForHadTauProducer);
