import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0A9C3265-9B03-EA11-9165-7CD30AD08DF4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0EE47A79-5C03-EA11-96EF-00269E95ACE8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/24202F78-5C03-EA11-B83D-AC1F6B0DE140.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2641F6A6-5C03-EA11-B6CC-24BE05C38CA1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/34D66152-5C03-EA11-8AC6-0090FAA573B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/385E90E5-5903-EA11-8CAF-008CFA56D870.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/72F6D5DE-5C03-EA11-8844-002590D9D84A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/86C6637A-EF03-EA11-9150-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/8CFD83B0-5C03-EA11-B60F-0CC47A6C14C8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/903FFE36-5C03-EA11-B3F2-FA163E9D19C4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A698F8A7-5903-EA11-B9CE-44A842B298F1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/BA6B4A7B-5C03-EA11-BB7D-0025909082CE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C6085739-5C03-EA11-82FD-6C2B599A0688.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E2D22FA7-5C03-EA11-866A-1866DA85DC7F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/FAA27FAB-5C03-EA11-8385-0242AC130002.root',
] )
