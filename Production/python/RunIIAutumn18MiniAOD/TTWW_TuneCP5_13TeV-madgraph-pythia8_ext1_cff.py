import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/2F5EA2EA-BE26-6F4F-8CF6-9CED3E0BC9FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/5F6CFC20-B11D-8D4C-B5B7-C0D3AA1AF723.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/81EE4D38-D502-C343-B8F5-5048C1C45527.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/93AE241C-DCD4-4B4A-A446-92127524E3E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/9C713CF7-F82C-5B48-8A4F-B25C43668DAD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/AD8F30B9-C8BE-1246-A46E-3EA76665D4F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/AE93D8C1-1C43-5E4F-B64B-E300E1A7A5AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/BB7AFFF1-B864-9041-88E4-0F80C0E35745.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/D668F276-9381-C246-BF2B-66F5FD3456AF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/F45E8AB1-8A62-F545-8329-7F1DC0591B7A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/80000/FD941594-979C-2C4B-B179-B7E027FE8057.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/1AF023CF-5117-F149-AECB-731A281D28A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/1BA2DE67-00D4-D24E-A7B5-60EAE5CDFE1A.root',
] )
