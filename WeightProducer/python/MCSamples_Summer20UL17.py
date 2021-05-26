import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL17
Summer20UL17samples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v6-v2', 'RunIISummer20UL17MiniAOD', 'Constant', 249603999, False),
]
