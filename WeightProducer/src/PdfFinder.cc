// system include files
#include <string>
#include <sstream>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"

//
// class declaration
//

class PdfFinder: public edm::one::EDAnalyzer<edm::one::WatchRuns> {
	public:
		explicit PdfFinder(const edm::ParameterSet&);
		~PdfFinder() override;
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
	private:
		void beginRun(edm::Run const&, edm::EventSetup const&) override;
		void analyze(edm::Event const&, edm::EventSetup const&) override {}
		void endRun(edm::Run const&, edm::EventSetup const&) override {}
	
		//member variables
		edm::InputTag lheRunTag_;
		edm::EDGetTokenT<LHERunInfoProduct> lheRunTok_;
};

PdfFinder::PdfFinder(const edm::ParameterSet& iConfig) :
	lheRunTag_(edm::InputTag("externalLHEProducer")),
	lheRunTok_(consumes<LHERunInfoProduct,edm::InRun>(lheRunTag_))
{}

PdfFinder::~PdfFinder() { }

void PdfFinder::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup) {
	edm::Handle<LHERunInfoProduct> h_lheRun;
	// getByToken throws since we're not in the endRun (see https://github.com/cms-sw/cmssw/pull/18499)
	//iRun.getByToken(lheRunTok_, h_lheRun);
	iRun.getByLabel(lheRunTag_, h_lheRun);

	const auto& lheRun = *(h_lheRun.product());
	for(auto iter = lheRun.headers_begin(); iter != lheRun.headers_end(); ++iter){
		std::stringstream ss;
		ss << iter->tag() << std::endl;
		for(const auto& line: iter->lines()){
			ss << line;
		}
		edm::LogInfo("TreeMaker") << ss.str();
	}
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PdfFinder::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PdfFinder);
