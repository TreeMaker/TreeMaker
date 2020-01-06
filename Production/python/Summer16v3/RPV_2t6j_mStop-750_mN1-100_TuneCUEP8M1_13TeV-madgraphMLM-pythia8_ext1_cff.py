import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/3CFF79E1-BBFD-E911-ABA1-002590DE6E36.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/48E28376-77FF-E911-B928-008CFA0A5818.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4C23453E-FBFD-E911-8FD2-0CC47AFF01F0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/564F2B8B-05FE-E911-B802-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/5A0CE967-CDFD-E911-B5C8-7CD30ACE1660.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/5A3E5965-05FE-E911-A524-1866DAEB3370.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/5CB29590-13FE-E911-BC67-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/627AF5C0-C4FD-E911-BA7D-002590907802.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/64CB61BF-01FE-E911-852E-20CF3027A670.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/6A9F8444-07FE-E911-9056-7CD30AD0A78C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/6E279C4D-FBFD-E911-A4EF-A4BF01125AF0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/8C31C12B-4DFE-E911-8115-B496910919E0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9A2F11F5-4FFE-E911-A579-0025905B8580.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9E0D2BF7-BBFD-E911-80E3-6CC2173CAAE0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AE39CEA7-FEFD-E911-B81A-6CC2173BB830.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B061CE3A-05FE-E911-B07A-506B4BB16AEE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/CEB4CBB7-D8FD-E911-A6FA-002590FD5E70.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/CEEC78A7-FEFD-E911-B8B8-0CC47A0AD6FE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/D082555A-CDFD-E911-8C35-002590DE6E1E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/DE77FC39-07FE-E911-811A-FA163E84C351.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/EA2B1482-05FE-E911-9C45-AC1F6B0DE45C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/F20374A3-FEFD-E911-8499-20CF3027A5CA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/FEBD0A85-29FE-E911-A28A-0CC47AD98D10.root',
] )
