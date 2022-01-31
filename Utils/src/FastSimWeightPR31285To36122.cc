// -*- C++ -*-
// Package:    TreeMaker
// Class:      FastSimWeightPR31285To36122
// Authors:   Sam Bein 
//         Created:  Wed March 7, 2014
//         Modified: Thurs March 3, 2021
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
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"
//#include "TLorentzVector.h"
#include <vector>
class FastSimWeightPR31285To36122 : public edm::global::EDProducer<> {
public:
    explicit FastSimWeightPR31285To36122(const edm::ParameterSet&);
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
    // ----------member data ---------------------------
    edm::InputTag genCollection;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> genCollectionTok;
    edm::InputTag genJetTag;
    edm::EDGetTokenT<edm::View<reco::GenJet>> genJetTok;    
    edm::InputTag recJetTag;
    edm::EDGetTokenT<edm::View<pat::Jet>> recJetTok;
   TH1F *hRatio_GenJetHadronPtGenJetHadronFlavorLt4;
   TH1F *hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4;
   TH1F *hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5;
   TAxis * xax;
};
FastSimWeightPR31285To36122::FastSimWeightPR31285To36122(const edm::ParameterSet& iConfig):
  genCollection(iConfig.getParameter<edm::InputTag>("genCollection")),
  genCollectionTok(consumes<edm::View<reco::GenParticle>>(genCollection)),
  genJetTag(iConfig.getParameter<edm::InputTag>("genJetTag")),
  genJetTok(consumes<edm::View<reco::GenJet>>(genJetTag)),
  recJetTag(iConfig.getParameter<edm::InputTag>("recJetTag")),
  recJetTok(consumes<edm::View<pat::Jet>>(recJetTag))  
{
   produces< double >();   
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4 = new TH1F("hRatio_GenJetHadronPtGenJetHadronFlavorLt4","",20,0,500);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(1,1.001089);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(2,1.015741);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(3,1.041511);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(4,1.060358);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(5,1.067062);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(6,1.075163);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(7,1.048214);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(8,1.068493);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(9,1.080569);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(10,1.056338);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(11,1.036364);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(12,1.014925);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(13,1.045455);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(14,1.125);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(15,1.095238);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(16,1);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(17,1.083333);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(18,1.142857);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(19,1);
   hRatio_GenJetHadronPtGenJetHadronFlavorLt4->SetBinContent(20,1.034483);
   xax = (TAxis*)hRatio_GenJetHadronPtGenJetHadronFlavorLt4->GetXaxis();
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4 = new TH1F("hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4","",20,0,500);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(1,1.013215);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(2,1.040373);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(3,1.107982);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(4,1.1659);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(5,1.233415);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(6,1.330198);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(7,1.406657);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(8,1.551876);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(9,1.558824);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(10,1.715789);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(11,1.685714);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(12,1.911392);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(13,2.212766);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(14,1.926829);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(15,2.166667);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(16,1.962963);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(17,3.125);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(18,2.625);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(19,3);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->SetBinContent(20,2.2);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5 = new TH1F("hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5","",20,0,500);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(1,1.010584);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(2,1.01473);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(3,1.071903);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(4,1.192592);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(5,1.332403);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(6,1.573248);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(7,1.732668);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(8,2.013557);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(9,2.270501);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(10,2.578063);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(11,2.806123);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(12,3.175);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(13,3.385366);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(14,3.609589);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(15,4.896341);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(16,4.672131);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(17,5.119048);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(18,5.574074);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(19,6.516129);
   hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->SetBinContent(20,7.685393);  
}
// ------------ method called for each event  ------------
void FastSimWeightPR31285To36122::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
    using namespace edm;
    double EventWeight = 1.0;    
    edm::Handle< View<reco::GenParticle> > genPartCands;
    iEvent.getByToken(genCollectionTok, genPartCands);
    edm::Handle< View<reco::GenJet> > genJets;
    iEvent.getByToken(genJetTok, genJets);
    edm::Handle< View<pat::Jet> > recJets;
    iEvent.getByToken(recJetTok, recJets);   
    bool jetHasOffendingGp_;
    float dr;    
    float mindr;
    double leadHadronPt;
    float originxy;   
    float decayxy;       
    int hadronFlavor;     
    int pdgid;
    float genJetPtThreshold = 30;
    float genParticlePtThreshold = 15;
    float drThreshold = 0.4;
    float justInsidePipe = 2.16;
    float justOutsidePipe = 2.17;
    float farOutsideCaloButNotTooFarAway = 2000;
    
    for(const auto& genJet : *genJets) 
    {
           if (!(genJet.pt()>genJetPtThreshold)) continue;
           jetHasOffendingGp_ = false;//must use
           mindr = 99;
           hadronFlavor = -11;
           leadHadronPt = 1;
           originxy = -1;
           for(const auto& recJet : *recJets) 
            {
                dr = deltaR(recJet.p4(),genJet.p4());
                if (!(dr<drThreshold && dr<mindr)) continue;
                mindr = dr;
                hadronFlavor = std::max(1,recJet.hadronFlavour());
                for(const auto& iPart : *genPartCands) {
                    if (!(iPart.pt()>genParticlePtThreshold)) continue;
                    pdgid = abs(iPart.pdgId());
                    if (!(deltaR(iPart,genJet)<drThreshold)) continue;
                    if(!(pdgid>100 && pdgid<600)) continue; //only consider hadrons
                    if (iPart.pt()>leadHadronPt) {
                        if ( (hadronFlavor<4 && pdgid>100 && pdgid<400) ||//only consider hadrons
                             (hadronFlavor==4 && pdgid>400 && pdgid<500) ||//only consider hadrons
                             (hadronFlavor==5 && pdgid>400 && pdgid<600) )//only consider hadrons
                        {
                            leadHadronPt = iPart.pt();
                        }
                    }                       
                    if(!(iPart.numberOfDaughters()>1)) continue;
                    originxy = sqrt(pow(iPart.vx(),2) + pow(iPart.vy(),2));
                    if(!(originxy<justInsidePipe)) continue;
                    decayxy = sqrt(pow(iPart.daughter(0)->vx(),2) + pow(iPart.daughter(0)->vy(),2));
                    if (decayxy>justOutsidePipe and decayxy<farOutsideCaloButNotTooFarAway)
                    {
                        jetHasOffendingGp_ = true;
                        break;
                    }
                }
            }
            leadHadronPt = xax->GetBinLowEdge(xax->FindBin(std::min(leadHadronPt, 498.)));
            if (jetHasOffendingGp_)
            {
                EventWeight*=0;
            }
            else
            {
               if (hadronFlavor<4) EventWeight*=hRatio_GenJetHadronPtGenJetHadronFlavorLt4->Interpolate(leadHadronPt);
               else if (hadronFlavor==4) EventWeight*=hRatio_GenJetHadronPtGenJetHadronFlavorEqEq4->Interpolate(leadHadronPt);
               else if (hadronFlavor==5) EventWeight*=hRatio_GenJetHadronPtGenJetHadronFlavorEqEq5->Interpolate(leadHadronPt);           
            }
        }
        auto EventWeight_double = std::make_unique<double>(EventWeight);
        iEvent.put(std::move(EventWeight_double));
}
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void FastSimWeightPR31285To36122::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}
#include "FWCore/Framework/interface/MakerMacros.h"
//define this as a plug-in
DEFINE_FWK_MODULE(FastSimWeightPR31285To36122);