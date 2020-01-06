import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/0E6D0D33-DBFF-E911-BCBD-0CC47A2B04A6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/26279BFA-DBFF-E911-9C21-FA163E1A7B34.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/46DA814B-DBFF-E911-B009-008CFA05E88C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/48897772-DBFF-E911-B3E1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/4C85A41D-DBFF-E911-B0A4-20CF305B0629.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/503356E6-4900-EA11-9A28-0CC47A78A4BA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/6CE70FE5-E4FF-E911-BF8E-D4AE526DEE96.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/96199A10-7800-EA11-B2C2-0090FA9DFD8A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/9EC2B860-DBFF-E911-BCDB-0CC47AFCC6BA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/A017879D-ECFF-E911-B596-246E96D14BC8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/BA502F1D-DBFF-E911-926C-B02628272370.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/BC991730-DBFF-E911-AE65-002590907876.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E221DB6F-DEFF-E911-9BA4-AC1F6BC67D4E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E274191E-DBFF-E911-A47B-E0071B6CAD20.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/F61BD646-DBFF-E911-BD27-0CC47A706F42.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/FE64A035-DBFF-E911-8D56-44A842CF05E6.root',
] )
