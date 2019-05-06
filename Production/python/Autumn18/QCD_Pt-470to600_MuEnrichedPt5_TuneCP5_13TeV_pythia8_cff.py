import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/084A4B26-84FF-924D-8DDF-4A1832B957F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/4C51770D-35BD-A84A-95CB-42E856CB532B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/4EB13E8F-4F6E-0A4A-A4F6-20FFE3D3129E.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/6019CEF4-E556-8143-8B68-B383AD37B208.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/6CBB1CC8-1F72-AD4A-9E91-4DC2379B3957.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/6F4EA211-64C6-844A-9383-C2B652B0C66C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A43A5C89-9679-5D4D-ACDA-187992E293E9.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A885DA10-C128-A347-BF43-7B0D6E24B84C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/BD6700B2-EDE2-484A-80F5-2BDC98B2038D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/F8D863B3-7FFF-EB43-A4D3-36239DBF68D7.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/27E28A5F-D6BF-7046-A34B-5650E7D9A075.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/37DE11D4-5995-0941-A26F-52511CD42951.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/5E4D2179-5DE1-EA4C-ADD0-5F6C06433514.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/94EBB999-A697-3741-B763-91157C3F1747.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/A6AE9519-0256-7F4B-8969-01C9E03B1502.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/BE745FB3-C2FA-8A47-A9C4-C9115A0511C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/CA3FEE51-8CEC-1C45-8DC2-399FF0068977.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/FAEAA216-08F9-BC4E-8060-7B5819F497AB.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/FDB60DD8-7536-534F-B8A3-459B845A596C.root',
] )
