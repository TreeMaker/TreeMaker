#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <vector>


class fourVectorProducer : public edm::EDProducer {

public:
  explicit fourVectorProducer(const edm::ParameterSet&);
  ~fourVectorProducer();
  
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
  
  edm::InputTag particleCollection;     // name of particle collection
  bool        debug;
};


