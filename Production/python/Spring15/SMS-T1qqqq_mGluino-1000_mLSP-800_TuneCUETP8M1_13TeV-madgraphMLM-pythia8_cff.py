import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/565157FB-8250-E511-AD2B-AC853D9DAC21.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/729B5C00-8650-E511-A793-00261894387E.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/8E3B090E-8350-E511-A16F-AC853D9F52D8.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/F0EB1CFC-8250-E511-8469-AC853D9DACF7.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9AEAD4D8-C151-E511-B000-000F530E4780.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9E7AAF38-E451-E511-8E78-008CFA19741C.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B889DEE4-C151-E511-BD05-842B2B182385.root',
       '/store/mc/RunIISpring15DR74/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B89726D5-C151-E511-BE56-842B2B28EB06.root' ] );


secFiles.extend( [
               ] )

