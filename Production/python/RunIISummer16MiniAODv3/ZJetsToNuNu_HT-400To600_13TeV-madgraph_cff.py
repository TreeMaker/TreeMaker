import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/10027574-1AEB-E811-B14A-001E67DFF61D.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/563F38EA-7BEB-E811-9D09-001E67DFF61D.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/5CD52BBC-1AEB-E811-938D-90B11C12EA74.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/90EFE0B2-16EB-E811-8D8D-001E67A3FDF8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9E303EDD-17EB-E811-B398-001E675A68C4.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/A0055CB3-1AEB-E811-AE2E-90B11C12E856.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/AACC9A71-1AEB-E811-94AA-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/AE37A6A6-1AEB-E811-8073-A4BF0102572F.root',
] )
