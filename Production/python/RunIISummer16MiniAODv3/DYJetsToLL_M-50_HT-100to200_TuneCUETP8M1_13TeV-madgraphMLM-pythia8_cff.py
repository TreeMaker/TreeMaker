import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/6266DD8E-E2F3-E811-AD96-0025901D09D0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/00CAD7E1-93F8-E811-925B-008CFA111240.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/00FE6C29-97F8-E811-A0A7-008CFAC91A24.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/24EA672D-97F8-E811-8FAD-008CFAC91A24.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/2C01ED68-8FF8-E811-B54C-008CFAC91C40.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/3AB5394D-97F8-E811-9C2B-008CFAC91C9C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/468D57F1-91F8-E811-848B-008CFAE45324.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/4C971012-99F8-E811-9285-008CFA197E18.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/5CBB3560-97F8-E811-A452-008CFAC91EB8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/68D5919B-98F8-E811-92FA-008CFA1113D8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/6CF9A736-97F8-E811-AFF2-008CFAC91A24.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/7013692A-97F8-E811-9886-008CFAC91A24.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/7AAA1C96-90F8-E811-B148-008CFAC93DD8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/980C5921-99F8-E811-80B9-008CFAC93D04.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/C44DA5BB-90F8-E811-AEA5-008CFAC9423C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/D02F367E-9AF8-E811-A9BF-008CFAC94144.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/D2D7ED3E-91F8-E811-A2BA-008CFAC94098.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/E278704B-97F8-E811-96C0-008CFAC91C9C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/EC136E2B-8DF8-E811-9D67-008CFAC94028.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/F8135EF5-8FF8-E811-9E01-008CFA111244.root',
] )
