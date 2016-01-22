
#include <memory>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TVector2.h"

#include "TreeMaker/Utils/interface/get_isolation_activity.h"

//
// class declaration
//



class IsolationProducer : public edm::EDProducer {
public:
  explicit IsolationProducer(const edm::ParameterSet&);
  ~IsolationProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
    
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag LeptonTag_, PFCandTag_, JetTag_, RhoTag_;
  edm::EDGetTokenT<edm::View<reco::Candidate>> LeptonTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> PFCandTok_;
  edm::EDGetTokenT<pat::JetCollection> JetTok_;
  edm::EDGetTokenT<double> RhoTok_;
  
  std::string LeptonTypeName_;
  enum lepton_type { electron = 0, muon = 1, gen = 2, track = 3, other = 4 };
  lepton_type LeptonType_;
  SUSYIsolation SUSYIsolationHelper;
    
  // ----------member data ---------------------------
};

IsolationProducer::IsolationProducer(const edm::ParameterSet& iConfig)
{
  //register your product
  LeptonTag_         =     iConfig.getParameter<edm::InputTag>("LeptonTag");
  LeptonTypeName_       =     iConfig.getParameter<std::string>("LeptonType");
  PFCandTag_        =     iConfig.getParameter<edm::InputTag>("PFCandTag");
  JetTag_        =     iConfig.getParameter<edm::InputTag>("JetTag");
  RhoTag_ = edm::InputTag("fixedGridRhoFastjetAll");
  
  LeptonTok_ = consumes<edm::View<reco::Candidate>>(LeptonTag_);
  PFCandTok_ = consumes<pat::PackedCandidateCollection>(PFCandTag_);
  JetTok_ = consumes<pat::JetCollection>(JetTag_);
  RhoTok_ = consumes<double>(RhoTag_);
  
  if(LeptonTypeName_=="electron") LeptonType_ = electron; 
  else if(LeptonTypeName_=="muon") LeptonType_ = muon; 
  else if(LeptonTypeName_=="gen") LeptonType_ = gen; 
  else if(LeptonTypeName_=="track") LeptonType_ = track; 
  else {
    LeptonType_ = other;
    std::cout << "IsolationProducer Error: " << LeptonTypeName_ << " is not a valid collection." << std::endl;
  }

  produces<std::vector<double> >("MiniIso");
  produces<std::vector<double> >("RA2Activity");
  produces<std::vector<double> >("MT2Activity");

}

IsolationProducer::~IsolationProducer()
{
    
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
    
}

void IsolationProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //  std::cout<<"Running IsolationProducer"<<std::endl;
 
  using namespace edm;
        
  std::auto_ptr<std::vector<double> > mini_iso(new std::vector<double>());
  std::auto_ptr<std::vector<double> > ra2_activity(new std::vector<double>());
  std::auto_ptr<std::vector<double> > mt2_activity(new std::vector<double>());

  
  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(PFCandTok_, pfcands);

  edm::Handle<pat::JetCollection> jets;
  iEvent.getByToken(JetTok_, jets);

  edm::Handle< double > rho_;
  iEvent.getByToken(RhoTok_, rho_);
  double rho = *rho_;

  if(LeptonType_ != other){
    //std::cout << "Computing mini isolation for " << LeptonTag_.label() << ":" << LeptonTag_.instance() << std::endl;
    edm::Handle<edm::View<reco::Candidate> > lepHandle;
    iEvent.getByToken(LeptonTok_, lepHandle);
    if(lepHandle.isValid())
    {
      SUSYIsolation::iso_types IsoType_ = SUSYIsolation::other;
      bool useEME = false;
      if(LeptonType_==electron){ IsoType_ = SUSYIsolation::electron; useEME = false; }
      else if(LeptonType_==muon){ IsoType_ = SUSYIsolation::muon; useEME = true; }
    
      for(unsigned int e=0; e<lepHandle->size(); ++e)
      {
        if(LeptonType_==gen){
          int pdgId = abs(lepHandle->at(e).pdgId());
          if (pdgId==11) IsoType_ = SUSYIsolation::electron;
          else IsoType_ = SUSYIsolation::muon; // treat taus as muons for now
          useEME = (pdgId==13);
        }
        else if(LeptonType_==track){
          int pdgId = abs(lepHandle->at(e).pdgId());
          if (pdgId==11) IsoType_ = SUSYIsolation::electron;
          else if(pdgId==13) IsoType_ = SUSYIsolation::muon;
          useEME = (pdgId==13);
        }
          
        const reco::Candidate* lep = &((*lepHandle)[e]);
        double mini_iso_val(0.);
        double mt2_activity_val(0.);
        SUSYIsolationHelper.GetMiniIsolation(pfcands, lep, IsoType_, rho, mini_iso_val, mt2_activity_val);
        mini_iso->push_back(mini_iso_val);
        mt2_activity->push_back(mt2_activity_val);
        ra2_activity->push_back(SUSYIsolationHelper.GetRA2Activity(jets, lep, useEME));
      }
    }
  }

  iEvent.put(mini_iso,"MiniIso");
  iEvent.put(ra2_activity,"RA2Activity");
  iEvent.put(mt2_activity,"MT2Activity");
  
}

// ------------ method called once each job just before starting event loop  ------------
void
IsolationProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
IsolationProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
IsolationProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
IsolationProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
IsolationProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
IsolationProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
IsolationProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(IsolationProducer);
