//
//

/**
*/

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/RefToBaseVector.h"
#include "DataFormats/Common/interface/PtrVector.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

class PackedCandPtrProjector : public edm::EDProducer{
  public:
    explicit PackedCandPtrProjector(const edm::ParameterSet & iConfig);
    ~PackedCandPtrProjector();

    virtual void produce(edm::Event & iEvent, const edm::EventSetup& iSetup) override;
    virtual void endJob() override;

  private:
    edm::EDGetTokenT<edm::View<pat::PackedCandidate> > packedCandSrcToken_;
    edm::EDGetTokenT<edm::View<reco::Candidate> > candSrcToken_;
    edm::EDGetTokenT<edm::View<reco::Candidate> > vetoSrcToken_;
};

PackedCandPtrProjector::PackedCandPtrProjector(const edm::ParameterSet & iConfig):
  packedCandSrcToken_(consumes<edm::View<pat::PackedCandidate> >(iConfig.getParameter<edm::InputTag>("src"))),
  candSrcToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("src"))),
  vetoSrcToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("veto")))
{
  produces<edm::PtrVector<pat::PackedCandidate> >();
}

PackedCandPtrProjector::~PackedCandPtrProjector()
{
}

void
PackedCandPtrProjector::produce(edm::Event & iEvent, const edm::EventSetup & iSetup)
{
  using namespace edm;
  Handle<View<pat::PackedCandidate> > packedCands;
  iEvent.getByToken(packedCandSrcToken_, packedCands);
  Handle<View<reco::Candidate> > cands;
  iEvent.getByToken(candSrcToken_, cands);
  Handle<View<reco::Candidate> > vetos;
  iEvent.getByToken(vetoSrcToken_, vetos);

  std::auto_ptr<PtrVector<pat::PackedCandidate> > result(new PtrVector<pat::PackedCandidate>());
  std::set<reco::CandidatePtr> vetoedPtrs;
  for(size_t i = 0; i< vetos->size();  ++i) {
   for(size_t j=0,n=(*vetos)[i].numberOfSourceCandidatePtrs(); j<n;j++ )    {
     vetoedPtrs.insert((*vetos)[i].sourceCandidatePtr(j));   
  }
  }
 for(size_t i = 0; i< cands->size();  ++i) {
    reco::CandidatePtr c = cands->ptrAt(i);
    if(vetoedPtrs.find(c)==vetoedPtrs.end())
    {
      result->push_back(packedCands->ptrAt(i));
    }
  }
  iEvent.put(result);
}

void PackedCandPtrProjector::endJob()
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PackedCandPtrProjector);
