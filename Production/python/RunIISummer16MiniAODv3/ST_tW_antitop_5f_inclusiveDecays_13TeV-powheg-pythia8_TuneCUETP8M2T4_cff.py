import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/0241B420-58BE-E811-8789-10983627C3DB.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/0AB542C7-FCBD-E811-822D-3417EBE528B5.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/32BC3662-F8BD-E811-BD07-44A842B298FE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/38EB9602-F5BD-E811-A05C-3417EBE528AF.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/96A087A1-FCBD-E811-82FE-549F351EDC46.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A031F93B-F1BD-E811-A9D1-F04DA27542B9.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C8A3003B-F1BD-E811-A223-008CFAF554C2.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/CA87BF5E-FBBD-E811-B082-44A842BE8F71.root',
] )
