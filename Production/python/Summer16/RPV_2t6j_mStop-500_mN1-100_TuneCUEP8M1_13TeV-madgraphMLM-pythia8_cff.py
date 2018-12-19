import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/14416677-D7B0-E811-975D-90E6BA693E13.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/149471FF-D7B0-E811-B2A4-90B11CBCFFC3.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1ACF8FB9-D7B0-E811-A8CF-FA163E1B54C5.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/460DD0D2-D7B0-E811-994E-1866DAEA7D94.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4A47C8D3-D7B0-E811-A757-002590D6013C.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/504AB47A-FAAB-E811-9C1C-002590E2D9FE.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5C6254A1-D8B0-E811-914E-0CC47AB0BB0A.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/605EF5BF-D7B0-E811-B735-A0369FE2C0D2.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6693169B-D7B0-E811-8DCE-20CF3027A58B.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/945DF7C6-D7B0-E811-A1A8-A4BF0112BE12.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/96E15FC4-D7B0-E811-BC14-0025905C53D8.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9E97A7C3-D7B0-E811-9424-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A44D90A6-D7B0-E811-AD14-002590DE6E72.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B425E393-D7B0-E811-8A0B-44A842CFD64D.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CCA9DCCB-D7B0-E811-A29A-782BCB3BDD3B.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E0513896-D7B0-E811-A8F4-1C6A7A21B70D.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EC664EB4-D7B0-E811-8D42-5065F3816291.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FCCE67C3-D7B0-E811-8B74-0CC47A4D769C.root',
       '/store/mc/RunIISummer16MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FCE6AE6E-46AB-E811-9CB5-5065F3819221.root',
] )
