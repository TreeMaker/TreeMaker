import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/0ACDE168-604E-E711-B4B0-34E6D7BEAF01.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/14A41000-504E-E711-A698-0242AC110008.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/164C0F81-494E-E711-B6C1-A0369FD20CF0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/16560993-AB4E-E711-8767-0025905A60AA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/1AA88D7C-3D4E-E711-8FD0-001E67792598.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/1EFD0C6A-4F4E-E711-9808-0CC47A546E5E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/305F0B24-C34E-E711-A9E3-FA163E52C01E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/320F672B-544E-E711-9D7A-0026B9532A81.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/3A7045EA-484E-E711-9520-0025905C53A8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/3ACCF517-504E-E711-9AB1-002590E7E00A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/3E272016-4B4E-E711-AE90-90B11CBCFF4E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/42EDA284-494E-E711-A855-00259073E500.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/5E16C3A9-AA4E-E711-8F11-0025905A611C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/5EAEF933-4D4E-E711-A30A-1CC1DE1D208E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/6871A384-4E4E-E711-9D73-10BF481A01ED.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/969B0661-484E-E711-83D3-0025901D40B2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/B60E5BF6-574E-E711-BC1C-44A842B4CC71.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/C835E32C-474E-E711-8ADA-3417EBE34CF9.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/CC4C7C86-DC50-E711-A6A1-3417EBE6457C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/D6361E02-C34E-E711-B147-FA163E89B8F3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/DEC7343E-464E-E711-8799-BC305B390A0B.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/F0FE812D-5B4F-E711-B840-0CC47A57CE00.root',
] )
