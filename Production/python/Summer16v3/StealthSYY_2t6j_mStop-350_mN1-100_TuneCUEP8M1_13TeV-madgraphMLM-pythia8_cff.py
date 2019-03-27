import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/12E7508E-B0F0-E811-B635-0CC47AFCC68A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/223D9A51-C0F0-E811-8D7D-0CC47AF9B2F2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/325564B7-B8F0-E811-BC45-0025904C516E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/6673C648-B4F0-E811-AA12-0025905D1E02.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A4F7F3BD-B8F0-E811-8BE6-0025905C54F4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A645012F-CCF0-E811-89F6-0025904CDDFA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/CAAD1A5D-ADF0-E811-A7C3-0CC47AFCC3FE.root',
] )
