import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/0A606E2A-DF4D-E711-9B84-E0071B741D70.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/1438F10F-ED4F-E711-B3A9-549F35AE5024.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/18BB2CB0-4F4E-E711-A1C7-0242AC110003.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/26EA579C-3C4E-E711-8BE8-001E677926AA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/4848E402-4C4E-E711-B436-3417EBE51901.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/4C32C782-6E4E-E711-AA93-20CF3019DF19.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/6AB940B2-4D4E-E711-923B-0CC47A546E5E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/76C542FD-3D4E-E711-8AA6-0090FAA57560.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/867E75B2-AA4E-E711-A684-0025905A60AA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/8C9783F6-D750-E711-A034-008CFAF228FA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/A809D171-474E-E711-9B0F-0025905C54C6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/AC1D0776-544E-E711-BEB9-AC162DACB208.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/B47D818F-494E-E711-98C3-3417EBE34CF9.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/D058BDAA-AA4E-E711-A19D-0025905B8560.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/D0C74808-524F-E711-8200-0025907859B8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/F868AA67-4B4E-E711-889D-A0369FD20730.root',
] )
