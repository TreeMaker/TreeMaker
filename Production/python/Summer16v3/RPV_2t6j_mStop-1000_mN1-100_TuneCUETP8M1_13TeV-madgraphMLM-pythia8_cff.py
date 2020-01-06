import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0A4D7ADF-E004-EA11-AE72-AC1F6B0DE338.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/28BDE608-3F05-EA11-964D-0025905C53D8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3E98144D-EB04-EA11-A4D7-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/64E2B5F4-3605-EA11-B15C-20040FE9CBD8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/6A2A35D0-E804-EA11-A75C-FA163EE80E60.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A8692D54-E004-EA11-8876-0CC47A5FBDC1.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B4B67B0E-D904-EA11-8E2F-00266CFFC4E0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B6E9B0A7-D504-EA11-9C0B-B8CA3A708F98.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E6C79A15-E804-EA11-8321-0CC47A6C1806.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1000_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/F6474DBF-DD04-EA11-B03A-44A842CF0571.root',
] )
