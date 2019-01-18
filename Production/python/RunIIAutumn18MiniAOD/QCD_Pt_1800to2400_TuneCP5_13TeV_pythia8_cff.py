import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/034E4F4A-8843-024B-BB81-160D0C69B88B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/1C9C6464-9CD3-2E49-82F5-00F2016AB768.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/3147C044-AABE-B742-91EE-7D2980A568D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/4760F95E-EF44-7546-B36C-BF86D6C0FA5F.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/493DFCD6-5D97-B746-B867-5AE7805EFF27.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/52BFA9F8-9E12-AE46-97D1-2712B3C342FA.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/53A787EF-A5D9-674E-8657-209682157492.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/5FF611F6-7694-9F4B-BBAE-1178E7F10993.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/69786076-5A17-1144-9E68-EA5F920B5C18.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/8071155C-0F79-7646-8C44-CAE82DE07AD3.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/813EF9CB-0AE6-A442-BC57-EE8F48CCDCA6.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/84710671-3D8C-5946-BFAF-F9068220CD70.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/85913998-23C8-4540-A3A8-8366BD198B9C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/9CD888EE-757B-1B41-8AC5-120502023A74.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/CF60A693-4CC7-5041-ABED-4ACCB773ABA0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/DC251B28-9A18-AB40-8751-1CAD6F605E99.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/FF66C5A6-7B60-C64C-93B9-F34A9395A908.root',
] )
