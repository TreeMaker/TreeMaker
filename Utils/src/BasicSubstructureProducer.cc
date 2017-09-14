// system include files
#include <memory>
#include <vector>
#include <cmath>
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
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

class BasicSubstructureProducer : public edm::global::EDProducer<> {
	public:
		explicit BasicSubstructureProducer(const edm::ParameterSet&);
	private:
		virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		edm::InputTag JetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
};

BasicSubstructureProducer::BasicSubstructureProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_))
{
	produces<std::vector<std::vector<TLorentzVector>>>("jetConstituents");
	produces<std::vector<double>>("overflow");
	produces<std::vector<double>>("girth");
	produces<std::vector<double>>("momenthalf");
	produces<std::vector<int>>("multiplicity");
	produces<std::vector<double>>("ptD");
	produces<std::vector<double>>("axismajor");
	produces<std::vector<double>>("axisminor");
}

void BasicSubstructureProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	//get the collections
	edm::Handle<edm::View<pat::Jet>> h_jets;
	iEvent.getByToken(JetTok_, h_jets);

	auto jetConstituents = std::make_unique<std::vector<std::vector<TLorentzVector>>>();
	auto overflow = std::make_unique<std::vector<double>>();
	auto girth = std::make_unique<std::vector<double>>();
	auto momenthalf = std::make_unique<std::vector<double>>();
	auto multiplicity = std::make_unique<std::vector<int>>();
	auto ptD = std::make_unique<std::vector<double>>();
	auto axismajor = std::make_unique<std::vector<double>>();
	auto axisminor = std::make_unique<std::vector<double>>();

	for(const auto& i_jet : *(h_jets.product())){
		std::vector<TLorentzVector> i_partvecs;
		int i_mult = i_jet.numberOfDaughters();
		//calculate jet "overflow": 1 - (scalar sum of pT w/ dR<0.4 over scalar sum of pT w/ dR<0.8)
		double i_numer = 0.0, i_denom = 0.0;
		double i_girth = 0.0, i_momenthalf = 0.0;
		double sumPt = 0.0, sumPt2 = 0.0;
		double sumDeta = 0.0, sumDphi = 0.0, sumDeta2 = 0.0, sumDphi2 = 0.0, sumDetaDphi = 0.0;

		for(int k = 0; k < i_mult; ++k){
			const reco::CandidatePtr& i_part = i_jet.daughterPtr(k);
			if(i_part.isNonnull() and i_part.isAvailable()){
				i_partvecs.emplace_back(i_part->px(),i_part->py(),i_part->pz(),i_part->energy());

				//overflow
				double dR = reco::deltaR(i_jet.p4(),i_part->p4());
				double pT = i_part->pt();
				if(dR < 0.8) i_denom += pT;
				if(dR < 0.4) i_numer += pT;

				//moment calcs
				i_girth += pT*dR;
				i_momenthalf += pT*std::sqrt(dR);

				//axis calcs
				double dphi = reco::deltaPhi(i_jet.phi(),i_part->phi());
				double deta = i_part->eta() - i_jet.eta();
				double pT2 = pT*pT;
				
				sumPt += pT;
				sumPt2 += pT2;
				sumDeta += deta*pT2;
				sumDphi += dphi*pT2;
				sumDeta2 += deta*deta*pT2;
				sumDphi2 += dphi*dphi*pT2;
				sumDetaDphi += deta*dphi*pT2;
			}
		}

		//finish overflow calc
		double i_underflow = i_denom > 0.0 ? i_numer/i_denom : 0.0;
		double i_overflow = 1.0 - i_underflow;

		//finish moment calcs
		i_girth /= i_jet.pt();
		i_momenthalf /= i_jet.pt();

		//finish axis calculations (eigenvectors)
		sumDeta /= sumPt2;
		sumDphi /= sumPt2;
		sumDeta2 /= sumPt2;
		sumDphi2 /= sumPt2;
		sumDetaDphi /= sumPt2;
		double a = 0.0, b = 0.0, c = 0.0, d = 0.0;
		a = sumDeta2 - sumDeta*sumDeta;
		b = sumDphi2 - sumDphi*sumDphi;
		c = sumDeta*sumDphi - sumDetaDphi;
		d = std::sqrt(std::fabs((a-b)*(a-b)+4*c*c));
		double i_axis1 = (a+b+d)>0 ? std::sqrt(0.5*(a+b+d)) : 0.0;
		double i_axis2 = (a+b-d)>0 ? std::sqrt(0.5*(a+b-d)) : 0.0;
		double i_ptD = std::sqrt(sumPt2)/sumPt;

		//store values
		jetConstituents->push_back(i_partvecs);
		overflow->push_back(i_overflow);
		girth->push_back(i_girth);
		momenthalf->push_back(i_momenthalf);
		multiplicity->push_back(i_mult);
		ptD->push_back(i_ptD);
		axismajor->push_back(i_axis1);
		axisminor->push_back(i_axis2);
	}

	iEvent.put(std::move(jetConstituents),"jetConstituents");
	iEvent.put(std::move(overflow),"overflow");
	iEvent.put(std::move(girth),"girth");
	iEvent.put(std::move(momenthalf),"momenthalf");
	iEvent.put(std::move(multiplicity),"multiplicity");
	iEvent.put(std::move(ptD),"ptD");
	iEvent.put(std::move(axismajor),"axismajor");
	iEvent.put(std::move(axisminor),"axisminor");
}

DEFINE_FWK_MODULE(BasicSubstructureProducer);

