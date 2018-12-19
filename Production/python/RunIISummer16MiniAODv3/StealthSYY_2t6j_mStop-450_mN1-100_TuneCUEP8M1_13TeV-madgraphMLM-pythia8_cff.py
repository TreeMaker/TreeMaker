import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/1EEF8238-71EF-E811-80FD-008CFA1978F0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/500A4D96-88EF-E811-B3A3-008CFA1111D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/622A890A-DDEF-E811-A458-008CFA197460.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/7A2495F4-7AEF-E811-B69B-008CFA1111EC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/ACE6BE1B-86EF-E811-8CBB-008CFAC91E98.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/C816995A-94EF-E811-A925-008CFA1979AC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/D8CB7A2C-76EF-E811-A291-008CFA197480.root',
] )
