import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/10B3AD26-C304-EA11-9DCC-EC0D9A0B3070.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/24326CB2-C204-EA11-A7CC-B496910A868C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2CD18EB6-C204-EA11-A648-A0369F6369D2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/32DEFCC6-C204-EA11-ACC8-0025904A9430.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3ED7263D-C304-EA11-B532-F01FAFE159DB.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5A227150-1C05-EA11-BF93-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5C25DCBC-C204-EA11-9B0F-0025904B0468.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5EC30A48-C304-EA11-9F52-0CC47A57D168.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/84890C23-C304-EA11-9776-FA163E950C5D.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/96DAC9A8-C204-EA11-BCFC-A0369FE2C020.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9A2EF722-C304-EA11-8093-506B4BB16A96.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C0E994C1-C304-EA11-A14C-509A4C858B2B.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C2095CB6-C204-EA11-8BA2-6C2B598FF837.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C60D53BB-C304-EA11-9CE0-002590908286.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D6521914-C304-EA11-A18F-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D84A6AA6-C204-EA11-9FBE-0025905D1CB2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D891E6B0-C204-EA11-B678-3417EBE644DA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DA2FE5AD-C204-EA11-9FD2-6CC2173BBAA0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E24290B5-C204-EA11-8812-AC1F6B0F3A26.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1300_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E80E7733-C304-EA11-9082-20040FE9CBB0.root',
] )
