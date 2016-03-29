import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/041DBC01-7795-E511-A04C-0CC47A0AD792.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/44FE8B93-7695-E511-8120-00259029E91C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6EBE27D6-7695-E511-93BA-0CC47A0AD668.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/98D230BC-7695-E511-908B-003048CB8610.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/FADEFE34-8F95-E511-9A9A-02163E015F74.root' ] );


secFiles.extend( [
               ] )

