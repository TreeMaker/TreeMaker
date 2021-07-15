import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/0AE7B55C-71C1-4F40-B292-A4F045A52FAF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/0E2601FD-A46E-0A41-99DA-202BA19C814A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/10BED48E-F37C-354D-8B5F-C64188822E18.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/18C131DC-F567-564A-978B-280E7F221771.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/21628270-090C-1B49-863C-15711410F9D7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/341BC5E0-19DD-064A-8FF1-D3AC6F82132C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/3B8A9D49-2B34-0343-B2B8-3540BE0D27C9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/41269734-DA62-C04D-ACF7-84629F216708.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/5F7FF0FF-6555-514F-BAD1-079C5E215F1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/65E435CE-3E5C-1E40-9B16-81CB86C76977.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/6C420819-6102-DB4F-933A-271D61169C9A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/70D5E264-DAEC-1D4E-99F4-338993999C87.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/7D7144FB-1781-A04A-AE20-A31207C610C2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/95ACEEC9-79E1-414D-B2AC-BB6497B4351C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/96FCC4F8-1D45-FA45-99B8-FCF072206EC7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/97A9F36D-36F4-BE4B-800D-38B021266479.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/9FF0E4DD-42DB-6342-A7AC-3C734F8767C0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/AAC15B25-6C17-8248-AB8B-95FACDBD6BA7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/C353188D-C070-7045-90AD-9BD839E117D4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/C5238FD2-2C75-D64F-8188-2A64E10E032D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/CF0AB80B-E6CD-1543-B0C5-6E8248A7FA4D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/E27383D6-3409-D74D-803B-4B494A5783D8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/230000/E974D700-DCD8-DB44-8AB6-A61A3CB86540.root',
] )
