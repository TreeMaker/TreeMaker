#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include <DataFormats/PatCandidates/interface/Photon.h>
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include <DataFormats/PatCandidates/interface/Electron.h>
#include <DataFormats/EgammaCandidates/interface/Conversion.h>
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
#include <DataFormats/BeamSpot/interface/BeamSpot.h>
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include <vector>


class PhotonIDisoProducer : public edm::EDProducer {

public:
  explicit PhotonIDisoProducer(const edm::ParameterSet&);
  ~PhotonIDisoProducer();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
    bool hasMatchedPromptElectron(const reco::SuperClusterRef &sc, const edm::Handle<std::vector<pat::Electron> > &eleCol,
				const edm::Handle<reco::ConversionCollection> &convCol, const math::XYZPoint &beamspot,
				float lxyMin=2.0, float probMin=1e-6, unsigned int nHitsBeforeVtxMax=0);
  // ----------member data ---------------------------


  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  edm::InputTag photonCollection; 
  edm::InputTag electronCollection; 
  edm::InputTag conversionCollection; 
  edm::InputTag beamspotCollection; 
  edm::InputTag ecalRecHitsInputTag_EE_;
  edm::InputTag ecalRecHitsInputTag_EB_;
  edm::InputTag rhoCollection;
  edm::InputTag genParCollection;
  edm::EDGetTokenT<edm::View<pat::Photon>> photonTok_;
  edm::EDGetTokenT<pat::ElectronCollection> electronTok_;
  edm::EDGetTokenT<std::vector<reco::Conversion>> conversionTok_;
  edm::EDGetTokenT<reco::BeamSpot> beamspotTok_;
  edm::EDGetTokenT<EcalRecHitCollection> ecalRecHitsInputTag_EE_Token_;
  edm::EDGetTokenT<EcalRecHitCollection> ecalRecHitsInputTag_EB_Token_;
  edm::EDGetTokenT<double> rhoTok_;
  edm::EDGetTokenT<edm::View<reco::GenParticle>> genParTok_;
  bool        debug;

};


