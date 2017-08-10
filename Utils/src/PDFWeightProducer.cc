#include <iostream>
#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "TVector2.h"

//
// class declaration
//



class PDFWeightProducer : public edm::global::EDProducer<> {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  
  // ----------member data ---------------------------
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;

};

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) : getterOfProducts_(edm::ProcessMatch("*"), this), genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator")))
{
  callWhenNewProductsRegistered(getterOfProducts_);
  produces<std::vector<double> >("ScaleWeights");
  produces<std::vector<double> >("PDFweights");
  produces<std::vector<int> >("PDFids");
}

PDFWeightProducer::~PDFWeightProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}

void PDFWeightProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{

  using namespace edm;

  std::vector<edm::Handle<LHEEventProduct> > handles;
  getterOfProducts_.fillHandles(iEvent, handles);
  
  std::vector<double> scaleweights;
  std::vector<double> pdfweights;
  std::vector<int> pdfids;
  
  bool found_weights = false;
  
  if(!handles.empty()){
    edm::Handle<LHEEventProduct> LheInfo = handles[0];
    
    std::vector< gen::WeightsInfo > lheweights = LheInfo->weights();
    if(!lheweights.empty()){
      found_weights = true;
      // these numbers are hard-coded by the LHEEventInfo
      //renormalization/factorization scale weights
      for (unsigned int i = 0; i < 9; i++){
        scaleweights.push_back(lheweights[i].wgt/lheweights[0].wgt);
      }
      //pdf weights
      for (unsigned int i = 9; i < 110; i++){
        pdfweights.push_back(lheweights[i].wgt/lheweights[9].wgt);
        pdfids.push_back(i-9);
      }
    }
  }
  
  //check GenEventInfoProduct if LHEEventProduct not found or empty
  if(!found_weights){
    edm::Handle<GenEventInfoProduct> genHandle;
    iEvent.getByToken(genProductToken_, genHandle);

	const std::vector<double>& genweights = genHandle->weights();
    // these numbers are hard-coded by the GenEventInfo (shifted by 1 wrt LHE)
    //renormalization/factorization scale weights
    for (unsigned int i = 1; i < 10; i++){
      scaleweights.push_back(genweights[i]/genweights[1]);
    }
    //pdf weights
    for (unsigned int i = 10; i < 111; i++){
      pdfweights.push_back(genweights[i]/genweights[10]);
      pdfids.push_back(i-10);
    }
  }

  auto scaleweights_ = std::make_unique<std::vector<double>>(scaleweights);
  iEvent.put(std::move(scaleweights_),"ScaleWeights");
  
  auto pdfweights_ = std::make_unique<std::vector<double>>(pdfweights);
  iEvent.put(std::move(pdfweights_),"PDFweights");
  
  auto pdfids_ = std::make_unique<std::vector<int>>(pdfids);
  iEvent.put(std::move(pdfids_),"PDFids");
  
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PDFWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PDFWeightProducer);
