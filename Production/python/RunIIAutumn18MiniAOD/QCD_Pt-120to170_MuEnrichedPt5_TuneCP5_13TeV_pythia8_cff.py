import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/2D3B74D9-24D0-8644-B5DC-76CF922C758F.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/2D8578FF-8530-8440-BDF6-6197E27FDE46.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/311932BD-57BE-1240-B2B6-27B892E861AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/553704CE-DF48-1E46-BE05-D5E6183B498A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/59D6D5D1-775C-1540-86EE-97572BEBC3D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/5D9DD102-FB70-EA46-8AFA-397D18061CC5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/63EC5E72-CB89-CD45-ABB5-89B44B417AB2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/67C66C0D-1F36-214E-A506-3F8F5CBB68F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/816E5B09-27C4-3E42-BAFD-6EF18D971BE5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/84B33FD0-76D8-AE41-B8A4-C2EAD39F4A0A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/B5E12354-A96F-3D4A-BC3B-33E10E8084AB.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/DAD78D55-E6D3-094C-BF45-D69FA5EB8AD5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/EA25C889-2C55-4045-A824-BA1F6CC8CB70.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/F6066182-DF98-DA40-99DA-1630558CEE3B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/739A5DE6-44CB-1249-827E-580371920F1B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/8D585067-25C6-2144-9D44-D2FDCA3B54E0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/ADBDFECC-8894-7243-B90B-EBC15E28A8F1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/C9CEF366-7A03-CA40-B23C-EDE0BCFDE173.root',
] )
