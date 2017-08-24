// system include files
#include <memory>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

class MinDeltaRDouble : public edm::global::EDProducer<> {
public:
	explicit MinDeltaRDouble(const edm::ParameterSet&);
private:
   virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   edm::EDGetTokenT<std::vector<reco::GenParticle>> genParticlesToken_;
};

MinDeltaRDouble::MinDeltaRDouble(const edm::ParameterSet& iConfig)
{
   genParticlesToken_ = consumes<std::vector<reco::GenParticle>>(edm::InputTag("prunedGenParticles"));
   produces<double>("madMinPhotonDeltaR");
   produces<int>("madMinDeltaRStatus");
}

void MinDeltaRDouble::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   double minDR = 999.;
   int status = 0;
   
   edm::Handle<std::vector<reco::GenParticle>> pruned;
   iEvent.getByToken(genParticlesToken_, pruned);
   if (pruned.isValid()) {
      reco::GenParticle * gen;
      // try to get the hard process photon or Z (DY/Zinv/GJets MC)
      bool haveGen = false;
      for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
         if ((iG->pdgId()==22&&iG->status()==23) || (iG->pdgId()==23&&iG->status()==22)) {
            gen = iG->clone();
            haveGen = true;
            status = gen->status();
            break;
         }
      }
      // try to get the highest pT photon with a parton mother (QCD)
      if (!haveGen) {
         double maxPt = 0.;
         for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
            if (iG->pdgId()==22) {
               const int motherID = std::abs(iG->mother()->pdgId());
               if ((motherID>=1 && motherID<=6) || motherID==21) {
                  if (iG->pt() > maxPt) {
                     gen = iG->clone();
                     haveGen = true;
                     status = gen->status();
                     maxPt = iG->pt();
                  }
               }
            }
         }
      }
      // try to get the highest pT photon
      if (!haveGen) {
         double maxPt = 0.;
         for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
            if (iG->pdgId()==22) {
               if (iG->pt() > maxPt) {
                  gen = iG->clone();
                  haveGen = true;
                  status = -gen->status();
                  maxPt = iG->pt();
               }
            }
         }
      }
      // now calculate deltaR
      if (haveGen) {
         for (auto iG = pruned->begin(); iG != pruned->end(); ++iG) {
            if (iG->status()==23) {
               const int tempID = std::abs(iG->pdgId());
               if ((tempID>=1 && tempID<=6) || tempID==21) {
                  double tempDR = deltaR(gen->p4(), iG->p4());
                  if (tempDR < minDR) minDR = tempDR;
               }
            }
         }
      } 
   } else {
      edm::LogWarning("TreeMaker") << "MinPhotonDeltaRDouble::Error tag invalid: " << "prunedGenParticles";
   }

   auto htp0 = std::make_unique<double>(minDR);
   iEvent.put(std::move(htp0), "madMinPhotonDeltaR");

   auto htp1 = std::make_unique<int>(status);
   iEvent.put(std::move(htp1), "madMinDeltaRStatus");
}

//define this as a plug-in
DEFINE_FWK_MODULE(MinDeltaRDouble);

