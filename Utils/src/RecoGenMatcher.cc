// system include files
#include <vector>
#include <utility>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

// new includes
#include "TreeMaker/Utils/interface/matchAB.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

class RecoGenMatcher : public edm::global::EDProducer<> {
  public:
    explicit RecoGenMatcher(const edm::ParameterSet&);
  private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
    edm::InputTag JetTag_, GenJetTag_;
    edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
    edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok_;
};

RecoGenMatcher::RecoGenMatcher(const edm::ParameterSet& iConfig) :
  JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
  GenJetTag_(iConfig.getParameter<edm::InputTag>("GenJetTag")),
  JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
  GenJetTok_(consumes<edm::View<reco::GenJet>>(GenJetTag_))
{
  produces<std::vector<int>>();
}

void RecoGenMatcher::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  //get the collections
  edm::Handle<edm::View<pat::Jet>> h_jets;
  iEvent.getByToken(JetTok_, h_jets);

  edm::Handle<edm::View<reco::GenJet>> h_genjets;
  iEvent.getByToken(GenJetTok_, h_genjets);

  auto genIndex = std::make_unique<std::vector<int>>();

  //gen:reco jet matching
  *genIndex = utils::matchAB(*(h_jets.product()), *(h_genjets.product()));

  iEvent.put(std::move(genIndex));
}

DEFINE_FWK_MODULE(RecoGenMatcher);
