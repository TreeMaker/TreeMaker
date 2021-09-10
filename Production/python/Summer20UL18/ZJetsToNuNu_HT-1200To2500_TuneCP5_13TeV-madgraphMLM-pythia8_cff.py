import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/66B426C1-A017-F944-AB9F-648D0BD46B76.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/75268A18-ED71-A140-9C6E-BD8835CD347D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/CA31EBBB-34D3-7146-8C9E-824528CE9A04.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/E10806E6-425D-AE4F-95DA-BB52F116E307.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/ACCD5F23-4D80-2F4C-AE17-61DEF528A6EE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/004B0A45-5C52-084A-9CC9-57B41479627A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/9F3BC4EB-1B76-E441-92E1-0C9AF4AFC6F3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/C48370D2-123E-D746-86B6-C93AD57098C0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/D03290C4-11E9-9844-A148-1472B02D5896.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/E462830B-9A35-6F4E-BB48-F23A4059FB99.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/5C8B9650-B888-894F-B9B6-109806B32297.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/70C7887E-FB3C-4946-BF96-C413F848B73D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/D018FBD5-A6E0-574E-B4E2-655E336733F0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/EBBD87E9-F06E-E240-A110-D2180D9915D9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/0875F6AE-E79D-1847-913F-E2AC0FE19160.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/528A526A-6DBF-0840-BB58-CBFC92E66AB5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/9A1C4DF2-E25B-584B-9FF7-33ACF7897544.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/A67D036E-ED15-0141-97E6-1D15E33CBB12.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/E96D99BB-C25A-5041-BCDC-FE5D1A334E0C.root',
] )
