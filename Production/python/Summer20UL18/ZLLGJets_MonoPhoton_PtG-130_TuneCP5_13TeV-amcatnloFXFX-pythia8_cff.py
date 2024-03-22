import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/1E652066-82CB-7F4F-A03B-632D6AF5C0CA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/5201B994-8519-EB43-9738-5594142C0C3B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/775AB7AE-C85C-984E-AE7B-5579B1235A3E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/7C9A39B1-5C8C-604F-A746-7DC21D40D2E3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/837E877E-2CD1-5043-B294-500D28B69607.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/897D94A2-2FCE-8045-B777-B64AC4886EDE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/A1F03E82-9ED6-2E40-B341-9D2283DFD166.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/D7C2ADB5-F25C-EA49-9DBB-13648A48AD1A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/DA912D66-8465-9D43-B6F8-E410BBC7531C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/E6C2F86C-102B-774F-9D93-ECB5A5EEC807.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/EC0F341A-73EB-4B4B-AD74-EBBC0FFEA533.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/D35AC663-2408-AB4D-9DAE-56C5468ED749.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/24DEBBC3-DEB3-F747-836A-C1FBF7E5C5C8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/671EE44D-A836-DC48-AC3E-07A461B8850B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/A7BD7088-6986-7941-8708-B764D8F7FEDB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2430000/92E18E4F-BDCD-1E46-82C0-6B73B1B98B8A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/250000/B92330D7-080D-6C4E-9EC7-8AA539A8CA32.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/079509EE-4C8A-9447-B972-82AF35068CC6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/397D4ED0-D53F-8942-AB3E-0675B7370B3E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/678F961F-6358-974F-B9E1-4FF3F8ED3DA1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/748B62B9-0B2A-8640-8BE9-0F76229D6E8C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/91564511-1454-0E42-8C10-56671F4210B5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/AA925D4F-3785-1943-8F0E-F6113AC04324.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/FBD1B9AB-4115-D24A-BB54-E30541A1A657.root',
] )
