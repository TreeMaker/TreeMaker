import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/34091D07-490A-4245-9568-D98F6C463160.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/4C11D735-158F-784C-813A-5C780F71D310.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/55548E5A-7D82-9A4D-B7A7-A487BD898DAB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/60C29DCA-341D-114B-ACEA-62B862E43C6B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6CC1CF25-51A2-EB4A-8789-89400CCBE0CA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/FCDC1382-4D91-C843-9256-1FC2BEF576CB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/0B640BBA-7C70-2C4D-99A7-0ABD625D6B67.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/0CA3F4EA-DEA4-864E-B2EF-8E5BC0092B82.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/19D0874B-F509-8545-9DE1-764F8E26EED2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/1E8E2C55-6E0C-5F4D-8B31-DB2A8FB065EB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/2597944F-23EF-A546-B345-09DEFD9ED7C3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/30FEF1D4-617E-1049-BBD9-F3F2FE4F6559.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/37FCD60B-9415-9F42-997C-8D180926F50A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/39C9B774-AB2B-C649-96B6-DAC887C2A046.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/39F569F9-E55C-3542-983A-3EEF94882D67.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/439A9401-8C90-3048-8CA7-80FF60A60969.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/4CDE6DDD-1359-5F48-A842-18E455CA93D8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/5616DD70-569B-5649-A73A-C976EEE72DA2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/5642DAD0-7517-0541-8CAB-B06964167DE8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/56DB01B1-6FDC-3845-8F70-BF7ADF7F23B1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/6036BF6B-3F58-CA43-805B-9610CA189EE9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/6194DC5D-2986-0C40-AA4F-127618B5BB43.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/6A4293A9-9948-9D46-87AC-E05E424EF455.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/7527B594-F47C-E642-B27D-E7F42FBE019F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/77FF9DE0-2856-5648-A0BC-CD2604D6D80B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/8155C5E0-2C75-D34C-9D17-B3B63A0E1491.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/835D5BA2-DD88-1346-9C40-C2E9EFE3BF2B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/8E82EE0C-18A2-4E41-8846-712DCDD7BC23.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/8FF3301C-7A55-2443-A23D-0D32560EC914.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/9E5E3AFC-42DB-F64F-B250-CC658471E973.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/9EFDEFC3-A33B-C34E-9DBF-F77F3B3EE910.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/A28C916C-0F3B-AD4B-B9F2-92A5A3F664FD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/A2A3E849-B7B7-AA47-8A34-8002DB6B5D70.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/A92877C8-AF8B-3645-8F9A-D028C640DD9A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/ADC2E653-4BB7-B449-B546-C607BEFD77A0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/B7F4D6BD-591A-8C4F-B2D3-30B7D6EECCF9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/B8E7BCB3-5448-2E49-A8D1-846EFCDD6F63.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/BB2B176F-BEB4-AA46-99CB-EB2A429BD7E5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/C6A34958-92C2-9243-970C-727C7D0583F8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/C8ADA76C-EB42-6947-8F2D-FB15F4B34B68.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/CC6220D2-3E5D-CF48-A4B2-96AEA08CF4DF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/D39ACFCF-9C82-1440-90F4-DB03DCC15C28.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/D5D2FC75-36F0-224E-9CAC-9C5456AEE05C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/D5D6341E-2ABB-1E48-B54B-F7438E9850D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/D9C5F7CF-C2B1-534A-B081-4D810E391D4E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/DAEC42A4-1C19-724D-8E64-CE15FEB6A536.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/DBC7E53E-EB2E-4B4D-ACCE-C1C6940B9ABC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/E6D53397-40D1-244F-9A3C-BAC7CFE2C465.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/ED67BBD2-7E9F-724E-9748-458BA7832554.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/F0DA8B2C-A20E-FE42-AAF3-1721D9B37F1C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/F881E630-4BCA-0545-993A-C13B0970D074.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/FAEAA9C7-233A-904E-9F45-10A99E5D2D8F.root',
] )
