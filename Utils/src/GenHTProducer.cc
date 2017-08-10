
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

#include "TVector2.h"

//
// class declaration
//



class GenHTProducer : public edm::global::EDProducer<> {
public:
  explicit GenHTProducer(const edm::ParameterSet&);
  ~GenHTProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  // ----------member data ---------------------------
  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
};

GenHTProducer::GenHTProducer(const edm::ParameterSet& iConfig) : getterOfProducts_(edm::ProcessMatch("*"), this)
{
  callWhenNewProductsRegistered(getterOfProducts_);
  produces<double>("genHT");
}

GenHTProducer::~GenHTProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}

void GenHTProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;

  // first calculate genHT
  double genHT = 0.0;

  std::vector<edm::Handle<LHEEventProduct> > handles;
  getterOfProducts_.fillHandles(iEvent, handles);

  if(!handles.empty()){
    edm::Handle<LHEEventProduct> evt = handles[0];
    const lhef::HEPEUP hepeup_ = evt->hepeup();
    const int nup_ = hepeup_.NUP;
    const std::vector<int> idup_ = hepeup_.IDUP;
    const std::vector<lhef::HEPEUP::FiveVector> pup_ = hepeup_.PUP;
    const std::vector<int> istup_ = hepeup_.ISTUP;
    const std::vector<std::pair<int,int> > momup_ = hepeup_.MOTHUP;

    for ( unsigned int icount = 0 ; icount < (unsigned int)nup_; icount++ ) {
      int PID    = idup_[icount];
      int status = istup_[icount];
      int mom1id = abs(idup_[momup_[icount].first-1]);
      int mom2id = abs(idup_[momup_[icount].second-1]);
      double px = (pup_[icount])[0];
      double py = (pup_[icount])[1];
      double pt = sqrt(px*px+py*py);

      if(status==1 && (abs(PID)<6 || abs(PID)==21) && mom1id!=6 && mom1id!=24 && mom2id!=6 && mom2id!=24) { // gen HT used to bin samples does not count top/W decay products
        genHT += pt;
      }
    }
  }

  auto genHT_ = std::make_unique<double>(genHT);
  iEvent.put(std::move(genHT_), "genHT");
  
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenHTProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenHTProducer);
