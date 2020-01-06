import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/06F1D366-0F00-EA11-B433-C4346BB2E5F8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/2668CC93-F3FF-E911-9BF9-F4E9D4DF2750.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/2E544000-2E00-EA11-B64A-509A4C85407E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/2EE19473-AB00-EA11-A592-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/420A17FD-4900-EA11-ADC8-44A842BECCB1.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/4C411CFF-7900-EA11-A8AD-48FD8EE739ED.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/6EC9DA6C-2100-EA11-9C40-0CC47AFF24D6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/7805C38A-F3FF-E911-A733-38EAA78D89AC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/88439989-4D00-EA11-BB61-AC1F6BAC7EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/9CC87F5B-5B00-EA11-9DC5-0023AEEEB208.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/A0A2C357-5B00-EA11-A861-AC1F6BC67D46.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/B0BF1B2D-F2FF-E911-9BEB-008CFAC91720.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/BCBA200A-F5FF-E911-9633-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/C0075C55-FFFF-E911-803D-24BE05C3CBE1.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/C67D5F56-5B00-EA11-A961-002590DE6C96.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/C6CDC60A-4500-EA11-8BC2-002590766A2A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/D84E2325-F0FF-E911-AAE2-001E67DDC051.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/D86B84E5-20FF-E911-B281-FA163E7555EA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/DA0BBA4C-0E00-EA11-B69A-008CFA1983BC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/E44FC6FC-0800-EA11-9256-00259090765E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/E89DAC96-FAFF-E911-8A80-98039B3B01D2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/EE2AC79A-F3FF-E911-8FB4-20040FE9AD64.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/F67F0880-F2FF-E911-91CA-90B11C2CA412.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/FCBF92D2-0600-EA11-9951-002590A887F8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/240000/FE91168E-F3FF-E911-AB9B-002590FD5E80.root',
] )
