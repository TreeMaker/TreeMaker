import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/022CA56A-A1F8-E911-936F-AC1F6B23C82E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/08F35C65-C2F8-E911-9FD8-AC1F6B23C77C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/0E69548F-E70D-EA11-9AD1-E0071B749C40.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/22DC498C-1B0B-EA11-BA18-0025905A60A0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/26889AF9-8D0C-EA11-B572-0025905A48E4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/3647B65D-E80D-EA11-86AE-0026B9278637.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/429B9671-67F9-E911-B644-0CC47AE0F33C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/44B687D8-E70D-EA11-87A0-0CC47A4DEEA2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/464B3863-E80D-EA11-91D0-6CC2173D44D0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/566B949B-E70D-EA11-BCCE-0025901D0948.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5E0372CD-37FA-E911-85AF-0CC47AB6503E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5EA21CF3-13FA-E911-823F-003048F5ADEE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/68321711-CCF8-E911-8E5F-AC1F6B23C806.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6CE7874B-1B09-EA11-B48E-0CC47A4C8F2C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6EC08ECA-9708-EA11-982D-0CC47A7C34C8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/7832123E-E80D-EA11-9B25-001E67F33348.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/7CCFD971-8DF9-E911-B84C-0025905C3D40.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/8C5871D1-F20D-EA11-8EAD-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/A6C8993D-E80D-EA11-854C-506B4BF38278.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B09AEB55-E80D-EA11-99A8-002590907812.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B2EC8954-E80D-EA11-BADE-B083FED1321B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B40B4B64-E70D-EA11-A7C7-FA163E550778.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B4DC6AAA-E70D-EA11-8AD0-0025901AEDA4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B6CC3825-8E09-EA11-BED4-E0071B691B81.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C2C661D4-E70D-EA11-90F4-0242AC1C0507.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D2AC6421-5D07-EA11-9814-0CC47A4D7606.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D6CC82F7-ABFA-E911-B4C0-0CC47AFF0454.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DAA79C8C-E70D-EA11-BBC2-20040FE9C7DC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DC9D379A-E70D-EA11-9E14-0025905B858C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E8C0FEF2-B2F8-E911-874F-0025904CFB88.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/EA69825B-0CF9-E911-B174-48FD8E28297D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/ECCEAB81-A404-EA11-AD55-6C3BE5B58198.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/EE0A9DA0-0BFA-E911-A4DE-AC1F6B0DE2EA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F89F6FC6-E70D-EA11-96F1-0025905C2CA6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/FABC9053-E80D-EA11-BE42-A0369FC5B848.root',
] )
