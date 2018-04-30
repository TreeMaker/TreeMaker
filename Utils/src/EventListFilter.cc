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
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "TreeMaker/Utils/interface/parse.h"

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

class EventListFilter : public edm::global::EDFilter<> {
public:
	explicit EventListFilter(const edm::ParameterSet&);
	~EventListFilter() override;
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	bool filter(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;	

	// ----------member data ---------------------------
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
	if(!inputFileList_.empty()){
		std::ifstream infile(inputFileList_.c_str());
		if(infile.is_open()){
			std::string line;
			while(getline(infile,line)){
				std::vector<std::string> items;
				parse::process(line,':',items);
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
			edm::LogWarning("TreeMaker") << "EventListFilter: could not open file: " << inputFileList_;
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
EventListFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
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

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EventListFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(EventListFilter);
