import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/2C143C9D-7908-EA11-ADCB-FA163EF69D2B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/303F173A-340B-EA11-AA38-0CC47A4C8E82.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/46B9E6CE-990B-EA11-A7FB-C4346BC75558.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/4AFA6249-3B0B-EA11-835E-0CC47A4DEF54.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/5CBD077B-7908-EA11-A0DA-0025905C5432.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/60AA0354-6C09-EA11-B761-68CC6EA5BE0A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/825B3059-6C09-EA11-B471-A4BF012881D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/842E6313-7908-EA11-B8F1-E0071B73C620.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/86D0915D-E90C-EA11-8B9A-6CC2173C9150.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/8C149F26-2209-EA11-BFC2-008CFAC93F14.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/9CB2F68D-3A0B-EA11-B655-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/BA1DAA9D-D80C-EA11-B8B4-20CF307C98F9.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/F27096F0-6B09-EA11-A94B-20040FE9CBD8.root',
] )
