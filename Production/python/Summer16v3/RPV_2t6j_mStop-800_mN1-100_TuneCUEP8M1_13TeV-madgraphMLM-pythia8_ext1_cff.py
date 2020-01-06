import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/240000/56596803-FC06-EA11-AFDF-EC0D9A0B3360.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/240000/864F63CE-FB06-EA11-B747-FA163E025578.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/240000/B69F023B-FC06-EA11-A648-6C2B598FF837.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/240000/F8FB710A-FC06-EA11-A364-A0369FD0B170.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/240000/FEC53710-FC06-EA11-A335-F01FAFE5F8C5.root',
] )
