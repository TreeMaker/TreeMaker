// system include files
#include <memory>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include <TVector2.h>

class JetCleaner : public edm::EDProducer {
public:
	explicit JetCleaner(const edm::ParameterSet&);
private:
	virtual void produce(edm::Event&, const edm::EventSetup&);
   double deltaR(double eta1, double phi1, double eta2, double phi2);
   edm::InputTag JetTag_;
   edm::InputTag ElectronTag_, MuonTag_, PhotonTag_;
   double ElectronR_, MuonR_, PhotonR_;
};

JetCleaner::JetCleaner(const edm::ParameterSet& iConfig)
{
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");

	ElectronTag_ = iConfig.getParameter<edm::InputTag>("ElectronTag");
   ElectronR_ = iConfig.getParameter<double>("ElectronR");
	MuonTag_ = iConfig.getParameter<edm::InputTag>("MuonTag");
   MuonR_ = iConfig.getParameter<double>("MuonR");
	PhotonTag_ = iConfig.getParameter<edm::InputTag>("PhotonTag");
   PhotonR_ = iConfig.getParameter<double>("PhotonR");

	produces<std::vector<pat::Jet>>("GoodJetsclean");
}

void JetCleaner::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	edm::Handle<std::vector<pat::Jet>> Jets;
   iEvent.getByLabel(JetTag_, Jets);
	
	edm::Handle<std::vector<pat::Electron>> Electrons;
	iEvent.getByLabel(ElectronTag_, Electrons);

   edm::Handle<std::vector<pat::Muon>> Muons;
	iEvent.getByLabel(MuonTag_, Muons);

   edm::Handle<std::vector<pat::Photon>> Photons;
	iEvent.getByLabel(PhotonTag_, Photons);

   std::vector<pat::Jet> newJets;

   for (unsigned int i = 0; i < Jets->size(); ++i) {
      double jeteta = (*Jets)[i].eta();
      double jetphi = (*Jets)[i].phi();
      bool addjet = true;
      for (unsigned int j = 0; j < Electrons->size(); ++j) {
         if (deltaR(jeteta, jetphi, (*Electrons)[j].eta(), (*Electrons)[j].phi()) < ElectronR_) {
            addjet = false;
            break;
         }
      }
      for (unsigned int j = 0; j < Muons->size(); ++j) {
         if (deltaR(jeteta, jetphi, (*Muons)[j].eta(), (*Muons)[j].phi()) < MuonR_) {
            addjet = false;
            break;
         }
      }
      for (unsigned int j = 0; j < Photons->size(); ++j) {
         if (deltaR(jeteta, jetphi, (*Photons)[j].eta(), (*Photons)[j].phi()) < PhotonR_) {
            addjet = false;
            break;
         }
      }
      if (addjet) newJets.push_back((*Jets)[i]);
   }

   std::auto_ptr<std::vector<pat::Jet>> item0(new std::vector<pat::Jet>(newJets));
   iEvent.put(item0, std::string("GoodJetsclean"));
}

double JetCleaner::deltaR(double eta1, double phi1, double eta2, double phi2)
{
  double deta = eta1-eta2;
  double dphi = TVector2::Phi_mpi_pi(phi1-phi2);
  return sqrt(deta * deta + dphi *dphi); 
}

DEFINE_FWK_MODULE(JetCleaner);

