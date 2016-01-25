import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0CC715DF-ED7B-E511-ADB7-0022194FE7C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/14FC509D-E97B-E511-8613-848F69FD4C94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/18A324A4-EB7B-E511-B8A7-0025905AC878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/1A807D9B-E97B-E511-A327-7845C4F9162D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3AF5CD4D-B57C-E511-AE29-02163E00E615.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6200678C-B47C-E511-8D5A-02163E010E7C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/7E05CAC9-E97B-E511-9A5D-0002C94D54EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/8CEF008E-B47C-E511-A30C-02163E0166A9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/AEAF1DA4-EB7B-E511-82B7-0025905C42D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/FAF3F431-EC7B-E511-A62E-003048D333EB.root' ] );


secFiles.extend( [
               ] )

