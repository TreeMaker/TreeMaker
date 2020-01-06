import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0A04766F-DAF6-F44F-9E70-7650A55D9DF6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/15779BA4-E3A6-8345-AE7F-0C7B6E3114CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2F516AB5-56EB-884D-8E8C-564A3F123640.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/301A1001-FDB8-3748-AC2B-7E9D9BC23DD3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4D217104-E024-804A-81AE-64F59A85F833.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5138DDBC-5538-9145-808B-811551AE9178.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/56911F29-1784-1447-A930-22D9452084E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/624D6962-724A-4D46-86EC-9EA3F9391F43.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/698A0141-3D25-FA41-8CF0-B2FD9C59D0E5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/86763A07-FE98-3F4B-8A6E-D79777A211FC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8FEC416D-3336-BF4D-83B9-DF1ED6023246.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9730EC47-0158-084E-987A-AFF815D40EF4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A762A440-F7F6-FD42-AABF-CF3161C7E728.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F4288E96-4526-4C46-BBBD-EEAD6AD6168C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F56DBCC2-700B-DD41-9A3A-87170FB17244.root',
] )
