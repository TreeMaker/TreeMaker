import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/0EEFEE5B-ADBA-BD4D-B684-0D0204F1450F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/13254EAC-7BF9-FD48-A182-B093A50F91DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/1640DBED-3BA2-CB44-B100-628936D7003E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/22E50E07-1AB2-CE4D-B997-2304D9DF6ADC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/2EFF7489-9079-A842-898F-BB3D9C035275.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/464FF744-022D-1F44-96FC-59A8E56CAF4D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/4C0FBBA3-6463-824A-8A74-92544C5A00BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/611F8134-ABAD-7947-86A8-C0308A989ED8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/69C080E9-839D-7045-84FC-76D33CA58C02.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/6EF3E437-E82F-8A42-972C-583AD9CD8828.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/6F501978-2E85-454C-8C8C-ADF57DB3D960.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/7274A424-A99F-FE46-9494-895CA3DE6817.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/8C4BCE43-2059-F24A-995B-A775B1D1A3CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/9959D1AF-C8D6-DD44-A266-033F2F64C80F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/A42A008B-4E78-9847-8844-EB7DBC5B2089.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/C29678B6-7497-8548-A739-1C947CD702BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/C338FF38-815D-0541-97DF-621E4B6427E2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/C470E0F5-B613-0D46-9D39-C1484AEAB196.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/CBAB9950-F067-0146-A2D4-6C16F4781138.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/D744ABBD-067F-A74C-9511-F5D6614D3FAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/E44B013F-B21B-1F4D-8C14-501B9AF1B26C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/E44DF511-3D24-C147-96F3-8F6AB2FA78C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/E6C98435-E575-0E46-AA32-117EC5EC0823.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/F4FE876C-0926-2445-B622-FA9122E8FCD9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/F8504EBC-C2F9-2E42-8AB0-CC0762EB4661.root',
] )
