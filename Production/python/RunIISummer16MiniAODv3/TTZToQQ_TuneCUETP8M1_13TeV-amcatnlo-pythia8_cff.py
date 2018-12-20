import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/186F2A28-C8F0-E811-8E43-0025905B85DC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/52157547-A6F0-E811-8F53-0CC47A7C3610.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/9247715B-A6F0-E811-9E4C-0CC47A4C8E5E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/9A655BB4-A6F0-E811-A9EC-0CC47A4C8F0A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/E0DBB7AD-BCF0-E811-98D4-0CC47A78A42E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/F8280F8E-10F1-E811-8F98-0CC47A4D7698.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/FE383642-29F1-E811-ACB5-0CC47A4D767A.root',
] )
