import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/0BF2455B-0A6D-734C-9B60-77A8A9C8FAF7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/0C1839FD-E28A-D244-8DC0-D702E2898E00.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/14C3705D-6325-6F43-8B54-496FB8128D46.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/2E83CC36-9295-1A47-B8BA-AC4D39C7177E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/3D9502F1-6870-4E4C-A291-C13B6C0F13A0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/4AC88577-049E-D249-BCF8-B17ABB8BE7B5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/4EB53D05-499C-684F-AAF9-D0BE70159138.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/577F172B-CEA8-9841-8523-CBC2201A4614.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/59D41601-4073-F946-88BD-058BD7684F95.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/5B912A3A-A2F6-EC4C-B1B5-34953531E243.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/612DCF1C-3C07-CB48-AC8C-67FD91D42F2A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/700EE678-45A9-E244-877A-92BFE1EE7624.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/750B1601-3EC7-A841-A52B-E4CB6A17A43B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/78A7E6FF-89CD-AF4B-84BB-CF58C65B6FE4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/84F661C7-B97F-F440-98D2-692287A87479.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/8B571327-0136-914B-9579-FF5F42D53666.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/90B35968-F409-0B42-9C32-57F1645F02CB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/A19C2512-E0D4-4C4C-8389-5351602D803A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/AE723AA3-43B5-8742-A131-C9FC790C8D5B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/BCD1BC9C-EFB2-5840-9956-A570F1F297FA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/C251574C-FFC5-C744-8003-17712C6BF9A7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/D3508DB5-3909-A941-994D-5F4CAFBF3330.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/EBDD88A3-BD0B-9342-8452-25416DBC9ED1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/ED5D2991-6A92-C840-97F8-AF692BAED261.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/F0CC1F4A-3196-BE44-8C80-063E8942AB68.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/F91DE53A-0297-EF42-AF46-5D67D72466B3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/FAD6F4C4-C746-254B-A51E-F1EFB28D8F94.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/130000/FE2E960C-89D8-A345-86F3-3B8800A29B42.root',
] )
