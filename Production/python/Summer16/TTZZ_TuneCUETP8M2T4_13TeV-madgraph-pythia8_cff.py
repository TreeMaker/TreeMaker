import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/3CA11BC0-C150-E711-AD77-7CD30ACE178C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/4409222E-854E-E711-BE88-0CC47A1E0468.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/5CED297A-4E4E-E711-B946-001E677927F0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/6C170267-544E-E711-9D65-7845C4FC3C4D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/863C9F31-E54D-E711-B7B7-D48564593FAC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/9A0E98DB-6A4E-E711-8FA9-0025905C975C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/9C6BE7C0-594E-E711-B730-485B39897251.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/A287F57D-A34E-E711-85B9-001CC47C50AA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/ACB6F17C-744E-E711-81CF-0017A4770470.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/D006C9B2-664E-E711-863F-0090FAA57720.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/D8694F04-6F4E-E711-99AD-1CB72C1B63C2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/E2D272AD-014F-E711-8D1F-003048CC71C0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/EED68CC5-AB4E-E711-B677-0025905B85B8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/F2CD5DE9-5C4E-E711-9AE0-0242AC110003.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/00000/FE5394F2-A34E-E711-9CD0-FA163EEFD873.root',
] )
