import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/3A040165-D4F1-E811-902C-001E67A3FB91.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/4ABAA446-C0F1-E811-8518-001E67A406E0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/601F88AB-C0F1-E811-8880-001E675A5244.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/7CFA33B8-C0F1-E811-A064-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/8053A1B4-EEF2-E811-B1C7-001E67A3EC05.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/827ACFB4-C0F1-E811-8CCC-001E675A6AB8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/98B7EF31-C1F1-E811-A2CD-485B3919F0FE.root',
] )
