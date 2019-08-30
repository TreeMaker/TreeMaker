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

#include "TreeMaker/Utils/interface/EnergyFractionCalculator.h"

#include "TLorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

// base class
class NamedPtrBase {
	public:
		//constructor
		NamedPtrBase() : name(""), fraction(false) {}
		NamedPtrBase(std::string name_, edm::stream::EDProducer<>* edprod, const edm::ParameterSet& iConfig) : name(name_), fraction(name.find("Fraction")!=std::string::npos) {
			if(iConfig.exists(name)) extraInfo = iConfig.getParameter<std::vector<std::string>>(name);
		}
		//destructor
		virtual ~NamedPtrBase() {}
		//accessors
		virtual void put(edm::Event& iEvent) { }
		virtual void reset() { }
		virtual void get_property(const pat::Jet& Jet) { }
		virtual void get_property(const EnergyFractionCalculator& Jet) { }
	
		//member variables
		std::string name;
		bool fraction;
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
		~NamedPtr() override {}
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
		void get_property(const pat::Jet& Jet) override { push_back(Jet.userFloat(extraInfo.at(0))); }
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
DEFAULT_NAMED_PTR(D,ecfN2b1);
DEFAULT_NAMED_PTR(D,ecfN2b2);
DEFAULT_NAMED_PTR(D,ecfN3b1);
DEFAULT_NAMED_PTR(D,ecfN3b2);
DEFAULT_NAMED_PTR(D,neutralPuppiMultiplicity);
DEFAULT_NAMED_PTR(D,neutralHadronPuppiMultiplicity);
DEFAULT_NAMED_PTR(D,photonPuppiMultiplicity);

class NamedPtr_I : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		//default for user ints
		void get_property(const pat::Jet& Jet) override { push_back(Jet.userInt(extraInfo.at(0))); }
};
DEFAULT_NAMED_PTR(I,multiplicity);
DEFAULT_NAMED_PTR(I,origIndex);

// specialized helper classes (for non-userfloats)

//----------------------------------------------------------------------------------------------------------------------------------------
//doubles

class NamedPtr_jetArea : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.jetArea()); }
};
DEFINE_NAMED_PTR(jetArea);

class NamedPtr_chargedHadronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.chargedHadronEnergyFraction()); }
};
DEFINE_NAMED_PTR(chargedHadronEnergyFraction);

class NamedPtr_neutralHadronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.neutralHadronEnergyFraction()); }
};
DEFINE_NAMED_PTR(neutralHadronEnergyFraction);

class NamedPtr_chargedEmEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.chargedEmEnergyFraction()); }
};
DEFINE_NAMED_PTR(chargedEmEnergyFraction);

class NamedPtr_neutralEmEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.neutralEmEnergyFraction()); }
};
DEFINE_NAMED_PTR(neutralEmEnergyFraction);

class NamedPtr_electronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.electronEnergyFraction()); }
};
DEFINE_NAMED_PTR(electronEnergyFraction);

class NamedPtr_photonEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.photonEnergyFraction()); }
};
DEFINE_NAMED_PTR(photonEnergyFraction);

class NamedPtr_muonEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.muonEnergyFraction()); }
};
DEFINE_NAMED_PTR(muonEnergyFraction);

class NamedPtr_hfEMEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.HFEMEnergyFraction()); }
};
DEFINE_NAMED_PTR(hfEMEnergyFraction);

class NamedPtr_hfHadronEnergyFraction : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const EnergyFractionCalculator& Jet) override { push_back(Jet.HFHadronEnergyFraction()); }
};
DEFINE_NAMED_PTR(hfHadronEnergyFraction);

class NamedPtr_bDiscriminator : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.bDiscriminator(extraInfo.at(0))); }
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
DEFAULT_NAMED_PTR(bDiscriminator,tDiscriminatorDeep);
DEFAULT_NAMED_PTR(bDiscriminator,wDiscriminatorDeep);
DEFAULT_NAMED_PTR(bDiscriminator,zDiscriminatorDeep);
DEFAULT_NAMED_PTR(bDiscriminator,hDiscriminatorDeep);
DEFAULT_NAMED_PTR(bDiscriminator,tDiscriminatorDeepDecorrel);
DEFAULT_NAMED_PTR(bDiscriminator,wDiscriminatorDeepDecorrel);
DEFAULT_NAMED_PTR(bDiscriminator,zhDiscriminatorDeepDecorrel);
//DEFAULT_NAMED_PTR(bDiscriminator,deepDoubleBDiscriminatorH);
//DEFAULT_NAMED_PTR(bDiscriminator,deepDoubleBDiscriminatorQ);
DEFAULT_NAMED_PTR(bDiscriminator,pfMassIndependentDeepDoubleBvLJetTagsProbHbb);
DEFAULT_NAMED_PTR(bDiscriminator,pfMassIndependentDeepDoubleCvLJetTagsProbHcc);
DEFAULT_NAMED_PTR(bDiscriminator,pfMassIndependentDeepDoubleCvBJetTagsProbHcc);

class NamedPtr_jecFactor : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.jecFactor(Jet.availableJECLevels().back())/Jet.jecFactor("Uncorrected")); }
};
DEFINE_NAMED_PTR(jecFactor);

//ak8 jet accessors
class NamedPtr_bDiscriminatorSubjet1 : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(!Jet.subjets(extraInfo.at(0)).empty() ? Jet.subjets(extraInfo.at(0)).at(0)->bDiscriminator(extraInfo.at(1)) : -10.); }
};
DEFINE_NAMED_PTR(bDiscriminatorSubjet1);

class NamedPtr_bDiscriminatorSubjet2 : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.subjets(extraInfo.at(0)).size() > 1 ? Jet.subjets(extraInfo.at(0)).at(1)->bDiscriminator(extraInfo.at(1)) : -10.); }
};
DEFINE_NAMED_PTR(bDiscriminatorSubjet2);

class NamedPtr_softDropMass : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		void get_property(const pat::Jet& Jet) override {
			LorentzVector fatJet;
			auto const & subjets = Jet.subjets(extraInfo.at(0));
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
		void get_property(const pat::Jet& Jet) override {
			if(extraInfo.size()==4){
				//eta,phi,eta,phi
				double eta1 = Jet.userFloat(extraInfo.at(0));
				double phi1 = Jet.userFloat(extraInfo.at(1));
				double eta2 = Jet.userFloat(extraInfo.at(2));
				double phi2 = Jet.userFloat(extraInfo.at(3));
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
		void get_property(const pat::Jet& Jet) override { push_back(Jet.chargedHadronMultiplicity()); }
};
DEFINE_NAMED_PTR(chargedHadronMultiplicity);

class NamedPtr_neutralHadronMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.neutralHadronMultiplicity()); }
};
DEFINE_NAMED_PTR(neutralHadronMultiplicity);

class NamedPtr_electronMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.electronMultiplicity()); }
};
DEFINE_NAMED_PTR(electronMultiplicity);

class NamedPtr_photonMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.photonMultiplicity()); }
};
DEFINE_NAMED_PTR(photonMultiplicity);

class NamedPtr_muonMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.muonMultiplicity()); }
};
DEFINE_NAMED_PTR(muonMultiplicity);

class NamedPtr_chargedMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.chargedMultiplicity()); }
};
DEFINE_NAMED_PTR(chargedMultiplicity);

class NamedPtr_neutralMultiplicity : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.neutralMultiplicity()); }
};
DEFINE_NAMED_PTR(neutralMultiplicity);

class NamedPtr_partonFlavor : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.partonFlavour()); }
};
DEFINE_NAMED_PTR(partonFlavor);

class NamedPtr_hadronFlavor : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.hadronFlavour()); }
};
DEFINE_NAMED_PTR(hadronFlavor);

class NamedPtr_NumBhadrons : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.jetFlavourInfo().getbHadrons().size()); }
};
DEFINE_NAMED_PTR(NumBhadrons);

class NamedPtr_NumChadrons : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		void get_property(const pat::Jet& Jet) override { push_back(Jet.jetFlavourInfo().getcHadrons().size()); }
};
DEFINE_NAMED_PTR(NumChadrons);

//----------------------------------------------------------------------------------------------------------------------------------------
//TLorentzVectors

class NamedPtr_constituents : public NamedPtr<std::vector<TLorentzVector>> {
	public:
		using NamedPtr<std::vector<TLorentzVector>>::NamedPtr;
		void get_property(const pat::Jet& Jet) override {
			std::vector<TLorentzVector> partvecs;
			for(unsigned k = 0; k < Jet.numberOfDaughters(); ++k){
				const reco::Candidate* subpart = Jet.daughter(k);
				partvecs.emplace_back(subpart->px(),subpart->py(),subpart->pz(),subpart->energy());			
			}
			std::sort(partvecs.begin(), partvecs.end(), [] (const TLorentzVector& a, const TLorentzVector& b){return a.Pt() > b.Pt();} );
			ptr->push_back(partvecs);
		}
};
DEFINE_NAMED_PTR(constituents);

class NamedPtr_subjets : public NamedPtr<std::vector<TLorentzVector>> {
	public:
		using NamedPtr<std::vector<TLorentzVector>>::NamedPtr;
		void get_property(const pat::Jet& Jet) override {
			std::vector<TLorentzVector> subvecs;
			const auto& subjets = Jet.subjets(extraInfo.at(0));
			subvecs.reserve(subjets.size());
			for (const auto& subjet : subjets) {
				const auto& p4 = subjet->correctedP4(0);
				subvecs.emplace_back(p4.px(),p4.py(),p4.pz(),p4.energy());
			}
			ptr->push_back(subvecs);
		}
};
DEFINE_NAMED_PTR(subjets);

//----------------------------------------------------------------------------------------------------------------------------------------
//subjet floats

class NamedPtr_SJD : public NamedPtr<std::vector<double>> {
	public:
		using NamedPtr<std::vector<double>>::NamedPtr;
		void get_property(const pat::Jet& Jet) override {
			std::vector<double> vec;
			const auto& subjets = Jet.subjets(extraInfo.at(0));
			vec.reserve(subjets.size());
			for (const auto& subjet : subjets) {
				vec.push_back(subjet->userFloat(extraInfo.at(1)));
			}
			ptr->push_back(vec);
		}
};
DEFAULT_NAMED_PTR(SJD,SJptD);
DEFAULT_NAMED_PTR(SJD,SJaxisminor);
DEFAULT_NAMED_PTR(SJD,SJaxismajor);

class NamedPtr_SJI : public NamedPtr<std::vector<int>> {
	public:
		using NamedPtr<std::vector<int>>::NamedPtr;
		void get_property(const pat::Jet& Jet) override {
			std::vector<int> vec;
			const auto& subjets = Jet.subjets(extraInfo.at(0));
			vec.reserve(subjets.size());
			for (const auto& subjet : subjets) {
				vec.push_back(subjet->userInt(extraInfo.at(1)));
			}
			ptr->push_back(vec);
		}
};
DEFAULT_NAMED_PTR(SJI,SJmultiplicity);

class NamedPtr_SJbDiscriminator : public NamedPtr<std::vector<double>> {
	public:
		using NamedPtr<std::vector<double>>::NamedPtr;
		void get_property(const pat::Jet& Jet) override {
			std::vector<double> vec;
			const auto& subjets = Jet.subjets(extraInfo.at(0));
			vec.reserve(subjets.size());
			for (const auto& subjet : subjets) {
				vec.push_back(subjet->bDiscriminator(extraInfo.at(1)));
			}
			ptr->push_back(vec);
		}
};
DEFAULT_NAMED_PTR(SJbDiscriminator,SJbDiscriminatorCSV);

//
// class declaration
//

class JetProperties : public edm::stream::EDProducer<> {
public:
	explicit JetProperties(const edm::ParameterSet&);
	~JetProperties() override;
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	void produce(edm::Event&, const edm::EventSetup&) override;
	std::string debugMessage(const pat::Jet& Jet, const std::string& name, int indent=0);
	
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
	for(auto & Ptr : Ptrs_){
		delete Ptr;
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
	for(auto & Ptr : Ptrs_){
		Ptr->reset();
	}

	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);
	if( Jets.isValid() ) {
		for(const auto& Jet : *Jets){
			EnergyFractionCalculator efc(Jet);
			for(auto & Ptr : Ptrs_){
				if(Ptr->fraction) Ptr->get_property(efc);
				else Ptr->get_property(Jet);
			}
			//for debugging: print out available subjet collections, btag discriminators, userfloats/ints
			//will recurse through subjet collections if any
			if(debug){
				edm::LogInfo("TreeMaker") << debugMessage(Jet,JetTag_.encode());
			}
		}
	}

	//put products
	for(auto & Ptr : Ptrs_){
		Ptr->put(iEvent);
	}

}

std::string
JetProperties::debugMessage(const pat::Jet& Jet, const std::string& name, int indent)
{
	std::string s_indent(indent,'\t');

	std::stringstream message;
	message << s_indent << name << ":\n";

	const auto& subjetLabels = Jet.subjetCollectionNames();
	message << s_indent << "subjetCollectionNames: ";
	std::copy(subjetLabels.begin(), subjetLabels.end(), std::ostream_iterator<std::string>(message, " "));
	message << "\n";
	
	const auto& btagLabels = Jet.getPairDiscri();
	message << s_indent << "btagDiscriminatorNames: ";
	for(const auto& bt : btagLabels) message << bt.first << " ";
	message << "\n";
	
	const auto& floatLabels = Jet.userFloatNames();
	message << s_indent << "userFloatNames: ";
	std::copy(floatLabels.begin(), floatLabels.end(), std::ostream_iterator<std::string>(message, " "));
	message << "\n";

	const auto& intLabels = Jet.userIntNames();
	message << s_indent << "userIntNames: ";
	std::copy(intLabels.begin(), intLabels.end(), std::ostream_iterator<std::string>(message, " "));
	message << "\n";

	std::string s_message = message.str();
	for(const auto& subjetLabel: subjetLabels){
		if(!Jet.subjets(subjetLabel).empty()) s_message += debugMessage(Jet.subjets(subjetLabel)[0], subjetLabel, indent+1);
	}

	return s_message;
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
