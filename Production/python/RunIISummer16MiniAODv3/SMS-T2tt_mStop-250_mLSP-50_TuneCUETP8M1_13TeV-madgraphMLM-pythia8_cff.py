import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/16FA9F51-6FEF-E811-9109-24BE05BDCEF1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/3C16CE4B-6EEF-E811-8E7B-24BE05BDBE61.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/82BD696D-6EEF-E811-BA1E-EC0D9A822606.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/949037AB-6EEF-E811-985D-EC0D9A822606.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/BA99AD6A-6EEF-E811-BA7F-EC0D9A822606.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/BACD26FC-7AEF-E811-BE19-24BE05C4D851.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/C0807C1C-6FEF-E811-BE44-24BE05BDCEF1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/F4EC7E4D-6EEF-E811-BA59-24BE05C6C7F1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/F6735C4B-6EEF-E811-800B-24BE05C6C7F1.root',
] )
