// -*- C++ -*-
//
// Package:    SubJetSelection
// Class:      SubJetSelection
// 
/**\class SubJetSelection SubJetSelection.cc RA2Classic/SubJetSelection/src/SubJetSelection.cc
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
//
// class declaration
//

class SubJetSelection : public edm::EDProducer {
public:
	explicit SubJetSelection(const edm::ParameterSet&);
	~SubJetSelection();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	edm::InputTag JetTag_;
	double MinPt_, MaxEta_;
        bool applyLooseID;
	
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
SubJetSelection::SubJetSelection(const edm::ParameterSet& iConfig)
{
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	MinPt_ = iConfig.getParameter <double> ("MinPt");
	MaxEta_ = iConfig.getParameter <double> ("MaxEta");
	applyLooseID = iConfig.getUntrackedParameter<bool>("applyLooseID",true);
	//register your products
	/* Examples
	 *   produces<ExampleData2>();
	 * 
	 *   //if do put with a label
	 *   produces<ExampleData2>("label");
	 * 
	 *   //if you want to put into the Run
	 *   produces<ExampleData2,InRun>();
	 */
	//now do what ever other initialization is needed
	//register your products
	produces<std::vector<Jet> >();
// 	produces<std::vector<Float_t> > ("testValue");
	
}


SubJetSelection::~SubJetSelection()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
SubJetSelection::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	std::auto_ptr<std::vector<Jet> > prodJets(new std::vector<Jet>());
// 	std::auto_ptr<std::vector<Float_t> > pFloat(new std::vector<Float_t>());
	// test
	edm::Handle< edm::View<Jet> > Jets;
	iEvent.getByLabel(JetTag_,Jets);
	if(Jets.isValid())
	{
		for(unsigned int i=0; i<Jets->size();i++)
		{
		  // applying loose jet ID
		  // neutralEmEnergyFraction<0.99&&neutralHadronEnergyFraction<0.99&&numberOfDaughters>1
		  if( applyLooseID )
		  {
		    if(Jets->at(i).pt()>MinPt_ && std::abs(Jets->at(i).eta() ) < MaxEta_ &&
		       Jets->at(i).neutralEmEnergyFraction()<0.99 && 
		       Jets->at(i).neutralHadronEnergyFraction()<0.99 &&
		       Jets->at(i).numberOfDaughters()>1 )
		      {
			prodJets->push_back(Jet(Jets->at(i)) );
		      }
		  }else
		  {
		    if(Jets->at(i).pt()>MinPt_ && std::abs(Jets->at(i).eta() ) < MaxEta_)
		    {
		      prodJets->push_back(Jet(Jets->at(i)) );
		    }
		  }
		}
	}
	// put in the event
	const std::string string1("");
	iEvent.put(prodJets );
	
// 	iEvent.put(pFloat, "testValue");
	
}

// ------------ method called once each job just before starting event loop  ------------
void 
SubJetSelection::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SubJetSelection::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
SubJetSelection::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SubJetSelection::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SubJetSelection::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SubJetSelection::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SubJetSelection::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SubJetSelection);
