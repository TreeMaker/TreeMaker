import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/0201980B-5E67-6644-92BE-64A4957A9F68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/05644786-09B5-1D4C-81A8-43A8E412BA1C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/05F331AA-F59F-1A41-BAF1-F9E21A2A902E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/338E139D-98DC-2546-96F7-7E585ABE670F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/48054E60-5B33-BD47-BDB7-8905E9CD0693.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/6CA1015A-0264-D74E-92DD-1D59D131929F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/6CEEE926-A219-2341-BE99-6BCDE6058E90.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/6E0B2F5B-A38C-F841-86B0-089D177F46FF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/70248D7F-68A7-304C-8767-5BA5E600CC27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/702DA8A8-FA02-DE45-A963-CB3A2CA710C6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/76DD3E42-76E8-8342-B582-835163DBC9BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/79B7FDC7-0AF3-1F44-B4B4-72ED2227C055.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/89E4C8AF-E806-BC4D-8C02-AB822F794682.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/8BA8C3B5-0101-CF42-BB1D-3D9C38B5652C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/98C665D5-6A43-184E-BE6D-5201194B2591.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/A2CB581A-088F-C04B-A283-BC222C309F19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/AD3493CD-7BBC-0744-B130-21FA5D6A0821.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/B68BB991-720F-9F4C-90C0-A55A8D022A13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/BBC75686-1D06-B042-A2B3-F0A3018C1F18.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/C87CA3B8-20AA-8E49-A7F1-5AA8C4EC1B1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/CAB6AEF6-F543-4840-903E-0B7C7E2D92E5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/D0D8378C-4ABF-F242-A01F-3BBD6C50521C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/E82B7FD0-A0F2-1844-9F46-49B5FC701F7B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/ECAE6DA1-81CD-2C42-AF8C-66CB9D88779E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/2810000/EFA31B4F-0191-124A-8B96-E337F7F17C51.root',
] )
