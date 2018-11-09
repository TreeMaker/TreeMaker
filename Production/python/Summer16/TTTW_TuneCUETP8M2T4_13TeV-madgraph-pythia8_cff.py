import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/06693B49-3E4E-E711-AF00-001E67E6F855.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/1C8E5B92-494E-E711-9F03-7CD30ACE1654.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/366B89AA-524E-E711-B67D-20CF3027A61A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/48FE282F-4D4E-E711-A41E-A0369F836288.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/565E173B-354E-E711-8836-0025905C54D8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/5AC7E819-5E4E-E711-B0D7-0CC47AB3608C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/5C176C90-494E-E711-9976-0026B927865E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/66871F02-C34E-E711-84BD-FA163E89B8F3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/66F15FA9-3A4E-E711-AD83-E0071B7A48A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/6E5E20A9-AA4E-E711-B9C8-0025905B855C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/70EAD00B-D64F-E711-BC68-008CFA1660F8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/7CC9BA63-374E-E711-9E5E-002590E7DFE4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/84BE1D4E-4C4E-E711-AB30-3417EBE5264B.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/901B1F1C-3C4E-E711-8AA4-3417EBE527B3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/A6532433-4A4E-E711-85CA-002481DE4818.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/B4584997-494E-E711-A66D-001E67504A65.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/BED7E34C-4D4E-E711-A866-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/C03AF515-3B4E-E711-961A-3417EBE70684.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/C28D516F-3A4E-E711-B86A-0090FAA58974.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/E2C8B622-D350-E711-B89B-3417EBE64B85.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/120000/EE5840AA-AA4E-E711-BB55-0025905A608A.root',
] )
