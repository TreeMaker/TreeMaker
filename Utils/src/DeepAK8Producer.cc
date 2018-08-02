// system include files
#include <memory>
#include <vector>
#include <string>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
// new includes
#include "NNKit/FatJetNN/interface/FatJetNN.h"
#include "NNKit/FatJetNN/interface/FatJetNNHelper.h"

#include "TLorentzVector.h"

class DeepAK8Producer : public edm::stream::EDProducer<> {
public:
    explicit DeepAK8Producer(const edm::ParameterSet&);
private:
    void produce(edm::Event&, const edm::EventSetup&) override;
    template <class T>
    void helpProduce(edm::Event& iEvent, const edm::Handle<edm::View<pat::Jet>>& jets, const std::vector<T>& vec, std::string name) const;
    edm::EDGetTokenT<edm::View<pat::Jet>> JetAK8Tok_;

    std::unique_ptr<deepntuples::FatJetNN> fatjetNN_;
};

DeepAK8Producer::DeepAK8Producer(const edm::ParameterSet& iConfig) :
    JetAK8Tok_(consumes<edm::View<pat::Jet>>(iConfig.getParameter<edm::InputTag>("JetAK8")))
{
    // Initialize the FatJetNN class in the constructor
    auto cc = consumesCollector();
    fatjetNN_ = std::make_unique<deepntuples::FatJetNN>(iConfig, cc);
    const auto& datapath_(iConfig.getParameter<std::string>("datapath"));
    // Load json for input variable transformation
    fatjetNN_->load_json(edm::FileInPath(datapath_+"/preprocessing.json").fullPath());
    // Load DNN model and parameter files
    fatjetNN_->load_model(edm::FileInPath(datapath_+"/resnet-symbol.json").fullPath(), edm::FileInPath(datapath_+"/resnet.params").fullPath());

    // Declare what is produced
    produces<edm::ValueMap<float>>("tDiscriminatorDeep");
    produces<edm::ValueMap<float>>("wDiscriminatorDeep");
    produces<edm::ValueMap<float>>("zDiscriminatorDeep");
    produces<edm::ValueMap<float>>("hDiscriminatorDeep");
}

template <class T>
void DeepAK8Producer::helpProduce(edm::Event& iEvent, const edm::Handle<edm::View<pat::Jet>>& jets, const std::vector<T>& vec, std::string name) const
{
    // Store as userfloat
    auto out = std::make_unique<edm::ValueMap<T>>();
    typename edm::ValueMap<T>::Filler filler(*out);
    filler.insert(jets, vec.begin(), vec.end());
    filler.fill();
    iEvent.put(std::move(out),name);
}

void DeepAK8Producer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    // Need to access event info
    fatjetNN_->readEvent(iEvent, iSetup);

    // Get, loop over the jets, and fill  
    edm::Handle<edm::View<pat::Jet>> jetDeepAK8;
    iEvent.getByToken(JetAK8Tok_, jetDeepAK8);

    std::vector<float> tDiscriminatorDeep, wDiscriminatorDeep, zDiscriminatorDeep, hDiscriminatorDeep;

    for(const pat::Jet& fatjet : *jetDeepAK8) 
    {
        // Run the NN predictions
        deepntuples::JetHelper jet_helper(&fatjet);
        const auto& nnpreds = fatjetNN_->predict(jet_helper);
        deepntuples::FatJetNNHelper nn(nnpreds);
        
        // Get the scores
        tDiscriminatorDeep.push_back(nn.get_binarized_score_top());
        wDiscriminatorDeep.push_back(nn.get_binarized_score_w());
        zDiscriminatorDeep.push_back(nn.get_binarized_score_z());
        hDiscriminatorDeep.push_back(nn.get_binarized_score_hbb());
    }

    // Make userfloat maps
    helpProduce(iEvent,jetDeepAK8,tDiscriminatorDeep,"tDiscriminatorDeep");
    helpProduce(iEvent,jetDeepAK8,wDiscriminatorDeep,"wDiscriminatorDeep");
    helpProduce(iEvent,jetDeepAK8,zDiscriminatorDeep,"zDiscriminatorDeep");
    helpProduce(iEvent,jetDeepAK8,hDiscriminatorDeep,"hDiscriminatorDeep");
}

DEFINE_FWK_MODULE(DeepAK8Producer);
