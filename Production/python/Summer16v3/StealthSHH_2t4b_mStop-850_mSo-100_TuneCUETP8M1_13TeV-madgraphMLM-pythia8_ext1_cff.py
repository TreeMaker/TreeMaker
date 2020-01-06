import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/1AF19BE6-D6F5-E911-89B2-1866DAEA7C48.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/30BEEBE7-D9F5-E911-8822-008CFAFC0416.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/4433D405-D7F5-E911-98D8-FA163E45D256.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/4ACC2E94-D6F5-E911-816B-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/68A47D68-D6F5-E911-B401-24BE05C6E7E1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7A990AD9-D6F5-E911-80F5-0090FAA58224.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7CAC990C-D7F5-E911-AD47-0023AEEEB6CD.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/94F95C6C-D6F5-E911-8B15-98039B3B003A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A233A1C6-D6F5-E911-97B5-D4856459AC42.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/B236D515-D7F5-E911-9593-7CD30AC0311A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/CAAD1083-D6F5-E911-8246-0CC47AD99116.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/D2CE5664-DBF5-E911-92C6-B026283D5620.root',
] )
