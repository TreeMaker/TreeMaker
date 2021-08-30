import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/046FB7B5-AF25-6D49-93B6-9A6026E6D5B5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/0BD54C8F-66A0-E04E-AC17-59B4B10CC795.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/0C37DE7A-0318-AE46-98F9-C2DCF2E2E8E6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/0D9EC36F-072E-0F44-BF98-F14548ABDD87.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/0FBFBA80-1152-B94C-B32C-88955DAB9F25.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/177951F4-D45A-1145-BB1A-C2398EDD5887.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/184B44E6-17AC-E641-9771-E76191228A47.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/1A1C77AF-3591-2E46-B0F8-EB3001A2BDE1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/1D06476A-BE76-7C49-9BF6-D1E7D5E76B33.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/1D1EFADA-68F2-604E-A67E-DB25ED094D21.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/2397B4DE-7DA5-1B48-95B4-734C6314F932.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/2565C920-5BB8-BF4A-8DF3-8960875D3811.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/31A46A21-84DD-A648-A624-332EBE31F93F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/332E246A-451C-514D-9C31-F01CD5512128.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/33AB92CF-BDC0-9541-8739-A28C264682EF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/38DDB0BC-787D-F64B-A479-A77731937C30.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/3D074144-9E7B-5844-B5F2-2F970E1E5518.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/4048AF2F-11D4-674C-8953-CE39C2C5EA44.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/413783F1-D0B4-8747-B91F-793525DE4592.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/4279AD74-81BB-CE42-AA63-4B8A1F8A7251.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/4A15F52D-C660-0B44-9289-64E73F0C091F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/55B5B99C-8BE7-4741-996F-37479F8FFCB9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/580CBDB9-AC6E-5345-A9BC-40A3412D6DA7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/590B8E81-B6EF-9D4A-8645-647EB18368A6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/59335BBA-312D-8841-ABF4-30DFAA5B7E50.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/5A0A5BED-775C-8D4B-A12B-D04BC66FBF0C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/5AEC8AFE-41F7-0843-A391-6E95BC997E91.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/5E095C58-BEFF-0B4D-AF0A-C5215C9D645B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/61FA6A2E-B596-A249-9686-5708AF7FBAB5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/6310D862-C8C0-0B44-8A05-AAF1820F61C9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/64C71B33-C059-8942-9E0B-2FFE6B7A8211.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/65C34DD3-C78D-0C4E-BD7B-A359A50F96D2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/6A321954-21FE-E148-812D-2255B9394F1D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/70675DDC-5FC2-2341-86CC-90D9C70D994A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/71E64064-79B8-4647-9BB3-447F1EE79147.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/768C844E-9CF5-C34D-8956-03C0F58EC1DA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/78F6A2C1-333E-9E4F-A722-F5D04E77A0D8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/796E8E67-3CED-4A42-92EE-54D61082CF16.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/81AF3F88-918F-7746-B347-9B1FE20757DE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8541EB79-B18A-1349-89E6-ECB550B440AD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/85C84AFF-1401-0041-ADBA-9272FC3FDEE1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/860697CE-3AE2-E949-B56A-EB86E3758E0C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8797A317-F197-2641-BAFF-FFDAFA6BA2F5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/87DE8ABA-564B-3040-8790-AC8AEDEED738.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/889F737C-B8F5-5D4B-B5C6-288ECA297C53.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8BAE7923-CEE9-1E45-900D-DE6311D4EC86.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8BF0EC3D-222C-BF49-B4C1-C75BB4FAB90B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8D76DE05-5DE1-9841-9A86-600B3890FF2F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8FD7F555-E8E1-2B45-8D74-03F1B94A805A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/8FF470FE-2C9F-8644-B6D5-36F59B014D41.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/9383B6FE-82D4-A942-B498-9550819F421B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/94AB9BA0-6CAF-1A49-B34E-53FF53E8EAE2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/A3D0025C-66CF-5343-9F61-2773181AD744.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/A821E4F1-9A14-F644-B566-CD7A4731A055.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/AA111C34-4A11-D249-93E1-BCF02DB313DA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/AB5E8E52-14C1-8245-8F8A-260E290977B4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/AD086833-3007-1643-B1CE-081A5A67B6FD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/AD5AB5C7-332D-074D-BB57-F3E7BC1E4C31.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/B00B5D73-930E-9C4C-908E-963D22B05008.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/BCCE0FB2-8EF4-D14F-BCB6-19A3B3E16350.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/BD640AE4-E270-AE40-AD8A-AF1AADE6C6A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/C9687690-3207-6741-9D52-B9DEE3D920FE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/D214149E-E43C-3044-B459-EBE2327D23B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/D35F26B9-5B9E-2242-B026-DFEAB60ECC36.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/D3BA12D7-955B-EB47-9448-C825AF09B0C6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/D4F6ACD4-0DC0-8C4E-AF1E-6ECA0FDFFDCF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/E288080E-EA93-F244-87BA-C5EBCAFD93D6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/E5B95AC8-6146-A04F-8803-9AF525193F72.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/EFAE9792-0170-CE42-933C-92ABFCBFEFBB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/F14BDDE6-38E3-A84E-8BDC-BDC298F6E5FC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/F973DE39-6630-E148-A67E-5C7BC993D14F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/FA79E9ED-6A92-E141-9133-75652F1F02DA.root',
] )