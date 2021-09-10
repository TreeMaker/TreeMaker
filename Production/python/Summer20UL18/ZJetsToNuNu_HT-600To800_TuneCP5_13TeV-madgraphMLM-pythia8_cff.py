import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/16CCACF4-39DD-ED40-9A1E-FD2183FF1E01.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/195B0952-14AA-9F4B-BD06-29B8A21C099C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/3763AF14-5E17-5941-BF40-01810AAE791C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/563591DD-A602-7542-8BE5-10748326393E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/6E2AA035-BDD9-FC48-A2D7-505C920D0DF2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/B38904DE-ECD2-DA45-9D4D-764F8E8ACE3E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/B560722C-0A67-5B46-A7ED-6A13EA86C3FB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/CD852FEA-CFB8-404A-9C54-A637636A5626.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/046D6407-859F-EF47-A408-6870A789C8A8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/6C03DF00-CCD4-9C4A-B658-DD43480DA60D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/77E799CD-0FAD-6044-AFEB-0305E000102D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/8E1C72E1-6D36-164A-A300-D2AFDD0073C6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/9E31AEBD-8676-B245-8C1E-5B1C88A6123D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/A5C2BCD0-AEBC-9E48-AE0B-C3FC766501F7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/D2E823B5-926C-4641-8B35-E722890271E5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/08A5AD7E-DEB2-A947-8F77-BFFB0546CACD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/168F77F4-5D84-4B4B-B7E3-84042AA42292.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/2EC88077-EE8E-B249-AB12-B4A75CF524D1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/2F9C3EDF-8987-A745-9CBA-345E248DB4B3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/41034BA7-7F7C-6E48-A3CF-09BE6AFA0909.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/505DBD72-EF0A-6D48-A469-3BCC9341DE32.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/779F2F8D-5B09-A247-A4E4-D260ED7C2343.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/89E20DCA-D78B-8D44-BDA1-28FC825D0E08.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/9041BD16-13CC-8747-A92C-8D948F6B668C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/90B900D0-769B-254B-93B4-0F9C7B80D191.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/98C952DF-A675-0E40-B4C1-D43321A9B9FB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/9B5FC6A5-A0DB-2D44-958A-06137FE7E1FD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/A14D244E-FA44-1544-A9E5-60CB506526B4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/A5E8DACC-B718-7344-8CE1-1314752BFAD0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/AA741529-F28B-924C-A5D4-BE5602BB0E17.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/BCA7A403-A8B6-ED45-8CD5-B5C428FD1E70.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/BF53EB52-3562-104B-9161-118D52071142.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/D248CC92-F54C-6C4D-8301-ADF7A12F3778.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/D24DEC9F-F67B-CD4D-B7B1-419F0FE4B0EB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/D990ACE1-B8D6-8A41-9061-DEF05A64C0E4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/DEB3C17C-2B06-5847-924C-4E42D53A46C2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/E7D1ABCD-ECDD-7540-A62D-C73DDA5D65E4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/FD84961C-72D3-6E42-BB3F-3C9D5100046B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/098232C7-2ABE-1747-8911-36E17E03DEA2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/16BB058E-3F9C-794D-AF73-0A564C357D00.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/2DA798E2-BF14-E346-9493-03F79995216F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/346CF536-8839-1D4B-9AF3-600C5D8EA83A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/37662EB5-6634-3F4C-A313-513E4F1B2DAC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/4B38198E-6FA6-2D4A-8541-29A20972C004.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/68430C11-EEFE-234C-9336-2A01F3BF8CCA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/81142124-EE44-4448-A336-C5A611AECAC0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/89AC040C-1726-6D46-8B4B-B51CFFB21B9D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/8EB1AF4E-1F1B-CD4A-88A2-9F7896DD5A0A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/B7082ECB-E269-3C49-809C-98E2641FA888.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/CE9B4487-891C-DB40-AB22-F3EA304AA170.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/260000/EC968E0C-F22B-1D48-8502-6C66A2ADA4D7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/034CD1C7-4BB3-014C-B6A3-6DF0683302EE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/08890188-5A64-8748-B499-C2DB58641FD7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/08BA23BE-00F4-FF49-8F39-197AC25D6B9B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/0D059B3B-B1A6-DD41-B321-943C4991E85E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/0EBE2C4A-465D-7A48-9118-7D7904F6176A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/1637CCDA-F581-9246-93FC-B0177E8C99AE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/18737F55-409D-3647-899D-D0515A8FBA97.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/20BE238E-22E2-6141-858C-170EDE76FB1C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/2197B0A6-ED1B-734D-9A3F-47C5C9E893C0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/244067DD-079C-B843-888D-EC1C18008A3E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/265FF393-2F7B-0440-AE87-E7E640E7173F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/267A3116-5FC2-AE4F-B5FD-311EF69C098D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/2E4F3F70-6C17-4246-B108-218E7D2AD723.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/2EA98BA3-73CB-3743-A0FA-F28F4F3115F7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/34F00333-07B1-7144-B468-7FD5E9A4ABBB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/359D5F8D-F0D3-5A41-84E8-5845E8C66A37.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/371AAA7C-5FC9-A143-BDD9-EA63AE497C89.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/3BA3776A-A8D6-8B4D-B927-3C660931057A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/411C1E60-52D6-A144-A461-781AA4FA519C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/42093873-CD62-9C41-BE0B-5434C1A85252.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/4373C194-1E60-7B4E-8255-9DBF402A3FCA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/47113758-7C60-A143-B51D-CE7B62EA99BB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/47409B3E-857E-BA4F-9675-EBCDD42E9DAA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/48799793-7FFA-DC46-94AB-6996F7631C09.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/4D2BFC47-5D7F-6342-A1F2-792679D0721F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/4DA25291-2338-394B-9B08-F54F9D579346.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/53D6D62B-1F05-F449-A0D4-21F1EEC0AD2B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/54513E0B-7E4B-C940-88E5-F0B496609A17.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/55AB963F-E9DA-CF49-A87F-A55716C40F34.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/59CCD9AA-F82B-6941-A9A1-C1F32DC03EB9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/6083ABEF-37A7-AC4F-8BF8-1670769919C8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/63C38821-4D91-9346-8083-84433D83DCE6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/63D8BE95-DDD0-B548-AE9D-88E9F5D56E91.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/67269D7C-2674-154A-92AF-C1BE23130CBA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/6863DD6A-CE2D-9546-96DB-D6097E1C4DE6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/6E57D1A6-1912-8241-A901-08FDDE320B94.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/722E8270-443C-4A40-BE92-5C1E5D8B305A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/770A570A-F1A2-C041-A975-945F4F49F22B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/784DBF27-4197-5E4F-91AB-6D7551CE483D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/7C22C88D-BBBE-0A44-BBBA-66C7D9999162.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/80E077AF-0D2A-ED48-AE45-053E0C8B4A4F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/830A3F60-E327-E941-B2EF-413C18799B19.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/83F84AFD-6F74-D544-BDF4-2077CA2CBE74.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/88E8E5F0-5072-114D-A5F4-D1EC173D40E6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/8FE1B8E6-C6E0-B647-BE3D-6F9A0B9538F1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/9615AD2C-C892-5346-BF2C-AEDCE8A1F825.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/98435C38-F90A-5A44-9009-E11A0FFCF3F1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/9B40A50B-93C4-E944-8135-915371B67959.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/9C6B0E16-8789-6A40-B2B1-BBA12394C52A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/A4D738AA-CBD2-1D48-900A-338567CE1AEF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/A77BE00B-BF9A-1E4A-B1D8-721CAD594106.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/AB359BC8-2FC6-CD4F-8AC0-AA3FF039A106.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/AB8DE1AD-B668-9846-A4A0-74F7FF467ED0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/ACF31352-D43A-C247-9BDF-56F053BA4C4E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/ADB9EC39-5984-8340-80A0-EDEBFA8CCB87.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/AE0F54DD-BC7B-9444-AE57-EED65085DCFB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/B0971177-CCF7-4047-A4FC-3A0249EEAA4F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/B33822F4-D73B-7B4C-83DF-634868559AB6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/B685C424-8A9D-2E49-B6D9-5DE97DFEFF92.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/B8266E22-8AE8-1648-A7E4-586988150129.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/BA4A0EB7-CB10-0D4D-AA52-5AE8212F2B45.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/BC42F719-A007-0F4F-905E-6D4E915FBE26.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/C801F5AC-C28E-8340-AAF8-D63CE825F1A7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/D0FB4650-0558-3D4E-90C0-FBD112346561.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/D8B27936-C5DE-7345-9453-730C9C48B012.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/DD97E805-6446-1A4A-9261-F3837D9B1E48.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/E777E181-42F6-DE43-88C9-5F8BD0F0F0CA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/EA0F306F-985C-224D-B521-B9C2CC46463C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/EE360076-50FA-C349-B185-1E87D0732027.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/F599BF70-82A2-AE41-9308-3886092068A3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/F79ADC6E-1285-F349-9472-CE32A0736A0C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/F7FDA4E7-7F9C-2B40-85F7-E11167F7771A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/F9033D8E-34FD-E04B-9158-F4F27BDE796B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/F9D9CE4A-5946-6943-86F3-6E0B42C3E245.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/FEAAC0A6-9EC5-6940-99E1-1EA37EF95FFF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/09E710EA-AB3D-DB45-A23B-CC601824CFB3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/27B3E9FE-14F8-FB41-8790-85A1C4302D1D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/4FBC858A-D901-044C-A088-0A8494AAEA06.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/6B6DB373-171B-1548-8AEE-6B991F6305C0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/AB95ED71-1D59-BC44-8AD9-9693813C8353.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/B224DE47-9A9E-AF4A-B634-113027AF6D00.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/D4DDF1F7-E8DC-1A4F-8A32-95E62BAC1385.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/51ADFAEE-4FCC-5E4F-BE04-701E02338715.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/9F43D8DF-3E88-6146-95B8-056B21B730A6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/B7CC253E-4BAF-474D-94D7-AF4348119A21.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/BE042EB2-187E-0F48-B0CB-140927CDEC44.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/E492C406-0707-0440-97C2-5A1FC3FE19AA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/F2BEA4C1-5097-124D-8A7E-4C74FCDB2985.root',
] )
