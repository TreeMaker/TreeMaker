import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/069ADD35-C4F6-E911-A715-AC1F6B56768C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/0C0A95DC-F4F6-E911-8C20-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/101C4E5B-CAF6-E911-8EF1-0090FAA58D64.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/20A8B846-BFF6-E911-B9D8-FA163E8531E0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/485D6413-B9F7-E911-91FF-3417EBE2F0DF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/622E186C-BDF6-E911-9EB2-44A842CFCA1A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/767E33C1-E8F6-E911-913C-20CF3027A6B0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7A5E91A6-C1F6-E911-9F63-A4BF01025C16.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A2F2C4BC-C0F6-E911-A35C-0CC47A6C1818.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A4DC907A-C3F6-E911-AF59-44A84225C629.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A6886E85-37FB-E911-BC10-B496910A80D4.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B044BE7E-CDF6-E911-94BB-B8CA3A70A410.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BE4C4610-1BF7-E911-A7F3-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C4506A28-BCF6-E911-9622-10983627C3E8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D0002215-C0F6-E911-A6B7-B02628750F30.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DCC8DECF-37F7-E911-947E-0025905A60B0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E8F09956-BDF6-E911-AC2C-0026B9277A18.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1250_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F0C53900-C4F6-E911-937A-90B11CBCFF82.root',
] )
