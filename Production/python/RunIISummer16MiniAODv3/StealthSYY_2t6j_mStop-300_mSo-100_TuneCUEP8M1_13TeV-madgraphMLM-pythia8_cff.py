import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/22123AF3-BEEF-E811-B301-48D539F38882.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/2620B573-ACEF-E811-B604-AC1F6B0DE228.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/5A9754E7-98EF-E811-8C2A-48FD8E069B81.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/683B1292-CEEF-E811-91B2-346AC29F11B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/AC55288A-BCEF-E811-A02B-48D539F38410.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/C862687A-B8EF-E811-B9BF-48FD8E28248B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/E20634C0-C0EF-E811-8168-AC1F6B0DE2F4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/FCD5A44B-A9EF-E811-A9D8-48FD8EE73A81.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/FE16CB76-ABEF-E811-A87B-A0369FE2C1B0.root',
] )
