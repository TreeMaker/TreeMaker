import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/08E810B2-9436-E911-A812-44A842BFA958.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/18B060EA-C036-E911-BD07-7CD30AC03006.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/30291477-8B36-E911-B5A5-44A842BECCBE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/32A2911B-7A37-E911-B32F-44A842B45218.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/34E389C1-9436-E911-988E-44A842BE8F8B.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/3A2DBF9C-8E36-E911-AB4A-B496912ED83C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/3E5D5516-B436-E911-8BD8-7CD30ABD2EEA.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/44BF8C08-B936-E911-9CFD-44A842BE7718.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/4C4CBB0C-8D36-E911-8659-44A842B45218.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/56AA88BC-5637-E911-9295-F04DA27541B7.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/74A8E515-BC36-E911-8E16-7CD30ABD2776.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/7A7DAA6F-9A36-E911-8BD6-7CD30AC030F8.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/828A0CC2-9436-E911-8128-44A842BFA93E.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/86A260BB-9436-E911-A40A-10983627C3DB.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/9A75815F-C536-E911-8EBF-F04DA2753F56.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/B4025E62-9936-E911-946E-00266CF85838.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/BA055603-C536-E911-BF36-7CD30ABD278A.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/CA1244DE-9836-E911-9026-405CFDFF4801.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/E80BE91B-C236-E911-B79E-44A842B2D658.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/ECC05DEA-C036-E911-A1AC-405CFDFF4828.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/F216B960-B636-E911-8B56-44A842BECCBE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/FE4530D5-9436-E911-9536-44A842B4CC71.root',
] )
