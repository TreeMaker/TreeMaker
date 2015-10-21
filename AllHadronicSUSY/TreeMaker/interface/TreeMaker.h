#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
// additional headers
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "TString.h"
#include "TTree.h"
#include <TFile.h>
#include <vector>
#include "TLorentzVector.h"
#include "Math/GenVector/LorentzVector.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
//
// class declaration
//

class TreeMaker : public edm::EDProducer {
public:
  explicit TreeMaker(const edm::ParameterSet&);
  ~TreeMaker();
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
private:
  virtual void beginJob() override;
  virtual void produce(edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  // ----------member data ---------------------------
  const unsigned int nMaxCandidates_;
  void setBranchVariablesToDefault();
  std::pair <std::string,std::string> SeparateString(std::string InputStr, std::string Separater);
  TString FinalizeName(std::string nameInTree);
  TString treeName_;
  TTree* tree_;	
  bool debug_;
  std::vector<std::string> nameCache_;
  // generell event information
  UInt_t runNum_;      
  UInt_t lumiBlockNum_;
  UInt_t evtNum_;
  std::vector<edm::InputTag> VarsTLorentzVectorTags_;
  std::vector<std::string> VarsTLorentzVectorNames_;
  std::vector<TLorentzVector> VarsTLorentzVector_;
  
  std::vector<edm::InputTag> VarsStringTags_;
  std::vector<std::string> VarsStringNames_;
  std::vector<std::string> VarsString_;
  
  std::vector<edm::InputTag> VarsDoubleTags_;
  std::vector<std::string> VarsDoubleNames_;
  std::vector<Float_t> VarsDouble_;
  // any int precision varialbes
  std::vector<edm::InputTag> VarsIntTags_;
  std::vector<std::string> VarsIntNames_;
  std::vector<Int_t> VarsInt_;
  // any bool precision varialbes
  std::vector<edm::InputTag> VarsBoolTags_;
  std::vector<std::string> VarsBoolNames_;
  std::vector<UChar_t> VarsBool_;
  
  std::vector<edm::InputTag> VectorDoubleTags_;
  std::vector<std::string> VectorDoubleNames_;
  std::vector<std::vector<double> > VectorDoubleVector_;
  
  std::vector<edm::InputTag> VectorIntTags_;
  std::vector<std::string> VectorIntNames_;
  std::vector<std::vector<int> > VectorIntVector_;
  
  std::vector<edm::InputTag> VectorBoolTags_;
  std::vector<std::string> VectorBoolNames_;
  std::vector<std::vector<unsigned int> > VectorBoolVector_;
  
  std::vector<edm::InputTag> VectorStringTags_;
  std::vector<std::string> VectorStringNames_;
  std::vector<std::vector<std::string> > VectorStringVector_;
  
  std::vector<edm::InputTag> VectorTLorentzVectorTags_;
  std::vector<std::string> VectorTLorentzVectorNames_;
  std::vector<std::vector<TLorentzVector> > VectorTLorentzVector_;
  // any reco candidate plus addiation doubles
  std::vector<edm::InputTag> varsRecoCandTags_;
  std::vector<std::string> varsRecoCandNames_;
  std::vector<UShort_t> RecoCandN_;
  std::vector<Float_t*> RecoCandPt_;
  std::vector<Float_t*> RecoCandEta_;
  std::vector<Float_t*> RecoCandPhi_;
  std::vector<Float_t*> RecoCandE_;
  std::vector<TLorentzVector*> RecoCandLorentzVector_;
  std::vector<UShort_t> RecoCandAdditionalBoolVariablesN_,RecoCandAdditionalIntVariablesN_,RecoCandAdditionalFloatVariablesN_;
  std::vector< std::vector<edm::InputTag> > RecoCandAdditionalBoolVariablesTags_;
  std::vector< std::vector<UChar_t*> > RecoCandAdditionalBoolVariables_;
  std::vector< std::vector<edm::InputTag> > RecoCandAdditionalIntVariablesTags_;
  std::vector< std::vector<Int_t*> > RecoCandAdditionalIntVariables_;
  std::vector< std::vector<edm::InputTag> > RecoCandAdditionalFloatVariablesTags_;
  std::vector< std::vector<Float_t*> > RecoCandAdditionalFloatVariables_;
};
