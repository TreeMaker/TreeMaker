import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/71E2BB61-4067-904C-BC2E-8287575C2EEC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/82969B46-F48D-B24A-956D-0D31C3E9BF54.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/8623E750-09CC-8C49-9DD5-01384B08B594.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/B6C88B1E-7F38-6840-B0D6-E7A496BE2EC8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/D839BE7E-4A66-A348-B2B6-D46E857BD5F9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/2AF8FB37-9F75-E545-B001-2F8EE6D0F9DC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/548E5D99-AEAC-B74F-B9EF-EB159DCE497E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/9B60DC3C-AD7E-6048-BBCD-8F509DD476B8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/D0BCD9F5-4852-3B47-8799-A78A7C542FB6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/D400812B-9657-8043-9536-CE4BA36EF3EE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/D841E262-39C6-A945-B7EF-04996F62CA6A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/F43C97B6-3B33-8A48-A042-7C4F3A02F5E3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/54DAC9E6-E837-914D-AD48-74155A4439F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/62ACBEAD-5D8A-7A4D-ABB5-8A03CB20DA74.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4166B4BE-06A5-4047-97CC-190E4751E0B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/65AC93BD-393E-2840-A71C-B62FE9CC4E49.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C9A397AD-91E9-5F49-AE73-36259CD85D3F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/247C75BC-424D-A848-92CB-DA3F61D8B981.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3F3814FB-183F-424F-B355-B8EC97A5577B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FD6E80B8-CAC9-4B44-A7BC-D8A3C7AF46EF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/48C7B3EB-E93F-B34E-A9A2-71674CD3E904.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/5AF46A54-B8C4-F845-A257-6AE3C93F9978.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/904D48DB-132D-7A40-BC4C-0EBD88A1C94B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/D0C0FADE-FCF6-754C-BF96-E731CFFDF3B6.root',
] )
