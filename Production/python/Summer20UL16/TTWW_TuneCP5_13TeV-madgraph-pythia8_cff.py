import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/06FD5E92-F6C5-AA4E-83AD-54B0A6501157.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/0BF033FC-5D4D-664F-B92F-8F1E4A149C8F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/12134CA3-D09E-8941-BF98-4E436794E485.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/12B35428-F6ED-7D4B-877D-39EE4CEB1790.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/1E51AEC5-8BA3-8A44-A684-D3790A3CB985.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/229ADD88-D60E-F548-BD5B-8F13105020AB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/380DC24B-9061-E047-B95A-34BC02AC3171.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/549C1539-36D9-B048-9C1A-0DD487DD92D0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/6F54F49F-92AA-DC42-B01D-AE403ED06C6B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/7CE9914A-8E50-3947-9874-269C5B6336E8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/878BB157-F142-C64A-9C30-F608CEC0FB83.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/A24E3F7E-E140-D545-BD43-54843FC68B29.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/A7BE5173-3BF9-2542-920B-64B3D6058DFD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/B2A37DFD-9E10-DC47-A5D7-9CF726FC1E41.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/C9708831-884C-6C42-BFCB-49C11E4977FD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/CAA87976-411F-444D-8FB1-CB7219F6A1ED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/CB2946E6-8D33-A54A-91D9-1664A725E700.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/D933296F-AD85-784C-830E-2674B9930669.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/DE183756-5401-AD43-86D5-F243717159F5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/1BF3212A-A488-A94E-A373-25A1CBA140E3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/796B5D92-2714-0645-922A-3E517EAB3100.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/CCDCAFDD-8245-1442-A0A7-38EBE4E3E144.root',
] )
