// -*- C++ -*-
//
// Package:    Mt2Producer
// Class:      Mt2Producer
// 
/**\class Mt2Producer Mt2Producer.cc RA2Classic/Mt2Producer/src/Mt2Producer.cc

   Description: [one line class summary]

   Implementation:
   [Notes on implementation]
*/
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
// Translated from HeppyTools to EDProducer by Sam Bein, Jan 2016

#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "TLorentzVector.h"
#include "PhysicsTools/Heppy/interface/Davismt2.h"
#include "PhysicsTools/Heppy/interface/Hemisphere.h"
#include "PhysicsTools/Heppy/interface/ReclusterJets.h"
//
// class declaration
//

using namespace std;

class Mt2Producer : public edm::global::EDProducer<> {
public:
  explicit Mt2Producer(const edm::ParameterSet&);
  ~Mt2Producer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
      
  edm::InputTag MetTag_, JetTag_;
  edm::EDGetTokenT<reco::CandidateView> JetTok_;
  edm::EDGetTokenT<edm::View<pat::MET>> MetTok_;

  vector<TLorentzVector> getHemispheres(vector<TLorentzVector> jets) const;
  double getMT2Hemi(vector<TLorentzVector> jets, TLorentzVector metVec) const;
  double computeMT2(TLorentzVector visaVec, TLorentzVector visbVec, TLorentzVector metVec) const;
};

//
// constructors and destructor
//
Mt2Producer::Mt2Producer(const edm::ParameterSet& iConfig)
{
  //register your produc
  JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
  JetTok_ = consumes<reco::CandidateView>(JetTag_);

  MetTag_ = iConfig.getParameter<edm::InputTag> ("METTag");
  MetTok_ = consumes<edm::View<pat::MET>>(MetTag_);
  produces<double>("mt2");

}

Mt2Producer::~Mt2Producer()
{
}


//
// member functions
//


double Mt2Producer::computeMT2(TLorentzVector visaVec, TLorentzVector visbVec, TLorentzVector metVec) const
{  
  double metVector[3]={0,metVec.Px(),metVec.Py()};
  double visaVector[3]={0,visaVec.Px(),visaVec.Py()};
  double visbVector[3]={0,visbVec.Px(),visbVec.Py()};

  heppy::Davismt2 davismt2_;
  davismt2_.set_momenta(visaVector,visbVector,metVector);
  davismt2_.set_mn(0);
  return davismt2_.get_mt2();
}

double Mt2Producer::getMT2Hemi(vector<TLorentzVector> jets, TLorentzVector metVec) const {
  if(!(jets.size()>=2))
    {
      return -1;
    }
  vector<float> pxvec;
  vector<float> pyvec;
  vector<float> pzvec;
  vector<float> Evec;
  vector<int> grouping;
           
  for (unsigned int j=0; j< jets.size(); j++)
    {
      pxvec.push_back(jets[j].Px());
      pyvec.push_back(jets[j].Py());
      pzvec.push_back(jets[j].Pz());
      Evec.push_back(jets[j].E());
    }
  heppy::Hemisphere hemisphere(pxvec, pyvec, pzvec, Evec, 2, 3);
  grouping=hemisphere.getGrouping();

  float pseudoJet1px = 0;
  float pseudoJet1py = 0; 
  float pseudoJet1pz = 0;
  float pseudoJet1energy = 0; 
  float multPSJ1 = 0;
  float pseudoJet2px = 0; 
  float pseudoJet2py = 0; 
  float pseudoJet2pz = 0;
  float pseudoJet2energy = 0; 
  float multPSJ2 = 0;
                
  for(unsigned int index=0; index<pxvec.size();index++)
    {
      if(grouping[index]==1)
	{
	  pseudoJet1px += pxvec[index];
	  pseudoJet1py += pyvec[index];
	  pseudoJet1pz += pzvec[index];
	  pseudoJet1energy += Evec[index];
	  multPSJ1 += 1;
	    }
      if(grouping[index]==2)
	{
	  pseudoJet2px += pxvec[index];
	  pseudoJet2py += pyvec[index];
	  pseudoJet2pz += pzvec[index];
	  pseudoJet2energy += Evec[index];
	  multPSJ2 += 1;
	}
    }
  float pseudoJet1pt2 = pseudoJet1px*pseudoJet1px + pseudoJet1py*pseudoJet1py;
  float pseudoJet2pt2 = pseudoJet2px*pseudoJet2px + pseudoJet2py*pseudoJet2py;
  TLorentzVector tlv1; tlv1.SetPxPyPzE(pseudoJet1px,pseudoJet1py,pseudoJet1pz,pseudoJet1energy);
  TLorentzVector tlv2; tlv2.SetPxPyPzE(pseudoJet2px,pseudoJet2py,pseudoJet2pz,pseudoJet2energy);
  float mt2 = -1;
  if (pseudoJet1pt2 >= pseudoJet2pt2)
    mt2=computeMT2(tlv1,tlv2,metVec);
  else
    mt2=computeMT2(tlv2,tlv1,metVec);
  return mt2;
}

// ------------ method called to produce the data  ------------
void
Mt2Producer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;
  edm::Handle< reco::CandidateView > Jets;
  iEvent.getByToken(JetTok_,Jets);

  edm::Handle< edm::View<pat::MET> > Met;
  iEvent.getByToken(MetTok_,Met);
  TLorentzVector metvec;
  metvec.SetPtEtaPhiE(Met->at(0).p4().Pt(),Met->at(0).p4().Eta(),Met->at(0).p4().Phi(),Met->at(0).p4().E());

  std::vector<TLorentzVector > jets; 
  if( Jets.isValid() ) {
    for(unsigned int i=0; i<Jets->size();i++)
      {
	TLorentzVector jet;
	jet.SetPtEtaPhiE(Jets->at(i).p4().Pt(),Jets->at(i).p4().Eta(),Jets->at(i).p4().Phi(),Jets->at(i).p4().E());
	jets.push_back(jet);
      }
  }
  
  double Mt2 = getMT2Hemi( jets, metvec);
  
  auto Mt2Final = std::make_unique<double>(Mt2);
  iEvent.put(std::move(Mt2Final),"mt2");
 
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
Mt2Producer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(Mt2Producer);
