import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/998A9CBA-7377-CE47-A9E6-476C8677311B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/7BD03EED-656C-9047-A9F2-A1720CEB6FEF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/DDA2B4F6-1BAC-2A40-87EB-DD67AA782FC8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/23EDB1CD-EC24-CE42-88C8-E453FE5A3835.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/337357AD-412D-7E45-AF87-AAB761503079.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3F4C6289-2BB6-0C4D-BC8C-A12BD23DBB70.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/951928E0-C4E8-184F-93E9-B60A40607C09.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9D7E192D-4076-2E46-BF47-29C367D6754C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F1495320-1C46-B84E-A3A3-C5BD28933510.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3195173B-E245-2D4F-9755-E20E4B675F37.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/731B125E-DCB2-7945-BCD5-03110F6FD875.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B8B736F8-925D-6342-A990-B7CB73528639.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/C65FC8B8-6B3E-C747-BF63-600364A1DF6D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E741D86A-C79A-004D-8851-DB9D78E3958D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FC2D7ABC-3F03-324D-95D8-1B14DF8068D2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/30782EC6-A6A8-FB47-B7BB-646A9152F000.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/A03AD488-3ED9-7A49-A1CD-4A888C40AC6C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/AB4E36F8-15B9-CB4C-924B-4190BC018156.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/B61E5BD2-23FB-2247-95EA-3CA62840F0D9.root',
] )
