
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
  edm::InputTag LeptonTag_, PFCandTag_, JetTag_;
  std::string LeptonType_;
	
  // ----------member data ---------------------------
};

IsolationProducer::IsolationProducer(const edm::ParameterSet& iConfig)
{
  //register your producer
  LeptonTag_ 	    = 	iConfig.getParameter<edm::InputTag>("LeptonTag");
  LeptonType_       = 	iConfig.getParameter<std::string>("LeptonType");
  PFCandTag_        = 	iConfig.getParameter<edm::InputTag>("PFCandTag");
  JetTag_        = 	iConfig.getParameter<edm::InputTag>("JetTag");

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
  iEvent.getByLabel(PFCandTag_, pfcands);

  edm::Handle<pat::JetCollection> jets;
  iEvent.getByLabel(JetTag_, jets);

  edm::Handle< double > rho_;
  iEvent.getByLabel("fixedGridRhoFastjetAll", rho_);
  double rho = *rho_;

  //std::cout << "Computing mini isolation for " << LeptonTag_.label() << ":" << LeptonTag_.instance() << std::endl;
  if (LeptonType_=="electron") {
    edm::Handle<edm::View<pat::Electron> > eleHandle;
    iEvent.getByLabel(LeptonTag_, eleHandle);
    if(eleHandle.isValid())
      {
	for(unsigned int e=0; e<eleHandle->size(); ++e)
	  {
	    const reco::Candidate* lep = dynamic_cast<const reco::Candidate *>(&((*eleHandle)[e]));
	    mini_iso->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, LeptonType_, rho));
	    ra2_activity->push_back(SUSYIsolation::GetRA2Activity(jets, lep, false));
	    mt2_activity->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, LeptonType_, rho, true));
	  }
      }
  }
  else if (LeptonType_=="muon") {
    edm::Handle<edm::View<pat::Muon> > muonHandle;
    iEvent.getByLabel(LeptonTag_, muonHandle);
    if(muonHandle.isValid()) {
      for(unsigned int m=0; m<muonHandle->size(); ++m)
	{
	  const reco::Candidate* lep = dynamic_cast<const reco::Candidate *>(&((*muonHandle)[m]));
	  mini_iso->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, LeptonType_, rho));
	  ra2_activity->push_back(SUSYIsolation::GetRA2Activity(jets, lep, true));
	  mt2_activity->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, LeptonType_, rho, true));
	}
    }
  }
  else if (LeptonType_=="gen") {
    edm::Handle<edm::View<reco::GenParticle> > genHandle;
    iEvent.getByLabel(LeptonTag_, genHandle);
    if(genHandle.isValid()) {
      for(unsigned int igen=0; igen<genHandle->size(); ++igen)
	{
	  int pdgId = abs(genHandle->at(igen).pdgId());
	  std::string gen_type="";
	  if (pdgId==11) gen_type="electron";
	  else gen_type="muon"; // treat taus as muons for now
	  const reco::Candidate* lep = dynamic_cast<const reco::Candidate *>(&((*genHandle)[igen]));
	  mini_iso->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, gen_type, rho));
	  ra2_activity->push_back(SUSYIsolation::GetRA2Activity(jets, lep, (pdgId==13)));
	  mt2_activity->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, gen_type, rho, true));
	}
    }
  }
  else if (LeptonType_=="track") {
    edm::Handle<edm::View<pat::PackedCandidate> > trackHandle;
    iEvent.getByLabel(LeptonTag_, trackHandle);
    if(trackHandle.isValid()) {
      for(unsigned int itrack=0; itrack<trackHandle->size(); ++itrack)
	{
	  int pdgId = abs(trackHandle->at(itrack).pdgId());
	  std::string track_type="";
	  if (pdgId==11) track_type="electron";
	  else if (pdgId==13) track_type="muon";
	  const reco::Candidate* lep = dynamic_cast<const reco::Candidate *>(&((*trackHandle)[itrack]));
	  mini_iso->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, track_type, rho));
	  ra2_activity->push_back(SUSYIsolation::GetRA2Activity(jets, lep, (pdgId==13)));
	  mt2_activity->push_back(SUSYIsolation::GetMiniIsolation(pfcands, lep, track_type, rho, true));
	}
    }
  }
  else std::cout << "IsolationProducer Error: " << LeptonType_ << " is not a valid collection." << std::endl;

  

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
