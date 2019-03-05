import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/12971E7E-A9BC-E811-A71A-0CC47A1DF800.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/44746303-1ABE-E811-9CFE-002590E7DFFC.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/669733EC-67C2-E811-BDB2-AC1F6B0DE0A0.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/78957431-81BD-E811-B797-002590E7DFFC.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/88C4E954-9FC2-E811-85DB-0CC47A1DF800.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/8A83078B-71BD-E811-AC50-0CC47A1DF7E8.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/E4EE1406-EDBC-E811-A46A-0CC47A1DF800.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/FC5C8FE6-C0BC-E811-AE16-002590E7DF2A.root',
] )
