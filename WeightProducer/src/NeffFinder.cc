// system include files
#include <string>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "TH1.h"

//
// class declaration
//

class NeffFinder: public edm::one::EDAnalyzer<edm::one::SharedResources> {
	public:
		explicit NeffFinder(const edm::ParameterSet&);
		~NeffFinder() override;
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
	private:
		void beginJob() override;
		void analyze(const edm::Event&, const edm::EventSetup&) override;
		void endJob() override;
	
		//member variables
		edm::Service<TFileService> fs;
		TH1F *hNeffInfo, *hTrueNumInt;
		std::string name;
		unsigned nbins;
		unsigned long pos, neg;
		edm::InputTag genEvtTag_, puInfoTag_;
		edm::EDGetTokenT<GenEventInfoProduct> genEvtTok_;
		edm::EDGetTokenT<std::vector<PileupSummaryInfo>> puInfoTok_;
};

NeffFinder::NeffFinder(const edm::ParameterSet& iConfig) :
	hNeffInfo(nullptr),
	hTrueNumInt(nullptr),
	name(iConfig.getParameter<std::string>("name")),
	nbins(iConfig.getParameter<unsigned>("nbins")),
	pos(0), neg(0),
	genEvtTag_(edm::InputTag("generator")),
	puInfoTag_(edm::InputTag("slimmedAddPileupInfo")),
	genEvtTok_(consumes<GenEventInfoProduct>(genEvtTag_)),
	puInfoTok_(consumes<std::vector<PileupSummaryInfo>>(puInfoTag_))
{
	usesResource("TFileService");
}

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

	//fill PU histogram
	edm::Handle<std::vector<PileupSummaryInfo>> puInfo;
	iEvent.getByToken(puInfoTok_, puInfo);
	for(const auto& PVI : *puInfo) {
		//look only at primary BX (in-time)
		if(PVI.getBunchCrossing()==0){
			hTrueNumInt->Fill(PVI.getTrueNumInteractions());
			break;
		}
	}
}

// ------------ method called once each job just before starting event loop  ------------
void 
NeffFinder::beginJob() {
	if( !fs ) {
		throw edm::Exception(edm::errors::Configuration, "TFile Service is not registered in cfg file");
	}
	hNeffInfo = fs->make<TH1F>(("NeffInfo_"+name).c_str(),("NeffInfo_"+name).c_str(),4,0,4);
	hTrueNumInt = fs->make<TH1F>(("TrueNumInteractions_"+name).c_str(),("TrueNumInteractions_"+name).c_str(),nbins,0,nbins);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
NeffFinder::endJob() {
	//put neff info into histo
	hNeffInfo->SetBinContent(1,pos-neg);
	hNeffInfo->SetBinContent(2,pos);
	hNeffInfo->SetBinContent(3,neg);
	hNeffInfo->SetBinContent(4,pos+neg);
	//also print it, just in case
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
