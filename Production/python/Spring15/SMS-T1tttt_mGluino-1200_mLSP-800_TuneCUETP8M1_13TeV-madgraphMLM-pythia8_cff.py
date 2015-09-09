import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/08212B35-3A4B-E511-A6AC-A4BADB3D00FF.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2CFEE82B-934B-E511-8B12-0026B95C1EE4.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5E764F2A-934B-E511-AE6C-001E6865A5A5.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7AD883EB-924B-E511-927D-047D7BD6DF5E.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/802785B2-394B-E511-BB9D-842B2B2AEE96.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8AD9F22E-934B-E511-BC98-000F530E46D8.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8C33EAB2-394B-E511-B886-842B2B185AAA.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/90E0FC2B-934B-E511-BD58-001E4F1BC725.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D83071B0-394B-E511-8373-001E6878F719.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D84FD64D-544B-E511-8B64-02163E011F92.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F0915CED-924B-E511-A0C9-0025907DCA64.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FA6FF2BF-704A-E511-A064-20CF30725200.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FA78E9E7-924B-E511-AEA8-003048F0DFBE.root' ] );


secFiles.extend( [
               ] )

