import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0CF05BBD-6B34-E911-82BA-24BE05CEEB31.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0CF5E8AD-6B34-E911-8611-AC1F6B0DE2A4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/128081E5-6934-E911-8D61-0017A477107C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/1A9A82CA-6B34-E911-9A62-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/1C6B5397-7334-E911-AF35-008CFAF28DB2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/227B0C10-7234-E911-9B85-001E67E6F65C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/22A51648-6A34-E911-B55E-AC1F6BB177EE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2C9A24D0-6B34-E911-B102-141877411367.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2E4FC567-6D34-E911-AC50-A4BF0102A4F5.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/54FC146D-A434-E911-BFB7-0025905B85DC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/5E7F0C3A-F334-E911-8F2D-0CC47A7E6A88.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/62357A51-6E34-E911-BB54-549F35AE4F88.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/6EF1A118-7134-E911-996C-0CC47A6C1038.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/7E54E2F7-6A34-E911-9F63-D48564593FD8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/80DAC53C-6F34-E911-ABF3-1866DA87AB73.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9CBB5595-B134-E911-958E-0CC47AF97150.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9EEE3DE3-7334-E911-9630-FA163E7F0694.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B8509DBD-7234-E911-92DF-3CFDFE636460.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/DE9244B7-6934-E911-A82C-AC1F6B8DBEC2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/E26015A4-7534-E911-AC32-0CC47AFF0218.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/E8194D0C-6C34-E911-B577-A0369FD20740.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/EAADDACD-9034-E911-926D-0242AC1C0501.root',
] )
