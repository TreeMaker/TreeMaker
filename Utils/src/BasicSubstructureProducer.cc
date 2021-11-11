// system include files
#include <memory>
#include <vector>
#include <cmath>
#include <string>
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
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

class BasicSubstructureProducer : public edm::global::EDProducer<> {
	public:
		explicit BasicSubstructureProducer(const edm::ParameterSet&);
	private:
		void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		template <class T>
		void helpProduce(edm::Event& iEvent, const edm::Handle<edm::View<pat::Jet>>& jets, const std::vector<T>& vec, const std::string& name) const;
		edm::InputTag JetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
};

BasicSubstructureProducer::BasicSubstructureProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_))
{
	produces<edm::ValueMap<float>>("girth");
}

template <class T>
void BasicSubstructureProducer::helpProduce(edm::Event& iEvent, const edm::Handle<edm::View<pat::Jet>>& jets, const std::vector<T>& vec, const std::string& name) const {
	//store as userfloat
	auto out = std::make_unique<edm::ValueMap<T>>();
	typename edm::ValueMap<T>::Filler filler(*out);
	filler.insert(jets, vec.begin(), vec.end());
	filler.fill();
	iEvent.put(std::move(out),name);
}

void BasicSubstructureProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	//get the collections
	edm::Handle<edm::View<pat::Jet>> h_jets;
	iEvent.getByToken(JetTok_, h_jets);

	std::vector<float> overflow, girth;

	for(const auto& i_jet : *(h_jets.product())){
		float i_girth = 0.0;

		for(unsigned k = 0; k < i_jet.numberOfDaughters(); ++k){
			const reco::Candidate* i_part = i_jet.daughter(k);
			float dR = reco::deltaR(i_jet.p4(),i_part->p4());
			float pT = i_part->pt();

			//moment calcs
			i_girth += pT*dR;
		}

		//finish moment calcs
		i_girth /= i_jet.pt();

		//store values
		girth.push_back(i_girth);
	}

	//make userfloat maps
	helpProduce(iEvent,h_jets,girth,"girth");
}

DEFINE_FWK_MODULE(BasicSubstructureProducer);

