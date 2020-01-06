import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/C645F4FA-0806-EA11-A43B-0CC47A4D762E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/0A203ECE-5005-EA11-B4BD-0CC47A1E047C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/1221EDF7-5005-EA11-87C5-B083FED04D67.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/1C60594D-5005-EA11-8A3F-509A4C85BE75.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/506B5459-5005-EA11-9175-AC1F6BAC8178.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/509CC15B-5005-EA11-A7B0-0090FAA588B4.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/74EA27D8-5005-EA11-9F9B-B49691091EA2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/9C91A5CC-5005-EA11-856F-00259090822A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/E66C874D-5005-EA11-AB1C-0025905D1E0A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1150_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/F87880F9-5005-EA11-9CE8-0CC47A703326.root',
] )
