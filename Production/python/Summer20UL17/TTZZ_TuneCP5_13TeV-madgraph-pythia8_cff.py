import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/21A6F110-AAF4-594D-B628-479E09BAA527.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/290253F1-3990-8C41-927D-5443604A0A76.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/33E58E8E-21B4-D544-9BA7-83AA005F123B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/3C83C770-F63C-094B-BE0E-9BD8E15FCC0D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/44BD4F5E-2B11-0240-A541-F28968893643.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/5948DFCA-E887-3E47-A67B-62FFA99A8FCE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/5F91F1D6-AD04-F448-837E-AD7F36797406.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/65065334-FC2D-7749-92FA-B592536F70BC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/709DB308-3ADA-F448-8D4F-84048C079DA5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/72A82FB2-1900-7B4E-980E-2D99D3C5D39C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/7537911F-AEE8-AB46-8C5B-55485D6F031F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/9CED20F2-DDCA-3E42-933F-2CC88DF5182F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/A3E7B745-6B41-4344-A332-10E2165ECDB5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/A5AF59FB-76F7-B14B-9B5F-70A45C60A088.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/AD81312A-255C-0D44-AEB7-C25F22403D75.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/BB7F9AC4-E698-0A4C-8387-3157FAD1FB55.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/C5B6FD37-538A-AD42-896B-0ADA0C7B417B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/C7F06CB4-082C-EC47-A2F7-C6579A567FF8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/D4C5EE90-3D99-634E-9B83-29971F120479.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/D6986F35-EC6D-AB4F-BCC7-431286B281E3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/D9A7AA69-DDE9-8940-AAC9-A4D5719DE245.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/EB8BFF74-CD4A-F946-BE5F-84E55C4A6E48.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/140000/EF890D6F-21E6-3843-9417-8BB3B96A58BF.root',
] )
