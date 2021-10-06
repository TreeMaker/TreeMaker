import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/072B60C7-10C2-DE46-B3EA-122EA1E253F9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/07DA85A6-6D7B-5042-B453-52BB9E7EC427.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/13AA5E68-0799-2D4D-B4E4-D2EADE27D6D0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/5391DF72-462F-D14C-80A8-D1CF4B7225E3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/6C859BD7-9660-424F-A13E-880991A328B3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/7744D5CC-EF20-B140-9D70-7ECCF8DA597F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/7AB91F11-0C45-EF44-85DE-C134DC10930E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/7E86D4E6-1C4C-B74C-BEC7-0112784D44A6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/89230AEB-B8B2-E045-9F33-C367359C72D4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/9FA32705-AAB4-2B49-B8BB-BFAB4220495F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/B4FCDFFB-5DC1-4D45-A918-CA6D3D12A89F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/B57A4769-DE14-C14C-887F-E984DA9F2E12.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/EE4F1607-0842-0341-81EA-B0F754856A48.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/FC48AA4E-D002-9747-9327-2E28116334FF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/064BFE0E-F12B-474F-910B-16BE5448D0DE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/21870488-4E54-0E43-A298-2B80384F441A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/2457D714-AC88-9549-A468-16C063FFAB7D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/2E309AB3-BA4B-4641-B63D-2045BE61E7A5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/3B7D69FD-D2E1-CD4F-A899-D808883E30D4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/3E6DC086-2297-4D48-B1BC-E8D3C8A8992B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/765C8404-D55C-EC47-A897-546DE0CB9210.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/ACC813A8-6025-1940-80F8-16841431BF94.root',
] )
