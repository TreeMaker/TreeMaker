import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/03FF2AFD-6892-474C-94DC-1BD71DDB7AD7.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/0B0DDCA0-308F-534C-9156-FBB9CC5D7744.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/16081B03-24C6-494A-81E9-F5B2E560B09D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/25C4CED6-6437-F040-8AF4-9019DB6E86C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/3C3675A2-17A3-4F47-9322-837FD0791376.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/42730F25-A0A0-BF44-A5CC-BC9FFD3C4825.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/451D5865-6C2B-E24B-B4B4-4D1F9F45CD2C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/57DF0EBF-F73A-6C44-B9D2-AAB79490B752.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/59BCC291-84DB-8544-968D-1F9D924D1F5D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/5C70DDC8-B460-DB48-B99B-EFE4F871B544.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/7324D60A-7570-9D45-B33E-304F990EE79A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/8038E520-7BF7-CC4D-9E8A-BD0E78DC9AC9.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/9473C9D4-EEC1-F846-9AE5-263F6A66C1DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/A97B9CA4-6072-304D-A090-8CE8F1E559AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/AFFF878E-0FA2-F346-8F69-86A0947A85F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/D78C0CFA-90A6-D942-AD2A-90D5ED335FBB.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/D80551FE-DAD8-2C45-9342-52661D87885B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/F38166DC-7E4B-3541-B8CF-6095425D79C2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/FBA4139B-B86A-3844-A056-E6039F5B7432.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/FF3575E0-DAC9-3F42-82F6-C6EEF90E83A5.root',
] )
