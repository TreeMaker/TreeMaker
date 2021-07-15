import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/01D374F2-9058-7046-9EC5-74B994763420.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/14FC32C9-CB92-4E4B-A2A1-44BB20EA3801.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/192F1F2D-8203-0E42-A61B-CD40BBC61A0D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/1D51181A-C46C-D64C-82F1-D49A8F88375D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/1FFC99DD-DF64-FD4D-8F6F-4C9165BD39BE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/2D4D5547-D1AE-FD40-B39B-7DACFE0A2775.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/2DDBCA36-C411-1944-B96E-A37AC6846FB3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/31994BDB-00FE-3747-9DBF-D4EB410B69DB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/32F669D2-6D59-494C-8C1F-019D74A49DC7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/425847B5-BC8C-E847-B525-A6D08B8EACC4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/42589B50-B73F-6844-8EC8-2A43FB4B00FF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/4B605C74-90E3-7D4B-98E4-0D01AD6301A7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/52F485D4-D7A1-E844-AE85-61D91E6CABB5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/5CA3DA49-EFFC-1740-B600-CFF89C165843.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/684A441A-A9DD-B440-9B22-0F1936FE00BF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/6BF7DA5E-B468-7940-8EC5-F74416374A70.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/7399623A-E488-D54D-9B08-D23AEE07581C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/79DE465B-0A93-164B-9521-590E071F3086.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/801A1917-EA25-E94F-9080-F5E212E49F28.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/86B18E70-9B35-D24F-A110-2A2E3CDC4DF5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/8B19D958-A71F-5B4B-94E5-4CA7C0D77186.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/9B9FAAB3-4807-CC4B-8983-8E4236C0A18F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/9E8A3D7A-2FDA-604B-B22E-B2211C9615E0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/CD6F9834-4EEE-1845-BC41-E62DC8D70583.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/CE056DE8-C0C2-D049-A3A4-5270685EFD8D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/D3AADAAA-F838-5741-865F-BA09CA0C2C85.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/D9BEA942-FEF8-BC48-AC96-BCF11FC1B25C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/E74DD8CD-ECA9-4543-ABDE-A24CD11570D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/E7D3B3A1-62FA-6B4C-A175-2BE831172E5F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/EE482E3F-51A4-FA49-8338-0AF35FBE381C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/FE75F4B3-7866-E54C-ABE0-C162387FFD01.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/130000/FF18F15E-00B1-554A-99FC-70D132AB357E.root',
] )
