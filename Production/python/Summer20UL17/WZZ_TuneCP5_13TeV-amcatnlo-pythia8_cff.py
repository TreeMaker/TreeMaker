import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/08394D73-7ADA-4844-A2E6-108CF7CB7775.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/1B0C30F6-D93E-D943-AAAA-5453E521E5BD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/1EF11918-202F-E841-AB54-6BF931120809.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/251ABD86-2147-B943-9928-628DA9F188DA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/329B2F5C-241E-9247-82EB-B0C109FF42DC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/3910272C-A948-9A40-A8A2-C64EAB4795A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/3DECA3B8-3048-0346-A7FB-22E471D4FB6F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/47D7AAE3-B23E-B244-8492-516490D279BE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/4CF760D9-8500-7349-900F-0D75F4F7B0BF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/5B45D025-13F4-294E-819F-875A20E17613.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/6DEC76ED-E146-D243-96BA-7BA73E35DFFD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/6F957AD4-9E95-B741-AB63-C99C5705092B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/7037B299-1D34-3448-ACCD-3F5B377687E2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/7616A629-A05F-4240-87C6-913A487CA4B3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/809F7E52-E457-3043-A261-460C4388BA18.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/9C9ADE33-808F-D249-9E94-50BF0E1C1B36.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/A34E9445-4AA0-344A-AE5F-8F740D0744E2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/B7BDBD9C-C558-244E-B211-5F7A3BC1BE02.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/C40110A2-41D5-454A-9975-9CF5B9223EC3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/C91E8292-42F2-F548-B688-D760A129762D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/D327536C-A014-4740-B08C-2F9ADA5995F2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/D665163B-E728-0A40-ACC3-8753D93D9972.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/D679123F-527D-594D-B504-53AAF5523330.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/E66EB229-E0BA-EC43-A117-70F1552C2945.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/EB7854E1-D64B-EE41-B226-CDFCC7647A3C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/F4DBB4AC-00CC-C749-B172-2262127FFFCD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/F9501D4F-6EE2-2C42-94ED-DB463A875B27.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/120000/FBA30309-9479-564D-A8B7-9FFDB23C548F.root',
] )
