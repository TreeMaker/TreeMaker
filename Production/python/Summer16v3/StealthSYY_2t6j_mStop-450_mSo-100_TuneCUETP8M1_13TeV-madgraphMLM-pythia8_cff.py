import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/00D9D443-C7F6-E911-8884-008CFAC91E04.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1EE2AA3F-CEF6-E911-AB7A-CCC5E5F2B53B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/24CAB050-CEF6-E911-8A18-28924A35059A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2A64513A-DBF6-E911-B530-00259075D706.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2EF19E13-CEF6-E911-94AB-AC1F6BC67D48.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3A9B6A7F-F4F6-E911-AEBA-0242AC1C0505.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3ED71882-C7F6-E911-B2CC-0CC47AA99070.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4AAAB118-BDF7-E911-9AE3-7CD30AD099EE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/72B16335-CAF6-E911-95CD-0CC47AFF23DE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7EFEBEB0-59F6-E911-BD74-FA163E629AEB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8A6BF9E0-D4F6-E911-B666-AC1F6B1B2390.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/92EEB83D-CEF6-E911-82F8-24BE05C4D801.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/98A4D14B-27F7-E911-9225-0025904B5F8C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A6EA8244-3EF6-E911-9298-AC1F6BAC7C0A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B6E8BF02-D5F6-E911-9B19-F01FAFD8EA6A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BE9FD817-D4F6-E911-A40F-509A4C74D18D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C28F2687-37FB-E911-938F-B496910A85E4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C462BE79-27F7-E911-8816-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C88BA3C6-F6F5-E911-B32A-AC1F6B0DE3A4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/CC1D56B6-F5F5-E911-873D-B083FED42FE3.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DE6744FB-D3F6-E911-8A0C-246E96D14D9C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DE73B518-D5F6-E911-99F4-90B11C08CDB7.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/ECA00FEC-DAF6-E911-BD72-20CF305B0629.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FA109A1C-8DF7-E911-8F3A-00259090785A.root',
] )
