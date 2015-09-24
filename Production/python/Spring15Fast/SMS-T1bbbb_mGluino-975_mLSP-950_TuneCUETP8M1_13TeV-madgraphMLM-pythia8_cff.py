import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/360AE4AA-605C-E511-BF47-24BE05C6B701.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5AA709B0-605C-E511-940F-0025905521C0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/8691DAAA-605C-E511-8329-5065F3812291.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A45DA6D1-605C-E511-830F-002590A370B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/C4EEBC3A-675C-E511-86D9-F45214C748C0.root' ] );


secFiles.extend( [
               ] )

