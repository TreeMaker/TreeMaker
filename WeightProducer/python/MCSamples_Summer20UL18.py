import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL18
Summer20UL18samples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v11_L1v1-v2', 'RunIISummer20UL18MiniAOD', 'Constant', 347426000, False),
]
