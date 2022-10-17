import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/0B1A95C2-9D22-F340-8403-F84BC61C240E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/0C40CF2E-E120-C443-908D-B63D200037A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/0E18052B-6322-F543-8A15-79348CAFB84C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/115D9DE4-C7FB-3245-A57A-6089D6504108.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/13CD0211-D155-594A-90CB-3D9D15F3A426.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/2EDEDCDB-5918-904E-9BE9-177F21AC57AB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/382A8EAC-574A-1547-B154-D5FD37819B50.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/5845B0B9-C8C9-4C4F-986E-2F690845B254.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/59F56337-8958-EF49-8CFA-4354E18D54A1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/791E43EC-6BCF-2E48-A991-1A2159B535DA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/7A77DE22-FE7A-2B45-8CBC-2DC0DDBCB75A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/7B319181-B127-9E41-80E1-E27016A3A604.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/7C602E6B-6B3B-1A4F-937F-76969215A017.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/85401195-6716-1640-A022-C834B8C305B4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/860C7702-C1B8-9547-8876-DBF4A638BD11.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/91FEC4CA-4697-7748-8C8E-91B0BC6923EC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/94A61EC7-5E5E-9544-8CBA-0FDD5C3EADF0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/9733156B-2C75-5747-94AC-80B644AD87DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/AE36C4BA-0E28-7843-886C-9FB1B45EE3B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/BFA6C3D3-0BCA-4546-B5FB-F3592222AA7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/C048140C-313D-984F-A39D-A5FB77568916.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/C7D2B054-E39C-7745-ABAF-E604F145FF7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/D1A87D7A-3D26-4044-BF4B-8E2D32BF9043.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/D3B0B485-C545-DD4C-A59F-24EB70A6EE7F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/DC9FD774-B452-8E47-A185-793E3AC8AE2A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/E5EB3E96-FD9C-464F-B62B-CB23A86540C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/ED52A3CA-1241-F940-AA1E-50EDB94BB2BF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/ED7807AF-521A-6146-AF3B-9F64F1232F98.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/F8C3CB87-ED0C-1848-A57C-C98AC8563DCF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/FAE7723E-4992-7E44-A670-9A16BF1E7A13.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/FC1484A1-64F4-4240-928C-136CDEA9128B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/FC758A1A-64D3-5843-915F-2D4BCD0C3BE7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/26AF4B5D-AA1E-D940-B23B-6F225822ED85.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D6474380-2778-0847-9DDD-3D4418A6F742.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B72B50E6-E095-4143-8AD5-E72C7F7BC6B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/E6C1EDE9-5AEE-224B-BA6B-E15E8A573749.root',
] )
