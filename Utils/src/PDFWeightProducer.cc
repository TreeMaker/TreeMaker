#include <iostream>
#include <cmath>
#include <memory>
#include <mutex>
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

#include "TVector2.h"

#include <Pythia8/Pythia.h>

enum class wtype { scale = 0, pdf = 1, ps = 2 };

template <class P>
class PDFWeightHelper {
  public:
    PDFWeightHelper(const P* prod, bool use_norm) : product_(prod), use_norm_(use_norm) {}
    bool fillWeights(std::vector<float>* output, unsigned offset, unsigned nWeights, wtype wt) {
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
  int lhapdfPDGID(const int pdgid) const { return std::abs(pdgid) == 21 ? 0 : pdgid; }
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  
  // ----------member data ---------------------------
  unsigned nScales_, nPDFs_, nPSs_, nQCD_, nEM_;
  bool norm_, recalculatePDFs_, recalculateScales_, debug_;
  std::string pdfSetName_;
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
  edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;
  static std::mutex mutex_;
  std::unique_ptr<Pythia8::Pythia> pythia_;
};

std::mutex PDFWeightProducer::mutex_;

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) :
  nScales_(iConfig.getParameter<unsigned>("nScales")),
  nPDFs_(iConfig.getParameter<unsigned>("nPDFs")),
  nPSs_(iConfig.getParameter<unsigned>("nPSs")),
  nQCD_(iConfig.getParameter<unsigned>("nQCD")),
  nEM_(iConfig.getParameter<unsigned>("nEM")),
  norm_(iConfig.getParameter<bool>("normalize")),
  recalculatePDFs_(iConfig.getParameter<bool>("recalculatePDFs")),
  recalculateScales_(iConfig.getParameter<bool>("recalculateScales")),
  debug_(iConfig.getParameter<bool>("debug")),
  getterOfProducts_(edm::ProcessMatch("*"), this), 
  genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator")))
{
  if(recalculatePDFs_) pdfSetName_ = iConfig.getParameter<std::string>("pdfSetName");
  if(!pdfSetName_.empty()){
     LHAPDF::initPDFSet(1,pdfSetName_);
     LHAPDF::setVerbosity(0);
  }
  if(recalculateScales_){
    pythia_ = std::make_unique<Pythia8::Pythia>("../share/Pythia8/xmldoc",false);
    //from https://github.com/cms-sw/cmssw/blob/master/FastSimulation/ParticleDecay/src/PythiaDecays.cc
    pythia_->settings.flag("ProcessLevel:all", false);
    pythia_->settings.flag("Print:quiet", true);
    //following https://github.com/cms-sw/cmssw/blob/master/GeneratorInterface/Pythia8Interface/src/Py8InterfaceBase.cc
    const auto& manual_settings = iConfig.getParameter<std::vector<std::string>>("pythiaSettings");
    for(const auto& s : manual_settings){
      if(!pythia_->readString(s))
        throw cms::Exception("PythiaError") << "Pythia 8 did not accept \"" << s << "\"." << std::endl;
    }
    pythia_->init();
  }

  callWhenNewProductsRegistered(getterOfProducts_);
  produces<std::vector<float> >("ScaleWeights");
  produces<std::vector<float> >("PDFweights");
  produces<std::vector<float> >("PSweights");
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
  
  auto scaleweights = std::make_unique<std::vector<float>>();
  auto pdfweights = std::make_unique<std::vector<float>>();
  auto psweights = std::make_unique<std::vector<float>>();
  
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
    if((!found_scales and nScales_>0) or (!found_pdfs and nPDFs_>0)){
      unsigned offset = 1;
      //renormalization/factorization scale weights
      found_scales = helper.fillWeights(scaleweights.get(),offset,nScales_,wtype::scale);
      //pdf weights
      if(found_scales) found_pdfs = helper.fillWeights(pdfweights.get(),nScales_+offset,nPDFs_,wtype::pdf);
    }
    if(!found_pss and found_scales and nPSs_>0){
      unsigned offset = 0;
      std::cout << "PS WEIGHTS" << std::endl;
      found_pss = helper.fillWeights(psweights.get(),nScales_+offset,nPSs_,wtype::ps);
    }

    //if pdf weights still not found, recalculate them
    //taken from https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_X/ElectroWeakAnalysis/Utilities/src/PdfWeightProducer.cc
    if(!found_pdfs and recalculatePDFs_){

      float Q = genHandle->pdf()->scalePDF;

      int id1 = lhapdfPDGID(genHandle->pdf()->id.first);
      double x1 = genHandle->pdf()->x.first;

      int id2 = lhapdfPDGID(genHandle->pdf()->id.second);
      double x2 = genHandle->pdf()->x.second;

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
          if(debug_) {
            edm::LogInfo("TreeMaker") << "PDFWeightProducer: index = " << i << ", x1 = " << x1 << ", x2 = " << x2
                                      << ", Q = " << Q << ", id1 = " << id1 << ", id2 = " << id2
                                      << ", newpdf1 = " << newpdf1 << ", newpdf2 = " << newpdf2
                                      << ", norm = " << norm << ", pdfweight = " << pdfweights->back() << std::endl;
          }
        }
      }
      found_pdfs = true;
    }

    //if rf scale weights still not found, recalculate them
    //based on https://gitlab.cern.ch/cms-desy-top/TopAnalysis/-/blob/Htottbar_2016/ZTopUtils/plugins/EventWeightMCSystematicRecalc.cc
    if(!found_scales and recalculateScales_){
      double kUp = 2;
      double kDn = 0.5;
      float Q = genHandle->pdf()->scalePDF;

      //factorization scale
      int id1 = lhapdfPDGID(genHandle->pdf()->id.first);
      double x1 = genHandle->pdf()->x.first;

      int id2 = lhapdfPDGID(genHandle->pdf()->id.second);
      double x2 = genHandle->pdf()->x.second;

      double pdf1, pdf1up, pdf1dn;
      double pdf2, pdf2up, pdf2dn;
      {
         std::lock_guard<std::mutex> lock(mutex_);
         LHAPDF::usePDFMember(1,0);
         pdf1 = LHAPDF::xfx(1, x1, Q, id1)/x1;
         pdf2 = LHAPDF::xfx(1, x2, Q, id2)/x2;
         pdf1up = LHAPDF::xfx(1, x1, kUp*Q, id1)/x1;
         pdf2up = LHAPDF::xfx(1, x2, kUp*Q, id2)/x2;
         pdf1dn = LHAPDF::xfx(1, x1, kDn*Q, id1)/x1;
         pdf2dn = LHAPDF::xfx(1, x2, kDn*Q, id2)/x2;
      }
      if(debug_)
        edm::LogInfo("TreeMaker") << "PDFWeightProducer: x1 = " << x1 << ", x2 = " << x2 << ", Q = " << Q
                                  << ", id1 = " << id1 << ", id2 = " << id2 << ", kUp = " << kUp << ", pdf1 = " << pdf1
                                  << ", pdf1up = " << pdf1up << ", pdf1dn = " << pdf1dn << ", pdf2 = " << pdf2
                                  << ", pdf2up = " << pdf2up << ", pdf2dn = " << pdf2dn << std::endl;

      float weightFacUp = (pdf1up*pdf2up)/(pdf1*pdf2);
      float weightFacDn = (pdf1dn*pdf2dn)/(pdf1*pdf2);

      //renormalization scale
      //compute directly from Pythia for consistency
      auto coup = pythia_->couplingsPtr;
      double Q2 = Q*Q;
      double alpEM = coup->alphaEM(Q2);
      double alpEMup = coup->alphaEM(kUp*kUp*Q2);
      double alpEMdn = coup->alphaEM(kDn*kDn*Q2);
      double alpS = coup->alphaS(Q2);
      double alpSup = coup->alphaS(kUp*kUp*Q2);
      double alpSdn = coup->alphaS(kDn*kDn*Q2);
      if(debug_)
        edm::LogInfo("TreeMaker") << "PDFWeightProducer: alpEM = " << alpEM << ", alpEMup = " << alpEMup
                                  << ", alpEMdn = " << alpEMdn << ", alpS = " << alpS << ", alpSup = " << alpSup
                                  << ", alpSdn = " << alpSdn << std::endl;

      //weights require process-dependent information about number of QCD and EM vertices
      float weightRenUp = std::pow(alpEMup/alpEM, nEM_) * std::pow(alpSup/alpS, nQCD_);
      float weightRenDn = std::pow(alpEMdn/alpEM, nEM_) * std::pow(alpSdn/alpS, nQCD_);

      //compute all variations to be consistent w/ what madgraph provides:
      //[mur=1, muf=1], [mur=1, muf=2], [mur=1, muf=0.5], [mur=2, muf=1], [mur=2, muf=2], [mur=2, muf=0.5], [mur=0.5, muf=1], [mur=0.5, muf=2], [mur=0.5, muf=0.5]
      *scaleweights = {
        1.0,
        weightFacUp,
        weightFacDn,
        weightRenUp,
        weightRenUp*weightFacUp,
        weightRenUp*weightFacDn,
        weightRenDn,
        weightRenDn*weightFacUp,
        weightRenDn*weightFacDn
      };
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
