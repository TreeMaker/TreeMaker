import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1AE62D82-0F4A-E511-9EA8-02163E0146ED.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/288EB22E-1F49-E511-885B-02163E0142A7.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/30D8CFD0-934A-E511-9027-B8CA3A709648.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/AA098599-8D4A-E511-86C9-0025905B860C.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/AE237EBF-8C4A-E511-9369-001E67397D55.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/DA6BCA0D-924A-E511-84F7-0002C92A1030.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E84419DA-4549-E511-969C-02163E014679.root',
       '/store/mc/RunIISpring15DR74/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/F6A0965E-8D4A-E511-80E2-02163E0168AC.root' ] );


secFiles.extend( [
               ] )

