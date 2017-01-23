import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/587B504D-79BE-E611-947E-0CC47A78A3E8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/64D66972-79BE-E611-88AA-0025905A60D6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A73948B-79BE-E611-9DAE-00266CFFC598.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90F504C3-79BE-E611-8300-02163E011512.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C8D12E80-79BE-E611-BEEC-047D7BD6DED2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DAF2FFB7-74BE-E611-AB7A-0CC47A4C8E38.root',
] )
