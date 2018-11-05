// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
#include <TVector2.h>
//
// class declaration
//

class BasicJetRemover : public edm::global::EDProducer<> {
public:
   explicit BasicJetRemover(const edm::ParameterSet&);
   ~BasicJetRemover() override;
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   
   edm::InputTag JetTag_;
   edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
};

using namespace pat;
BasicJetRemover::BasicJetRemover(const edm::ParameterSet& iConfig)
{
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
   
   produces<std::vector<Jet> >();
}


BasicJetRemover::~BasicJetRemover() { }


void
BasicJetRemover::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   using namespace edm;
   
   auto prodJets = std::make_unique<std::vector<Jet>>();

   edm::Handle< edm::View<Jet> > Jets;
   iEvent.getByToken(JetTok_,Jets);

   if(Jets.isValid())
   {
      prodJets->reserve(Jets->size());
      for(const auto & iJet : *Jets)
      {
         if (!iJet.isPFJet()) continue;
         prodJets->push_back(Jet(iJet));
      }
   }

   // put in the event
   iEvent.put(std::move(prodJets));
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
BasicJetRemover::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(BasicJetRemover);
