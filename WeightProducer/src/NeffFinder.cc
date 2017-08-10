// system include files
#include <string>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

//
// class declaration
//

class NeffFinder: public edm::one::EDAnalyzer<> {
	public:
		explicit NeffFinder(const edm::ParameterSet&);
		~NeffFinder();
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
	private:
		virtual void beginJob();
		virtual void analyze(const edm::Event&, const edm::EventSetup&);
		virtual void endJob();
	
		//member variables
		std::string name;
		unsigned long pos, neg;
		edm::InputTag genEvtTag_;
		edm::EDGetTokenT<GenEventInfoProduct> genEvtTok_;
};

NeffFinder::NeffFinder(const edm::ParameterSet& iConfig) :
name(iConfig.getParameter<std::string>("name")), pos(0), neg(0), genEvtTag_(edm::InputTag("generator")), genEvtTok_(consumes<GenEventInfoProduct>(genEvtTag_)) { }

NeffFinder::~NeffFinder() { }

// ------------ method called for each event  ------------
void
NeffFinder::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
	//account for negative weights
	edm::Handle<GenEventInfoProduct> genEvtInfoHandle;
	iEvent.getByToken(genEvtTok_, genEvtInfoHandle);
	if (genEvtInfoHandle.isValid()) {
		double genweight_ = genEvtInfoHandle->weight();
		if(genweight_ < 0) ++neg;
		else ++pos;
	}	
}

// ------------ method called once each job just before starting event loop  ------------
void 
NeffFinder::beginJob() { }

// ------------ method called once each job just after ending the event loop  ------------
void 
NeffFinder::endJob() {
	edm::LogInfo("TreeMaker") << "NeffFinder: " << name << " : " << pos-neg << "" << " (pos = " << pos << ", neg = " << neg << ", tot = " << pos+neg << ")";
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
NeffFinder::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NeffFinder);
