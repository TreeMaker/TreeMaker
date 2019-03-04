import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/140BA2A3-FAF1-E811-8FA7-20040FE8EA44.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/32C5E37A-65F0-E811-BD0F-1866DAEA8220.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/3EEFF902-41F0-E811-8FFC-842B2B181788.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/5271D2E2-C3F1-E811-B5DC-20040FE8EA44.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/667A08C5-C9F2-E811-87DD-782BCB539B50.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/94D45C07-0AF3-E811-B529-141877410316.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/B0B545CF-07F2-E811-AF62-842B2B42BCF6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/C82CBE2E-3DF1-E811-9BBC-20040FE9CBD8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/DABCC00A-CAF2-E811-9361-001EC94B51EC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/F2AD7868-C9F2-E811-9C75-A4BADB1E72AE.root',
] )
