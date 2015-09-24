import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/043ECD0B-BE5D-E511-9B2B-002618943930.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/086AA30F-BE5D-E511-8725-0025905A606A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/22BA6117-5C5D-E511-8889-0002C952E794.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/569FB0F2-BD5D-E511-9F48-002354EF3BCE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/9E12CA65-6C5D-E511-8ED2-0002C92A1020.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/D0181695-865D-E511-BBF5-0002C92DB418.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/D4F678F6-5D5D-E511-8028-24BE05C6B701.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/E62D1F5D-6C5D-E511-9A2A-0002C92DB530.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/60000/F6FDA602-BE5D-E511-B190-003048D15E0E.root' ] );


secFiles.extend( [
               ] )

