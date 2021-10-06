import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/02EAFEA6-D04E-624E-AB81-44AB29D08A4F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/03110399-29C4-724A-A497-F4CB071F4F85.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0F43C323-CFF5-214A-B59A-1A0064C531EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1670C21B-B0DB-9841-9541-2CC72F064F50.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1FAB80E4-91A6-3549-AC5F-5D0C3196EDA9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2D2157C5-C9ED-DF4B-AFCB-44D580EF9A0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2F7D54FE-1105-7741-84E8-585A9CB46816.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/302F8B90-2414-1D44-A2DE-C11AAC76FB52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/31C92A4A-914B-AD47-9B68-D9ACEA7C22D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3316EAA5-FE43-754C-94CB-C88B6A47FE9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/34D0331B-C2F3-E04C-9307-881E0B81119A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5693ACDF-4C6F-DC41-9986-6F64601D2FC9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/649F8617-17D6-BB4A-84AF-6D273C74B309.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6FEA32CB-D3F6-2349-A3A6-3DBA45B3B8FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/85027D5D-107A-644D-8442-617AD16BE9BE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/86A30CA3-345B-2749-B6AB-3A71C17E44C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8EEDC588-075E-5947-BFB5-3ADBB57E32AA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/94575E14-0A3D-5C48-B40F-AD5932AB076D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A11ADA85-F28A-7A4B-B872-EDA735229428.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A1F3A0E7-0D06-4949-9417-3DFA4532AEED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A2FA2075-4151-4743-89B5-3D5DBAF9363B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A615BC45-EA47-A94F-9C77-E0F1DE96B07B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A66EB4F5-1D6E-0A4A-8042-E4BE58B87F95.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A97C0D1D-D68C-CF4A-B437-F372DFDF81EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B524E056-A3B6-CE4B-8A47-6ADE7366141A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B719A10B-AA59-C246-BA35-B2E8D5653C6B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C09DF296-6D00-904F-86B7-E0D0C90EDA5D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C280B99D-4ED8-7945-AF34-DBBC39F4239B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D9A3AFCF-C13E-DC45-AA40-D7E4BE1BB20C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E8D3A318-5A8F-E64B-9E57-7F244AD76B86.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E98E056C-B581-7F4C-AB17-FF912D7F2B0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EDDDEF64-D80A-324C-BD0E-B43BA46D237D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F14431E8-AA2B-BC47-8020-0EBD8B477DF7.root',
] )
