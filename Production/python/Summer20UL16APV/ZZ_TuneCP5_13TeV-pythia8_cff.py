import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6E42E93D-96EE-5940-B07B-35851285CF30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C0051D0C-6E54-1E44-B9FA-011FF426642C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/597EB941-BBDA-344F-A8C8-DD2F8145C1F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/772928C3-D67D-7746-8F6B-E741CF738D9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/7CD35730-B392-1C4E-8B52-D5B631811479.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/820FB410-DDB3-A24A-8153-83834097BFC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B1184556-3B72-8D43-8BF1-A28B63B8A0B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DE59CE94-FA5A-1B47-90C6-F23860AF66AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/33F5EB42-ABC0-8745-AA1A-35289352DA07.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8FDD2286-E4D8-9C4A-AF75-29D51496B36C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DD4A6C52-8B60-7C46-8C60-2575E2A5B7EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/082C070C-DD5B-DA4B-B8AA-FAC3861B4E9D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0899DF26-C9D9-2B43-9AA3-649DAD5403B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1207C3E4-4455-2A48-AED5-71D5B6EFD3C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/180886B3-DFEF-0E4F-853E-96CBB15A4D5E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/32F76380-32B8-4D44-A866-9A92CC08F787.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/330B1DBD-6423-D045-B9C7-D70CD187D72E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/425AD4EC-1F3D-624A-9846-6FD2BDA7986E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5CABB9D2-9C68-0C4E-8D18-8C697920B0D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/973AF36F-FE91-8941-BE4A-E47BD5C498B5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A6E5AF95-C063-EE4C-9C14-C0D23FA0DF4B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B1386010-7796-5B40-AF3D-5D2C56D807F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B5CB890A-EF1A-464F-858E-3C27CF913722.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/BFC826A3-5055-2F47-8C06-5B19FDF0BBBE.root',
] )
