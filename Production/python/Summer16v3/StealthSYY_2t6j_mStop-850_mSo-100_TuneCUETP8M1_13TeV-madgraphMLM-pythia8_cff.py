import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/068E9BD5-7304-EA11-B489-34800D4F9608.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/1227E61C-7404-EA11-9877-509A4C748A3D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5025C821-7904-EA11-99CD-24BE05C44BC1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/509FD300-7404-EA11-83BE-0CC47A2B03A2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/588751DE-7304-EA11-A94D-001CC4A6AE8A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/6C0E72D2-7304-EA11-9610-6CC2173C4580.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/80DDD0B4-7704-EA11-8E0E-A0369FD0B142.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/8E0BB407-7404-EA11-8450-0242AC130003.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A4DE5ED3-7304-EA11-91DA-AC1F6B0DE2FA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C0C73952-7404-EA11-9814-FA163E1A8BD9.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DCCECCEC-7304-EA11-9EB9-E4115BE5F180.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E687E60F-7404-EA11-8AE7-0CC47AFF24C2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/EE2218D2-7304-EA11-B8BE-B496910A9A24.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/F0934112-7404-EA11-AD3D-6CC2173D5F20.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-850_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/FEE3A919-7404-EA11-93BB-0026182FD740.root',
] )
