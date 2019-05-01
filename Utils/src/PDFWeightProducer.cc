#include <iostream>
#include <cmath>
#include <memory>
#include <mutex>

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

enum class wtype { scale = 0, pdf = 1, ps = 2 };

template <class P>
class PDFWeightHelper {
  public:
    PDFWeightHelper(const P* prod, bool use_norm) : product_(prod), use_norm_(use_norm) {}
    bool fillWeights(std::vector<double>* output, unsigned offset, unsigned nWeights, wtype wt) {
      unsigned max = this->getMax();
      if(max==0 or offset > max) return false;
      double norm = use_norm_ ? 1./this->getNorm(offset,wt) : 1.;
      max = std::min(nWeights+offset,max);
      output->reserve(max-offset);
      for (unsigned int i = offset; i < max; i++) {
        output->push_back(this->getWeight(i)*norm);
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

namespace LHAPDF {
  void initPDFSet(int nset, const std::string& filename, int member=0);
  int numberPDF(int nset);
  void usePDFMember(int nset, int member);
  double xfx(int nset, double x, double Q, int fl);
  void setVerbosity(int v);
}

class PDFWeightProducer : public edm::global::EDProducer<> {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  
  // ----------member data ---------------------------
  unsigned nScales_, nPDFs_, nPSs_;
  bool norm_, recalculatePDFs_;
  std::string pdfSetName_;
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;
  static std::mutex mutex_;
};

std::mutex PDFWeightProducer::mutex_;

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) :
  nScales_(iConfig.getParameter<unsigned>("nScales")),
  nPDFs_(iConfig.getParameter<unsigned>("nPDFs")),
  nPSs_(iConfig.getParameter<unsigned>("nPSs")),
  norm_(iConfig.getParameter<bool>("normalize")),
  recalculatePDFs_(iConfig.getParameter<bool>("recalculatePDFs")),
  getterOfProducts_(edm::ProcessMatch("*"), this), 
  genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator")))
{
  if(recalculatePDFs_) pdfSetName_ = iConfig.getParameter<std::string>("pdfSetName");
  if(!pdfSetName_.empty()){
     LHAPDF::initPDFSet(1,pdfSetName_);
     LHAPDF::setVerbosity(0);
  }

  callWhenNewProductsRegistered(getterOfProducts_);
  produces<std::vector<double> >("ScaleWeights");
  produces<std::vector<double> >("PDFweights");
  produces<std::vector<double> >("PSweights");
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
  auto psweights = std::make_unique<std::vector<double>>();
  
  bool found_scales = false;
  bool found_pdfs = false;
  bool found_pss = false;
  
  if(!handles.empty()){
    edm::Handle<LHEEventProduct> LheInfo = handles[0];
    auto helper = makeHelper(LheInfo.product(),norm_);
    //renormalization/factorization scale weights
    found_scales = helper.fillWeights(scaleweights.get(),0,nScales_,wtype::scale);
    //pdf weights
    if(found_scales) found_pdfs = helper.fillWeights(pdfweights.get(),nScales_,nPDFs_,wtype::pdf);
  }
  
  //check GenEventInfoProduct if LHEEventProduct not found or empty
  //if LHEEventProduct was filled, check GenEventInfoProduct for parton shower weights from Pythia8
  edm::Handle<GenEventInfoProduct> genHandle;
  iEvent.getByToken(genProductToken_, genHandle);
  if(genHandle.isValid()){
    auto helper = makeHelper(genHandle.product(),norm_);
    if(!found_scales or !found_pdfs){
      unsigned offset = 1;
      //renormalization/factorization scale weights
      found_scales = helper.fillWeights(scaleweights.get(),offset,nScales_,wtype::scale);
      //pdf weights
      if(found_scales) found_pdfs = helper.fillWeights(pdfweights.get(),nScales_+offset,nPDFs_,wtype::pdf);
    }
    else if(!found_pss){
      unsigned offset = 0;
      found_pss = helper.fillWeights(psweights.get(),offset,nPSs_,wtype::ps);
    }

    //if pdf weights still not found, recalculate them
    //taken from https://github.com/cms-sw/cmssw/blob/master/ElectroWeakAnalysis/Utilities/src/PdfWeightProducer.cc
    //not sure what to do about missing scale weights
    if(!found_pdfs and recalculatePDFs_){
      float Q = genHandle->pdf()->scalePDF;

      int id1 = genHandle->pdf()->id.first;
      double x1 = genHandle->pdf()->x.first;
      double pdf1 = genHandle->pdf()->xPDF.first;

      int id2 = genHandle->pdf()->id.second;
      double x2 = genHandle->pdf()->x.second;
      double pdf2 = genHandle->pdf()->xPDF.second;
      if(pdf1 <= 0 && pdf2 <= 0) {
         std::lock_guard<std::mutex> lock(mutex_);
         LHAPDF::usePDFMember(1,0);
         pdf1 = LHAPDF::xfx(1, x1, Q, id1)/x1;
         pdf2 = LHAPDF::xfx(1, x2, Q, id2)/x2;
      }

      unsigned nweights = 1;
      if(LHAPDF::numberPDF(1)>1) nweights += LHAPDF::numberPDF(1);
      pdfweights->reserve(nweights);
      double norm = 1.;
      //make it thread safe
      {
        std::lock_guard<std::mutex> lock(mutex_);
        for (unsigned int i=0; i<nweights; ++i) {
          LHAPDF::usePDFMember(1,i);
          double newpdf1 = LHAPDF::xfx(1, x1, Q, id1)/x1;
          double newpdf2 = LHAPDF::xfx(1, x2, Q, id2)/x2;
          pdfweights->push_back(newpdf1*newpdf2);
          if(i==0 and norm_) norm = 1/pdfweights->back();
          pdfweights->back() *= norm;
        }
      }
      found_pdfs = true;
    }
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
