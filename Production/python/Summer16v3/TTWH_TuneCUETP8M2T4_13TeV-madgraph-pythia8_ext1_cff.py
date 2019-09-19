import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/043319B6-702A-E911-80A5-A0369FD0B2F4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/06E6B3D8-5D2A-E911-8002-18DED7C60DEB.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/0A01EC5E-5D2A-E911-AD5F-0023AEFF2D80.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/0CA8954B-6E2A-E911-9919-001E677928E2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/24379B01-5C2A-E911-8BFA-90B11C2CB7A9.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/326FBD38-622A-E911-9610-002590D9D822.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/3A3EEEBF-6E2A-E911-B89E-002590E7DF2A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/46910263-5D2A-E911-81E7-0CC47A5FA211.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/56EBD9EA-5C2A-E911-AC43-C4346BC7EDD8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/682411EB-5C2A-E911-85F5-3417EBE644BF.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/6884DD1E-5C2A-E911-8679-38EAA78D8AD0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/7A814AA9-5F2A-E911-8EA6-0025905C3DD6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/8CA248CF-5D2A-E911-AE1F-40F2E9C6ADBA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/9216428B-972A-E911-8342-A0369FC5D92C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/9CEB6C66-5D2A-E911-880B-246E96D10CC4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/B41BA014-5C2A-E911-8528-FA163E4006D5.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/B6CE09FF-5C2A-E911-AD2E-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/D4D65015-5C2A-E911-B73E-0CC47A7FC72C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/EC6FFCBE-8C2A-E911-AA0C-20040FE9BCD4.root',
] )
