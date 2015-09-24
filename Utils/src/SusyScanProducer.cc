// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

// STL include files
#include <memory>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>

//
// class declaration
//

class SusyScanProducer : public edm::EDProducer {
	public:
		explicit SusyScanProducer(const edm::ParameterSet&);
		~SusyScanProducer();
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob();
		virtual void produce(edm::Event&, const edm::EventSetup&);
		virtual void endJob();
		
		virtual void beginRun(edm::Run&, edm::EventSetup const&);
		virtual void endRun(edm::Run&, edm::EventSetup const&);
		virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
		virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
		
		void process(std::string line, char delim, std::vector<std::string>& fields);
		
		// ----------member data ---------------------------
		edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
		bool shouldScan_, debug_;
};

SusyScanProducer::SusyScanProducer(const edm::ParameterSet& iConfig) : 
	getterOfProducts_(edm::ProcessMatch("*"), this), shouldScan_(iConfig.getParameter<bool>("shouldScan")), debug_(iConfig.getParameter<bool>("debug"))
{
	callWhenNewProductsRegistered(getterOfProducts_);
	produces<double>("SusyMotherMass");
	produces<double>("SusyLSPMass");
}

SusyScanProducer::~SusyScanProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}

void SusyScanProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	//  std::cout<<"Running SusyScanProducer"<<std::endl;
 
	using namespace edm;

	//mass variables
	double motherMass = 0.0;
	double lspMass = 0.0;

	std::vector<edm::Handle<LHEEventProduct> > handles;
	getterOfProducts_.fillHandles(iEvent, handles);

	if(!handles.empty() && shouldScan_){
		edm::Handle<LHEEventProduct> product = handles[0];
		for(LHEEventProduct::comments_const_iterator cit = product->comments_begin(); cit != product->comments_end(); ++cit){
			size_t found = (*cit).find("model");
			if(found != std::string::npos){
				//strip newline
				std::string comment = *cit;
				if(comment.back()=='\n') comment.pop_back();
				
				if(debug_) std::cout << comment << std::endl;
				
				std::vector<std::string> fields;
				//underscore-delimited data
				process(comment,'_',fields);
				
				//convert fields 1:n to doubles
				std::vector<double> dfields;
				dfields.reserve(fields.size()-1);
				for(unsigned f = 1; f < fields.size(); ++f){
					std::stringstream sfield(fields[f]);
					double tmp = 0;
					sfield >> tmp;
					dfields.push_back(tmp);
				}

				//two options:
				//model name_mMother_mLSP (1+2 fields)
				//model name_xChi_mMother_mLSP (1+3 fields)
				
				if(dfields.size()==2){
					motherMass = dfields[0];
					lspMass = dfields[1];
				}
				else if(dfields.size()==3){
					motherMass = dfields[1];
					lspMass = dfields[2];
				}
				
				//finished with this event
				break;
			}
		}
	}

	std::auto_ptr<double > motherMass_(new double(motherMass));
	iEvent.put(motherMass_, "SusyMotherMass");
	
	std::auto_ptr<double > lspMass_(new double(lspMass));
	iEvent.put(lspMass_, "SusyLSPMass");
	
}

// ------------ method called once each job just before starting event loop  ------------
void
SusyScanProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SusyScanProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
SusyScanProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SusyScanProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SusyScanProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SusyScanProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SusyScanProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//generalization for processing a line
void
SusyScanProducer::process(std::string line, char delim, std::vector<std::string>& fields){
	std::stringstream ss(line);
	std::string field;
	while(std::getline(ss,field,delim)){
		fields.push_back(field);
	}
}

//define this as a plug-in
DEFINE_FWK_MODULE(SusyScanProducer);
