#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"

#include <iostream>
#include <vector>
#include <cmath>

class GenTopProducer : public edm::global::EDProducer<> {

public:
  explicit GenTopProducer(const edm::ParameterSet&);
  ~GenTopProducer();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  double getSF(const reco::GenParticle& part) const;
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  
  // ----------member data ---------------------------
  
  double a, b;
  edm::InputTag genEvtTag;
  edm::EDGetTokenT<TtGenEvent> genEvtTok;
};

GenTopProducer::GenTopProducer(const edm::ParameterSet& iConfig):
  a(iConfig.getParameter<double>("a")),
  b(iConfig.getParameter<double>("b")),
  genEvtTag(iConfig.getParameter<edm::InputTag>("genEvent")),
  genEvtTok(consumes<TtGenEvent>(genEvtTag))
{
  produces<std::vector<reco::GenParticle>>();
  produces<double>("weight");
}

GenTopProducer::~GenTopProducer()
{
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
}

//
// member functions
//

//helper
double GenTopProducer::getSF(const reco::GenParticle& part) const {
  return exp(a+b*part.pt());
}

// ------------ method called for each event  ------------
void
GenTopProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  edm::Handle<TtGenEvent> genEvt;
  iEvent.getByToken(genEvtTok, genEvt);

  auto genTop_vec = std::make_unique<std::vector<reco::GenParticle>>();

  //store t, then tbar (if present)
  const reco::GenParticle* tmp = NULL;
  tmp = genEvt->top();
  if(tmp) genTop_vec->push_back(*tmp);
  tmp = genEvt->topBar();
  if(tmp) genTop_vec->push_back(*tmp);
  
  double weight = 1.0;
  if(genTop_vec->size()==2) {
    weight = sqrt(getSF(genTop_vec->at(0))*getSF(genTop_vec->at(1)));
  }
  auto pWeight = std::make_unique<double>(weight);

  iEvent.put(std::move(genTop_vec));
  iEvent.put(std::move(pWeight),"weight");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenTopProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  */

}

#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(GenTopProducer);
