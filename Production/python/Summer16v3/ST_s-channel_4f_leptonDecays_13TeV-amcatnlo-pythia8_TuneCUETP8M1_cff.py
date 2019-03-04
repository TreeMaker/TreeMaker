import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/34DD7CFF-BB20-E911-A84C-90E2BAD1BDF0.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/380582CF-BF20-E911-8662-1CB72C1B65D4.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/90318AE6-BC20-E911-B62A-34E6D7E05F28.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/96463C2D-C220-E911-86EF-AC1F6B4E0166.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/D62AE119-C120-E911-A08E-D8D385AE888A.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/DCD4EA69-BC20-E911-BC04-441EA1714E4C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/EC99BB1F-6021-E911-9772-34E6D7E05F01.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/F820C268-BF20-E911-BF19-1CB72C1B2D80.root',
] )
