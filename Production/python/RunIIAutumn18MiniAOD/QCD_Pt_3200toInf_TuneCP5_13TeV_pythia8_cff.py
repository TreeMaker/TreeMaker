import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/30E98A35-64A0-5B4F-AF1B-EA6B48E3D57B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/39AA776A-67EA-9046-854E-8F30F4241BE0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/3D5015B2-5E6C-9E4C-B953-1F3C20DC7AC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/3F34D2E3-32F9-254D-B2A9-8505EFC56A9C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/75B89C7B-BF48-3A45-A388-5E4C119F0FCF.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/8DED36E2-153A-E146-AEA2-2AC3FAFF7C53.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/9504CE81-DDC5-FA40-A9F7-88C834BF34C2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/B4550FC7-C066-1D43-B339-9072D5B579F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/D367383A-E27D-AC4F-BBDF-2C6081435DD6.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/DA2298E4-9C76-2E42-A042-612B177ABAD1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/EAD44B1C-2F84-674F-9F61-570D92C7F697.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/EBC3F97A-550F-C742-955D-5F2E28D45A55.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/270000/FEDC3CC4-69C4-0A45-A04F-CAB3B4F16673.root',
] )
