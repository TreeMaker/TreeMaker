// -*- C++ -*-
//
// Package:    DoubleFilter
// Class:      DoubleFilter
// 
/**\class DoubleFilter DoubleFilter.cc RA2Classic/DoubleFilter/src/DoubleFilter.cc
 * 
 D escription: [one line class s*u*mmary]
 
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,,,uni-hamburg
//         Created:  Mon Oct 22 11:46:48 CEST 2012
// $Id: DoubleFilter.cc,v 1.2 2012/11/19 14:23:04 adraeger Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//
// class declaration
//

class DoubleFilter : public edm::global::EDFilter<> {
public:
	explicit DoubleFilter(const edm::ParameterSet&);
	~DoubleFilter();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual bool filter(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
	// ----------member data ---------------------------
	edm::InputTag DoubleTag_;
	edm::EDGetTokenT<double> DoubleTok_;
	double CutValue_;
};

//
// constructors and destructor
//
DoubleFilter::DoubleFilter(const edm::ParameterSet& iConfig)
{
	//now do what ever initialization is needed
	DoubleTag_ = iConfig.getParameter<edm::InputTag>("DoubleTag");
	DoubleTok_ = consumes<double>(DoubleTag_);
	CutValue_ = iConfig.getParameter <double> ("CutValue");
}


DoubleFilter::~DoubleFilter()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
DoubleFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	edm::Handle<double> var;	
	iEvent.getByToken(DoubleTok_,var);
	if(*var<CutValue_) return false;
	
	return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DoubleFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(DoubleFilter);
