#include <vector>
#include "TLorentzVector.h"
#include <DataFormats/PatCandidates/interface/Jet.h>
#include "DataFormats/Common/interface/Wrapper.h"

namespace {
  struct dictionary {
    std::vector<TLorentzVector> vlv;
    std::vector<pat::Jet> vpj;
    std::vector<std::vector<TLorentzVector> > vvlv;
    std::vector<std::vector<pat::Jet> > vvpj;
    edm::Wrapper<std::vector<TLorentzVector> > wvlv;
    edm::Wrapper<std::vector<std::vector<TLorentzVector> > > wvvlv;
  };
}
