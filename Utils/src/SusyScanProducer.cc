// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "TreeMaker/Utils/interface/parse.h"

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

class SusyScanProducer : public edm::stream::EDProducer<> {
	public:
		explicit SusyScanProducer(const edm::ParameterSet&);
		~SusyScanProducer();
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void produce(edm::Event&, const edm::EventSetup&) override;
		
		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
		
		void getModelInfo(std::string comment);
		
		// ----------member data ---------------------------
		edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
		edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
		bool shouldScan_, debug_, isLHE_;
		double motherMass_, lspMass_;
};

SusyScanProducer::SusyScanProducer(const edm::ParameterSet& iConfig) : 
	getterOfProducts_(edm::ProcessMatch("*"), this),
	genLumiHeaderToken_(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator"))),
	shouldScan_(iConfig.getParameter<bool>("shouldScan")),
	debug_(iConfig.getParameter<bool>("debug")),
	isLHE_(iConfig.getParameter<bool>("isLHE")),
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

	if(isLHE_ && shouldScan_){
		if(debug_) edm::LogInfo("TreeMaker") << "SusyScanProducer: checking LHEEventProduct";
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

	auto motherMass = std::make_unique<double>(motherMass_);
	iEvent.put(std::move(motherMass), "SusyMotherMass");
	
	auto lspMass = std::make_unique<double>(lspMass_);
	iEvent.put(std::move(lspMass), "SusyLSPMass");
	
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SusyScanProducer::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iSetup)
{
	//new way of getting SUSY scan info
	if(!isLHE_ && shouldScan_){
		if(debug_) edm::LogInfo("TreeMaker") << "SusyScanProducer: checking GenLumiInfoHeader";
		edm::Handle<GenLumiInfoHeader> gen_header;
		iLumi.getByToken(genLumiHeaderToken_, gen_header);
		std::string model = gen_header->configDescription();
		getModelInfo(model);
	}
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
	
	if(debug_) edm::LogInfo("TreeMaker") << comment;
	
	std::vector<std::string> fields;
	//underscore-delimited data
	parse::process(comment,'_',fields);

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

//define this as a plug-in
DEFINE_FWK_MODULE(SusyScanProducer);
