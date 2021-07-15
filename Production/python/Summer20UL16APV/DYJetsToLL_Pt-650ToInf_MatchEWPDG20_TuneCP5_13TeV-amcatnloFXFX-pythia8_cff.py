import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/120000/172A2CBA-BAAD-584A-BA85-BE17F8FC5959.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/01487B15-0BB4-8649-90C7-E2F264854B4A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/0CED8523-F55E-8740-A442-C5FC1120E5AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/0ED90C9D-2895-3148-9EC6-BC3C5AD7585D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/179CB63B-3679-8944-85E6-D573D8DC72DC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/26C2358A-2298-5E40-947B-709F049B5D65.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/360654E6-5312-D146-ABD0-902C66DB8F3A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/37A5B4D7-A39E-8B49-B116-E05A6C100D2E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/5B7573D8-0996-754D-A1AE-1BD1C2BDC206.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/6188FF8F-028B-EF46-9541-FEE3ACB2EDEF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/85EC2BC6-077D-FB4F-96C6-39079EF83D3A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/9446F102-4CB1-B14C-ABEF-700E92CDF21E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/A8E28547-E419-1843-8D41-8B6B29C17301.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/ADF289E6-2153-374E-B9B8-CD2B71142DC1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/B95E1A7D-DBC4-8F47-B518-CC144D29703A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/BA420832-EC9F-6343-961B-05D6E9205A87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/BB527291-8FFB-9948-8DF0-1F70AA886028.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/CAAE3C21-7684-E848-B011-989A5E2E86A5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/D8DD4DB2-A484-304C-8367-5A16522AC1AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/DD3C7CBE-487B-2941-AB63-9849AD257A84.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/DD622E04-480C-7E4C-9076-8D43115364F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/E4B94337-7643-3C4D-85C1-DDBBECF35110.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/EFB8EB38-B2CF-224C-A2DD-F979B3684B25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/0366ED12-FA6F-F145-8EC9-6E48CD7332D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/0B317DEA-2E4A-1648-9D82-F0E075CA785C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/0B47DFAD-EBE2-964D-B0F8-39B1F4C02949.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/105B533B-33ED-B84B-A539-4DC209AF3273.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/12EA10AE-D7DD-4A42-ADAE-BDF48FFB7A2E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/1B647544-C053-1043-88D5-1D0B8C27AFCD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/25A9EC19-422A-6444-9E40-22D83ABD0268.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/3675EFF2-29BB-874B-923B-C9E786795F19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/37F286BE-8344-F74E-AB3A-5277BAF5623B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/3C510581-79C0-9E49-8B6E-9E7FD41CF587.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/42C05A2D-47D2-FC45-98D4-1CE769FB5448.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/4D069477-35B2-F148-AEF2-7CAACD0F01DE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/4ED025B5-E185-5A49-9EC2-9CF378F1699A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/5642EFFF-B08F-B046-8B08-BBB294A04A61.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/5959772A-2FDC-5849-B7BB-367E1BE7AF1E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/5E972A9C-0A68-8746-BE01-A5FCFEAE4182.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/683E9AAF-9698-DE49-91A6-33880DCF6352.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/6AF4BEDA-9D17-8742-967F-F570C980C29B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/77274CFE-AC8E-8B46-A5EB-850106CFB101.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/7E7DAD2E-CA94-9F4E-A41E-2BDA8CFC400B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/86B9B70F-9571-3348-AA01-AF61E4CAEBE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/8861AFA3-32BE-B845-AF35-8048F893A749.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/8ABCF6F5-4B95-AD44-A55C-ED1DA3D4B2B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/9475174F-7375-924B-A34A-927768BEBCDE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/AF9A1C38-E432-3A48-9665-030EDCFE8F3D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/B103E81A-2BE6-CE47-93D1-B62FC2549486.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/B1366026-067B-864E-90C3-4D905CE01AF0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/BDC5EB10-C69C-BA4C-A8FF-BF44D1F3C9D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/C846D57C-422E-E247-B913-C93E2913DE02.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/E6BFEB61-2BEE-724B-9EC1-5CFE8583B609.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/E872D986-BE9F-2244-B3C1-C47FF9A61A2E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/ED12443F-D54A-2B4D-A3D4-9BFBF681C302.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/F5A23644-42DE-8C4E-94F4-43E4453C60C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/FB890F7B-2621-3A48-92BF-1DB70E181C56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/FDACC470-D4B1-CE43-A8AC-2C02292FAFEB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/260000/FF1C05A6-B4D3-8143-9588-6D0BD5004C2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/0924E04D-860A-DF46-94EF-8F1DDE576D01.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/68D6D8DD-5994-5A40-8E78-1EA30A5B7DC6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/AC069DB1-CB0C-4C4F-8ABB-FB08B3A0927C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/AECB393E-89F8-A04D-9713-BEB9A3A9D4DC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/F2C1E43E-DCF9-A14F-8F8F-A92572DC0159.root',
] )
