import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/3682E1C5-33F0-E811-8DBA-B499BAAC0572.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/BC2354DA-6CEF-E811-8EFB-0025905A60C6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/F49DF1A4-52EF-E811-98F5-0CC47A4D765E.root',
] )
