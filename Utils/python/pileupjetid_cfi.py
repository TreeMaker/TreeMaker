from RecoJets.JetProducers.PileupJetID_cfi import pileupJetId
from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL16
from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL16APV
from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL17
from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL18
import FWCore.ParameterSet.Config as cms


pileupjetalgos={
    "2016UL" : _chsalgos_106X_UL16,
    "2016UL_APV" : _chsalgos_106X_UL16APV,
    "2017UL" : _chsalgos_106X_UL17,
    "2018UL" : _chsalgos_106X_UL18
}
