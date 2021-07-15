import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/004F95D0-AF75-7141-B834-98998E8040B6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/028BE47F-5C23-784D-8C4A-E4E602C72BC1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/07F3464D-C235-0242-A426-37AB97EC943E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/19168B49-5689-9046-A2FA-81246AFBDF12.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/231C5403-7B73-6343-A08A-2C671CA3A52B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/3B077297-2D2E-7E4D-BEC9-CC025CADA4E9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/3B21DFA9-7289-4B46-96D5-361478A9284A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/3B2B800A-6EBC-C941-BB3F-AD0E06A25643.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/3F9C63F3-12DD-B946-B698-4D2376B47EFA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6C694407-650A-A04D-BD5F-DD11D5411D0C.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6CE57395-6988-1642-9AD0-A9B6079ACED6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6DFE9D76-CEAF-994D-A4DC-4D159745D509.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6EB87B60-97D0-2B4F-B455-D6A55C6D34FA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/84406749-8BD4-0B4C-A3CD-DE7256C556A5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/8BE58EB7-8CC1-6341-8F6D-508A106D87B4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/8E4F4B1D-3DCB-0845-9C74-1C12D5051E6D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/9D580BCD-BB6A-FB41-B0EF-52ACAD8F9F47.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/A2DDCA2C-4108-DE4D-803E-EBD044A3CA3E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/B81763DA-7839-E043-9E3F-A034466A0EFD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/B92D494B-76DB-2949-94B6-63AA81F28F22.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/BEC6B68A-DA41-7D46-9FD4-1700476819E3.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/C50BB04F-B800-B340-BD1E-CF7368FCA108.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/C7D48229-2173-B846-9638-9CF8B80064DE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/C9100CD0-0BE8-5341-A85E-8A3719663F2E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/CA57ECD2-8BE7-234E-9247-8CA22A59D9AC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/CD25794E-D55E-B84D-AA21-805EA3562C5F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/DEBE3739-AB1F-9344-931B-4805056D6FB9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/E9F51051-CDA1-D041-B04C-C4C851FA6B52.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/F2DBA251-22E0-4F41-9AD3-2C519BB0F26E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/F661EA7E-FEE4-1049-B478-1F7184CF5341.root',
] )
