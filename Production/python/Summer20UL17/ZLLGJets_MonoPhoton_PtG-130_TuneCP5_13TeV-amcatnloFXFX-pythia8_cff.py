import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/110000/8CCD53F4-3BE4-DC47-9BB2-E94BD638A286.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/110000/D0E3BBBC-A2AC-6445-AC6C-F27D21BC2161.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/130000/993CB379-3462-AB4B-B8C4-D8105B3BC257.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/1413F2CD-CA7B-9649-AEB5-AD80215C2AA1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2430000/0F8C5144-F618-8643-993B-BAE1CDFCA1CF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1A72335C-B8C8-9740-B8D6-C220B8D6CDDB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2F794594-3E7B-9441-8146-299A1B720310.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3C3F294A-A5D5-974E-A6E6-144EDEE71CD8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3CEF15EE-2311-4049-92B9-7B5F41440E95.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/43BC77A4-15BC-2A42-82A0-1B2EB62B5607.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/503D581E-9411-2544-A13D-13B545D36298.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5F485549-4C30-DD45-B34E-76917954E042.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6B9D5B95-4A55-E746-BF95-E34F84BBD8F7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/772CB37C-8484-3A46-B27A-8F5C3EF5FB6E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8119E43C-AF4C-3844-BD19-2FFBC9DA9ED3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8FAF0EF7-43E0-E147-B114-AF96D4433C41.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9AD0968A-DA6C-1A49-BD35-76566677DC41.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A3CECF61-A9DC-5649-ACA3-ED6561405CDC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BD8B8166-2E67-AF4F-AE16-3415A234700C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D1D4BD86-9AF1-2645-A11A-C2BBD34DABC1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D273C2D7-DC2C-EE48-8C8A-A76F305FCD90.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D8B4ECBC-7712-C84F-B29B-7ACFCF339BAC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EDCCB3CD-8001-4443-B7D6-50716A32852F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F671A237-BE01-764B-8AEE-FC7C247D157E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/FA9E6768-6AF7-3E48-99B2-CD21C6B9AA16.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/5F3CBEB2-F2FA-5D44-9C95-C3C8B0E61A3E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/B3B70CC0-3754-4848-B029-960DA8F297D9.root',
] )
