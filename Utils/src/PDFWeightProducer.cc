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

template <class P>
class PDFWeightHelper {
  public:
    PDFWeightHelper(const P* prod) : product_(prod) {}
    bool fillWeights(std::vector<double>* output, unsigned offset, unsigned nWeights, bool isPDF) {
      if(offset > this->getMax()) return false;
      double norm = this->getNorm(offset,isPDF);
      unsigned max = std::min(nWeights+offset,this->getMax());
      for (unsigned int i = offset; i < max; i++) {
        output->push_back(this->getWeight(i)/norm);
      }
      return !output->empty();
    }
    double getWeight(unsigned index) { return 1.; }
    double getNorm(unsigned offset, bool isPDF) { return 1.; }
    unsigned getMax() { return product_->weights().size(); }

    //members
    const P* product_;
};

//for template class inference
template <class P>
PDFWeightHelper<P> makeHelper(const P* prod) { return PDFWeightHelper<P>(prod); }

template <> double PDFWeightHelper<LHEEventProduct>::getWeight(unsigned index){
  return product_->weights()[index].wgt;
}
template <> double PDFWeightHelper<LHEEventProduct>::getNorm(unsigned offset, bool isPDF){
  return isPDF ? product_->originalXWGTUP() : this->getWeight(offset);
}

template <> double PDFWeightHelper<GenEventInfoProduct>::getWeight(unsigned index){
  return product_->weights()[index];
}
template <> double PDFWeightHelper<GenEventInfoProduct>::getNorm(unsigned offset, bool isPDF){
  return this->getWeight(offset);
}

class PDFWeightProducer : public edm::global::EDProducer<> {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  
  // ----------member data ---------------------------
  unsigned nScales_, nPDFs_;
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;

};

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) :
  nScales_(iConfig.getParameter<unsigned>("nScales")),
  nPDFs_(iConfig.getParameter<unsigned>("nPDFs")),
  getterOfProducts_(edm::ProcessMatch("*"), this), 
  genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator")))
{
  callWhenNewProductsRegistered(getterOfProducts_);
  produces<std::vector<double> >("ScaleWeights");
  produces<std::vector<double> >("PDFweights");
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
  
  auto scaleweights = std::make_unique<std::vector<double>>();
  auto pdfweights = std::make_unique<std::vector<double>>();
  
  bool found_scales = false;
  bool found_pdfs = false;
  
  if(!handles.empty()){
    edm::Handle<LHEEventProduct> LheInfo = handles[0];
    auto helper = makeHelper(LheInfo.product());
    //renormalization/factorization scale weights
    found_scales = helper.fillWeights(scaleweights.get(),0,nScales_,false);
    //pdf weights
    if(found_scales) found_pdfs = helper.fillWeights(pdfweights.get(),nScales_,nPDFs_,true);
  }
  
  //check GenEventInfoProduct if LHEEventProduct not found or empty
  if(!found_scales or !found_pdfs){
    edm::Handle<GenEventInfoProduct> genHandle;
    iEvent.getByToken(genProductToken_, genHandle);
    auto helper = makeHelper(genHandle.product());
    unsigned offset = 1;
    //renormalization/factorization scale weights
    found_scales = helper.fillWeights(scaleweights.get(),offset,nScales_,false);
    //pdf weights
    if(found_scales) found_pdfs = helper.fillWeights(pdfweights.get(),nScales_+offset,nPDFs_,true);
  }

  iEvent.put(std::move(scaleweights),"ScaleWeights");
  iEvent.put(std::move(pdfweights),"PDFweights");
  
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
