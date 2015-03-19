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
        edm::InputTag metTag_, JetTag_, cleanTag_;
        double MinJetPt_,MaxJetEta_;	
	
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
	//register your product
	metTag_   = iConfig.getParameter<edm::InputTag> ("METTag");
	JetTag_   = iConfig.getParameter<edm::InputTag> ("JetTag");
	cleanTag_ = iConfig.getUntrackedParameter<edm::InputTag> ("cleanTag",edm::InputTag(""));
	MinJetPt_ = iConfig.getUntrackedParameter<double> ("minJetPt",30.);
	MaxJetEta_= iConfig.getUntrackedParameter<double> ("minJetEta",5.);

	produces<double>("DeltaPhiN1");
        produces<double>("DeltaPhiN2");
        produces<double>("DeltaPhiN3");
        produces<double>("minDeltaPhiN");	
	produces<double>("Pt");
	produces<double>("Phi");

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
	double metpt_=0, metphi_=0;;
	edm::Handle< edm::View<pat::MET> > MET;
	iEvent.getByLabel(metTag_,MET); 
	
	edm::Handle< edm::View<pat::Jet> > Jets;
        iEvent.getByLabel(JetTag_,Jets);
	
	edm::Handle< edm::View<reco::Candidate> > cleanCands;
	iEvent.getByLabel(cleanTag_,cleanCands);
	
	double dpnhat[3];
	unsigned int goodcount=0;
    	
	for(int i=0; i<3; ++i)dpnhat[i]=-999;
	    reco::MET::LorentzVector metLorentz(0,0,0,0);
	if(MET.isValid() ){

		metpt_=MET->at(0).pt();
		metphi_=MET->at(0).phi();
		metLorentz=MET->at(0).p4();

	}else std::cout<<"METDouble::Invlide Tag: "<<metTag_.label()<<std::endl;
	
	// loop over all reco::candidates in cleanCands
	// and remove from the MET four vector 
	if( cleanCands.isValid() ){
	 
	  for( View< reco::Candidate >::const_iterator iCand = cleanCands->begin();
	       iCand != cleanCands->end();
	       ++iCand){
	    
	    metLorentz += iCand->p4();

	  }// end loop over cleanCands

	  metpt_ = metLorentz.Pt();
	  metphi_ = metLorentz.Phi();
	  
	}
	
	std::auto_ptr<double> htp(new double(metpt_));
	iEvent.put(htp,"Pt");
	std::auto_ptr<double> htp2(new double(metphi_));
	iEvent.put(htp2,"Phi");
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

// ------------ method called once each job just after ending the event loop  ------------
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
