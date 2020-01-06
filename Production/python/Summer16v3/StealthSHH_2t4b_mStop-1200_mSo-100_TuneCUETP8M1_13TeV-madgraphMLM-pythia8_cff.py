import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2CFA2D0F-60F6-E911-AE07-7CD30ACDCA58.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/52D63CC5-61F6-E911-9E2E-D4856459AC30.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5C795803-60F6-E911-AFC3-0090FAA58D64.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/60D5267E-61F6-E911-B859-0CC47A1E0488.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6857C444-5FF6-E911-8DD6-FA163EDD2DC6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7659AE13-27F7-E911-92FA-3417EBE7009F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/78F27955-61F6-E911-84C2-00259029E670.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/809A3DBC-5EF6-E911-9139-5065F3812221.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/84F941D1-5FF6-E911-956F-0017A4770458.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8E87EDED-5EF6-E911-BC92-B083FED024B1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/941E7A1E-5FF6-E911-BC39-1CB72C1B6C32.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9EE2CF9F-5FF6-E911-BD45-008CFAF28DB2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B043B272-5FF6-E911-BC24-0025900B20E2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B225B52E-62F6-E911-8902-C45444922958.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D2BA02D2-61F6-E911-AAD8-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D6ECCFC1-5FF6-E911-9FFF-0CC47A4C8F2C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F0F69887-61F6-E911-A743-0025905C94D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F68734DE-5FF6-E911-BA55-7CD30AC030C4.root',
] )
