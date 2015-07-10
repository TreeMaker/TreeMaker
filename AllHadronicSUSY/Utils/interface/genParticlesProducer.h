#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/PatCandidates/interface/Photon.h>
#include "FWCore/Utilities/interface/InputTag.h"

#include <vector>


class genParticlesProducer : public edm::EDProducer {

public:
  explicit genParticlesProducer(const edm::ParameterSet&);
  ~genParticlesProducer();
  
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
  
  edm::InputTag genCollection; 
  bool        debug;

};


