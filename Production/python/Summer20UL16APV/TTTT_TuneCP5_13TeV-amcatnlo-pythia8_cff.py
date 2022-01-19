import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/0A4693DC-3F07-BE4A-A3E7-6303E8F353E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/0AD9EE2D-6792-A54B-AF1C-1BDED1C9A994.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/0E7C68EF-0130-B542-A73C-5071B9C72B09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/10DF6869-413B-FC4A-99AE-5FDC072260B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/122AB57C-7BAB-024F-BE2A-D6A826C9F53E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1290ADA7-29A5-DE4D-9AAD-BCC60479C27B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/159837D2-A1AB-C447-9269-EF981556F747.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1A48858D-19C3-8F45-A30A-9C91B2452080.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/22206DC6-6A94-0D41-AF97-27052D99D6BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/28D81625-5F39-7341-9ED5-367B3BA38F37.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/2B8D989A-179A-1B4D-8793-9DC05B24B85A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/32B3C5B4-E4C6-DF41-A57E-5A724349EB3B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/3FD807C5-1F57-F949-A77B-B6A2937E8261.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4119A500-04DD-A146-BCDB-209856C3C3EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/43243B48-6520-A74E-A14F-DD11F504AE1C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/460912AA-BFEE-2646-A6BC-B391A9B12510.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4D542BFE-5B9F-874E-8E52-CD87CA6AE4A1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4E591B85-5FF6-ED48-AD1B-257821BE0EF9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/65E8C4FF-66D2-4D40-A595-C4582727463E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/668593E0-B1EC-7742-A2CB-8A30667F5CA1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/69FCECCD-B2E6-7B42-A658-75A9BAE7BEC8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/6CE78BD8-497F-054B-A8A9-6FC4C88083C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/6D566396-DDE4-5746-AD10-18B95D0A38E6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/6DE97440-318B-8B49-AD03-1ACE05A87AEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/75C581A5-57B4-FD41-8C0B-63E738E02CA6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/77EBD1CD-7046-F042-A222-A87098AC2F0B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/7A8AC1AF-EDB4-2C44-AD76-472A3F4A6A63.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/7CC58201-0232-FC4C-8A04-D4080CB1E0F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/819CD758-2705-2E4A-94B7-66E08C81B6D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/88AA9AEB-4B69-8749-81F3-0AC3B89A5247.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/8AD1DE66-3B59-E040-ACC2-5AFE4FBF4B25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/8BE46F35-B7E2-F74D-B2DF-6CBFA589A840.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/8BF90E4B-048E-904B-BB59-BD45402D116C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/8DDB93C8-FA5A-5A48-B4DB-9B405C0D4877.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/91A0CEF0-9A55-BA41-B369-73B4BE949FEF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/96664CD3-3A99-1B4A-8FB6-F097A5510089.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/96E71662-41CB-7A45-87B5-333E0469E3BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/97BA9C90-027F-FD4A-A0BB-3CCC1A0AC557.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/9E6D47C3-C56F-9843-B5B9-DB96DC1491D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/A15DF0CA-B9AA-2340-BB6A-1D92222EF230.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/A8CD0C21-C0D7-434A-9649-D103FE7EF3C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/AC5A4F28-B749-3F49-A5F5-A8C590752EA4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/B419761D-6361-4D46-BF23-AA8DD3A0282C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/BB823F1B-49EB-DA41-BB09-CCD947DD4BD4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/BF81288A-554B-E540-813B-D341A363A0A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/BFB852D5-8F20-7A48-9948-465F77192F72.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C2169717-2076-9040-B457-1F25164A901A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C4BC2DCE-FBD9-A14E-84E7-2E74A52FC956.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C5180A2B-A26C-BA48-A66C-6906CF5741F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C67C2329-C2C3-6D49-AAC3-E51FE33C0748.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/CD047706-9B3A-E149-B54C-CB766A2A59D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/E6F45322-D8D4-5941-8ED4-A4A63853E879.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/E7701FD1-82A5-0F46-8EDD-56FA26CD4500.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/EEF79899-4982-5240-AB28-E47528D9A646.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/F4EF68A2-D3D3-8747-86F3-321A93304856.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/F65B3854-DD65-B14D-AE0A-CBE062F8020B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/F7898058-31F9-B042-850A-B1BCCBF70905.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/FBB2EFD3-14E9-0B47-A85E-3D583371B2CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/01A187D6-1311-AB45-BBA6-1A04DB8F68F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/6599EB4C-46ED-624C-80A3-F46EC65FB00C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/8F4AB3C5-BE17-C24A-A951-21C51A13FA40.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/99417784-46D4-D147-95DF-7929FA3EE03D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/0BA8CD99-DCDE-1F44-92F6-A22E00658E0E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/1DEEC5CA-5DA1-B84B-824F-6D3029CCDEAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/29CB9D49-3400-D54F-B9F2-D223A7A30990.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/2DBFE19E-1115-4F4D-9FA3-37121E5A5C6C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/3FD099B3-F5A4-634E-8ACE-9178CBD4647E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/535EA693-F3DB-D84C-825D-28D7D9961904.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/5AAC459C-6854-6140-AB54-E5550C7BADD1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/781C039A-9D3D-2843-94C9-B5C0F5E2AB26.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/79258266-CAFF-194D-8D68-D6C4C8E888DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/7C8FFE69-1908-5A49-BDF2-576613C84716.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/83E04F14-3BE7-E145-BC5E-EB3B53A61478.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/90CB720A-967B-9145-AF9C-599E8F64C26B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/A4B8DAB7-1F44-6242-9378-5AFB893D5685.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/BB0BE6A5-AEC8-744C-A3A2-7554E0FD2917.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/BCDA3801-56E9-5944-B7E3-DDC1F2AAC280.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/C6D60CA7-EFDD-334A-9D27-80C900EF67B6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/C92062E9-974C-6A4E-A2A1-451D54E54AC4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/D3573C2A-0153-6347-8132-DCE34CB4E8EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/FBCB04C0-B2AF-A645-A8B9-2D4DA1D505C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/1623A351-0417-1348-A831-6AC0BF0EB3D7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/312AABB9-B3AD-6A48-AB3F-89C6E30E6C09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/5FF4ECDE-3950-D748-9529-5BB42D2DFD42.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/6AF7128B-5BC1-3C49-8F60-7FDE9AEA43B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/7171142C-DF4F-644A-8980-DC69DC99878C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/77D9DAE2-1866-1648-BD57-4E074985E134.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/79480886-CD2C-BE47-88EE-1A02EBA009A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/7BAD426E-4F8A-4C4E-BD98-7EA69300BD3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/8657EA6D-6309-3B46-B8C8-67CB7AEFF7E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/C02FC04D-BF79-3F4F-AF29-3C47FAF0F5EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/D4BF0032-D71E-3047-B07F-4C0F7A101A03.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/E59BA004-CF4E-7143-BD68-EA4BA66B6EBE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/EF0AF5D0-AB5F-4D4A-8DFA-AE063579CA31.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/F8C6E48B-197C-DD42-BF79-3FB4F1578770.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/FA579DDB-1EFB-A74E-8536-7F2F01BFB144.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/FC9EEAE6-4C99-4749-84BC-DD04B1C2DF25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2500000/2AFE5D35-0B73-574F-ADB6-BB3CB9EB463F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2510000/365ADA30-EFC7-DB4F-9D2F-B53F49A2DFEE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2510000/395A6F3A-D869-3B45-A961-DE3878BED019.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2510000/68F00571-DBCA-1146-977E-D2CB0CF8673F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/2C525908-284A-EE48-BC39-BB3A35F41414.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/56AC923D-40C6-C041-8149-AFD60DC69A9C.root',
] )