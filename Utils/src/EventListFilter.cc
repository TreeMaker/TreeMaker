// system include files
#include <memory>
#include <utility>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_set>
#include <tuple>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"

//
// constants, enums and typedefs
//

//from: http://stackoverflow.com/questions/20834838/using-tuple-in-unordered-map
typedef std::tuple<unsigned, unsigned, unsigned long long> Triple;
struct triple_hash : public std::unary_function<Triple, std::size_t>
{
	std::size_t operator()(const Triple& k) const
	{
		return std::get<0>(k) ^ std::get<1>(k) ^ std::get<2>(k);
	}
};
typedef std::unordered_set<Triple,triple_hash> TripleSet;

//
// class declaration
//

class EventListFilter : public edm::EDFilter {
public:
	explicit EventListFilter(const edm::ParameterSet&);
	~EventListFilter();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual bool filter(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual bool beginRun(edm::Run&, edm::EventSetup const&);
	virtual bool endRun(edm::Run&, edm::EventSetup const&);
	virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	
	// ----------member data ---------------------------
	void process(std::string line, char delim, std::vector<std::string>& fields);
	std::string inputFileList_;
	bool TagMode_;
	TripleSet eventList_;
};

//
// constructors and destructor
//
EventListFilter::EventListFilter(const edm::ParameterSet& iConfig) :
	inputFileList_(iConfig.getParameter<std::string>("inputFileList")),
	TagMode_(iConfig.getParameter<bool>("TagMode"))
{
	//initialize the set of events
	if(inputFileList_.size()>0){
		std::ifstream infile(inputFileList_.c_str());
		if(infile.is_open()){
			std::string line;
			while(getline(infile,line)){
				std::vector<std::string> items;
				process(line,':',items);
				//convert input to proper types
				if(items.size()==3){
					unsigned run_tmp;
					std::stringstream s0(items[0]);
					s0 >> run_tmp;
					
					unsigned ls_tmp;
					std::stringstream s1(items[1]);
					s1 >> ls_tmp;
					
					unsigned long long evt_tmp;
					std::stringstream s2(items[2]);
					s2 >> evt_tmp;
					
					//insert into set
					eventList_.emplace(run_tmp,ls_tmp,evt_tmp);
				}
			}
		}
		else {
			std::cout << "EventListFilter: could not open file: " << inputFileList_ << std::endl;
		}
	}
	
	produces<bool>();
}

EventListFilter::~EventListFilter()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}

//
// member functions
//

// ------------ method called on each new Event  ------------
bool
EventListFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	// Event information
	edm::EventAuxiliary aux = iEvent.eventAuxiliary();
	unsigned runNum            = aux.run();
	unsigned lumiBlockNum      = aux.luminosityBlock();
	unsigned long long evtNum  = aux.event();

	//check in list
	auto itr = eventList_.find(std::make_tuple(runNum,lumiBlockNum,evtNum));
	
	//events pass if not in the list
	if(TagMode_){
		auto pass = std::make_unique<bool>(itr==eventList_.end());
		iEvent.put(std::move(pass));
		return true;
	}
	else {
		return (itr==eventList_.end());
	}
}

// ------------ method called once each job just before starting event loop  ------------
void 
EventListFilter::beginJob() { }

// ------------ method called once each job just after ending the event loop  ------------
void 
EventListFilter::endJob() { }

// ------------ method called when starting to processes a run  ------------
bool 
EventListFilter::beginRun(edm::Run&, edm::EventSetup const&) { return true; }

// ------------ method called when ending the processing of a run  ------------
bool 
EventListFilter::endRun(edm::Run&, edm::EventSetup const&) { return true; }

// ------------ method called when starting to processes a luminosity block  ------------
bool 
EventListFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&) { return true; }

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
EventListFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&) { return true; }

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EventListFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//generalization for processing a line
void EventListFilter::process(std::string line, char delim, std::vector<std::string>& fields){
	std::stringstream ss(line);
	std::string field;
	while(getline(ss,field,delim)){
		fields.push_back(field);
	}
}

//define this as a plug-in
DEFINE_FWK_MODULE(EventListFilter);