import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/27FF84BD-5363-0C49-B758-98036F739438.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/42B71B60-46FF-A640-8326-2F6D808E579D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/E4118FA9-8A78-9041-904E-58D14176EB5E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F2FB8845-8A36-9448-8667-79AE07F7B5C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/38BC1A27-9DB4-A144-B74C-64F1D0490E2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/40D0DF67-E828-244A-B7C4-36E2A2BA43C6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8050735A-270E-AA44-B3BD-524C5DC79C46.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/ED9AB831-9FA1-B843-BB0D-84541E8E7490.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FA123725-C1D6-C94B-A9E0-757895B61984.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6BD7C70A-3615-7B44-A4B9-3F54775F4255.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/90AE9AEF-47FF-824F-8874-99961F7E400C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0868E17D-CF10-544C-A0A4-06329236ED43.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B1851EB1-1387-4443-B59F-6758FAC64F08.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E3270A43-15FC-CB45-87D3-A418A62DE506.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/32013F7C-5BC7-2443-97A8-C15CF365922D.root',
] )
