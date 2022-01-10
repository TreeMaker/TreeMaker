import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/5BDD19E9-5FDE-2F4D-8270-616DB4C2B67E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/E26B36A4-B730-5E45-BE55-127D03A43A4C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/FAB1B0AA-5F87-9B4E-BCD0-ED7C1A9926F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/03F506DC-FBBD-3D4B-B053-389B4C1EC966.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/359FDE39-1083-144F-92E7-F94B7B20D719.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/B4DDC7F0-8050-534B-B3F9-C8CA3D9ED8D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/1A89A15C-8C6A-3743-98B2-908DA0AD9ECA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/27F6FEEB-397B-2F42-98ED-B4C825723C35.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/82282D4D-F7FB-2B49-8E7E-63E8F1D505AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/90EFDB69-D944-9E42-81F4-F222A62073C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/B11D02E5-1AF9-CE4A-8066-47B226A83B38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/CA228D19-F2A0-7A45-B73A-D526E8920DF0.root',
] )
