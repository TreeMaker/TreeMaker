import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/54B31F2C-73EA-E811-AD90-001E67460572.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/025001D1-D8EA-E811-9A02-001E6724799A.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1CF6E823-D9EA-E811-9A91-001E67247CC9.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/228D8ED2-D8EA-E811-A8B1-0CC47A713A04.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/4A56BA10-D8EA-E811-A463-0CC47AC1757C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/90F793B0-D6EA-E811-8910-0CC47AC52FCC.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/E4DC1230-E0EA-E811-BF33-001E67247F8A.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FC0286A0-D7EA-E811-8328-0CC47AC52A94.root',
] )
