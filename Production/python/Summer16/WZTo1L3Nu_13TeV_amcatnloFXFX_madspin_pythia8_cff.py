import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CADBC31D-8BC8-E611-84C5-008CFA111330.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/0404AD1F-ECC9-E611-8265-008CFA1979FC.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/045F6F63-D6C9-E611-B687-008CFA111184.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/10F46626-DFC9-E611-8EA0-008CFA110B08.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/2C5C2376-DBC9-E611-A3D3-008CFA110B08.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/2C960E2F-DAC9-E611-8C90-008CFA110C6C.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/3217C27B-E4C9-E611-A7D2-008CFA197448.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/42A6B260-F2C9-E611-9800-008CFA197C58.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/46476B0C-E9C9-E611-9B8B-008CFA110AA8.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4EE7030E-DEC9-E611-8256-008CFA197AC4.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/50E11406-D9C9-E611-A37C-008CFA197AA0.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/6634DCFE-DCC9-E611-9EE4-008CFA19741C.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/669CC53D-E3C9-E611-9C5C-008CFA111330.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/66EC11E3-CAC8-E611-9A6F-008CFA197B34.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/7072CEBA-D2C9-E611-BE2E-008CFA111184.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/8EA17CC9-E1C9-E611-A016-008CFA111314.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/90D54689-BCCA-E611-A205-008CFA1111AC.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/BAAF2417-C1C9-E611-89CD-008CFA197C70.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C874268F-E7C9-E611-BEB1-008CFA166234.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/D221575C-E6CA-E611-890B-02163E019C33.root',
       '/store/mc/RunIISummer16MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FEDF0DE6-99C9-E611-AD15-008CFA111330.root',
] )
