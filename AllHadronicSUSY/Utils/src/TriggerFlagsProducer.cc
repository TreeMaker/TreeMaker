//TODO: Do not define the flags in the module, but accept them as a parameter.
//Even better is to receive them as pairs. One part is the flag name in the miniAOD file,
//the second the name the tag should be saved under during Tree production.

// system include files
#include <memory>
#include <iostream>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"


class TriggerFlagsProducer : public edm::EDProducer {
   public:
      explicit TriggerFlagsProducer(const edm::ParameterSet&);
      ~TriggerFlagsProducer() {}

   private:
      virtual void produce(edm::Event&, const edm::EventSetup&);

      edm::EDGetTokenT<edm::TriggerResults> triggerBits_;
//      std::vector<std::string> filterNames;
      std::vector< std::string >  filterNameVec; 
      std::vector< std::string >  statusNameVec;      

};


TriggerFlagsProducer::TriggerFlagsProducer(const edm::ParameterSet& iConfig):
    triggerBits_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits")))

{
        filterNameVec = iConfig.getParameter<std::vector<std::string> >("filterNames");
	statusNameVec = iConfig.getParameter<std::vector<std::string> >("statusNames");

	std::cout << "filterNameVec (size = " << filterNameVec.size() << ")" <<std::endl;
	for(int i = 0, n = filterNameVec.size(); i < n; i++){
		std::cout << filterNameVec.at(i) << std::endl;
	}

	std::cout << "statusNameVec (size = " << statusNameVec.size() << ")" <<std::endl;
	for(int i = 0, n = statusNameVec.size(); i < n; i++){
		std::cout << statusNameVec.at(i) << std::endl;
	}

	//The following vector is setup, we will look for these bits, This producer only works with miniAOD files. They have a 
	//specific method of saving the Filter status flags in the HLT trigger area.

        /*
	filterNames = {"Flag_trackingFailureFilter", "Flag_goodVertices", "Flag_CSCTightHaloFilter",
			"Flag_trkPOGFilters",
			"Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_ecalLaserCorrFilter",
			"Flag_eeBadScFilter", "Flag_METFilters", "Flag_HBHENoiseFilter",
			"Flag_hcalLaserEventFilter"};

	for(int i = 0, n = filterNames.size(); i < n; ++i){
		produces<bool>(filterNames[i].substr(5,std::string::npos));
	}
        */

        for(int i = 0, n = statusNameVec.size(); i < n; ++i){

        	produces<bool>(statusNameVec.at(i)); 
        }

}

void TriggerFlagsProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
//We will use the convention from the MiniAODTriggerAnalyzer, where True means the event passed the filter
//False is the event failed the filter, or the filter wasn't run
{
    edm::Handle<edm::TriggerResults> triggerBits;
    bool passing = false;

    iEvent.getByToken(triggerBits_, triggerBits);

    const edm::TriggerNames &names = iEvent.triggerNames(*triggerBits);
    //We look for each of the filters that we are interested in
    for(int j = 0, m = filterNameVec.size(); j < m; ++j){
        passing = false;

        //Loop over all of the Trigger Results looking for a match
        for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {
        
		if( filterNameVec.at(j) == names.triggerName(i) ){
			passing = triggerBits->accept(i);
			break;
		}
	}	
        
	//Save the result to the event
	std::auto_ptr<bool> result(new bool(passing));
	   
	iEvent.put(result,statusNameVec.at(j));

    }

}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerFlagsProducer);
