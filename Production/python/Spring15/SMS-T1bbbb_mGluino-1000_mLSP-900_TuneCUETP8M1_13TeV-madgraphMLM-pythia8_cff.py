import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/34A98B05-AF50-E511-A9F1-000F530E47A4.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/4450DF96-AE50-E511-B9F4-842B2B2922E2.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/68214069-AE50-E511-959F-B083FED03632.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/6ADCBA86-AE50-E511-80F8-842B2B29273C.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/00567F63-3A50-E511-9F9F-00259073E384.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/00C98A80-3A50-E511-B1BB-000F530E46DC.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/66BEA79F-4350-E511-8F3F-000F530E4BD4.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B07ED204-3B50-E511-AA6F-002590D4FC5C.root',
       '/store/mc/RunIISpring15DR74/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D21A4098-3A50-E511-B1EA-B083FED76637.root' ] );


secFiles.extend( [
               ] )

