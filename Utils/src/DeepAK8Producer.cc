// system include files
#include <memory>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <TMath.h>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "NNKit/FatJetNN/interface/FatJetNN.h"
#include "NNKit/FatJetNN/interface/FatJetNNHelper.h"

#include "TLorentzVector.h"

class DeepAK8Producer : public edm::global::EDProducer<> {
public:
    explicit DeepAK8Producer(const edm::ParameterSet&);
private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
    edm::EDGetTokenT<edm::View<pat::Jet>> JetAK8Tok_;

    deepntuples::FatJetNN* fatjetNN_;
};

DeepAK8Producer::DeepAK8Producer(const edm::ParameterSet& iConfig) :
    JetAK8Tok_(consumes<edm::View<pat::Jet>>(iConfig.getUntrackedParameter<edm::InputTag>("JetDeepAK8", edm::InputTag("slimmedJetsAK8")))),
    fatjetNN_(nullptr)
{
    // Initialize the FatJetNN class in the constructor
    auto cc = consumesCollector();
    fatjetNN_ = new deepntuples::FatJetNN(iConfig, cc);
    // Load json for input variable transformation
    fatjetNN_->load_json("preprocessing.json"); // use the full path or put the file in the current working directory (i.e., where you run cmsRun)
    // Load DNN model and parameter files
    fatjetNN_->load_model("resnet-symbol.json", "resnet.params"); // use the full path or put the file in the current working directory (i.e., where you run cmsRun)

    // Declare what is produced
    produces<edm::ValueMap<float>>("tDiscriminatorDeep");
    produces<edm::ValueMap<float>>("wDiscriminatorDeep");
}

void DeepAK8Producer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
    // Need to access event info
    fatjetNN_->readEvent(iEvent, iSetup);

    // Get, loop over the jets, and fill  
    edm::Handle<edm::View<pat::Jet>> jetDeepAK8;
    iEvent.getByToken(JetAK8Tok_, jetDeepAK8);

    auto tDiscriminatorDeep = std::make_unique<std::vector<double>>();
    auto wDiscriminatorDeep = std::make_unique<std::vector<double>>();

    for(const pat::Jet& fatjet : *jetDeepAK8) 
    {
        // Run the NN predictions
        deepntuples::JetHelper jet_helper(&fatjet);
        const auto& nnpreds = fatjetNN_->predict(jet_helper);
        deepntuples::FatJetNNHelper nn(nnpreds);
        
        // Get the scores
        tDiscriminatorDeep->push_back(nn.get_binarized_score_top());
        wDiscriminatorDeep->push_back(nn.get_binarized_score_w());
    }

    iEvent.put(std::move(tDiscriminatorDeep), "tDiscriminatorDeep");
    iEvent.put(std::move(wDiscriminatorDeep), "wDiscriminatorDeep");
}

DEFINE_FWK_MODULE(DeepAK8Producer);
