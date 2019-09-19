import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1669EA96-29EB-E811-A8FD-0CC47AFB7D80.root',
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/20171122-29EB-E811-A782-0CC47AF9B32A.root',
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/224D8E0D-29EB-E811-81C0-003048947BB9.root',
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3EABD078-29EB-E811-97FC-0025905C53A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/728279CE-29EB-E811-AF28-0CC47AFCC39A.root',
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/8E1E1AAD-29EB-E811-A861-0025905C2CEA.root',
       '/store/mc/RunIISummer16MiniAODv3/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9439498F-29EB-E811-B02A-0CC47AFCC626.root',
] )
