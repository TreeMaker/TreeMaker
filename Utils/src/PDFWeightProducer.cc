#include <iostream>
#include <cmath>
#include <memory>
#include <vector>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"

enum class wtype { scale = 0, pdf = 1, ps = 2 };

template <class P>
class PDFWeightHelper {
  public:
    PDFWeightHelper(const P* prod, bool use_norm) : product_(prod), use_norm_(use_norm) {}
    bool fillWeights(std::vector<float>* output, unsigned offset, unsigned nWeights, wtype wt, const std::vector<unsigned>& indices={}) {
      unsigned max = this->getMax();
      if(max==0 or offset > max) return false;
      double norm = use_norm_ ? 1./this->getNorm(offset,wt) : 1.;
      max = std::min(nWeights+offset,max);
      output->reserve(max-offset);
      if(indices.empty()){
        for (unsigned int i = offset; i < max; i++) {
          output->push_back(this->getWeight(i)*norm);
        }
      }
      else {
        for (auto index : indices) {
          output->push_back(this->getWeight(index)*norm);
        }
      }
      return !output->empty();
    }
    double getWeight(unsigned index) { return 1.; }
    double getNorm(unsigned offset, wtype wt) { return 1.; }
    unsigned getMax() { return product_->weights().size(); }

    //members
    const P* product_;
	bool use_norm_;
};

//for template class inference
template <class P>
PDFWeightHelper<P> makeHelper(const P* prod, bool use_norm) { return PDFWeightHelper<P>(prod, use_norm); }

template <> double PDFWeightHelper<LHEEventProduct>::getWeight(unsigned index){
  return product_->weights()[index].wgt;
}
template <> double PDFWeightHelper<LHEEventProduct>::getNorm(unsigned offset, wtype wt){
  return wt==wtype::pdf ? product_->originalXWGTUP() : this->getWeight(offset);
}

template <> double PDFWeightHelper<GenEventInfoProduct>::getWeight(unsigned index){
  return product_->weights()[index];
}
template <> double PDFWeightHelper<GenEventInfoProduct>::getNorm(unsigned offset, wtype wt){
  return wt==wtype::ps ? 1.0 : this->getWeight(offset);
}

struct WeightIndices {
  std::vector<unsigned> scaleWeightIndices_;
  std::vector<unsigned> psWeightIndices_;
};

class PDFWeightProducer : public edm::global::EDProducer<edm::LuminosityBlockCache<WeightIndices>> {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer() override {}

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  std::shared_ptr<WeightIndices> globalBeginLuminosityBlock(const edm::LuminosityBlock&, const edm::EventSetup&) const override;
  void globalEndLuminosityBlock(const edm::LuminosityBlock&, const edm::EventSetup&) const override {}

  // ----------member data ---------------------------
  unsigned nScales_, nPDFs_, nPSs_;
  bool norm_, debug_;
  std::map<std::string, unsigned> scaleWeightNamesIndices_;
  std::map<std::string, unsigned> psWeightNamesIndices_;
  edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;
};

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) :
  nScales_(iConfig.getParameter<unsigned>("nScales")),
  nPDFs_(iConfig.getParameter<unsigned>("nPDFs")),
  nPSs_(iConfig.getParameter<unsigned>("nPSs")),
  norm_(iConfig.getParameter<bool>("normalize")),
  debug_(iConfig.getParameter<bool>("debug")),
  genLumiHeaderToken_(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator"))),
  getterOfProducts_(edm::ProcessMatch("*"), this), 
  genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator")))
{
  //transform vectors into map w/ index for easier searching
  if(nScales_>0){
    const auto& scaleNames = iConfig.getParameter<std::vector<std::string>>("scaleNames");
    if (!scaleNames.empty()){
      nScales_ = scaleNames.size();
      for(unsigned i = 0; i < nScales_; ++i){
        scaleWeightNamesIndices_.emplace(scaleNames[i],i);
      }
    }
  }
  const auto& psNames = iConfig.getParameter<std::vector<std::string>>("psNames");
  if (!psNames.empty()){
    nPSs_ = psNames.size();
    for(unsigned i = 0; i < nPSs_; ++i){
      psWeightNamesIndices_.emplace(psNames[i],i);
    }
  }

  callWhenNewProductsRegistered(getterOfProducts_);
  produces<std::vector<float> >("ScaleWeights");
  produces<std::vector<float> >("PDFweights");
  produces<std::vector<float> >("PSweights");
}

std::shared_ptr<WeightIndices> PDFWeightProducer::globalBeginLuminosityBlock(const edm::LuminosityBlock& iLumi, const edm::EventSetup& iSetup) const {
  if(scaleWeightNamesIndices_.empty() and psWeightNamesIndices_.empty()) return nullptr;

  edm::Handle<GenLumiInfoHeader> gen_header;
  iLumi.getByToken(genLumiHeaderToken_, gen_header);
  const auto& weightNames = gen_header->weightNames();

  auto holder = std::make_shared<WeightIndices>();
  holder->scaleWeightIndices_.resize(scaleWeightNamesIndices_.size(),0);
  holder->psWeightIndices_.resize(psWeightNamesIndices_.size(),0);
  for(unsigned i = 0; i < weightNames.size(); ++i){
    const auto& weightName(weightNames[i]);
    auto scale_iter = scaleWeightNamesIndices_.find(weightName);
    if(scale_iter != scaleWeightNamesIndices_.end())
      holder->scaleWeightIndices_[scale_iter->second] = i;
    auto ps_iter = psWeightNamesIndices_.find(weightName);
    if(ps_iter != psWeightNamesIndices_.end())
      holder->psWeightIndices_[ps_iter->second] = i;
  }
  return holder;
}


void PDFWeightProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{

  using namespace edm;

  std::vector<edm::Handle<LHEEventProduct> > handles;
  getterOfProducts_.fillHandles(iEvent, handles);
  
  auto scaleweights = std::make_unique<std::vector<float>>();
  auto pdfweights = std::make_unique<std::vector<float>>();
  auto psweights = std::make_unique<std::vector<float>>();
  
  bool found_scales = false;
  bool found_pss = false;
  
  if(!handles.empty()){
    edm::Handle<LHEEventProduct> LheInfo = handles[0];
    auto helper = makeHelper(LheInfo.product(),norm_);
    //renormalization/factorization scale weights
    found_scales = helper.fillWeights(scaleweights.get(),0,nScales_,wtype::scale);
    //pdf weights
    if(found_scales) helper.fillWeights(pdfweights.get(),nScales_,nPDFs_,wtype::pdf);
  }
  
  //check GenEventInfoProduct if LHEEventProduct not found or empty
  //if LHEEventProduct was filled, check GenEventInfoProduct for parton shower weights from Pythia8, and/or scale weights
  //(no known case w/ PDF weights in GenEventInfoProduct)
  edm::Handle<GenEventInfoProduct> genHandle;
  iEvent.getByToken(genProductToken_, genHandle);
  if(genHandle.isValid()){
    auto helper = makeHelper(genHandle.product(),norm_);
    auto holder = luminosityBlockCache(iEvent.getLuminosityBlock().index());
    if(!found_scales and nScales_>0)
      found_scales = helper.fillWeights(scaleweights.get(),0,nScales_,wtype::scale,holder->scaleWeightIndices_);
    if(!found_pss and nPSs_>0)
      found_pss = helper.fillWeights(psweights.get(),0,nPSs_,wtype::ps,holder->psWeightIndices_);
  }

  iEvent.put(std::move(scaleweights),"ScaleWeights");
  iEvent.put(std::move(pdfweights),"PDFweights");
  iEvent.put(std::move(psweights),"PSweights");
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
