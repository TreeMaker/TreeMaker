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
#include <TLorentzVector.h>

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
   produces<int>("ZNum");
   produces<std::vector<TLorentzVector>>("Zp4");
}

void ZProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   std::auto_ptr<std::vector<TLorentzVector>> Zp4(new std::vector<TLorentzVector>());
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
               theZ.addDaughter(*iL1, "positive daughter");
               theZ.addDaughter(*iL2, "negative daughter");
               ZCandidates->push_back(theZ);
               TLorentzVector p4temp(theZ.px(), theZ.py(), theZ.pz(), theZ.energy());
               Zp4->push_back(p4temp);
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
               theZ.addDaughter(*iL1, "positive daughter");
               theZ.addDaughter(*iL2, "negative daughter");
               ZCandidates->push_back(theZ);
               TLorentzVector p4temp(theZ.px(), theZ.py(), theZ.pz(), theZ.energy());
               Zp4->push_back(p4temp);
            }
         }
      }
   }

   // add the number of Z candidates to the event
   std::auto_ptr<int> item0(new int(ZCandidates->size()));
	iEvent.put(item0, std::string("ZNum"));

   // add the TLorentzVectors to the event
   
	iEvent.put(Zp4, std::string("Zp4"));

   // add the Z candidates to the event
   
   iEvent.put(ZCandidates, std::string("ZCandidates"));
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZProducer);

