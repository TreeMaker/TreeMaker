import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/05E5BB02-377C-B64E-8B1F-08980347E5C8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/062355B9-741E-964C-A791-4680FEB17A58.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/06C431CA-BE51-0F44-ACC8-129C2E92536D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/07B6D37D-EC42-2C4F-8B93-F46BD9CF2822.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/09770FA9-78BD-844A-8B4D-8B1E9CFC834D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/0CC2B775-D5DB-BA4A-AD76-335FC108AEF8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/0FA90193-17CF-7444-9D7A-6338278BA476.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1359D816-7F8A-A449-A863-7EDAB587EEFC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/13680025-0B6F-EE4B-8F79-05D235F58AEF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/14A61AB2-C415-AA47-AE95-2EEE340922F2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/15A582CD-3722-D744-A385-2AA1FF80BEE9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/16B24CF1-D2E7-794C-AFC8-51160843FD09.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/175ACA09-35F3-274B-8DA1-2B225F8B774D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1A4E1D72-B69A-E048-9B6D-151AF3827446.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1A5E8E4F-4ADA-404D-B180-D503520649AE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1A65D735-683E-AB4A-A9F0-CE8B71408A9E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1B82C0E0-E77D-8443-80A9-E64C13A14E1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1C739DF8-AD18-A64C-AAE2-D292E4AE17A7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1DBFDCA1-AB73-814F-87C1-CA4CC96F3557.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/1FF2B7E0-171C-6446-AC3E-B2A0A2FF6897.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/20124760-9110-3948-851B-EDD69DACA60F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/20593E91-2F31-B348-8F83-94D25037F5E9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/21340AF1-B8AA-3345-AE1C-0BC8F2EA5112.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/22A4C9BA-654A-3641-B712-2B4DA28AA56B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/22C01E56-C174-F347-A93B-5993BB4EA008.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/2339104D-F2A7-1E4F-A3BA-0EDF75AC0F1F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/23604B8C-4EE8-E349-B79F-B257455262CD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/23B495D2-4476-DD4F-BD9A-C560CA388A85.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/23FB2779-BE62-7440-9E94-EDF30F1E07BD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/2853812D-0AD3-974B-9E96-DE289ABBCB9F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/2899CD1B-9A5D-0D47-BF92-CCDF18BBDCBB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/2D6F8531-ACD1-9048-A754-117B1F4B9596.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/32A6DB2C-6F7F-4440-8676-5AA89A4E9CB4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/32D71852-3FEC-8743-A37A-12428FCB8B82.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/3915674A-4D38-A44D-883D-0AC67076AABE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/39B8C98A-42EA-2947-BE1B-8AA98DE414AE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/3A729CF1-C0CB-BE4B-B4F5-0739EBB884D2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/3EAFE817-C358-1E4D-BA52-3F15AEB05BAC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/3FA4AD1F-9AA5-C348-B8B8-3DBCAF09B2CB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/3FB1F598-C70D-4C43-8D09-6D77D821AF34.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/403F15A1-A9C8-9540-BCF4-831D4D74F314.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/44EBF164-28B1-9545-8CFD-63DACE121436.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/453D84EB-4A94-A446-AE0F-B7B56BB0EF6C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/47F68561-C06E-F840-AB79-43348D26EA8D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/4933754F-7ADB-004E-A523-9A71B28CA4B0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/4C47BAB3-9B65-DA44-A734-4D7775418168.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/4EBC03B3-C01B-A94D-AE13-DB80B69FCCD3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/511CB818-1E80-3D41-B8C5-7ABFB20AF3CF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/518ECF64-018C-0446-85EA-9A08550A6712.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/525713BF-0D8E-2148-AAB9-03F34D804A48.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/5716DC54-D13B-8B43-92D3-EB02D52B2A5E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/5B5598BD-39DE-8145-899C-131E19029E7F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/5BF3157F-B8EC-DF41-B1AD-3137CF56C8AF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/5CD74243-92CE-8D42-A314-7D2A2902BCDD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/5D488360-2280-D546-8DD6-8C548F5B7BD0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/5FFF794B-293E-9A49-9A6B-EE3BC8FE137E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/61682239-83E6-AB41-BDDC-6EB0F2DFBBE4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/61A6175A-8322-0C41-9718-B16B64897A77.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/653FCC67-E2B2-3F40-A7E6-B00EFA121E39.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/65CCFFB6-0B34-3648-A23C-EF9E5C4F0065.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/677DE7D8-FF8E-9440-A5AE-0F0DB37321B8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/67A4472A-E470-E148-851D-777A7B9A047C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/694CEE76-1D40-4647-B57B-4C7E39AAF725.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/6B71282D-3CCB-2C43-9695-7E74194B8365.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/6D6526D9-7E4C-6448-A29A-25A4AE9B374D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/6E495ABE-C794-B54C-A110-3AD68FA2DA95.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/6E58561D-56F4-DC48-9845-05236A1610B9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/6E7BE779-80F3-0744-AB8C-E05137A34C1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/70D6DD6B-AA8D-7B48-B133-E40F4DE74872.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/7160A376-E8C3-394A-AAA3-F27D93ED9DF8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/71890486-C2E5-A84C-980F-2A26689F1365.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/71B240AE-395E-7D4A-A5B0-3C9A22CC5CB0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/74276A99-7DB4-494F-9F54-431C403140D3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/744C35CF-DA6B-C443-B7CE-714C5D2A4268.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/74EBE4BA-ED26-D845-8F57-5DFD977CE437.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/762444F6-ABAF-5447-B318-E880C152B40B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/76C9065E-50F0-E94E-97B9-484FCBCBCF2B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/78422DEA-B0F0-FE46-AC28-B11E5C2FB13D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/78E3D60C-C6B3-7A43-9FAD-BE8BDE58FD1F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/7950BFD4-4BA9-DB49-A17E-DA71BFF58803.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/7A56ED66-52C1-EB4B-B0A8-0B05C08FBB0A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/7EA9AC2F-0B7A-1341-BF97-A942F804CFE2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/7F067947-5BD5-FE41-822E-8220B0E76D48.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/8092799A-18EA-504D-A5F8-011DF55B3D26.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/8174BE70-F57B-3D44-84BC-62461AE3EFC0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/82B0AFD1-01A1-624C-AB77-FEEAEA8BB029.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/834F2598-EB7B-2143-861A-456AEF8FAEA4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/867E253A-4342-D245-88E8-26C862ED17B5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/86B20496-2DF6-AF45-A529-8BFDD15A27D2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/86D8CE5E-19A8-F340-A3A8-BECED40C9B7A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/87A9007E-59FB-0240-B4B8-5F92159EE95A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/881ADF26-BE7F-DB46-8A51-B6FC948C61B5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/8A69A92C-F419-6448-BE3C-617416DE3A6A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/8DF4AD39-F190-4246-8FA7-7DB8C1B38F21.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/8E2B6293-F61B-0D42-B20F-C2DDA8AC01F2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/928F6669-E81D-5247-8A24-1437D1FBC0BE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/92C62695-0A24-0D41-A9C0-5E7FD2BC5512.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/92D8D8AF-F318-AC45-A68D-1C7C05CF21E1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/99A501BA-E2D7-774C-A357-BFE85E65948C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/9A1869F4-5B92-AB49-9C52-AAC7BC3DC4C2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/9BE4F66A-7CB6-FA47-9027-6C2A4A94ADF6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/9DE72870-03D4-1B48-8D20-3549F5D6FFE8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/9E610AC6-7E35-BE4D-B274-FAB261319BDC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/9F84B76D-43EB-3F43-86C6-E371C5290D52.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/A1DBAC53-2E90-3942-8F2F-9743894ED2AB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/A2574DC3-A726-E247-9310-41DBCE26BD50.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/A64F13E9-F447-C349-9CC4-6D348DFA2E7E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/A67C41C0-CB5B-0748-B21B-0E6F9D27FC80.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/A9FB23DD-D2E1-F440-B8D8-44A487B53155.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/AA1FAC60-2B89-404F-B8B5-042C9A8F9EAF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/AEDFAF53-D66C-C94E-83F3-6E390CB3B787.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/AFC2C550-FE1A-2A4C-9251-6DCF0B44845E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/B0875886-5198-3041-8750-24B61B98A147.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/B44521F2-1AE7-9544-9582-BF83E2406491.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/B5B8693E-1E4C-EF48-83F2-D322929A872C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/B6657F94-2BC4-EA4E-A13E-645EDB5959FB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/B95101B4-199F-C64C-B5C9-317FE0DD4AEC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BA2422C5-01CB-5145-A61D-028A1C9E2907.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BA92BEFD-CF25-1546-85A5-CA67285FC570.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BD042FE1-65E4-BD49-AEDC-6570D309D35E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BE937621-2CB1-164D-BFD2-A8C98C2EB36E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BE952E6A-F422-0D48-8A7E-E424229FD637.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BEE51A26-5731-4A45-8D51-94815EFB690A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BEF8D0C9-A881-4A4C-A8FE-C15C0173158A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BF368EF0-BD9F-504F-BC39-54ABCAD6D55B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/BF673D86-BE7B-FB4E-AEAB-57209F4A3249.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C0049461-9A7C-164D-BBCA-35A28BC5DDF5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C0861990-DDE8-5146-8B5E-347C314A3687.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C08D1139-11CE-DB41-8DF5-211FD452FE9F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C0BF8EFF-8E4D-9140-B447-FDB74565AC2F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C1CB5F30-4506-8943-B0BA-2A638751D218.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C21263E3-A5F2-CC48-A852-67DF6560D39B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/C9B5CC9E-3356-224F-B660-4C62E4273BC2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/CAE06461-E61C-E240-9495-95182D2DBF8B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/CBAD8A4B-E999-114E-BEEA-5794F7379C74.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/CC580DE3-1C67-864C-9B3D-620DC93BF158.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/CE01ED44-EC34-1441-B59D-BC0FCCF4A499.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/CE2EE9A6-2C1B-EA4D-AEE9-05ABFA31CD2B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D00812BF-F3EE-0647-A142-F120B1E5028B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D16C28BC-EC23-D042-8E70-512C1062D175.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D32C2FC6-ED00-F942-8B6B-717ABD856EEF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D70368E7-89CF-404E-B81D-E4AE1A9E6911.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D7316410-41A7-2B4B-958C-888DE4D72A45.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D74BC057-C97E-194A-B226-9C3099EE18DF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/D98D81C7-F59D-1E44-8789-10539F01555C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/DB29F2BA-49D4-8E46-90EC-BB0ED96D189D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/DB644C12-214C-664D-A9D3-F445AE65D603.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/DC91B3B5-137C-7746-9AC0-2AD825F4C47C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/DC9E08C3-617D-CF4A-A63D-60192877816F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/DCF51156-7788-C54E-8489-65C23F8C6636.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/E086702E-BD3D-9C47-9537-CBF7BC30AD11.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/E34FFA22-97C9-8944-B474-9E86D0F4FA67.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/E41A76F7-2B2B-EA40-8968-59F4A46F228F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/E76279D9-A88C-A44C-9EC7-F413A54F75E2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/E7F43731-4538-6443-851C-405018C25911.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/E824D878-6573-2143-ABC8-F02569D4A8B4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/EA52A9DB-9C6D-A844-8B9E-6910D0173B42.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/EB174829-8D4C-6243-A524-D91B041DC131.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/EE3DBBFF-8DEB-254D-8918-F28F6FB09910.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/F01A9908-6B68-674A-AF90-09740DF2FBE2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/F0F3B2C3-65CE-F046-9599-C355802A178D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/F1E58C61-6B50-6144-BD34-59DA4C10D7D6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/F3C9FBB4-F784-C446-8C21-3E28C1D7B0F8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/F3FA5125-F155-F24B-9B30-75120FA14CDB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/F64032AF-0C05-0A46-9877-00F51227D5CE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/FD47F826-6C4F-5A48-B909-E5F99BEF62BC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/110000/FE6192E8-96D6-6A46-9AEC-FCA32DEE2F9E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/140000/5AB38A5E-E5FD-514A-B733-F6CCBA58B0D3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/280000/6C029C51-F0B8-5A43-BDE0-4AA8B63C5198.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/280000/8BD3FD76-FFC3-5548-A7CD-62182DEC173E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/280000/8E7296DB-AF89-074D-9A79-4902AA81FF33.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/280000/AB7E2C5B-AF97-FF44-8257-2C9C8568E923.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/280000/E0A27637-C1CB-6543-8F1A-36A3C7A2131A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/2810000/0220DC2C-6F55-5840-9540-9D2971E5C14B.root',
] )