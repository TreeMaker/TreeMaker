import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/1308DF6D-A730-3740-97E5-773522791C27.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/16977E5F-3412-E845-B8BE-82D3DFA08FFB.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/1DD14408-A6FF-BA4D-87A5-403E9433C6EF.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/55ADD529-2798-2C41-A7DF-79914FB24BBA.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/829CED7D-6CE1-2644-A069-FCCF94F982F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/8ABFDE4A-A9BA-514C-ADFD-6E1FBD5EA410.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/93BA0E7C-04D0-8C47-9900-8424E1F06B85.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/D4DEC3DA-7269-384F-8530-5768AFF56868.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/D8858571-AEBA-F946-9F60-1B0F5DC48AD7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/EBB5C353-CBA9-8C46-9F33-5CAE9100EB1A.root',
] )
