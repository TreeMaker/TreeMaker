// system include files
#include <memory>
#include <vector>
#include <cmath>
#include <utility>
#include <unordered_set>
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

class HiddenSectorProducer : public edm::global::EDProducer<> {
  public:
    explicit HiddenSectorProducer(const edm::ParameterSet&);
  private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
    //helper
    double TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const;
    template <class P>
    void addDaughters(const P* i_part, std::vector<CandPtr>& listOfDaughters) const;
    void fillSet(PidSet& IDset, const std::string& name, const edm::ParameterSet& iConfig);
    bool isParticle(const PidSet& darkList, CandPtr part) const;
    bool isParticle(const PidSet& darkList, int pid) const;
    bool isParticle(const CandSet& darkList, CandPtr part) const;
    bool isAncestor(const PidSet& darkList, CandPtr part) const;
    void medDecay(CandPtr part, CandSet& firstQdM, CandSet& firstQsM, CandPtr& firstQdM1, CandPtr& firstQdM2, CandPtr& firstQsM1, CandPtr& firstQsM2, bool& secondDM, bool& secondSM) const;
    void firstDark(CandPtr part, CandSet& firstMd, CandSet& firstQd, CandSet& firstGd, CandSet& firstQdM, CandSet& firstQsM, CandPtr& firstQdM1, CandPtr& firstQdM2, CandPtr& firstQsM1, CandPtr& firstQsM2, bool& secondDM, bool& secondSM) const;
    int checkLast(const reco::GenJet& jet, const CandSet& stableDs, int value, double& frac) const;
    int checkFirst(const reco::GenJet& jet, const CandSet& firstP, int value) const;
    double calculateMT2(const edm::Handle<edm::View<reco::GenMET>>& h_genmets, const reco::GenJet& dQM1J, const reco::GenJet& SMM1J, const reco::GenJet& dQM2J, const reco::GenJet& SMM2J) const;
    bool signal_;
    edm::InputTag JetTag_, MetTag_, GenMetTag_, GenTag_, GenJetTag_;
    edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
    edm::EDGetTokenT<edm::View<pat::MET>> MetTok_;
    edm::EDGetTokenT<edm::View<reco::GenMET>> GenMetTok_;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> GenTok_;
    edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok_;
    double coneSize_;
    PidSet DarkSMediatorIDs_, DarkTMediatorIDs_, DarkQuarkIDs_, DarkHadronIDs_, DarkGluonIDs_, DarkStableIDs_, DarkFirstIDs_, SMQuarkIDs_;
};

void HiddenSectorProducer::fillSet(PidSet& IDset, const std::string& name, const edm::ParameterSet& iConfig){
  const auto& ids = iConfig.getParameter<std::vector<unsigned>>(name);
  IDset.insert(ids.begin(),ids.end());
}

bool HiddenSectorProducer::isParticle(const PidSet& darkList, CandPtr part) const {
  return isParticle(darkList, part->pdgId());
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

HiddenSectorProducer::HiddenSectorProducer(const edm::ParameterSet& iConfig) :
  signal_(iConfig.getParameter<bool>("signal")),
  JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
  MetTag_(iConfig.getParameter<edm::InputTag>("MetTag")),
  GenMetTag_(iConfig.getParameter<edm::InputTag>("GenMetTag")),
  GenTag_(iConfig.getParameter<edm::InputTag>("GenTag")),
  GenJetTag_(iConfig.getParameter<edm::InputTag>("GenJetTag")),
  JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
  MetTok_(consumes<edm::View<pat::MET>>(MetTag_)),
  GenMetTok_(consumes<edm::View<reco::GenMET>>(GenMetTag_)),
  GenTok_(consumes<edm::View<reco::GenParticle>>(GenTag_)),
  GenJetTok_(consumes<edm::View<reco::GenJet>>(GenJetTag_)),
  coneSize_(iConfig.getParameter<double>("coneSize"))
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

void HiddenSectorProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
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

  auto jet_isHV_vec = std::make_unique<std::vector<bool>>();
  auto hvCategory = std::make_unique<std::vector<int>>();
  auto darkPtFrac = std::make_unique<std::vector<double>>();
  auto MT2JetsID = std::make_unique<std::vector<int>>();

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
  }

  if(signal_){
    iEvent.put(std::move(jet_isHV_vec),"isHV");
    iEvent.put(std::move(hvCategory),"hvCategory");
    iEvent.put(std::move(darkPtFrac),"darkPtFrac");
    iEvent.put(std::move(MT2JetsID),"MT2JetsID");
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
