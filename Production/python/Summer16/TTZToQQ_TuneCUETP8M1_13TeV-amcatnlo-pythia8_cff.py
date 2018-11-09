import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0AC42490-2FD3-E611-9800-0025904C7A58.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0CCEDFF0-3ED3-E611-9C3B-E0071B74AC10.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0E7E12C2-2ED3-E611-BF95-0CC47A546E5E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/103521A4-3ED3-E611-A69C-0CC47A7C3424.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/2450A1AD-3FD3-E611-9301-0CC47AD98CF6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/747F023B-31D3-E611-B09D-0CC47A706D18.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8473C2C9-33D3-E611-82BE-001E67457A5D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/90EB7610-32D3-E611-A549-0CC47A706CDE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/90FF6665-38D3-E611-ACB5-001E674FBA1D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/92B592B2-3ED3-E611-9C80-0025905A60FE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B09F1FDC-3ED3-E611-80ED-00259029E7FC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B8B59FB5-3FD3-E611-8641-90B11C050429.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C08EE40A-2ED3-E611-B722-001E674FCA99.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C2FC1BCB-43D3-E611-AB1F-001E67457E36.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/CCD1938C-3FD3-E611-BE6E-0025904C7A5C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/DACA11A4-3ED3-E611-8A83-74867AF198F1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E691E924-31D3-E611-8BF4-001E67457E36.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E8DFC0BB-36D3-E611-A478-001E674FCAE9.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F2F5D602-32D3-E611-A935-0CC47A546E5E.root',
] )
