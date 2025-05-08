// system include files
#include <map>
#include <memory>
#include <vector>
#include <cmath>
#include <utility>
#include <unordered_set>
#include <tuple>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TreeMaker/Utils/interface/lester_mt2_bisect.h"
#include "TreeMaker/Utils/interface/matchAB.h"
#include "TreeMaker/Utils/interface/NjettinessHelper.h"
// new includes
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
typedef math::PtEtaPhiELorentzVector CLorentzVector;

typedef std::unordered_set<unsigned> PidSet;
typedef const reco::Candidate* CandPtr;
typedef std::unordered_set<CandPtr> CandSet;

//some daughters (primarily GenParticles) may be dropped from miniAOD
//trying to access these daughers directly with the daughter() accessor will cause an exception:
//InvalidID get by product ID: invalid ProductID supplied
//to work around this, we check the corresponding edm::Ptr to see if its ProductID is valid
template <typename T>
CandPtr daughter_noexcept(const T& mother, unsigned i) {
  auto tmp = mother.daughterPtr(i);
  return tmp.id().isValid() ? &*tmp : nullptr;
}

class HiddenSectorProducer : public edm::global::EDProducer<edm::StreamCache<NjettinessHelper>> {
  public:
    explicit HiddenSectorProducer(const edm::ParameterSet&);
  private:
    void produce(edm::StreamID iID, edm::Event&, const edm::EventSetup&) const override;
    //helper
    double TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const;
    template <class P>
    void addDaughters(const P* i_part, std::vector<CandPtr>& listOfDaughters) const;
    void fillSet(PidSet& IDset, const std::string& name, const edm::ParameterSet& iConfig);
    bool isParticle(const PidSet& darkList, CandPtr part) const;
    bool isParticle(int partPid, CandPtr part) const;
    bool isParticle(const PidSet& darkList, int pid) const;
    bool isParticle(const CandSet& darkList, CandPtr part) const;
    bool isAncestor(const PidSet& darkList, CandPtr part) const;
    bool isAncestor(int ancestorPid, CandPtr part) const;
    CandPtr getAncestor(const PidSet& darkList, CandPtr part) const;
    void medDecay(CandPtr part, CandSet& firstQdM, CandSet& firstQsM, CandPtr& firstQdM1, CandPtr& firstQdM2, CandPtr& firstQsM1, CandPtr& firstQsM2, bool& secondDM, bool& secondSM) const;
    void firstDark(CandPtr part, CandSet& firstMd, CandSet& firstQd, CandSet& firstGd, CandSet& firstQdM, CandSet& firstQsM, CandPtr& firstQdM1, CandPtr& firstQdM2, CandPtr& firstQsM1, CandPtr& firstQsM2, bool& secondDM, bool& secondSM) const;
    int checkLast(const reco::GenJet& jet, const CandSet& stableDs, int value, double& frac) const;
    int checkFirst(const reco::GenJet& jet, const CandSet& firstP, int value) const;
    double calculateMT2(const edm::Handle<edm::View<reco::GenMET>>& h_genmets, const reco::GenJet& dQM1J, const reco::GenJet& SMM1J, const reco::GenJet& dQM2J, const reco::GenJet& SMM2J) const;
    void matchJetsCands(edm::Handle<edm::View<pat::Jet>>& h_jets, edm::Handle<edm::View<reco::Candidate>>& h_cands, std::vector<std::vector<CLorentzVector> >& cands_out, std::vector<std::vector<int> >& pdgids_out) const;
    std::vector<std::vector<int> > matchParticles(std::vector<std::vector<CLorentzVector> >& genSubjetConstituents, std::vector<std::vector<int> >& genSubjetPdgid, std::vector<CLorentzVector>& jetCands, std::vector<int>& jetCandsPdgid, std::vector<bool>& recoMatched, std::vector<int>& matchStageReco) const;
    bool signal_;
    edm::InputTag JetTag_, MetTag_, GenMetTag_, GenTag_, GenJetTag_, GenIndexTag_, CandTag_;
    edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
    edm::EDGetTokenT<edm::View<pat::MET>> MetTok_;
    edm::EDGetTokenT<edm::View<reco::GenMET>> GenMetTok_;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> GenTok_;
    edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok_;
    edm::EDGetTokenT<edm::View<reco::Candidate>> CandTok_;
    edm::EDGetTokenT<std::vector<int>> GenIndexTok_;
    double coneSize_;
    edm::ParameterSet njhConfig; 
    PidSet DarkSMediatorIDs_, DarkTMediatorIDs_, DarkQuarkIDs_, DarkHadronIDs_, DarkGluonIDs_, DarkStableIDs_, DarkFirstIDs_, SMQuarkIDs_;
    std::unique_ptr<NjettinessHelper> beginStream(edm::StreamID) const {
      return std::unique_ptr<NjettinessHelper>(new NjettinessHelper(njhConfig));
    }

};

void HiddenSectorProducer::fillSet(PidSet& IDset, const std::string& name, const edm::ParameterSet& iConfig)
{
  const auto& ids = iConfig.getParameter<std::vector<unsigned>>(name);
  IDset.insert(ids.begin(),ids.end());
}

bool HiddenSectorProducer::isParticle(const PidSet& darkList, CandPtr part) const {
  return isParticle(darkList, part->pdgId());
}

bool HiddenSectorProducer::isParticle(int partPid, CandPtr part) const {
  return (partPid == part->pdgId());
}

bool HiddenSectorProducer::isParticle(const PidSet& darkList, int pid) const {
  return darkList.find(std::abs(pid)) != darkList.end();
}

bool HiddenSectorProducer::isParticle(const CandSet& darkList, CandPtr part) const {
  return darkList.find(part) != darkList.end();
}

bool HiddenSectorProducer::isAncestor(const PidSet& darkList, CandPtr part) const {
  if(isParticle(darkList, part)) return true;
  for(size_t i=0;i< part->numberOfMothers();i++)
  {
    if(isAncestor(darkList,part->mother(i))) return true;
  }
  return false;
}

bool HiddenSectorProducer::isAncestor(int ancestorPid, CandPtr part) const {
  if(isParticle(ancestorPid, part)) return true;
  for(size_t i=0;i< part->numberOfMothers();i++)
  {
    if(isAncestor(ancestorPid,part->mother(i))) return true;
  }
  return false;
}


CandPtr HiddenSectorProducer::getAncestor(const PidSet& darkList, CandPtr part) const {
  if(part==nullptr or isParticle(darkList, part)) return part;
  for(size_t i=0;i< part->numberOfMothers();i++)
  {
    auto tmp = getAncestor(darkList,part->mother(i));
    if (tmp!=nullptr) return tmp;
  }
  return nullptr;
}

// this function intends to collect immediate non-mediator daughters of the mediators. These mediator daughters can then be used to reconstruct the mass of the mediator.
void HiddenSectorProducer::medDecay(CandPtr part, CandSet& firstQdM, CandSet& firstQsM, CandPtr& firstQdM1, CandPtr& firstQdM2, CandPtr& firstQsM1, CandPtr& firstQsM2, bool& secondDM, bool& secondSM) const {
  for(unsigned i = 0; i < part->numberOfDaughters(); i++){
    CandPtr dau = part->daughter(i);
    // if the first dark mediator's daughter is still a dark mediator, then check the daughters of this daughter dark mediator until we get daughters that are not dark mediator
    if(isParticle(DarkTMediatorIDs_,dau)) medDecay(dau,firstQdM,firstQsM,firstQdM1,firstQdM2,firstQsM1,firstQsM2,secondDM,secondSM);
    else{
      // a mediator decays into a dark and an SM quark. Here we are collecting the dark quarks from the mediators while labeling them firstQdM1 and firstQdM2 depending on which mediator the quarks came from.
      if(isParticle(DarkQuarkIDs_,dau)){
        firstQdM.insert(dau);
        // this condition makes sure that the firstQdM1 (firstQdM2) and firstQsM1 (firstQsM2) came from the same mediator.
        // The labels 1 and 2 have no significance other than making sure that we get the correct pairings of dark and SM quarks from the mediators.
        if(secondDM == false){
          firstQdM1 = dau;
          secondDM = true;
        }
        else firstQdM2 = dau;
      }
      // Here we are collecting the SM quarks from the mediators which assigning them to firstQsM1 and firstQsM2 depending on which mediator the quarks came from.
      else if(isParticle(SMQuarkIDs_,dau)){
        firstQsM.insert(dau);
        if(secondSM == false){
          firstQsM1 = dau;
          secondSM = true;
        }
        else firstQsM2 = dau;
      }
    }
  }
}

void HiddenSectorProducer::firstDark(CandPtr part, CandSet& firstMd, CandSet& firstQd, CandSet& firstGd, CandSet& firstQdM, CandSet& firstQsM, CandPtr& firstQdM1, CandPtr& firstQdM2, CandPtr& firstQsM1, CandPtr& firstQsM2, bool& secondDM, bool& secondSM) const {
  if(isParticle(DarkFirstIDs_,part)){
    CandPtr parent = part->mother(0);
    if(isParticle(DarkFirstIDs_,parent)) firstDark(parent, firstMd, firstQd, firstGd, firstQdM, firstQsM, firstQdM1, firstQdM2, firstQsM1, firstQsM2, secondDM, secondSM);
    else{
      // SM parent of first dark particles
      // looping through the daughters of this SM parent
      for(unsigned i = 0; i < part->numberOfDaughters(); i++){
        CandPtr dau = part->daughter(i);
        if (isParticle(DarkTMediatorIDs_,dau)){
          if(firstMd.find(dau)==firstMd.end()){
            firstMd.insert(dau);
            // once a mediator daughter is found, we look for the descendants of the mediator
            medDecay(dau,firstQdM,firstQsM,firstQdM1,firstQdM2,firstQsM1,firstQsM2,secondDM,secondSM);
          }
        }
        else if (isParticle(DarkQuarkIDs_,dau)) firstQd.insert(dau);
        else if (isParticle(DarkGluonIDs_,dau)) firstGd.insert(dau);
      }
    }
  }
}

int HiddenSectorProducer::checkLast(const reco::GenJet& jet, const CandSet& stableDs, int value, double& frac) const {
  //compare jet constituents to set of last particles
  //also compute dark pt fraction in same loop
  bool match = false;
  LorentzVector p4;
  LorentzVector totPt = jet.p4();
  for(unsigned i = 0; i < jet.numberOfDaughters(); ++i){
    CandPtr dau = daughter_noexcept(jet,i);
    if(!dau) continue;
    if(isAncestor(DarkHadronIDs_,dau)){
        match = true;
        p4 += dau->p4();
    }
  }
  for(const auto& part : stableDs){
     if(reco::deltaR(jet, *part) < coneSize_)
     {
       p4 += part->p4();
       totPt += part->p4();
     }
  }
  frac = p4.pt()/totPt.pt();
  return match ? value : 0;
}

int HiddenSectorProducer::checkFirst(const reco::GenJet& jet, const CandSet& firstP, int value) const {
  //compare first particles using jet cone (can't compare constituents' parents because all dark hadrons descend from all first dark particles, strong force problems)
  for(const auto& part : firstP){
    if(reco::deltaR(jet, *part) < coneSize_) return value;
  }
  return 0;
}

double HiddenSectorProducer::calculateMT2(const edm::Handle<edm::View<reco::GenMET>>& h_genmets, const reco::GenJet& dQM1J, const reco::GenJet& SMM1J, const reco::GenJet& dQM2J, const reco::GenJet& SMM2J) const {
  const auto& i_met = h_genmets->front();
  double METx = i_met.px();
  double METy = i_met.py();
  LorentzVector FJet0 = dQM1J.p4() + SMM1J.p4();
  LorentzVector FJet1 = dQM2J.p4() + SMM2J.p4();
  return asymm_mt2_lester_bisect::get_mT2(
    FJet0.M(), FJet0.Px(), FJet0.Py(),
    FJet1.M(), FJet1.Px(), FJet1.Py(),
    METx, METy, 0.0, 0.0, 0
  );
}

void HiddenSectorProducer::matchJetsCands(edm::Handle<edm::View<pat::Jet>>& h_jets, edm::Handle<edm::View<reco::Candidate>>& h_cands, std::vector<std::vector<CLorentzVector> >& cands_out, std::vector<std::vector<int> >& pdgids_out) const {

  //loop over PF candidate collection once: check every jet in every jet collection
  //only PF candidates found in a jet collection will be kept
  for(unsigned c = 0; c < h_cands->size(); ++c){
    const auto& candPtr = h_cands->ptrs()[c];
    //if this cand is kept, it will be appended to cands_out

    for(unsigned j = 0; j < h_jets->size(); ++j){
      if (cands_out.size() <= j) cands_out.emplace_back();
      if (pdgids_out.size() <= j) pdgids_out.emplace_back();
      const auto& jet = h_jets->at(j);
      const auto& daughterPtrs = jet.daughterPtrVector();
      if(cands_out[j].size()==daughterPtrs.size()) continue;
      bool keep = false; 
      for(const auto& candJetDau : jet.daughterPtrVector()){ 
	keep = candJetDau.key() == candPtr.key();
	if (keep) { 
	  cands_out[j].emplace_back(candPtr->pt(),candPtr->eta(),candPtr->phi(),candPtr->energy());
	  pdgids_out[j].emplace_back(candPtr->pdgId());
	  //in a given jet collection, a candidate can only be in one jet
	  break;
	}
      }
      // if we are here either we broke out of candJetDau loop because we matched that jet dau, and we should skip the rest of the jets by breaking out of jet loop and going to next h_cand, or we went through all jet daughters and keep is false and we should go to next jet and see if we match there. Basically if we break out of daughters, also break out of jets loop 
      if (keep) break;
    }
  }

  return; 
}


std::vector<std::vector<int> > HiddenSectorProducer::matchParticles(std::vector<std::vector<CLorentzVector> >& genSubjetConstituents, std::vector<std::vector<int> >& genSubjetPdgid, std::vector<CLorentzVector>& jetCands, std::vector<int>& jetCandsPdgid, std::vector<bool>& recoMatched, std::vector<int>& matchStageReco) const {

  std::vector<std::vector<int>> indices = genSubjetPdgid;
  for(unsigned i = 0; i < indices.size(); i++){
    for(unsigned j = 0; j < indices[i].size(); j++) indices[i][j] = -1;
  }

  std::vector<bool> tmpRecoMatched(jetCands.size(), false);


  struct matchInfo{
    std::vector<int> genIndexTop;
    std::vector<int> genIndex;
    std::vector<CLorentzVector> genParts;
    std::vector<int> recoIndex;
    std::vector<CLorentzVector> recoParts;    
    std::vector<int> matchedIndex;
  };

  matchInfo tmpMatch, leftovers; 

  // Separate particles into separate lists by pdgid and use matchAB for deltaR matching within pdgids
  // preserve original list ordering somewhere
  std::vector<int> pdgids = {13, -13, 11, -11, 22};
  //one struct for each pdgid
  std::vector<matchInfo> toMatch(pdgids.size(), tmpMatch);
  // one for hadrons 
  toMatch.push_back(tmpMatch); 

  // get list of gen particles for each pdgid 
  for(unsigned i = 0; i < genSubjetConstituents.size(); i++){
    for(unsigned j = 0; j < genSubjetConstituents[i].size(); j++){
      auto it = std::find(pdgids.begin(), pdgids.end(), genSubjetPdgid[i][j]);
      if ( it != pdgids.end() ) {
	int index = it - pdgids.begin(); 
	toMatch[index].genParts.push_back(genSubjetConstituents[i][j]);
	toMatch[index].genIndexTop.push_back(i);
	toMatch[index].genIndex.push_back(j);
      }
      else if (std::find(pdgids.begin(), pdgids.end(), genSubjetPdgid[i][j]) == pdgids.end() ) { 
	toMatch[pdgids.size()].genParts.push_back(genSubjetConstituents[i][j]);
	toMatch[pdgids.size()].genIndexTop.push_back(i);
	toMatch[pdgids.size()].genIndex.push_back(j);
      }
    }
  }

  // get list of reco particles for each pdgid/hadrons
  for(unsigned r = 0; r < jetCands.size(); r++){
    auto it = std::find(pdgids.begin(), pdgids.end(), jetCandsPdgid[r]);
    if(it != pdgids.end() ) {
      int index = it - pdgids.begin();
      toMatch[index].recoParts.push_back(jetCands[r]);
      toMatch[index].recoIndex.push_back(r);
    }
    else if(std::find(pdgids.begin(), pdgids.end(), jetCandsPdgid[r]) == pdgids.end() ) {
      toMatch[pdgids.size()].recoParts.push_back(jetCands[r]);
      toMatch[pdgids.size()].recoIndex.push_back(r);
    }

  }

  for( auto& m: toMatch ) {  
    m.matchedIndex = utils::matchAB(m.genParts, m.recoParts);
    //Save matched indices to final array
    for(unsigned i = 0; i < m.matchedIndex.size(); i++){
      if (m.matchedIndex[i] != -1) {
	indices[m.genIndexTop[i]][m.genIndex[i]] = m.recoIndex[m.matchedIndex[i]];
	tmpRecoMatched[m.recoIndex[m.matchedIndex[i]]] = true;
	matchStageReco[m.recoIndex[m.matchedIndex[i]]] = 0;
      }
    }
  }


  // Need pdgid based matching to be already done, and then
  // do this again for anything that's left... (aka the leftovers) 
  for(unsigned i = 0; i < genSubjetConstituents.size(); i++){
    for(unsigned j = 0; j < genSubjetConstituents[i].size(); j++){
      if ( indices[i][j] == -1 ){
  	leftovers.genParts.push_back(genSubjetConstituents[i][j]);
  	leftovers.genIndexTop.push_back(i);
  	leftovers.genIndex.push_back(j);
      }
    }
  }

  for(unsigned r = 0; r < jetCands.size(); r++){
    if( tmpRecoMatched[r] == false ) {
      leftovers.recoParts.push_back(jetCands[r]);
      leftovers.recoIndex.push_back(r);
    }
  }

  leftovers.matchedIndex = utils::matchAB(leftovers.genParts, leftovers.recoParts);

  //Save matched indices to final array
  for(unsigned m = 0; m < leftovers.matchedIndex.size(); m++){
    if (leftovers.matchedIndex[m] != -1) {
      indices[leftovers.genIndexTop[m]][leftovers.genIndex[m]] = leftovers.recoIndex[leftovers.matchedIndex[m]];
      tmpRecoMatched[leftovers.recoIndex[leftovers.matchedIndex[m]]] = true;
      matchStageReco[leftovers.recoIndex[leftovers.matchedIndex[m]]] = 2;
    }
  }
  recoMatched = tmpRecoMatched;

  return indices;
}

HiddenSectorProducer::HiddenSectorProducer(const edm::ParameterSet& iConfig) :
  signal_(iConfig.getParameter<bool>("signal")),
  JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
  MetTag_(iConfig.getParameter<edm::InputTag>("MetTag")),
  GenMetTag_(iConfig.getParameter<edm::InputTag>("GenMetTag")),
  GenTag_(iConfig.getParameter<edm::InputTag>("GenTag")),
  GenJetTag_(iConfig.getParameter<edm::InputTag>("GenJetTag")),
  GenIndexTag_(iConfig.getParameter<edm::InputTag>("genIndexTag")),
  CandTag_(iConfig.getParameter<edm::InputTag>("CandTag")),
  JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
  MetTok_(consumes<edm::View<pat::MET>>(MetTag_)),
  GenMetTok_(consumes<edm::View<reco::GenMET>>(GenMetTag_)),
  GenTok_(consumes<edm::View<reco::GenParticle>>(GenTag_)),
  GenJetTok_(consumes<edm::View<reco::GenJet>>(GenJetTag_)),
  CandTok_(consumes<edm::View<reco::Candidate>>(CandTag_)),
  GenIndexTok_(consumes<std::vector<int>>(GenIndexTag_)),
  coneSize_(iConfig.getParameter<double>("coneSize")),
  njhConfig(iConfig.getParameter<edm::ParameterSet>("nsubjettiness"))
{
  fillSet(DarkSMediatorIDs_,"DarkSMediatorIDs",iConfig);
  fillSet(DarkTMediatorIDs_,"DarkTMediatorIDs",iConfig);
  fillSet(DarkQuarkIDs_,"DarkQuarkIDs",iConfig);
  fillSet(DarkHadronIDs_,"DarkHadronIDs",iConfig);
  fillSet(DarkGluonIDs_,"DarkGluonIDs",iConfig);
  fillSet(DarkStableIDs_,"DarkStableIDs",iConfig);
  fillSet(SMQuarkIDs_,"SMQuarkIDs",iConfig);
  //combined list of possible first particles
  DarkFirstIDs_.insert(DarkTMediatorIDs_.begin(),DarkTMediatorIDs_.end());
  DarkFirstIDs_.insert(DarkQuarkIDs_.begin(),DarkQuarkIDs_.end());
  DarkFirstIDs_.insert(DarkGluonIDs_.begin(),DarkGluonIDs_.end());
  asymm_mt2_lester_bisect::disableCopyrightMessage();

  produces<double>("MJJ");
  produces<double>("Mmc");
  produces<double>("MT");
  produces<double>("GenMT2");
  produces<double>("DeltaPhi1");
  produces<double>("DeltaPhi2");
  produces<double>("DeltaPhiMin");
  if(signal_){
    produces<std::vector<bool>>("isHV");
    //first two branches for GenJetsAK8, last is for JetsAK8 (matching index)
    produces<std::vector<int>>("hvCategory");
    produces<std::vector<double>>("darkPtFrac");
    produces<std::vector<int>>("MT2JetsID");
    produces<std::vector<int>>("GenJetsNConstituents");
    produces<std::vector<int>>("GenJetsNConstituentsDarkHadrons");
    produces<std::vector<int>>("GenJetsNConstituentsUnmatched");
    produces<std::vector<int>>("JetsNConstituents");
    produces<std::vector<int>>("JetsNConstituentsUnmatched");

    produces<std::vector<std::vector<CLorentzVector>>>("GenJetsDarkHadrons");
    produces<std::vector<std::vector<CLorentzVector>>>("GenJetsDarkHadronJets");
    produces<std::vector<std::vector<CLorentzVector>>>("JetsDarkHadronJets");

    produces<std::vector<std::vector<int>>>("GenJetsDarkHadronJetsMultiplicity");
    produces<std::vector<std::vector<int>>>("JetsNConstituentsUnmatchedPdgid");
    produces<std::vector<std::vector<int>>>("JetsNConstituentsIsAssigned");

    produces<std::vector<std::vector<int>>>("JetsConstituentPdgid");
    produces<std::vector<std::vector<int>>>("GenJetsConstituentPdgid");
    produces<std::vector<std::vector<int>>>("JetsConstituentMatchStageReco");
    produces<std::vector<std::vector<int>>>("GenJetsConstituentMatchIndex");

    produces<std::vector<std::vector<double>>>("GenJetsDarkHadronJetsTau1");
    produces<std::vector<std::vector<double>>>("GenJetsDarkHadronJetsTau2");
    produces<std::vector<std::vector<double>>>("GenJetsDarkHadronJetsTau3");

    produces<std::vector<std::vector<std::vector<CLorentzVector>>>>("GenJetsDarkHadronJetsConstituents");
    produces<std::vector<std::vector<std::vector<CLorentzVector>>>>("JetsDarkHadronJetsConstituents");
    produces<std::vector<std::vector<std::vector<CLorentzVector>>>>("JetsDarkHadronJetsConstituentsGenMatchOnly");
    produces<std::vector<std::vector<std::vector<CLorentzVector>>>>("JetsDarkHadronJetsConstituentsNextDH");
  }
}

double HiddenSectorProducer::TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const {
  double E1 = std::sqrt(std::pow(px1,2)+std::pow(py1,2)+std::pow(m1,2));
  double E2 = std::sqrt(std::pow(px2,2)+std::pow(py2,2)+std::pow(m2,2));
  double MTsq = std::pow(E1+E2,2)-std::pow(px1+px2,2)-std::pow(py1+py2,2);
  return std::sqrt(std::max(MTsq,0.0));
}

template <class P>
void HiddenSectorProducer::addDaughters(const P* i_part, std::vector<CandPtr>& listOfDaughters) const {
  for (unsigned idau=0; idau < i_part->numberOfDaughters(); ++idau) { // add all daughters of HVquark to list
    CandPtr dau = i_part->daughter(idau);
    if(isParticle(DarkQuarkIDs_,dau)) addDaughters(dau,listOfDaughters); // recurse down to HV-quark copy's daughters
    else listOfDaughters.push_back(dau);
  }
}

void HiddenSectorProducer::produce(edm::StreamID iID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  //get the collections
  edm::Handle<edm::View<pat::Jet>> h_jets;
  iEvent.getByToken(JetTok_, h_jets);

  edm::Handle<edm::View<pat::MET>> h_mets;
  iEvent.getByToken(MetTok_, h_mets);

  edm::Handle<edm::View<reco::GenMET>> h_genmets;
  iEvent.getByToken(GenMetTok_, h_genmets);

  edm::Handle<edm::View<reco::GenParticle>> h_parts;
  iEvent.getByToken(GenTok_, h_parts);

  edm::Handle<edm::View<reco::GenJet>> h_genjets;
  iEvent.getByToken(GenJetTok_, h_genjets);

  edm::Handle<edm::View<reco::Candidate>> h_cands;
  iEvent.getByToken(CandTok_, h_cands);

  edm::Handle<std::vector<int>> genIndex;
  iEvent.getByToken(GenIndexTok_, genIndex);


  auto jet_isHV_vec = std::make_unique<std::vector<bool>>();
  auto hvCategory = std::make_unique<std::vector<int>>();
  auto darkPtFrac = std::make_unique<std::vector<double>>();
  auto MT2JetsID = std::make_unique<std::vector<int>>();
  auto GenJets_nLundSubjets = std::make_unique<std::vector<int>>();
  auto GenJets_nConstituents = std::make_unique<std::vector<int>>();
  auto GenJets_nConstituentsDarkHadrons = std::make_unique<std::vector<int>>();
  auto GenJets_nConstituents_unmatched = std::make_unique<std::vector<int>>();
  auto Jets_nConstituents = std::make_unique<std::vector<int>>();
  auto Jets_nConstituents_unmatched = std::make_unique<std::vector<int>>();

  auto GenJets_darkHadrons = std::make_unique<std::vector<std::vector<CLorentzVector>>>();
  auto GenJets_darkHadronJets = std::make_unique<std::vector<std::vector<CLorentzVector>>>();
  auto Jets_darkHadronJets = std::make_unique<std::vector<std::vector<CLorentzVector>>>();

  auto GenJets_darkHadronJets_multiplicity = std::make_unique<std::vector<std::vector<int>>>();
  auto Jets_nConstituents_unmatched_pdgid = std::make_unique<std::vector<std::vector<int>>>();
  auto Jets_nConstituents_isAssigned = std::make_unique<std::vector<std::vector<int>>>();

  auto Jets_constituents_pdgid = std::make_unique<std::vector<std::vector<int>>>();
  auto GenJets_constituents_pdgid = std::make_unique<std::vector<std::vector<int>>>();
  auto Jets_constituents_matchStageReco = std::make_unique<std::vector<std::vector<int>>>();
  auto GenJets_constituents_matchIndex = std::make_unique<std::vector<std::vector<int>>>();

  auto GenJets_darkHadronJets_tau1 = std::make_unique<std::vector<std::vector<double>>>();
  auto GenJets_darkHadronJets_tau2 = std::make_unique<std::vector<std::vector<double>>>();
  auto GenJets_darkHadronJets_tau3 = std::make_unique<std::vector<std::vector<double>>>();
  
  auto GenJets_darkHadronJets_constituents_2d = std::make_unique<std::vector<std::vector<CLorentzVector>>>();
  auto Jets_darkHadronJets_constituents_2d = std::make_unique<std::vector<std::vector<CLorentzVector>>>();

  auto GenJets_darkHadronJets_constituents = std::make_unique<std::vector<std::vector<std::vector<CLorentzVector>>>>();
  auto GenJets_darkHadronJets_constituentsPdgid = std::make_unique<std::vector<std::vector<std::vector<int>>>>();
  auto Jets_darkHadronJets_constituentsMatchStage = std::make_unique<std::vector<std::vector<std::vector<int>>>>();
  auto Jets_darkHadronJets_constituentsPdgid = std::make_unique<std::vector<std::vector<std::vector<int>>>>();
  auto Jets_darkHadronJets_constituents = std::make_unique<std::vector<std::vector<std::vector<CLorentzVector>>>>();
  auto Jets_darkHadronJets_constituents_genMatchOnly = std::make_unique<std::vector<std::vector<std::vector<CLorentzVector>>>>();
  auto Jets_darkHadronJets_constituents_nextDH = std::make_unique<std::vector<std::vector<std::vector<CLorentzVector>>>>();


  LorentzVector vpartsSum;
  if(h_parts.isValid()){
    for(const auto& i_part : *(h_parts.product())){
      if(isParticle(DarkStableIDs_,i_part.pdgId())){
        vpartsSum += i_part.p4();
      }
    }
  }

  double MJJ = 0, Mmc = 0, MT = 0, GenMT2 = 0, DeltaPhi1 = 10, DeltaPhi2 = 10, DeltaPhiMin = 10;
  //only fill these parts if there are >=2 jets
  if(h_jets->size()>=2){
    //delta phi
    DeltaPhi1 = std::abs(reco::deltaPhi(h_jets->at(0).phi(),h_mets->at(0).phi()));
    DeltaPhi2 = std::abs(reco::deltaPhi(h_jets->at(1).phi(),h_mets->at(0).phi()));
    DeltaPhiMin = std::min(DeltaPhi1,DeltaPhi2);

    //masses
    LorentzVector vjj = h_jets->at(0).p4()+h_jets->at(1).p4();
    MJJ = vjj.M();

    //include all jets in MC mass
    LorentzVector vmc = vjj + vpartsSum;
    Mmc = vmc.M();

    //MET is massless, but jets aren't
    double MET = h_mets->at(0).pt(), METPhi = h_mets->at(0).phi();
    MT = TransverseMass(vjj.Px(),vjj.Py(),vjj.M(),MET*std::cos(METPhi),MET*std::sin(METPhi),0);
  }

  //ISRJetProducer method, find jets with hard process particles at their 'core' and other jets are ISR
  if(signal_ and h_parts.isValid()){
    for(const auto& i_jet : *(h_jets.product())){ // loop over AK8 jets
      bool matched = false; // matched == true means that this jet has a hard process (descendant particle of the Z') at its 'core'
      for (const auto& i_part : *(h_parts.product())){ // loop over GenParticles
        if (matched) break; // only need to match one particle to the jet to tag it as FSR
        if(i_part.status()!=23) continue; // only want particles outgoing from the hard process
        if(!isParticle(DarkSMediatorIDs_,i_part.mother())) continue; // only want direct descendants of Z' (kind of redundant)
        //check against daughters in case of hard initial splitting, from ISRJetProducer...
        std::vector<CandPtr> listOfDaughters;
        addDaughters(&i_part,listOfDaughters);
        for (const auto& daughter : listOfDaughters) {
          float dR = deltaR(i_jet, daughter->p4());
          if(dR<0.8){
            matched = true;
            break;
          }
        }
      }
      jet_isHV_vec->push_back(matched);
    }

    //t-channel jet categorization
    //gen particle organization: last daughters of last copies of dark hadrons, first copies of dark quarks/gluons/mediators, first copies of quarks/gluons/SM quarks from mediator
    //naming scheme: dark particles Pd, SM particles Ps; P = D (generic daughters), Q (quarks), G (gluons), M (mediators)
    CandSet stableDs, firstMd, firstQd, firstGd, firstQdM, firstQsM;
    CandPtr firstQdM1, firstQdM2, firstQsM1, firstQsM2;
    bool secondDM = false, secondSM = false;
    
    //loop over gen particles
    for(const auto& i_part : *(h_parts.product())){
      firstDark(&i_part, firstMd, firstQd, firstGd, firstQdM, firstQsM, firstQdM1, firstQdM2, firstQsM1, firstQsM2,secondDM,secondSM);
      if(static_cast<const reco::GenParticle*>(&i_part)->isLastCopy() and isParticle(DarkStableIDs_,&i_part)) stableDs.insert(&i_part);
    }

    //loop over gen jets
    for(const auto& i_jet : *(h_genjets.product())){
      int category = 0;
      double frac = 0;
      category += checkLast(i_jet, stableDs, 1, frac);
      category += checkFirst(i_jet, firstQd, 2);
      category += checkFirst(i_jet, firstGd, 4);
      category += checkFirst(i_jet, firstQdM, 8);
      category += checkFirst(i_jet, firstQsM, 16);
      hvCategory->push_back(category);
      darkPtFrac->push_back(frac);
    }

    std::vector<CandPtr> firsts{firstQdM1,firstQdM2,firstQsM1,firstQsM2};
    std::vector<int> pgenIndex(firsts.size(),-1);
    *MT2JetsID = std::vector<int>(h_genjets->size(),-1);
    bool matchedAll = true;
    if(firstMd.size()==2){
      pgenIndex = utils::matchAB(firsts,*(h_genjets.product()));
      for(unsigned p = 0; p < pgenIndex.size(); ++p){
        if(pgenIndex[p]>-1) MT2JetsID->at(pgenIndex[p]) = p+1;
        else matchedAll = false;
      }
      if(matchedAll) GenMT2 = calculateMT2(h_genmets,h_genjets->at(pgenIndex[0]),h_genjets->at(pgenIndex[2]),h_genjets->at(pgenIndex[1]),h_genjets->at(pgenIndex[3]));
      else GenMT2 = 0.;
    }

    //reassemble each dark hadron within GenJet from final state SM particles
    //sort dark hadrons descending in pt
    auto comp = [](CandPtr a, CandPtr b){ return a->pt() > b->pt(); };
    //loop over genjets
    for(const auto& i_jet : *(h_genjets.product())){

      GenJets_nConstituents->push_back(i_jet.numberOfDaughters());
      
      int nDaus = 0;
      std::map<CandPtr,std::vector<CandPtr>,decltype(comp)> darkHadronMap(comp);
      for(unsigned i = 0; i < i_jet.numberOfDaughters(); ++i){
        CandPtr dau = daughter_noexcept(i_jet,i);
        CandPtr darkHadron = getAncestor(DarkHadronIDs_,dau);
        if (darkHadron!=nullptr){
          darkHadronMap[darkHadron].push_back(dau);
	  nDaus++;
	}
      }

      GenJets_nConstituentsDarkHadrons->push_back(nDaus);

      std::vector<CLorentzVector> tmp_darkHadrons;
      std::vector<CLorentzVector> tmp_darkHadronJets;
      std::vector<std::vector<CLorentzVector> > tmp_darkHadronJets_constituents;
      std::vector<std::vector<int> > tmp_darkHadronJets_ConstituentPdgid;
      //std::vector<std::vector<CLorentzVector> > tmp_darkHadronSubjets_constituents;
      std::vector<int> tmp_darkHadronJets_multiplicity;
      std::vector<double> tmp_darkHadronJets_tau1;
      std::vector<double> tmp_darkHadronJets_tau2;
      std::vector<double> tmp_darkHadronJets_tau3;
      for(const auto& entry : darkHadronMap){
        tmp_darkHadrons.emplace_back(entry.first->pt(),entry.first->eta(),entry.first->phi(),entry.first->energy());
        LorentzVector tmpjet;
	std::vector<CLorentzVector> tmpjetconstituents;
	std::vector<int> tmpjetconstituentspdgid;
        for(const auto& dau : entry.second){
	  tmpjet += dau->p4();
	  tmpjetconstituents.emplace_back(dau->pt(),dau->eta(),dau->phi(),dau->energy());
	  tmpjetconstituentspdgid.emplace_back(dau->pdgId());
        }
        tmp_darkHadronJets.emplace_back(tmpjet.pt(),tmpjet.eta(),tmpjet.phi(),tmpjet.energy());
	tmp_darkHadronJets_constituents.push_back(tmpjetconstituents);
	tmp_darkHadronJets_ConstituentPdgid.push_back(tmpjetconstituentspdgid);
        tmp_darkHadronJets_multiplicity.push_back(entry.second.size());
	tmp_darkHadronJets_tau1.push_back(streamCache(iID)->getTau(1, tmpjetconstituents));
	tmp_darkHadronJets_tau2.push_back(streamCache(iID)->getTau(2, tmpjetconstituents));
	tmp_darkHadronJets_tau3.push_back(streamCache(iID)->getTau(3, tmpjetconstituents));
	
      }


      GenJets_darkHadrons->push_back(tmp_darkHadrons);
      GenJets_darkHadronJets->push_back(tmp_darkHadronJets);
      GenJets_darkHadronJets_constituents->push_back(tmp_darkHadronJets_constituents);
      GenJets_darkHadronJets_constituentsPdgid->push_back(tmp_darkHadronJets_ConstituentPdgid);
      GenJets_darkHadronJets_multiplicity->push_back(tmp_darkHadronJets_multiplicity);
      GenJets_darkHadronJets_tau1->push_back(tmp_darkHadronJets_tau1);
      GenJets_darkHadronJets_tau2->push_back(tmp_darkHadronJets_tau2);
      GenJets_darkHadronJets_tau3->push_back(tmp_darkHadronJets_tau3);
      GenJets_nConstituents_unmatched->emplace_back(-1);
      GenJets_constituents_pdgid->push_back({-1});
      GenJets_constituents_matchIndex->push_back({-1});
    }
  }

  
  //Lund Reweighting Matching 

  //Get Constituents for RecoJet (have genJetConstituents already from each dark hadron in the gen jet in GenJets_darkHadronJets_constituents)
  std::vector<std::vector<CLorentzVector> > jets_cands;
  std::vector<std::vector<int> > cands_pdgids;
  matchJetsCands(h_jets, h_cands, jets_cands, cands_pdgids);

  //Iterate through reco jets and get matching genjets
  int recoJetIndex = 0;
  int nRecoJetCands = 0;
  for(const auto& i_jet : *(h_jets.product())){

    int genJetIndex = genIndex->at(recoJetIndex);
    
    Jets_nConstituents->push_back(jets_cands[recoJetIndex].size());
    //Jets_constituents_pdgid->push_back(cands_pdgids[recoJetIndex]);
 
    if (genJetIndex == -1) {
      std::vector<int> tmp = {-1}; 
      std::vector<CLorentzVector> tmpJet;
      tmpJet.emplace_back(-9999, -9999, -9999, -9999);
      std::vector< std::vector< CLorentzVector> > tmpJetV = {{tmpJet}};
      // If you don't do this coffea gets mad 
      Jets_nConstituents_unmatched->push_back(-1);
      Jets_nConstituents_unmatched_pdgid->push_back(tmp);
      Jets_nConstituents_isAssigned->push_back(tmp);
      Jets_constituents_pdgid->push_back(tmp);
      Jets_darkHadronJets->push_back(tmpJet);
      Jets_darkHadronJets_constituents->push_back(tmpJetV);
      Jets_constituents_matchStageReco->push_back(tmp);
      Jets_darkHadronJets_constituents->push_back(tmpJetV);
      Jets_darkHadronJets_constituentsMatchStage->push_back({tmp});
      Jets_darkHadronJets_constituents_nextDH->push_back(tmpJetV);
      continue;
    }

    const auto i_genJet = h_genjets->at(genJetIndex);


    // Match gen to reco particles using pdgid and deltaR matching
    std::vector<bool> recoMatched;
    std::vector<int> matchStageReco(jets_cands[recoJetIndex].size(), -1);

    std::vector<std::vector<int>> matchedRecoIndex = matchParticles(GenJets_darkHadronJets_constituents->at(genJetIndex), GenJets_darkHadronJets_constituentsPdgid->at(genJetIndex), jets_cands[recoJetIndex], cands_pdgids[recoJetIndex], recoMatched, matchStageReco);
    
    // make list of "dark hadron subjets" in reco particles using the match to gen
    int unmatchedGen = 0;
    std::vector<std::vector<CLorentzVector> > recoSubjets;
    std::vector<CLorentzVector> recoDarkHadronJets;
    std::vector<int> flatIndex;
    std::vector<int> flatGenPdgId;
    std::vector<int> flatRecoPdgId;
    std::vector<int> RecoMatchStage;
    std::vector<std::vector<int>> matchStage;
    std::vector<std::vector<int>> RecoPdgid;

    for(unsigned i = 0; i < matchedRecoIndex.size(); i++){
      std::vector<CLorentzVector> recoSubjetConstituents;
      CLorentzVector tmpJet;
      std::vector<int> tmpMatchStage;
      std::vector<int> tmpRecoPdgid;
      for(unsigned j = 0; j < matchedRecoIndex[i].size(); j++){
	if (matchedRecoIndex[i][j] != -1) {
	  flatIndex.push_back(matchedRecoIndex[i][j]);
	  flatGenPdgId.push_back(GenJets_darkHadronJets_constituentsPdgid->at(genJetIndex)[i][j]);
	  flatRecoPdgId.push_back(cands_pdgids[recoJetIndex][matchedRecoIndex[i][j]]);
	  RecoMatchStage.push_back(matchStageReco[matchedRecoIndex[i][j]]);
	  tmpMatchStage.push_back(matchStageReco[matchedRecoIndex[i][j]]);
	  tmpRecoPdgid.push_back(cands_pdgids[recoJetIndex][matchedRecoIndex[i][j]]);
	  tmpJet += jets_cands[recoJetIndex][matchedRecoIndex[i][j]];
	  recoSubjetConstituents.emplace_back(jets_cands[recoJetIndex][matchedRecoIndex[i][j]]);
	}
	else {
	  unmatchedGen++;
	}
      }
      recoDarkHadronJets.emplace_back(tmpJet);
      recoSubjets.emplace_back(recoSubjetConstituents);
      matchStage.emplace_back(tmpMatchStage);
      RecoPdgid.emplace_back(tmpRecoPdgid);
    }

    GenJets_constituents_pdgid->at(genJetIndex) = flatGenPdgId;
    GenJets_constituents_matchIndex->at(genJetIndex) = flatIndex;
    GenJets_nConstituents_unmatched->at(genJetIndex) = unmatchedGen;
    Jets_darkHadronJets->push_back(recoDarkHadronJets);
    Jets_darkHadronJets_constituents_genMatchOnly->push_back(recoSubjets);
    Jets_darkHadronJets_constituentsMatchStage->push_back(matchStage);
    Jets_darkHadronJets_constituentsPdgid->push_back(RecoPdgid);
    Jets_constituents_pdgid->push_back(flatRecoPdgId);
    Jets_constituents_matchStageReco->push_back(RecoMatchStage);

    //For unmatched reco particles, assign them to the closest dark hadron, and the second closest to demonstrate an uncertainty in this procedure
    std::vector<std::vector<CLorentzVector> > recoSubjetsNextDH = recoSubjets;
    std::vector<std::vector<CLorentzVector> > newRecoSubjets = recoSubjets;
    std::vector<int> recoUnmatchedPdgid = {};
    std::vector<int> isAssigned;
    int nRecoUnmatched = 0;
    for(unsigned i = 0; i < recoMatched.size(); i++){
      isAssigned.push_back(0);
      //std::cout << recoMatched[i] << std::endl;
      if (recoMatched[i] == false ) {
    	recoUnmatchedPdgid.push_back(cands_pdgids[recoJetIndex][i]);
	nRecoUnmatched++;

	CLorentzVector recoPart = jets_cands[recoJetIndex][i];
	std::vector<CLorentzVector> darkHadronJets = GenJets_darkHadronJets->at(genJetIndex);
	std::vector<double> dhjDeltaR; 

	for (const auto& dhj : darkHadronJets){
	  dhjDeltaR.push_back(deltaR(dhj, recoPart));
	}
	if (dhjDeltaR.size() > 0) {
	  std::vector<int> idx(dhjDeltaR.size()); 
	  std::iota(idx.begin(), idx.end(), 0);
	  // sort indexes based on comparing deltaR values using std::stable_sort, now idx vector is a list of indices sorted by deltaR 
	  std::stable_sort(idx.begin(), idx.end(), [&dhjDeltaR](int i1, int i2) {return dhjDeltaR[i1] < dhjDeltaR[i2];});	
	  newRecoSubjets[idx[0]].push_back(jets_cands[recoJetIndex][i]);
	  isAssigned[i] = 1;
	  if (dhjDeltaR.size() > 1) recoSubjetsNextDH[idx[1]].push_back(jets_cands[recoJetIndex][i]);
	}
      }
    }
    double unmatchedFraction = nRecoUnmatched / jets_cands[recoJetIndex].size();
    Jets_nConstituents_unmatched->push_back(nRecoUnmatched);
    Jets_nConstituents_unmatched_pdgid->push_back(recoUnmatchedPdgid);
    Jets_nConstituents_isAssigned->push_back(isAssigned);
    Jets_darkHadronJets_constituents->push_back(newRecoSubjets);
    Jets_darkHadronJets_constituents_nextDH->push_back(recoSubjetsNextDH);

    recoJetIndex++;
  }

  if(signal_){
    iEvent.put(std::move(jet_isHV_vec),"isHV");
    iEvent.put(std::move(hvCategory),"hvCategory");
    iEvent.put(std::move(darkPtFrac),"darkPtFrac");
    iEvent.put(std::move(MT2JetsID),"MT2JetsID");

    iEvent.put(std::move(GenJets_nConstituents),"GenJetsNConstituents");
    iEvent.put(std::move(GenJets_nConstituentsDarkHadrons),"GenJetsNConstituentsDarkHadrons");
    iEvent.put(std::move(GenJets_nConstituents_unmatched),"GenJetsNConstituentsUnmatched");
    iEvent.put(std::move(Jets_nConstituents),"JetsNConstituents");
    iEvent.put(std::move(Jets_nConstituents_unmatched),"JetsNConstituentsUnmatched");

    iEvent.put(std::move(GenJets_darkHadrons),"GenJetsDarkHadrons");
    iEvent.put(std::move(GenJets_darkHadronJets),"GenJetsDarkHadronJets");
    iEvent.put(std::move(Jets_darkHadronJets),"JetsDarkHadronJets");
    iEvent.put(std::move(GenJets_darkHadronJets_multiplicity),"GenJetsDarkHadronJetsMultiplicity");
    iEvent.put(std::move(Jets_nConstituents_unmatched_pdgid),"JetsNConstituentsUnmatchedPdgid");
    iEvent.put(std::move(Jets_nConstituents_isAssigned),"JetsNConstituentsIsAssigned");
    iEvent.put(std::move(Jets_constituents_pdgid),"JetsConstituentPdgid");
    iEvent.put(std::move(GenJets_constituents_pdgid),"GenJetsConstituentPdgid");
    iEvent.put(std::move(Jets_constituents_matchStageReco),"JetsConstituentMatchStageReco");
    iEvent.put(std::move(GenJets_constituents_matchIndex),"GenJetsConstituentMatchIndex");

    iEvent.put(std::move(GenJets_darkHadronJets_tau1),"GenJetsDarkHadronJetsTau1");
    iEvent.put(std::move(GenJets_darkHadronJets_tau2),"GenJetsDarkHadronJetsTau2");
    iEvent.put(std::move(GenJets_darkHadronJets_tau3),"GenJetsDarkHadronJetsTau3");

    iEvent.put(std::move(GenJets_darkHadronJets_constituents),"GenJetsDarkHadronJetsConstituents");
    iEvent.put(std::move(Jets_darkHadronJets_constituents),"JetsDarkHadronJetsConstituents"); 
    iEvent.put(std::move(Jets_darkHadronJets_constituents_genMatchOnly),"JetsDarkHadronJetsConstituentsGenMatchOnly"); 
    iEvent.put(std::move(Jets_darkHadronJets_constituents_nextDH),"JetsDarkHadronJetsConstituentsNextDH"); 
  }
  auto pMJJ = std::make_unique<double>(MJJ);
  iEvent.put(std::move(pMJJ),"MJJ");
  auto pMmc = std::make_unique<double>(Mmc);
  iEvent.put(std::move(pMmc),"Mmc");
  auto pMT = std::make_unique<double>(MT);
  iEvent.put(std::move(pMT),"MT");
  auto pMT2 = std::make_unique<double>(GenMT2);
  iEvent.put(std::move(pMT2),"GenMT2");
  auto pDeltaPhi1 = std::make_unique<double>(DeltaPhi1);
  iEvent.put(std::move(pDeltaPhi1),"DeltaPhi1");
  auto pDeltaPhi2 = std::make_unique<double>(DeltaPhi2);
  iEvent.put(std::move(pDeltaPhi2),"DeltaPhi2");
  auto pDeltaPhiMin = std::make_unique<double>(DeltaPhiMin);
  iEvent.put(std::move(pDeltaPhiMin),"DeltaPhiMin");
}

DEFINE_FWK_MODULE(HiddenSectorProducer);
