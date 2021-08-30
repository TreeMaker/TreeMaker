import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/159E77AB-C27F-D34A-A53D-53532D73A81B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/19D0060F-5B73-424C-BFE5-6B6B2ACC1F0C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/1B84363D-8E71-3F4B-83BC-782D5C94006A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/23447D99-FBFD-544C-BA2A-43B953902F69.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/2D122C68-3314-9546-8D34-981282AACE96.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/2FB85F89-DDC5-3C43-A4BA-CED482505F41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/3233DBBF-A0F2-9644-8CCC-A01654A03A99.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/50F72047-33AA-694F-B121-F7BD7914B248.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/689BC3B1-1789-9C4C-AE09-C7A4037F2860.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/69AE91F7-61EB-864C-B2DA-10CCDE15C51D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/8E26A5F2-4330-DE44-B112-421FC950D7AF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/918C763F-DBCE-6C47-9A05-831F66DDE936.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/A363EC57-636B-2949-B120-C857A78CE6AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/B5EFC557-9DE5-744A-B868-01E02BB36C38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/B68FA13B-BDED-4A42-8E30-9102CB4B0A2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/CC711A36-5932-8849-8028-536A5E3A159A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/DC5AB8A5-E2AA-B542-B315-C9BC58F28CD0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/E6BF4006-DE7C-C541-A088-45610F70275E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/FE80F423-9805-0C4F-880E-B11C31D42FAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/00B29FC1-830B-6C4C-98EC-819B8845BBB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/02356A85-6D5F-F947-9A32-3B4DBA5BEDCE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/03B1EB99-D4EE-ED45-9716-F16D1517467B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/238A9BC8-6776-CB40-AAF3-E3F5F5269CBA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/23DC1AB8-9E5D-0049-A608-E88FB599B0A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/29C4DB34-DBC9-6C40-A1CB-3941C6645764.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/35D9845F-6ADA-DA43-91F7-3E414682B493.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/3B3D02F7-96FF-3849-9E65-141A088BD125.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/3EDDC761-2792-4840-B276-09A9E1CC63B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/41D40260-486D-E044-88E0-1C989F418106.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/4F389E80-1690-224B-B31A-FF818A37C78F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/6501B1EE-7194-0F46-A5E8-DD1074C898DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/692A9CF6-7309-BB4F-A013-C103618FBECF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/6A7A3409-FE42-6D41-A253-418194640498.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/6D5B0A73-137F-DF4E-AA2D-62DDB9D3DDD0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/7171888E-4489-4545-8A38-49A4076BD9CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/83598913-AB02-3A41-A292-E1A2C4ED890F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/88034B1D-4362-E048-A412-74070BE194EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/894AA6B0-D854-1040-8380-E44186C6FF5B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/940FFA61-EA56-3D4E-AE7C-005D77C285F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/A930CB9F-2304-5D42-8B80-6F7083F575F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C1B6E004-ABBC-724D-9D32-7F3FE8988F02.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C23C15D5-D314-864E-8CD6-9A9DF9A2CCFF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C3E05AA4-1C70-C543-B14B-8B4C819B1328.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C722E182-4212-EE49-989E-12ADE0000E19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/D02D6105-9CDF-6546-ACDB-0AF2A9528950.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/E537B8C4-615E-5849-A30A-B3ECE0C37231.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/F0910EC8-F3FD-4F4F-965D-947A0BF900C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/F371C1E1-6DE5-4243-9D72-6334216CC7E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/F75F3BA4-05F9-E647-99F4-F1C586B40C12.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/FA619EE9-32A6-AF43-8648-29FB41FFF356.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/FE332F35-7F26-D84F-8925-C8E5DBAE1EE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/07DA47A0-AB26-0B4B-B8D9-12D15F5CC744.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/1D1B0E4F-EC45-504D-B748-8178F581EC21.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/1DAE4DBE-2223-3141-A1F7-DBC45ADF39B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/1DDA93B6-DD02-2240-AEF5-A135FCE26746.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/22C1D719-4C14-314E-A973-62ECCC2FC156.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/2B738D82-0E7B-E04A-BF7C-DB1751242BFF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/2F3110C4-780E-A84C-967E-AF9BDA5F0A23.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/31EA1E75-8FCE-6740-8534-11F354AC4D2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/324A9342-F361-7A4E-A508-3E5BE6B60E8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/327F3E51-1103-C24A-923E-95709BC214C6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/3C43141D-AC27-864D-9E22-F3446D4F0AF4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/40E6E205-A4CF-9B4C-866D-E0DC3528D27E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/428B8018-A72B-0B4A-9322-9F91A6D1FB34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/44C28111-E324-0C4A-88F5-5740684E1D5B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/49C5EFA8-E955-8F49-907E-2BD8A2FE5D1E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/4D72F08F-4B55-BC49-AE9A-2ABC999A3C2A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/4E7A4F12-5A0C-5644-B44B-311F60B20A21.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/4ECE367F-DA76-484C-90E8-CA79AD6D94FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/52DC9A80-A0A9-C143-A238-F5CCFC8FB1A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/57ABB2E6-E50B-FC47-8B70-AE9B4CCF4C67.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/57AD762F-8887-FD48-B317-A50AE6654823.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/5BD44C72-8133-E149-A103-A598552864F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/5C5D79D5-AF54-D249-BD83-A18DA147CF05.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/5D4AD37D-BFF4-5247-A98A-C7D9A63E2412.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/60B5850A-76CF-6744-A03A-076FB99185EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/68F3E71F-6FB2-2E42-B507-169415FA3F82.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/6E28DAEC-484A-DF48-AA44-04F54C8FCF9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/716F48C3-2903-1B4C-B837-1E1B21B4574E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/76907641-008C-714A-A5D3-79AE1336B621.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/7A2573D7-7EA9-8E45-B8E0-8FE209D239AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/7D28E7DB-0F3A-4C44-A3DF-86F5EFE26254.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/7D78314D-2DB9-504D-9186-6DC8D46D6332.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/7FC083ED-472C-7E4E-86C7-CA88A04B443E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/84D21C62-407E-C74D-9479-31333E0D9E41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/87007BF3-BE61-F04C-9668-EE39434119EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/91F52A6B-E0EB-D642-96DE-31F36E67A443.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/96522C19-0C9B-534C-828E-6EC9CB0D5293.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/9D2C84E9-E32E-1D44-8F26-081D41B781C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/9FB1AEA1-A11D-D242-8893-143D83433EA6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/A437E887-07BB-E744-A67C-A55E4C078FD3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/AC006122-FA91-1244-8126-3D1C4756E57C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/AE213732-A388-4C4D-8F9E-45BB0D5650C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/B0B058B4-BF77-624D-B272-7CD401D54DEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/BB98C1E2-4E4F-974A-8EBC-0B103153457B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/C545EFCC-9816-4D4D-86B3-605824F85F53.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/C840619A-AE86-7449-A9C4-C7ED33CC621F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/D7ED6474-D904-A24C-A784-F99817883873.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/D8458FB3-D0D9-3E4A-9E34-693C02F585E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/D8C919B9-9C97-8244-AEFE-CCB9FDEA092F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/D9D7C312-D387-1B41-A91E-B11C01EB5C95.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/DAA9CE5D-CC11-C64F-9444-B26E8189034D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/E3775694-61C3-AC46-9A98-5FE2459FFD36.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/E7F8B6FE-A6F4-CC42-B996-1A78E00C0CD6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/EAB47A34-B6DC-8B49-9B07-537A546EE956.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/EB6B5AEB-D1F8-7348-8542-B7FFC75045E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/50000/F6D8B001-0C52-B247-9361-0860C5FD9AC8.root',
] )