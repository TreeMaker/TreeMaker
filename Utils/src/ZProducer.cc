// system include files
#include <memory>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"

class ZProducer : public edm::EDProducer {
public:
	explicit ZProducer(const edm::ParameterSet&);
private:
   virtual void produce(edm::Event&, const edm::EventSetup&);
   edm::InputTag ElectronTag_;
   edm::InputTag MuonTag_;
};

ZProducer::ZProducer(const edm::ParameterSet& iConfig)
{
   ElectronTag_ = iConfig.getParameter<edm::InputTag>("ElectronTag");
   MuonTag_ = iConfig.getParameter<edm::InputTag>("MuonTag");
   produces<pat::CompositeCandidateCollection>("ZCandidates");
}

void ZProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   std::auto_ptr<pat::CompositeCandidateCollection> ZCandidates(new pat::CompositeCandidateCollection());

   // make candidates from electrons
   edm::Handle<std::vector<pat::Electron>> electronHandle;
	iEvent.getByLabel(ElectronTag_, electronHandle);
   const std::vector<pat::Electron> * electrons = electronHandle.product();
   for (std::vector<pat::Electron>::const_iterator iL1 = electrons->begin(); iL1 != electrons->end(); ++iL1) {
      if (iL1->charge() > 0) {
         for (std::vector<pat::Electron>::const_iterator iL2 = electrons->begin(); iL2 != electrons->end(); ++iL2) {
            if (iL2->charge() < 0) {
               pat::CompositeCandidate theZ;
               theZ.setP4(iL1->p4()+ iL2->p4());
               theZ.addDaughter(*iL1, "positive electron daughter");
               theZ.addDaughter(*iL2, "negative electron daughter");
               ZCandidates->push_back(theZ);
            }
         }
      }
   }

   // make candidates from muons
   edm::Handle<std::vector<pat::Muon>> muonHandle;
	iEvent.getByLabel(MuonTag_, muonHandle);
   const std::vector<pat::Muon> * muons = muonHandle.product();
   for (std::vector<pat::Muon>::const_iterator iL1 = muons->begin(); iL1 != muons->end(); ++iL1) {
      if (iL1->charge() > 0) {
         for (std::vector<pat::Muon>::const_iterator iL2 = muons->begin(); iL2 != muons->end(); ++iL2) {
            if (iL2->charge() < 0) {
               pat::CompositeCandidate theZ;
               theZ.setP4(iL1->p4()+iL2->p4());
               theZ.addDaughter(*iL1, "positive muon daughter");
               theZ.addDaughter(*iL2, "negative muon daughter");
               ZCandidates->push_back(theZ);
            }
         }
      }
   }

   // add the Z candidates to the event
   iEvent.put(ZCandidates, std::string("ZCandidates"));
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZProducer);

