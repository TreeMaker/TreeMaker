// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"

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
		
		virtual void beginRun(edm::Run const&, edm::EventSetup const&);
		virtual void endRun(edm::Run const&, edm::EventSetup const&);
		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
		virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
		
		void process(std::string line, char delim, std::vector<std::string>& fields);
		void getModelInfo(std::string comment);
		
		// ----------member data ---------------------------
		edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
		edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
		bool shouldScan_, debug_, is74X_;
		double motherMass_, lspMass_;
};

SusyScanProducer::SusyScanProducer(const edm::ParameterSet& iConfig) : 
	getterOfProducts_(edm::ProcessMatch("*"), this),
	genLumiHeaderToken_(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator"))),
	shouldScan_(iConfig.getParameter<bool>("shouldScan")),
	debug_(iConfig.getParameter<bool>("debug")),
	is74X_(iConfig.getParameter<bool>("is74X")),
	motherMass_(0),
	lspMass_(0)
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
	using namespace edm;

	if(is74X_ && shouldScan_){
		if(debug_) std::cout << "SusyScanProducer: checking LHEEventProduct" << std::endl;
		std::vector<edm::Handle<LHEEventProduct> > handles;
		getterOfProducts_.fillHandles(iEvent, handles);

		if(!handles.empty()){
			edm::Handle<LHEEventProduct> product = handles[0];
			for(LHEEventProduct::comments_const_iterator cit = product->comments_begin(); cit != product->comments_end(); ++cit){
				size_t found = (*cit).find("model");
				if(found != std::string::npos){
					//parse string
					std::string comment = *cit;
					getModelInfo(comment);

					//finished with this event
					break;
				}
			}
		}
	}
	//otherwise, values are picked up in beginLuminosityBlock()

	std::auto_ptr<double > motherMass(new double(motherMass_));
	iEvent.put(motherMass, "SusyMotherMass");
	
	std::auto_ptr<double > lspMass(new double(lspMass_));
	iEvent.put(lspMass, "SusyLSPMass");
	
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
SusyScanProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SusyScanProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SusyScanProducer::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iSetup)
{
	//new way of getting SUSY scan info
	if(!is74X_ && shouldScan_){
		if(debug_) std::cout << "SusyScanProducer: checking GenLumiInfoHeader" << std::endl;
		edm::Handle<GenLumiInfoHeader> gen_header;
		iLumi.getByToken(genLumiHeaderToken_, gen_header);
		std::string model = gen_header->configDescription();
		getModelInfo(model);
	}
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SusyScanProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
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

//parse model comment
void SusyScanProducer::getModelInfo(std::string comment){
	//strip newline
	if(comment.back()=='\n') comment.pop_back();
	
	if(debug_) std::cout << comment << std::endl;
	
	std::vector<std::string> fields;
	//underscore-delimited data
	process(comment,'_',fields);

	//several possible formats:
	//model name_mMother_mLSP (1+2 fields)
	//model name_xChi_mMother_mLSP (1+3 fields)
	//model name_name_name_mMother_mLSP (3+2 fields)
	//just take last two values and convert to doubles
	
	std::stringstream sfield1(fields.end()[-1]);
	sfield1 >> lspMass_;
	
	std::stringstream sfield2(fields.end()[-2]);
	sfield2 >> motherMass_;
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
