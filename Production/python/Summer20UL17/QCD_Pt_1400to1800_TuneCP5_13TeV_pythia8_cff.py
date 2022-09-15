import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/0219F5D7-E01E-3045-9F88-BD63D237A86E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/BD906831-B3D1-004B-A188-E49C84ECFDF2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/C2B3DF93-A60F-344F-B974-AB71EDEC869A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/ECDA3546-2008-FE49-8FCA-13A5E7490069.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/EA2087ED-453E-E447-9A0C-3D887B8BC6DE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/012F35B0-EDBB-9B44-BCEE-03ADF48A76C8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/016E1426-79C7-4E45-8794-B39D108E23F3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/020A4E01-DCD2-5840-AB1B-B3D939D9149E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/05837E2E-F666-5F4D-BD01-15D5F2F011C4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0CE9C42A-2B18-6448-BFC5-1BEFDD5542B2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0FDFF447-B5E7-C74F-AACE-F8A925C74894.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/17525DD2-359B-4D46-A100-BF8E4D662FA0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1F92AAC0-7B1E-CA43-94F8-738C074B0D1A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2003297E-EE70-0E48-BFAE-50A62B129223.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2442C51F-FC4C-9F4A-A99B-9DF68DA7227F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/24AB2218-8C08-3A40-B638-7B824751D99F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2817B57C-4B7C-684B-9F0C-8F13B63A8A62.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2A7AE876-E665-7A4C-B62F-AC278853FC3A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2D6B35CA-D5C9-2A43-AACD-94036BEE3D9B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2D769858-E144-E549-B83A-DA2BA0B88DEE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2F5A4DE5-5000-7041-B447-3FEF3B84DAB7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2FE5C216-8C21-4944-852E-327EBCE41C99.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3273CB15-5DBB-4C4F-97BF-A21011B939E2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3353EFC7-CF4F-F045-9AA0-8B0F56150A70.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/33EEC331-5BB1-E240-BB8B-1A98E0889929.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3A520538-B4AA-4E48-9B5C-EE1425657234.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3E53F949-0F76-8740-B65A-78DBFEE63D90.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/40A895B8-FF41-D84E-B17B-EC3D6579AA90.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/411B1E66-E22B-3744-B2CA-CA67910DCC0E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/43890173-3A99-234F-AA18-4CC3654D5B45.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/4656CEAE-019A-714B-BDF3-3932A840A558.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/4A34F4AA-8CD2-A54B-925B-D2D9E550CEE8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/4E8FE8EE-BABF-A344-BE98-92A844B5567D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/51FB7A6B-D0D3-204E-B38D-E3D5F06779F6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/52D6C4FF-4AAF-E340-8B53-3234D8BC4797.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/533746F3-EF13-4946-8165-3F1F20246814.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/5479E2FE-B0C8-BD42-B45A-2207AB81FAA9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/55547311-A9A4-5847-A7FB-D51A3253179C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/600F96E8-9807-A646-A9D6-6308BD33BB44.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/65324E59-1B85-3E4A-AE0E-27D10C7CF3E9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/694F174F-46D5-8E41-BF94-AB376E161044.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/73D51189-89CF-2442-8E7C-DE8C584EE2B9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/78758BA0-D7DA-2047-B2BA-C9FB2A6117EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/7CAA9817-FED7-3140-B73A-A0B8CD8C11F7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/81490961-5F40-FD4C-B0A3-5FA5EF8739A5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/829C1348-5D88-3D4A-869A-B08F1A4C0052.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/853FD71F-8A17-2944-8D67-49F05207C565.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/886A3CE7-D1CC-C249-8882-97401D82A5EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/88896447-BE9F-A64A-A297-A0987ECE64DB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/8B90D61E-3174-C94C-AC82-A5C1E6DC1D4B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/92099572-E26A-F841-B03D-713E59F6180F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/94A45141-8FA8-DC41-882C-DD06BFF99E76.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A048218B-6B44-A44E-AFCB-4C5B393D12E0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A0C5175A-03E4-264E-83C3-28ACFD1E0951.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A87E4E22-6D1E-BE45-B78F-CA7901283C7F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/ACDA5A53-727C-CC4E-8016-88FFCD15CAAF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/AD908B00-5D47-E84A-92CE-DF67D4A189D9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B36995B3-4457-F749-A6CC-BE93E8E720EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B4E3DDE6-981B-9D45-87FB-D1DA24E7E0B4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B81D5AAC-4B0B-6242-8B38-931015A9F75D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B882C2A9-4651-E048-9B6E-8B47A8E656C1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BA1CF818-C4FC-2A4E-9C26-012BE384D22B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BB0FA888-C231-7F45-A923-014F2940A7E1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BC41DBFB-75E4-F749-900B-273157A9D8EA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BCD0F172-ED49-9446-AB0C-50F6C33BCFCD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BD90ED06-F72F-2E44-BD6F-7CA4F36051CF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C3EFDF2B-A3FE-114A-A974-118FCB9FAD75.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C4200208-C7B5-CC47-A509-ED79AD8329EA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CE6069A6-0D45-8B4D-9FCD-392FD2227E4C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DA4F57F1-5BCE-304D-9389-54E51B9A3D6F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DA8FA4BA-26E5-7B48-9D78-F8C1D37C4579.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DB68500A-183C-2646-8A47-85549D3D01DF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DCE88EFB-D308-7049-87E2-FFFE1D263A92.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E51FD5C6-F93D-8443-9B0F-252FD4E1E8D3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E616701A-CD10-0242-97D7-44B8ECC31B5E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E69E544B-141A-1945-BE0F-3F9A2FC681A8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E783D79D-1448-3C4D-B1E5-BA98CDE4D63D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E9FCCA97-FD3D-FA4C-BDE3-14483AB2122F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/ECE8B192-4A1F-C84D-ACA5-D039F31DADED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/EDFD1275-7D4F-4045-A4FD-9C13D95FFCA3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F2DCC3AC-E881-9A4A-88FE-7C4FABF2EAC1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F75A9213-FC5B-9C47-8FA1-7006C675505E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F7C393AC-5104-AC43-9A74-CA3972CB5A3E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F7C43B6E-459B-DF47-A181-B77C6842E833.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F837CBA4-BDAA-8045-B9AB-B291CF6454FA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F9B25BBA-288B-6040-8A93-93C9603E5EA9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/FA430229-61DC-9446-87ED-E21D87F04DC9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/FF506E67-1CB3-CB4B-AFA6-94FDADF0B170.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/010A1E6E-486B-854B-9443-DCA397AC6C77.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/402D726D-B12D-5F43-88AD-5FF2218CB613.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/4BB70D74-BDF1-FB43-9817-8C9EE4082E5A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/547C23C2-BE68-8047-9F19-98AF73D5F447.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/6CD6D1BB-2148-A246-A578-DE925AE83F1A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/7081BA8B-C00B-4345-974E-29097E08FDC7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/7ACCCAAA-7F4B-B84B-AF35-307898BDA5E5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8DF76A91-A179-B340-8D5F-E790905CC07A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/04A977E8-E69C-874D-9646-60444A73E1EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/04AF203A-A0C7-7047-9938-F7DA1F8190BF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/0B9C5C89-D35F-6747-8E63-B8B6B1065EA2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/10F72DA3-6756-4C41-984E-C1AD6842F7D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/16EB91CB-B3C3-6F4C-BCA7-C9C4398C1085.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/1C2F172B-42BB-6A46-B5D6-D4B1B79A1344.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/1C8DBF0B-46F0-644C-BAEE-7095DAAF5620.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/1E051479-BF06-C946-A99C-1FF90A086FC5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/2B9CF188-6693-A945-860B-9DD282154135.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/2BC2E4C0-7599-6D45-98E4-5A42846CA452.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/33D87EA8-A7FE-CF40-A084-7A20DB22B18D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/39D514C2-A311-CC42-88A4-09F0B2CEADB0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/40F7B68E-3AE1-FD49-878D-A8910FAA5F7E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/489D01AC-EC18-DD43-B667-7A6D1316D187.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/51609AB4-0F78-EC4D-98BD-F31DC79D9AFD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/575681DF-2872-9B42-BF13-F7432AA95BDF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/598E7C51-A3A8-7F47-B4EB-6EB2BB2F2DFC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/5B6BE63B-2523-6947-997B-C9231847857E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/623224FB-9EC2-D545-AE33-D7571610F400.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/6731AA05-194E-5B47-A682-6E3F5569B584.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/6D7C005F-D2D5-DE44-B59B-1330268A474A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/6F63208D-B820-5247-A94B-899BAD8C1985.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/73F1C3EE-5216-1C49-B887-DD93DC8B19AE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/766F2D1D-C9A6-1742-81CF-D0D71975943B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/78A54915-0F51-1E46-8391-6D5244F390B2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/833EFCB5-E423-3D42-B27D-5175A19AB201.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/86C08C6B-E210-3046-8EEF-6322BBC564E8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/8AD3F9D2-90E7-D740-972B-80871B06A6B9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/8B796F72-636D-D744-A95A-F07AB5B65A5E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/8EC5CD94-EAF1-344E-9134-00B7E19E730F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9417D32F-9B17-2E44-8AD7-FC27A7A103B6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/958D8D92-4A5F-EC4A-B37D-7602F76FC784.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9D450549-6A2E-2A48-B58E-1310EDC7AA0C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9D7E58CA-B5C0-BC40-B93B-7F8C6BC17A17.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/A9F3CD04-10DC-E046-AE2A-60A5F94BF45A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/B0DBA61F-5917-E74C-BCF3-3C34AD27E447.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/C2463212-D4FD-3B46-9669-1E5CEBFC25AE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/C8092E0F-7F90-594E-8F94-DC51D1AF1B8D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/D3D0F7C1-0C78-D143-BE1F-7DA3CC75CE67.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/D3DC9D7D-A0D7-654B-A3E1-F23202FF4260.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/DD02B255-B2FF-C049-94CA-C4AADA1712D3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/DF17867A-5FF6-E64F-A093-B2C5B00B7432.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/E0AAAF00-2B1B-CF41-8A8A-E9C5B5F1C007.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/E3DF1FCD-407C-1E42-9ED3-DF40244BE497.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/EFCA7D63-8D86-3C49-956F-680D95915CF8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/F5FA5BFA-7932-804F-9206-15720E6F455E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/F6DF9A90-23AA-404C-9EA6-8BF61481A26B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/FF8F96F6-FC40-C042-AC6A-7C0E9A903A94.root',
] )