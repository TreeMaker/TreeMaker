import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/0A5B5361-4058-E711-B497-008CFAF558EE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/1402B376-5158-E711-BB16-02163E013B28.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/288F2485-7158-E711-9741-A4BADB22A4AE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/3C876E8F-3E58-E711-8D84-0425C5DE7BEC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/46698515-ED57-E711-864E-00266CFFBCB0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/486B5CAC-A758-E711-B77B-002590D8C68A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/58F063B5-5758-E711-BF62-BCAEC5097201.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/667840A2-3458-E711-A317-0025904C6624.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/9661A77E-FB57-E711-A73C-80000025FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/A6F10E58-4C58-E711-BFDE-44A842CFC9CC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/BE6B09BC-A757-E711-B94F-549F3525A184.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/CE3A0430-5E58-E711-88D0-0025905B85FE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/D81B9F8C-9E62-E711-84D6-001E67457E36.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/E8943A91-4858-E711-9615-008CFAF721CA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/EA9EEF23-7758-E711-80FD-002590D9D8AC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/F8E852DB-8B58-E711-930C-0090FAA56994.root',
] )
