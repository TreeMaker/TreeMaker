import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0BD23F64-874C-714D-B08E-A2756CBC05AB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/2468E085-151E-1542-8F97-DA81E49C1D51.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/256724C0-DA14-BA4C-A1E1-B59CB4A4BA96.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/27E4E1BE-7A36-D14D-B83B-0E1328C84FE8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/31909FFC-A919-9D4F-B22D-F91E81728703.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/3715D057-A5E1-9E4D-8F54-2F018B3ED155.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/49CBA0EC-21ED-A048-8DF9-499846B2555B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/593AC5B3-D611-774A-99ED-10CC8EA8C254.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/5C3C2CCC-B3D9-0540-84A9-D8EB2A85E0D7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/5F9EB007-212F-5D48-943E-099A59013AAB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/749C8956-6BA7-704A-B959-59C388A6C908.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/82C74011-B7B8-8D4D-926C-8BA616FA5026.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/843D37CE-21ED-1244-96C9-345D9BCBBDB5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/8B8560BF-7605-C640-9E1E-13552C52B824.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/9225C3BA-4A8E-554E-9DFD-375D6FFF974B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/A7DCCBF2-1BCC-DE4E-B841-49637C19D535.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/AFF43D1C-83D7-8145-A53D-7262958BE8D4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/BA73A69B-0CD2-C84A-854B-81CE2C6729B9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/C054907B-2CB2-4D45-B510-95CE71ACF286.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/C7260110-427C-AA4F-8D2F-FEB20ACA7B01.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/C8FAC160-FA4A-504E-83A2-B32322AF7322.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/D1B737B4-06B7-DF42-B709-E0E8B4FFB4ED.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/E45F8F95-AD35-3641-9411-08B2C5B4789F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/E9B27031-1238-AD4C-AB0F-9CEA54ECBE88.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/EA83A91B-A43E-2E48-B654-6499964441FF.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/F32760C3-B0E2-2A49-AFBC-74706B963EBE.root',
] )
