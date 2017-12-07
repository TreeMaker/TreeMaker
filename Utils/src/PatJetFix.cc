// -*- C++ -*-
//
// Package:     ECALSlewFix/PatJetFix
// Class:        PatJetFix
// 
/**\class PatJetFix PatJetFix.cc ECALSlewFix/PatJetFix/plugins/PatJetFix.cc

 Description: [one line class summary]

 Implementation:
      [Notes on implementation]
*/
//
// Original Author:  Rishi Patel
//            Created:  Sun, 05 Feb 2017 21:04:50 GMT
//
//


// system include files
#include <memory>
#include <algorithm>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "TLorentzVector.h"
#include "TVector3.h"

//
// class declaration
//

class PatJetFix : public edm::global::EDProducer<> {
    public:
        explicit PatJetFix(const edm::ParameterSet&);
        ~PatJetFix();
     
        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

        // ----------member data ---------------------------
        edm::InputTag met_;
        edm::InputTag metFix_;
        edm::InputTag pho_;
        edm::InputTag ele_;
        edm::InputTag jets_;
        edm::EDGetTokenT<edm::View<pat::MET> > METCorrTok_;
        edm::EDGetTokenT<edm::View<pat::MET> > METTok_;
        edm::EDGetTokenT<edm::View<pat::Jet> > JetTok_;
        edm::EDGetTokenT<edm::View<pat::Electron> >  eleToken_;
        edm::EDGetTokenT<edm::View<pat::Photon> >  phoToken_;
        edm::EDGetTokenT<edm::View<pat::Electron> >  eleFixToken_;
        edm::EDGetTokenT<edm::View<pat::Photon>  >  phoFixToken_;
        edm::EDGetTokenT<edm::View<pat::PackedCandidate>  >  pCandToken_;
        edm::InputTag phoFix_;
        edm::InputTag MET_;
        edm::InputTag METFix_;
        edm::InputTag eleFix_;
        edm::InputTag pCand_;
};

//
// constructors and destructor
//
PatJetFix::PatJetFix(const edm::ParameterSet& iConfig)
{
    //register your products
    //now do what ever initialization is needed
    MET_=iConfig.getParameter<edm::InputTag>("MET");
    METFix_=iConfig.getParameter<edm::InputTag>("METCorr");
    eleFix_=iConfig.getParameter<edm::InputTag>("electronsFixed");
    ele_=iConfig.getParameter<edm::InputTag>("electrons");
    pho_=iConfig.getParameter<edm::InputTag>("photons");
    phoFix_=iConfig.getParameter<edm::InputTag>("photonsFixed");
    jets_=iConfig.getParameter<edm::InputTag>("jets");
    pCandToken_ = consumes< edm::View<pat::PackedCandidate> >(pCand_);
    phoToken_ = consumes< edm::View<pat::Photon> >(pho_);
    phoFixToken_ = consumes< edm::View<pat::Photon> >(phoFix_);
    eleToken_ = consumes< edm::View<pat::Electron> >(ele_);
    eleFixToken_ = consumes< edm::View<pat::Electron> >(eleFix_);
    JetTok_=consumes< edm::View<pat::Jet> >(jets_);
    METTok_=consumes< edm::View<pat::MET> >(MET_);
    METCorrTok_=consumes< edm::View<pat::MET> >(METFix_);
    produces<std::vector<pat::Jet> >();  
}


PatJetFix::~PatJetFix()
{
 
    // do anything here that needs to be done at destruction time
    // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PatJetFix::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
    using namespace edm;

    Handle< View< pat::PackedCandidate> > hPackedCand;
    iEvent.getByToken(pCandToken_,hPackedCand);
    Handle< View< pat::Photon> > hPhotonProduct;
    iEvent.getByToken(phoToken_,hPhotonProduct);
    Handle< View< pat::Photon> > hPhotonFixProduct;
    iEvent.getByToken(phoFixToken_,hPhotonFixProduct);
    Handle< View< pat::Electron> > hElectronProduct;
    iEvent.getByToken(eleToken_,hElectronProduct);
    Handle< View< pat::Electron> > hElectronFixProduct;
    iEvent.getByToken(eleFixToken_,hElectronFixProduct);
    Handle<edm::View<pat::MET> >PFMET;
    Handle<edm::View<pat::MET> >PFCorrMET;
    iEvent.getByToken(METTok_, PFMET);
    iEvent.getByToken(METCorrTok_, PFCorrMET);
    Handle<edm::View<pat::Jet> >PFJets;
    iEvent.getByToken(JetTok_, PFJets);

    std::auto_ptr< std::vector<pat::Jet> > patJets ( new std::vector<pat::Jet>() );
    patJets->reserve(PFJets->size());
    if(fabs((PFCorrMET->at(0).pt()-PFMET->at(0).pt()))<0.00001){
        for(auto Jet = PFJets->begin(); Jet != PFJets->end(); ++Jet){
            unsigned int idx=Jet-PFJets->begin();
            edm::RefToBase<pat::Jet> jetRef = PFJets->refAt(idx);
            pat::Jet ajet(jetRef);
            patJets->push_back(ajet);
        }
        iEvent.put(patJets);//Just a copy of the original collection
        return;
    }

    std::vector<unsigned int>ElePFParticles;
    std::vector<unsigned int >EleCorrection;
    std::vector<unsigned int>PhoPFParticles;
    std::vector<unsigned int >PhoCorrection;
    std::vector<unsigned int >PhoNominal;
    auto phoFix=hPhotonFixProduct->begin();
    auto pho=hPhotonProduct->begin();
    auto eleFix=hElectronFixProduct->begin();
    auto ele=hElectronProduct->begin();
    for(ele=hElectronProduct->begin(); ele!=hElectronProduct->end(); ++ele, ++eleFix){
        unsigned int eleindex=ele-hElectronProduct->begin();
        if(ele->energy()/eleFix->energy()>1.000001 || ele->energy()/eleFix->energy()<0.999999){
            for( const edm::Ref<pat::PackedCandidateCollection> & ref : ele->associatedPackedPFCandidates() ) {
                ElePFParticles.push_back(ref.key());
                EleCorrection.push_back(eleindex);
            }
        }
    }

    phoFix=hPhotonFixProduct->begin();
    pho=hPhotonProduct->begin();
    for(pho=hPhotonProduct->begin(); pho!=hPhotonProduct->end(); ++pho){
        unsigned int phoindex=pho-hPhotonProduct->begin();
        bool SameSC=false;
        for(unsigned int e=0; e<EleCorrection.size(); ++e){
            ele=hElectronProduct->begin();
            std::advance(ele,EleCorrection[e]);
            if(pho->superCluster()==ele->superCluster()){SameSC=true;break;}
        }
        if(!SameSC){
            unsigned int PhoFixIndex=0;//phoindex;
            float  ECorr=1;
            float dRMin=99;
            for(phoFix=hPhotonFixProduct->begin(); phoFix!=hPhotonFixProduct->end(); ++phoFix){
                float dR=sqrt((pho->eta()-phoFix->eta())*(pho->eta()-phoFix->eta())+(pho->phi()-phoFix->phi())*(pho->phi()-phoFix->phi()));
                if(phoFix->superCluster()==pho->superCluster() || dR<0.1){
                    if(dRMin>dR){
                        dRMin=dR;
                        PhoFixIndex=phoFix-hPhotonFixProduct->begin();
                        ECorr=pho->energy()/phoFix->energy();
                    }
                }
            }
            if((ECorr>1.00001 || ECorr<0.999999) && dRMin<0.1){
                for( const edm::Ref<pat::PackedCandidateCollection> & ref : pho->associatedPackedPFCandidates() ) {
                    PhoPFParticles.push_back(ref.key());
                    PhoNominal.push_back(phoindex);
                    PhoCorrection.push_back(PhoFixIndex);//not necessarily the same index
                }
            }
        }
    }
    std::vector<unsigned int> PhoFixed;
    std::vector<unsigned int> EleFixed;
    for(auto Jet = PFJets->begin(); Jet != PFJets->end(); ++Jet){
        bool EGMatch=false;
        unsigned int idx=Jet-PFJets->begin();
        edm::RefToBase<pat::Jet> jetRef = PFJets->refAt(idx);
        pat::Jet ajet(jetRef);
        int EleIndx=-1;
        int PhoIndx=-1;
        int PhoFixIndx=-1;
        for( const edm::Ptr<reco::Candidate> & ref : Jet->getJetConstituents() ) {
            std::vector<unsigned int>::iterator it = find (ElePFParticles.begin(), ElePFParticles.end(), ref.key());        
            if(it!=ElePFParticles.end()){
                std::vector<unsigned int>::iterator itFixed =find(EleFixed.begin(),EleFixed.end(),EleCorrection[it-ElePFParticles.begin()]);
                if(itFixed==EleFixed.end()){
                    EGMatch=true;
                    EleIndx=EleCorrection[it-ElePFParticles.begin()];
                    EleFixed.push_back(EleIndx);
                    break; 
                }
            }
            it = find (PhoPFParticles.begin(), PhoPFParticles.end(), ref.key()); 
            if(it!=PhoPFParticles.end()){
                std::vector<unsigned int>::iterator itFixed =find(PhoFixed.begin(),PhoFixed.end(),PhoNominal[it-PhoPFParticles.begin()]);
                if(itFixed==PhoFixed.end()){
                    EGMatch=true;
                    PhoIndx=PhoNominal[it-PhoPFParticles.begin()];
                    PhoFixed.push_back(PhoIndx);
                    PhoFixIndx=PhoCorrection[it-PhoPFParticles.begin()];
                    break;
                }
            }
        }

        if(EGMatch){
            math::XYZTLorentzVector pVecShift=ajet.p4();
            if(EleIndx>-1){
                eleFix=hElectronFixProduct->begin();
                ele=hElectronProduct->begin();
                std::advance(ele,EleIndx);
                std::advance(eleFix,EleIndx);        
                pVecShift=pVecShift+(eleFix->p4()-ele->p4());
                ajet.setP4(pVecShift);
            }
            if(PhoIndx>-1){
                phoFix=hPhotonFixProduct->begin();
                pho=hPhotonProduct->begin();
                std::advance(pho,PhoIndx);
                std::advance(phoFix,PhoFixIndx);        
                pVecShift=pVecShift+(phoFix->p4()-pho->p4());
                ajet.setP4(pVecShift);
            }
        }
        patJets->push_back(ajet);
    }
    
    iEvent.put(patJets);
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PatJetFix::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PatJetFix);
