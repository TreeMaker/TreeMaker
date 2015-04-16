#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/PatCandidates/interface/Photon.h>
#include <DataFormats/PatCandidates/interface/Jet.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include <vector>
#include "TLorentzVector.h"

class CleanPATJetProducer : public edm::EDProducer {

public:
  explicit CleanPATJetProducer(const edm::ParameterSet&);
  ~CleanPATJetProducer();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  // ----------member data ---------------------------


  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string jetCollection;     // name of particle collection
  edm::InputTag photonCollection;
  edm::InputTag rhoCollection;
  bool        debug;
  
  bool isBarrelPhoton,isEndcapPhoton,isGenMatched;
  double chIso,nuIso,gamIso;
  bool passID,passIso,passAcc;
















};
