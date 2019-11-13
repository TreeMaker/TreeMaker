import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/39F3CBB3-994B-8644-8334-86F1808317A7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3EFA7EA0-8003-A446-9496-BF7556222E75.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/59F34B9F-B0FD-6D47-84B8-7F2B7A00C6FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/81C6D66E-2BFF-2541-99B5-9AD545273BEF.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C837A440-4B72-E946-8362-AA4222505FA6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CA7C902F-9D08-A944-AB9A-A748E6E1468C.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E561B5F3-4AB1-EF43-9270-DD26FF9B64C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F21EA2E3-DF36-8842-A024-4D917A66BA59.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F985E877-8DD1-7C43-8671-2AD3AC3408FB.root',
] )
