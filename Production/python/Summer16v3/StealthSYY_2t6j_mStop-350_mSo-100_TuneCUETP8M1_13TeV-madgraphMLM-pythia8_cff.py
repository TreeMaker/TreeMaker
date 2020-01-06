import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/18695F73-E2F6-E911-AD1B-20CF3027A582.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1EAB7CFE-CEF6-E911-9FE2-AC1F6B595F4E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/22B0C5FC-CEF6-E911-915A-CCC5E5F2B53B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/26935F5E-CEF6-E911-B0CA-D4856444C6F2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/26D817E2-B0F7-E911-919B-509A4C748038.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/40C85FFF-D3F6-E911-8252-008CFAFFEA48.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4230629A-59F6-E911-A873-FA163EA08616.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/525AB9A1-0BF7-E911-B9C1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/560D2BE5-26F7-E911-82DE-3417EBE7009F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5C9E3471-37FB-E911-BF7D-B496910A80D4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5ECE0198-D4F6-E911-AD51-AC1F6B34AC92.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/861F2F97-CFF6-E911-B99E-001E67DFF67C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8E786B80-17F6-E911-9686-AC1F6BAC7EAE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A0DE371A-8DF7-E911-BE51-0025909081F2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A24D58F9-F4F6-E911-9991-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/AA1A2995-CCF6-E911-9913-14DDA924324B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C4DD14D2-D5F6-E911-8623-B8CA3A70A410.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D20274C7-DAF6-E911-B4C4-AC1F6B0DE2EC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E857BC79-DEF6-E911-8532-0090FAA58084.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F293B0EF-C9F6-E911-9861-44A842CFC97E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F6F013E4-D4F6-E911-A498-0025905C2D98.root',
] )
