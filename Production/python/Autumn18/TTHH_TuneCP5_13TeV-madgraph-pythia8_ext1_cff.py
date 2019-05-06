import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/19BED0B8-1244-E445-A82B-0E7285F924D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/1A9A75EC-0A4B-244D-BBAF-D13C31C66EC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/335278F5-4C4A-2245-8693-AD659FB2BD77.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/38F7F09D-F616-6044-BCFF-17EFF08B5814.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/500C45C4-E449-F342-B686-3A8FB481B4B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/88E3E77A-116A-FA4A-AF56-DFE53BB1A87D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/A69FE108-77FD-0F49-8B1B-9494F12FEA15.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/B419AF7B-9800-4549-B17D-F2B3E3F8F629.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/D959577E-042B-504A-B706-62CFBF1F7801.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/1FC83BB1-8235-0548-B1F5-3ED6A9995B7C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/80000/5470D6FF-AB09-E046-B935-760784DFB695.root',
] )
