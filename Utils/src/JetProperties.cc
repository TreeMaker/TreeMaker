// -*- C++ -*-
//
// Package:    JetProperties
// Class:      JetProperties
// 
/**\class JetProperties JetProperties.cc RA2Classic/JetProperties/src/JetProperties.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//

// root include files
#include "TLorentzVector.h"

// system include files
#include <memory>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//enum lists of properties
enum JetPropD { d_jetArea, d_chargedHadronEnergyFraction, d_neutralHadronEnergyFraction, d_chargedEmEnergyFraction, d_neutralEmEnergyFraction,
				d_electronEnergyFraction, d_photonEnergyFraction, d_muonEnergyFraction, d_bDiscriminatorCSV, d_bDiscriminatorMVA,
				d_jecFactor, d_jecUnc, d_jerFactor, d_jerFactorUp, d_jerFactorDown, d_qgLikelihood, d_qgPtD, d_qgAxis2,
				d_prunedMass, d_PuppiSoftDropMass, d_bDiscriminatorSubjet1, d_bDiscriminatorSubjet2, d_NsubjettinessTau1, d_NsubjettinessTau2, d_NsubjettinessTau3 }; //AK8 properties
enum JetPropI { i_chargedHadronMultiplicity, i_neutralHadronMultiplicity, i_electronMultiplicity, i_photonMultiplicity,
				i_muonMultiplicity, i_NumBhadrons, i_NumChadrons, i_chargedMultiplicity, i_neutralMultiplicity, i_partonFlavor, i_hadronFlavor, i_qgMult };

// helper class
template <class T>
class NamedPtr {
	public:
		//constructor
		NamedPtr() : name("") {}
		NamedPtr(std::string name_, edm::EDProducer* edprod) : name(name_), ptr(std::make_unique<std::vector<T>>()) {
			edprod->produces<std::vector<T>>(name);
		}
		//destructor
		virtual ~NamedPtr() {}
		//accessors
		void put(edm::Event& iEvent) { iEvent.put(std::move(ptr),name); }
		void reset() { ptr.reset(new std::vector<T>()); }
		void push_back(T tmp) { ptr->push_back(tmp); }
		void setExtraInfo(const std::vector<std::string>& extraInfo_) { extraInfo = extraInfo_; }
		virtual void get_property(const pat::Jet* Jet) { }
	
		//member variables
		std::string name;
		std::unique_ptr<std::vector<T>> ptr;
		std::vector<std::string> extraInfo;
};

// specialized helper classes
template <JetPropD D>
class NamedPtrD : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		//default for user floats
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->userFloat(extraInfo.at(0))); }
};

template <JetPropI I>
class NamedPtrI : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		//default for user ints
		virtual void get_property(const pat::Jet* Jet) { push_back(Jet->userInt(extraInfo.at(0))); }
};

//define accessors (for non-userfloats)
template<> void NamedPtrD<d_jetArea>::get_property(const pat::Jet* Jet)                     { push_back(Jet->jetArea()); }
template<> void NamedPtrD<d_chargedHadronEnergyFraction>::get_property(const pat::Jet* Jet) { push_back(Jet->chargedHadronEnergyFraction()); }
template<> void NamedPtrD<d_neutralHadronEnergyFraction>::get_property(const pat::Jet* Jet) { push_back(Jet->neutralHadronEnergyFraction()); }
template<> void NamedPtrD<d_chargedEmEnergyFraction>::get_property(const pat::Jet* Jet)     { push_back(Jet->chargedEmEnergyFraction()); }
template<> void NamedPtrD<d_neutralEmEnergyFraction>::get_property(const pat::Jet* Jet)     { push_back(Jet->neutralEmEnergyFraction()); }
template<> void NamedPtrD<d_electronEnergyFraction>::get_property(const pat::Jet* Jet)      { push_back(Jet->electronEnergyFraction()); }
template<> void NamedPtrD<d_photonEnergyFraction>::get_property(const pat::Jet* Jet)        { push_back(Jet->photonEnergyFraction()); }
template<> void NamedPtrD<d_muonEnergyFraction>::get_property(const pat::Jet* Jet)          { push_back(Jet->muonEnergyFraction()); }
template<> void NamedPtrD<d_bDiscriminatorCSV>::get_property(const pat::Jet* Jet)           { push_back(Jet->bDiscriminator(extraInfo.at(0))); }
template<> void NamedPtrD<d_bDiscriminatorMVA>::get_property(const pat::Jet* Jet)           { push_back(Jet->bDiscriminator(extraInfo.at(0))); }
template<> void NamedPtrD<d_jecFactor>::get_property(const pat::Jet* Jet)                   { push_back(Jet->jecFactor(Jet->availableJECLevels().back())/Jet->jecFactor("Uncorrected")); }
//ak8 jet accessors
template<> void NamedPtrD<d_bDiscriminatorSubjet1>::get_property(const pat::Jet* Jet)       { push_back(Jet->subjets(extraInfo.at(0)).size() > 0 ? Jet->subjets(extraInfo.at(0)).at(0)->bDiscriminator(extraInfo.at(1)) : -10.); }
template<> void NamedPtrD<d_bDiscriminatorSubjet2>::get_property(const pat::Jet* Jet)       { push_back(Jet->subjets(extraInfo.at(0)).size() > 1 ? Jet->subjets(extraInfo.at(0)).at(1)->bDiscriminator(extraInfo.at(1)) : -10.); }
template<> void NamedPtrD<d_PuppiSoftDropMass>::get_property(const pat::Jet* Jet)           { 
    TLorentzVector fatJet, subjet;
    auto const & subjets = Jet->subjets(extraInfo.at(0));
    for ( auto const & it : subjets ) {
        subjet.SetPtEtaPhiM(it->correctedP4(0).pt(),it->correctedP4(0).eta(),it->correctedP4(0).phi(),it->correctedP4(0).mass());
        fatJet+=subjet;
    }
    push_back(fatJet.M());
}

template<> void NamedPtrI<i_chargedHadronMultiplicity>::get_property(const pat::Jet* Jet)   { push_back(Jet->chargedHadronMultiplicity()); }
template<> void NamedPtrI<i_neutralHadronMultiplicity>::get_property(const pat::Jet* Jet)   { push_back(Jet->neutralHadronMultiplicity()); }
template<> void NamedPtrI<i_electronMultiplicity>::get_property(const pat::Jet* Jet)        { push_back(Jet->electronMultiplicity()); }
template<> void NamedPtrI<i_photonMultiplicity>::get_property(const pat::Jet* Jet)          { push_back(Jet->photonMultiplicity()); }
template<> void NamedPtrI<i_muonMultiplicity>::get_property(const pat::Jet* Jet)            { push_back(Jet->muonMultiplicity()); }
template<> void NamedPtrI<i_NumBhadrons>::get_property(const pat::Jet* Jet)                 { push_back(Jet->jetFlavourInfo().getbHadrons().size()); }
template<> void NamedPtrI<i_NumChadrons>::get_property(const pat::Jet* Jet)                 { push_back(Jet->jetFlavourInfo().getcHadrons().size()); }
template<> void NamedPtrI<i_chargedMultiplicity>::get_property(const pat::Jet* Jet)         { push_back(Jet->chargedMultiplicity()); }
template<> void NamedPtrI<i_neutralMultiplicity>::get_property(const pat::Jet* Jet)         { push_back(Jet->neutralMultiplicity()); }
template<> void NamedPtrI<i_partonFlavor>::get_property(const pat::Jet* Jet)                { push_back(Jet->partonFlavour()); }
template<> void NamedPtrI<i_hadronFlavor>::get_property(const pat::Jet* Jet)                { push_back(Jet->hadronFlavour()); }

//
// class declaration
//

class JetProperties : public edm::EDProducer {
public:
	explicit JetProperties(const edm::ParameterSet&);
	~JetProperties();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	
	template <class T>
	void checkExtraInfo(const edm::ParameterSet& iConfig, const std::string& name, T ptr){
		if(iConfig.exists(name)) ptr->setExtraInfo(iConfig.getParameter<std::vector<std::string>>(name));
	}
	
	edm::InputTag JetTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
	std::vector<NamedPtr<int>*> IntPtrs_;
	std::vector<NamedPtr<double>*> DoublePtrs_;
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
	
	//register your products
	for(auto& p : props){
		     if(p=="chargedHadronMultiplicity"  ) { IntPtrs_.push_back(new NamedPtrI<i_chargedHadronMultiplicity>     ("chargedHadronMultiplicity",this)  ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="neutralHadronMultiplicity"  ) { IntPtrs_.push_back(new NamedPtrI<i_neutralHadronMultiplicity>     ("neutralHadronMultiplicity",this)  ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="electronMultiplicity"       ) { IntPtrs_.push_back(new NamedPtrI<i_electronMultiplicity>          ("electronMultiplicity",this)       ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="photonMultiplicity"         ) { IntPtrs_.push_back(new NamedPtrI<i_photonMultiplicity>            ("photonMultiplicity",this)         ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="muonMultiplicity"           ) { IntPtrs_.push_back(new NamedPtrI<i_muonMultiplicity>              ("muonMultiplicity",this)           ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="NumBhadrons"                ) { IntPtrs_.push_back(new NamedPtrI<i_NumBhadrons>                   ("NumBhadrons",this)                ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="NumChadrons"                ) { IntPtrs_.push_back(new NamedPtrI<i_NumChadrons>                   ("NumChadrons",this)                ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="chargedMultiplicity"        ) { IntPtrs_.push_back(new NamedPtrI<i_chargedMultiplicity>           ("chargedMultiplicity",this)        ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="neutralMultiplicity"        ) { IntPtrs_.push_back(new NamedPtrI<i_neutralMultiplicity>           ("neutralMultiplicity",this)        ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="partonFlavor"               ) { IntPtrs_.push_back(new NamedPtrI<i_partonFlavor>                  ("partonFlavor",this)               ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="hadronFlavor"               ) { IntPtrs_.push_back(new NamedPtrI<i_hadronFlavor>                  ("hadronFlavor",this)               ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="qgMult"                     ) { IntPtrs_.push_back(new NamedPtrI<i_qgMult>                        ("qgMult",this)                     ); checkExtraInfo(iConfig, p, IntPtrs_.back());    }
		else if(p=="jetArea"                    ) { DoublePtrs_.push_back(new NamedPtrD<d_jetArea>                    ("jetArea",this)                    ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="chargedHadronEnergyFraction") { DoublePtrs_.push_back(new NamedPtrD<d_chargedHadronEnergyFraction>("chargedHadronEnergyFraction",this)); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="neutralHadronEnergyFraction") { DoublePtrs_.push_back(new NamedPtrD<d_neutralHadronEnergyFraction>("neutralHadronEnergyFraction",this)); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="chargedEmEnergyFraction"    ) { DoublePtrs_.push_back(new NamedPtrD<d_chargedEmEnergyFraction>    ("chargedEmEnergyFraction",this)    ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="neutralEmEnergyFraction"    ) { DoublePtrs_.push_back(new NamedPtrD<d_neutralEmEnergyFraction>    ("neutralEmEnergyFraction",this)    ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="electronEnergyFraction"     ) { DoublePtrs_.push_back(new NamedPtrD<d_electronEnergyFraction>     ("electronEnergyFraction",this)     ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="photonEnergyFraction"       ) { DoublePtrs_.push_back(new NamedPtrD<d_photonEnergyFraction>       ("photonEnergyFraction",this)       ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="muonEnergyFraction"         ) { DoublePtrs_.push_back(new NamedPtrD<d_muonEnergyFraction>         ("muonEnergyFraction",this)         ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="bDiscriminatorCSV"          ) { DoublePtrs_.push_back(new NamedPtrD<d_bDiscriminatorCSV>          ("bDiscriminatorCSV",this)          ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="bDiscriminatorMVA"          ) { DoublePtrs_.push_back(new NamedPtrD<d_bDiscriminatorMVA>          ("bDiscriminatorMVA",this)          ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="jecFactor"                  ) { DoublePtrs_.push_back(new NamedPtrD<d_jecFactor>                  ("jecFactor",this)                  ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="jecUnc"                     ) { DoublePtrs_.push_back(new NamedPtrD<d_jecUnc>                     ("jecUnc",this)                     ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="jerFactor"                  ) { DoublePtrs_.push_back(new NamedPtrD<d_jerFactor>                  ("jerFactor",this)                  ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="jerFactorUp"                ) { DoublePtrs_.push_back(new NamedPtrD<d_jerFactorUp>                ("jerFactorUp",this)                ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="jerFactorDown"              ) { DoublePtrs_.push_back(new NamedPtrD<d_jerFactorDown>              ("jerFactorDown",this)              ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="qgLikelihood"               ) { DoublePtrs_.push_back(new NamedPtrD<d_qgLikelihood>               ("qgLikelihood",this)               ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="qgPtD"                      ) { DoublePtrs_.push_back(new NamedPtrD<d_qgPtD>                      ("qgPtD",this)                      ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="qgAxis2"                    ) { DoublePtrs_.push_back(new NamedPtrD<d_qgAxis2>                    ("qgAxis2",this)                    ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="prunedMass"                 ) { DoublePtrs_.push_back(new NamedPtrD<d_prunedMass>                 ("prunedMass",this)                 ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
        else if(p=="PuppiSoftDropMass"          ) { DoublePtrs_.push_back(new NamedPtrD<d_PuppiSoftDropMass>          ("PuppiSoftDropMass",this)          ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="NsubjettinessTau1"          ) { DoublePtrs_.push_back(new NamedPtrD<d_NsubjettinessTau1>          ("NsubjettinessTau1",this)          ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="NsubjettinessTau2"          ) { DoublePtrs_.push_back(new NamedPtrD<d_NsubjettinessTau2>          ("NsubjettinessTau2",this)          ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="NsubjettinessTau3"          ) { DoublePtrs_.push_back(new NamedPtrD<d_NsubjettinessTau3>          ("NsubjettinessTau3",this)          ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="bDiscriminatorSubjet1"      ) { DoublePtrs_.push_back(new NamedPtrD<d_bDiscriminatorSubjet1>      ("bDiscriminatorSubjet1",this)      ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else if(p=="bDiscriminatorSubjet2"      ) { DoublePtrs_.push_back(new NamedPtrD<d_bDiscriminatorSubjet2>      ("bDiscriminatorSubjet2",this)      ); checkExtraInfo(iConfig, p, DoublePtrs_.back()); }
		else std::cout << "JetsProperties: unknown property " << p << std::endl;
	}	
}


JetProperties::~JetProperties()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetProperties::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	//reset ptrs
	for(unsigned ip = 0; ip < IntPtrs_.size(); ++ip){
		IntPtrs_[ip]->reset();
	}
	for(unsigned ip = 0; ip < DoublePtrs_.size(); ++ip){
		DoublePtrs_[ip]->reset();
	}

	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);
	if( Jets.isValid() ) {
		for(auto Jet = Jets->begin();  Jet != Jets->end(); ++Jet){
			for(unsigned ip = 0; ip < IntPtrs_.size(); ++ip){
				IntPtrs_[ip]->get_property(&(*Jet));
			}
			for(unsigned ip = 0; ip < DoublePtrs_.size(); ++ip){
				DoublePtrs_[ip]->get_property(&(*Jet));
			}
			//for debugging: print out available subjet collections & btag discriminators
			if(debug){
				const auto& subjetLabels = Jet->subjetCollectionNames();
				std::cout << "subjetCollectionNames: ";
				std::copy(subjetLabels.begin(), subjetLabels.end(), std::ostream_iterator<std::string>(std::cout, " "));
				std::cout << std::endl;
				
				const auto& btagLabels = Jet->getPairDiscri();
				std::cout << "btagDiscriminatorNames: ";
				for(const auto& bt : btagLabels) std::cout << bt.first << " ";
				std::cout << std::endl;
			}
		}
	}

	//put products
	for(unsigned ip = 0; ip < IntPtrs_.size(); ++ip){
		IntPtrs_[ip]->put(iEvent);
	}
	for(unsigned ip = 0; ip < DoublePtrs_.size(); ++ip){
		DoublePtrs_[ip]->put(iEvent);
	}

}

// ------------ method called once each job just before starting event loop  ------------
void 
JetProperties::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetProperties::endJob() {
	//memory management
	for(unsigned ip = 0; ip < IntPtrs_.size(); ++ip){
		delete (IntPtrs_[ip]);
	}
	IntPtrs_.clear();
	for(unsigned ip = 0; ip < DoublePtrs_.size(); ++ip){
		delete (DoublePtrs_[ip]);
	}
	DoublePtrs_.clear();
}

// ------------ method called when starting to processes a run  ------------
void 
JetProperties::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
JetProperties::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
JetProperties::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
JetProperties::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
