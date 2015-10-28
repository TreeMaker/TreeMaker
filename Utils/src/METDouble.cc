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
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/MET.h"

//
// class declaration
//

class METDouble : public edm::EDProducer {
public:
   explicit METDouble(const edm::ParameterSet&);
   ~METDouble();
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   virtual void beginJob() ;
   virtual void produce(edm::Event&, const edm::EventSetup&);
   virtual double DeltaT(unsigned int i, edm::Handle< edm::View<pat::Jet> > Jets );
   virtual void endJob() ;
   
   virtual void beginRun(edm::Run&, edm::EventSetup const&);
   virtual void endRun(edm::Run&, edm::EventSetup const&);
   virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   edm::InputTag metTag_, genMetTag_, JetTag_;
   std::vector<edm::InputTag> cleanTag_;
   double MinJetPt_,MaxJetEta_;
   bool geninfo_;
   
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
METDouble::METDouble(const edm::ParameterSet& iConfig)
{
   metTag_    = iConfig.getParameter<edm::InputTag> ("METTag");
   genMetTag_ = iConfig.getParameter<edm::InputTag> ("GenMETTag");
   JetTag_    = iConfig.getParameter<edm::InputTag> ("JetTag");
   cleanTag_  = iConfig.getUntrackedParameter<std::vector<edm::InputTag>>("cleanTag");
   MinJetPt_  = iConfig.getUntrackedParameter<double> ("minJetPt",30.);
   MaxJetEta_ = iConfig.getUntrackedParameter<double> ("minJetEta",5.);
   geninfo_   = iConfig.getUntrackedParameter<bool>("geninfo",false);
   
   //register your product
   produces<double>("DeltaPhiN1");
   produces<double>("DeltaPhiN2");
   produces<double>("DeltaPhiN3");
   produces<double>("minDeltaPhiN");
   produces<double>("Pt");
   produces<double>("Phi");
   produces<double>("CaloPt");
   produces<double>("CaloPhi");
   produces<double>("GenPt");
   produces<double>("GenPhi");

   produces<double>("metType1PtJetResUp");           
   produces<double>("metType1PtJetResDown");      
   produces<double>("metType1PtJetEnUp");         
   produces<double>("metType1PtJetEnDown");       
   produces<double>("metType1PtMuonEnUp");        
   produces<double>("metType1PtMuonEnDown");      
   produces<double>("metType1PtElectronEnUp");    
   produces<double>("metType1PtElectronEnDown");  
   produces<double>("metType1PtTauEnUp");	      
   produces<double>("metType1PtTauEnDown");       
   produces<double>("metType1PtUnclusteredEnUp"); 
   produces<double>("metType1PtUnclusteredEnDown");
   produces<double>("metType1PtPhotonEnUp");      
   produces<double>("metType1PtPhotonEnDown");    
 
   produces<double>("metType1PhiJetResUp");       
   produces<double>("metType1PhiJetResDown");     
   produces<double>("metType1PhiJetEnUp");        
   produces<double>("metType1PhiJetEnDown");        
   produces<double>("metType1PhiMuonEnUp");       
   produces<double>("metType1PhiMuonEnDown");     
   produces<double>("metType1PhiElectronEnUp");     
   produces<double>("metType1PhiElectronEnDown");       
   produces<double>("metType1PhiTauEnUp");        
   produces<double>("metType1PhiTauEnDown");        
   produces<double>("metType1PhiUnclusteredEnUp");      
   produces<double>("metType1PhiUnclusteredEnDown");	      
   produces<double>("metType1PhiPhotonEnUp");       
   produces<double>("metType1PhiPhotonEnDown");     

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
METDouble::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   double metpt_=0, metphi_=0;
   double genmetpt_=0, genmetphi_=0;
   double calometpt_=0, calometphi_=0;


   double metType1PtJetResUp_ = 0.;           
   double metType1PtJetResDown_ = 0.;   
   double metType1PtJetEnUp_ = 0.;      
   double metType1PtJetEnDown_ = 0.;    
   double metType1PtMuonEnUp_ = 0.;     
   double metType1PtMuonEnDown_ = 0.;   
   double metType1PtElectronEnUp_ = 0.; 
   double metType1PtElectronEnDown_ = 0.;     
   double metType1PtTauEnUp_ = 0.;	           
   double metType1PtTauEnDown_ = 0.;          
   double metType1PtUnclusteredEnUp_ = 0.;    
   double metType1PtUnclusteredEnDown_ = 0.;  
   double metType1PtPhotonEnUp_ = 0.;         
   double metType1PtPhotonEnDown_ = 0.;       	     
      
   double metType1PhiJetResUp_ = 0.;          
   double metType1PhiJetResDown_ = 0.;        
   double metType1PhiJetEnUp_ = 0.;           
   double metType1PhiJetEnDown_ = 0.;         
   double metType1PhiMuonEnUp_ = 0.;          
   double metType1PhiMuonEnDown_ = 0.;        
   double metType1PhiElectronEnUp_ = 0.;      
   double metType1PhiElectronEnDown_ = 0.;        
   double metType1PhiTauEnUp_ = 0.;           
   double metType1PhiTauEnDown_ = 0.;         
   double metType1PhiUnclusteredEnUp_ = 0.;       
   double metType1PhiUnclusteredEnDown_ = 0.;     
   double metType1PhiPhotonEnUp_ = 0.;        
   double metType1PhiPhotonEnDown_ = 0.;   
   
   edm::Handle< edm::View<pat::MET> > MET;
   iEvent.getByLabel(metTag_,MET);

   edm::Handle< edm::View<pat::MET> > GenMET;
   iEvent.getByLabel(genMetTag_,GenMET);
   
   edm::Handle< edm::View<pat::Jet> > Jets;
   iEvent.getByLabel(JetTag_,Jets);
   
   double dpnhat[3];
   unsigned int goodcount=0;
   
   for(int i=0; i<3; ++i)dpnhat[i]=-999;
   reco::MET::LorentzVector metLorentz(0,0,0,0);
   if(MET.isValid() ){
      
      metpt_=MET->at(0).pt();
      metphi_=MET->at(0).phi();
      metLorentz=MET->at(0).p4();
	  
      metType1PtJetResUp_  = MET->at(0).shiftedPt(pat::MET::JetResUp, pat::MET::Type1);
      metType1PtJetResDown_ = MET->at(0).shiftedPt(pat::MET::JetResDown, pat::MET::Type1);
      metType1PtJetEnUp_   = MET->at(0).shiftedPt(pat::MET::JetEnUp, pat::MET::Type1);
      metType1PtJetEnDown_  = MET->at(0).shiftedPt(pat::MET::JetEnDown, pat::MET::Type1);
      metType1PtMuonEnUp_  = MET->at(0).shiftedPt(pat::MET::MuonEnUp, pat::MET::Type1);
      metType1PtMuonEnDown_ = MET->at(0).shiftedPt(pat::MET::MuonEnDown, pat::MET::Type1);
      metType1PtElectronEnUp_      = MET->at(0).shiftedPt(pat::MET::ElectronEnUp, pat::MET::Type1);
      metType1PtElectronEnDown_     = MET->at(0).shiftedPt(pat::MET::ElectronEnDown, pat::MET::Type1);
      metType1PtTauEnUp_   = MET->at(0).shiftedPt(pat::MET::TauEnUp, pat::MET::Type1);
      metType1PtTauEnDown_  = MET->at(0).shiftedPt(pat::MET::TauEnDown, pat::MET::Type1);
      metType1PtUnclusteredEnUp_    = MET->at(0).shiftedPt(pat::MET::UnclusteredEnUp, pat::MET::Type1);
      metType1PtUnclusteredEnDown_  = MET->at(0).shiftedPt(pat::MET::UnclusteredEnDown, pat::MET::Type1);
      metType1PtPhotonEnUp_ = MET->at(0).shiftedPt(pat::MET::PhotonEnUp, pat::MET::Type1);
      metType1PtPhotonEnDown_       = MET->at(0).shiftedPt(pat::MET::PhotonEnDown, pat::MET::Type1);

      metType1PhiJetResUp_  = MET->at(0).shiftedPhi(pat::MET::JetResUp, pat::MET::Type1);
      metType1PhiJetResDown_        = MET->at(0).shiftedPhi(pat::MET::JetResDown, pat::MET::Type1);
      metType1PhiJetEnUp_ = MET->at(0).shiftedPhi(pat::MET::JetEnUp, pat::MET::Type1);	      
      metType1PhiJetEnDown_ = MET->at(0).shiftedPhi(pat::MET::JetEnDown, pat::MET::Type1);	      
      metType1PhiMuonEnUp_  = MET->at(0).shiftedPhi(pat::MET::MuonEnUp, pat::MET::Type1);	      
      metType1PhiMuonEnDown_        = MET->at(0).shiftedPhi(pat::MET::MuonEnDown, pat::MET::Type1);	 
      metType1PhiElectronEnUp_      = MET->at(0).shiftedPhi(pat::MET::ElectronEnUp, pat::MET::Type1);	      
      metType1PhiElectronEnDown_    = MET->at(0).shiftedPhi(pat::MET::ElectronEnDown, pat::MET::Type1);	      
      metType1PhiTauEnUp_ = MET->at(0).shiftedPhi(pat::MET::TauEnUp, pat::MET::Type1);	      
      metType1PhiTauEnDown_ = MET->at(0).shiftedPhi(pat::MET::TauEnDown, pat::MET::Type1);	      
      metType1PhiUnclusteredEnUp_   = MET->at(0).shiftedPhi(pat::MET::UnclusteredEnUp, pat::MET::Type1);	      
      metType1PhiUnclusteredEnDown_ = MET->at(0).shiftedPhi(pat::MET::UnclusteredEnDown, pat::MET::Type1);	      
      metType1PhiPhotonEnUp_        = MET->at(0).shiftedPhi(pat::MET::PhotonEnUp, pat::MET::Type1);	      
      metType1PhiPhotonEnDown_      = MET->at(0).shiftedPhi(pat::MET::PhotonEnDown, pat::MET::Type1);	      
	  
   }
   else std::cout<<"METDouble::Invalid Tag: "<<metTag_.label()<<std::endl;

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
   else if(!GenMET.isValid()) std::cout<<"METDouble::Invalid Tag: "<<genMetTag_.label()<<std::endl;
 
   
   // remove particles from MET calculation
   // cleanTag_ is a vector of edm::InputTag
   if (cleanTag_.size()) {
      // loop over each edm::InputTag
      for (std::vector<edm::InputTag>::const_iterator iC = cleanTag_.begin(); iC != cleanTag_.end(); ++iC) {
         // get each collection the edm::InputTag corresponds to
         edm::Handle<edm::View<reco::Candidate>> cleanCands;
         iEvent.getByLabel(*iC, cleanCands);
         if (cleanCands.isValid()) {
            // for each element in the collection add the p4 back in to the MET
            for (View<reco::Candidate>::const_iterator iCand = cleanCands->begin(); iCand != cleanCands->end(); ++iCand) {
               metLorentz += iCand->p4();
            }
         }
      }
      metpt_ = metLorentz.Pt();
      metphi_ = metLorentz.Phi();
   }
   
   std::auto_ptr<double> htp(new double(metpt_));
   iEvent.put(htp,"Pt");
   std::auto_ptr<double> htp2(new double(metphi_));
   iEvent.put(htp2,"Phi");

   std::auto_ptr<double> chtp(new double(calometpt_));
   iEvent.put(chtp,"CaloPt");
   std::auto_ptr<double> chtp2(new double(calometphi_));
   iEvent.put(chtp2,"CaloPhi");

   if(geninfo_){
       std::auto_ptr<double> ghtp(new double(genmetpt_));
       iEvent.put(ghtp,"GenPt");
       std::auto_ptr<double> ghtp2(new double(genmetphi_));
       iEvent.put(ghtp2,"GenPhi");

       std::auto_ptr<double> uncp1(new double(metType1PtJetResUp_));           
       iEvent.put(uncp1,"metType1PtJetResUp");
       std::auto_ptr<double> uncp2(new double(metType1PtJetResDown_));   
       iEvent.put(uncp2,"metType1PtJetResDown");
       std::auto_ptr<double> uncp3(new double(metType1PtJetEnUp_));      
       iEvent.put(uncp3,"metType1PtJetEnUp");
       std::auto_ptr<double> uncp4(new double(metType1PtJetEnDown_));    
       iEvent.put(uncp4,"metType1PtJetEnDown");
       std::auto_ptr<double> uncp5(new double(metType1PtMuonEnUp_));     
       iEvent.put(uncp5,"metType1PtMuonEnUp");
       std::auto_ptr<double> uncp6(new double(metType1PtMuonEnDown_));   
       iEvent.put(uncp6,"metType1PtMuonEnDown");
       std::auto_ptr<double> uncp7(new double(metType1PtElectronEnUp_)); 
       iEvent.put(uncp7,"metType1PtElectronEnUp");
       std::auto_ptr<double> uncp8(new double(metType1PtElectronEnDown_));     
       iEvent.put(uncp8,"metType1PtElectronEnDown");
       std::auto_ptr<double> uncp9(new double(metType1PtTauEnUp_));	           
       iEvent.put(uncp9,"metType1PtTauEnUp");
       std::auto_ptr<double> uncp10(new double(metType1PtTauEnDown_));          
       iEvent.put(uncp10,"metType1PtTauEnDown");
       std::auto_ptr<double> uncp11(new double(metType1PtUnclusteredEnUp_));    
       iEvent.put(uncp11,"metType1PtUnclusteredEnUp");
       std::auto_ptr<double> uncp12(new double(metType1PtUnclusteredEnDown_));  
       iEvent.put(uncp12,"metType1PtUnclusteredEnDown");
       std::auto_ptr<double> uncp13(new double(metType1PtPhotonEnUp_));         
       iEvent.put(uncp13,"metType1PtPhotonEnUp");
       std::auto_ptr<double> uncp14(new double(metType1PtPhotonEnDown_));       	     
       iEvent.put(uncp14,"metType1PtPhotonEnDown");
      
       std::auto_ptr<double> uncp15(new double(metType1PhiJetResUp_));          
       iEvent.put(uncp15,"metType1PhiJetResUp");
       std::auto_ptr<double> uncp16(new double(metType1PhiJetResDown_));        
       iEvent.put(uncp16,"metType1PhiJetResDown");
       std::auto_ptr<double> uncp17(new double(metType1PhiJetEnUp_));           
       iEvent.put(uncp17,"metType1PhiJetEnUp");
       std::auto_ptr<double> uncp18(new double(metType1PhiJetEnDown_));         
       iEvent.put(uncp18,"metType1PhiJetEnDown");
       std::auto_ptr<double> uncp19(new double(metType1PhiMuonEnUp_));          
       iEvent.put(uncp19,"metType1PhiMuonEnUp");
       std::auto_ptr<double> uncp20(new double(metType1PhiMuonEnDown_));        
       iEvent.put(uncp20,"metType1PhiMuonEnDown");
       std::auto_ptr<double> uncp21(new double(metType1PhiElectronEnUp_));      
       iEvent.put(uncp21,"metType1PhiElectronEnUp");
       std::auto_ptr<double> uncp22(new double(metType1PhiElectronEnDown_));        
       iEvent.put(uncp22,"metType1PhiElectronEnDown");
       std::auto_ptr<double> uncp23(new double(metType1PhiTauEnUp_));           
       iEvent.put(uncp23,"metType1PhiTauEnUp");
       std::auto_ptr<double> uncp24(new double(metType1PhiTauEnDown_));         
       iEvent.put(uncp24,"metType1PhiTauEnDown");
       std::auto_ptr<double> uncp25(new double(metType1PhiUnclusteredEnUp_));       
       iEvent.put(uncp25,"metType1PhiUnclusteredEnUp");
       std::auto_ptr<double> uncp26(new double(metType1PhiUnclusteredEnDown_));     
       iEvent.put(uncp26,"metType1PhiUnclusteredEnDown");
       std::auto_ptr<double> uncp27(new double(metType1PhiPhotonEnUp_));        
       iEvent.put(uncp27,"metType1PhiPhotonEnUp");
       std::auto_ptr<double> uncp28(new double(metType1PhiPhotonEnDown_));   
       iEvent.put(uncp28,"metType1PhiPhotonEnDown");
   }

   if( Jets.isValid() ) {
      for(unsigned int i=0; i<Jets->size();i++){
         if(goodcount<3 && Jets->at(i).pt()>MinJetPt_ && fabs( Jets->at(i).eta() ) < MaxJetEta_ ){
            float dphi=std::abs(reco::deltaPhi(Jets->at(i).phi(),metLorentz.phi()));
            float dT=DeltaT(i, Jets);
            if(dT/metLorentz.pt()>=1.0)dpnhat[goodcount]=dphi/(TMath::Pi()/2.0);
            else dpnhat[goodcount]=dphi/asin(dT/metLorentz.pt());
            ++goodcount;
         }
      }// end loop over jets
   }// end Jets.isValid()
   std::auto_ptr<double> htp3(new double(dpnhat[0]));
   iEvent.put(htp3,"DeltaPhiN1");
   std::auto_ptr<double> htp4(new double(dpnhat[1]));
   iEvent.put(htp4,"DeltaPhiN2");
   std::auto_ptr<double> htp5(new double(dpnhat[2]));
   iEvent.put(htp5,"DeltaPhiN3");
   float mindpn=9999;
   for(int i=0; i<3; ++i){
      if(mindpn>fabs(dpnhat[i]))mindpn=fabs(dpnhat[i]);
   }
   std::auto_ptr<double> htp6(new double(mindpn));
   iEvent.put(htp6,"minDeltaPhiN");
}

// ------------ method called once each job just before starting event loop  ------------
void
METDouble::beginJob()
{
}

// ------------ helper method to calculate DeltaT ------------
double METDouble::DeltaT(unsigned int i, edm::Handle< edm::View<pat::Jet> > Jets ){
   
   double deltaT=0;
   float jres=0.1;
   double sum=0;
   if( Jets.isValid() ) {
      for(unsigned int j=0; j<Jets->size(); ++j){
         if(j==i)continue;
         sum=sum+(Jets->at(i).px()*Jets->at(j).py()-Jets->at(j).px()*Jets->at(i).py()) * (Jets->at(i).px()*Jets->at(j).py()-Jets->at(j).px()*Jets->at(i).py());
      }
      deltaT=jres*sqrt(sum)/Jets->at(i).pt();
      
   }
   
   return deltaT;
}

// ------------ method called once each job just after ending the event loop  ------------
void
METDouble::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
METDouble::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
METDouble::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
METDouble::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
METDouble::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
