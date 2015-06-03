// -*- C++ -*-
//
// Package:    LostLepton/ActivityProducer
// Class:      ActivityProducer
// 
/**\class ActivityProducer ActivityProducer.cc LostLepton/ActivityProducer/plugins/ActivityProducer.cc
 * 
 D escription: [one line class s*ummary]
 
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Florent Sylvain Lacroix
//         Created:  Fri, 22 May 2015 13:37:22 GMT
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
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/Common/interface/ValueMap.h"
// #include "LostLepton/Tool/Activity.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"

//
// class declaration
//

class ActivityProducer : public edm::EDProducer {
public:
	explicit ActivityProducer(const edm::ParameterSet&);
	~ActivityProducer();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() override;
	virtual void produce(edm::Event&, const edm::EventSetup&) override;
	virtual void endJob() override;
	
	edm::InputTag objectSource_, objectMatchSource_;
	unsigned int objectTyp_, activityTyp_;
	double maxDeltaR_;
	edm::InputTag jetSrc_;
	
	//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
	//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
	//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
	//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
	
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
ActivityProducer::ActivityProducer(const edm::ParameterSet& iConfig)
{
	objectSource_       = iConfig.getParameter<edm::InputTag>("objectSource"); // probe shource
	objectMatchSource_ = iConfig.getParameter<edm::InputTag>("objectMatchSource"); // probe shource
	objectTyp_ = iConfig.getParameter<int>("objectTyp"); // 0 muon, 1 electron, 2 isolated track
	activityTyp_ = iConfig.getParameter<int>("activityTyp");
	maxDeltaR_= iConfig.getParameter<double>("maxDeltaR");
	jetSrc_ = iConfig.getParameter<edm::InputTag>("jetSrc");
	
// 	produces<edm::ValueMap<float> >("miniIso");
	produces<edm::ValueMap<float> >("Activity");
	produces<edm::ValueMap<float> >("Passing");
// 	const std::string string1("PassingProbes");
// 	produces<std::vector<pat::Muon> > (string1).setBranchAlias(string1);
	
}


ActivityProducer::~ActivityProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
ActivityProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	std::vector<pat::Muon> probePassingCandidate_;
	edm::Handle<std::vector<pat::Jet> > jets;
	iEvent.getByLabel(jetSrc_, jets);
	//object

	
	// prepare vector for output
	std::vector<float> values;
	std::vector<float> passing;
	//for (std::vector<pat::Muon>::const_iterator m = object->begin(); m != object->end(); ++m)
	
	// convert into ValueMap and store	

	if(objectTyp_==1)
	{
		edm::Handle<std::vector<pat::Muon> > object;
		iEvent.getByLabel(objectSource_, object);
		edm::Handle<std::vector<pat::Muon> > objectMatch;
		iEvent.getByLabel(objectMatchSource_, objectMatch);
		for(unsigned int i=0; i<object->size();i++)
		{
			float activity=0;
			for(unsigned int ii=0; ii<jets->size();ii++)
			{
				if( deltaR(object->at(i).eta(),object->at(i).phi(),jets->at(ii).eta(),jets->at(ii).phi()) < maxDeltaR_)
				{
					if(activityTyp_==0)
					{
						activity+= jets->at(ii).pt() * (jets->at(ii).chargedHadronEnergyFraction() + jets->at(ii).chargedEmEnergyFraction() );
					}
					else 
						std::cout<<"ActivityProducer::Error activityTyp_: "<<activityTyp_<<" not defined please check input value!"<<std::endl;
				}
			}
			values.push_back(activity);
			// check if the probe object can be matched to an object from the objectMatchSource collection if so passing if not failing
			float passingTemp=0;
			for(unsigned int ii=0; ii< objectMatch->size();ii++)
			{
				if(deltaR(object->at(i).eta(),object->at(i).phi(),objectMatch->at(ii).eta(),objectMatch->at(ii).phi() ) < 0.07&& std::abs(object->at(i).pt() - objectMatch->at(ii).pt() )/objectMatch->at(ii).pt() < 0.4)
				{
					passingTemp++;
					if(passingTemp>1.5) continue;
					probePassingCandidate_.push_back(object->at(i));
				}
			}
			passing.push_back(passingTemp);
			if(passingTemp>1) std::cout<<"Warning 2 have been matched!!!"<<std::endl;
		}
// 		std::cout<<"Amount of object: "<<object->size()<<" amount of activity variables in vector to be stored: "<<values.size()<<std::endl;
		std::auto_ptr<ValueMap<float> > valMap2(new ValueMap<float>());
		ValueMap<float>::Filler filler2(*valMap2);
		filler2.insert(object, values.begin(), values.end());
		filler2.fill();
		iEvent.put(valMap2, "Activity");
		std::auto_ptr<ValueMap<float> > valMap1(new ValueMap<float>());
		ValueMap<float>::Filler filler1(*valMap1);
		filler1.insert(object, passing.begin(), passing.end());
		filler1.fill();
		iEvent.put(valMap1, "Passing");
// 		const std::string string1("PassingProbes");
// 		if(probePassingCandidate_.size()<1)std::cout<<"No PassingCand filled"<<std::endl;
// 		std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(probePassingCandidate_));
// 		iEvent.put(htp1,string1);
// 		std::cout<<"Event Dont!"<<std::endl;
	}
	else if(objectTyp_==11)
	{
// 		edm::Handle<std::vector<pat::Muon> > object;
// 		iEvent.getByLabel(objectSource_, object);
		edm::Handle<edm::View< pat::PackedCandidate> >object;
	        iEvent.getByLabel(objectSource_, object);
		edm::Handle<std::vector<pat::Muon> > objectMatch;
		iEvent.getByLabel(objectMatchSource_, objectMatch);
		for(unsigned int i=0; i<object->size();i++)
		{
		  
			float activity=0;
			for(unsigned int ii=0; ii<jets->size();ii++)
			{
				if( deltaR(object->at(i).eta(),object->at(i).phi(),jets->at(ii).eta(),jets->at(ii).phi()) < maxDeltaR_)
				{
					if(activityTyp_==0)
					{
						activity+= jets->at(ii).pt() * (jets->at(ii).chargedHadronEnergyFraction() + jets->at(ii).chargedEmEnergyFraction() );
					}
					else 
						std::cout<<"ActivityProducer::Error activityTyp_: "<<activityTyp_<<" not defined please check input value!"<<std::endl;
				}
			}
			values.push_back(activity);
			// check if the probe object can be matched to an object from the objectMatchSource collection if so passing if not failing
			float passingTemp=0;
			for(unsigned int ii=0; ii< objectMatch->size();ii++)
			{
				if(deltaR(object->at(i).eta(),object->at(i).phi(),objectMatch->at(ii).eta(),objectMatch->at(ii).phi() ) < 0.07&& std::abs(object->at(i).pt() - objectMatch->at(ii).pt() )/objectMatch->at(ii).pt() < 0.4)
				{
					passingTemp++;
					if(passingTemp>1.5) continue;
// 					probePassingCandidate_.push_back(object->at(i));
				}
			}
			passing.push_back(passingTemp);
			if(passingTemp>1) std::cout<<"Warning 2 have been matched!!!"<<std::endl;
		}
// 		std::cout<<"Amount of object: "<<object->size()<<" amount of activity variables in vector to be stored: "<<values.size()<<std::endl;
		std::auto_ptr<ValueMap<float> > valMap2(new ValueMap<float>());
		ValueMap<float>::Filler filler2(*valMap2);
		filler2.insert(object, values.begin(), values.end());
		filler2.fill();
		iEvent.put(valMap2, "Activity");
		std::auto_ptr<ValueMap<float> > valMap1(new ValueMap<float>());
		ValueMap<float>::Filler filler1(*valMap1);
		filler1.insert(object, passing.begin(), passing.end());
		filler1.fill();
		iEvent.put(valMap1, "Passing");
// 		const std::string string1("PassingProbes");
// 		if(probePassingCandidate_.size()<1)std::cout<<"No PassingCand filled"<<std::endl;
// 		std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(probePassingCandidate_));
// 		iEvent.put(htp1,string1);
// 		std::cout<<"Event Dont!"<<std::endl;
	}
	
	
	
	
	
	else if(objectTyp_==2)
	{
		edm::Handle<std::vector<pat::Electron> > object;
		iEvent.getByLabel(objectSource_, object);
		edm::Handle<std::vector<pat::Electron> > objectMatch;
		iEvent.getByLabel(objectMatchSource_, objectMatch);
		for(unsigned int i=0; i<object->size();i++)
		{
			float activity=0;
			for(unsigned int ii=0; ii<jets->size();ii++)
			{
				if( deltaR(object->at(i).eta(),object->at(i).phi(),jets->at(ii).eta(),jets->at(ii).phi()) < maxDeltaR_)
				{
					if(activityTyp_==0)
					{
						activity+= jets->at(ii).pt() * (jets->at(ii).chargedHadronEnergyFraction() );
					}
					else 
						std::cout<<"ActivityProducer::Error activityTyp_: "<<activityTyp_<<" not defined please check input value!"<<std::endl;
				}
			}
			values.push_back(activity);
			// check if the probe object can be matched to an object from the objectMatchSource collection if so passing if not failing
			float passingTemp=0;
			for(unsigned int ii=0; ii< objectMatch->size();ii++)
			{
				if(deltaR(object->at(i).eta(),object->at(i).phi(),objectMatch->at(ii).eta(),objectMatch->at(ii).phi() ) < 0.07&& std::abs(object->at(i).pt() - objectMatch->at(ii).pt() )/objectMatch->at(ii).pt() < 0.4)
				{
					passingTemp++;
					if(passingTemp>1.5) continue;
					
				}
			}
			passing.push_back(passingTemp);
			if(passingTemp>1) std::cout<<"Warning 2 have been matched!!!"<<std::endl;
		}
		// 		std::cout<<"Amount of object: "<<object->size()<<" amount of activity variables in vector to be stored: "<<values.size()<<std::endl;
		std::auto_ptr<ValueMap<float> > valMap2(new ValueMap<float>());
		ValueMap<float>::Filler filler2(*valMap2);
		filler2.insert(object, values.begin(), values.end());
		filler2.fill();
		iEvent.put(valMap2, "Activity");
		std::auto_ptr<ValueMap<float> > valMap1(new ValueMap<float>());
		ValueMap<float>::Filler filler1(*valMap1);
		filler1.insert(object, passing.begin(), passing.end());
		filler1.fill();
		iEvent.put(valMap1, "Passing");
		// 		const std::string string1("PassingProbes");
		// 		if(probePassingCandidate_.size()<1)std::cout<<"No PassingCand filled"<<std::endl;
		// 		std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(probePassingCandidate_));
		// 		iEvent.put(htp1,string1);
		// 		std::cout<<"Event Dont!"<<std::endl;
	}
	else if(objectTyp_==22)
	{
		edm::Handle<std::vector<pat::Photon> > object;
		iEvent.getByLabel(objectSource_, object);
		edm::Handle<std::vector<pat::Electron> > objectMatch;
		iEvent.getByLabel(objectMatchSource_, objectMatch);
		for(unsigned int i=0; i<object->size();i++)
		{
			float activity=0;
			for(unsigned int ii=0; ii<jets->size();ii++)
			{
				if( deltaR(object->at(i).eta(),object->at(i).phi(),jets->at(ii).eta(),jets->at(ii).phi()) < maxDeltaR_)
				{
					if(activityTyp_==0)
					{
						activity+= jets->at(ii).pt() * (jets->at(ii).chargedHadronEnergyFraction() );
					}
					else 
						std::cout<<"ActivityProducer::Error activityTyp_: "<<activityTyp_<<" not defined please check input value!"<<std::endl;
				}
			}
			values.push_back(activity);
			// check if the probe object can be matched to an object from the objectMatchSource collection if so passing if not failing
			float passingTemp=0;
			for(unsigned int ii=0; ii< objectMatch->size();ii++)
			{
				if(deltaR(object->at(i).eta(),object->at(i).phi(),objectMatch->at(ii).eta(),objectMatch->at(ii).phi() ) < 0.7&& std::abs(object->at(i).pt() - objectMatch->at(ii).pt() )/objectMatch->at(ii).pt() < 0.4)
				{
					passingTemp++;
					if(passingTemp>1.5) continue;
					
				}
			}
			passing.push_back(passingTemp);
// 			std::cout<<"Electron photon has been matched"<<std::endl;
			if(passingTemp>1) std::cout<<"Warning 2 have been matched!!!"<<std::endl;
		}
		// 		std::cout<<"Amount of object: "<<object->size()<<" amount of activity variables in vector to be stored: "<<values.size()<<std::endl;
		std::auto_ptr<ValueMap<float> > valMap2(new ValueMap<float>());
		ValueMap<float>::Filler filler2(*valMap2);
		filler2.insert(object, values.begin(), values.end());
		filler2.fill();
		iEvent.put(valMap2, "Activity");
		std::auto_ptr<ValueMap<float> > valMap1(new ValueMap<float>());
		ValueMap<float>::Filler filler1(*valMap1);
		filler1.insert(object, passing.begin(), passing.end());
		filler1.fill();
		iEvent.put(valMap1, "Passing");
		// 		const std::string string1("PassingProbes");
		// 		if(probePassingCandidate_.size()<1)std::cout<<"No PassingCand filled"<<std::endl;
		// 		std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(probePassingCandidate_));
		// 		iEvent.put(htp1,string1);
		// 		std::cout<<"Event Dont!"<<std::endl;
	}
	// isolated track muon
	else if(objectTyp_==3)
	{
		// 		edm::Handle<std::vector<pat::Muon> > object;
		// 		iEvent.getByLabel(objectSource_, object);
		edm::Handle<edm::View< pat::PackedCandidate> >object;
		iEvent.getByLabel(objectSource_, object);
		edm::Handle<std::vector<pat::PackedCandidate> > objectMatch;
		iEvent.getByLabel(objectMatchSource_, objectMatch);
		for(unsigned int i=0; i<object->size();i++)
		{
			
			float activity=0;
			for(unsigned int ii=0; ii<jets->size();ii++)
			{
				if( deltaR(object->at(i).eta(),object->at(i).phi(),jets->at(ii).eta(),jets->at(ii).phi()) < maxDeltaR_)
				{
					if(activityTyp_==0)
					{
						activity+= jets->at(ii).pt() * (jets->at(ii).chargedHadronEnergyFraction() + jets->at(ii).chargedEmEnergyFraction() );
					}
					else 
						std::cout<<"ActivityProducer::Error activityTyp_: "<<activityTyp_<<" not defined please check input value!"<<std::endl;
				}
			}
			values.push_back(activity);
			// check if the probe object can be matched to an object from the objectMatchSource collection if so passing if not failing
			float passingTemp=0;
			for(unsigned int ii=0; ii< objectMatch->size();ii++)
			{
				if(deltaR(object->at(i).eta(),object->at(i).phi(),objectMatch->at(ii).eta(),objectMatch->at(ii).phi() ) < 0.07&& std::abs(object->at(i).pt() - objectMatch->at(ii).pt() )/objectMatch->at(ii).pt() < 0.4)
				{
					passingTemp++;
					if(passingTemp>1.5) continue;
					// 					probePassingCandidate_.push_back(object->at(i));
				}
			}
			passing.push_back(passingTemp);
			if(passingTemp>1) std::cout<<"Warning 2 have been matched!!!"<<std::endl;
		}
		// 		std::cout<<"Amount of object: "<<object->size()<<" amount of activity variables in vector to be stored: "<<values.size()<<std::endl;
		std::auto_ptr<ValueMap<float> > valMap2(new ValueMap<float>());
		ValueMap<float>::Filler filler2(*valMap2);
		filler2.insert(object, values.begin(), values.end());
		filler2.fill();
		iEvent.put(valMap2, "Activity");
		std::auto_ptr<ValueMap<float> > valMap1(new ValueMap<float>());
		ValueMap<float>::Filler filler1(*valMap1);
		filler1.insert(object, passing.begin(), passing.end());
		filler1.fill();
		iEvent.put(valMap1, "Passing");
		// 		const std::string string1("PassingProbes");
		// 		if(probePassingCandidate_.size()<1)std::cout<<"No PassingCand filled"<<std::endl;
		// 		std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(probePassingCandidate_));
		// 		iEvent.put(htp1,string1);
		// 		std::cout<<"Event Dont!"<<std::endl;
	}
	else if(objectTyp_==4)
	{
		// 		edm::Handle<std::vector<pat::Muon> > object;
		// 		iEvent.getByLabel(objectSource_, object);
		edm::Handle<edm::View< pat::PackedCandidate> >object;
		iEvent.getByLabel(objectSource_, object);
		edm::Handle<std::vector<pat::PackedCandidate> > objectMatch;
		iEvent.getByLabel(objectMatchSource_, objectMatch);
		for(unsigned int i=0; i<object->size();i++)
		{
			
			float activity=0;
			for(unsigned int ii=0; ii<jets->size();ii++)
			{
				if( deltaR(object->at(i).eta(),object->at(i).phi(),jets->at(ii).eta(),jets->at(ii).phi()) < maxDeltaR_)
				{
					if(activityTyp_==0)
					{
						activity+= jets->at(ii).pt() * (jets->at(ii).chargedHadronEnergyFraction() );
					}
					else 
						std::cout<<"ActivityProducer::Error activityTyp_: "<<activityTyp_<<" not defined please check input value!"<<std::endl;
				}
			}
			values.push_back(activity);
			// check if the probe object can be matched to an object from the objectMatchSource collection if so passing if not failing
			float passingTemp=0;
			for(unsigned int ii=0; ii< objectMatch->size();ii++)
			{
				if(deltaR(object->at(i).eta(),object->at(i).phi(),objectMatch->at(ii).eta(),objectMatch->at(ii).phi() ) < 0.07&& std::abs(object->at(i).pt() - objectMatch->at(ii).pt() )/objectMatch->at(ii).pt() < 0.4)
				{
					passingTemp++;
					if(passingTemp>1.5) continue;
					// 					probePassingCandidate_.push_back(object->at(i));
				}
			}
			passing.push_back(passingTemp);
			if(passingTemp>1) std::cout<<"Warning 2 have been matched!!!"<<std::endl;
		}
		// 		std::cout<<"Amount of object: "<<object->size()<<" amount of activity variables in vector to be stored: "<<values.size()<<std::endl;
		std::auto_ptr<ValueMap<float> > valMap2(new ValueMap<float>());
		ValueMap<float>::Filler filler2(*valMap2);
		filler2.insert(object, values.begin(), values.end());
		filler2.fill();
		iEvent.put(valMap2, "Activity");
		std::auto_ptr<ValueMap<float> > valMap1(new ValueMap<float>());
		ValueMap<float>::Filler filler1(*valMap1);
		filler1.insert(object, passing.begin(), passing.end());
		filler1.fill();
		iEvent.put(valMap1, "Passing");
		// 		const std::string string1("PassingProbes");
		// 		if(probePassingCandidate_.size()<1)std::cout<<"No PassingCand filled"<<std::endl;
		// 		std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(probePassingCandidate_));
		// 		iEvent.put(htp1,string1);
		// 		std::cout<<"Event Dont!"<<std::endl;
	}
	
	else std::cout<<"ActivityProducer::Error could not identify the objectTyp_: "<<objectTyp_<<std::endl;
	
	
	
	
}

// ------------ method called once each job just before starting event loop  ------------
void 
ActivityProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ActivityProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
 v oid                           *
 ActivityProducer::beginRun(edm::Run const&, edm::EventSetup const&)
	{
	}
	*/

// ------------ method called when ending the processing of a run  ------------
/*
 v oid                           *
 ActivityProducer::endRun(edm::Run const&, edm::EventSetup const&)
	{
	}
	*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
 v oid                           *
 ActivityProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
	{
	}
	*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
 v oid                           *
 ActivityProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
	{
	}
	*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ActivityProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ActivityProducer);