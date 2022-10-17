import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/120000/5240C2D9-B248-764A-AA78-CEA10D2E77E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/120000/9FDFB801-791E-254D-9311-441DB6EDA569.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/130000/723F94A7-90F4-7548-A122-C38ABCD1BD31.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/130000/7AD28F6B-ABE8-2E4B-A720-ECB77237F976.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/130000/7DA4FB50-42CF-2D4F-94B6-8FB88C306F25.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/130000/9B91924F-9DB7-A94C-8863-0C8768A8EC02.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/130000/E65ABE1C-A1C0-1E41-99B3-2E49CCBED1EC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/1BD839F7-2FA5-B44C-A1F2-AC7E9571D114.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/72FABF5A-22E9-9E40-A7AD-C4F4E0157DFC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/9E4CC96F-F533-6C42-B8DF-A5BF403E9BDE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/F600E248-D698-6C40-A29F-D540DF844671.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/5F09FB20-B77A-6E4A-9C26-DF3C2F736F96.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2500000/11E3470B-6098-0543-9E40-783C62FCD676.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2500000/DDC03A89-E6BF-6047-94D2-5AFCA1F5249C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2500000/F3329AA4-A671-434A-810C-E8A4BC211D31.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/D47E2084-1566-D144-BB5E-1CAC8FCCB069.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/467DE3F4-2624-A34D-BEF6-3999C2671B0A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/04D6F03B-ECC9-C84A-B6D0-93DCED3C3DAD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/0D74CDD6-9928-F748-97A3-C454F706A388.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/1145338E-B977-274B-94D0-4D6770152DAB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/203643AE-1A5C-3841-9B14-68526D0210F4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/219ECF42-48A7-5D41-84D7-E9479DC032A5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/24BCC8EB-9C13-574E-9255-BF1372B4F470.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/25A25E02-F7AF-AE4A-A820-158DF2341260.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/29FA2D71-D8C9-2D48-9EF3-5B3D55C1D0EF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/35AF497E-CB08-564C-AF7B-C0923CE9D9D8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/3A0B8422-AEF7-EF40-A35A-D471962B2C15.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/475AFB52-422A-B844-8BD5-F32159F684D6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/4F25343F-9B7C-8642-8D9C-04911C534BB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/5163A339-0B0D-7C47-999D-963FEBCD51BF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/53023E77-AD2C-834F-992F-486DE93C04F7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/595DDAF1-558D-D84D-AB22-A32899429D54.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/702BB90C-671F-EE45-A836-B93DF261F291.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/705658AF-C6A2-7F40-B99F-05C5A039DD3E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/70580E70-C531-C74C-BBF8-42805660CEA1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/8B248F83-7B6D-DE42-9020-4AD98B573136.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/91EF4956-3C0D-484B-A27A-0C23DF8B5FE3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9571D451-4DDD-8241-B7D1-160270913CE7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9DD9058F-37B9-C146-B9FD-4D25F56BFEAF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/AE519934-7ABE-034C-BFC9-B08803309CCB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/CCDBC4E1-A8B5-F44A-AB44-239682E10CB8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/D249425E-CC9B-F540-8FC6-5A6F2516825D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/DD0B1C78-E71C-8347-9B1B-EF847BD9216C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/ECB39CEA-78C9-DA4C-91FE-8296CE7BCE7D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/F0DF509D-C08B-C74F-9E8F-1648E70EE205.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/F1D78B07-B58F-8F4E-9DC3-69CC61F659AA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/FC932B95-1934-E845-9859-AB170216586E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/22009267-2A3F-EB4B-867E-FE3584647F3E.root',
] )
