import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/D62EC3EC-3FF7-E911-B997-0CC47A7FC6D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/22916233-93F6-E911-980E-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/22BE0EF0-93F6-E911-8485-48FD8E28249F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2C3FE094-DEF5-E911-A0D8-FA163E9EE402.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/60482C38-93F6-E911-93A3-001E67DDBEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/66507EFF-93F6-E911-B90D-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6C20F8F0-93F6-E911-9161-00259090821E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/70C9E42A-93F6-E911-9296-AC1F6B34AC92.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/864237EA-92F6-E911-AAD1-24BE05CEADA1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/88E87E7C-93F6-E911-9DD0-141877411D83.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8A00ACA9-97F6-E911-A558-509A4C748A76.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9AC159E8-93F6-E911-8EA9-0CC47AFF2492.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A0D1C6B1-92F6-E911-B9F0-0CC47AF97126.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B03484D5-93F6-E911-8891-A4BF01158B18.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BEB80CDE-93F6-E911-B713-246E96D14B5C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C65A0A40-94F6-E911-B72A-002590FD5A48.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D4B6E0AA-93F6-E911-A7B0-00259068AD8E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D6514A2C-93F6-E911-8124-44A842B4D8CB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E6D0C7FB-93F6-E911-81DF-90B11CBCFF5B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/EACA80EA-93F6-E911-BF20-BC305B390A25.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FCDC7549-94F6-E911-AF39-0CC47A78A41C.root',
] )
