import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0EEA1F92-A879-744A-892A-C15738D31546.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/174458B4-1069-5940-BF32-A50419E27A0E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1E33E939-8FC3-CE40-9112-CE2B6E8E71DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3355AEA6-D4FE-FD46-9DE3-56CFC05A81D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/45532711-C902-4F47-8EC5-146BD2ABADB9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6368501B-252A-714C-B1D9-7F56DE09F90C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7751B922-D940-E247-A2DF-232C02735B5D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/81B4AB0C-590F-9248-87EE-F6C85AC23456.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/89E8FBEE-01AF-5545-87EE-5A8D45B073CD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8EB7B1A0-B35F-6343-ACE9-489DF555E4AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/92A0E946-61DF-0B40-AD66-1FE003569F05.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/97D5EFFF-6504-374D-9CE9-04551B510CAD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/ABC49A2C-3040-4C4D-A745-D86F204BCCBB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AE3338D0-2707-A84A-8749-38E8298948E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AE40C891-0C62-1943-AA8C-30AAD4D58A98.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B5D7E93C-FAF6-7A40-A197-499592C3B5B2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/BE2C8087-C4D1-784E-8636-00B7C514945E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C69FB006-41FA-284E-8430-109EFC4A6B56.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CB5F6C41-3C94-C148-AF7F-37E2E81BD180.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D87C41B4-B16A-7B4A-81B1-FD29E6A3B88A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E6DC2F88-D9F3-CD4D-964B-36B90730117C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/FD888D91-5776-464C-8655-7DD65B3E116A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/22352DB4-1B8D-9147-8308-D98435664D87.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/5062E7AA-6322-4441-9A24-BDE5DD41316B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/5448350C-EBAE-4C4B-B87C-1D5AC0BE4A99.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/735B5BCF-0CA8-EB43-A0BC-3608EAED35EB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/7511831A-D6AF-044F-9CE8-D39B9504E76A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/8EE2D502-8CC1-6D4C-85EB-0D49C426DAEF.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/B25FD10A-FD73-184F-94B7-BDE63E2A7F1E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/BF806281-E83D-9F47-84B4-59A2122E1C94.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/D8429A16-7CC0-804C-8633-98CB51F7365A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/DF9BE55A-6E4D-CA4D-ABF6-E3A88F3E2A32.root',
] )
