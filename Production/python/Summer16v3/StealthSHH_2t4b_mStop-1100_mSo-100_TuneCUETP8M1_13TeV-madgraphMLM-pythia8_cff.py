import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/0653FBAD-D0F5-E911-BE38-0CC47AD98BCC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/169E867C-D0F5-E911-A2BA-0CC47AFC3C76.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2C8DE969-D0F5-E911-B5F8-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2E1A07D1-D0F5-E911-A9E0-002481CFE642.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/346C1DEA-D0F5-E911-934A-FA163E4D2929.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/54229F6A-D0F5-E911-9255-B02628346AE0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7C1793B8-D0F5-E911-AA65-10983627C3C1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/863AE2AF-D0F5-E911-9AB7-5065F3815281.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/90535862-D0F5-E911-9BE3-0CC47A78A42C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D8C0BEA2-D3F5-E911-9029-B02628341FC0.root',
] )
