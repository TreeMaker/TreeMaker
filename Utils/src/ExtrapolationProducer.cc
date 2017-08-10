
#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TVector2.h"

//
// class declaration
//



class ExtrapolationProducer : public edm::global::EDProducer<> {
public:
  explicit ExtrapolationProducer(const edm::ParameterSet&);
  ~ExtrapolationProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  TVector2 GetWVec(double met, double met_phi, double lep_pt, double lep_phi) const {
    TVector2 nu;
    nu.SetMagPhi(met, met_phi);
    TVector2 lep;
    lep.SetMagPhi(lep_pt, lep_phi);
    
    TVector2 W(nu+lep);
    return W;
  }

  double GetMTW(double met, double met_phi, double lep_pt, double lep_phi) const {
    double deltaPhi =TVector2::Phi_mpi_pi(lep_phi-met_phi);
    return sqrt(2*lep_pt*met*(1-cos(deltaPhi)) );
  }

  double GetCDTT(double met, double met_phi, double lep_pt, double lep_phi) const {
    TVector2 w_lab_vec = GetWVec(met, met_phi, lep_pt, lep_phi);
    double pt_lab_w = w_lab_vec.Mod();

    double dphi_lab_lepton_met = TVector2::Phi_mpi_pi(lep_phi - met_phi);
    double cosdphi_lab_lepton_met = cos( dphi_lab_lepton_met ) ;

    double mt_w = GetMTW(met, met_phi, lep_pt, lep_phi);
    double et_lab_w = sqrt( pow( pt_lab_w, 2. ) + pow( mt_w, 2. ) ) ;

    double pt_parallel_lab_lepton = (lep_pt/pt_lab_w)*(lep_pt + met*cosdphi_lab_lepton_met ) ;

    double cos_dthetat = (2*pt_parallel_lab_lepton - pt_lab_w)/et_lab_w ;
    if ( cos_dthetat < -1. ) cos_dthetat = -1. ;
    if ( cos_dthetat > +1. ) cos_dthetat = +1. ;

    return cos_dthetat;
  }

private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
  edm::InputTag MuonTag_, ElecTag_, MHTPtTag_, MHTPhiTag_;
  edm::EDGetTokenT<edm::View<pat::Muon>> MuonTok_;
  edm::EDGetTokenT<edm::View<pat::Electron>> ElecTok_;
  edm::EDGetTokenT<double> MHTPtTok_, MHTPhiTok_;
	
	
  // ----------member data ---------------------------
};

ExtrapolationProducer::ExtrapolationProducer(const edm::ParameterSet& iConfig)
{
  //register your products
  MuonTag_ 				= 	iConfig.getParameter<edm::InputTag >("MuonTag");
  ElecTag_ 				= 	iConfig.getParameter<edm::InputTag >("ElectronTag");
  MHTPtTag_ = edm::InputTag("MHT","Pt");
  MHTPhiTag_ = edm::InputTag("MHT","Phi");
  MuonTok_ = consumes<edm::View<pat::Muon>>(MuonTag_);
  ElecTok_ = consumes<edm::View<pat::Electron>>(ElecTag_);
  MHTPtTok_ = consumes<double>(MHTPtTag_);
  MHTPhiTok_ = consumes<double>(MHTPhiTag_);

  produces<std::vector<double> >("MuPTW");
  produces<std::vector<double> >("MuCDTT");
  produces<std::vector<double> >("ElecPTW");
  produces<std::vector<double> >("ElecCDTT");

}

ExtrapolationProducer::~ExtrapolationProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}

void ExtrapolationProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;
		
  auto muPTW = std::make_unique<std::vector<double>>();
  auto muCDTT = std::make_unique<std::vector<double>>();
  auto elecPTW = std::make_unique<std::vector<double>>();
  auto elecCDTT = std::make_unique<std::vector<double>>();

  edm::Handle < double > mhtHandle ;
  iEvent.getByToken(MHTPtTok_,mhtHandle);
  double MHT = *mhtHandle;
  edm::Handle < double > mhtPhiHandle ;
  iEvent.getByToken(MHTPhiTok_,mhtPhiHandle);
  double MHTPhi = *mhtPhiHandle;
  TVector2 mhtVec(0,0);
  if (mhtHandle.isValid() && mhtPhiHandle.isValid()) {
    mhtVec.SetMagPhi(MHT, MHTPhi);
  } else edm::LogWarning("TreeMaker")<<"ExtrapolationProducer can't find MHT";

  edm::Handle<edm::View<pat::Muon> > muonHandle;
  iEvent.getByToken(MuonTok_, muonHandle);
  if(muonHandle.isValid()) {
    for(unsigned int m=0; m<muonHandle->size(); ++m)
      {
	muPTW->push_back(GetWVec(MHT, MHTPhi, muonHandle->at(m).pt(), muonHandle->at(m).phi()).Mod());
	muCDTT->push_back(GetCDTT(MHT, MHTPhi, muonHandle->at(m).pt(), muonHandle->at(m).phi()));
      }
  }

  edm::Handle<edm::View<pat::Electron> > eleHandle;
  iEvent.getByToken(ElecTok_, eleHandle);
  if(eleHandle.isValid())
    {
      for(unsigned int e=0; e<eleHandle->size(); ++e)
	{
	  elecPTW->push_back(GetWVec(MHT, MHTPhi, eleHandle->at(e).pt(), eleHandle->at(e).phi()).Mod());
	  elecCDTT->push_back(GetCDTT(MHT, MHTPhi, eleHandle->at(e).pt(), eleHandle->at(e).phi()));
	}
    }


  iEvent.put(std::move(muPTW),"MuPTW");
  iEvent.put(std::move(muCDTT),"MuCDTT");
  
  iEvent.put(std::move(elecPTW),"ElecPTW");
  iEvent.put(std::move(elecCDTT),"ElecCDTT");

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ExtrapolationProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ExtrapolationProducer);
