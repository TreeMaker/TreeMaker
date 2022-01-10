import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/0B1DFDBA-3F5F-7149-A677-2692FEF75344.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/0BAEF45D-8996-CC46-B8EA-6E93E0BA5B82.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/1DE5F5AA-22A8-7443-AD6E-282839863A39.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/29EBAF9E-1BFF-9C41-803F-BDEA2AE2DF3A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/2A369B30-F608-FE45-8611-7CD2EC5C5DB0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/3F405F2D-FF6D-8647-9378-163F4B2D28C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/4CD3A880-B618-1648-B73A-D822FDEF0D44.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/554E0D44-7F3E-1D44-8DE2-36CF1818D496.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/7E15B210-D203-E84D-8381-BEF4E61BF789.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/87D254F3-0CA9-6A43-B9F5-926C0ED04675.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/BD69E424-81C4-0643-ADF2-DF0E98FE29FD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/DAFB04BE-AB42-2A47-8474-FDFDDF92F7B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/DC83F373-A849-9D46-8D4B-190245A98FF6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/E3568C83-9F5C-E049-9778-7A7A781D66D8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/E68E5195-57A2-2344-B2BF-03D472A7DA5F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/F49A0414-F8D4-8F45-9B87-20598A1170F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/04A2066A-22B0-124D-A7FE-FCD61FB4930E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/290BAB49-3F57-6E43-B1E3-C558707C9E82.root',
] )
