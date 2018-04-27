#ifndef mht_h
#define mht_h

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

namespace utils {
	//for MHT calculation
	inline reco::MET::LorentzVector calculateMHT(const edm::View<reco::Candidate>* Jets){
		reco::MET::LorentzVector mhtLorentz(0,0,0,0);
		for(const auto & Jet : *Jets){
			mhtLorentz -= Jet.p4();
		}
		return mhtLorentz;
	}
}

#endif
