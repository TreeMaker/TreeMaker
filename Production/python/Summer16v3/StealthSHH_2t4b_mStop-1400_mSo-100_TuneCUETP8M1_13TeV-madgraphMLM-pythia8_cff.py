import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0C99F80F-1105-EA11-A23F-0CC47AC1750E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/1067A0F5-1005-EA11-8D3A-00259074AE48.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2ADCCF40-1105-EA11-9E70-AC1F6BAC815A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/4C023C4B-1105-EA11-B204-B499BAAC0572.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/50EB40FA-1005-EA11-8796-801844DEE7F8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/541A08F5-1105-EA11-AAED-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/54C573E4-1005-EA11-B1DD-E0071B7AC710.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/685EC846-1105-EA11-A2F0-A0369FE2C146.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/72F02499-1105-EA11-9BF3-A4BF01125628.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/80F8A5F3-1005-EA11-89F5-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/8CD2B034-1105-EA11-AE50-0CC47AFF0280.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A44D098A-1105-EA11-A3FB-FA163EF6329F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/BA7879C9-1105-EA11-ACAB-AC1F6B56768A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D67CFCE5-1005-EA11-9F15-EC0D9A0B3180.root',
] )
