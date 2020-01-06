import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/10D2F308-20FC-E911-B165-B026283D4010.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/181BF7D3-1EFC-E911-A9A0-5065F37DA092.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/2058A22E-1FFC-E911-B94E-AC1F6B0DE294.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/283FF0D6-20FC-E911-80FF-0CC47A5FC285.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/3A94ED7E-1EFC-E911-9F7B-509A4C9EF923.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/3C8DECDE-1EFC-E911-9A4C-0CC47A74524E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/3EDD7EFE-29FC-E911-BA71-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/541FD967-22FC-E911-BBFC-A0369FF882EA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/640AA288-1FFC-E911-9A1B-FA163EDB8161.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/669ECCA4-1FFC-E911-87E1-44A842BECCBE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/6E60B33F-38FC-E911-A4E6-6C2B5999349F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/78525AD4-47FB-E911-9475-0023AEEEB703.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/8CE2F877-1FFC-E911-BE6E-20CF305B05BE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9AECD1B0-31FC-E911-BBC0-003048CB860C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A0F7B0DD-1EFC-E911-8620-0CC47A6C06C6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A8A9C036-1FFC-E911-AEDB-A4BF01159320.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AA359286-1FFC-E911-9F1E-00259090768E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/D0D3275A-1FFC-E911-83DF-485B3919F0B5.root',
] )
