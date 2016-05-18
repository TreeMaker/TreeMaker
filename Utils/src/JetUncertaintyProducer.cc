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
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "CommonTools/Utils/interface/PtComparator.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

class JetUncertaintyProducer : public edm::EDProducer {
	public:
		explicit JetUncertaintyProducer(const edm::ParameterSet&);
	private:
		virtual void produce(edm::Event&, const edm::EventSetup&);
		GreaterByPt<pat::Jet> pTComparator_;
		edm::InputTag JetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
		std::string JetType_;
		int jecUncDir_;
};

JetUncertaintyProducer::JetUncertaintyProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	JetType_(iConfig.getParameter<std::string>("JetType")),
	jecUncDir_(iConfig.getParameter<int>("jecUncDir"))
{
	if(jecUncDir_==0){
		produces<std::vector<double>>("jecFactor");
		produces<std::vector<double>>("jecUnc");
	}
	else{
		produces<std::vector<pat::Jet>>();
	}
}

void JetUncertaintyProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	//get the JEC uncertainties
	edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
	iSetup.get<JetCorrectionsRecord>().get(JetType_,JetCorParColl); 
	JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
	std::auto_ptr<JetCorrectionUncertainty> jecUnc( new JetCorrectionUncertainty(JetCorPar) );

	//get the input jet collection (nominal JECs already applied)
	edm::Handle<edm::View<pat::Jet>> jets;
	iEvent.getByToken(JetTok_, jets);

	std::auto_ptr< std::vector<pat::Jet> > newJets ( new std::vector<pat::Jet>() );
	newJets->reserve(jets->size());
	std::auto_ptr< std::vector<double> > jecFactorVec ( new std::vector<double>() );
	jecFactorVec->reserve(jets->size());
	std::auto_ptr< std::vector<double> > jecUncVec ( new std::vector<double>() );
	jecUncVec->reserve(jets->size());

	for (edm::View<pat::Jet>::const_iterator itJet = jets->begin(); itJet != jets->end(); itJet++) {
		// construct the Jet from the ref -> save ref to original object
		unsigned int idx = std::distance(jets->begin(),itJet);
		edm::RefToBase<pat::Jet> jetRef = jets->refAt(idx);
		edm::Ptr<pat::Jet> jetPtr = jets->ptrAt(idx);
		pat::Jet ajet(jetPtr);
		math::XYZTLorentzVector vjet = ajet.p4();
		
		//get JEC unc for this jet, using corrected pT
		jecUnc->setJetEta(itJet->eta());
		jecUnc->setJetPt(itJet->pt());
		double uncertainty = jecUnc->getUncertainty(true);
		//safety check if uncertainty is not available for a jet
		if(uncertainty==-999.) uncertainty = 0;
		
		double jesUncScale = 1.0;
		//no variation - just store scale factor & uncertainty
		if(jecUncDir_==0){
			//store JEC unc for this jet
			jecUncVec->push_back(uncertainty);
			
			//store JEC factor for this jet
			std::vector<std::string> availableJECLevels = jetPtr->availableJECLevels();
			double scaleRawToFull = jetPtr->jecFactor(availableJECLevels.back())/jetPtr->jecFactor("Uncorrected");
			jecFactorVec->push_back(scaleRawToFull);
			
			continue;
		}
		//downward variation
		if(jecUncDir_ < 0){
			jesUncScale = 1 - uncertainty;
		}
		//upward variation
		else if(jecUncDir_ > 0){
			jesUncScale = 1 + uncertainty;
		}
		
		//apply variation
		vjet *= jesUncScale;
		
		//set new p4 in jet object
		ajet.setP4(vjet);
		
		//store varied jet
		newJets->push_back(ajet);		
	}

	if(jecUncDir_==0){
		//JEC factor and unc are NOT sorted (kept in order of original collection)	
		iEvent.put(jecUncVec,"jecUnc");
		iEvent.put(jecFactorVec,"jecFactor");		
	}
	else{
		//sort jets in pt
		std::sort(newJets->begin(), newJets->end(), pTComparator_);
	
		iEvent.put(newJets);
	}
}

DEFINE_FWK_MODULE(JetUncertaintyProducer);

