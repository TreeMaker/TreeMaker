import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/2C415595-AF75-C342-8204-8C030FEF89A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/2EB6AE25-1C41-4B44-B7A3-78F19004CF0B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/5A7E2F36-DE7A-5941-A614-0BF243B73884.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/AFFEEBA8-5E2D-6849-ADD7-F6862B99154E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/F0E85A0F-AD97-AC40-B554-3EC2443BC3C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/266EE7A3-FE4B-E345-BF90-4845BD84D0F7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/334A6A87-E491-7C49-BB1E-32363190C78E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E8928740-AED7-E746-A8A6-3E60CB029C2E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E8EC9486-3B8A-FA48-B719-21817025E9C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/15044B27-1A23-3540-96E3-1B2E0C6AE35B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/15B7DA50-116F-1B46-BEB3-1C0E4D0F3C95.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C38D71DF-FF1D-744C-A2E7-B2F40D5A6643.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0C8A4851-1E81-F646-9BA0-1BEA02027ADD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0E23941D-C3E7-6D42-AEE0-FC6D23C53736.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6A17352B-E833-1A4C-8234-1BCA393C9FB1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/00F37BD9-3D84-4B49-943C-3068458D24A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/2F1A7FBB-2FCF-EB4C-A91E-03A6D8DBF27A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3473DE37-9CC0-C940-8CF8-878519B483E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/427A9FC8-DC68-6B49-B700-DDE1862F8394.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8079C058-1866-9748-8E6A-6E9CCEAA230D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZNuNuGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/BE46D3C5-A9D9-1D41-B95C-0A83EFB1AA3A.root',
] )
