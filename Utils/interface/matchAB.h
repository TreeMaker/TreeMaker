#ifndef matchAB_h
#define matchAB_h

#include <vector>
#include <map>
#include <tuple>
#include <utility>
#include <unordered_set>

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"

namespace utils {
    template <typename A, typename B>
    inline double deltaRAB(const A& candA, const B& candB) {
		return reco::deltaR(candA,candB);
	}
    //overload for pointer case
    template <typename B>
    inline double deltaRAB(const reco::Candidate* candA, const B& candB) {
		return reco::deltaR(*candA,candB);
	}
	//use official JetMET matching procedure: equiv to set<DR,jet_index,gen_index> sorted by DR
	//from https://github.com/cms-jet/JetMETAnalysis/blob/master/JetUtilities/plugins/MatchRecToGen.cc
	//returns index array of length A pointing to B
    template <typename A, typename B>
    inline std::vector<int> matchAB(const A& collA, const B& collB) {
		std::map<double,std::pair<unsigned,unsigned>> matchMap;
		for(unsigned a = 0; a < collA.size(); ++a){
			for(unsigned b = 0; b < collB.size(); ++b){
				matchMap.emplace(std::piecewise_construct, std::forward_as_tuple(deltaRAB(collA[a],collB[b])), std::forward_as_tuple(a,b));
			}
		}
		
		std::vector<int> bIndex(collA.size(),-1);
		std::unordered_set<unsigned> a_used, b_used;
		for(const auto& matchItem: matchMap){
			unsigned a = matchItem.second.first;
			unsigned b = matchItem.second.second;
			if(a_used.find(a)==a_used.end() and b_used.find(b)==b_used.end()){
				bIndex[a] = b;
				a_used.insert(a);
				b_used.insert(b);
			}
		}
		
		return bIndex;
	}
}

#endif
