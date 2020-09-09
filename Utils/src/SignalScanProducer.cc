// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "TreeMaker/Utils/interface/parse.h"

// STL include files
#include <memory>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>

//
// class declaration
//

enum class signal_type {
	None=0,
	SUSY=1,
	pMSSM=2,
	SVJ=3
};

class SignalScanProducer : public edm::stream::EDProducer<> {
	public:
		explicit SignalScanProducer(const edm::ParameterSet&);
		~SignalScanProducer() override;
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		void produce(edm::Event&, const edm::EventSetup&) override;
		
		void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

		void reset();
		
		void getSUSYComment(const LHEEventProduct& lhe);
		void getSUSYComment(const GenLumiInfoHeader& gen);
		void getSUSYModelInfo(std::string comment);

		void getpMSSMComment(const LHEEventProduct& lhe);
		//todo: add pMSSM parser for GenLumiInfoHeader, once available/understood

		//LHE will never be used for SVJ
		void getSVJComment(const GenLumiInfoHeader& gen);
		
		// ----------member data ---------------------------
		edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
		edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
		bool shouldScan_, debug_, isLHE_;
		signal_type type_;
		std::vector<double> signalParameters_;
};

SignalScanProducer::SignalScanProducer(const edm::ParameterSet& iConfig) : 
	getterOfProducts_(edm::ProcessMatch("*"), this),
	genLumiHeaderToken_(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator"))),
	shouldScan_(true),
	debug_(iConfig.getParameter<bool>("debug")),
	isLHE_(iConfig.getParameter<bool>("isLHE"))
{
	std::string stype(iConfig.getParameter<std::string>("signalType"));
	if(stype=="None") { type_ = signal_type::None; shouldScan_ = false; }
	else if(stype=="SUSY") type_ = signal_type::SUSY;
	else if(stype=="pMSSM") type_ = signal_type::pMSSM;
	else if(stype=="SVJ") type_ = signal_type::SVJ;
	else throw cms::Exception("UnknownType") << "SignalScanProducer: unknown signal type " << stype;

	callWhenNewProductsRegistered(getterOfProducts_);
	produces<std::vector<double>>("SignalParameters");
}

SignalScanProducer::~SignalScanProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}

void SignalScanProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;

	if(isLHE_ && shouldScan_){
		reset();
		if(debug_) edm::LogInfo("TreeMaker") << "SignalScanProducer: checking LHEEventProduct";
		std::vector<edm::Handle<LHEEventProduct> > handles;
		getterOfProducts_.fillHandles(iEvent, handles);

		if(!handles.empty()){
			edm::Handle<LHEEventProduct> product = handles[0];
			if(type_==signal_type::SUSY) getSUSYComment(*product);
			else if(type_==signal_type::pMSSM) getpMSSMComment(*product);
		}
	}
	//otherwise, values are picked up in beginLuminosityBlock()

	auto signalParameters = std::make_unique<std::vector<double>>(signalParameters_);
	iEvent.put(std::move(signalParameters), "SignalParameters");
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SignalScanProducer::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iSetup)
{
	//new way of getting SUSY scan info
	if(!isLHE_ && shouldScan_){
		reset();
		if(debug_) edm::LogInfo("TreeMaker") << "SignalScanProducer: checking GenLumiInfoHeader";
		edm::Handle<GenLumiInfoHeader> gen_header;
		iLumi.getByToken(genLumiHeaderToken_, gen_header);
		if(type_==signal_type::SUSY) getSUSYComment(*gen_header);
		else if(type_==signal_type::SVJ) getSVJComment(*gen_header);
	}
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SignalScanProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//reset output vars
void SignalScanProducer::reset(){
	signalParameters_.clear();
}

//parse LHE for SUSY
void SignalScanProducer::getSUSYComment(const LHEEventProduct& lhe){
	for(auto cit = lhe.comments_begin(); cit != lhe.comments_end(); ++cit){
		size_t found = (*cit).find("model");
		if(found != std::string::npos){
			//parse string
			std::string comment = *cit;
			getSUSYModelInfo(comment);

			//finished with this event
			break;
		}
	}
}

//parse GenLumiInfo for SUSY
void SignalScanProducer::getSUSYComment(const GenLumiInfoHeader& gen){
	getSUSYModelInfo(gen.configDescription());
}

//parse model comment for SUSY
void SignalScanProducer::getSUSYModelInfo(std::string comment){
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

	double motherMass, lspMass;

	std::stringstream sfield1(fields.end()[-1]);
	sfield1 >> lspMass;
	
	std::stringstream sfield2(fields.end()[-2]);
	sfield2 >> motherMass;

	signalParameters_.push_back(motherMass);
	signalParameters_.push_back(lspMass);
}

//parse LHE for pMSSM
void SignalScanProducer::getpMSSMComment(const LHEEventProduct& lhe){
	for(auto cit = lhe.comments_begin(); cit != lhe.comments_end(); ++cit){
		size_t found = (*cit).find(".slha");
		if(found != std::string::npos){
			std::string comment = (*cit).substr(1,(*cit).find(".slha")-1);
			if(comment.back()=='\n') comment.pop_back();
			std::vector<std::string> nameblocks;
			parse::process(comment, '_', nameblocks);
			std::string character_string = nameblocks[2]+nameblocks[3];
			std::stringstream s0(character_string);
			double pmssmId;
			s0 >> pmssmId;
			signalParameters_.push_back(pmssmId);
			if(debug_) edm::LogInfo("TreeMaker") << comment;
			break; //finished with this event
		}
	}
}

//parse GenLumiInfo for SVJ
void SignalScanProducer::getSVJComment(const GenLumiInfoHeader& gen){
	const std::map<std::string,double> alpha_vals{
		{"peak",-2.},
		{"high",-1.},
		{"low",-3.},
	};
	std::string model = gen.configDescription();
	if(debug_) edm::LogInfo("TreeMaker") << model;
	std::vector<std::string> fields;
	parse::process(model,'_',fields);

	//format: SVJ_mZprime-X_mDark-Y_rinv-Z_alpha-W
	for(const auto& f : fields){
		std::vector<std::string> subfields;
		parse::process(f,'-',subfields);
		if(subfields.size()!=2) continue;
		double val = 0.;
		if(subfields[0]=="alpha") val = alpha_vals.at(subfields[1]);
		else {
			std::stringstream sval(subfields[1]);
			sval >> val;
		}
		signalParameters_.push_back(val);
	}
}

//define this as a plug-in
DEFINE_FWK_MODULE(SignalScanProducer);
