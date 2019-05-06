import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/05BC82C7-E349-254E-9DC3-6122B89C1781.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/2443B184-9366-0F49-B53E-74CEF4B79CC4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/3309028F-6E00-9545-9550-681383CE93DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/46287C62-D3FA-D543-A596-EDAECD38AC3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/5368B9E9-DC23-4141-AA85-CFFBC4129C5A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/6FD94E6A-F4CF-7C44-A334-9673BBFE23CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/9B684AF9-569E-134E-8206-C737B7419D13.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/9D9778CE-E575-DC40-BE5D-B47B10A3BB4B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/A7DF7393-11D5-274E-9B09-02FBE699FE7A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/C4BDCCA4-A2E7-464D-9590-37A495EC0694.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/CF2C0407-0ECC-B244-B309-DAEECF3B28BA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/D8416D01-74F7-E34C-BECB-33AE67634663.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/EEFA4609-9B52-2441-B375-C54ABF2C2B52.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/F7CB1BF7-F282-6142-8B85-54A0026649E8.root',
] )
