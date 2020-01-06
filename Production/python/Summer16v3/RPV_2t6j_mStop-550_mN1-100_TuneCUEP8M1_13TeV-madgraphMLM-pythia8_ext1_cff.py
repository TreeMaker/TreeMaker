import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1419D9C8-C4FD-E911-BC01-7CD30AD08974.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/18D2106D-5EFD-E911-B352-001E67396DEC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/22A4777A-5EFD-E911-A52F-0025905504C8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/24E318DF-67FD-E911-9ABA-002590D60056.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/463FFC5C-65FD-E911-9263-C0BFC0E56826.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4C7D9BC7-67FD-E911-AD27-7CD30ACDCBA8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/507877E6-5EFD-E911-BF78-B083FED406AC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/5A580C59-5EFD-E911-B931-48FD8EE73ACD.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/70764442-5EFD-E911-828E-00259090821E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/74F1045D-5EFD-E911-99FB-B49691554B28.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9017DF29-61FD-E911-ACA4-AC1F6B799D60.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9C6B8ABD-5DFD-E911-A934-98039B3B0036.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AAE012DA-71FD-E911-A4F7-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AC595D63-68FE-E911-8BD5-AC1F6BAC7D18.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/ACB86FE2-73FD-E911-83B7-AC1F6BC67D50.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B0F4193A-6EFD-E911-936A-0CC47AFF0640.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B0FA1750-5EFD-E911-A7E2-24BE05CECB51.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B2C940BF-5EFD-E911-B710-FA163EDD6208.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/EE3CBB08-5FFD-E911-AEAB-1CB72C1B6574.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/EEA945ED-73FD-E911-8C9D-001E67A3EBD8.root',
] )
