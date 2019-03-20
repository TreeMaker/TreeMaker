import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/00399DCF-F127-E911-9F2F-001E67E6F5EE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/0242F6E3-EC27-E911-A50D-A0369FE2C0DA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/12F0ECEF-DA28-E911-BE70-0CC47A7C35A4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/30785707-DB28-E911-BFFF-003048F23B78.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/32B44C1B-EA27-E911-B48C-A0369FE2C1FE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/3E27FBC5-4C29-E911-A2ED-801844DEF4E0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/5CD8FA20-E327-E911-AD9C-AC1F6B0DE0BA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/62998835-4B29-E911-B480-0242AC1C0506.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/80D987F3-DA28-E911-A271-A4BF0112BE0E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/8A6B2EED-DA28-E911-B127-001E67CBE45A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/8AB027EB-DA28-E911-955B-001E6779272C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/9EC5370A-4B29-E911-BD30-002590FD5A78.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/D449F424-4B29-E911-B87F-001E67E6F8D7.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/D494ABF2-DA28-E911-920A-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/D89A25EB-DB28-E911-B57E-AC1F6BAC815A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/DA1CE7BD-EC27-E911-BAE8-001E67792626.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/DC9D9A60-4E29-E911-A9F4-A0369FD0B28E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/E8BE1CE2-F127-E911-B2ED-001E67E71A56.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1275to2225_dM-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/90000/F0A575C4-5229-E911-ACE2-0CC47A4C8EA8.root',
] )
