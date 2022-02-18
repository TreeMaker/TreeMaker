import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/2065F164-F348-154B-9AB4-F86E0DB1AD40.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/3B0CB115-2C4E-564F-9B43-AE59D736C058.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/8CFE6668-DDA6-EE44-ABF1-89B0B9B4D837.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/A7CE6FDF-0410-6544-8786-C93EE202533F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/D4E8F176-6F0D-8F4E-8A5D-718946AD8553.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5CE6DBDE-31FF-544F-A08D-C8B83E40857D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BDAEDB7A-EF37-C848-A7C6-CE38DDAC0CC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0CC33C6F-022A-B945-B4D1-5803DBEB73B6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/13120A97-681E-BF48-85F0-962EAC90EA45.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/137733F8-F6ED-1949-AF8F-B02FB8F53F28.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/14C90432-FE72-AF43-9DE0-E6EA4997C7F2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2B65324D-3E57-8240-BAE3-6B0155D04D32.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/37178703-BE12-644C-9751-8EE9099FD0A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3BFDC88D-0A2C-7048-A753-60744E058B0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/417230F6-88A3-414D-A47F-F7939AB9A047.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5D65665B-B1D4-1244-9F8D-E71CC6A96395.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7B9F7727-E44F-7949-AC03-9C4ECE9D373B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8D1E91D1-48DA-4842-BEF7-DC887320E113.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A750BBA8-3A6A-2343-B50D-238E20ADD3C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CA0AD449-C2E0-9E42-AFFD-BA7A6A2C12A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EC5BF03E-900E-2844-AC7F-DC35E4B0BEF7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F52A3B93-6FB7-7742-95B5-B8DA491CFB6C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/09171982-D9F1-6548-A0B9-976C270DB7D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0967C890-7EC0-F643-9D2D-A7A16B310E06.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/46863060-6003-F745-98FE-953C347F1446.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4A2600AA-60CB-4E4E-9AEF-4AF9F92029FC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5DDBD539-4D05-2E41-A0CC-A43AC8B1AB00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/7216CA7D-4E29-7840-8058-CD08AE980E17.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9C000FD7-2114-CE41-A225-57389A38CF37.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A76F52C1-32D7-A14D-804F-23A4E848BC06.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/AD36C01C-3C74-0746-9C58-03C177718BBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B69B1CB2-9D90-214E-9639-CA6409AFADC2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DD2E2B2B-BEB2-B944-A38D-BED9D2353323.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E8466C4B-7506-0A49-ABD7-BC5F864643FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/EF02D94A-BCA4-304B-BA1E-AF114B3BF46A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F0E211A5-3B7C-7542-A706-43C8DB9C300F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F65CEE88-DF1F-8F43-8275-32B444D7F71B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/02FB500D-C3B2-FE4C-88F9-6EBAB4842F00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0B8DCCDA-4D2E-E84F-B9F8-B32636135612.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/11BA2ECF-33C7-7F45-BFA8-1CC8CAC02DEB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/13217948-61D3-EC4B-912E-97D648C80F4C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/220E0C32-F961-3D48-AFC2-521D7B17BB14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/357D5218-B30E-8349-84A1-6A0D9BBEB885.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/36CA2482-8983-B14F-AF40-6EAEBD2EAFE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/376D27C7-B172-424B-BE1C-BFF97AFFBA73.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/44BC74B8-0F9D-6549-96C4-7A3026A920A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5785CD42-58CB-8A45-8F27-E3DB2E2DC3BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/593AF9E2-9B47-B842-9CCD-62964B9EE574.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5B466191-7461-3342-BD54-1A35B9A1CA43.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6116A774-BDFA-2F4E-B873-FC5AB743472A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/63135F11-2587-6F41-9563-5F6AA84266E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/69F6C4E0-E65C-3746-BF85-50CAFE808AE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6B3745EC-AD5B-944C-9D66-127084B24B26.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6C88B929-94B6-1545-8FF6-898A3C4EBF5D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6CDB53DC-37DD-494D-B4C2-B4AD1E3B1086.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6D437515-7F69-5849-832E-34ED51A7CC0E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/757416D5-A339-4C49-8D72-5A08E576FFED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/78F76F17-1395-1242-B6E3-C13B6DB6C2D9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/828E2673-3386-864C-AE19-3BA8E2BCE0B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/84067E2A-685B-C44F-B73C-2823DDE03DE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8709C2AD-AB31-2D40-8DC5-1F2645904EF9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8EB5804A-D41C-464F-8E76-5DB1D1D419A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/999B3EA2-C930-4843-B0F3-12A5F241B03A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D478AD2E-4B6A-9347-BF8F-836A5A695B40.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DD2DD994-0F69-5E43-BA1C-56921BF4DA8C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E88326DD-3908-E648-A4E2-E51F4C4970C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E9FC5262-A88C-3747-9DB2-72CAFAC00485.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/ECB21CFF-824F-084C-AD72-C9CFD4051F88.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/EF34D4D1-2D22-DA4D-B507-3A567A10E32E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1AFCED82-4350-B24D-8937-7A51E21E8C19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/231F2BAD-F243-B54C-994F-5269C5DA77E6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/38505976-7758-614D-9195-458BBE3C97CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3E2FE8B8-3E51-4F45-BC0C-98AD9892CE9D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/4DEE01F1-32E2-ED4F-9B07-9D8380F664DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/68BBCCF9-8295-104D-B1F1-D94FA318D5F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/777388D2-100E-8F4F-A8B7-9818B5B5436F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/88566603-9C4F-3548-9397-492A8BFF9D4A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/96966A87-37C8-EA45-8232-DC24C5CA6801.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A312D2EB-3D63-2C44-A89F-D6DC014F14F6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AABED8CB-7AAF-604A-ADB0-2F2A6C1DDE2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B491CE85-AEEF-7347-B264-3DDE222FE4EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/BB6A507A-E416-8C46-B83F-E1AA1C6A7E1B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D147A310-8E75-384E-9BDE-2176AA039B41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/DEAF8782-3DF1-7B4A-85B2-ED7BDD0552F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EA565E2C-A9B4-3046-B8C3-D15A5A86BDD6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EBF1EDCE-F9C1-D84A-A7F8-ABEC17720F5D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F54051AC-99C3-8C45-B37E-92E75AFB5A17.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F560654A-1356-9649-9CDF-3DE065A5A446.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/FD481F2C-4FFB-7E48-AAE2-7F217061A461.root',
] )