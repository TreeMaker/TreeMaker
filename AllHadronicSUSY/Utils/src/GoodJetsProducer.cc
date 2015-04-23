// -*- C++ -*-
//
// Package:    GoodJetsProducer
// Class:      GoodJetsProducer
// 
/**\class GoodJetsProducer GoodJetsProducer.cc RA2Classic/GoodJetsProducer/src/GoodJetsProducer.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Thu Apr 17 10:49:52 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include <TVector2.h>
//
// class declaration
//

class GoodJetsProducer : public edm::EDFilter {
public:
	explicit GoodJetsProducer(const edm::ParameterSet&);
	~GoodJetsProducer();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
   virtual void beginJob() override;
   virtual bool filter(edm::Event&, const edm::EventSetup&) override;
   virtual void endJob() override;
   
   virtual void beginRun(edm::Run&, edm::EventSetup const&);
   virtual void endRun(edm::Run&, edm::EventSetup const&);
   virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   edm::InputTag JetTag_;
   edm::InputTag MuonTag_, ElecTag_, IsoTrackTag_;
   double maxEta_;
   double maxMuFraction_, minNConstituents_, maxNeutralFraction_, maxPhotonFraction_, minChargedMultiplicity_, minChargedFraction_, maxChargedEMFraction_;
   double jetPtFilter_;
   bool ExcludeLeptonIsoTrackPhotons_;
   double JetConeSize_;
   double deltaR(double eta1, double phi1, double eta2, double phi2);
   
   // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
using namespace pat;
GoodJetsProducer::GoodJetsProducer(const edm::ParameterSet& iConfig)
{
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   maxEta_ = iConfig.getParameter <double> ("maxJetEta");
   maxMuFraction_ = iConfig.getParameter <double> ("maxMuFraction");
   minNConstituents_ = iConfig.getParameter <double> ("minNConstituents");
   maxNeutralFraction_ = iConfig.getParameter <double> ("maxNeutralFraction");
   maxPhotonFraction_ = iConfig.getParameter <double> ("maxPhotonFraction");
   minChargedMultiplicity_ = iConfig.getParameter <double> ("minChargedMultiplicity");
   minChargedFraction_ = iConfig.getParameter <double> ("minChargedFraction");
   maxChargedEMFraction_ = iConfig.getParameter <double> ("maxChargedEMFraction");
   jetPtFilter_ = iConfig.getParameter <double> ("jetPtFilter");
   produces<std::vector<Jet> >();
   ExcludeLeptonIsoTrackPhotons_ = iConfig.getParameter <bool> ("ExcludeLepIsoTrackPhotons");
   MuonTag_ = iConfig.getParameter<edm::InputTag>("MuonTag");
   ElecTag_ = iConfig.getParameter<edm::InputTag>("ElecTag");
   IsoTrackTag_ = iConfig.getParameter<edm::InputTag>("IsoTrackTag");
   JetConeSize_ = iConfig.getParameter <double> ("JetConeSize");
}


GoodJetsProducer::~GoodJetsProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
bool
GoodJetsProducer::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   // load to be excluded leptons, isotracks and photons
   edm::Handle<edm::View<pat::Muon> > muonHandle;
   iEvent.getByLabel(MuonTag_, muonHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !muonHandle.isValid()) std::cout<<"Warning Muon Tag not valid in GoodJetSelector: "<<MuonTag_<<std::endl;
   edm::Handle<edm::View<pat::Electron> > eleHandle;
   iEvent.getByLabel(ElecTag_, eleHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !eleHandle.isValid()) std::cout<<"Warning elec Tag not valid in GoodJetSelector: "<<ElecTag_<<std::endl;
   edm::Handle<edm::View<pat::PackedCandidate> > isoTrackHandle;
   iEvent.getByLabel(IsoTrackTag_, isoTrackHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !isoTrackHandle.isValid()) std::cout<<"Warning isotrack Tag not valid in GoodJetSelector: "<<IsoTrackTag_<<std::endl;
   std::auto_ptr<std::vector<Jet> > prodJets(new std::vector<Jet>());
   edm::Handle< edm::View<Jet> > Jets;
   iEvent.getByLabel(JetTag_,Jets);
   if(Jets.isValid())
   {
      for(unsigned int i=0; i<Jets->size();i++)
      {
         if (std::abs(Jets->at(i).eta())>maxEta_) continue;
         float neufrac=Jets->at(i).neutralHadronEnergyFraction();//gives raw energy in the denominator
         float phofrac=Jets->at(i).neutralEmEnergyFraction();//gives raw energy in the denominator
         float chgfrac=Jets->at(i).chargedHadronEnergyFraction();
         float chgEMfrac=Jets->at(i).chargedEmEnergyFraction();
         float muFrac=Jets->at(i).muonEnergyFraction();
         unsigned int nconstit=Jets->at(i).nConstituents();
	 bool skip=false;
	 if(ExcludeLeptonIsoTrackPhotons_)
	 {
	 for(unsigned int m=0; m<muonHandle->size(); ++m)
	 {
	   if(std::abs(Jets->at(i).pt() - muonHandle->at(m).pt() ) / muonHandle->at(m).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),muonHandle->at(m).eta(),muonHandle->at(m).phi())<JetConeSize_ ) skip=true;
	 }
	 for(unsigned int e=0; e<eleHandle->size(); ++e)
	 {
	   if(std::abs(Jets->at(i).pt() - eleHandle->at(e).pt() ) / eleHandle->at(e).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),eleHandle->at(e).eta(),eleHandle->at(e).phi())<JetConeSize_ ) skip=true;
	 }
	 for(unsigned int e=0; e<isoTrackHandle->size(); ++e)
	 {
	   if(std::abs(Jets->at(i).pt() - isoTrackHandle->at(e).pt() ) / isoTrackHandle->at(e).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),isoTrackHandle->at(e).eta(),isoTrackHandle->at(e).phi())<JetConeSize_ ) skip=true;
	 }
	 if(skip) 
	 {
	   prodJets->push_back(Jet(Jets->at(i)));
	   continue;
	 }
	 }
         if (std::abs(Jets->at(i).eta()) < 2.4){
            int chgmulti=Jets->at(i).chargedHadronMultiplicity();
            if (muFrac<maxMuFraction_ && nconstit>=minNConstituents_ && neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ &&chgmulti>=minChargedMultiplicity_ && chgfrac>minChargedFraction_ && chgEMfrac<maxChargedEMFraction_) {
               prodJets->push_back(Jet(Jets->at(i)));
            } else {
               if (Jets->at(i).pt() > jetPtFilter_) {
                  std::cout << "Filtered jet pT, eta: " << Jets->at(i).pt() << ", " << Jets->at(i).eta() << std::endl;
                  return false;
               }
            }
         } else {
            if (neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ ) {
               prodJets->push_back(Jet(Jets->at(i)));
            } else {
               if (Jets->at(i).pt() > jetPtFilter_) {
                  std::cout << "Filtered jet pT, eta: " << Jets->at(i).pt() << ", " << Jets->at(i).eta() << std::endl;
                  return false;
               }
            }
         }
      }
   }
   // put in the event
   const std::string string1("");
   iEvent.put(prodJets );
   return true;
   
}

// ------------ method called once each job just before starting event loop  ------------
void 
GoodJetsProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GoodJetsProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
GoodJetsProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GoodJetsProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GoodJetsProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GoodJetsProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GoodJetsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}
double GoodJetsProducer::deltaR(double eta1, double phi1, double eta2, double phi2)
{
  double deta = eta1-eta2;
  double dphi = TVector2::Phi_mpi_pi(phi1-phi2);
  return sqrt(deta * deta + dphi *dphi); 
}

//define this as a plug-in
DEFINE_FWK_MODULE(GoodJetsProducer);
