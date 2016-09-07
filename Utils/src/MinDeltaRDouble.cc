// system include files
#include <memory>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

class MinDeltaRDouble : public edm::EDProducer {
public:
	explicit MinDeltaRDouble(const edm::ParameterSet&);
private:
   virtual void produce(edm::Event&, const edm::EventSetup&);
   edm::EDGetTokenT<std::vector<reco::GenParticle>> genParticlesToken_;
};

MinDeltaRDouble::MinDeltaRDouble(const edm::ParameterSet& iConfig)
{
   genParticlesToken_ = consumes<std::vector<reco::GenParticle>>(edm::InputTag("prunedGenParticles"));
   produces<double>("");
}

void MinDeltaRDouble::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   double minDR = 999.;
   
   edm::Handle<std::vector<reco::GenParticle>> pruned;
   iEvent.getByToken(genParticlesToken_, pruned);
   if (pruned.isValid()) {
      for (auto iG1 = pruned->begin(); iG1 != pruned->end(); ++iG1) {
         if (iG1->isHardProcess() && (iG1->pdgId()==22 || iG1->pdgId()==23)) {
            for (auto iG2 = pruned->begin(); iG2 != pruned->end(); ++iG2) {
               if (iG2->isHardProcess()) {
                  int tempID = std::abs(iG2->pdgId());
                  if ((tempID>=1 && tempID<=6) || tempID==21) {
                     double tempDR = deltaR(iG1->p4(), iG2->p4());
                     if (tempDR < minDR) minDR = tempDR;
                  }
               }
            }
         }
      }
   } else {
      std::cout << "MinPhotonDeltaRDouble::Error tag invalid: " << "prunedGenParticles" << std::endl;
   }

   auto htp = std::make_unique<double>(minDR);
   iEvent.put(std::move(htp));
  
}

//define this as a plug-in
DEFINE_FWK_MODULE(MinDeltaRDouble);

