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
      reco::GenParticle gen;
      // target GJets, DY, and Zinv MC
      bool haveGen = false;
      for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
         if (iG->status()==23 && (iG->pdgId()==22 || iG->pdgId()==23)) {
            gen = *iG;
            haveGen = true;
            break;
         }
      }
      // target QCD MC (or anything else really)
      if (!haveGen) {
         double maxPt = 0.;
         for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
            if (iG->pdgId()==22) {
               if (iG->pt() > maxPt) {
                  gen = *iG;
                  maxPt = iG->pt();
                  haveGen = true;
               }
            }
         }
      }
      // now calculate deltaR
      if (haveGen) {
         for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
            if (iG->status()==23) {
               int tempID = std::abs(iG->pdgId());
               if ((tempID>=1 && tempID<=6) || tempID==21) {
                  double tempDR = deltaR(gen.p4(), iG->p4());
                  if (tempDR < minDR) minDR = tempDR;
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

