// system include files
#include <memory>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"

class ZProducer : public edm::global::EDProducer<> {
public:
	explicit ZProducer(const edm::ParameterSet&);
private:
   void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   edm::InputTag ElectronTag_;
   edm::InputTag MuonTag_;
   edm::EDGetTokenT<std::vector<pat::Electron>> ElectronTok_;
   edm::EDGetTokenT<std::vector<pat::Muon>> MuonTok_;
};

ZProducer::ZProducer(const edm::ParameterSet& iConfig)
{
   ElectronTag_ = iConfig.getParameter<edm::InputTag>("ElectronTag");
   MuonTag_ = iConfig.getParameter<edm::InputTag>("MuonTag");
   
   ElectronTok_ = consumes<std::vector<pat::Electron>>(ElectronTag_);
   MuonTok_ = consumes<std::vector<pat::Muon>>(MuonTag_);
   
   produces<pat::CompositeCandidateCollection>("ZCandidates");
}

void ZProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   auto ZCandidates = std::make_unique<pat::CompositeCandidateCollection>();

   // make candidates from electrons
   edm::Handle<std::vector<pat::Electron>> electronHandle;
   iEvent.getByToken(ElectronTok_, electronHandle);
   const std::vector<pat::Electron> * electrons = electronHandle.product();
   for (std::vector<pat::Electron>::const_iterator iL1 = electrons->begin(); iL1 != electrons->end(); ++iL1) {
      if (iL1->charge() > 0) {
         for (const auto & electron : *electrons) {
            if (electron.charge() < 0) {
               pat::CompositeCandidate theZ;
               theZ.setP4(iL1->p4()+ electron.p4());
               theZ.addDaughter(*iL1, "positive electron daughter");
               theZ.addDaughter(electron, "negative electron daughter");
               ZCandidates->push_back(theZ);
            }
         }
      }
   }

   // make candidates from muons
   edm::Handle<std::vector<pat::Muon>> muonHandle;
   iEvent.getByToken(MuonTok_, muonHandle);
   const std::vector<pat::Muon> * muons = muonHandle.product();
   for (std::vector<pat::Muon>::const_iterator iL1 = muons->begin(); iL1 != muons->end(); ++iL1) {
      if (iL1->charge() > 0) {
         for (const auto & muon : *muons) {
            if (muon.charge() < 0) {
               pat::CompositeCandidate theZ;
               theZ.setP4(iL1->p4()+muon.p4());
               theZ.addDaughter(*iL1, "positive muon daughter");
               theZ.addDaughter(muon, "negative muon daughter");
               ZCandidates->push_back(theZ);
            }
         }
      }
   }

   // add the Z candidates to the event
   iEvent.put(std::move(ZCandidates), std::string("ZCandidates"));
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZProducer);

