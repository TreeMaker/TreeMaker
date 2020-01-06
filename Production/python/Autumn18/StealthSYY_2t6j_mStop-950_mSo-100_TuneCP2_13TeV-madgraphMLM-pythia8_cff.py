import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/210000/D3F68103-B800-734E-AF4A-063404BE5F8E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1785168B-C42D-1547-BEBC-1596E1006079.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2BBE6EF7-B9BF-E848-A3CC-211D2CE445C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3F66E41B-CEC7-1749-8F98-A8E71F980882.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5FA6AEFD-5C51-2740-8929-49ED68DEC616.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/605695C5-3A5D-DD47-8CBA-37C92C6056C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/69DAAF86-40F0-534C-A25E-147AB2B38870.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7F28E5EF-64F4-064B-B0D6-904E8A38C630.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8B466A2B-D27D-1544-B47B-E52013A81F9F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9342A6A0-F332-2B4E-82BC-95B44A10CB73.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/97B915BC-3645-6E43-A109-C1B535A66281.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9F4815F1-2D03-C44E-AF78-74FA447833E8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A00F91F2-81F8-3144-BDFE-F3390E083876.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DC22AB3C-644C-F846-88E3-7E00EEFB5F12.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DFD60ECB-998A-D544-9B24-929A97E62CB2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E48C8B63-8ACB-D94E-AC9A-78EC55162522.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F284F8AA-1A67-9C4F-B179-F74DA638E990.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F77803AA-3810-6D4D-AC8F-8EDD37831E6E.root',
] )
