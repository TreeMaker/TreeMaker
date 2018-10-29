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
	produces<std::vector<double>>("ISRminDeltaRsm");
	produces<std::vector<double>>("ISRminDeltaRhv");
	produces<std::vector<int>>("nSMISRparts");
	produces<std::vector<int>>("nHVISRparts");
	produces<std::vector<double>>("fracptISR");
	produces<std::vector<double>>("fracptHV");
	produces<std::vector<bool>>("isISR");
}

double HiddenSectorProducer::TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const{
	double E1 = std::sqrt(std::pow(px1,2)+std::pow(py1,2)+std::pow(m1,2));
	double E2 = std::sqrt(std::pow(px2,2)+std::pow(py2,2)+std::pow(m2,2));
	double MTsq = std::pow(E1+E2,2)-std::pow(px1+px2,2)-std::pow(py1+py2,2);
	return std::sqrt(std::max(MTsq,0.0));
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

	auto jet_minDRsm_vec = std::make_unique<std::vector<double>>();
	auto jet_minDRhv_vec = std::make_unique<std::vector<double>>();

	auto jet_fracptISR_vec = std::make_unique<std::vector<double>>();
	auto jet_fracptHV_vec = std::make_unique<std::vector<double>>();

	auto jet_nSMISRparts_vec = std::make_unique<std::vector<int>>();
	auto jet_nHVISRparts_vec = std::make_unique<std::vector<int>>();

	auto jet_isISR_vec = std::make_unique<std::vector<bool>>();

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
	
	//determining jet ISR status, minDR is junk
	// minDR: HV and SM
	// record, for each jet, the minimum deltaR between it and all SM and HV particles (seperatly) that are part of the ISR process (code 43, 44)
	double deltaRjp = 15.;
	for(const auto& i_jet : *(h_jets.product())){ // loop over AK8 jets
		double minDRhv = 15.;
		double minDRsm = 15.;
		int nSMISR = 0;
		int nHVISR = 0;
		for(const auto& i_part : *(h_parts.product())){ // loop over GenParticles
			if(!(std::abs(i_part.status())==43 || std::abs(i_part.status())==44)) continue; // skip non-outgoing ISR particles
			if(i_part.pt() == 0) continue; //skip particles that are eta == inf
			deltaRjp = deltaR(i_jet,i_part);
			if(std::abs(i_part.pdgId())>=4900000){ 
				nHVISR++;
				if(deltaRjp < minDRhv) minDRhv = deltaRjp;
			}
			else if(std::abs(i_part.pdgId())< 4900000){
				nSMISR++;
				if(deltaRjp < minDRsm) minDRsm = deltaRjp;
			}
		} // end loop over GenParticles
		jet_minDRsm_vec->push_back(minDRsm);
		jet_minDRhv_vec->push_back(minDRhv);
		jet_nSMISRparts_vec->push_back(nSMISR);
		jet_nHVISRparts_vec->push_back(nHVISR);
	}  //  end loop over AK8 jets


	//Second method: fracPt
	// first, determine which GenParticles are from HVQuarks
	// only care about status == 1 particles, though
	std::vector<int> isHVdec;
	// loop over all genParticles
	for(const auto& i_part : *(h_parts.product())){ // loop over Genparticles
		int partIsHV = 3;
		if(!(i_part.status()==1)) partIsHV = 0; // dont care about parts not status == 1
		const reco::Candidate *ancestor = i_part.mother();
		while (partIsHV == 3){
			if(std::abs(ancestor->pdgId()) == 4900101){// specifcally find HVQuark in ancestry, not just any HVParticle (Z'->qqbar problem)
				partIsHV = 1;
			}
			if(std::abs(ancestor->pdgId()) == 2212){
				partIsHV = 0;
			}
			ancestor = ancestor->mother();
		}
		isHVdec.push_back(partIsHV);
	} //end Genpartiles loop

	// now, calculate fracpt for each jet
	for(const auto& i_jet : *(h_jets.product())){ // loop over AK8 jets
		double jetPt = 0.;
		double HVPt = 0.;
		double ISRPt = 0.;
		for (unsigned imc=0; imc < h_parts->size(); ++imc){ // loop over GenParticles
			const reco::GenParticle &i_part = (*h_parts)[imc];
			if(!(i_part.status()==1)) continue;
			if(deltaR(i_jet,i_part)<0.8){
				jetPt += i_part.pt();
				if(isHVdec[imc] == 1) HVPt += i_part.pt();
				if(isHVdec[imc] == 0) ISRPt += i_part.pt();
			}
		} // end loop over GenParticles
		jet_fracptHV_vec->push_back(HVPt/jetPt);
		jet_fracptISR_vec->push_back(ISRPt/jetPt);
	}  //  end loop over AK8 jets
/*
	//Second method: fracPt, new algorithm. Don't store HVQuarkDecendant status..., dont work.
	// first, determine which GenParticles are from HVQuarks
	// only care about status == 1 particles, though
	// loop over all genParticles
	std::vector<double> jetPt;
	std::vector<double> HVPt;
	std::vector<double> ISRPt;
	jetPt.reserve(h_jets->size());
	HVPt.reserve(h_jets->size());
	ISRPt.reserve(h_jets->size());
	for(unsigned i_jet=0 ; i_jet<h_jets->size(); ++i_jet){ // loop over AK8 jets
		jetPt[i_jet] = 0.;
		HVPt[i_jet] = 0.;
		ISRPt[i_jet] = 0.;
	}

	for(const auto& i_part : *(h_parts.product())){ // loop over Genparticles
		int partIsHV = 3;
		if(!(i_part.status()==1)) partIsHV = 0; // dont care about parts not status == 1
		const reco::Candidate *ancestor = i_part.mother();
		while (partIsHV == 3){
			if(std::abs(ancestor->pdgId()) >= 4900000){
				partIsHV = 1;
			}
			if(std::abs(ancestor->pdgId()) == 2212){
				partIsHV = 0;
			}
			ancestor = ancestor->mother();
		}
		for(unsigned i_jet=0 ; i_jet<h_jets->size(); ++i_jet){ // loop over AK8 jets
			const pat::Jet &iJet = (*h_jets)[i_jet];
			if(deltaR(iJet, i_part)<0.8){
				jetPt[i_jet] += i_part.pt();
				if(partIsHV == 1) HVPt[i_jet] += i_part.pt();
				if(partIsHV == 0) ISRPt[i_jet] += i_part.pt();
				if(partIsHV == 3) std::cout << "Particle HV status is still 3!" <<std::endl;
			}
		}
	} //end Genpartiles loop
	// loop over jets again to fill out branches
	for(unsigned i_jet=0 ; i_jet<h_jets->size(); ++i_jet){ // loop over AK8 jets
		jet_fracptHV_vec->push_back(HVPt[i_jet]/jetPt[i_jet]);
		jet_fracptISR_vec->push_back(ISRPt[i_jet]/jetPt[i_jet]);
	}
*/
	//ISRJetProducer method, find jets with hard process particles at their 'core' and other jets are ISR
	for(const auto& i_jet : *(h_jets.product())){ // loop over AK8 jets
		bool matched = false; // matched == true means that this jet has a hardprocess (decendant particle of the Z') at their 'core'
		for (unsigned imc=0; imc < h_parts->size(); ++imc){ // loop over GenParticles
			if (matched) break; // only need to match one particle to the jet to tag it as FSR
			const reco::GenParticle &i_part = (*h_parts)[imc];
			if(!(i_part.status()==23)) continue; // only want particles outgoing from the hard process
			int momid = std::abs(i_part.mother()->pdgId());
			if(!(momid==4900023)) continue; // only want direct decendants of Z' (kind of redundant)
			//check against daughters in case of hard initial splitting, from ISRJetProducer...
			//std::vector<reco::CandidatePtr> listOfDaughters;
			std::vector<const reco::Candidate*> listOfDaughters;
			int nHVQuarksInDaughterList = 0;
			for (unsigned idau=0; idau < i_part.numberOfDaughters(); ++idau) { // add all daughters of HVquark to list
				//reco::CandidatePtr dau = edm::refToPtr(i_part.daughterRef(idau));
				const reco::Candidate *dau = i_part.daughter(idau);
				listOfDaughters.push_back(dau);
				if( std::abs(dau->pdgId())==4900101) nHVQuarksInDaughterList++; // note how many HV-quarks(gluons) (copies) are in the list
			}
			while(nHVQuarksInDaughterList>0){// while there are copies...
				unsigned numOldHVQuarks = (unsigned) nHVQuarksInDaughterList;
				nHVQuarksInDaughterList=0;
				for (unsigned i = 0; i<listOfDaughters.size();i++) { 
					const reco::Candidate *daughter = listOfDaughters.at(i);
					if(!(std::abs(daughter->pdgId())==4900101)) continue;// find the copies
					for (unsigned idau=0; idau < daughter->numberOfDaughters(); ++idau) {
						const reco::Candidate *dau = daughter->daughter(idau);
						listOfDaughters.push_back(dau);// add copies' daughters to list
					}
				}
				for (unsigned i = 0; i<numOldHVQuarks;i++) { 
					for (unsigned i=0; i < listOfDaughters.size(); ++i){
						const reco::Candidate *daughter = listOfDaughters.at(i);
						if(std::abs(daughter->pdgId())==4900101){
							listOfDaughters.erase(listOfDaughters.begin()+i); // remove the copies
							break;
						}
					}
				}
				for (unsigned i = 0; i<listOfDaughters.size();i++) {
					const reco::Candidate *daughter = listOfDaughters.at(i);
					if(std::abs(daughter->pdgId())==4900101) nHVQuarksInDaughterList++; // count the copies	
				}
			}
			for (unsigned i = 0; i<listOfDaughters.size();i++) {//for (unsigned idau=0; idau < i_part.numberOfDaughters(); ++idau) {
				const reco::Candidate *daughter = listOfDaughters.at(i);
				float dR = deltaR(i_jet, daughter->p4());//float dR = deltaR(i_jet, i_part.daughter(idau)->p4());
				if(dR<0.8){
					matched = true;
					break;
				}
			}
		}
		jet_isISR_vec->push_back(!matched);
	}
	
	
	iEvent.put(std::move(jet_minDRsm_vec), "ISRminDeltaRsm");
	iEvent.put(std::move(jet_minDRhv_vec), "ISRminDeltaRhv");
	iEvent.put(std::move(jet_nSMISRparts_vec), "nSMISRparts");
	iEvent.put(std::move(jet_nHVISRparts_vec), "nHVISRparts");
	iEvent.put(std::move(jet_fracptISR_vec), "fracptISR");
	iEvent.put(std::move(jet_fracptHV_vec), "fracptHV");
	iEvent.put(std::move(jet_isISR_vec),"isISR");
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

