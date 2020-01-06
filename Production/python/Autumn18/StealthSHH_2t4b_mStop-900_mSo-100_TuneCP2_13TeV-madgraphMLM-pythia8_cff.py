import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1E9D617C-C63B-D646-B5D4-0D79B3276FC7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4966A041-8FB3-4844-947B-80DA35F1AA06.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5CC71FD9-E36C-BB4B-8581-2FE0F6CBE72F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6941923D-5EC4-0647-A087-DF0EB660011F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7F3495A3-97D9-D240-B33F-15DFB3E37C3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/97ED43DE-561E-0548-A565-281DB049D2E1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AC7A03F8-23C7-564C-9A71-9990BA5EE794.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B3F31A7E-D9C5-284F-A4F6-47735A9F5930.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CE6187D2-B761-454A-B6E9-1B8BB7CAEBD5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D587EFB1-6141-EF4B-A3FB-7F082225531B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E56DA2B4-35B0-7246-A8E1-A9EB9C876818.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/ED3039D9-4D59-8747-A9D3-481F866265F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/FD5A731E-5D48-034A-8DBB-A6CCDB7B37AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/4B346FE8-0CFD-084B-9897-029B748CD250.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/54D8CAF0-700D-0046-9A6E-B005618E7DB1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/62480502-D708-FD4A-9522-6CB86FEB042A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/62F85457-CF56-4342-A30E-0D95DD616932.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/65BB52B6-6A14-6147-B28F-2B6C69AF40C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/6623C7C7-0652-DC4B-80E3-ECDBEAA4AC51.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/7D81EF53-899E-A247-B7F9-221BEB52360F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/8F3696C2-E971-5345-8F96-053443A82C1F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/91FF96FC-9709-7748-8B3A-A03DE702C764.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/F0318027-BF52-6D4B-A21A-FA75EA1AB6E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/FA862781-DF4F-3E47-BB85-EF06DE01C66A.root',
] )
