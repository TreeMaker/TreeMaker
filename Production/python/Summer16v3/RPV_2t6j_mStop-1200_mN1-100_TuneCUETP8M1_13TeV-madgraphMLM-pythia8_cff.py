import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0CAFDE50-1505-EA11-8E5C-A4BF01125780.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/18088AF5-1405-EA11-A641-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/1E263F9A-1405-EA11-84FB-0CC47A4C8EB6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/7625EA46-1505-EA11-8BDE-FA163E5DF1B9.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/7686C5E2-1405-EA11-A6D6-EC0D9A0B3260.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/86923E11-1505-EA11-A668-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/96396093-1405-EA11-94BD-008CFAFBFC72.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9694E2C9-1405-EA11-B9DE-0CC47A5FC61D.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/98328997-1405-EA11-83F5-AC1F6B0DE2EA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B0432DE8-1405-EA11-98CB-0CC47AD98D0E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B6980394-1405-EA11-ADD3-6CC2173C9150.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E6FF95EC-1405-EA11-A8C4-549F351EDC46.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/EE21D097-1405-EA11-9FA5-0025905C3E66.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1200_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/F6ACFFDE-1405-EA11-9284-24BE05C4D801.root',
] )
