#ifndef mht_h
#define mht_h

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

namespace utils {
	//for MHT calculation
	inline reco::MET::LorentzVector calculateMHT(const edm::View<reco::Candidate>* Jets){
		reco::MET::LorentzVector mhtLorentz(0,0,0,0);
		for(unsigned i = 0; i < Jets->size(); ++i){
			mhtLorentz -= Jets->at(i).p4();
		}
		return mhtLorentz;
	}
}

#endif
