import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/102EA7B4-5EFD-E911-93AF-FA163EFAF66A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1A18287B-5FFD-E911-A575-00259029E71C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1AA25358-5EFD-E911-85BF-F4E9D4DF2910.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/54179062-5EFD-E911-8E67-00259090840A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/562C8D58-5EFD-E911-802C-001E6779276A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/56CED607-5FFD-E911-9A08-0023AEEEB538.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/587905E1-5EFD-E911-A8C6-141877411D77.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/5A99BB71-5C00-EA11-8F9E-3CFDFE639860.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/64A6C162-65FD-E911-8982-C0BFC0E56846.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/6C22C852-5EFD-E911-B909-6C2B59916057.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/70C136D8-71FD-E911-8DBF-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/74D5F6DB-5EFD-E911-812B-A4BF012EB202.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/783CC52D-56FD-E911-8905-AC1F6B5676BA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/80630321-5FFD-E911-A359-0022640671E8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/80F2694A-5EFD-E911-BF12-00259073E42C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/849B7FE0-73FD-E911-A783-AC1F6B596094.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/8C9E4F09-C5FD-E911-87FB-3417EBE34C42.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/96AC5170-67FD-E911-86DC-0CC47AFF0460.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A00FE055-5EFD-E911-9AE9-44A842B451FE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A667A55A-5EFD-E911-B00D-0090FAA57C74.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A806B758-4B00-EA11-9860-D4AE5264D964.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B0CF9AD2-6AFD-E911-8681-0CC47AA98A32.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/E6D0BEE4-89FD-E911-9BD1-0CC47A7C34A0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/F04CB87D-5DFD-E911-B079-98039B3B0036.root',
] )
