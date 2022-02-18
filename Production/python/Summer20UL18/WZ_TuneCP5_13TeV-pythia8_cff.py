import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/49FCA235-D8E3-0B46-96F2-2B3432C79CEE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/5C8B1204-B83D-6040-A4C8-90BB1B6DEAA9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/9AC24813-C250-FD4F-906C-08A5E15C1993.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/B77DC3DE-AC00-F94E-8439-E598529B280F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/BC028D8F-E28B-9B4A-9EAF-CDEF9A36AD7F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/00B17712-3DA3-FA44-ADED-F94867AA064A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/0627DE7F-3CA2-514E-A9D8-8EC39F0E13DB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/0C0781DD-D8BC-004C-BB04-FC47562AB7DC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/0CFC8E4C-7D54-0B4C-9350-43B79D5C68BD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/22F0E52F-E14E-7348-A650-3250DCD50FF5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/27F0EBF5-5DF2-1848-B76E-B4F4BC967264.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/3EC924F5-9A8B-9F41-8E44-BD95D5146678.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/3EFA45D3-5ABB-AE42-8D68-AA44BD5517C3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/452F71DD-D0CB-CA40-8473-4599E0FF76E2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/4695E499-F9DD-6D42-B104-0C59FB475287.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/491C79D5-CFEC-3247-86A4-B3F248A47CEA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/59DF56E2-A998-A549-81D1-B709DBF25EE6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/6EF7F914-8D3D-C14D-B17E-9BD5B86AE4FB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/72037A1B-5483-994F-A10C-D8D0F03FE73B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/7B52D585-06DA-DE40-8C91-75AF605AA3D0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/8286BAEA-AA68-984D-8A31-DFAC1442F983.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/852E2F3F-50D6-874F-9F09-834FA3B652CC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/8CCB58D5-CECC-0940-A13F-92C9E4916169.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/8D1D3ABC-7623-3846-B51D-732C144AE7EC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/93FE627B-3627-904D-AADF-8CBDCB654F48.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/978F779A-29F2-9047-9DE4-AB8537A75B96.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/9B6DB74D-2E51-3243-8EA0-6DB777FE596A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A06DB22C-D92A-B649-A9EA-44250BA80F6B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A4833F0E-0B84-5A4A-A056-22477433F5A6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A596F3B0-09EF-9240-B64A-7F8AEC2CC57F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A603B3C9-93CF-884C-BBEF-1B6ED5AEAAA4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A6887E19-3D87-8148-8357-752FF63188AF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A6A0208B-3ABE-0B4F-9412-4C86EC1601D4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/A73989F4-4BD9-5C4D-AB29-05D0F4A22603.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/AC52F2DE-CA27-1241-9410-BF2D7D3A27A3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/AD8C681B-591E-5B4E-A410-4CFC568C484B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/B4BEED03-216A-0B46-8738-312E8A37F1D7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/B9C25A81-56F1-1046-96CF-EFC0F1F910EE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/BCD47E70-B264-A242-9649-F47C7377FE8E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/BE18FC5D-3A68-544E-8B0B-952089546FBE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/C62EE67D-77CE-354E-A03E-363840A9FD7D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/D27E1C0A-E418-7C4F-936A-895117C90BF2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/D99F592B-D3A8-B048-B491-FCACBEC16FEB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/DCF5E09A-3E9F-B840-889A-EEA615F8B2EB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/E1806C89-D338-0840-8185-A1F12085367C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/E61ABB39-8AFE-BF44-88C2-8BD023591766.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/E6300D59-ED61-5B4E-B517-898F3C8F2A9E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/E6846CED-E6C8-EB44-B49B-C1B1943767E5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/EB1EF950-A0FB-1447-9953-933E045C3253.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/EB7BF4A3-BFA3-9C48-B922-A008A9432EF6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/ED30AAAE-7D9C-CF45-B4D4-5F8B52A93BCC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/F15E16E5-62F2-8D4E-8DE3-30D4E185131A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/FAF4E091-7C85-0142-8399-21A415AA7694.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/17D4237F-30FB-3A44-9EFE-C723048AE7DD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/23B7892A-9094-6544-966A-B86FFFB638CC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/23E21A5E-D71D-8945-A928-36D150C69AC6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/48CDB839-0E3D-4948-91D2-A381231F28DE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/48E557E1-332E-A14D-B87A-53B66F852D7E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/4FAA520E-E78F-B14A-BD66-D398E473AD38.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/5D0BA4E8-C9F6-244C-B70F-63826679F982.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/5D5F2FEF-C5BF-C94F-9A20-21551CE8A9C0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/623BE610-D2EF-4945-A24E-C29EF235490C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/790EDDFB-9B73-514B-9D4B-75A475A0BD59.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/8398F18E-98B3-4343-A599-C4215E451176.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/9F23B338-6D1D-A841-8C8B-149B90E69179.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/AA1ACDEE-9842-2B43-9383-CC999D996003.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/AB8B9376-2747-0549-957A-16FA38712E80.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/AD08B580-6B90-144E-BEA8-7E0D875B347C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/ADC61133-8996-CD4D-B638-71121348AAF4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/B93C1049-6B98-A745-91AA-5B6CD74E0DE3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C539604B-E372-B648-849E-24DD1822926D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C61C8AA1-DF61-C94F-B367-E75B841EA8B9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C8EFD226-F2D8-204B-9DCE-8CD4DD4FE149.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/CB72D26B-A0B2-1749-B5CD-62ED631CFA10.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/CCCB0DEF-3D8C-B34B-B7FF-DF4A710B1F0C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/E302D6B0-2A8D-1746-8575-E1B18F7C4E2B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/E7262AE8-6930-7544-9A33-E5855290861F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/F40FD48B-7A2D-A54C-A55E-08E91A9694E2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/05502F2F-38BF-B942-A2D2-32834A14D274.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/1C29DD62-BAA9-9B43-B82E-7A6DC33D0927.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/1D1E5DA5-9EDA-8D41-83D3-0922A10AC1A8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/23CD4EC7-BF71-6E4C-BF40-9B60AD0B83C2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/25C48284-6024-A346-BF76-D58B9D690ED6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/299C54D1-C5A5-4D42-8BEF-15CA134DAAEB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/47021802-F6A4-4942-935A-019A2EB484FE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/481FC5FA-893B-FC45-87B1-7DA42BF4934A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/619B07A4-712C-8041-B6CF-1A636504EF2D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/659A77C2-FEAA-A44D-9FBD-A10995B96B42.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/66CBE7AB-7240-A743-9E5D-F57AA9237959.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/73C968E1-ABEE-2A4D-B8E9-C43524AD9421.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/836C9512-49C4-1246-B4DC-0B97B9023190.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/8430D318-7939-1140-BFB5-3B2FD3ED7125.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/8B47E054-B0DB-A54D-AAEB-73DD31AE5958.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/907DF99A-5CC3-5846-BBF9-9AD01B5E2350.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/9B2E9E5E-4C11-CD43-AAC6-CD4920153E65.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/A86D5075-CFC5-5641-93A8-18BE2F3DEDB3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/A891F245-54B8-0248-B7CF-D2374E742D06.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/A9114873-1E8B-2741-BAD7-E792794B4010.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/B3103C6C-4700-0845-BE64-9E5CCFC997D9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/B4AE0E97-A317-4247-8570-8CF35FB5C6D1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/BDDF2077-B730-7A4A-8309-A6BA99735586.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/CC755734-E0F0-F64A-87F5-B3533B1B74BD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/D75F3F74-037F-E843-BD12-CAC6FD9786D4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/D8240DDE-015A-9848-99C7-B7E178B3F98A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/EF451F06-8160-534B-A956-8A4D45BEE552.root',
] )