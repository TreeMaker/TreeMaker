import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/21821CBF-0D49-704D-82D0-D9937E18BDC2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/3AEC968C-9D73-C74F-896D-95E47AB39F61.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/5E0147BC-E27E-8C49-9200-09AAC7A067FC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/B24D93EA-C9BD-0B44-B9D4-159845EC8052.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/B42AEA2F-F7A8-EA47-82F0-11DBF3A745DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/C09149C7-FF03-EA4F-A104-68BEFCEBEF92.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/DE554293-3818-8B46-AB37-9D4F5EE8FAB0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/F355EF7D-6B1A-074F-9EA1-CF4C1F8820B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/F5C58E7C-C95D-3543-8D93-3E4FEEA31D80.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/F6A90F00-A32B-AE41-BBFE-88C539C0C5ED.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/F6B90E2D-B502-8044-B954-2745EA071FE2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/1110000/10543674-BD84-6D45-B24F-933B5C859FF3.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/1110000/220A1066-5B93-304A-91AE-4DD48D8A4649.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/1110000/27BF0757-CB46-E54D-9BB7-F98F21606BA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/1110000/4829EB83-132C-EF45-BD05-EAC0D7734B06.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/1110000/AC8D13B4-CEED-E34C-A056-FCB456F0AE03.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/01CCE29A-EF58-2846-814A-DB648F33402A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/03353FE2-E790-974F-AE48-7DDDA99CF72A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/296D6324-4EFB-3D4E-82A8-E46846F3A0D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/619EE5CB-B73B-D149-BFCB-00E8A74E6FDE.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/67821476-7E5C-124D-BDB0-06B73102E8B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/689A857A-96F6-2D4C-BD7B-4FE862FAEA22.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/96B27C52-7784-AF40-B6D0-E3D352F49943.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/9A6B5338-E310-F946-A619-3C3FA8055005.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/B3BB8D39-3C18-3D44-85D7-4892EB24054F.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/B719769A-C38E-E244-9D17-A0132F859BC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/C0BA4BF8-DA64-3842-A528-09165E9A204D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/CBC66D4B-F98F-164D-924F-2707108F5074.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/F025460D-F4B7-CC48-A0FD-2EF31F5693C5.root',
] )
