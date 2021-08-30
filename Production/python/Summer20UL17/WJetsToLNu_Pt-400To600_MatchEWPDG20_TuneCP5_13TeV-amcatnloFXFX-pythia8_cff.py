import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/016AAA70-2C59-B443-BFD1-488F4B8D2E20.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/02CC8EC3-73B4-654A-A0F3-6747ACFD38DB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/05E03DEB-35FA-0646-9FC0-D9CC55D06533.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/09156CA6-630B-0A42-9E60-79A6B2D497BA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/097C0FF1-6719-B949-885D-CB354C9A849C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/09BDF28B-3638-1C42-B77F-AEAE528C6348.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/0BA859E1-0E60-D449-B1FB-CD5F96919C1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/0CA68EB7-5F06-BE41-AE99-14DF1724B04B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/0D2CC978-EB8D-A640-B656-3C8492C43B9D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/0EFB555A-DD00-B74B-934F-5E9C7A574DA6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/16E5B369-A94E-6742-8D17-0F34245E0B12.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/19A01E37-7611-4C45-B85E-CB21CFC93C88.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/1A519D6E-86E1-FA4C-80EB-700D41104E0C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/1AB0244B-40EA-A140-8C64-130BD387493E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/1AB4DB61-764D-2B43-9D26-A81438F50289.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/1C092D82-758D-9D4C-AA06-46815E732526.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/24442B8F-D2F5-5544-A2F5-ADA4EAFC28E8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/246A82DF-CFAB-7848-BE4C-220A5454DA60.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/263E7F02-6354-DF44-B04C-627A9983B641.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/285598D4-6FFC-764E-8DD5-FF411D1C246C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/29FE2444-BFCD-7D4E-8081-D980832A3E0B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2A41C404-03EE-7542-ACCD-5BC8CFB434B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2AAA33AC-12C0-C949-8EBB-32BE1B430D1C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2BC0266A-A3E1-4242-AE7C-754E4D996F5A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2BD3E047-50E7-864A-8D51-5855BE1A268E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2D93BE7B-C00F-6C42-8B6F-EE0FE946C6A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2DAA1D58-B121-6544-B542-AE9BE88101A6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2DAEB700-5B55-EA4E-A6CC-C13D42F7FBAE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2F62BE1A-C0A2-5A49-BF3B-7EA039923AC3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/321E1B91-7E48-3844-A1A2-5E8591AF73C8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/32FFE28F-870A-E348-A04D-EFCBFD75C323.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/3374E2E7-590E-8A4E-80F5-7A3503B76BCB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/33E1C163-1A6E-094E-BD02-D511DD45A7E0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/3411AFDC-3233-D14B-AA19-BC8E6EBF3409.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/34AC8430-560A-3A44-8F0F-19C41EED73BA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/36FB540D-9BC8-CC41-9EFD-303254858222.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/38021162-1994-604B-889F-F31A86249B82.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/39034AFB-7783-634E-86A4-B5224BCB189D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/39A8F4C0-A2C4-5C46-98DB-10A32A1162FA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/3CD57E71-5AE6-C644-97EC-439C5B24AE36.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/3E5C51FF-E435-4244-B3CE-C59AB8EB0602.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/41749A0E-60CF-AD48-AD51-4B5A2A7EFCF2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/41EED67A-A810-5342-8EE7-279CC56CF8A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/41FE7CFE-0317-C443-84B6-AF8B3BF7CA14.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/46EDC9B9-E21D-354E-A8F1-F8DE44C51F12.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/4700468C-CF89-364A-AE1B-5F1E188F698D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/4A95CA29-2310-CA43-8A9A-BA152286C486.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/4C7571D6-E86F-354A-9932-5ADD8BA715C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/4D946E9B-7BAB-D64F-8723-30435693DC7A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5011F859-2D38-3D4E-8875-BF42EBDC1408.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5086485C-753D-2D40-93EF-739929DBA92B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/51FFB59B-D4B7-4C4D-90EB-3689B0171BFD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5257F492-A437-694B-BCCB-406CBB143888.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/52CC145E-7A25-4A4F-92AE-39F92E4A83F1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5330EE78-7EFD-9D4C-AE40-A90055FF5044.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/54707D1C-5A74-5747-93E9-0771168D31DD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/551F1B50-114E-0544-83AD-ABC927572B1E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/554CC5D7-571E-954F-9CB4-7780EC2CC354.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/555F0972-89F2-6043-AA51-FB209371323D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/58271A86-21F4-624C-97A0-34E6D27EE5D7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/58782ED1-6639-294B-8DCF-BD9AF0C078A5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/589C0D30-671C-5240-8C57-1547F554B44B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5AF52E55-1BD2-D542-8DB5-DB0177429334.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5B77A9F5-B795-3049-B044-5415A6C14C61.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5B91BE52-62B2-494C-B636-C0E0828AD47C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5C1D98A3-D51E-8B41-87A0-9048EC43382A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5C3B5C70-5ACB-5B47-989A-9F96773630CF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5D919E6E-CE97-8B43-8B5C-793FC78F5055.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6260C67F-1C71-C647-84C9-DDB368A4A707.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/629C7BF1-6399-C24B-9D76-DC8B3FF02471.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/64A9242E-1109-184E-898F-B6189228ACAA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/65C48A4E-8715-C84B-A64C-67BB327CD867.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/66179518-C4A2-0A40-96E7-21DDD6368FBA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/66517C42-F519-7F47-8EB1-A05D632B3187.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/69CE3525-C086-FB42-8FBE-66AD3666DD4F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/69D54E3A-434A-4E44-84F6-A6B6CFEBF2DE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6BC9D0E8-F5BE-FA49-B2B0-6D3F0FA84CD2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6C733CE6-0A87-864F-95CE-7527F5F3A350.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6CE20C34-2732-2D43-9BD4-A95388636D81.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6D356BCE-D765-4C40-9EFA-3C903C450A5C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6FD50E46-51DA-7246-8C29-75E12E0C57C7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/730EB95B-9F48-4240-8C26-D41B03DEFEFB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/738F8B2F-5893-734C-8079-CC5EDB636E90.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/73CC254F-951B-9043-8A68-157F10D6C1A5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/76198A81-22D0-F940-9243-718C25071015.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/77CEA7C0-4001-7043-AE39-57129588FD86.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/78362CD2-BFFD-CA45-AF43-1950A3BF356B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/795F8EAA-4729-6447-A19F-346C185AEC67.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/7A7FC5DD-AD55-404B-8971-D6AB48776ACB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/808E8C64-0A15-8847-A954-DC0465B2D305.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/84E5825F-BCCC-6A4E-9E7B-61AB9CBDAF94.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/879A59CC-2B91-0C4B-91D3-62C4028AAAF5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/87B7D31D-E03A-F34A-AD26-7A81CA49DC43.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/87C82306-20E2-C449-A240-D49C2F03504D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/89091189-9DD7-A647-B1E7-9AFE0758B61D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/8AE5976C-6675-A243-BA5C-65F02BCBCC99.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/8C806738-32C5-8849-B132-2ABFC7DCEAAF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/8DAADB51-A32C-B84F-B709-73BC2ECFBE3E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/8E754CE3-301A-E843-B52A-F02D4F72C1D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/90297A70-01AE-4640-9D47-E304CB6F0F3F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/909B9544-55DF-D347-A7B1-78C055563990.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/910F6666-F061-2243-AA04-A83B21A6AFFA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/916D7D15-459C-B34A-83A6-E6971C1BAE35.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/925E211F-673B-8147-B888-090309C8E3D5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/936D573B-A0F2-0747-9ACB-CD2B2EAEF286.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/93A92128-A97F-4043-9598-0E25823F6E96.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/93D1CDC0-6D32-ED43-A8A2-398AE878582C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9471E07D-C96D-FD40-A0FB-CA4B9F1894B7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/99B07537-AB00-EB4F-9E86-209A9ED855C3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9AA18C0B-D5AD-D44F-8B65-5DFF82870E52.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9AA7B0BB-A76F-9145-B1DD-90D02909F5A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9B54EC7F-2BA1-AB44-A818-6A394F01D294.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9C548FF5-9020-AA45-839B-2BC87D25C6E9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9D150EA1-4489-D341-8CAE-4229C011C443.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9D19AF73-16E0-9848-B0EC-D4C61EE40544.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9D8AE490-89A0-BA42-B844-E676687E7A13.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/9E5F79AF-D839-E246-B6EE-FF23F931B213.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A252AC5D-6CDE-E44B-A239-8DDD75395305.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A2AF8E6D-F617-934E-A3CA-A2713BE22195.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A3D12950-3D50-5C41-A1FD-2CB9BD4F21E9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A4C79255-FAB3-A140-A1AA-C81F244E7DCE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A65D9E10-A9E3-5F48-A0A9-0F74F842E2BD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A6E40594-8572-BC42-A88F-E3F841138B5E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A94F694C-6D81-B64E-A92E-0F11F5C6BD4C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/AA251674-298D-6D42-85C6-054859BEFC5B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/AAB6F3BA-5FC5-D049-A038-369FF35D5DC4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/AFE7E98F-9564-6549-87E0-02D74060629E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B0EAE58F-966F-9946-9343-8001E7B4F140.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B1C49054-9462-AD43-9744-34EAD7F7B909.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B3174F4B-1212-8E49-A129-B68DC11F2024.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B357D586-78BE-E046-8117-D179A23CBB53.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B758F00F-C90E-A649-BB5D-88CDFA229394.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B88044D4-2260-C843-8879-1724469458D0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B9056127-A26A-E646-B491-1A27EE1F2BCC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BB8DE1B4-3D8C-4148-9663-E8649CBD373D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BCD10513-D804-F345-9E5A-1C9A0A7C5D5F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BEFFE452-EE04-B549-A8EC-053BFE200FA5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BF7B6D9B-2DED-7A47-848D-F31CC49DCA38.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BFF9B7E0-8047-7B43-B6F7-ADB805978250.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C0425973-B5C7-7849-A158-DE8F82AF35A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C04E24CB-78F3-9942-827D-1F7E0F3006A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C1A27500-2AE5-6A44-BCF7-7D80B7C6E45A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C2DE0169-A0BE-304C-958A-81946118E89B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C38AEF87-5209-CC44-B01C-60B2CB64EA0F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C4251727-CD79-DD46-8183-4AB6A93A8E29.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C4DBAFE3-B08B-8E49-88CC-649DBD2D29F6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C677F0F4-90E7-3E42-9B9A-2D028E29E402.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C8663233-D5F8-CF47-8945-1CC9EE117AB6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C8CC4E66-0F3D-C246-9432-921C9E6CA27B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/CC03D514-CA85-5042-B461-CFBD9EE52766.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/CCF91F83-26AE-EB43-A1D6-72054C9F5FCC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/CE462596-096D-5C49-9973-5B1CA978BB69.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D0D055BF-0FBB-FB49-9D18-7799AB267CEE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D19A8F69-DE58-5147-9096-042FD8CE0E17.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D37E1F79-D047-584B-AFD9-5525F733CB10.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D3FBF7E1-8B67-674A-A31E-CC3B564C18AB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D5EEE855-D4E5-5342-AFCB-28F8EF6A178B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D66E0F2C-E896-9946-B2EF-A1F806550D7F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DD79A95B-0DEE-2D43-BFD2-654B3F08D035.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DE85A9DA-6D4A-0E48-B038-65A1738606A6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DEBC4863-C81F-9E46-AC73-B95E78835DF6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DEFA4180-C19E-AF49-8F51-794B1D27104C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DEFBA015-8515-E147-96D8-9BD7F0C6C812.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DF728061-62A1-6440-A49D-77CD576C2AFA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DF82F2F9-5E3F-014A-98A1-384D064BD286.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/E006A4F2-A7DF-7D44-9F8D-BE1394C910AA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/E2124E7D-B64C-0640-A304-1006A7E41227.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/E5ACEE5F-0EEF-0A4F-ADC0-C39EC4B36C9F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/EB8C62E1-2E10-AE43-88CF-B561E28C84E8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/EFA3CAF3-B2EA-7E4A-A05C-C82E43ED586F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F0ECA7DF-6B80-9B4A-B4C3-36318BB30E1D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F3E86495-6FDD-9D4C-9C31-53190856EBF4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F4E296E3-427B-F44B-95B4-999BC6726886.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F646E5C2-AC6B-964A-A7E9-79526130B593.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F65C8BBF-8A75-5F42-A4B7-9FE801B48B6B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F6B9700A-F777-0946-9D0E-1A956AFFBF54.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F6F721A2-FA28-2142-9760-C97184ADE697.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/FA7901B0-3428-B047-A262-5B64FA86A516.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/FB65DF9F-19A4-4348-9F57-98E9FFF11198.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/FF8F0673-F877-E741-BFD9-7DD676745F91.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WJetsToLNu_Pt-400To600_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/FFE0D500-41F3-DC43-BCEA-95F22FC89635.root',
] )