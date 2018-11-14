import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/0C1A1CA4-7957-E711-92B8-002590D60062.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/0CE9A110-1357-E711-B2EF-0025905B85AE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/14D138A5-1057-E711-864B-0CC47A4D766C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/162B2CBA-3D57-E711-8F51-0CC47A1E0C70.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/204615E5-3B57-E711-9919-002590D5FFDA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/4654AC56-4057-E711-976D-000AE488542F.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/6864D40F-B056-E711-BFB7-D48564591B64.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/76B5A5CD-2557-E711-BAA4-008CFA0027B4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/E8118646-3F57-E711-94FC-A0369F5BD91C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/90000/F4443DAF-6257-E711-A9D5-34E6D7E3879B.root',
] )
