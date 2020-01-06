import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/02FC78DD-D8F5-E911-8DE2-FA163E90BACF.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/16169860-71F6-E911-B31E-00266CFFBF84.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3C71D55B-71F6-E911-8495-A4BF01125D96.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B6A7BA57-71F6-E911-8E4D-0025905C94D2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/CA66B95D-71F6-E911-84AD-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E033D2CF-71F6-E911-817B-48D539F38866.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/EAB77B6B-71F6-E911-859D-509A4C854019.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FAD4E46B-71F6-E911-BC96-0CC47A78A42E.root',
] )
