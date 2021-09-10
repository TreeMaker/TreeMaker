import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/69E36308-012A-9044-985D-C552CD7287A3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/A2CE5081-B452-684B-878B-BEF16B0B4FFF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/B8FED6F8-C3A8-7346-9148-2B2353118550.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/DDBFD090-2BF6-EB4D-BAD6-B7B34A9C0D7B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/E473AC67-DF7E-EF40-8966-E3B027F0FA1E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/EE560AA1-94A5-F846-BB3A-EB246143C985.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/11F5A3FF-3334-EA4D-9455-0F5C9DF33D2A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/6A4BD5BC-3CC1-F54D-9C75-725115D26204.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/7F3BBF42-7D36-DC40-8042-C56E4502FDCA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/AE7BDA6A-7A69-8C41-8F12-374928B0C064.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/5EC5A93E-D363-834C-B5BF-334FE37069FC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/63E23D26-5E42-AF4D-A6FD-B95EA65B6A1C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/CF7B1E71-6B9D-F442-A45E-69253BB06E0B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/0AA365FF-8F40-B148-B6B5-616FFE097DAF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/19C3DA63-E1BF-3C4B-BF09-01A680D474DA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/341EA177-3EE3-954E-9D36-5F13B71AD46A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/BDB0EA2B-6EBA-D045-A48F-B389AC3648FA.root',
] )
