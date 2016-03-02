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

class CandPtrPrefer : public edm::EDProducer{
  public:
    explicit CandPtrPrefer(const edm::ParameterSet & iConfig);
    ~CandPtrPrefer();

    virtual void produce(edm::Event & iEvent, const edm::EventSetup& iSetup) override;
    virtual void endJob() override;

  private:
    edm::EDGetTokenT<edm::View<reco::Candidate> > firstSrcToken_;
    edm::EDGetTokenT<edm::View<reco::Candidate> > secondSrcToken_;
};

CandPtrPrefer::CandPtrPrefer(const edm::ParameterSet & iConfig):
  firstSrcToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("first"))),
  secondSrcToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("second")))
{
  produces<edm::PtrVector<reco::Candidate> >();
}

CandPtrPrefer::~CandPtrPrefer()
{
}

void
CandPtrPrefer::produce(edm::Event & iEvent, const edm::EventSetup & iSetup)
{
  using namespace edm;
  Handle<View<reco::Candidate> > firstGroup;
  iEvent.getByToken(firstSrcToken_, firstGroup);
  Handle<View<reco::Candidate> > secondGroup;
  iEvent.getByToken(secondSrcToken_, secondGroup);

  std::auto_ptr<PtrVector<reco::Candidate> > result(new PtrVector<reco::Candidate>());
  if(firstGroup->size()==0){
    for(size_t i = 0; i< secondGroup->size();  ++i) {
        result->push_back(secondGroup->ptrAt(i));
    }  
  }
  else {
    for(size_t i = 0; i< firstGroup->size();  ++i) {
        result->push_back(firstGroup->ptrAt(i));
    }
  }
  iEvent.put(result);
}

void CandPtrPrefer::endJob()
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CandPtrPrefer);
