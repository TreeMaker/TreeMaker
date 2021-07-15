import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/01927B20-C337-A641-A001-7C0A8EE95E6F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/11E073A6-6CDF-5742-9D41-B06753E31F8E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/131513BC-3253-EF4C-93A7-4F76C5899DA5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/18916A2C-B451-5642-B7A5-4BB121564455.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/282B0F88-C087-614B-B7F9-0CFC645E8476.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/29A8C249-64AB-114A-9268-DD25A6F7886F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/39F3316A-9577-4D48-AB77-E7ABC7499B8C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/432CF997-2B50-BD43-A539-D844470EF348.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/47A32FC8-FCC5-5544-8ECF-D22DF7C3BE30.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/5AE2F748-C50F-0B4D-8085-62AA08449860.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/5BFE00DB-DF23-A746-884F-9E43C7FD3D23.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/5F4B7AE0-72C5-5C47-AD2E-C9B638F5009F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/73D80610-3ECA-C343-8FF4-EA3896E699FE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/7DA05260-BB35-B143-B5B6-C70A0B5FD029.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/80589390-D1E1-0246-894E-5023B42BE20D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/913A440D-30C7-0C4A-8BD5-C6335C238A13.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/9DC14140-C044-A048-8F3D-D89B6D3F6BE4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/9FE62F65-477B-8B4A-BD5C-D96C4EC9BE64.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/AACCB57F-979A-644B-9684-9933AA2BB04E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/AC1BC99F-F84B-754E-82ED-FCE9E43DA51B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/B3AF688B-F253-FF4F-913E-AA297C28444E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/B473E723-CB82-9944-8FD6-6706A1DE7CD3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/D07E4CAE-9CA5-A749-82CB-AF2C6215929E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/D4195C4D-5868-AC45-9478-54C0DFEF8B1C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/E2230345-F7B6-6047-8074-FFDE5DB32051.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/EBF6765C-1335-F841-B6B1-4D26AC7B8B46.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/F16DCCB7-5EB3-6F40-9984-EB75613EC843.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/F3964EEE-3EA3-6B45-859F-7CA575E28041.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/F9641D1E-8F42-3E47-8E7F-70E19586774B.root',
] )
