import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8CD22847-FFFA-2141-B90B-F5EB3C19666D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B953A1B9-2CFD-5749-94BB-B4E1E0B2F0D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/03E3370B-541B-224F-BEC3-218663DC19F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/133343EB-FE49-E148-80D0-EC2622BBE69F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/163733B0-F19B-664F-A244-A4180BB7AFB6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/1B3D3692-997E-764D-A66F-BE95B66BEE80.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/3A124FA0-3147-F148-9F8D-70F63C449449.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4176ED0E-317A-3F4C-94AC-9C790FD29F73.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4DEC2299-6689-BD4F-BDD1-67C039DE139F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/683C3FD9-2016-AD4A-A261-9F8410DFCD98.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/7FAC17D4-5907-C54A-9B65-285F6A1BA3D8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/87348F64-B727-C842-93D6-8DC4BC06E8D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/9E8E362D-B90D-5240-AB76-3793337C0B35.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A2875A93-BCFB-3D47-BBB2-B339CBF2C2FC.root',
] )
