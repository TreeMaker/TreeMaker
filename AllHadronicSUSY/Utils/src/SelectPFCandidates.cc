// -*- C++ -*-
//
// Package:    SelectPFCandidates
// Class:      SelectPFCandidates
// 
/**\class SelectPFCandidates SelectPFCandidates.cc RA2Classic/SelectPFCandidates/src/SelectPFCandidates.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
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
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//
// class declaration
//

class SelectPFCandidates : public edm::EDProducer {
public:
  explicit SelectPFCandidates(const edm::ParameterSet&);
  ~SelectPFCandidates();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag packedPFCandidatesTag_;
  double minPT_, maxEta_;
  
  
  
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
SelectPFCandidates::SelectPFCandidates(const edm::ParameterSet& iConfig)
{
  //register your produc
  packedPFCandidatesTag_ 				= 	iConfig.getParameter<edm::InputTag >("PackedPFCandidatesTag");	
  minPT_ = iConfig.getParameter<double> ("MinPt");
  maxEta_ = iConfig.getParameter<double> ("MaxEta");
  produces<std::vector<pat::PackedCandidate> >("");
	const std::string string1t("Charge");
	produces<std::vector<int> > (string1t).setBranchAlias(string1t);
	const std::string string2t("Typ");
	produces<std::vector<int> > (string2t).setBranchAlias(string2t);

	

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
  
}


SelectPFCandidates::~SelectPFCandidates()
{
  
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
SelectPFCandidates::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;	
  std::auto_ptr< std::vector<pat::PackedCandidate> > selectedFPCandidates(new std::vector<pat::PackedCandidate>);
	std::auto_ptr< std::vector<int> > selectedPFCandCharge(new std::vector<int>);
	std::auto_ptr< std::vector<int> > selectedPFCandTyp(new std::vector<int>);
  Handle<edm::View<pat::PackedCandidate> > packed;
  iEvent.getByLabel(packedPFCandidatesTag_,packed);
  for(size_t i=0; i<packed->size();i++)
  {
    if((*packed)[i].pt() > minPT_ && abs((*packed)[i].eta() )<maxEta_)
    {
      selectedFPCandidates->push_back((*packed)[i]);
			selectedPFCandCharge->push_back((*packed)[i].charge());
			if((*packed)[i].isJet() ) selectedPFCandTyp->push_back(0);
 			else if((*packed)[i].isMuon() ) selectedPFCandTyp->push_back(1);
 			else if((*packed)[i].isElectron() ) selectedPFCandTyp->push_back(2);
 			else if((*packed)[i].isPhoton() ) selectedPFCandTyp->push_back(3);
			else  selectedPFCandTyp->push_back(-1);
    }
  }
//   std::cout<<"Original: "<<packed->size()<<" selected: "<<selectedFPCandidates->size()<<std::endl;
// std::cout<<"Size pfcand: "<<selectedFPCandidates->size()<<" " 

  iEvent.put(selectedFPCandidates);
	const std::string string1t("Charge");
	iEvent.put(selectedPFCandCharge,string1t);
	const std::string string2t("Typ");
	iEvent.put(selectedPFCandTyp,string2t);

  
}

// ------------ method called once each job just before starting event loop  ------------
void 
SelectPFCandidates::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SelectPFCandidates::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
SelectPFCandidates::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SelectPFCandidates::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SelectPFCandidates::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SelectPFCandidates::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SelectPFCandidates::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SelectPFCandidates);
