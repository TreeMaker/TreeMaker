import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A203CB9-5E7C-E511-ACF0-C4346BC8C310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CF2CBC4-5D7C-E511-8966-00266CFFCC50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0EFCFAD4-5D7C-E511-B64E-00266CFFC76C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/123B3CBA-5D7C-E511-B55F-6CC2173BBAB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A1716C5-5D7C-E511-96B3-AC162DABAF78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2296FDC4-5D7C-E511-91CF-AC162DABAF78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26A7B1F0-787B-E511-8798-00259073E3D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6285FBC4-5D7C-E511-9D79-AC162DABAF78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/689341C0-5D7C-E511-A594-00266CFFBF90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7415CAC2-5D7C-E511-B0A6-00266CFE79A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/786856BC-5D7C-E511-BA6C-00266CFE79A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7EC0E5BF-5D7C-E511-AC19-00266CFFC76C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88461556-5D7C-E511-AD02-00266CFFBCFC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88879FC1-5D7C-E511-BA8A-C4346BC7EDD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2E239BA-5D7C-E511-9A27-6CC2173BBAB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C61F99BA-5D7C-E511-A633-6CC2173BBA60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C8C069C4-5D7C-E511-8F25-00266CFEFF04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE0CC5C4-5D7C-E511-A1AB-00266CFEFF04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE7B01BA-5D7C-E511-AD43-6CC2173BC220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4FB9DBA-5D7C-E511-B680-C4346BC8C310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE4953BC-5D7C-E511-9F63-00266CFE79A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FEC091F1-787B-E511-9F00-20CF3056170A.root' ] );


secFiles.extend( [
               ] )

