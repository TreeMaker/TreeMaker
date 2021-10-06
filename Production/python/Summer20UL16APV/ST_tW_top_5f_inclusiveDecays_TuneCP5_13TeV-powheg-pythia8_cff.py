import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/43CCEA50-B5B7-3943-BE1A-073C1F968C89.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/01C1AB0A-5032-C545-B5D0-0AB14473D3C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1765ECF2-2AC6-4C47-8032-B7C7CC6454E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1E9006D1-507D-894F-8EEE-C1B42EC2D520.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/24937984-3D2E-B94B-BCCE-7FA78F1E5D17.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2AAA5E40-FAE2-164F-AC3F-24D64B8B5945.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2CF38E71-D30A-FB41-B29D-CEBF88EF0456.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/4883BD4A-B46C-664F-AE54-0A51719B50DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/506CC897-4764-2343-BBAA-7A2573E49B99.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5EB118D2-8E06-8142-9DD9-B6FC52729BE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6919235B-1435-F445-890C-E2DE5CE85038.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6F1A1FB8-E5AD-684B-9073-8DA1230C1ED3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7547480C-DAD1-DB44-B606-906C9A87BC64.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9F7BD2A0-AF0A-D047-B0C6-15EA9C031F34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A290696D-DCB1-F740-B578-82BEF88A07A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B876510E-B95B-6D41-B345-08E29F52448A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C95A2C5F-5CC3-5346-80C5-BE27AAD5AACA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D1529566-8D0F-F34D-91A8-86E8E2583474.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D6692BE0-A1A7-C94E-B058-245AF63B96D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E2D8C58A-5E17-C242-95F4-C87A9FE04758.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F3D88AEA-F571-774B-B8B6-BD1A90C5A114.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0396A7AD-A28A-BF47-B4D2-8E08A0B9A214.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/17CF2373-7AA2-674F-A4E4-0AB539AB5C87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/18437229-7E5F-224D-A9E2-735BD9E128E5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/19BCCCD4-8FDD-1C41-8266-EA32FD69BBDF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2A15D569-7BA4-8D47-9D8D-95940F64B0F9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/7DA9F5F7-BEDD-584D-8388-B5CFC96EBF31.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/87B1F381-85F4-B148-B10D-F0DAEEB452E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/961AF495-05C5-8049-9AA1-E263C92F63A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A04ADD3C-AA47-204D-A3D6-9AC25397FBF4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DF9B670B-508C-AB4C-9587-F4DBE637FDF7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DFE7C9F4-D08D-7F42-BA4A-5780FC8AE3AF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E9E505F2-300F-7E4F-BBD9-34B738F43741.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/FE72E53E-74C4-8449-88BA-60DB4F813C85.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5F39A928-59E4-5F46-A0BE-060BD362C154.root',
] )
