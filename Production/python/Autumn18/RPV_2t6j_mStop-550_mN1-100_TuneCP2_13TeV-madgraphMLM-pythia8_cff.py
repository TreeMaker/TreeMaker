import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/22A32F8D-3AC1-BB48-97EB-3AD5998A9398.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/2F587617-BB0F-8B41-A0D9-D31097DADBE9.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/3211EA42-81F8-624B-992C-B3A2FC8A0A3F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/372A7609-A496-DE4F-897C-25F291CEC5D6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/46DA71BD-4B89-364B-B2B7-A5230146F3E9.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/48C7CFCD-0905-924B-853E-AF045D56ADE6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/8C85C26E-6F22-D44C-8F9E-1F99F0686DB3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/8F54F165-9CEE-784B-A3BB-6A1A05E00918.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/91BDC0D1-4019-D648-AB88-B05A868C27B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/A0D5A6F1-C559-0741-B75F-0598CF61A02A.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/AC4AF6B9-EBB7-2041-9152-73D35A204136.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/B10E82E3-1966-0E42-A322-53065CD24EDD.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/DE6F00A0-B3C2-B644-A5BE-2A0029D5406D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/FC406309-EAD0-7D4A-B318-E83B77127147.root',
] )
