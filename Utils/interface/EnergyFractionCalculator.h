#ifndef EnergyFractionCalculator_h
#define EnergyFractionCalculator_h

#include "DataFormats/PatCandidates/interface/Jet.h"

class EnergyFractionCalculator {
	public:
		//constructor
		EnergyFractionCalculator(const pat::Jet& jet) : jet_(jet) {
			rawEnergy_ = jet_.energy();
			if(jet_.jecSetsAvailable()) rawEnergy_ *= jet_.jecFactor(0);
			if(jet_.hasUserFloat("jerFactor")) rawEnergy_ /= jet_.userFloat("jerFactor");
			rawEnergyInv_ = 1./rawEnergy_;
		}

		//accessors
		float rawEnergy() const { return rawEnergy_; }
		float chargedHadronEnergyFraction() const { return jet_.chargedHadronEnergy()*rawEnergyInv_; }
		float neutralHadronEnergyFraction() const { return jet_.neutralHadronEnergy()*rawEnergyInv_; }
		float chargedEmEnergyFraction() const { return jet_.chargedEmEnergy()*rawEnergyInv_; }
		float neutralEmEnergyFraction() const { return jet_.neutralEmEnergy()*rawEnergyInv_; }
		float photonEnergyFraction() const { return jet_.photonEnergy()*rawEnergyInv_; }
		float electronEnergyFraction() const { return jet_.electronEnergy()*rawEnergyInv_; }
		float muonEnergyFraction() const { return jet_.muonEnergy()*rawEnergyInv_; }
		float HFHadronEnergyFraction() const { return jet_.HFHadronEnergy()*rawEnergyInv_; }
		float HFEMEnergyFraction() const { return jet_.HFEMEnergy()*rawEnergyInv_; }
		float chargedMuEnergyFraction() const { return jet_.chargedMuEnergy()*rawEnergyInv_; }
		float hoEnergyFraction() const { return jet_.hoEnergy()*rawEnergyInv_; }

	private:
		//members
		const pat::Jet& jet_;
		float rawEnergy_, rawEnergyInv_;
};

#endif
