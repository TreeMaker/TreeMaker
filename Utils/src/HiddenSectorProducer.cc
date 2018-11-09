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
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/RefToPtr.h"

typedef math::XYZTLorentzVector LorentzVector;

class HiddenSectorProducer : public edm::global::EDProducer<> {
	public:
		explicit HiddenSectorProducer(const edm::ParameterSet&);
	private:
		void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		//helper
		double TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const;
		template <class P>
		void addDaughters(const P* i_part, std::vector<const reco::Candidate*>& listOfDaughters) const;
		edm::InputTag JetTag_, MetTag_, GenTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
		edm::EDGetTokenT<edm::View<pat::MET>> MetTok_;
		edm::EDGetTokenT<edm::View<reco::GenParticle>> GenTok_;
		std::unordered_set<unsigned> DarkIDs_;
		unsigned DarkQuarkID_, DarkMediatorID_;
};

HiddenSectorProducer::HiddenSectorProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	MetTag_(iConfig.getParameter<edm::InputTag>("MetTag")),
	GenTag_(iConfig.getParameter<edm::InputTag>("GenTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	MetTok_(consumes<edm::View<pat::MET>>(MetTag_)),
	GenTok_(consumes<edm::View<reco::GenParticle>>(GenTag_)),
	DarkQuarkID_(iConfig.getParameter<unsigned>("DarkQuarkID")),
	DarkMediatorID_(iConfig.getParameter<unsigned>("DarkMediatorID"))
{
	const auto& ids = iConfig.getParameter<std::vector<unsigned>>("DarkIDs");
	DarkIDs_.insert(ids.begin(),ids.end());

	produces<double>("MJJ");
	produces<double>("Mmc");
	produces<double>("MT");
	produces<double>("DeltaPhi1");
	produces<double>("DeltaPhi2");
	produces<double>("DeltaPhiMin");
	produces<std::vector<bool>>("isHV");
}

double HiddenSectorProducer::TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const {
	double E1 = std::sqrt(std::pow(px1,2)+std::pow(py1,2)+std::pow(m1,2));
	double E2 = std::sqrt(std::pow(px2,2)+std::pow(py2,2)+std::pow(m2,2));
	double MTsq = std::pow(E1+E2,2)-std::pow(px1+px2,2)-std::pow(py1+py2,2);
	return std::sqrt(std::max(MTsq,0.0));
}

template <class P>
void HiddenSectorProducer::addDaughters(const P* i_part, std::vector<const reco::Candidate*>& listOfDaughters) const {
	for (unsigned idau=0; idau < i_part->numberOfDaughters(); ++idau) { // add all daughters of HVquark to list
		const reco::Candidate *dau = i_part->daughter(idau);
		if(std::abs(dau->pdgId())==DarkQuarkID_) addDaughters(dau,listOfDaughters); // recurse down to HV-quark copy's daughters
		else listOfDaughters.push_back(dau);
	}
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

	auto jet_isHV_vec = std::make_unique<std::vector<bool>>();

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
		
		//MET is massless, but jets aren't
		double MET = h_mets->at(0).pt(), METPhi = h_mets->at(0).phi();
		MT = TransverseMass(vjj.Px(),vjj.Py(),vjj.M(),MET*std::cos(METPhi),MET*std::sin(METPhi),0);
	}
	
	//ISRJetProducer method, find jets with hard process particles at their 'core' and other jets are ISR
	for(const auto& i_jet : *(h_jets.product())){ // loop over AK8 jets
		bool matched = false; // matched == true means that this jet has a hard process (descendant particle of the Z') at its 'core'
		for (const auto& i_part : *(h_parts.product())){ // loop over GenParticles
			if (matched) break; // only need to match one particle to the jet to tag it as FSR
			if(i_part.status()!=23) continue; // only want particles outgoing from the hard process
			unsigned momid = std::abs(i_part.mother()->pdgId());
			if(momid!=DarkMediatorID_) continue; // only want direct descendants of Z' (kind of redundant)
			//check against daughters in case of hard initial splitting, from ISRJetProducer...
			std::vector<const reco::Candidate*> listOfDaughters;
			addDaughters(&i_part,listOfDaughters);
			for (const auto& daughter : listOfDaughters) {
				float dR = deltaR(i_jet, daughter->p4());//float dR = deltaR(i_jet, i_part.daughter(idau)->p4());
				if(dR<0.8){
					matched = true;
					break;
				}
			}
		}
		jet_isHV_vec->push_back(matched);
	}
	
	iEvent.put(std::move(jet_isHV_vec),"isHV");
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

