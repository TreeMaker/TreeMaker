import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/70F5A081-4E0B-EA11-9E02-002590907832.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/044EECF4-2709-EA11-8563-AC1F6B4E0148.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/106AB393-3009-EA11-93B7-C4346BC8D390.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/127B3CE6-1409-EA11-B468-20CF3027A6C6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/128E82B0-0F09-EA11-B04C-B083FECFD4F0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/160E04D0-0BF7-E911-830D-506B4BB16ADE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/180EE098-CCF8-E911-AC94-003048F7CC8A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1EB8B595-3E09-EA11-BC69-509A4C85400A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/32A1AB6E-3B09-EA11-A980-B499BAABFEB0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/32CCBE0E-D3F7-E911-B7C9-0CC47A2AED04.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/44176404-A208-EA11-A00F-0025905B85C0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5E5E97D2-1B09-EA11-BD20-7CD30AC030B4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/685C1D81-95F8-E911-8DDE-1866DA85DACC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/76CB11F4-DEF7-E911-8953-E0071B7A48A0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/784F94C5-3909-EA11-BF3D-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/8E364B0E-1F09-EA11-821A-008CFAC94020.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/948D21DB-1409-EA11-8D06-588A5AAEEBB8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9C4982BE-3909-EA11-B8F1-1866DAEA79A4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9C7B7D3A-7EF8-E911-9D32-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/AC71C282-3909-EA11-A391-509A4C748095.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BA3A6DF1-1109-EA11-BEC5-FA163E7ECC92.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C817E345-1B09-EA11-8D9D-5065F381C2A2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D08DF180-B0F7-E911-89F1-F01FAFD9C64C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DAA46129-1A09-EA11-877F-782BCB3BDD3B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DAE2E9E1-3B09-EA11-8350-0242AC1C0506.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E25FF0CB-3909-EA11-8D46-0CC47A5450FA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F085E27B-6AF8-E911-ACCB-008CFAEBDA78.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/FE8A3670-6F10-EA11-8C34-D4AE5280690B.root',
] )
