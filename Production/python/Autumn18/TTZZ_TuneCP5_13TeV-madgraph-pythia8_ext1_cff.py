import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/19E4717E-F6D5-524E-B29E-55AF0D357728.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/2CF962B2-799C-B64E-A675-9162FBC72836.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/2E831D2D-47D0-0940-A78E-3F3096752957.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/40EE5A3A-AB03-B840-BD36-90F11CFA7842.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/622CAABB-321F-D744-AFF8-844B33B962BA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/68970187-BD7E-6342-B02A-630FD3DFBDD1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/7FFE3DB3-9439-744B-8F15-74CC1F31CD11.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/86D6AC3B-A83F-6043-8930-6782785C07B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/BA89B12B-CA5C-BC44-A9E7-958400D7C8CD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/DF3F074A-1969-F340-A726-D01C4C9EB040.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/D968F4A0-ECB4-0E4B-95D2-04272CB59524.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/198429A5-453C-A84A-9D05-D0EEABA6DAD0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/FDCAEAB3-A89A-E849-AF29-1AC241C1331E.root',
] )
