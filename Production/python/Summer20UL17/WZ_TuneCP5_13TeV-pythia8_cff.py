import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/02D10B77-1F18-9A4A-876E-335295ED65BC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/035E7436-6255-3F4B-9ABD-44B76D8A7F69.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/095299AB-A7EC-684A-A744-B16E9EB34967.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/095F4349-FBA1-BB4F-B0BB-361C8F9E25EE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/0D58A460-7603-1E4A-9604-533854690C6A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/114AD9BD-4AED-6E4C-880F-6EEEABE0CAA4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/148AA814-50D1-2A46-8A92-49D67B40BA21.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/156345BC-F455-9244-9F40-3025AF26C3A5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/16B9F934-0C5B-6240-B309-B487422A0505.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/183886D0-61EA-014F-991B-592F1022B9D5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/19DBBD78-F34B-A64A-A33B-E3A44818B5FA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1A40A929-9A05-EA4A-BA67-85F45D5748D7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1B97DF4E-FD5B-2D4C-BBA2-AE4BD1B16123.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1E784E35-C2AF-824E-8293-339EEC9ACB41.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1F0FCC84-BAD9-C248-9747-23220BBD4FCA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1FBA6115-28E4-CC48-8DB6-6380F7BC7B4F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/25D760D7-A043-1B41-92EE-B17DFE9BF475.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/290055A1-95E8-7242-914D-F487B816C522.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/29D787A0-4CA0-1B42-AA76-07F76A558BAD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2AEE5AF1-D871-EC46-8AEF-2ABEA5565C0D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2E12A557-DE4C-2042-9BDD-5394DC8E6C1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2E2C4F5F-B923-DD48-8428-614ACA3C9958.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2E573237-CDC2-6F4D-A03C-B7E66934CF44.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2F2433EC-9396-DF41-B5C5-B568636719A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2FCD1730-AF09-EC4D-A8DD-CEFECC1AEE26.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/2FDAED9E-A78A-6D4C-922F-838CF4513EB7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/31A17597-84C1-4249-8A4F-D726CFBBC87B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/328ADE3D-4EB3-E44C-97D1-A67EDCB11CC4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/343BD89C-6203-1F46-961E-2066972CB885.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/383AF52C-F519-CD44-A4BC-5C51A980B214.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3A520908-9AA7-6246-BA45-FCD99BA6A8BA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3A9CEB65-EED2-1D4D-A991-6BF4B0C583AA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3CC43B90-D345-0B4C-9A1A-90755A6A2520.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3D155DDC-160C-4D40-B8C4-165A6EDC4BFE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3E1961AB-5868-9242-89D1-35E99F291CA8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3F5CC3C9-6E20-114C-9828-5649E3D57D1C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/432E5BAE-1F54-6A4B-9407-46822ACC58CC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4886A3FF-652B-364E-8CEF-992A3FCF4F80.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/48F89474-476F-974A-A234-BA0C49E2C9AA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4A43CCE9-5359-BE42-87C1-FB687D6ACA51.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4BF50833-B0FA-8144-8C7C-F4C730CA530F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4E059D21-01C6-EA46-A0CD-20B53A231D24.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4FC85792-7A98-574C-934F-2ADB048582E3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/50D5103F-F28C-1148-9695-844DB5E2B97D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/549D7279-CA09-8B41-AE7B-BA89415276C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/5F8BF580-415E-B34D-B89B-4D4BAC9C0C18.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/60A63E87-4CBB-BE45-A4B9-B92EE2667B69.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/628D3A73-5915-A542-8EDD-A5A71216126B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/6377FE91-7926-1443-9EFA-66431AEAFF03.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/6551F158-31DF-2F45-87BB-F8B50A2EB64B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/671C6BA0-9180-844B-AF87-3C695AE961F9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/68326A80-9417-3F41-B5E8-353D2367742D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/6D633993-60C3-7945-90C3-7D4AF8975F1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/6ECA226A-FFBD-A142-AF4A-941E47F30E2E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/75D0A9FC-C2CE-A34A-A6E6-14365D8F3EBB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/78D1766E-1095-9742-B797-ECF8E8C25C52.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7A3DD46F-FB5F-CC47-AD31-702FC54CA9A8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7AAFFA24-4CB9-9243-9E18-1939ED1932D5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7B92D6A5-D607-9D45-A371-3EE0C9974B98.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7BF9C22E-1557-094E-AED8-BC64CFB20E20.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7E307A42-3FC6-324D-9799-BA7215B04397.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7E63CD7B-3F93-F54C-9284-468775EDDDA5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7E8359DD-D412-DB4B-A7D4-AC8C485F2CAA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7F08B72B-9123-F34E-A378-4CCE031712BD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7FEC9977-9F8B-BF4C-86D6-062EADDC38F2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/80C423F1-CC0C-5E4E-A3AD-899FB44377F6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/816892D5-2418-F449-B931-60DC9621AD55.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/8461B80B-FA18-7A44-89AE-2BD8865A114C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/84DD1F04-C9A2-8047-B880-352A27B4FC99.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/857B46ED-E48A-C648-B498-3B1D16ED28F1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/8D1331E4-6E5C-FD40-A960-011E0C8E2659.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/8F4F43B8-D552-DF44-B5C2-C9092294B826.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/91DE5445-7CC6-394A-898A-20C5CBA2D4A7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/94898562-835D-A945-BB1A-AB126B086F28.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/9B44B3F3-9097-DD4B-AB33-959BD4A420EB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/9FAC7DCC-74FB-4F41-BC17-61C6F89D1CCA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/A19E255D-F452-984A-B1D3-938A9E039E37.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/A1D096D5-4E45-4A4E-8DAA-0629859D6B04.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/A28608AB-8D08-CD4F-80DF-5BFB64602AF3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/AAC06EED-1C67-BE44-A43A-768801B778A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/AF9FC15C-62B8-E844-BE65-87F403E260B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B1D7230D-5FDE-4440-A26F-5BA001CF42B3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B28D9580-DF3B-1B43-8983-A60FBC81E9FD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B49B60CE-5C79-9049-BC3E-8B1D4A7B737E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B67132B7-31D8-BC49-BA49-461832D09EDD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B7AA9E10-14A5-AD44-9A67-4587354DDC79.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B93D24A1-D11C-154F-B5C8-8322D22546C1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BA02DD9D-7F15-5842-A0AD-91BCE3BA58E7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BA66AA13-9D23-844B-955B-963DB8206061.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BB7088C1-8A61-3349-9544-5E8DFC8534F8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BB75DBB0-5A1E-994C-85D5-331F2A8E4041.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BF672F61-54AD-054B-B59D-6A0CDC3F063D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C07457DC-54C1-D248-AB3C-71CB1B7BF783.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C08F3B86-A3F0-834B-9EE0-C775811B31A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C62BC06D-8EBF-574E-9F60-17E7FABE5903.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C7F37A59-63C3-004E-9D83-83E3FA03F847.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C85BB8B2-CFBF-9049-97A9-8C2F5041D3B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C93BEC8E-3A57-9041-ADD6-932B9E85D47A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C9987FB0-0C2D-5B4C-BF79-12959DFB3344.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CA4057EC-382C-3343-8130-CA819AAB148F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CE5DD4A9-39A6-9849-A364-D615D8439E8B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D0A3B986-ABBC-064A-9D06-9A3B49A88BD8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D34FD75A-A5A3-5D45-88BC-B8147C3EABCA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D846664E-2341-7340-B420-7BC1CAF1DCC9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D8782774-F1F7-C944-8AD8-EF4095041F7C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D89BD5CE-A2C6-0343-A273-8CA8177C0056.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D8BCF96E-546A-A244-BDFE-CF09F8C56192.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DA8A7F87-4B0D-6A44-8113-A9F5E8A6B9BC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DEAC9B45-2E92-5247-8942-B029926D3B68.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DEF8DE44-4FCB-0148-AF80-2725845A9499.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DF9241F5-DD9A-E447-817A-75E10A2E6D0A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DFE45156-FFA2-BD41-9F1F-E420810A9EB6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E3F4D07B-AADE-EB4B-9DE1-9FBCDDAD4D3D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E4E18A4B-AD06-7146-99D6-DA1968C13C63.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E61DFFF4-0EB6-8E46-9208-AE0DDD6A6C6B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E818C7CB-B342-AF48-B9D2-D769A0A1BA46.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E83E9A38-D3DD-F744-9A65-492C1A1F63CF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/EB397F18-3D58-5941-AD65-A12490D80476.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/EE558AB1-1902-964D-903F-459060144849.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F1A511E0-0E25-6140-A13D-9876049B84C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F3B45A6A-642D-3143-9FFD-E8E19D9A57E4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F44407B2-5167-B54D-8867-31BFC289BF7D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F7D2E689-5C78-CF48-9DF7-A749AEAC35B2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F8CF4732-AB88-A840-9FFF-CE9C0179B4A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/FC636216-4849-A74E-B168-3F6E5D829AE1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/FF20B24C-B74F-034F-A695-293ECBF9E4A3.root',
] )
