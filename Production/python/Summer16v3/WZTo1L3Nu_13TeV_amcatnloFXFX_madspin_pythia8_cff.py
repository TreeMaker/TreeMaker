import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0EDE7FD7-F4F0-E811-AFE8-44A842CFCA1A.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2ABEE3C7-95F0-E811-8B29-6C3BE5B5C0C0.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/346353B1-ABF0-E811-8A91-6C3BE5B54138.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/36896BD2-F4F0-E811-A568-44A842CFD60C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3E3370D0-21F1-E811-A93C-001F290860A6.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/487D51FA-81F0-E811-97F8-001F2908BE6A.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/582E17CE-F4F0-E811-AFCF-44A842CF0600.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/7667EAB1-6EF0-E811-BA35-44A842CFC9A5.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/94853DF0-F5F0-E811-A5E8-B499BAAC0658.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/AE969E72-F6F0-E811-8EA5-6C3BE5B533A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/B21049C2-A1F0-E811-ADCC-6C3BE5B580C8.root',
       '/store/mc/RunIISummer16MiniAODv3/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/FE0BEDDC-78F0-E811-8531-B499BAAC0694.root',
] )
