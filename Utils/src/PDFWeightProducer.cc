#include <iostream>
#include <cmath>
#include <memory>
#include <vector>
#include <string>
#include <array>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/ProcessMatch.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "SimDataFormats/GeneratorProducts/interface/GenWeightInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenWeightProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/PartonShowerWeightGroupInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/PdfWeightGroupInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/ScaleWeightGroupInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/WeightGroupInfo.h"

//indices: 0: PDF, 1: scale, 2: PS
typedef std::array<gen::WeightGroupData, 3> WeightGroupsToStore;
std::shared_ptr<WeightGroupsToStore> defaultCache() {
  auto holder = std::make_shared<WeightGroupsToStore>();
  holder->at(0) = {0, nullptr};
  holder->at(1) = {0, nullptr};
  holder->at(2) = {0, nullptr};
  return holder;
}

//many parts taken from PhysicsTools/NanoAOD/plugins/GenWeightsTableProducer.cc in https://github.com/cms-sw/cmssw/pull/32167
class PDFWeightProducer : public edm::global::EDProducer<edm::RunCache<WeightGroupsToStore>, edm::LuminosityBlockCache<WeightGroupsToStore>> {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer() override {}

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
  std::shared_ptr<WeightGroupsToStore> globalBeginRun(const edm::Run&, const edm::EventSetup&) const override;
  void globalEndRun(const edm::Run&, const edm::EventSetup&) const override {}
  std::shared_ptr<WeightGroupsToStore> globalBeginLuminosityBlock(const edm::LuminosityBlock&, const edm::EventSetup&) const override;
  void globalEndLuminosityBlock(const edm::LuminosityBlock&, const edm::EventSetup&) const override {}

  //helpers
  void fillPDF(std::vector<float>& product, const std::vector<double>& weights) const;
  void fillScale(std::vector<float>& product, const std::vector<double>& weights, const gen::ScaleWeightGroupInfo& info) const;
  void fillPS(std::vector<float>& product, const std::vector<double>& weights, const gen::PartonShowerWeightGroupInfo& info) const;

  // ----------member data ---------------------------
  bool debug_;
  bool storePDFs_, storeScales_, storePSs_;
  edm::InputTag lheRunTag_, lheWeightTag_, genWeightTag_;
  edm::EDGetTokenT<LHERunInfoProduct> lheRunToken_;
  edm::EDGetTokenT<GenWeightProduct> lheWeightToken_;
  edm::EDGetTokenT<GenWeightInfoProduct> lheWeightInfoToken_;
  edm::EDGetTokenT<GenWeightProduct> genWeightToken_;
  edm::EDGetTokenT<GenWeightInfoProduct> genWeightInfoToken_;
};

PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) :
  debug_(iConfig.getParameter<bool>("debug")),
  storePDFs_(iConfig.getParameter<bool>("storePDFs")),
  storeScales_(iConfig.getParameter<bool>("storeScales")),
  storePSs_(iConfig.getParameter<bool>("storePSs")),
  lheRunTag_(iConfig.getParameter<edm::InputTag>("lheRunTag")),
  lheWeightTag_(iConfig.getParameter<edm::InputTag>("lheWeightTag")),
  genWeightTag_(iConfig.getParameter<edm::InputTag>("genWeightTag")),
  lheRunToken_(consumes<LHERunInfoProduct, edm::InRun>(lheRunTag_)),
  lheWeightToken_(consumes<GenWeightProduct>(lheWeightTag_)),
  lheWeightInfoToken_(consumes<GenWeightInfoProduct, edm::InRun>(lheWeightTag_)),
  genWeightToken_(consumes<GenWeightProduct>(genWeightTag_)),
  genWeightInfoToken_(consumes<GenWeightInfoProduct, edm::InLumi>(genWeightTag_))
{
  produces<std::vector<float>>("ScaleWeights");
  produces<std::vector<float>>("PDFweights");
  produces<std::vector<float>>("PSweights");
}

std::shared_ptr<WeightGroupsToStore> PDFWeightProducer::globalBeginRun(const edm::Run& iRun, const edm::EventSetup& iSetup) const {
  auto holder = defaultCache();
  //skip if not needed
  if(!storePDFs_ and !storeScales_)
    return holder;

  std::vector<int> pdfIds;
  edm::Handle<LHERunInfoProduct> lheRunInfoHandle;
  //can't use getByToken in beginRun
  iRun.getByLabel(lheRunTag_, lheRunInfoHandle);
  if(lheRunInfoHandle.isValid()){
    //get pdf used to generate this sample
    pdfIds.push_back(lheRunInfoHandle->heprup().PDFSUP.first);
  }

  edm::Handle<GenWeightInfoProduct> lheWeightInfoHandle;
  //can't use getByToken in beginRun
  iRun.getByLabel(lheWeightTag_, lheWeightInfoHandle);
  if(lheWeightInfoHandle.isValid()){
    //pdf variations (only for original pdf)
    const auto& pdfgroups = lheWeightInfoHandle->pdfGroupsWithIndicesByLHAIDs(pdfIds);
    //only keep the first one
    if(!pdfgroups.empty())
      holder->at(0) = pdfgroups[0];

    //scale variations
    const auto& scalegroups = lheWeightInfoHandle->weightGroupsAndIndicesByType(gen::WeightType::kScaleWeights);
    //only keep the first one
    if(!scalegroups.empty())
      holder->at(1) = scalegroups[0];
  }

  return holder;
}

std::shared_ptr<WeightGroupsToStore> PDFWeightProducer::globalBeginLuminosityBlock(const edm::LuminosityBlock& iLumi, const edm::EventSetup& iSetup) const {
  auto holder = defaultCache();
  //skip if not needed
  if(!storePSs_ and !storeScales_)
    return holder;

  edm::Handle<GenWeightInfoProduct> genWeightInfoHandle;
  iLumi.getByToken(genWeightInfoToken_, genWeightInfoHandle);

  //get PS weights and maybe scale variations from gen
  if(genWeightInfoHandle.isValid()){
    //scale variations
    const auto& scalegroups = genWeightInfoHandle->weightGroupsAndIndicesByType(gen::WeightType::kScaleWeights);
    //only keep the first one
    if(!scalegroups.empty())
      holder->at(1) = scalegroups[0];

    //parton shower variations
    const auto& psgroups = genWeightInfoHandle->weightGroupsAndIndicesByType(gen::WeightType::kPartonShowerWeights);
    //only keep the first one
    if(!psgroups.empty())
      holder->at(2) = psgroups[0];
  }

  return holder;
}

void PDFWeightProducer::fillPDF(std::vector<float>& product, const std::vector<double>& weights) const {
  product.reserve(weights.size());
  product.insert(product.end(), weights.begin(), weights.end());
}

void PDFWeightProducer::fillScale(std::vector<float>& product, const std::vector<double>& weights, const gen::ScaleWeightGroupInfo& info) const {
  if(product.empty()){
    if(debug_)
      edm::LogWarning("TreeMaker") << "Did not find any scale weights for this event";
    return;
  }
  const unsigned nScales = 9;
  if(info.isWellFormed()){
    product.reserve(nScales);
    for(auto index : {info.centralIndex(), info.muR1muF2Index(), info.muR1muF05Index(), info.muR2muF1Index(), info.muR2muF2Index(), info.muR2muF05Index(), info.muR05muF1Index(), info.muR05muF2Index(), info.muR05muF05Index()}){
      product.emplace_back(weights.at(index));
    }
  }
  else {
    fillPDF(product, weights);
    edm::LogWarning("TreeMaker") << "Unexpected format found for scale weights; saving " << weights.size() << " elements";
  }
}

void PDFWeightProducer::fillPS(std::vector<float>& product, const std::vector<double>& weights, const gen::PartonShowerWeightGroupInfo& info) const {
  if(product.empty()){
    if(debug_)
      edm::LogWarning("TreeMaker") << "Did not find any PS weights for this event";
    return;
  }
  const unsigned nPSs = 14;
  if(info.isWellFormed()){
    product.reserve(nPSs);
    for(auto index : {info.weightIndexFromLabel("nominal"), info.weightIndexFromLabel("Baseline"), info.isrCombinedDownIndex(gen::PSVarType::red), info.fsrCombinedDownIndex(gen::PSVarType::red), info.isrCombinedUpIndex(gen::PSVarType::red), info.fsrCombinedUpIndex(gen::PSVarType::red), info.isrCombinedDownIndex(gen::PSVarType::def), info.fsrCombinedDownIndex(gen::PSVarType::def), info.isrCombinedUpIndex(gen::PSVarType::def), info.fsrCombinedUpIndex(gen::PSVarType::def), info.isrCombinedDownIndex(gen::PSVarType::con), info.fsrCombinedDownIndex(gen::PSVarType::con), info.isrCombinedUpIndex(gen::PSVarType::con), info.fsrCombinedUpIndex(gen::PSVarType::con)}){
      product.emplace_back(weights.at(index));
    }
  }
  else {
    fillPDF(product, weights);
    edm::LogWarning("TreeMaker") << "Unexpected format found for PS weights; saving " << weights.size() << " elements";
  }
}

void PDFWeightProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  auto pdfweights = std::make_unique<std::vector<float>>();
  auto scaleweights = std::make_unique<std::vector<float>>();
  auto psweights = std::make_unique<std::vector<float>>();

  edm::Handle<GenWeightProduct> lheWeightHandle;
  iEvent.getByToken(lheWeightToken_, lheWeightHandle);
  if(lheWeightHandle.isValid()){
    const auto& lheWeights = lheWeightHandle->weights();
    const auto& lheWeightInfos = *runCache(iEvent.getRun().index());

    if(debug_) {
      std::stringstream ss;
      ss << "LHE weight vector entries: ";
      for(const auto& weightvec : lheWeights){
        ss << weightvec.size() << ", ";
      }
      ss << "\nLHE weight indices: "
         << (storePDFs_ and lheWeightInfos[0].group ? lheWeightInfos[0].index : -1) << ", "
         << (storeScales_ and lheWeightInfos[1].group ? lheWeightInfos[1].index : -1);
      edm::LogInfo("TreeMaker") << ss.str();
    }

    //fill pdf weights
    if(storePDFs_ and lheWeightInfos[0].group)
      fillPDF(*pdfweights, lheWeights.at(lheWeightInfos[0].index));

    //fill scale weights
    if(storeScales_ and lheWeightInfos[1].group)
      fillScale(*scaleweights, lheWeights.at(lheWeightInfos[1].index), *static_cast<const gen::ScaleWeightGroupInfo*>(lheWeightInfos[1].group));
  }

  edm::Handle<GenWeightProduct> genWeightHandle;
  iEvent.getByToken(genWeightToken_, genWeightHandle);
  if(genWeightHandle.isValid()){
    const auto& genWeights = genWeightHandle->weights();
    const auto& genWeightInfos = *luminosityBlockCache(iEvent.getLuminosityBlock().index());

    if(debug_) {
      std::stringstream ss;
      ss << "Gen weight vector entries: ";
      for(const auto& weightvec : genWeights){
        ss << weightvec.size() << ", ";
      }
      ss << "\nGen weight indices: "
         << (storeScales_ and genWeightInfos[1].group ? genWeightInfos[1].index : -1) << ", "
         << (storePSs_ and genWeightInfos[2].group ? genWeightInfos[2].index : -1);
      edm::LogInfo("TreeMaker") << ss.str();
    }

    //fill scale weights if not already found in lhe
    if(storeScales_ and genWeightInfos[1].group and scaleweights->empty())
      fillScale(*scaleweights, genWeights.at(genWeightInfos[1].index), *static_cast<const gen::ScaleWeightGroupInfo*>(genWeightInfos[1].group));

    //fill parton shower weights
    if(storePSs_ and genWeightInfos[2].group)
      fillPS(*psweights, genWeights.at(genWeightInfos[2].index), *static_cast<const gen::PartonShowerWeightGroupInfo*>(genWeightInfos[2].group));
  }

  iEvent.put(std::move(scaleweights),"ScaleWeights");
  iEvent.put(std::move(pdfweights),"PDFweights");
  iEvent.put(std::move(psweights),"PSweights");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PDFWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PDFWeightProducer);
