import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL16APV
Summer20UL16APVsamples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v8-v2', 'RunIISummer20UL16MiniAODAPV', 'Constant', 98093000, False),
]
