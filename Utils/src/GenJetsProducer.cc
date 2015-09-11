
#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/GenJet.h"

#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

#include "TVector2.h"

//
// class declaration
//



class GenJetsProducer : public edm::EDProducer {
public:
  explicit GenJetsProducer(const edm::ParameterSet&);
  ~GenJetsProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  double * genHT_;
  edm::InputTag LHEEventProducerTag_, GenJetsTag_;
	
	
  // ----------member data ---------------------------
};

GenJetsProducer::GenJetsProducer(const edm::ParameterSet& iConfig)
{
  //register your producer
  GenJetsTag_   		= 	iConfig.getParameter<edm::InputTag >("GenJetsTag");

  produces<double>("genHT");
  const std::string s_GenJets("GenJets");
  produces<std::vector<reco::GenJet> > (s_GenJets).setBranchAlias(s_GenJets);

  genHT_ = new double;

}

GenJetsProducer::~GenJetsProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  delete genHT_;
	
}

void GenJetsProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //  std::cout<<"Running GenJetsProducer"<<std::endl;
 
  using namespace edm;

  // first calculate genHT
  double genHT = 0.0;
  
  edm::Handle<LHEEventProduct> evt;
  iEvent.getByLabel( "externalLHEProducer", evt );
  const lhef::HEPEUP hepeup_ = evt->hepeup();
  const int nup_ = hepeup_.NUP;
  const std::vector<int> idup_ = hepeup_.IDUP;
  const std::vector<lhef::HEPEUP::FiveVector> pup_ = hepeup_.PUP;
  const std::vector<int> istup_ = hepeup_.ISTUP;
  const std::vector<std::pair<int,int> > momup_ = hepeup_.MOTHUP;

  for ( unsigned int icount = 0 ; icount < (unsigned int)nup_; icount++ ) {
    int PID    = idup_[icount];
    int status = istup_[icount];
    int mom1id = abs(idup_[momup_[icount].first-1]);
    int mom2id = abs(idup_[momup_[icount].second-1]);
    double px = (pup_[icount])[0];
    double py = (pup_[icount])[1];
    double pt = sqrt(px*px+py*py);

    if(status==1 && (abs(PID)<6 || abs(PID)==21) && mom1id!=6 && mom1id!=24 && mom2id!=6 && mom2id!=24) { // gen HT used to bin samples does not count top/W decay products
      genHT += pt;
    }
  }

  std::auto_ptr<double > genHT_(new double(genHT));
  iEvent.put(genHT_, "genHT");
  
  // now get the gen jets
  std::vector<reco::GenJet> GenJets_;
    edm::Handle<edm::View<reco::GenJet> > GenJetsHandle;
  iEvent.getByLabel(GenJetsTag_, GenJetsHandle);
  if(GenJetsHandle.isValid())
    {
      for(unsigned int ijet=0; ijet<GenJetsHandle->size(); ++ijet)
	{
	  GenJets_.push_back(GenJetsHandle->at(ijet));
	}
    }

  const std::string s_GenJets("GenJets");
  std::auto_ptr<std::vector<reco::GenJet> > gjp(new std::vector<reco::GenJet>(GenJets_));
  iEvent.put(gjp,s_GenJets);
 
  

}

// ------------ method called once each job just before starting event loop  ------------
void
GenJetsProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenJetsProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
GenJetsProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GenJetsProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GenJetsProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GenJetsProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenJetsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenJetsProducer);
