import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/160C3AF0-68D5-E611-998F-A0369F310374.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5825E6ED-68D5-E611-815C-00259074AE9A.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5A07ADDE-68D5-E611-98C7-1866DAEB5D80.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/70C517FA-68D5-E611-9BCE-0025905A60D2.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/84E2BC05-69D5-E611-A1B2-00266CFFA750.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/84E2E9EC-68D5-E611-883A-6CC2173BC2E0.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/887AA800-69D5-E611-82AE-0025905A60BE.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D0BB5AE3-68D5-E611-9609-02163E013726.root' ] );


secFiles.extend( [
               ] )
