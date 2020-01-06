import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/07306712-1E1A-C345-8192-1F2DA45A575E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2B9162CC-DF76-FE4A-810C-5183E38E1BD7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2C48681B-18A0-E24D-8591-213E5D119D93.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3374E720-22DA-C447-91B2-B652B7D250B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/357C56E4-ACD6-F545-9CC5-47F205F88935.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/53E221D4-F7B5-574D-95C3-6479F3E43760.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7EBCCB12-2078-8E4A-9335-344B421B73E8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9005B7B0-6342-F340-AD43-F14F7FE98D49.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/962AA0F4-8935-5B47-8AE1-A5A7E3449ABC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AF080DFA-DFAB-6A4A-A4DB-C6A21E4403A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B1A77C96-C58D-F94C-A1E9-4EED379317B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B2157A1E-2E85-D54C-9252-434D71F4A6BD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C567EC28-E8A3-9848-8276-EE6779218B3A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CA6B4639-62CF-274F-A26D-C02E4D66895A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/EF232EC7-69AA-EE4A-8358-889BD1088334.root',
] )
