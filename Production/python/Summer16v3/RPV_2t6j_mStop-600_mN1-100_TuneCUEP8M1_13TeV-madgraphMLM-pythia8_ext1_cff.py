import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/04EE84EE-55F9-E911-A350-28924A33AFC2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/08752AF4-51F9-E911-AD50-00259048BF92.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/22BE317F-84F9-E911-9A28-0CC47AFF0478.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/3EF189D0-5EF9-E911-ABA7-141877411E9A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7A6836EB-61F9-E911-B05B-002590909126.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7AAD6EA1-51F9-E911-9B1C-FA163E6257D8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7C33F538-B0F9-E911-BD07-0CC47A4D76AA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7C9B7671-70F9-E911-87E0-6C3BE5B5F0A0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/8AD4BFC2-4DF9-E911-B664-002590DE38C8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/ACB75339-4DF9-E911-9A89-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/B6E4C5CD-87F9-E911-8940-842B2B6F81CC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C0FE727D-70F9-E911-8F0A-44A842BE76FE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C42D7603-55F9-E911-8847-0CC47A4DEEF0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C89E5B6C-55F9-E911-9C86-20CF3027A6DA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/CECED247-90F9-E911-AD5D-AC1F6BC67D48.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/DE3D6E8D-2FFA-E911-8F48-C0BFC0E5684E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/E0993EBA-4DF9-E911-BFB4-509A4C9EF8FF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/F2024672-2BFA-E911-BC3A-509A4C7489E2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/F2E147E8-A7F9-E911-BD6E-E0071B695B81.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/FEFDBD0F-B5F9-E911-94F8-F4E9D4DF1F70.root',
] )
