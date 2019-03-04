import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/3423F013-FCEA-E811-AC92-001E67DDD348.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/3AC29B78-D3EA-E811-85D1-001E67DFFF5F.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/6AF9C81F-E3EA-E811-9E5B-0026181D28BB.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/803DB74E-D5EA-E811-B6B3-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/98EDDF93-D1EA-E811-9A19-A4BF0102572F.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/D405D65F-7EEB-E811-8D4E-001E67A402C1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/EE36548A-D1EA-E811-8C58-A4BF01026229.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/F6E9102F-FBEA-E811-B0C4-001E675A6AB8.root',
] )
