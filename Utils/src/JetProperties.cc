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


// system include files
#include <memory>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>

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
				d_electronEnergyFraction, d_photonEnergyFraction, d_muonEnergyFraction, d_bDiscriminatorUser, d_bDiscriminatorMVA, d_bDiscriminatorSimpleCSV, d_qgLikelihood };
enum JetPropI { i_chargedHadronMultiplicity, i_neutralHadronMultiplicity, i_electronMultiplicity, i_photonMultiplicity,
				i_muonMultiplicity, i_NumBhadrons, i_NumChadrons, i_chargedMultiplicity, i_neutralMultiplicity, i_partonFlavor, i_hadronFlavor };
enum JetAK8PropD { d_prunedMass, d_bDiscriminatorSubjet1, d_bDiscriminatorSubjet2, d_NsubjettinessTau1, d_NsubjettinessTau2, d_NsubjettinessTau3 };

// helper class
template <class T>
class NamedPtr {
	public:
		//constructor
		NamedPtr() : name("") {}
		NamedPtr(std::string name_, edm::EDProducer* edprod) : name(name_), ptr(new std::vector<T>()) {
			edprod->produces<std::vector<T>>(name).setBranchAlias(name);
		}
		//destructor
		virtual ~NamedPtr() {}
		//accessors
		void put(edm::Event& iEvent) { iEvent.put(ptr,name); }
		void reset() { ptr.reset(new std::vector<T>()); }
		void push_back(T tmp) { ptr->push_back(tmp); }
		virtual void get_property(const pat::Jet* Jet) { }
	
		//member variables
		std::string name;
		std::auto_ptr< std::vector<T> > ptr;
};

// specialized helper classes
template <JetPropD D>
class NamedPtrD : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { }
};

template <JetPropI I>
class NamedPtrI : public NamedPtr<int> {
	public:
		using NamedPtr<int>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { }
};

template <JetAK8PropD D>
class NamedPtrAK8D : public NamedPtr<double> {
	public:
		using NamedPtr<double>::NamedPtr;
		virtual void get_property(const pat::Jet* Jet) { }
};

//define accessors
template<> void NamedPtrD<d_jetArea>::get_property(const pat::Jet* Jet)                     { push_back(Jet->jetArea()); }
template<> void NamedPtrD<d_chargedHadronEnergyFraction>::get_property(const pat::Jet* Jet) { push_back(Jet->chargedHadronEnergyFraction()); }
template<> void NamedPtrD<d_neutralHadronEnergyFraction>::get_property(const pat::Jet* Jet) { push_back(Jet->neutralHadronEnergyFraction()); }
template<> void NamedPtrD<d_chargedEmEnergyFraction>::get_property(const pat::Jet* Jet)     { push_back(Jet->chargedEmEnergyFraction()); }
template<> void NamedPtrD<d_neutralEmEnergyFraction>::get_property(const pat::Jet* Jet)     { push_back(Jet->neutralEmEnergyFraction()); }
template<> void NamedPtrD<d_electronEnergyFraction>::get_property(const pat::Jet* Jet)      { push_back(Jet->electronEnergyFraction()); }
template<> void NamedPtrD<d_photonEnergyFraction>::get_property(const pat::Jet* Jet)        { push_back(Jet->photonEnergyFraction()); }
template<> void NamedPtrD<d_muonEnergyFraction>::get_property(const pat::Jet* Jet)          { push_back(Jet->muonEnergyFraction()); }
//bDiscriminatorUser gets special attention
template<> void NamedPtrD<d_bDiscriminatorMVA>::get_property(const pat::Jet* Jet)           { push_back(Jet->bDiscriminator("combinedMVABJetTags")); }
template<> void NamedPtrD<d_bDiscriminatorSimpleCSV>::get_property(const pat::Jet* Jet)     { push_back(Jet->bDiscriminator("combinedSecondaryVertexBJetTags")); }
//qgLikelihood gets special attention
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
//ak8 jet accessors
template<> void NamedPtrAK8D<d_prunedMass>::get_property(const pat::Jet* Jet)               { push_back(Jet->userFloat("ak8PFJetsCHSPrunedMass")); }
//bDiscriminatorSubjet1,2 get special attention
template<> void NamedPtrAK8D<d_NsubjettinessTau1>::get_property(const pat::Jet* Jet)        { push_back(Jet->userFloat("NjettinessAK8:tau1")); }
template<> void NamedPtrAK8D<d_NsubjettinessTau2>::get_property(const pat::Jet* Jet)        { push_back(Jet->userFloat("NjettinessAK8:tau2")); }
template<> void NamedPtrAK8D<d_NsubjettinessTau3>::get_property(const pat::Jet* Jet)        { push_back(Jet->userFloat("NjettinessAK8:tau3")); }

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
	edm::InputTag JetTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
	edm::InputTag QGTag_;
	edm::EDGetTokenT<edm::ValueMap<float>> QGTok_;
	std::string   btagname_;
	bool doQG_, doAK8_;
	std::vector<NamedPtr<int>*> IntPtrs_;
	std::vector<NamedPtr<double>*> DoublePtrs_;
	NamedPtr<double> *DoublePtr_bDiscriminatorUser_, *DoublePtr_qgLikelihood_;
	NamedPtr<double> *DoublePtr_bDiscriminatorSubjet1_, *DoublePtr_bDiscriminatorSubjet2_;
};

//
// constructors and destructor
//
JetProperties::JetProperties(const edm::ParameterSet& iConfig)
{
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	btagname_ = iConfig.getParameter<std::string>  ("BTagInputTag");
	QGTag_ = iConfig.getParameter<edm::InputTag>("QGTag");
	doAK8_ = iConfig.getParameter<bool>("AK8");
	doQG_ = (QGTag_.label().size()>0);
	
	JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
	if(doQG_) QGTok_ = consumes<edm::ValueMap<float>>(QGTag_);
	
	//register your products
	/* Examples
	 *   produces<ExampleData2>();
	 * 
	 *   //if do put with a label
	 *   produces<ExampleData2>("label");
	 * 
	 *   //if you want to put into the Run
	 *   produces<ExampleData2,InRun>();
	 */
	//now do what ever other initialization is needed
	//register your products
	if(doAK8_){
		DoublePtrs_.push_back(new NamedPtrAK8D<d_prunedMass>       ("prunedMass",this)       );
		DoublePtrs_.push_back(new NamedPtrAK8D<d_NsubjettinessTau1>("NsubjettinessTau1",this));
		DoublePtrs_.push_back(new NamedPtrAK8D<d_NsubjettinessTau2>("NsubjettinessTau2",this));
		DoublePtrs_.push_back(new NamedPtrAK8D<d_NsubjettinessTau3>("NsubjettinessTau3",this));
		
		DoublePtr_bDiscriminatorSubjet1_ = new NamedPtrAK8D<d_bDiscriminatorSubjet1>("bDiscriminatorSubjet1",this);
		DoublePtr_bDiscriminatorSubjet2_ = new NamedPtrAK8D<d_bDiscriminatorSubjet2>("bDiscriminatorSubjet2",this);
		DoublePtr_bDiscriminatorUser_ = NULL;
		DoublePtr_qgLikelihood_ = NULL;
	}
	else {
		IntPtrs_.push_back(new NamedPtrI<i_chargedHadronMultiplicity>("chargedHadronMultiplicity",this));
		IntPtrs_.push_back(new NamedPtrI<i_neutralHadronMultiplicity>("neutralHadronMultiplicity",this));
		IntPtrs_.push_back(new NamedPtrI<i_electronMultiplicity>     ("electronMultiplicity",this)     );
		IntPtrs_.push_back(new NamedPtrI<i_photonMultiplicity>       ("photonMultiplicity",this)       );
		IntPtrs_.push_back(new NamedPtrI<i_muonMultiplicity>         ("muonMultiplicity",this)         );
		IntPtrs_.push_back(new NamedPtrI<i_NumBhadrons>              ("NumBhadrons",this)              );
		IntPtrs_.push_back(new NamedPtrI<i_NumChadrons>              ("NumChadrons",this)              );
		IntPtrs_.push_back(new NamedPtrI<i_chargedMultiplicity>      ("chargedMultiplicity",this)      );
		IntPtrs_.push_back(new NamedPtrI<i_neutralMultiplicity>      ("neutralMultiplicity",this)      );
		IntPtrs_.push_back(new NamedPtrI<i_partonFlavor>             ("partonFlavor",this)             );
		IntPtrs_.push_back(new NamedPtrI<i_hadronFlavor>             ("hadronFlavor",this)             );

		DoublePtrs_.push_back(new NamedPtrD<d_jetArea>                    ("jetArea",this)                    );
		DoublePtrs_.push_back(new NamedPtrD<d_chargedHadronEnergyFraction>("chargedHadronEnergyFraction",this));
		DoublePtrs_.push_back(new NamedPtrD<d_neutralHadronEnergyFraction>("neutralHadronEnergyFraction",this));
		DoublePtrs_.push_back(new NamedPtrD<d_chargedEmEnergyFraction>    ("chargedEmEnergyFraction",this)    );
		DoublePtrs_.push_back(new NamedPtrD<d_neutralEmEnergyFraction>    ("neutralEmEnergyFraction",this)    );
		DoublePtrs_.push_back(new NamedPtrD<d_electronEnergyFraction>     ("electronEnergyFraction",this)     );
		DoublePtrs_.push_back(new NamedPtrD<d_photonEnergyFraction>       ("photonEnergyFraction",this)       );
		DoublePtrs_.push_back(new NamedPtrD<d_muonEnergyFraction>         ("muonEnergyFraction",this)         );
		DoublePtrs_.push_back(new NamedPtrD<d_bDiscriminatorMVA>          ("bDiscriminatorMVA",this)          );
		DoublePtrs_.push_back(new NamedPtrD<d_bDiscriminatorSimpleCSV>    ("bDiscriminatorSimpleCSV",this)    );
		
		DoublePtr_bDiscriminatorUser_ = new NamedPtrD<d_bDiscriminatorUser>("bDiscriminatorUser",this);
		DoublePtr_qgLikelihood_ = new NamedPtrD<d_qgLikelihood>("qgLikelihood",this);
		DoublePtr_bDiscriminatorSubjet1_ = NULL;
		DoublePtr_bDiscriminatorSubjet2_ = NULL;
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
	if(DoublePtr_bDiscriminatorSubjet1_) DoublePtr_bDiscriminatorSubjet1_->reset();
	if(DoublePtr_bDiscriminatorSubjet2_) DoublePtr_bDiscriminatorSubjet2_->reset();
	if(DoublePtr_bDiscriminatorUser_) DoublePtr_bDiscriminatorUser_->reset();
	if(DoublePtr_qgLikelihood_) DoublePtr_qgLikelihood_->reset();

	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);
	edm::Handle<edm::ValueMap<float>> qgHandle;
	if(doQG_) iEvent.getByToken(QGTok_, qgHandle);
	bool qgValid = qgHandle.isValid();
	if( Jets.isValid() ) {
		for(auto Jet = Jets->begin();  Jet != Jets->end(); ++Jet){
			for(unsigned ip = 0; ip < IntPtrs_.size(); ++ip){
				IntPtrs_[ip]->get_property(&(*Jet));
			}
			for(unsigned ip = 0; ip < DoublePtrs_.size(); ++ip){
				DoublePtrs_[ip]->get_property(&(*Jet));
			}
			//special attention for a few properties
			if(doAK8_) {
				//for debugging: print out available subjet collections
				//std::vector<std::string> labels = Jet->subjetCollectionNames();
				//std::copy(labels.begin(), labels.end(), std::ostream_iterator<std::string>(std::cout, " "));
				DoublePtr_bDiscriminatorSubjet1_->push_back( Jet->subjets("SoftDrop").size() > 0 ? Jet->subjets("SoftDrop").at(0)->bDiscriminator(btagname_) : -10. );
				DoublePtr_bDiscriminatorSubjet2_->push_back( Jet->subjets("SoftDrop").size() > 1 ? Jet->subjets("SoftDrop").at(1)->bDiscriminator(btagname_) : -10. );
			}
			
			if(DoublePtr_bDiscriminatorUser_) DoublePtr_bDiscriminatorUser_->push_back( Jet->bDiscriminator(btagname_) );
			
			if(qgValid && DoublePtr_qgLikelihood_){
				edm::RefToBase<pat::Jet> jetRef(edm::Ref<edm::View<pat::Jet> >(Jets, Jet - Jets->begin()));
				float qgLikelihood_ = (*qgHandle)[jetRef];
				DoublePtr_qgLikelihood_->push_back( qgLikelihood_ );
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
	if(DoublePtr_bDiscriminatorSubjet1_) DoublePtr_bDiscriminatorSubjet1_->put(iEvent);
	if(DoublePtr_bDiscriminatorSubjet2_) DoublePtr_bDiscriminatorSubjet2_->put(iEvent);
	if(DoublePtr_bDiscriminatorUser_) DoublePtr_bDiscriminatorUser_->put(iEvent);
	if(DoublePtr_qgLikelihood_) DoublePtr_qgLikelihood_->put(iEvent);

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
	delete DoublePtr_bDiscriminatorSubjet1_;
	delete DoublePtr_bDiscriminatorSubjet2_;
	delete DoublePtr_bDiscriminatorUser_;
	delete DoublePtr_qgLikelihood_;
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
