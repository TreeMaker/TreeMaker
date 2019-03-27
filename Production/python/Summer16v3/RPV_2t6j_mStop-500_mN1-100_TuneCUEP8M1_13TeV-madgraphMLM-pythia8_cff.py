import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/280000/46FD2E97-E705-E911-A315-F46D043DE4EF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/280000/BCAA4BCD-3F05-E911-A0F8-F46D043DE4FF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/A2370552-3E05-E911-AFB1-F46D043DE4EF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/B6241BB0-2D05-E911-8A3F-5CB901E1BCA4.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/DEE8AE16-0B05-E911-B6BC-F46D043DE50F.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/90000/8E6BD5BE-4005-E911-8315-F46D043DE4F9.root',
] )
