import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/10000/5669995B-5CF5-E811-ADAA-0CC47AFCC422.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/10000/8802E120-5CF5-E811-A69B-0CC47AFCC64A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/10000/BE0A9B82-5CF5-E811-AB23-0CC47AFCC62A.root',
] )
