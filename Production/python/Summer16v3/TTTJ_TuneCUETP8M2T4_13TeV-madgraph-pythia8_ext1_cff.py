import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/02325D70-3132-E911-B9A2-B499BAAB427C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/04F51F98-3132-E911-A67F-3CFDFE63EAA0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0CF43262-3432-E911-AD66-002590D9D966.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0E7FDB7F-3132-E911-9A8D-008CFAFBF576.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/56C18D0B-3232-E911-8C9C-0CC47A7E6ADC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/5E409A0E-3232-E911-BA19-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/66F57EAE-3132-E911-B6E7-001E67E6F882.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/683CEC7F-3132-E911-888E-0CC47A0092D0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/7EE60083-3132-E911-9CFB-0CC47AFCC68A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/80B06601-3132-E911-9A93-A45D36FC89C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/8C48F8A2-3132-E911-9B50-AC1F6B0DE3F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A816A533-3232-E911-9240-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B662EE22-3132-E911-9BDF-848F69FBC085.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CA9FD481-3132-E911-ACB5-A0369F836338.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/F8F2900D-3132-E911-AB7D-FA163E85281B.root',
] )
