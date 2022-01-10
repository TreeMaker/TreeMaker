import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/1933FD81-AF44-0D4C-BF34-93086509A5E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/67B8456B-B3E9-6A40-ABA2-7059E34FED0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/25010000/A96386BE-CCC0-4946-B090-BE193732A064.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/0F75BB18-C69A-6F42-B77D-6F1A33E4F3E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/18C07C98-4224-014D-887D-FA3D386BD697.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/33D0EDA4-C684-C546-9B60-9FBC5AF9E838.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/7673F551-33DB-9E44-A251-F898194F64AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/A324ED93-E681-9146-9FDA-ACA5B66F6631.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/895C3ACB-8985-E045-8A57-FCDDC74AE5F6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/CFD59EF8-5319-3D48-A037-1CDDFF27ED6A.root',
] )
