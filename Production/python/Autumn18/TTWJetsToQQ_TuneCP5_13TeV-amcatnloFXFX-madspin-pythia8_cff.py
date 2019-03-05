import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/AD59AAF8-93B5-D245-92AD-369CB0683A9C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/088B2EE2-3E22-744D-906F-05A998B2B712.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/373516ED-7CF1-B841-8221-ACE056F75A8F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/7DD6A6FE-EFAD-864A-AB1E-D544D393A5C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/80A12C97-49BD-5E43-8D68-1402AD7B5817.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B1379666-7624-7146-BE7A-63AD2A4BF6D7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/D4B5347C-F94C-E94F-B2CD-CF97A5561BFF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/07BAC7F8-47D7-7A4B-A19C-3F87F4B54F8F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/08FD10B2-A3A1-B34E-B44F-34A3C5064479.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/140F6869-4FE7-B648-9223-AD0D213AE233.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/23737A69-2726-B74D-938D-1833561F9316.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/2502B976-2F70-2A44-948C-118F546B4CB1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/2D1269F2-54D9-2645-9FB3-6176CE1C749F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/331E0D85-B032-1F47-9E96-3F1EA66B6871.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/451F619A-2CD1-D247-B9D8-E4C3682D15BC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/4809A077-11D0-0148-9ED1-72B50FD61C2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/68616846-4332-374D-83F1-89B3DFB2BC44.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/755D161A-7563-6C4E-9237-5642FC81DAB0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/82F684FF-A3D1-204D-B49F-609347FE25E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/867B4058-DB94-A143-84B5-1C12C5A9CB63.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/968F0289-0E69-254C-80A4-D42517E6C882.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/9B527C14-F06B-9B4A-93CD-BDC20DE6E18F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/A231E6BB-5B19-B84B-B396-BF9221CC0C0C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/AD1C36E3-FE26-B843-B836-71660141DD2A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/B4373150-2460-7440-B0E2-8F6C67DE93F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/B801FDE7-3495-F340-94EF-3DEFE21D33E4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/C4A08053-3557-CF4A-A06B-E270F1D76A41.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/F035F68E-7ED7-3846-8A4B-C6666374CC48.root',
] )
