// system include files
#include <memory>
#include <vector>
#include <cmath>
#include <unordered_set>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

class HiddenSectorProducer : public edm::global::EDProducer<> {
	public:
		explicit HiddenSectorProducer(const edm::ParameterSet&);
	private:
		virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		edm::InputTag JetTag_, MetTag_, GenTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
		edm::EDGetTokenT<edm::View<pat::MET>> MetTok_;
		edm::EDGetTokenT<edm::View<reco::GenParticle>> GenTok_;
		std::unordered_set<unsigned> DarkIDs_;
};

HiddenSectorProducer::HiddenSectorProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	MetTag_(iConfig.getParameter<edm::InputTag>("MetTag")),
	GenTag_(iConfig.getParameter<edm::InputTag>("GenTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	MetTok_(consumes<edm::View<pat::MET>>(MetTag_)),
	GenTok_(consumes<edm::View<reco::GenParticle>>(GenTag_))
{
	const auto& ids = iConfig.getParameter<std::vector<unsigned>>("DarkIDs");
	DarkIDs_.insert(ids.begin(),ids.end());

	produces<double>("MJJ");
	produces<double>("Mmc");
	produces<double>("MT");
	produces<double>("DeltaPhi1");
	produces<double>("DeltaPhi2");
	produces<double>("DeltaPhiMin");
}

void HiddenSectorProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	//get the collections
	edm::Handle<edm::View<pat::Jet>> h_jets;
	iEvent.getByToken(JetTok_, h_jets);

	edm::Handle<edm::View<pat::MET>> h_mets;
	iEvent.getByToken(MetTok_, h_mets);

	edm::Handle<edm::View<reco::GenParticle>> h_parts;
	iEvent.getByToken(GenTok_, h_parts);

	LorentzVector vpartsSum;
	if(h_parts.isValid()){
		for(const auto& i_part : *(h_parts.product())){
			if(DarkIDs_.find(std::abs(i_part.pdgId()))!=DarkIDs_.end()){
				vpartsSum += i_part.p4();
			}
		}
	}

	double MJJ = 0, Mmc = 0, MT = 0, DeltaPhi1 = 10, DeltaPhi2 = 10, DeltaPhiMin = 10;
	//only fill these parts if there are >=2 jets
	if(h_jets->size()>=2){
		//delta phi
		DeltaPhi1 = std::abs(reco::deltaPhi(h_jets->at(0).phi(),h_mets->at(0).phi()));
		DeltaPhi2 = std::abs(reco::deltaPhi(h_jets->at(1).phi(),h_mets->at(0).phi()));
		DeltaPhiMin = std::min(DeltaPhi1,DeltaPhi2);
		
		//masses
		LorentzVector vjj = h_jets->at(0).p4()+h_jets->at(1).p4();
		MJJ = vjj.M();
		
		//include all jets in MC mass
		LorentzVector vmc = vjj + vpartsSum;
		Mmc = vmc.M();
		
		//assume MET is massless
		MT = std::sqrt(2*h_mets->at(0).pt()*vjj.pt()*(1-cos(reco::deltaPhi(h_mets->at(0).phi(),vjj.phi()))));
	}

	auto pMJJ = std::make_unique<double>(MJJ);
	iEvent.put(std::move(pMJJ),"MJJ");
	auto pMmc = std::make_unique<double>(Mmc);
	iEvent.put(std::move(pMmc),"Mmc");
	auto pMT = std::make_unique<double>(MT);
	iEvent.put(std::move(pMT),"MT");
	auto pDeltaPhi1 = std::make_unique<double>(DeltaPhi1);
	iEvent.put(std::move(pDeltaPhi1),"DeltaPhi1");
	auto pDeltaPhi2 = std::make_unique<double>(DeltaPhi2);
	iEvent.put(std::move(pDeltaPhi2),"DeltaPhi2");
	auto pDeltaPhiMin = std::make_unique<double>(DeltaPhiMin);
	iEvent.put(std::move(pDeltaPhiMin),"DeltaPhiMin");
}

DEFINE_FWK_MODULE(HiddenSectorProducer);

