import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/243ACF6B-C005-EA11-BC79-782BCB539A7E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2CAFC1CB-C805-EA11-B23F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3EE37956-450A-EA11-AF77-002590FD5E80.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/489397C8-460A-EA11-97B8-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/4AA5417E-B905-EA11-B5B2-0CC47AFC3C64.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5060C9DB-DB05-EA11-81F5-001E67DFFF5F.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/609070B1-B505-EA11-9EB8-00259090768E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/760BEDF1-B205-EA11-86A6-00266CF3E0BC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/8A2F691F-B305-EA11-B5AC-7CD30AC03006.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/947B6C6D-C005-EA11-8A1A-0CC47AD98D0C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A0BA136F-B305-EA11-810D-EC0D9A82260E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C2C045F2-BC05-EA11-B049-FA163E786846.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DA23AC15-B305-EA11-8A67-B49691386D14.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1350_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/DEBA13D7-BF07-EA11-903B-AC1F6B1B2364.root',
] )
