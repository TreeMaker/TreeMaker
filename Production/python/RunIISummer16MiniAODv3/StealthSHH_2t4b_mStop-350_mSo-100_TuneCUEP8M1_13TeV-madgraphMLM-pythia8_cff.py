import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/003A5EA7-07F1-E811-93BF-24BE05CE3C91.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/02B79264-23F1-E811-81DC-A0369F3102B6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0C76A282-FFF0-E811-91E7-24BE05C6E591.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/4465199C-F7F0-E811-ADEA-E0071B73B6B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/6A1470DA-ECF0-E811-A7FD-EC0D9A82260E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9A0DC765-04F1-E811-BF46-B8CA3A70B608.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B4265CFE-EEF0-E811-8D26-E0071B7A48A0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DE143458-13F1-E811-96DE-24BE05CECB71.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E4E5914D-EEF0-E811-ABEB-5065F381B271.root',
] )
