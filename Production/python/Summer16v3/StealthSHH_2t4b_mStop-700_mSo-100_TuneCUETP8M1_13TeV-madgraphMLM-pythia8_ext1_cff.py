import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/005C1BFA-6B09-EA11-81BA-B083FED42A19.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/0C585741-F508-EA11-9AA0-549F351EDC46.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/223CDEAE-9808-EA11-8332-FA163EA45C09.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/326CC8E6-A309-EA11-B8A8-AC1F6B5676BA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/389F05A6-7908-EA11-835D-AC1F6BAC7D16.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/5C0D2CC7-1A0B-EA11-87B4-AC1F6B0DE3E8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/8C28B028-7908-EA11-9E47-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/A2282476-800B-EA11-8A00-00259094F286.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/AC2AC974-7908-EA11-AB68-0CC47AFCC612.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/B08E6E76-800B-EA11-B877-BC305B390A59.root',
] )
