import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL16
Summer20UL16samples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v13-v2', 'RunIISummer20UL16MiniAOD', 'Constant', 112592000, False),
]
