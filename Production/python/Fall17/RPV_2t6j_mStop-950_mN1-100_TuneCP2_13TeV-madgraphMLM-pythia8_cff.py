import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/1A837F59-18FE-E911-8C46-FA163EA3E5D5.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/DA1C6687-18FE-E911-B6C0-0CC47A4D9A40.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/EAE18390-F7FF-E911-A291-AC1F6BAC7C06.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/EC68A8B0-72EE-E911-92D6-FA163EC5E53E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/250000/06AE2384-0701-EA11-89D7-E0071B7A7840.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/250000/9C59ACFA-0701-EA11-A0B9-F4E9D4AED1E0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/250000/9CAE66AA-0701-EA11-A92D-001E67792786.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/250000/B40157B8-0701-EA11-9317-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/250000/C4E8C7C8-0701-EA11-881E-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/250000/CC022AC2-0701-EA11-B593-3417EBE64A7D.root',
] )
