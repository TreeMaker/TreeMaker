import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/0C85A66A-5852-964E-A40C-14503366A7E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/2A6EB489-A30E-4942-945D-BEB02171F3FA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/2AB57783-42F5-0448-BFD6-214FA1284850.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/2E7AF2E9-37A2-C645-BEAD-494BD08773B9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/3CC32E7C-B4A0-694D-A8BB-34B2BCD20E0B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/48B62533-69D7-004D-B256-EE0FAA77A20C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/4A7B30A1-5454-5C40-969B-C8084021F100.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/5AAF1EAF-CCD6-BF40-B728-7EAE32ADAC5B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/64D01E66-1DBE-F543-AA9A-51C3DA994A4E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/689F05A1-0D57-534B-868B-A6FA206B59A7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/6A1D851D-A7C6-584B-9467-442F36CD3B6E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/6E37C0C9-2CA3-9640-8ED5-4E0E5C35D884.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/7A98B5F5-FDC8-384D-B8C1-EC780B0D9261.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/94CCCFE3-E49C-474E-997C-B25F916A925A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/A39D4D67-91BB-3745-AFA9-CC90FA2B3491.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/C0C166F6-0A42-3C4E-92D1-132E561144E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/D911051A-C327-234D-9BE2-28608429D0A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/DDABF104-B055-C44B-8629-4B0D5C47F15B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/E72F6530-8F87-BC4F-84EF-D38B90DF3448.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/E74A11E4-44D8-534F-9360-E2EDEB0467FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/EB233D34-88E3-0D41-8861-C31106D5EC19.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/F87610DE-0208-5D45-8BFD-87B52ED8820F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/10000/FF80DF28-1F2F-DC48-A07B-BB62C7375B40.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/90000/61C1ED37-CD44-FA40-BA0C-47419B3AA7CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/90000/69A03D70-3E4D-404F-8E10-4DAD7D82FB02.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/90000/C8708BF4-130B-1343-9DFF-3F65E4ACC035.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/90000/DED3628A-7F92-C645-A7F2-CEB795BB1263.root',
] )
