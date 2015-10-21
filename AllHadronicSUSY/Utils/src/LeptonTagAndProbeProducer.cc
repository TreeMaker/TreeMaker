// -*- C++ -*-
//
// Package:    LeptonTagAndProbeProducer
// Class:      LeptonTagAndProbeProducer
// 
/**\class LeptonTagAndProbeProducer LeptonTagAndProbeProducer.cc RA2Classic/LeptonTagAndProbeProducer/src/LeptonTagAndProbeProducer.cc
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

#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include <TRandom2.h>
#include <vector>
#include <TVector2.h>
#include <TMath.h>
#include <math.h>
#include "TLorentzVector.h"

//
// class declaration
//


class LeptonTagAndProbeProducer : public edm::EDProducer {
public:
	explicit LeptonTagAndProbeProducer(const edm::ParameterSet&);
	~LeptonTagAndProbeProducer();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	double GetMinDeltaPhi(reco::LeafCandidate lepCand, edm::Handle< edm::View<pat::Jet> > Jets);
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	edm::InputTag TagPFCandTag_, ProbePFCandTag_, ProbeTestPFCandTag_, JetTag_;
	double deltaR(double eta1, double phi1, double eta2, double phi2);
	double DeltaT(unsigned int i, edm::Handle< edm::View<pat::Jet> > Jets );

	
	
	// ----------member data ---------------------------
};


double LeptonTagAndProbeProducer::GetMinDeltaPhi(reco::LeafCandidate lepCand, edm::Handle< edm::View<pat::Jet> > Jets)
{
	double result =9999;

	
	double dpnhat[3];
	unsigned int goodcount=0;
	for(int i=0; i<3; ++i)dpnhat[i]=-999;
	reco::MET::LorentzVector metLorentz(0,0,0,0);
		metLorentz=lepCand.p4();
	if( Jets.isValid() ) {
		for(unsigned int i=0; i<Jets->size();i++){
			if(goodcount<3 && Jets->at(i).pt()>30){ //make this pt cut configurable
                float dphi=std::abs(reco::deltaPhi(Jets->at(i).phi(),metLorentz.phi()));
								float dT=DeltaT(i, Jets);
								if(dT/metLorentz.pt()>=1.0)dpnhat[goodcount]=dphi/(TMath::Pi()/2.0);
								else dpnhat[goodcount]=dphi/asin(dT/metLorentz.pt());
								++goodcount;
			}
		}
	}
	for(int i=0; i<3; ++i){
		if(result>fabs(dpnhat[i]))result=fabs(dpnhat[i]);
	}
	
	return result;
}

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
LeptonTagAndProbeProducer::LeptonTagAndProbeProducer(const edm::ParameterSet& iConfig)
{
	//register your produc
	TagPFCandTag_ 				= 	iConfig.getParameter<edm::InputTag >("TagPFCand");
	ProbePFCandTag_ 				= 	iConfig.getParameter<edm::InputTag >("ProbePFCand");
	ProbeTestPFCandTag_ 				= 	iConfig.getParameter<edm::InputTag >("ProbeTestPFCand");
	JetTag_ = iConfig.getParameter<edm::InputTag> ("JetTag");

	
	const std::string string1("Tag");
	produces<std::vector<reco::LeafCandidate> > (string1).setBranchAlias(string1);
	const std::string string2("Probe");
	produces<std::vector<reco::LeafCandidate> > (string2).setBranchAlias(string2);
	const std::string string2t("PassingOrFail");
	produces<std::vector<int> > (string2t).setBranchAlias(string2t);
	const std::string string2tt("InvariantMass");
	produces<std::vector<double> > (string2tt).setBranchAlias(string2tt);
	const std::string string3("MinDeltaPhiN");
	produces<double> (string3).setBranchAlias(string3);
}


LeptonTagAndProbeProducer::~LeptonTagAndProbeProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
LeptonTagAndProbeProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	std::vector<reco::LeafCandidate> tagCandidate_, probeCandidate_;
	std::auto_ptr< std::vector<int> > passing_(new std::vector<int>);
	std::auto_ptr< std::vector<double> > invariantMass_ (new std::vector<double>);
	edm::Handle< edm::View<reco::LeafCandidate> > ProbeCands;
	iEvent.getByLabel(ProbePFCandTag_,ProbeCands);
	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByLabel(JetTag_,Jets);
	double minDeltaPhiTemp=0;
	if( !ProbeCands.isValid() ) 
	{
		std::cout<<"TagCand invalide, with tag: "<<ProbePFCandTag_.label()<<std::endl;
	}
	edm::Handle< edm::View<reco::LeafCandidate> > TagCands;
	iEvent.getByLabel(TagPFCandTag_,TagCands);
	if( !TagCands.isValid() ) 
	{
		std::cout<<"ProbeCand invalide, with tag: "<<TagPFCandTag_.label()<<std::endl;
	}
	edm::Handle< edm::View<reco::LeafCandidate> > ProbeTestCands;
	iEvent.getByLabel(ProbeTestPFCandTag_,ProbeTestCands);
	if( !ProbeTestCands.isValid() ) 
	{
		std::cout<<"TagCand invalide, with tag: "<<ProbeTestPFCandTag_.label()<<std::endl;
	}
	if(TagCands.isValid() && ProbeCands.isValid() && ProbeTestCands.isValid())
	{
		if(TagCands->size()>0 && ProbeCands->size()>1)
		{
			// select randomly the tag object from collection
			unsigned int tagSize = TagCands->size();
			TRandom2 * random = new TRandom2(0);
			int tagIndex = (int) random->Uniform(tagSize);
			tagCandidate_.push_back(TagCands->at(tagIndex));
			// compute min deltaPhi for tag lepton which is assmued to be the neutrino in w decay
			minDeltaPhiTemp = GetMinDeltaPhi(TagCands->at(tagIndex),Jets);
			// 		std::cout<<"TagSize: "<<tagSize<<"Random number: "<< index<<"\n";
			// do anti matching with probe collection
			int tagInProbeIndex = -1;
			double tagEta = TagCands->at(tagIndex).eta();
			double tagPhi = TagCands->at(tagIndex).phi();
			int tagCharge = TagCands->at(tagIndex).charge();
			double tagE = TagCands->at(tagIndex).energy();
			double tagPx = TagCands->at(tagIndex).px();
			double tagPy = TagCands->at(tagIndex).py();
			double tagPz = TagCands->at(tagIndex).pz();
			TLorentzVector TagLorentzReco(tagPx, tagPy, tagPz, tagE);
			for(unsigned int i=0; i<ProbeCands->size();i++)
			{
				
				double probeEta = ProbeCands->at(i).eta();
				double probePhi = ProbeCands->at(i).phi();
				if( std::abs(ProbeCands->at(i).pt() - TagCands->at(tagIndex).pt() )/TagCands->at(tagIndex).pt() < 0.5 && deltaR(probeEta,probePhi,tagEta,tagPhi)<0.03 )
				{
					if(tagInProbeIndex!=-1)std::cout<<"Warning more than one match found!!"<<std::endl;
					tagInProbeIndex=i;
				}
			}
			if(tagInProbeIndex==-1)std::cout<<"Error no match found!"<<std::endl;
			else
			{
				
				for(unsigned int i=0; i<ProbeCands->size();i++)
				{
					if((int)i==tagInProbeIndex)continue;
					if(tagCharge == ProbeCands->at(i).charge()) continue;
					probeCandidate_.push_back(ProbeCands->at(i));
					double probeE = ProbeCands->at(i).energy();
					double probePx = ProbeCands->at(i).px();
					double probePy = ProbeCands->at(i).py();
					double probePz = ProbeCands->at(i).pz();
					TLorentzVector ProbeLorentzReco(probePx, probePy, probePz, probeE);
					ProbeLorentzReco = ProbeLorentzReco + TagLorentzReco;
					invariantMass_->push_back(ProbeLorentzReco.M() );
					double probeEta = ProbeCands->at(i).eta();
					double probePhi = ProbeCands->at(i).phi();
					int matched=0;
					for(unsigned int ii=0; ii<ProbeTestCands->size();ii++)
					{
						double TagEta = ProbeTestCands->at(ii).eta();
						double TagPhi = ProbeTestCands->at(ii).phi();
						if( std::abs(ProbeTestCands->at(ii).pt() - TagCands->at(tagIndex).pt() )/TagCands->at(tagIndex).pt() < 0.5 && deltaR(TagEta,TagPhi,tagEta,tagPhi)<0.03 ) continue;
						if( std::abs(ProbeCands->at(i).pt() - ProbeTestCands->at(ii).pt() )/ProbeTestCands->at(ii).pt() < 0.5 && deltaR(probeEta,probePhi,TagEta,TagPhi)<0.03 )
						{
							matched++;
						}
					}
					passing_->push_back(matched );
				}
			}
		}
	}

	const std::string string1("Tag");
	
	const std::string string2("Probe");
	const std::string string2t("PassingOrFail");
	const std::string string2tt("InvariantMass");
	const std::string string3("MinDeltaPhiN");
	
	std::auto_ptr<std::vector<reco::LeafCandidate> > htp1(new std::vector<reco::LeafCandidate>(tagCandidate_));
	iEvent.put(htp1,string1);
	std::auto_ptr<std::vector<reco::LeafCandidate> > htp2(new std::vector<reco::LeafCandidate>(probeCandidate_));
	iEvent.put(htp2,string2);
	iEvent.put(passing_,string2t);
	iEvent.put(invariantMass_,string2tt);
std::auto_ptr<double> htp6(new double(minDeltaPhiTemp));
iEvent.put(htp6,string3);	

	
}

// ------------ method called once each job just before starting event loop  ------------
void 
LeptonTagAndProbeProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LeptonTagAndProbeProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
LeptonTagAndProbeProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
LeptonTagAndProbeProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
LeptonTagAndProbeProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
LeptonTagAndProbeProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonTagAndProbeProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

double LeptonTagAndProbeProducer::deltaR(double eta1, double phi1, double eta2, double phi2)
{
	double deta = eta1-eta2;
	double dphi = TVector2::Phi_mpi_pi(phi1-phi2);
	return sqrt(deta * deta + dphi *dphi); 
}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonTagAndProbeProducer);

double LeptonTagAndProbeProducer::DeltaT(unsigned int i, edm::Handle< edm::View<pat::Jet> > Jets ){
	
	double deltaT=0;
	float jres=0.1;
	double sum=0;
	if( Jets.isValid() ) {
		for(unsigned int j=0; j<Jets->size(); ++j){
			if(j==i)continue;
			sum=sum+(Jets->at(i).px()*Jets->at(j).py()-Jets->at(j).px()*Jets->at(i).py()) * (Jets->at(i).px()*Jets->at(j).py()-Jets->at(j).px()*Jets->at(i).py());
		}
		deltaT=jres*sqrt(sum)/Jets->at(i).pt();
		
	}
	
	return deltaT;
}
