import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0CCB2D3A-95F0-E811-940F-68CC6EA5BDDA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/327ED5BA-33F1-E811-A7AE-AC1F6B8DD2A0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/34B34752-67F0-E811-A643-68CC6EA5BDDA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3A48FA65-97F0-E811-AE3A-441EA171A206.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/405C63FC-87F0-E811-9B71-68CC6EA5BE7A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A27E96D8-85F0-E811-9659-68B59972C37C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D83B1966-73F0-E811-9A2A-34E6D7E3879B.root',
] )
