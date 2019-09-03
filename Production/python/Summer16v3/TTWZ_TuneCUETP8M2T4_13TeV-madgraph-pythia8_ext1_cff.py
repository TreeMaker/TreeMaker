import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/110000/C2ECFCD4-9733-E911-B4EA-0CC47A009E10.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/04738CCB-8B32-E911-8C45-008CFAFBF1EC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/08D212E2-8B32-E911-AC05-28924A33AFC2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0EAE2D21-8C32-E911-B589-0CC47A78A340.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/123E21B8-8B32-E911-9866-FA163E53B7DF.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/24D59B48-8C32-E911-9CDA-AC1F6B596094.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2C6AAA6F-8C32-E911-891C-484D7E8DF114.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2C6C824A-8C32-E911-8157-A0369F7FC0BC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2EB7AFCB-8B32-E911-A33D-A4BF01125A90.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/385112E8-8B32-E911-B559-0CC47A2AECFA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/686F3CC0-8B32-E911-A324-001E67E5E8B6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/88C2561E-8C32-E911-90BE-002590D60000.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/88D7B752-8C32-E911-919E-002590E7DEBE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/8E57A511-8C32-E911-9633-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/981B49C8-8B32-E911-AA40-A0369F3102B6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9C20F9C8-8B32-E911-A353-A0369FE2C174.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C214F453-8C32-E911-A291-44A842B4B40B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C6825102-8C32-E911-B944-842B2B6E981B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CC1FDD32-8C32-E911-8C56-1866DAEB3370.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/DC1ACFC2-8B32-E911-BEAE-0CC47AFF0470.root',
] )
