// -*- C++ -*-
//
// Package:    IntFilter
// Class:      IntFilter
// 
/**\class IntFilter IntFilter.cc RA2Classic/IntFilter/src/IntFilter.cc
 * 
 D escription: [one line class s*u*mmary]
 
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,,,uni-hamburg
//         Created:  Mon Oct 22 11:46:48 CEST 2012
// $Id: IntFilter.cc,v 1.2 2012/11/19 14:23:04 adraeger Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "FWCore/Utilities/interface/EDMException.h"


#include <DataFormats/PatCandidates/interface/Jet.h>
#include <DataFormats/PatCandidates/interface/MET.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/Electron.h>
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TH2.h"
#include <utility>
#include <vector>
#include "TString.h"
#include "TTree.h"

#include "DataFormats/Candidate/interface/CandMatchMap.h"

//
// class declaration
//

class IntFilter : public edm::EDFilter {
public:
	explicit IntFilter(const edm::ParameterSet&);
	~IntFilter();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual bool filter(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual bool beginRun(edm::Run&, edm::EventSetup const&);
	virtual bool endRun(edm::Run&, edm::EventSetup const&);
	virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	
	// ----------member data ---------------------------
	
	edm::InputTag IntTag_;
	double CutValue_;
	int CutTyp_;
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
IntFilter::IntFilter(const edm::ParameterSet& iConfig)
{
	//now do what ever initialization is needed
	IntTag_ = iConfig.getParameter<edm::InputTag>("IntTag");
	CutValue_ = iConfig.getParameter <double> ("CutValue");
	CutTyp_ = iConfig.getParameter <int> ("CutTyp");
}


IntFilter::~IntFilter()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
IntFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	edm::Handle<int> var;	
	iEvent.getByLabel(IntTag_,var);
	if(CutTyp_==0)
	{
	  if(*var<CutValue_) return false;
	}
	else if(CutTyp_==1){
	  
	  if(*var>CutValue_) return false;
	}
	else if(CutTyp_==2){
	  
	  if(*var<=CutValue_) return false;
	  }
	else if(CutTyp_==3){
	  
	  if(*var>=CutValue_) return false;
	  }
	else std::cout<<"IntFilter: CutTyp: "<<CutTyp_<<" not defined!"<<std::endl;
	
	return true;
}

// ------------ method called once each job just before starting event loop  ------------
void 
IntFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
IntFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
IntFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
	return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
IntFilter::endRun(edm::Run&, edm::EventSetup const&)
{
	return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
IntFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
	return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
IntFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
	return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
IntFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(IntFilter);