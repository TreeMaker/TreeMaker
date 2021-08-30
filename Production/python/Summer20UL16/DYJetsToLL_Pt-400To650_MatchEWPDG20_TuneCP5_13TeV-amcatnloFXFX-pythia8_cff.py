import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/0783035E-849A-2047-BD92-8A83EF00FBCB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/18782ADD-BC9A-804F-BE30-21E0C91D7F14.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/1F058628-4A96-694B-9F66-FE97D88F5AC2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/1FBAA5E8-6EDC-DC42-85AF-C4CD5ED125AB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/23507D85-CAD2-FD4E-96C0-9E95C5DF8328.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/29B61AC2-D68B-8F4D-99C7-6E6E57DB314D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/2B58FCCB-CFBC-DC4D-AFF0-AA9F3413C328.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/309BE014-9F79-9246-9BED-58ACE5151E7F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/3DE47746-0240-754A-8A47-2599E4B8EB7B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/3EA1CA97-E972-9844-9211-AF09FB421B57.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/3FC88CCF-08BC-C241-ACFC-B1982D4C4528.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/433D258A-3ABE-3043-9958-11AFEA88CA1A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/47293617-21A6-CD46-8B3D-82217E82FB71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/5792D0F3-C48E-374E-9F1D-B15A96622741.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/597ED797-0F0B-284A-9A15-B8442AF56157.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/5BAA8E9B-61E3-AB40-8125-E0FA0DA48E11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/6B5E6C49-D040-2942-81A2-BEF284A20FF0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/7A2D0A2A-47F9-4B42-B1AB-168DA545D7A4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/7ADF9732-3D4F-DD44-8DFB-8DE1AA17F021.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/85A659A5-467F-584D-9470-6EB22F545EBA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/8F0D5ADF-0344-154F-AAC8-988699F5264E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/9696D26C-D3D9-814D-9C84-1BBB203F635E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/9B0BB988-F792-0645-9E63-3B123135FD1F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/B3C056E0-DF18-A544-B90E-8AE985C5071F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/B6EE140B-7043-2F40-8A16-EE895D2D205D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/B7241F44-C9CB-564C-9AC6-5FF2624695A6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/BAF242CE-A9EA-484B-AC14-233C61A4515E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/BCE8C793-D112-CF4E-86C7-961B4C185FEF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/C1236964-A9A7-7945-B779-56B314018DD4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/D7A8B172-14E3-7743-B0D1-2F671B478884.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/DB30F006-2970-FA45-BC95-01810A1983BC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/DB7E9FCB-3189-434D-BAF3-9F17B55E7F50.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/DEF7AD76-B90E-3548-94ED-0077A18F907F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/E912D5C6-DDE9-3043-93F9-C7390541E60E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/F00DF61C-435C-D843-AB85-6ED916DF27C3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/F0A4B6A3-C224-584E-A286-BBB143F7A534.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/F29EC3FD-2A35-D349-B08F-96B3E47419DB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/F9A8DC8E-E22E-944B-B23D-FD5B840D827B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/0A35CBDD-FB3E-A841-9092-E94B818F3A11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/1481549B-B959-4C4F-AB48-D4ED6711C250.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/1A33DBDB-7657-5446-9575-250811DDEE1B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/1F9D0E39-BA7C-5342-8678-F56A20132954.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/28BB760C-F144-5B4F-9143-C67B69990475.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/32A3651F-0F67-5140-A536-44F4F0C4A364.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/37B5DAFD-C6EB-5C4D-85C6-FDCCF699C681.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/38EC0FDB-EB68-1E40-BA10-45EA37CCA1F8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/3C44A3C7-A210-3741-BB3E-307DF98D6492.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/3EEB7AFC-C511-BA42-A705-3146193E285B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/48ADA59C-4AF6-A64C-97F4-A3653A7111CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/4F22481A-88ED-3944-9562-25296E69BF0A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/560E84AF-24D1-BF4D-B133-BEDEBEDAF0E3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/58505837-334B-7B47-AFCB-46F3509F0D56.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/624A456E-9610-E34C-B479-6F7A527C140F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/72F62FF7-0BD5-0743-94F4-688CF6B350B1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/8F9BD2C6-2D47-214A-808B-3D30F6B7E0DF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/8FFA3552-9FE7-554A-BF06-041BE7D9D17A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/9812D2F5-ED1F-4340-ACD9-7AB8E42F4736.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/9A5243ED-5055-2C43-8609-9E62DCEDAB6A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A0A2152E-56E0-C94F-BF31-A5837C29A0E9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A24D6C08-1193-F34F-ACA4-5527F081CE6C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A43C3212-40D2-5947-BB2A-227D4A11FEC2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A8100FEF-A9D7-DD4F-B0DB-3FD8BF0F3493.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/AC365AA5-117F-CD4A-ADD8-663302F0DA97.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/AF4FD5B1-A93E-334F-916D-717720165D9C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/B09BFCF4-0310-4B4E-AED3-9356BE946975.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/B15D5D70-90B7-9146-B650-1686B9B7994D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/B224F21A-8826-C84B-A75D-DC9DD229553B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/B747F8D7-46A7-6343-A1E6-1DE3504F86B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/C51E8661-5DAF-6541-A7C2-37DAD74BE6A3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/D0A338E2-2BA8-304D-91CD-2AE8E4E969C5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/D2BF0488-EEDD-FD42-9DA1-B9088D850204.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/D32BAF25-C0B6-3147-96EC-5966637898BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/D813C637-9D75-364E-8C26-E25F54908297.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/E01B655F-5C60-2240-9EAC-52D926CA209F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/E1FCB914-E50E-154E-9EE5-C02A1BFE2C95.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/EF8C8111-E5E2-BA4C-9129-704A1D2D6284.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/EFFCE104-D59A-6F4E-942B-1B8139D12C18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/F4AD346F-E1F8-C144-BDB5-7D5BAFD6B324.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/F7624220-169C-8049-B327-065FE8DA1F4E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/F958640C-7249-6440-95C9-D4525F8097E2.root',
] )