// -*- C++ -*-
//
// Package:    METDouble
// Class:      METDouble
//
/**\class METDouble METDouble.cc RA2Classic/METDouble/src/METDouble.cc
 *
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// March 8, 2015: Making pt & eta cut on jets configurable and adding
// the ability to pass a collection of reco::candidates to be removed
// from the MET calculation -- Andrew Whitbeck.
//
// $Id$
//
//


// system include files
#include <memory>
#include <TMath.h>
// user include files
//
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/MET.h"

//
// class declaration
//

class METDouble : public edm::global::EDProducer<> {
public:
   explicit METDouble(const edm::ParameterSet&);
   ~METDouble() override;
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   
   // ----------member data ---------------------------
   edm::InputTag metTag_, genMetTag_, puppiMetTag_, InfTagAK8_;
   edm::EDGetTokenT<edm::View<pat::MET>> metTok_, genMetTok_, puppiMetTok_;
   edm::EDGetTokenT<edm::View<pat::Jet>> InfTokAK8_;
   double MinJetPt_,MaxJetEta_;
   bool geninfo_;
   std::vector<pat::MET::METUncertainty> uncUpList, uncDownList;
};

//
// constructors and destructor
//
METDouble::METDouble(const edm::ParameterSet& iConfig)
{
   metTag_    = iConfig.getParameter<edm::InputTag> ("METTag");
   genMetTag_ = iConfig.getParameter<edm::InputTag> ("GenMETTag");
   puppiMetTag_ = iConfig.getParameter<edm::InputTag> ("PuppiMETTag");
   InfTagAK8_ = iConfig.getParameter<edm::InputTag> ("InfTagAK8");
   MinJetPt_  = iConfig.getUntrackedParameter<double> ("minJetPt",30.);
   MaxJetEta_ = iConfig.getUntrackedParameter<double> ("minJetEta",5.);
   geninfo_   = iConfig.getUntrackedParameter<bool>("geninfo",false);
   
   metTok_ = consumes<edm::View<pat::MET>>(metTag_);
   genMetTok_ = consumes<edm::View<pat::MET>>(genMetTag_);
   puppiMetTok_ = consumes<edm::View<pat::MET>>(puppiMetTag_);
   InfTokAK8_ = consumes<edm::View<pat::Jet>>(InfTagAK8_);
   
   uncUpList = {pat::MET::JetResUp, pat::MET::JetEnUp, pat::MET::MuonEnUp, pat::MET::ElectronEnUp, pat::MET::TauEnUp, pat::MET::UnclusteredEnUp, pat::MET::PhotonEnUp};
   uncDownList = {pat::MET::JetResDown, pat::MET::JetEnDown, pat::MET::MuonEnDown, pat::MET::ElectronEnDown, pat::MET::TauEnDown, pat::MET::UnclusteredEnDown, pat::MET::PhotonEnDown};
   
   //register your product
   produces<double>("Pt");
   produces<double>("Phi");
   produces<double>("RawPt");
   produces<double>("RawPhi");
   produces<double>("CaloPt");
   produces<double>("CaloPhi");
   produces<double>("GenPt");
   produces<double>("GenPhi");
   produces<double>("PuppiPt");
   produces<double>("PuppiPhi");
   produces<double>("PFCaloPtRatio");
   produces<double>("Significance");

   produces<std::vector<double> >("PtUp");
   produces<std::vector<double> >("PtDown");
   produces<std::vector<double> >("PhiUp");
   produces<std::vector<double> >("PhiDown");
   produces<std::vector<double> >("PuppiPtUp");
   produces<std::vector<double> >("PuppiPtDown");
   produces<std::vector<double> >("PuppiPhiUp");
   produces<std::vector<double> >("PuppiPhiDown");
}


METDouble::~METDouble()
{
   
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
   
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
METDouble::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;
   double metpt_=0, metphi_=0;
   double rawmetpt_=0, rawmetphi_=0;
   double genmetpt_=0, genmetphi_=0;
   double calometpt_=0, calometphi_=0;
   double puppimetpt_=0, puppimetphi_=0;
   double metsig_=0;

   std::vector<double> metPtUp_(uncUpList.size(),0.);
   std::vector<double> metPhiUp_(uncUpList.size(),0.);
   std::vector<double> metPtDown_(uncDownList.size(),0.);
   std::vector<double> metPhiDown_(uncDownList.size(),0.);

   std::vector<double> puppiPtUp_(uncUpList.size(),0.);
   std::vector<double> puppiPhiUp_(uncUpList.size(),0.);
   std::vector<double> puppiPtDown_(uncDownList.size(),0.);
   std::vector<double> puppiPhiDown_(uncDownList.size(),0.);

   edm::Handle< edm::View<pat::MET> > MET;
   iEvent.getByToken(metTok_,MET);

   edm::Handle< edm::View<pat::MET> > GenMET;
   iEvent.getByToken(genMetTok_,GenMET);

   edm::Handle< edm::View<pat::MET> > PuppiMET;
   iEvent.getByToken(puppiMetTok_,PuppiMET);

   double dpnhat[3];

   for(double & i : dpnhat)i=-999;
   if(MET.isValid() ){
      metpt_=MET->at(0).pt();
      metphi_=MET->at(0).phi();
      metsig_=MET->at(0).metSignificance();

      for(unsigned u = 0; u < uncUpList.size(); ++u){
        metPtUp_[u] = MET->at(0).shiftedPt(uncUpList[u], pat::MET::Type1);
        metPtDown_[u] = MET->at(0).shiftedPt(uncDownList[u], pat::MET::Type1);
        metPhiUp_[u] = MET->at(0).shiftedPhi(uncUpList[u], pat::MET::Type1);
        metPhiDown_[u] = MET->at(0).shiftedPhi(uncDownList[u], pat::MET::Type1);
      }

      rawmetpt_=MET->at(0).uncorPt();
      rawmetphi_=MET->at(0).uncorPhi();
   }
   else edm::LogWarning("TreeMaker")<<"METDouble::Invalid Tag: "<<metTag_;

   if(PuppiMET.isValid() ){
      puppimetpt_=PuppiMET->at(0).pt();
      puppimetphi_=PuppiMET->at(0).phi();

      for(unsigned u = 0; u < uncUpList.size(); ++u){
        puppiPtUp_[u] = PuppiMET->at(0).shiftedPt(uncUpList[u], pat::MET::Type1);
        puppiPtDown_[u] = PuppiMET->at(0).shiftedPt(uncDownList[u], pat::MET::Type1);
        puppiPhiUp_[u] = PuppiMET->at(0).shiftedPhi(uncUpList[u], pat::MET::Type1);
        puppiPhiDown_[u] = PuppiMET->at(0).shiftedPhi(uncDownList[u], pat::MET::Type1);
      }
   }
   else edm::LogWarning("TreeMaker")<<"METDouble::Invalid Tag: "<<puppiMetTag_;

   //GenMET is really the original MET collection from the event (re-correction zeroes out some values)
   if(GenMET.isValid()){
      if(geninfo_ && GenMET->at(0).genMET()){
        const reco::GenMET* theGenMET( GenMET->at(0).genMET () ) ;
        genmetpt_     = theGenMET->pt  ();
        genmetphi_    = theGenMET->phi ();
      }
      calometpt_=GenMET->at(0).caloMETPt();
      calometphi_=GenMET->at(0).caloMETPhi();      
   }
   else if(!GenMET.isValid()) edm::LogWarning("TreeMaker")<<"METDouble::Invalid Tag: "<<genMetTag_;
   
   auto htp = std::make_unique<double>(metpt_);
   iEvent.put(std::move(htp),"Pt");
   auto htp2 = std::make_unique<double>(metphi_);
   iEvent.put(std::move(htp2),"Phi");
   auto htp0 = std::make_unique<double>(metsig_);
   iEvent.put(std::move(htp0),"Significance");

   auto rhtp = std::make_unique<double>(rawmetpt_);
   iEvent.put(std::move(rhtp),"RawPt");
   auto rhtp2 = std::make_unique<double>(rawmetphi_);
   iEvent.put(std::move(rhtp2),"RawPhi");

   auto chtp = std::make_unique<double>(calometpt_);
   iEvent.put(std::move(chtp),"CaloPt");
   auto chtp2 = std::make_unique<double>(calometphi_);
   iEvent.put(std::move(chtp2),"CaloPhi");

   auto phtp = std::make_unique<double>(puppimetpt_);
   iEvent.put(std::move(phtp),"PuppiPt");
   auto phtp2 = std::make_unique<double>(puppimetphi_);
   iEvent.put(std::move(phtp2),"PuppiPhi");

   double ratio = metpt_/calometpt_;
   double ratio_inf = 0.;
   edm::Handle<edm::View<pat::Jet>> InfAK8;
   iEvent.getByToken(InfTokAK8_,InfAK8);
   if(InfAK8.isValid() and InfAK8->size()>0) ratio_inf -= 8;
   auto chtp3 = std::make_unique<double>(ratio_inf<0 ? ratio_inf : ratio);
   iEvent.put(std::move(chtp3),"PFCaloPtRatio");

   if(geninfo_){
       auto ghtp = std::make_unique<double>(genmetpt_);
       iEvent.put(std::move(ghtp),"GenPt");
       auto ghtp2 = std::make_unique<double>(genmetphi_);
       iEvent.put(std::move(ghtp2),"GenPhi");

       auto uncp1 = std::make_unique<std::vector<double>>(metPtUp_);
       iEvent.put(std::move(uncp1),"PtUp");
       auto uncp2 = std::make_unique<std::vector<double>>(metPtDown_);
       iEvent.put(std::move(uncp2),"PtDown");
       auto uncp3 = std::make_unique<std::vector<double>>(metPhiUp_);
       iEvent.put(std::move(uncp3),"PhiUp");
       auto uncp4 = std::make_unique<std::vector<double>>(metPhiDown_);
       iEvent.put(std::move(uncp4),"PhiDown");

       auto puncp1 = std::make_unique<std::vector<double>>(puppiPtUp_);
       iEvent.put(std::move(puncp1),"PuppiPtUp");
       auto puncp2 = std::make_unique<std::vector<double>>(puppiPtDown_);
       iEvent.put(std::move(puncp2),"PuppiPtDown");
       auto puncp3 = std::make_unique<std::vector<double>>(puppiPhiUp_);
       iEvent.put(std::move(puncp3),"PuppiPhiUp");
       auto puncp4 = std::make_unique<std::vector<double>>(puppiPhiDown_);
       iEvent.put(std::move(puncp4),"PuppiPhiDown");
   }
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
METDouble::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(METDouble);
