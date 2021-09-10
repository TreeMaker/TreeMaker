import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/9C05CDD3-46A0-474D-A214-FE977FF3F26F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/D7962292-4EA6-D747-BA3B-F14A6F4BE45E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/E3BC570F-B697-CF4F-8946-2A3E6DA19FED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/1FBB2556-4029-5240-92F4-38979A8F72E8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/2147DE08-D727-AF47-8FC9-18A57A64DD25.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/308CF3CC-850D-E048-BE7A-A32277AB0F99.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/34CBFFC1-3D31-6A4D-B032-FD49C5BC86E5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/54AC7C3E-82D9-714F-ABF3-DA768DCA3849.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/61290F18-9DE1-CC49-BAAF-EEA22BF50264.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/7BD30EB1-7253-ED43-AB4B-4AF7A8072C6D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/7C02A8AD-60E4-F648-A291-165EE43B07F4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/87864FE4-782C-A349-9FC8-9EE29F0E6FFB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/A3A0614B-6283-5E43-BDDE-BBA9BCF19140.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/BFBECEE9-F063-6F40-939E-FDF810266AEE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/DA0F0AA5-32FA-2D42-B267-356F4F01DA96.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/E6D7060F-50C2-2E4F-8726-2311FD5F989C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/5B948F79-8354-3345-8074-680EA307AAAC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/C76DE30C-1E5D-124B-9DEA-3311ACD85F5C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/C91244D9-B62D-BB45-AD5E-F2B5FE49575A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/03C6BBDF-0F61-844C-B52F-B97E0CE8751B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/09D515A8-3261-A646-AD39-CE12DD6847F8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/18E59647-B2DA-8D43-8DCC-F365BCBC6A25.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/1C91CBD5-90F5-4F4E-8B09-4534BBFD192E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/2BCA568F-A9EB-4547-9AE5-153B439B5E16.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/3F5DD0C0-7CC0-854D-9778-CE6614251FE3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/5D6F7C94-42B1-7349-B81B-C975E7C81448.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/675DB5DC-C2DB-F549-9F2E-3706C8852182.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/BCAAEA93-FD52-8D4B-A2F9-4D2A72588158.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/BEE00208-072B-A64F-9948-F333235C238C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/EFF6CA94-9D4A-EE40-B026-51024A50DEFC.root',
] )
