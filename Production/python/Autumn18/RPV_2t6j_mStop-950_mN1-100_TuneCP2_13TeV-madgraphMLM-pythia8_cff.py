import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/57CEB83E-AA88-1842-A969-42D2C63A49A7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/659D2096-12A1-804F-AC05-C7D3B018FC14.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/66D7B0A6-D384-3D4F-893A-593F3980E31D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/844CB9D9-8C4F-E14B-8BC8-CCAAE8D7574A.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/A048D466-A923-C744-ABEB-F9BCC6014C8E.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/A7278AB1-3F54-CE45-A5FC-567C2FD66DA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/C2B3598E-69B1-1A44-AE1F-3D441D55C39A.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/CC34A69A-596E-9945-B935-51CDF7E9E4AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-950_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/D5F0C70A-A753-264A-899E-97027A8EB678.root',
] )
