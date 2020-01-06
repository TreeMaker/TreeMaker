import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0CF55B8E-A104-EA11-949F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/18DFC67D-A104-EA11-B7DA-0CC47A57CE00.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/1E6CB970-A104-EA11-A7BE-0CC47A4D766C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/323AA980-A104-EA11-A1C7-001E67DDD22B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/386E6C41-A204-EA11-A7DB-44A842B4520B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3ACC5A67-A104-EA11-BDEA-0CC47AFF0270.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/58C30764-A104-EA11-B3A6-509A4C7812EC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5CD2A449-A204-EA11-A036-44A84225CABC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/727340A2-A104-EA11-97B8-FA163E19AEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9AD5607A-A104-EA11-B23D-0CC47AD98CFA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C4CABEC0-A104-EA11-A2CE-A0369F310374.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/CAF1F660-A104-EA11-B511-48FD8E28246D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D8712851-A104-EA11-A93D-00259094F286.root',
] )
