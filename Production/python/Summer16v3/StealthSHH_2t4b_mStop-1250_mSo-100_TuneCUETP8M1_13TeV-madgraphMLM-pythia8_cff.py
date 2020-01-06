import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/0AA3830A-CEF6-E911-A2D6-4CD98F816A1D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2403F40A-CFF6-E911-9E0F-AC1F6B0DE49C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/30144F20-CEF6-E911-BC46-509A4C9EF8EC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/60CFB72E-34F7-E911-9EA5-0CC47A78A2F6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/82BE94BE-D4F6-E911-B788-F4E9D4AF6CE0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8C231553-ECF6-E911-8B98-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A034B226-D4F6-E911-8534-D4856459AE7C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A631243E-DEF6-E911-8BF7-FA163E69B3D1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/AAF9F6A0-D7F6-E911-8BD5-008CFAFC0416.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DAE36713-D5F6-E911-8361-20040FE9C898.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DE003884-37FB-E911-BB4E-B496910A0290.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E49D93E2-B0F7-E911-8841-7CD30AD09B26.root',
] )
