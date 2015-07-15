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

	edm::InputTag JetTag_;
        edm::InputTag reclusJetTag_;
	double maxEta_;
	double maxMuFraction_, minNConstituents_, maxNeutralFraction_, maxPhotonFraction_, minChargedMultiplicity_, minChargedFraction_, maxChargedEMFraction_;

        double jetPtCut_miniAOD_, genMatch_dR_;
        double relPt_for_xCheck_, dR_for_xCheck_;
        bool debug_;	
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
        const std::string string1t("JetFlag");
        const std::string string1("Jet");
        produces<std::vector<Jet> > (string1).setBranchAlias(string1);
        produces<std::vector<int> > (string1t).setBranchAlias(string1t);

	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
        reclusJetTag_ = iConfig.getParameter<edm::InputTag>("reclusJetTag");
	maxEta_ = iConfig.getParameter <double> ("maxJetEta");
	maxMuFraction_ = iConfig.getParameter <double> ("maxMuFraction");
	minNConstituents_ = iConfig.getParameter <double> ("minNConstituents");
	maxNeutralFraction_ = iConfig.getParameter <double> ("maxNeutralFraction");
	maxPhotonFraction_ = iConfig.getParameter <double> ("maxPhotonFraction");
	minChargedMultiplicity_ = iConfig.getParameter <double> ("minChargedMultiplicity");
	minChargedFraction_ = iConfig.getParameter <double> ("minChargedFraction");
	maxChargedEMFraction_ = iConfig.getParameter <double> ("maxChargedEMFraction");
        jetPtCut_miniAOD_ = iConfig.getParameter<double>("jetPtCut_miniAOD");
        genMatch_dR_ = iConfig.getParameter<double>("genMatch_dR");
        dR_for_xCheck_ = iConfig.getParameter<double>("dR_for_xCheck");
        relPt_for_xCheck_ = iConfig.getParameter<double>("relPt_for_xCheck");
        debug_ = iConfig.getParameter<bool>("debug");
        
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
  std::auto_ptr<std::vector<Jet> > prodJets(new std::vector<Jet>());
  std::auto_ptr< std::vector<int> > prodJetsFlag(new std::vector<int>);
//  edm::Handle< edm::View<Jet> > Jets;
//  edm::Handle< edm::View<Jet> > reclusJets;
  edm::Handle<std::vector<pat::Jet> > Jets,reclusJets; 
  edm::Handle<edm::View<reco::GenParticle> > pruned;
  edm::Handle<edm::View<pat::Muon> > muon;
  edm::Handle<edm::View<pat::Electron> > electron;  

  iEvent.getByLabel(JetTag_,Jets);
  iEvent.getByLabel(reclusJetTag_,reclusJets);
  iEvent.getByLabel("prunedGenParticles",pruned);
  iEvent.getByLabel("slimmedMuons", muon);
  iEvent.getByLabel("slimmedElectrons", electron);

  // finalJets should be equal to slimmedJets when pt>10. 
  // We just want to add low pT reclustered Jets to it. 
  std::vector<pat::Jet> finalJets = (*Jets); 
  
  if(Jets.isValid() && reclusJets.isValid() )
  {

//.................................////.................................//
    
    // Check which ones to keep
    int cntJetPassPtCut = 0;
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
/*
             for(unsigned int ig=0; ig<muon->size(); ig++){
               // Only keep the jet if it matches one of the gen or reco leptons // this is to save disk space
                TLorentzVector muLVec; muLVec.SetPtEtaPhiE((*muon)[ig].pt(),(*muon)[ig].eta(),(*muon)[ig].phi(),(*muon)[ig].energy());
                double perdeltaR = perLVec.DeltaR(muLVec);
                if( perdeltaR < genMatch_dR_ ) cntgenMatch ++;
             }
*/             
             if( otjet_pt>0 && otjet_pt < 14000 &&  cntgenMatch ){
              finalJets.push_back(reclusJets->at(io));          
             }
          }
       }
    }

//.................................////.................................//

    for(unsigned int i=0; i<finalJets.size();i++)
    {
      //if(std::abs(finalJets.at(i).eta())>maxEta_)
      //{
	//prodJets->push_back(Jet(finalJets.at(i)) );
	//continue;
     // }
      float neufrac=finalJets.at(i).neutralHadronEnergyFraction();//gives raw energy in the denominator
      float phofrac=finalJets.at(i).neutralEmEnergyFraction();//gives raw energy in the denominator
      float chgfrac=finalJets.at(i).chargedHadronEnergyFraction();
      float chgEMfrac=finalJets.at(i).chargedEmEnergyFraction();
      float muFrac=finalJets.at(i).muonEnergyFraction();
      unsigned int nconstit=finalJets.at(i).nConstituents();
      int chgmulti=finalJets.at(i).chargedHadronMultiplicity();
      if(muFrac<maxMuFraction_ && std::abs(finalJets.at(i).eta())<2.4 &&  nconstit>minNConstituents_ && neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ &&chgmulti>minChargedMultiplicity_ && chgfrac>minChargedFraction_ && chgEMfrac<maxChargedEMFraction_)prodJetsFlag->push_back(1);
      else if(muFrac<maxMuFraction_ && std::abs(finalJets.at(i).eta())>=2.4 && nconstit>minNConstituents_ && neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_)prodJetsFlag->push_back(1);
      else prodJetsFlag->push_back(0);
      prodJets->push_back(Jet(finalJets.at(i)) );
      // 	std::cout<<"muFrac<maxMuFraction_"<<muFrac<<" < "<<maxMuFraction_<<std::endl
      // 	<<"nconstit>minNConstituents_"<<nconstit<<" > "<<minNConstituents_<<std::endl
      // 	<<"neufrac<maxNeutralFraction_"<<neufrac<<" < "<<maxNeutralFraction_<<std::endl
      // 	<<"phofrac<maxPhotonFraction_"<<phofrac<<" < "<<maxPhotonFraction_<<std::endl
      // 	<<"chgmulti>minChargedMultiplicity_"<<chgmulti<<" > "<<minChargedMultiplicity_<<std::endl
      // 	<<"chgfrac>minChargedFraction_"<<chgfrac<<" > "<<minChargedFraction_<<std::endl
      // 	<<"chgEMfrac<maxChargedEMFraction_"<<chgEMfrac<<" < "<<maxChargedEMFraction_<<std::endl
      // 	<<std::endl<<std::endl<<std::endl;
    }
  }
  // put in the event
  const std::string string1t("JetFlag");
  const std::string string1("Jet");
  iEvent.put(prodJetsFlag,string1t);
  iEvent.put(prodJets,string1);
  
  if(!finalJets.empty())
    finalJets.clear();
  
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
