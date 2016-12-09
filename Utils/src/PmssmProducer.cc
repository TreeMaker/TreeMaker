// Producer class to pull the pMSSM point ID from the LHEEventProduct
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
#include <fstream>

//
// class declaration
//

class PmssmProducer : public edm::EDProducer {
public:
  explicit PmssmProducer(const edm::ParameterSet&);
  ~PmssmProducer();
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
  double getXsec(double pmssmid);
		
  // ----------member data ---------------------------
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  bool shouldScan_, debug_, do_xsec_; std::string _xsecFilename;
};

PmssmProducer::PmssmProducer(const edm::ParameterSet& iConfig) : 
  getterOfProducts_(edm::ProcessMatch("*"), this), 
  shouldScan_(iConfig.getParameter<bool>("shouldScan")), 
  debug_(iConfig.getParameter<bool>("debug")),
  do_xsec_(iConfig.getParameter<bool>("do_xsec")),
  _xsecFilename(iConfig.getParameter<std::string> ("xsecFilename"))
{
  callWhenNewProductsRegistered(getterOfProducts_);
  produces<double >("PmssmId");
  produces<double>("PmssmXsec");	
}

PmssmProducer::~PmssmProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}

double PmssmProducer::getXsec(double pmssmid)
{
  double xsec = -1;
  std::ifstream fileInput;
  std::string line;//use a sprintf with pmssmid
  char search [30];
  sprintf (search, "%d", int(pmssmid));
  fileInput.open(_xsecFilename.c_str());
  if(fileInput.is_open()){
    while(getline(fileInput, line)) {
      if (size_t(line.find(search, 0)) != std::string::npos) {
	xsec = atof(line.substr(line.find("\t"),line.size()).c_str());
      }
    }
    fileInput.close();
  }
  else std::cout << "Unable to open file.";
  return xsec;
}

void PmssmProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  double pmssmXsec = -1.0;
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
	process(comment, '_', nameblocks);
	char character_string [30];
	sprintf (character_string, "%s%s", nameblocks[2].c_str(),nameblocks[3].c_str());
	std::stringstream s0(character_string);
	s0 >> pmssmId;
	if(debug_) std::cout << comment << std::endl;
	if (do_xsec_) pmssmXsec = getXsec(pmssmId);
	break;//finished with this event
      }
    }
  }

  auto pmssmId_ = std::make_unique<double >(pmssmId);
  iEvent.put(std::move(pmssmId_), "PmssmId");
	
  auto pmssmXsec_ = std::make_unique<double>(pmssmXsec);
  iEvent.put(std::move(pmssmXsec_), "PmssmXsec");
	
}

// ------------ method called once each job just before starting event loop  ------------
void
PmssmProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PmssmProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
PmssmProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PmssmProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PmssmProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PmssmProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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

//generalization for processing a line
void
PmssmProducer::process(std::string line, char delim, std::vector<std::string>& fields){
  std::stringstream ss(line);
  std::string field;
  while(std::getline(ss,field,delim)){
    fields.push_back(field);
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(PmssmProducer);
