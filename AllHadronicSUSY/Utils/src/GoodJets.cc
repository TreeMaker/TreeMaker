#include "DataFormats/PatCandidates/interface/Jet.h"
class GoodJets{
//bool isGood_;
public:
GoodJets(const pat::Jet& aJet){
isGood_=false;
        float neufrac=aJet.neutralHadronEnergyFraction();//gives raw energy in the denominator
        float phofrac=aJet.neutralEmEnergyFraction();//gives raw energy in the denominator
        float chgfrac=aJet.chargedHadronEnergyFraction();
        float chgEMfrac=aJet.chargedEmEnergyFraction();
        float muFrac=aJet.muonEnergyFraction();
        unsigned int nconstit=aJet.nConstituents();
        int chgmulti=aJet.chargedHadronMultiplicity();
      	if(muFrac<0.99 && nconstit>1 && neufrac<0.99 && phofrac<0.99 &&chgmulti>0 && chgfrac>0 && chgEMfrac<0.99)isGood_=true;
};
bool isGood(){return isGood_;};
private:
bool isGood_;
};

