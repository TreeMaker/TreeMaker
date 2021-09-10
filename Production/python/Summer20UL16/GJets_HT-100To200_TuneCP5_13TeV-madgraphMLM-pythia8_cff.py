import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/0E06426A-CBE7-124B-BC8F-8C9A55593B73.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/1053B1AE-13A2-6545-B281-74789334BA17.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/110BA91A-7BC8-8F4E-B2D5-F59991BBD0C2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/3C26F64D-CE44-5349-823E-512F5E135C76.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/5A7F860F-0045-1440-8B67-B70C915610B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/B4808421-8A5A-7F44-A24E-6FEBF665D5E9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/B612CBCB-2573-A74A-9FAD-D6457A19C153.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/B91B1FFC-7350-EC40-918E-2DC07FD3C5F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/120000/E8526534-53C3-3146-9C96-E4A59029B749.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/04BCF7DF-9465-E84F-82A4-60FDF6A66FE2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/217B45FB-8BB1-884C-B022-9580B3DFF028.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/24260965-1AF9-0E45-96DA-F4B444D65349.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/2CBF57FE-EFF0-144C-96B5-1EFDDFBF714C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/358BCB64-FCBB-AC4F-AC8D-5EAD316E32FA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/3BE3F72E-3E24-E743-8D84-10ACF4F10E97.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/41B2E189-0AA6-FD49-810F-1E2C59944703.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/5CF58725-1F68-B041-8C0C-6E9B0B0F5DF7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/6C4AD7FE-D730-F34F-B371-6470ECE559A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/963C15CA-F0B2-474D-A234-7B700F8144B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/C1D35E9E-DF1D-F647-BD1A-7632667EC363.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/C55EBD50-3096-9C42-8ED4-1DD3459F060B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/C800A1E4-1550-804A-BA6A-DFA6611E14D4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/C8276A7C-BBAD-A045-936C-BD67A8E2AB0B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/CCE0079C-DBAE-8545-946C-7468444AFBA9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/D17CA08D-3C53-5E4D-B1A5-CAE59F4849B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/DDE9A29C-EA5B-9E4A-B3A2-FCCCEFFE0D8D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/EA09B99D-0567-D14D-A61B-3C8715400EE7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/130000/FBF5908F-7BCC-D243-B098-DD40B399E00A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/0E51657F-5FDB-524A-89A1-C524B7404F51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/10DBF8BF-40B2-2840-BDC5-C0FCB12ED1DA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/17BFF376-A47F-4A4B-A3DE-AC16C4037E28.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/1A2271E1-F732-3049-AF42-869FDE9D5442.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/1DC96CE2-4CC5-B94F-8E8B-1CB9C122556E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/1F71EC8B-B449-F540-B099-53267DBBEC40.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/4C7748B6-D8AC-BC4B-878D-0E826F98BDFC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/5A4B64C9-0982-9849-B600-FC7EB12DFCA4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/61B07426-5D7C-6A41-B114-A0BFF542F724.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/7941340F-7036-AE43-8BE3-CCF38716147E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/7957C8EE-5F01-634C-BF37-9D759CC39C66.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/8CB4442D-FB83-2A44-88FA-F4BD4E4A99C5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/91AA6F55-303E-8146-8B1C-B65DFBC8F3BF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/94A95F56-3BD6-8D47-A7E5-BA703859398B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/9C522C87-7EC0-244F-87AF-E0DBEF0C81E3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/B819F418-5545-5C4C-9079-E5ABDC3240CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/B9A46091-DECA-CD4E-92B8-CF4522C9E844.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/BDA1E151-E66D-EF4C-95DB-76FA5166B75A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/D21B7D4C-48C6-CD43-9B7F-2900C9D50723.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/F361E7D1-31A0-5549-AF4B-53A6F11C6B4B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/140000/FD021494-A488-364A-8C0D-13CE2B1E47A8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/01D7AB9E-6467-DC4D-9997-95C1ED2785D5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/03915892-B30A-A447-9BF5-1564CF8127DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/09FFB3F3-B6B4-2C48-AAC5-7D8FC584D42E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/0CC78CD1-DB68-1447-9D7C-5807F9A3654C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/10F2076B-A4C5-3F4E-9CB1-3F0BABC42FA3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/1557CEEF-D36B-0D4F-B114-7AC3450DF97D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/1C0245F6-9B4C-BC48-AAB4-21FAB20DB9D6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/29571756-2535-464A-A8F7-4B072D73025E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/33A10E45-4BBB-8543-A9A3-EDCC8A3D2949.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/39EDEFA5-D1F1-AC4F-8719-73FB2D7447FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/3DF2AE5D-F05D-7D4D-ADE2-E91B5FF71014.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/69F35590-6DF4-3448-B086-65B3944B21AE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/78289AD3-DEDE-BC4D-89C6-E9C6804A738B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/799ECBCA-E5BC-074D-BFB1-5EBC3195A689.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/8AD9E456-8D06-0544-9FD7-767633A97149.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/8B993842-5957-E145-BED1-9CF4D98CF218.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/8D098521-BE9A-DB47-A70C-E96BDD23BBBF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/90F3714D-E46D-9646-BA03-BC9E87A9D8E2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/A14F2BA9-74F6-7E45-A479-FBE26435A90E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/A8D7EA4E-B1C7-6341-83C7-F86087640547.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/BE770F52-CB6D-8542-827B-EBBEA12BF2D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/DA8AC5F2-E75B-7E4E-8BDC-96DAE723D678.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/DD920810-EDA0-A749-8694-2CA694E79658.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/E8C6B45B-AE0E-1746-A09F-C5B505BB13A3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/ED099FFB-9E81-8641-A916-23A2877F5953.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/F51BDC43-A196-8E47-B904-5435BF51733B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/270000/FCF8B8DC-726A-D040-A5B0-9017D0EE17E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/10999E55-B40C-EA47-942F-BDB91408306D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/1E1E2325-90DC-7743-977C-1275BF5A4C24.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/25DCF6AE-C747-C74E-B2E8-121E6640EE51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/2B2E7630-0782-014C-AD09-E83F3B42859C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/33A6D131-D222-374C-AD50-E6D9D7F6DF4E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/371835EC-05C3-854E-88AE-C04C5138D21C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/4059F4E8-EA44-7B4C-B28B-A8D305FED59A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/4889CF49-43CF-2C49-8A5B-056A4F5AC37D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/50307FDB-3FC8-5F47-BA71-A5B896315813.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/52D4D79E-F65C-5048-AC49-9068ADCEDB85.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/53B2AEC4-E12D-0C4E-B532-07DBD6F53AD2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/56EF106C-4328-B14E-B90B-FA49AE683485.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/7B67DA77-979B-B34A-951B-2CB1665B8140.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/7E793759-79F2-9947-A622-4E4D33987D06.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/7FBC6A43-B1DC-A348-97AA-908D16F381D6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/81CC5DFA-DD6E-F243-937F-579902B7CE28.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/8C587C90-48E8-6D4F-8727-302918D4C713.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/AA6BBD9E-ECB4-AA48-B233-876CD71C9BAC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/AC722679-5F2F-0F43-A29D-055AE33CF211.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/B3FF3235-A9FC-0442-9C16-0817E0D1686D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/BC8810C6-25A5-6045-ABE2-0008DD5093BA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/BE0D5230-2073-7043-9D30-90ED691A66AC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/BE70EAE8-6B6C-DA46-83A1-D754810CAEA6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/BE751A6D-A910-964F-A5FF-2742A1249637.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/CFB687B0-A88D-BC45-8EAC-05F6C703C31B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/D281195A-315C-EF48-AB01-8152872D9E3E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/D311033D-C028-C346-956F-2335917AB8FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/D581D43D-BAD0-3047-A69A-52DD18740BB7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/D888361F-02CC-784F-B486-AFE9E722F7C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/D8AACEB9-07DE-D746-B170-757D5D03F12E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/DA26D15B-0A0D-4B43-B1A5-E03875FC940E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/DBD9D9C3-BD75-5D4C-BEFB-F7E707968175.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/280000/F093C11A-2A03-8948-BEB9-09FF874CC245.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/06F36184-EC71-DF4E-A1B3-88BC25C3BFA7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/118027E8-BA92-5B42-A3DA-CCD5488C384B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/12159A4B-869F-EC4B-8EBB-C21ED88FEF14.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/1372C372-A46D-8546-B104-CB008ABFF69C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/16F79B4C-0A73-6046-9F70-9A99A8ED0B9D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/25ACAD67-264D-1441-856F-7D0516B6C6C7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/2A592FC6-29F9-4B4D-A213-24C9DAFF8053.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/2F94352C-9CF2-614E-9EEE-52BB75D74D2A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/30A5E190-4C5D-B243-B8B4-B2740AC89844.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/323F9207-0E2D-8B49-BE98-F4E160D27694.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/3EF8D467-AC96-9947-9D03-F15DBFAF8534.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/45F2E2DB-1708-CB45-AB98-BD6465F227A0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/46D3EAC2-3D7B-E64F-B7AC-F939641F6A10.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/4F32C8D3-B355-4C43-9F57-94F8C346900B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/53016E73-505C-1144-A005-4EECFE41ECC9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/5DA9C5B4-6616-9B4E-8832-29D1588F59D9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/5EF3DF08-7991-5745-8A6F-B46FA63F5D20.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/5F0C076F-D746-0B4D-BCB7-9889FC2F6CB9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/5F9EF6A2-EFA1-504D-AC6F-866505D35463.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/62D3AA61-27D8-C54E-91AE-96FC3DB09487.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/62F14600-2A40-1140-8E9E-0DDD889FEE5B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/710A21DF-BD1B-9843-BB7C-B40C4EBA8B26.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/7114A7B8-6B0A-9A43-B13F-1F50DE87079C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/71EFA98E-765F-CD47-8D15-10004BA01C20.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/79940584-6C84-E54F-BB4E-55D967ACA021.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/806DB392-812C-D440-9A6C-C0DD27F4FAB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/810AE7EB-BB5D-1C41-B8D9-305839AED561.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/8598F956-61DC-5A44-8B75-243643D278CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/937E0762-C0CA-B948-ABFF-A98CC45DA6FC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/9E41D240-9A41-C842-9426-32CD3EC46324.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/A402479C-6CCE-0C4D-AC4E-42B72F43BE0B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/A501124E-D3F4-7044-8646-C64D0FAE557C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/AA5B2B99-8B5F-5D45-ADD5-40E1D513430D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/B0073B41-2AF3-DD41-9142-6A1F5933DAB9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/B393C54E-2CAE-2A48-BD4B-29DC45E9E9F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/BF5700A6-1F0E-0540-BCBB-50424A7B28B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/C3C22255-2251-EC47-A4F9-8ED161E6468F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/CF0E358F-0748-E24F-93E9-14CA1BA71C2A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/E3CB9573-4F1B-514D-BF15-9A68CC84A7CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/E9AD04B1-E667-5346-A5A8-2FB2AEA5A342.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/EE71ADE0-80D1-3049-A2F4-77B673AAECA3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/F2C6E769-976B-2C47-8F03-7BB7710EC602.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/F4BA6F05-EF80-B746-BE2F-05B078A5AEC6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/FDDF19D4-C7CB-9F44-A451-7A99FD49AA08.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_v17-v1/70000/FEB30804-A5B0-364D-ADF5-D6A817335022.root',
] )
