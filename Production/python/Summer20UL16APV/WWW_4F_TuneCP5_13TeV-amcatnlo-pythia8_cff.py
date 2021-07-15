import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/087049AC-49A7-A649-ABFC-8D0504846B74.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/1312B229-F8FD-AB45-91A3-CA64D0B4BB4C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/390BF1A3-79E5-6342-B68C-CFD0EC7692CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/47D756BB-84C2-DD4F-96E0-8D1813A7F621.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/54A11885-3024-A449-AE67-BCFDC94F259D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/70974549-1130-9C43-85F3-359363106092.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/767304BB-8571-9247-BD56-126D744C0E3C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/8DD026EF-34C8-204F-9CA7-7B44691B8429.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/B4EA5DFE-FE5E-C34F-9611-1AF205B7FFC7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/BB44CDCF-5872-A048-BAFE-B52A077EEF38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/CD13E259-8703-564B-961B-E6076656BC50.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/D47ED47E-16E9-3D4C-88A3-C96DE4F1D5CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/D504739C-1995-2F4D-8F35-C9D40D970931.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/D81BB996-8CA3-2748-A555-ABA94B11730D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/E964C6A9-B699-8940-8407-49A98D6EE864.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/FA8D6DF2-C58C-E14B-9C73-E78AB181C43F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/FF0BC22B-E10E-5244-AD6A-20B50A5F84AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/FFC3B2AB-C354-B141-9342-914ECBE8494A.root',
] )
