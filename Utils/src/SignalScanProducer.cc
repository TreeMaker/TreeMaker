// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
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

enum class signal_type {
	None=0,
	SUSY=1,
	pMSSM=2,
	SVJ=3
};

class SignalScanProducer : public edm::global::EDProducer<edm::LuminosityBlockCache<std::vector<double>>> {
	public:
		explicit SignalScanProducer(const edm::ParameterSet&);
		~SignalScanProducer() override {}
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		std::shared_ptr<std::vector<double>> globalBeginLuminosityBlock(const edm::LuminosityBlock&, const edm::EventSetup&) const override;
		void globalEndLuminosityBlock(const edm::LuminosityBlock&, const edm::EventSetup&) const override {}

		void getSUSYComment(const std::string& comment, std::vector<double>& signalParameters) const;
		void getSVJComment(const std::string& gen, std::vector<double>& signalParameters) const;
		void getpMSSMComment(const std::string& gen, std::vector<double>& signalParameters) const;

		// ----------member data ---------------------------
		edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
		bool shouldScan_, debug_;
		signal_type type_;
};

SignalScanProducer::SignalScanProducer(const edm::ParameterSet& iConfig) : 
	genLumiHeaderToken_(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator"))),
	shouldScan_(true),
	debug_(iConfig.getParameter<bool>("debug"))
{
	std::string stype(iConfig.getParameter<std::string>("signalType"));
	if(stype=="None") { type_ = signal_type::None; shouldScan_ = false; }
	else if(stype=="SUSY") type_ = signal_type::SUSY;
	else if(stype=="pMSSM") type_ = signal_type::pMSSM;
	else if(stype=="SVJ") type_ = signal_type::SVJ;
	else throw cms::Exception("UnknownType") << "SignalScanProducer: unknown signal type " << stype;

	produces<std::vector<double>>("SignalParameters");
}

void SignalScanProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
    auto holder = luminosityBlockCache(iEvent.getLuminosityBlock().index());
	auto signalParameters = std::make_unique<std::vector<double>>(*holder);
	iEvent.put(std::move(signalParameters), "SignalParameters");
}

// ------------ method called when starting to processes a luminosity block  ------------
std::shared_ptr<std::vector<double>>
SignalScanProducer::globalBeginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iSetup) const
{
	auto holder = std::make_shared<std::vector<double>>();
	//new way of getting SUSY scan info
	if(shouldScan_){
		if(debug_) edm::LogInfo("TreeMaker") << "SignalScanProducer: checking GenLumiInfoHeader";
		edm::Handle<GenLumiInfoHeader> gen_header;
		iLumi.getByToken(genLumiHeaderToken_, gen_header);
		const auto& configDesc = gen_header->configDescription();
		if(type_==signal_type::SUSY) getSUSYComment(configDesc,*holder);
		else if(type_==signal_type::pMSSM) getpMSSMComment(configDesc,*holder);
		else if(type_==signal_type::SVJ) getSVJComment(configDesc,*holder);
	}
	return holder;
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

//parse model comment for SUSY
void SignalScanProducer::getSUSYComment(const std::string& comment, std::vector<double>& signalParameters) const {
	if(debug_) edm::LogInfo("TreeMaker") << comment;

	std::vector<std::string> fields;
	//underscore-delimited data
	parse::process(comment,'_',fields);
	//strip newline
	if(fields.back().back()=='\n') fields.back().pop_back();

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

	signalParameters.push_back(motherMass);
	signalParameters.push_back(lspMass);
}

//parse GenLumiInfo for SVJ
void SignalScanProducer::getSVJComment(const std::string& comment, std::vector<double>& signalParameters) const {
	const std::map<std::string,double> alpha_vals{
		{"peak",-2.},
		{"high",-1.},
		{"low",-3.},
	};
	if(debug_) edm::LogInfo("TreeMaker") << comment;
	std::vector<std::string> fields;
	parse::process(comment,'_',fields);

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
		signalParameters.push_back(val);
	}
}

//parse model comment for pMSSM
void SignalScanProducer::getpMSSMComment(const std::string& comment, std::vector<double>& signalParameters) const {
	if(debug_) edm::LogInfo("TreeMaker") << comment;

	std::vector<std::string> fields;
	parse::process(comment, '_', fields);
	//strip ".slha", newline
	fields.back() = fields.back().substr(0,fields.back().find(".slha")-1);

	//format: pMSSM_MCMC_id1_id2.slha

	double field1, field2;
	std::stringstream sfield1(fields.end()[-1]);
	sfield1 >> field1;

	std::stringstream sfield2(fields.end()[-2]);
	sfield2 >> field2;

	signalParameters.push_back(field1);
	signalParameters.push_back(field2);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SignalScanProducer);
