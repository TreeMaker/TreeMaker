// system include files
#include <memory>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <TMath.h>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "CommonTools/Utils/interface/PtComparator.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/ValueMap.h"

class JetUncertaintyProducer : public edm::global::EDProducer<> {
	public:
		explicit JetUncertaintyProducer(const edm::ParameterSet&);
	private:
		void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		GreaterByPt<pat::Jet> pTComparator_;
		edm::InputTag JetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
		std::string JetType_;
		int jecUncDir_;
		bool storeUnc_;
};

JetUncertaintyProducer::JetUncertaintyProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	JetType_(iConfig.getParameter<std::string>("JetType")),
	jecUncDir_(iConfig.getParameter<int>("jecUncDir")),
	storeUnc_(iConfig.getParameter<bool>("storeUnc"))
{
	if(storeUnc_){
		produces<edm::ValueMap<float>>("");
	}
	produces<std::vector<pat::Jet>>();
}

void JetUncertaintyProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	//get the JEC uncertainties
	edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
	iSetup.get<JetCorrectionsRecord>().get(JetType_,JetCorParColl); 
	JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
	auto jecUnc = std::make_unique<JetCorrectionUncertainty>(JetCorPar);

	//get the input jet collection (nominal JECs already applied)
	edm::Handle<edm::View<pat::Jet>> jets;
	iEvent.getByToken(JetTok_, jets);

	auto newJets  = std::make_unique<std::vector<pat::Jet>>();
	newJets->reserve(jets->size());
	auto jecUncVec  = std::make_unique<std::vector<double>>();
	if(storeUnc_){
		jecUncVec->reserve(jets->size());
	}

	for (unsigned idx = 0; idx < jets->size(); ++idx) {
		// construct the Jet from the ref -> save ref to original object
		edm::Ptr<pat::Jet> jetPtr = jets->ptrAt(idx);
		pat::Jet ajet(jetPtr);
		ajet.addUserInt("jecOrigIndex",idx);

		//get JEC unc for this jet, using corrected pT
		jecUnc->setJetEta(jets->at(idx).eta());
		jecUnc->setJetPt(jets->at(idx).pt());
		double uncertainty = jecUnc->getUncertainty(true);
		//safety check if uncertainty is not available for a jet
		if(uncertainty==-999.) uncertainty = 0;
		
		double jesUncScale = 1.0;
		if(storeUnc_){
			//store JEC unc for this jet
			jecUncVec->push_back(uncertainty);
		}
		//downward variation
		if(jecUncDir_ < 0){
			jesUncScale = 1 - uncertainty;
		}
		//upward variation
		else if(jecUncDir_ > 0){
			jesUncScale = 1 + uncertainty;
		}
		
		//apply variation to p4 in jet object
		ajet.scaleEnergy(jesUncScale);
		
		//store varied jet
		newJets->push_back(ajet);		
	}

	if(storeUnc_){
		//store uncertainty as a userfloat (keyed to input collection)
		auto out = std::make_unique<edm::ValueMap<float>>();
		typename edm::ValueMap<float>::Filler filler(*out);
		filler.insert(jets, jecUncVec->begin(), jecUncVec->end());
		filler.fill();
		iEvent.put(std::move(out),"");
	}
	//sort jets in pt
	std::sort(newJets->begin(), newJets->end(), pTComparator_);
	
	iEvent.put(std::move(newJets));
}

DEFINE_FWK_MODULE(JetUncertaintyProducer);

