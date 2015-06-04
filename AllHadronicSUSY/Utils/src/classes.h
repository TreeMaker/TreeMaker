#include <vector>
#include "TLorentzVector.h"
#include "DataFormats/Common/interface/Wrapper.h"

namespace { 
  struct dictionary {

    std::vector<TLorentzVector> vt;
    edm::Wrapper<std::vector<TLorentzVector> > wvt;
    std::vector<std::vector<TLorentzVector> > vtt;
    edm::Wrapper<std::vector<std::vector<TLorentzVector> > > wvtt;

  };
}
