#include <iostream>
#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
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



class PDFWeightProducer : public edm::EDProducer {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
	
  // ----------member data ---------------------------
};

namespace LHAPDF {
       void initPDFSet(int nset, const std::string& filename, int member=0);
       int numberPDF(int nset);
       void usePDFMember(int nset, int member);
       double xfx(int nset, double x, double Q, int fl);
       double getXmin(int nset, int member);
       double getXmax(int nset, int member);
       double getQ2min(int nset, int member);
       double getQ2max(int nset, int member);
       void extrapolate(bool extrapolate=true);
}

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig)
{
  produces<std::vector<double> >("PDFweights");
  produces<std::vector<int> >("PDFids");
}

PDFWeightProducer::~PDFWeightProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}

void PDFWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //  std::cout<<"Running PDFWeightProducer"<<std::endl;
 
  using namespace edm;

  edm::Handle<GenEventInfoProduct> GenInfo;
  iEvent.getByLabel("generator",GenInfo);

  std::vector<double> pdfweights;
  std::vector<int> pdfids;
  pdfweights.clear();
  pdfids.clear();

  // pdf inputs  
  double q = GenInfo->pdf()->scalePDF;
  int id1 = GenInfo->pdf()->id.first;
  int id2 = GenInfo->pdf()->id.second;
  double x1 = GenInfo->pdf()->x.first;
  double x2 = GenInfo->pdf()->x.second;

  // weirdo LHA conventions, gluons are 0
  if (id1 == 21) id1 = 0;
  if (id2 == 21) id2 = 0;

  int N_pdfsets = 3; // hard-coded for now...
  int pdfset_internalIdNumber = -99;
  int pdfid = -99;
  for (int i = 1; i <= N_pdfsets; i++){
    
    // std::cout << "inputs for PDF weights = " << q << "," << id1 << "," << id2 << "," << x1 << "," << x2 << std::endl;
    // std::cout << "...there are this many members = " << LHAPDF::numberPDF(i) << std::endl;
    // get central value
    LHAPDF::usePDFMember(i,0);
    double xpdf1 = LHAPDF::xfx(i, x1, q, id1);
    double xpdf2 = LHAPDF::xfx(i, x2, q, id2);
    double w0 = xpdf1 * xpdf2;

    pdfset_internalIdNumber = i*1000;

    int N_eigensets = LHAPDF::numberPDF(i);
    for (int j = 1; j <= N_eigensets; j++){
      
      LHAPDF::usePDFMember(i,j);
      double xpdf1_new = LHAPDF::xfx(i, x1, q, id1);
      double xpdf2_new = LHAPDF::xfx(i, x2, q, id2);
      double w_new = xpdf1_new * xpdf2_new;
      double lhaweight = w_new / w0;
      //pdf_weights.push_back(weight);
      pdfid = pdfset_internalIdNumber + j;
      
      // std::cout << "lhaweight " << pdfid << " = " << lhaweight << "..." << w_new << "," << w0 << std::endl;
      
      pdfweights.push_back(lhaweight);
      pdfids.push_back(pdfid);

    }
  }

  std::auto_ptr<std::vector<double> > pdfweights_(new std::vector<double>(pdfweights));
  iEvent.put(pdfweights_,"PDFweights");

  std::auto_ptr<std::vector<int> > pdfids_(new std::vector<int>(pdfids));
  iEvent.put(pdfids_,"PDFids");

}

// ------------ method called once each job just before starting event loop  ------------
void
PDFWeightProducer::beginJob()
{
  LHAPDF::initPDFSet(1, "NNPDF30_lo_as_0130.LHgrid");
  LHAPDF::initPDFSet(2, "CT10nlo.LHgrid");
  LHAPDF::initPDFSet(3, "MMHT2014nlo68cl.LHgrid");
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PDFWeightProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
PDFWeightProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PDFWeightProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PDFWeightProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PDFWeightProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
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
