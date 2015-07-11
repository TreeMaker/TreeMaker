// -*- C++ -*-
//
// Package:    GenLeptonRecoCand
// Class:      GenLeptonRecoCand
// 
/**\class GenLeptonRecoCand GenLeptonRecoCand.cc RA2Classic/GenLeptonRecoCand/src/GenLeptonRecoCand.cc
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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"

//
// class declaration
//

class GenLeptonRecoCand : public edm::EDProducer {
public:
	explicit GenLeptonRecoCand(const edm::ParameterSet&);
	~GenLeptonRecoCand();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	edm::InputTag PrunedGenParticleTag_;
	int pdgID_;
	
	const reco::GenParticle* BosonFound(const reco::GenParticle * particle);
	const reco::GenParticle* TauFound(const reco::GenParticle * particle);
	
	
	// ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
GenLeptonRecoCand::GenLeptonRecoCand(const edm::ParameterSet& iConfig)
{
	//register your produc
	PrunedGenParticleTag_ 				= 	iConfig.getParameter<edm::InputTag >("PrunedGenParticleTag");	
	const std::string string1("Boson");
	const std::string string1t("BosonPDGId");
	const std::string string2("Muon");
	const std::string string2t("MuonTauDecay");
	const std::string string3("Electron");
	const std::string string3t("ElectronTauDecay");
	const std::string string4("Tau");
	const std::string string4t("TauHadronic");
	produces<std::vector<reco::GenParticle> > (string1).setBranchAlias(string1);
	produces<std::vector<int> > (string1t).setBranchAlias(string1t);
	produces<std::vector<reco::GenParticle> > (string2).setBranchAlias(string2);
	produces<std::vector<int> > (string2t).setBranchAlias(string2t);
	produces<std::vector<reco::GenParticle> > (string3).setBranchAlias(string3);
	produces<std::vector<int> > (string3t).setBranchAlias(string3t);
	produces<std::vector<reco::GenParticle> > (string4).setBranchAlias(string4);
	produces<std::vector<int> > (string4t).setBranchAlias(string4t);
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
	
}


GenLeptonRecoCand::~GenLeptonRecoCand()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
GenLeptonRecoCand::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;	
	std::auto_ptr< std::vector<reco::GenParticle> > selectedBoson(new std::vector<reco::GenParticle>);
	std::auto_ptr< std::vector<int> > selectedBosonPDGId(new std::vector<int>);
	std::auto_ptr< std::vector<reco::GenParticle> > selectedMuon(new std::vector<reco::GenParticle>);
	std::auto_ptr< std::vector<int> > selectedMuonTauDecay(new std::vector<int>);
	std::auto_ptr< std::vector<reco::GenParticle> > selectedElectron(new std::vector<reco::GenParticle>);
	std::auto_ptr< std::vector<int> > selectedElectronTauDecay(new std::vector<int>);
	std::auto_ptr< std::vector<reco::GenParticle> > selectedTau(new std::vector<reco::GenParticle>);
	std::auto_ptr< std::vector<int> > selectedTauHadTronic(new std::vector<int>);
	Handle<edm::View<reco::GenParticle> > pruned;
	iEvent.getByLabel(PrunedGenParticleTag_,pruned);
	for(size_t i=0; i<pruned->size();i++)
	{
		if( (abs((*pruned)[i].pdgId() ) == 24 || abs((*pruned)[i].pdgId() ) == 23 ) && (*pruned)[i].status()==22) // needs to be checked if this workes for Z 23 as well
		{
			const reco::GenParticle * FinalBoson = BosonFound(&(*pruned)[i]);
			size_t bosonDaugthers = FinalBoson->numberOfDaughters();
			selectedBoson->push_back(*FinalBoson);
			selectedBosonPDGId->push_back(FinalBoson->pdgId());
			for(size_t ii=0;ii< bosonDaugthers; ii++)
			{
				if(abs(FinalBoson->daughter(ii)->pdgId())== 11) 
				{
					selectedElectron->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));
					selectedElectronTauDecay->push_back(0);
				}
				if(abs(FinalBoson->daughter(ii)->pdgId())== 13) 
				{
					selectedMuon->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));
					selectedMuonTauDecay->push_back(0);
				}
				if(abs(FinalBoson->daughter(ii)->pdgId())== 15) 
				{
					selectedTau->push_back(*((reco::GenParticle*) FinalBoson->daughter(ii) ));

// 					selectedTauHadTronic->push_back(0);
					const reco::GenParticle * FinalTauDecay = TauFound((reco::GenParticle*)FinalBoson->daughter(ii));
					int hadTauDecay=1;
					for(size_t iii=0; iii<FinalTauDecay->numberOfDaughters();iii++)
					{
						if(abs(FinalTauDecay->daughter(iii)->pdgId())== 11) 
						{
							selectedElectron->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
							selectedElectronTauDecay->push_back(1);
							hadTauDecay=0;
						}
						if(abs(FinalTauDecay->daughter(iii)->pdgId())== 13) 
						{
							selectedMuon->push_back(*((reco::GenParticle*) FinalTauDecay->daughter(iii) ));
							selectedMuonTauDecay->push_back(1);
							hadTauDecay=0;
						}
					}
					selectedTauHadTronic->push_back(hadTauDecay);
				}
			}

		}
	}
	const std::string string1("Boson");
	const std::string string1t("BosonPDGId");
	const std::string string2("Muon");
	const std::string string2t("MuonTauDecay");
	const std::string string3("Electron");
	const std::string string3t("ElectronTauDecay");
	const std::string string4("Tau");
	const std::string string4t("TauHadronic");
	iEvent.put(selectedBoson,string1);
	iEvent.put(selectedBosonPDGId,string1t);
	iEvent.put(selectedMuon,string2);
	iEvent.put(selectedMuonTauDecay,string2t);
	iEvent.put(selectedElectron,string3);
	iEvent.put(selectedElectronTauDecay,string3t);
	iEvent.put(selectedTau,string4);
	iEvent.put(selectedTauHadTronic,string4t);
	
}

// ------------ method called once each job just before starting event loop  ------------
void 
GenLeptonRecoCand::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenLeptonRecoCand::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
GenLeptonRecoCand::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GenLeptonRecoCand::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GenLeptonRecoCand::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GenLeptonRecoCand::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenLeptonRecoCand::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}
const reco::GenParticle* GenLeptonRecoCand::BosonFound(const reco::GenParticle * particle)
{
	for(size_t i=0;i< particle->numberOfDaughters();i++)
	{
		if(abs(particle->daughter(i)->pdgId() )== 24 || abs(particle->daughter(i)->pdgId() ) == 23 ) return BosonFound((reco::GenParticle*)particle->daughter(i));
	}
	return particle;
	
}

const reco::GenParticle* GenLeptonRecoCand::TauFound(const reco::GenParticle * particle)
{
	for(size_t i=0;i< particle->numberOfDaughters();i++)
	{
		if(abs(particle->daughter(i)->pdgId() )== 24 || abs(particle->daughter(i)->pdgId() )== 15) return TauFound((reco::GenParticle*)particle->daughter(i));
	}
	return particle;
	
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenLeptonRecoCand);
