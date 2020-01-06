import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0827AE07-CB04-EA11-90B3-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/22209B49-CA04-EA11-AA37-008CFA166014.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3EC1A8A1-CA04-EA11-B8C1-48D539F3840E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3ECF4A97-CA04-EA11-930A-0CC47AC1750C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/4EBB3736-CA04-EA11-BFCC-0025905D1D78.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5E668799-CA04-EA11-92CE-0025901D08D8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/7A6E3C43-CA04-EA11-A04C-246E96D149C4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/7C068588-CA04-EA11-BB9D-5065F37D9171.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/92AC8D37-CA04-EA11-A2EF-7CD30AD08EA8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B633DC42-CA04-EA11-9DF7-AC1F6BC67D50.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/BA590351-CA04-EA11-A4BD-C81F66C8BA4C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C0E5C84E-CA04-EA11-A6A2-C45444922B77.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/CEF3BA40-CA04-EA11-914F-00266CFBE43C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DA11C5FC-CA04-EA11-A2DC-FA163E771E04.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DA2AE302-CA04-EA11-B3DD-AC1F6BAC7ACC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E8EDBE91-CA04-EA11-B5C3-001E675A68BF.root',
] )
