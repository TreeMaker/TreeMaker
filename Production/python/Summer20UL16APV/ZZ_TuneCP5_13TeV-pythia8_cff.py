import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/0213F743-07E7-974A-89B9-41376EB5D52F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/29DE436E-E29B-FF41-999C-95755EB1FADE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/2A023AB7-EBC4-DC4C-8F4C-F6D726461B1B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/2EC6189C-1A5A-C148-9B42-45A35E8C0AFC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/2F1F6FA3-E9D1-0D4F-A25B-8977D6B1CB9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/30C2742F-514A-C543-B942-2308ECFE0FA0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/34FD4CE0-6359-EB46-ABA3-4D2B06184838.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/3EF3BDD7-E3B4-2747-9074-F639ACC3435E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/4959B2C7-048D-DF40-A7C5-55BC8EB16AFC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/4AE63132-363C-9C47-832E-56CE86E4A9F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/54838C12-E7F6-2048-AF11-12DD10871B28.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/6591BFE5-B007-A241-9740-1D6591EFCCC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/6770AB8C-966A-0A42-8061-850A9ED047D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/6C684702-358F-474E-A8A0-692716538142.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/7595397E-9CF1-2E45-8F4F-1C0CDBD43E71.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/84F1E4EE-2ADB-4B44-8186-0BA2AD629FC0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8E83CC3A-29FB-A54C-B4AF-32171F924999.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/95EDB15B-A645-0E4B-B538-1A18E9C8DBAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/A0D808FF-E9EC-1340-AE9B-03D2E215CC2A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/A1A33AB2-A06C-2E4E-A68B-25FBBE773BC8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/AFA23FD4-D30A-3045-8531-DBC4CA4B05FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/B2FA4AB6-CBD3-4E4F-BBD4-AF9B55FC1D66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/BAF40FB7-356B-EF48-8D5B-7D0F11F808F9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/E26C6744-F07C-6940-97DD-EA21AD812F5F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/E91E1D6E-22D3-254B-8392-0F3F3D3E8DA1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/FD86B199-CAE1-664E-A387-1139E826FEE8.root',
] )
