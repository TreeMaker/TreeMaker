#include <vector>
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/Wrapper.h"
#include "DataFormats/Common/interface/PtrVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/Point3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

namespace {
  struct dictionary {
    std::vector<math::PtEtaPhiELorentzVector> vlv;
    std::vector<math::XYZVector> vxyzv;
    std::vector<math::XYZPoint> vxyzp;
    std::vector<pat::Jet> vpj;
    std::vector<std::vector<math::PtEtaPhiELorentzVector> > vvlv;
    std::vector<std::vector<pat::Jet> > vvpj;
    std::vector<std::vector<bool> > vvb;
	edm::PtrVector<pat::PackedCandidate> rv2pp;
    edm::Wrapper<std::vector<std::vector<math::PtEtaPhiELorentzVector> > > wvvlv;
    edm::Wrapper<std::vector<std::vector<double> > > wvvd;
    edm::Wrapper<std::vector<std::vector<bool> > > wvvb;
	edm::Wrapper<edm::PtrVector<pat::PackedCandidate> > wrv2pp;
  };
}
