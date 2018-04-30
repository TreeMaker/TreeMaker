// Producer class to pull the pMSSM point ID from the LHEEventProduct
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "TreeMaker/Utils/interface/parse.h"

// STL include files
#include <memory>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <fstream>

//
// class declaration
//

class PmssmProducer : public edm::global::EDProducer<> {
public:
  explicit PmssmProducer(const edm::ParameterSet&);
  ~PmssmProducer() override;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

  // ----------member data ---------------------------
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  bool shouldScan_, debug_;
};

PmssmProducer::PmssmProducer(const edm::ParameterSet& iConfig) : 
  getterOfProducts_(edm::ProcessMatch("*"), this), 
  shouldScan_(iConfig.getParameter<bool>("shouldScan")), 
  debug_(iConfig.getParameter<bool>("debug"))
{
  callWhenNewProductsRegistered(getterOfProducts_);
  produces<double >("PmssmId");
}

PmssmProducer::~PmssmProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}

void PmssmProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{

  using namespace edm;
  double pmssmId = -1;
  std::vector<edm::Handle<LHEEventProduct> > handles;
  getterOfProducts_.fillHandles(iEvent, handles);

  if(!handles.empty() && shouldScan_){
    edm::Handle<LHEEventProduct> product = handles[0];
    for(LHEEventProduct::comments_const_iterator cit = product->comments_begin(); cit != product->comments_end(); ++cit){
      size_t found = (*cit).find(".slha");
      if(found != std::string::npos){
	std::string comment = (*cit).substr(1,(*cit).find(".slha")-1);
	if(comment.back()=='\n') comment.pop_back();
	std::vector<std::string> nameblocks;
	parse::process(comment, '_', nameblocks);
	std::string character_string = nameblocks[2]+nameblocks[3];
	std::stringstream s0(character_string);
	s0 >> pmssmId;
	if(debug_) edm::LogInfo("TreeMaker") << comment;
	break;//finished with this event
      }
    }
  }

  auto pmssmId_ = std::make_unique<double >(pmssmId);
  iEvent.put(std::move(pmssmId_), "PmssmId");
	
	
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PmssmProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PmssmProducer);
