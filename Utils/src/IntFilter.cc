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
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"

//
// class declaration
//

class IntFilter : public edm::global::EDFilter<> {
public:
	explicit IntFilter(const edm::ParameterSet&);
	~IntFilter() override;
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	bool filter(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
	// ----------member data ---------------------------
	
	edm::InputTag IntTag_;
	edm::EDGetTokenT<int> IntTok_;
	double CutValue_;
	int CutType_;
};

//
// constructors and destructor
//
IntFilter::IntFilter(const edm::ParameterSet& iConfig)
{
	//now do what ever initialization is needed
	IntTag_ = iConfig.getParameter<edm::InputTag>("IntTag");
	CutValue_ = iConfig.getParameter <double> ("CutValue");
	CutType_ = iConfig.getParameter <int> ("CutType");
	IntTok_ = consumes<int>(IntTag_);
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
IntFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	edm::Handle<int> var;	
	iEvent.getByToken(IntTok_,var);
	if(CutType_==0)
	{
	  if(*var<CutValue_) return false;
	}
	else if(CutType_==1){
	  
	  if(*var>CutValue_) return false;
	}
	else if(CutType_==2){
	  
	  if(*var<=CutValue_) return false;
	  }
	else if(CutType_==3){
	  
	  if(*var>=CutValue_) return false;
	  }
	else edm::LogWarning("TreeMaker")<<"IntFilter: CutType: "<<CutType_<<" not defined!";
	
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
