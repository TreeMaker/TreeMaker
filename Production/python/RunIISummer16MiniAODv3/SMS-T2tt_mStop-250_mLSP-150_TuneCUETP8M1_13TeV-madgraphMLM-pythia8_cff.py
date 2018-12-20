import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2CE6774C-62F0-E811-910B-90B11C0BB9FB.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3C27E478-B9F0-E811-AC62-14187741121F.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/401E2293-7FF0-E811-95EF-782BCB20F01B.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/68FAD3C9-6AF0-E811-A011-549F3525DDFC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6C936E47-5BF0-E811-B62B-D4AE527EE011.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8E7922B4-5AF0-E811-8BA6-141877410B85.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9433B0A9-71F0-E811-B919-801844DEF068.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/AEBA44C5-61F0-E811-8B84-549F3525C0BC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E4FAEBF4-5AF0-E811-A0D5-1866DAEB40CC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E8FDB46E-7FF0-E811-A2FE-001EC94BFB5F.root',
] )
