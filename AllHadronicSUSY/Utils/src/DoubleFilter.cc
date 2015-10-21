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

class DoubleFilter : public edm::EDFilter {
public:
	explicit DoubleFilter(const edm::ParameterSet&);
	~DoubleFilter();
	
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
	
	edm::InputTag DoubleTag_;
	double CutValue_;
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
DoubleFilter::DoubleFilter(const edm::ParameterSet& iConfig)
{
	//now do what ever initialization is needed
	DoubleTag_ = iConfig.getParameter<edm::InputTag>("DoubleTag");
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
DoubleFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	edm::Handle<double> var;	
	iEvent.getByLabel(DoubleTag_,var);
	if(*var<CutValue_) return false;
	
	return true;
}

// ------------ method called once each job just before starting event loop  ------------
void 
DoubleFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DoubleFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
DoubleFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
	return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
DoubleFilter::endRun(edm::Run&, edm::EventSetup const&)
{
	return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
DoubleFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
	return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
DoubleFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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