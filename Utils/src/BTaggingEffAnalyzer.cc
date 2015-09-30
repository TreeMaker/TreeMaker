// -*- C++ -*-
//
// Package:    BTaggingEffAnalyzer
// Class:      BTaggingEffAnalyzer
// 
/**\class BTaggingEffAnalyzer BTaggingEffAnalyzer.cc Analysis/EDSHyFT/plugins/BTaggingEffAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Dinko Ferencek
//         Created:  Thu Oct  4 20:25:54 CDT 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH2D.h"


//
// class declaration
//

class BTaggingEffAnalyzer : public edm::EDAnalyzer {
   public:
      explicit BTaggingEffAnalyzer(const edm::ParameterSet&);
      ~BTaggingEffAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      // ----------member data ---------------------------
      const edm::InputTag jetsTag;
      const std::string   discriminatorTag;
      const std::string   csvTag;
      const double  discriminatorValue;
      const int     ptNBins;
      const double  ptMin;
      const double  ptMax;
      const int     etaNBins;
      const double  etaMin;
      const double  etaMax;
      edm::Service<TFileService>  fs;
      TH2D  *h2_BTaggingEff_Denom_b;
      TH2D  *h2_BTaggingEff_Denom_c;
      TH2D  *h2_BTaggingEff_Denom_udsg;
      TH2D  *h2_BTaggingEff_Num_b;
      TH2D  *h2_BTaggingEff_Num_c;
      TH2D  *h2_BTaggingEff_Num_udsg;
};

//
// constants, enums and typedefs
//
typedef std::vector<pat::Jet> PatJetCollection;

//
// static data member definitions
//

//
// constructors and destructor
//
BTaggingEffAnalyzer::BTaggingEffAnalyzer(const edm::ParameterSet& iConfig) :

  jetsTag(iConfig.getParameter<edm::InputTag>("JetsTag")),
  discriminatorTag(iConfig.getParameter<std::string>("DiscriminatorTag")),
  discriminatorValue(iConfig.getParameter<double>("DiscriminatorValue")),
  ptNBins(iConfig.getParameter<int>("PtNBins")),
  ptMin(iConfig.getParameter<double>("PtMin")),
  ptMax(iConfig.getParameter<double>("PtMax")),
  etaNBins(iConfig.getParameter<int>("EtaNBins")),
  etaMin(iConfig.getParameter<double>("EtaMin")),
  etaMax(iConfig.getParameter<double>("EtaMax"))

{
   //now do what ever initialization is needed
   h2_BTaggingEff_Denom_b    = fs->make<TH2D>("h2_BTaggingEff_Denom_b", ";p_{T} [GeV];#eta", ptNBins, ptMin, ptMax, etaNBins, etaMin, etaMax);
   h2_BTaggingEff_Denom_c    = fs->make<TH2D>("h2_BTaggingEff_Denom_c", ";p_{T} [GeV];#eta", ptNBins, ptMin, ptMax, etaNBins, etaMin, etaMax);
   h2_BTaggingEff_Denom_udsg = fs->make<TH2D>("h2_BTaggingEff_Denom_udsg", ";p_{T} [GeV];#eta", ptNBins, ptMin, ptMax, etaNBins, etaMin, etaMax);
   h2_BTaggingEff_Num_b    = fs->make<TH2D>("h2_BTaggingEff_Num_b", ";p_{T} [GeV];#eta", ptNBins, ptMin, ptMax, etaNBins, etaMin, etaMax);
   h2_BTaggingEff_Num_c    = fs->make<TH2D>("h2_BTaggingEff_Num_c", ";p_{T} [GeV];#eta", ptNBins, ptMin, ptMax, etaNBins, etaMin, etaMax);
   h2_BTaggingEff_Num_udsg = fs->make<TH2D>("h2_BTaggingEff_Num_udsg", ";p_{T} [GeV];#eta", ptNBins, ptMin, ptMax, etaNBins, etaMin, etaMax);
}

BTaggingEffAnalyzer::~BTaggingEffAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
BTaggingEffAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<PatJetCollection> jets;
  iEvent.getByLabel(jetsTag,jets);

  //grab event selection variables:
  edm::Handle<double> HT;
  edm::Handle<double> MHT; 
  edm::Handle<double>DeltaPhi1;
  edm::Handle<double>DeltaPhi2;
  edm::Handle<double>DeltaPhi3;
  edm::Handle<double>DeltaPhi4;
  edm::Handle<int> NJets;
  edm::Handle<int> Leptons;
  edm::Handle<int> isoPionTracks;
  edm::Handle<int> isoMuonTracks;
  edm::Handle<int> isoElectronTracks;
  edm::Handle<bool> JetID; 

  iEvent.getByLabel("HT", HT);
  iEvent.getByLabel("MHT","Pt", MHT);
  iEvent.getByLabel("DeltaPhi", "DeltaPhi1", DeltaPhi1);
  iEvent.getByLabel("DeltaPhi","DeltaPhi2", DeltaPhi2);
  iEvent.getByLabel("DeltaPhi","DeltaPhi3", DeltaPhi3);
//  iEvent.getByLabel("DeltaPhi","DeltaPhi4", DeltaPhi4);

  iEvent.getByLabel("NJets", NJets);
  iEvent.getByLabel("LeptonsNew", Leptons);
  iEvent.getByLabel("isoPionTracks", isoPionTracks);
  iEvent.getByLabel("isoMuonTracks", isoMuonTracks);
  iEvent.getByLabel("isoElectronTracks", isoElectronTracks);
  iEvent.getByLabel("JetID", JetID);
  bool passEvSel=false;
  if(*HT>500 && *MHT>200 && *DeltaPhi1>0.5 && *DeltaPhi2>0.5 && *DeltaPhi3>0.3 && *NJets>=4 && *Leptons==0 && *isoPionTracks==0 && *isoMuonTracks==0 && *isoElectronTracks==0 && *JetID)passEvSel=true;
 
  // loop over jets
  for(PatJetCollection::const_iterator it = jets->begin(); it != jets->end(); ++it)
  {
    if(!passEvSel)continue;    
    int partonFlavor = it->partonFlavour();

    if( abs(partonFlavor)==5 )
    {
      h2_BTaggingEff_Denom_b->Fill(it->pt(), it->eta());
      if( it->bDiscriminator(discriminatorTag.c_str()) >= discriminatorValue ) h2_BTaggingEff_Num_b->Fill(it->pt(), it->eta());
    }
    else if( abs(partonFlavor)==4 )
    {
      h2_BTaggingEff_Denom_c->Fill(it->pt(), it->eta());
      if( it->bDiscriminator(discriminatorTag.c_str()) >= discriminatorValue ) h2_BTaggingEff_Num_c->Fill(it->pt(), it->eta());
    }
    else
    {
      h2_BTaggingEff_Denom_udsg->Fill(it->pt(), it->eta());
      if( it->bDiscriminator(discriminatorTag.c_str()) >= discriminatorValue ) h2_BTaggingEff_Num_udsg->Fill(it->pt(), it->eta());
    }
  }
}


// ------------ method called once each job just before starting event loop  ------------
void 
BTaggingEffAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BTaggingEffAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
BTaggingEffAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
BTaggingEffAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
BTaggingEffAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
BTaggingEffAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
BTaggingEffAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(BTaggingEffAnalyzer);
