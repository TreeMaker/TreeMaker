#include <iostream>
#include <cmath>
#include <memory>
#include <vector>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include <Pythia8/Pythia.h>

namespace LHAPDF {
  void initPDFSet(int nset, const std::string& filename, int member=0);
  int numberPDF(int nset);
  void usePDFMember(int nset, int member);
  double xfx(int nset, double x, double Q, int fl);
  void setVerbosity(int v);
}

class PDFRecalculator : public edm::one::EDProducer<> {
public:
  explicit PDFRecalculator(const edm::ParameterSet&);
  ~PDFRecalculator() override {}

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  int lhapdfPDGID(const int pdgid) const { return std::abs(pdgid) == 21 ? 0 : pdgid; }
  void produce(edm::Event&, const edm::EventSetup&) override;

  // ----------member data ---------------------------
  bool norm_, debug_, recalculatePDFs_, recalculateScales_;
  unsigned nQCD_, nEM_;
  std::string pdfSetName_;
  edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;
  std::unique_ptr<Pythia8::Pythia> pythia_;
};

PDFRecalculator::PDFRecalculator(const edm::ParameterSet& iConfig) :
  norm_(iConfig.getParameter<bool>("normalize")),
  debug_(iConfig.getParameter<bool>("debug")),
  recalculatePDFs_(iConfig.getParameter<bool>("recalculatePDFs")),
  recalculateScales_(iConfig.getParameter<bool>("recalculateScales")),
  nQCD_(iConfig.getParameter<unsigned>("nQCD")),
  nEM_(iConfig.getParameter<unsigned>("nEM")),
  pdfSetName_(iConfig.getParameter<std::string>("pdfSetName")),
  genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator")))
{
  if(recalculatePDFs_){
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

  produces<std::vector<float>>("PDFweights");
  produces<std::vector<float>>("ScaleWeights");
}

//LHAPDF functions are not thread-safe, hence the use of a one:: module
void PDFRecalculator::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  auto pdfweights = std::make_unique<std::vector<float>>();
  auto scaleweights = std::make_unique<std::vector<float>>();

  edm::Handle<GenEventInfoProduct> genHandle;
  iEvent.getByToken(genProductToken_, genHandle);

  //recalculate pdf weights
  //taken from https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_X/ElectroWeakAnalysis/Utilities/src/PDFRecalculator.cc
  if(recalculatePDFs_){
    float Q = genHandle->pdf()->scalePDF;

    int id1 = lhapdfPDGID(genHandle->pdf()->id.first);
    double x1 = genHandle->pdf()->x.first;

    int id2 = lhapdfPDGID(genHandle->pdf()->id.second);
    double x2 = genHandle->pdf()->x.second;

    unsigned nweights = 1;
    if(LHAPDF::numberPDF(1)>1) nweights += LHAPDF::numberPDF(1);
    pdfweights->reserve(nweights);
    double norm = 1.;

    for (unsigned int i=0; i<nweights; ++i) {
      LHAPDF::usePDFMember(1,i);
      double newpdf1 = LHAPDF::xfx(1, x1, Q, id1)/x1;
      double newpdf2 = LHAPDF::xfx(1, x2, Q, id2)/x2;
      pdfweights->push_back(newpdf1*newpdf2);
      if(i==0 and norm_) norm = 1/pdfweights->back();
      pdfweights->back() *= norm;
      if(debug_) {
        edm::LogInfo("TreeMaker") << "PDFRecalculator: index = " << i << ", x1 = " << x1 << ", x2 = " << x2
                                  << ", Q = " << Q << ", id1 = " << id1 << ", id2 = " << id2
                                  << ", newpdf1 = " << newpdf1 << ", newpdf2 = " << newpdf2
                                  << ", norm = " << norm << ", pdfweight = " << pdfweights->back() << std::endl;
        }
      }
    }

  //recalculate rf scale weights
  //based on https://gitlab.cern.ch/cms-desy-top/TopAnalysis/-/blob/Htottbar_2016/ZTopUtils/plugins/EventWeightMCSystematicRecalc.cc
  if(recalculateScales_){
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
    LHAPDF::usePDFMember(1,0);
    pdf1 = LHAPDF::xfx(1, x1, Q, id1)/x1;
    pdf2 = LHAPDF::xfx(1, x2, Q, id2)/x2;
    pdf1up = LHAPDF::xfx(1, x1, kUp*Q, id1)/x1;
    pdf2up = LHAPDF::xfx(1, x2, kUp*Q, id2)/x2;
    pdf1dn = LHAPDF::xfx(1, x1, kDn*Q, id1)/x1;
    pdf2dn = LHAPDF::xfx(1, x2, kDn*Q, id2)/x2;
    if(debug_)
      edm::LogInfo("TreeMaker") << "PDFRecalculator: x1 = " << x1 << ", x2 = " << x2 << ", Q = " << Q
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
      edm::LogInfo("TreeMaker") << "PDFRecalculator: alpEM = " << alpEM << ", alpEMup = " << alpEMup
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

  iEvent.put(std::move(pdfweights),"PDFweights");
  iEvent.put(std::move(scaleweights),"ScaleWeights");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PDFRecalculator::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PDFRecalculator);
