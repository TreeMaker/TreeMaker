import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/97CF62B7-13A7-1144-9021-CDF16708F4B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/0DC1264B-98DD-054D-934F-B46D16AEA2DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/2C2BC671-C18E-FF47-947E-B293CD33BEE2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/2CB0A228-DDDD-0946-A030-6B0ED1F50B8A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/626CC6DD-7373-0A44-99B0-933D20F1088D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/6F7C5F93-53F0-AE45-BA6B-A95CCDCBD59A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/7E24A0DA-B32D-5D44-BAF0-7AE8C465D170.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/8FD11F87-C024-1042-A459-FCFDC8445277.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/92CF84BB-1255-3243-9E69-C4C05B8922D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/9CBFC750-9804-CF47-8FB7-9C862D1137F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/E0CDD379-4CDE-2E4C-8014-F9573A6E9943.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/ED4F9CB6-82B7-054D-A20A-254A0AF0FED3.root',
] )
