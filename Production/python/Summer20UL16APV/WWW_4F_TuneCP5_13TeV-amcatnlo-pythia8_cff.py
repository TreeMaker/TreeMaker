import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/7EF3A78F-D0DC-A341-AA0F-27A4E9E271B6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/C5D73102-F822-1D48-9CF6-9E182B9E58C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/EB215F2A-D3C6-334B-A385-518FE6AB639C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5B8445A9-8696-174F-8C48-F538B6DEB6BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/8C530CCC-2B93-7A4E-92B0-F8C9E661201C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0564A663-7925-BD48-A5AA-E0D80EDE59E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/4C02C47C-C87C-644C-871D-D73C3BE9BDCB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0D283D63-C5FA-934A-A90C-E97914A8F4BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/863D59CE-79CA-5A43-9C81-8FA03C7142B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F3361E05-3484-584E-A07B-A0F8A5513792.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/159EF5D9-A977-3C4B-AB77-378BBDA5BDCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/168A16CC-8B0C-144E-A4CD-0BFEDE93F5B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/33E17A6F-FE15-624E-B043-251C94CC37A1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3AC06601-DDE5-B246-BBC2-AE9642944E99.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/BBF822F9-6846-6247-981B-30A2AE94B767.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E218BC25-65E0-834F-9218-1BF6123C92B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E2497D91-D9B6-8847-9038-AE7B339265C1.root',
] )
