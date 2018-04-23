// -*- C++ -*-
//
// Package:    JetProperties
// Class:      JetProperties
// 

// system include files
#include <memory>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PluginManager/interface/PluginFactory.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"

#include "TLorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

// base class
class NamedPtrBase {
	public:
		//constructor
		NamedPtrBase() : name("") {}
		NamedPtrBase(std::string name_, edm::stream::EDProducer<>* edprod, const edm::ParameterSet& iConfig) : name(name_) {
			if(iConfig.exists(name)) extraInfo = iConfig.getParameter<std::vector<std::string>>(name);
		}
		//destructor
		virtual ~NamedPtrBase() {}
		//accessors
		virtual void put(edm::Event& iEvent) { }
		virtual void reset() { }
		virtual void get_property(const pat::Jet* Jet) { }
	
		//member variables
		std::string name;
		std::vector<std::string> extraInfo;		
};

// helper class
template <class T>
class NamedPtr : public NamedPtrBase {
	public:
		//constructor
		NamedPtr() : NamedPtrBase() {}
		NamedPtr(std::string name_, edm::stream::EDProducer<>* edprod, const edm::ParameterSet& iConfig) : NamedPtrBase(name_,edprod,iConfig), ptr(std::make_unique<std::vector<T>>()) {
			edprod->produces<std::vector<T>>(name);
		}
		//destructor
		virtual ~NamedPtr() {}
		//accessors
		void put(edm::Event& iEvent) override { iEvent.put(std::move(ptr),name); }
		void reset() override { ptr.reset(new std::vector<T>()); }
		void push_back(T tmp) { ptr->push_back(tmp); }
	
		//member variables
		std::unique_ptr<std::vector<T>> ptr;
};

// factory
typedef edmplugin::PluginFactory<NamedPtrBase *(std::string, edm::stream::EDProducer<>*, const edm::ParameterSet&)> NamedPtrFactory;
EDM_REGISTER_PLUGINFACTORY(NamedPtrFactory, "NamedPtrFactory");
#define DEFINE_NAMED_PTR(type) DEFINE_EDM_PLUGIN(NamedPtrFactory,NamedPtr_##type,#type)
#define DEFAULT_NAMED_PTR(type,name) DEFINE_EDM_PLUGIN(NamedPtrFactory,NamedPtr_##type,#name)

// default helper classes
class NamedPtr_D : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		//default for user floats
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->userFloat(extraInfo.at(0))); }
};
DEFAULT_NAMED_PTR(D,jecUnc);
DEFAULT_NAMED_PTR(D,jerFactor);
DEFAULT_NAMED_PTR(D,jerFactorUp);
DEFAULT_NAMED_PTR(D,jerFactorDown);
DEFAULT_NAMED_PTR(D,qgLikelihood);
DEFAULT_NAMED_PTR(D,ptD);
DEFAULT_NAMED_PTR(D,axisminor);
DEFAULT_NAMED_PTR(D,axismajor);
DEFAULT_NAMED_PTR(D,prunedMass);
DEFAULT_NAMED_PTR(D,NsubjettinessTau1);
DEFAULT_NAMED_PTR(D,NsubjettinessTau2);
DEFAULT_NAMED_PTR(D,NsubjettinessTau3);
DEFAULT_NAMED_PTR(D,overflow);
DEFAULT_NAMED_PTR(D,girth);
DEFAULT_NAMED_PTR(D,momenthalf);
DEFAULT_NAMED_PTR(D,ptdrlog);

class NamedPtr_I : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		//default for user ints
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->userInt(extraInfo.at(0))); }
};
DEFAULT_NAMED_PTR(I,multiplicity);

// specialized helper classes (for non-userfloats)

//----------------------------------------------------------------------------------------------------------------------------------------
//doubles

class NamedPtr_jetArea : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->jetArea()); }
};
DEFINE_NAMED_PTR(jetArea);

class NamedPtr_chargedHadronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->chargedHadronEnergyFraction()); }
};
DEFINE_NAMED_PTR(chargedHadronEnergyFraction);

class NamedPtr_neutralHadronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->neutralHadronEnergyFraction()); }
};
DEFINE_NAMED_PTR(neutralHadronEnergyFraction);

class NamedPtr_chargedEmEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->chargedEmEnergyFraction()); }
};
DEFINE_NAMED_PTR(chargedEmEnergyFraction);

class NamedPtr_neutralEmEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->neutralEmEnergyFraction()); }
};
DEFINE_NAMED_PTR(neutralEmEnergyFraction);

class NamedPtr_electronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->electronEnergyFraction()); }
};
DEFINE_NAMED_PTR(electronEnergyFraction);

class NamedPtr_photonEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->photonEnergyFraction()); }
};
DEFINE_NAMED_PTR(photonEnergyFraction);

class NamedPtr_muonEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->muonEnergyFraction()); }
};
DEFINE_NAMED_PTR(muonEnergyFraction);

class NamedPtr_hfEMEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->HFEMEnergyFraction()); }
};
DEFINE_NAMED_PTR(hfEMEnergyFraction);

class NamedPtr_hfHadronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->HFHadronEnergyFraction()); }
};
DEFINE_NAMED_PTR(hfHadronEnergyFraction);

class NamedPtr_bDiscriminator : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->bDiscriminator(extraInfo.at(0))); }
};
DEFAULT_NAMED_PTR(bDiscriminator,bDiscriminatorCSV);
DEFAULT_NAMED_PTR(bDiscriminator,bDiscriminatorMVA);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepCSVprobb);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepCSVprobc);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepCSVprobudsg);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepCSVprobbb);
DEFAULT_NAMED_PTR(bDiscriminator,bDiscriminatorDeepCSVBvsAll);
DEFAULT_NAMED_PTR(bDiscriminator,bDiscriminatorDeepCSVCvsB);
DEFAULT_NAMED_PTR(bDiscriminator,bDiscriminatorDeepCSVCvsL);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepFlavourprobb);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepFlavourprobc);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepFlavourprobg);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepFlavourproblepb);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepFlavourprobbb);
DEFAULT_NAMED_PTR(bDiscriminator,bJetTagDeepFlavourprobuds);

class NamedPtr_jecFactor : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->jecFactor(Jet->availableJECLevels().back())/Jet->jecFactor("Uncorrected")); }
};
DEFINE_NAMED_PTR(jecFactor);

//ak8 jet accessors
class NamedPtr_bDiscriminatorSubjet1 : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->subjets(extraInfo.at(0)).size() > 0 ? Jet->subjets(extraInfo.at(0)).at(0)->bDiscriminator(extraInfo.at(1)) : -10.); }
};
DEFINE_NAMED_PTR(bDiscriminatorSubjet1);

class NamedPtr_bDiscriminatorSubjet2 : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->subjets(extraInfo.at(0)).size() > 1 ? Jet->subjets(extraInfo.at(0)).at(1)->bDiscriminator(extraInfo.at(1)) : -10.); }
};
DEFINE_NAMED_PTR(bDiscriminatorSubjet2);

class NamedPtr_softDropMass : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) {
			LorentzVector fatJet;
			auto const & subjets = Jet->subjets(extraInfo.at(0));
			for ( auto const & it : subjets ) {
				fatJet += it->correctedP4(0);
			}
			push_back(fatJet.M());
		}
};
DEFINE_NAMED_PTR(softDropMass);

//deltaR of axes for tau1_beta1, tau1_beta2
class NamedPtr_lean : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) {
			if(extraInfo.size()==4){
				//eta,phi,eta,phi
				double eta1 = Jet->userFloat(extraInfo.at(0));
				double phi1 = Jet->userFloat(extraInfo.at(1));
				double eta2 = Jet->userFloat(extraInfo.at(2));
				double phi2 = Jet->userFloat(extraInfo.at(3));
				double dphi = reco::deltaPhi(phi1,phi2);
				push_back(std::sqrt(std::pow(eta1-eta2,2)+std::pow(dphi,2)));
			}
			else push_back(-10);
		}
};
DEFINE_NAMED_PTR(lean);

//----------------------------------------------------------------------------------------------------------------------------------------
//ints

class NamedPtr_chargedHadronMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->chargedHadronMultiplicity()); }
};
DEFINE_NAMED_PTR(chargedHadronMultiplicity);

class NamedPtr_neutralHadronMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->neutralHadronMultiplicity()); }
};
DEFINE_NAMED_PTR(neutralHadronMultiplicity);

class NamedPtr_electronMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->electronMultiplicity()); }
};
DEFINE_NAMED_PTR(electronMultiplicity);

class NamedPtr_photonMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->photonMultiplicity()); }
};
DEFINE_NAMED_PTR(photonMultiplicity);

class NamedPtr_muonMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->muonMultiplicity()); }
};
DEFINE_NAMED_PTR(muonMultiplicity);

class NamedPtr_chargedMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->chargedMultiplicity()); }
};
DEFINE_NAMED_PTR(chargedMultiplicity);

class NamedPtr_neutralMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->neutralMultiplicity()); }
};
DEFINE_NAMED_PTR(neutralMultiplicity);

class NamedPtr_partonFlavor : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->partonFlavour()); }
};
DEFINE_NAMED_PTR(partonFlavor);

class NamedPtr_hadronFlavor : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->hadronFlavour()); }
};
DEFINE_NAMED_PTR(hadronFlavor);

class NamedPtr_NumBhadrons : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->jetFlavourInfo().getbHadrons().size()); }
};
DEFINE_NAMED_PTR(NumBhadrons);

class NamedPtr_NumChadrons : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->jetFlavourInfo().getcHadrons().size()); }
};
DEFINE_NAMED_PTR(NumChadrons);

//----------------------------------------------------------------------------------------------------------------------------------------
//TLorentzVectors

class NamedPtr_constituents : public NamedPtr<std::vector<TLorentzVector>> {
	public:
		using NamedPtr<std::vector<TLorentzVector>>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) {
			std::vector<TLorentzVector> partvecs;
			for(unsigned k = 0; k < Jet->numberOfDaughters(); ++k){
				const reco::Candidate* part = Jet->daughter(k);
				//for AK8, subjets stored as daughters, need to get constituents from them
				unsigned numdau = part->numberOfDaughters();
				for(unsigned m = 0; m < std::max(numdau,1u); ++m){
					const reco::Candidate* subpart = numdau==0 ? part : part->daughter(m);
					partvecs.emplace_back(subpart->px(),subpart->py(),subpart->pz(),subpart->energy());			
				}
			}
			std::sort(partvecs.begin(), partvecs.end(), [] (const TLorentzVector& a, const TLorentzVector& b){return a.Pt() > b.Pt();} );
			ptr->push_back(partvecs);
		}
};
DEFINE_NAMED_PTR(constituents);

class NamedPtr_subjets : public NamedPtr<std::vector<TLorentzVector>> {
	public:
		using NamedPtr<std::vector<TLorentzVector>>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) {
			std::vector<TLorentzVector> subvecs;
			auto const & subjets = Jet->subjets(extraInfo.at(0));
			for ( auto const & it : subjets ) {
				const auto& p4 = it->correctedP4(0);
				subvecs.emplace_back(p4.px(),p4.py(),p4.pz(),p4.energy());
			}
			ptr->push_back(subvecs);
		}
};
DEFINE_NAMED_PTR(subjets);

//
// class declaration
//

class JetProperties : public edm::stream::EDProducer<> {
public:
	explicit JetProperties(const edm::ParameterSet&);
	~JetProperties();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void produce(edm::Event&, const edm::EventSetup&) override;
	
	edm::InputTag JetTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
	std::vector<NamedPtrBase*> Ptrs_;
	bool debug;
};

//
// constructors and destructor
//
JetProperties::JetProperties(const edm::ParameterSet& iConfig)
{
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
	debug = iConfig.getParameter<bool>("debug");

	//get lists of desired properties
	std::vector<std::string> props = iConfig.getParameter<std::vector<std::string>> ("properties");
	
	auto fac = NamedPtrFactory::get();
	Ptrs_.reserve(props.size());
	//register your products
	for(auto& p : props){
		Ptrs_.push_back(fac->create(p,p,this,iConfig));
	}	
}


JetProperties::~JetProperties()
{
	//memory management
	for(unsigned ip = 0; ip < Ptrs_.size(); ++ip){
		delete (Ptrs_[ip]);
	}
	Ptrs_.clear();
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetProperties::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	//reset ptrs
	for(unsigned ip = 0; ip < Ptrs_.size(); ++ip){
		Ptrs_[ip]->reset();
	}

	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);
	if( Jets.isValid() ) {
		for(auto Jet = Jets->begin();  Jet != Jets->end(); ++Jet){
			for(unsigned ip = 0; ip < Ptrs_.size(); ++ip){
				Ptrs_[ip]->get_property(&(*Jet));
			}
			//for debugging: print out available subjet collections & btag discriminators
			if(debug){
				std::stringstream message;
				const auto& subjetLabels = Jet->subjetCollectionNames();
				message << "subjetCollectionNames: ";
				std::copy(subjetLabels.begin(), subjetLabels.end(), std::ostream_iterator<std::string>(message, " "));
				message << "\n";
				
				const auto& btagLabels = Jet->getPairDiscri();
				message << "btagDiscriminatorNames: ";
				for(const auto& bt : btagLabels) message << bt.first << " ";
				message << "\n";
				
				const auto& floatLabels = Jet->userFloatNames();
				message << "userFloatNames: ";
				std::copy(floatLabels.begin(), floatLabels.end(), std::ostream_iterator<std::string>(message, " "));
				message << "\n";

				const auto& intLabels = Jet->userIntNames();
				message << "userIntNames: ";
				std::copy(intLabels.begin(), intLabels.end(), std::ostream_iterator<std::string>(message, " "));
				message << "\n";

				edm::LogInfo("TreeMaker") << message.str();
			}
		}
	}

	//put products
	for(unsigned ip = 0; ip < Ptrs_.size(); ++ip){
		Ptrs_[ip]->put(iEvent);
	}

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetProperties::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetProperties);
