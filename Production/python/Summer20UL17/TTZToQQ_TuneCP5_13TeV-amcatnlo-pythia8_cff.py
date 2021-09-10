import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/1D4EB6B9-0338-0043-850E-4CDE2E1442E6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/27BC367E-5B2E-8C4E-9471-10CC82154371.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/55BC45B9-9695-3347-A9A9-B14E876A6E3A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/5A0CCD1C-239C-224A-B330-6A36295454FD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/5B09CAD5-5337-6648-BD63-DCC5B8865663.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/632BA27B-7596-FF40-ADC9-5D93EFB60F4B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/79616865-8875-B842-BDE6-3CDD4C877F1B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/7B03134C-0F6F-E141-98BA-F6FAA3EF8E89.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/855A297C-FF99-DE48-BB34-931343BF5DF6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/98B942C2-EC48-A84F-B34D-81073669FF73.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/9D28CE1B-C6B9-8848-B8AB-5063E53E5B80.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/A86A2C81-0C67-9548-A0DD-CE656B68697F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/A9D86CCB-828D-C946-83AA-3FCB9FD3737F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/B467C257-9789-BE4A-BA36-1BBA1E3F4609.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/B87ADFFF-9E7E-AE47-8CD8-4DE73737330E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/BA57D5DD-E823-134E-9FF5-89771412B6DF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/BB31CF77-D8FD-5644-9285-F60FCA07806E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/BD651FB3-9AF1-EA47-A7A1-6BE180623CA0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/D2EC015E-F7D4-824F-BE70-6E07DBC3E721.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/D348D83D-35DC-114F-8FFE-B69C4B61FB6B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/D5EA61D1-28F9-C645-853C-F568D1F60297.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/D850DBA2-2F30-0A4E-B340-46D477AC7C58.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/D998FE17-D8F2-414F-801F-D580FF1DDB3A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/F098D0C8-7AA8-E841-ABBA-162B6C4F2A0E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/F28074DB-035D-074B-B5E3-F331A1791783.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/100000/F6BA113D-9FEB-2B47-9B22-31E239874891.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/08F38596-CEF1-0C4E-AE5C-054FE93DD2A7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/6704B953-5613-E849-A963-0B053D7B615B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/DEE37CB8-8796-6248-8708-2A940C0BEEDA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/FB0043F4-9784-D441-AE21-F8AC8EFD82D8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/00BA0DAC-74D9-2043-A894-B9DD10F42D93.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/011E0A33-7230-0C4D-B5FD-3C25EEC0969B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/01289523-F681-4B47-8395-CE866F936987.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/03410D13-A3F9-B843-B308-DAA4B0C4D845.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/06512B2D-0416-8F4D-A658-16F142B6C8EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/08CEC23E-FAE3-E445-B7B5-76385E2C51C2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0A58115A-D8F6-7C4D-A378-A125F8AB64AB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0D7C2DD1-FEE0-DB4A-8566-796AC17C84D9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0F2A7EB3-D238-C148-9F07-9832B9EE6E16.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/14C9D486-9BB9-9C4B-B808-0FDAD29D47C4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/19139EB1-9A5E-C449-99DA-E6C04EDCD241.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1AC6021E-24C6-A74A-A7CE-6D533287E65C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1C1079D9-5092-4B4E-860E-749EAF8FDC0D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1C5C4A49-4763-624D-B484-4DF0A2630A3B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1F44AB46-FFF4-C04E-BE57-1A40BFE6253F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1F465358-B392-9548-98DD-F85AD7E20DA3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1F5D63DE-7444-8449-AA8A-5C92DD203968.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/22B8FDA5-C6EA-8B40-817E-FEFAFDD1E799.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/25003B30-2106-844A-AE36-D36407924BFF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2712E2B9-7D0E-064B-A2A6-E330041EE783.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/29AA0B71-81BF-CA48-BEB2-EF6A254A6B56.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2AE3DEDB-875B-DC4E-A7F4-93C84D7E30EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2B7082FA-45B2-D44A-975F-65572892FE2A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2B70EFF7-B4C2-1F4A-AC5D-15D34D733F9E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/2EB504DA-2F59-1C4B-AC9E-466D4D82A7C8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/301D8792-B71B-4548-A8F5-8AD4BBE4F7AD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/32EA2972-6471-BE49-AC14-45ACE78CD1A6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/36CE64FA-4F3D-B348-9733-5226A910F713.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/37268288-343A-934D-89FB-442FC4D29B19.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/381BF147-62EB-1843-804A-8F9CD68AA4C8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3A59EFB6-8ECF-7443-BE61-5A5BDB855D6F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3ACEDF78-3C25-3943-A810-E6BFCE3E779A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3C85EAFC-A317-6E45-9109-3BA6125F7922.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3CD3DB1C-1FA7-0F41-9A4E-2C6F1B27A31D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3DF9A043-25DE-A149-BFAB-F6833C5A46B4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/40858315-E0D4-974C-8426-9502502DCCB3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/416BDC07-BEF2-9648-AAD0-97DEEE8A3800.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/44608A31-A3E8-954A-B696-2FB9DCE29AE0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/47330D27-5B68-4845-B2B2-08A4D0EDBC1A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/47C0A234-63CE-084F-9CD4-54BC0D0362FA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/47F49725-59DF-484C-8414-FB43A5E6EBC1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/49A24AAB-A580-8649-932B-65FB00EA9A23.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/4B2C07FF-C90F-E744-8AC1-694D50617850.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/4C9A11C7-A106-2042-8AE9-CCDDADA8078D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/4EF3F565-575F-3847-AAA5-6E45267993ED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/5480BF9A-A756-6740-9E82-FFD0DEBD1D26.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/54913B8E-28F2-D346-8FF7-45DBB47CC8D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/56525CE3-D2F4-1149-B23D-7E983AC202EC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/569DB24A-0C90-9A42-9E24-AE4F473DC2B4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/5BDBEF96-23A5-CB44-873F-732E54470387.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/5EC28C56-2366-334B-ACB7-68522B1369A6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/60056127-9B75-264F-AC7A-2C3137ED2D3B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/6A021D93-9535-8A4D-B411-50BAABA1C3C9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/6A644FE9-17C3-5642-86E0-E6203B715ECF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/6D2E04AB-3AC3-1C4B-8677-319B2CE4B65B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/70B6AF1B-C6AC-EC40-B922-6DA6D6E8EE3E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/72D0E207-A481-0A42-8024-DB65E165875A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/770B5244-B6E2-C44B-9D09-007D65D1025D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/8774B42D-111F-4643-B905-01F8FBB5A2FB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/88DC98A0-5124-D843-B271-31CD3871A0A2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/897F4B7C-FB1D-B14E-9135-D421FF425954.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/89A441D8-0685-5946-A0A3-F3A6B3FE065B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/8D98569C-CC67-3742-8BA9-1BA8BE3A32CF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/8F341CFC-8B3B-2941-B0DF-46078706B496.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/931BBE6F-88DA-B346-9018-AEA392B60FF7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/96BC2F04-C675-AA47-82A8-594979397AD3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/9A61CA8D-798A-E54E-BE54-E5B7DCA64E5E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/9E06E538-E4E1-3643-AD8C-23F54B6D0834.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A1A48C4C-9A12-3547-8C59-C2EFFE346866.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A240F5E5-E40D-A84A-8025-1DAB6EE3C9F2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A7B39B1A-0690-A741-811F-ECEAEFB6AE08.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/A7E082CA-F031-E846-B6E5-6680F3A19317.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/AD615210-E8D0-534B-9867-6AB595D917AE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/AFF6ABD9-C4BB-5A49-A098-EE8D68771F94.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B060742C-2094-074E-9700-D513238A5D72.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B15E2561-3294-F840-9EEC-7723250089C6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BC46D60D-6ED7-A046-8B26-81AC5A1AC72C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BD2D2373-22BA-124F-BAA4-D4A0525CB513.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BD367AB4-9F27-0345-9434-4C58BB275BC4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C0327C3A-C19D-884D-8D41-FEFF6B82FEC1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C0B31B13-5302-4A48-89EA-9832B09D6355.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C5BB3E25-8731-5D48-8384-BC3058D066B2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C61EF958-4D9C-5242-9EE0-94A7776324C7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C706C092-5E4D-1145-948A-6415D4F3BB7C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C7D24B00-44F2-314A-987E-CE2D46348220.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CA938E43-D6CA-DC4B-BCEB-E0DE03AD280E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CBBB7390-0E76-914D-9BD7-613306AF2D73.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CBD3BEEB-0735-7A46-947A-134CC0114483.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CD3923CA-749E-704D-AD38-25458F07B6D6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CE4E1696-1749-3F45-9608-5D27F57B6483.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/D281F5ED-AEE0-B741-9BCC-E6EB381E13A3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/D7C49E2B-8B6A-EB4D-9CB2-AA6564278123.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DA07B419-7260-494E-957E-305849985B3B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DB9EE984-741D-BA4F-A4B9-99E80CBC5DCD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DBBE1A0D-4E50-0546-B85B-B27DDCFA8970.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DCF6E179-F78D-2040-8F8B-A8EDAE54604B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DDA5D59C-0DA2-D74E-8618-1FCF25B3B096.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E1A1DFD0-C261-4B47-AC7A-FD79C0226588.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E2B6363A-95B7-D64E-8623-8C56ADDEF49D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E2B73C90-19B3-A349-9820-B0D4E81B39C5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E4928A71-84FF-C341-9177-BA4E503A5202.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E5901E12-7E4E-3A45-8CB3-B1FF89CBDC13.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E8B14C7C-0063-0648-A5F7-993A420F248D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E8F21C45-65CF-9648-B000-5FC3BD4A0F56.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E90C4608-5209-5E45-81AC-392086321347.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/EA1325E1-38E5-984A-AB40-C55DF1B6D468.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/EA6AF90E-E7E5-5940-A5E3-596BF5FF9547.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/EC0764A4-20DB-E046-AE1A-E139B708045C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/ED9C22A3-8645-3446-A700-33C131D473CC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/ED9CB6E9-8383-1E49-9955-EA8AE8838ADE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F3D9F1E4-25CB-5A48-9440-D55B169E479F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/FA6D0596-25EC-AA40-867B-DF2FC0E833D3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/FD82FDF8-B120-EB4F-A93E-75AF39C99A38.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/0729E308-36C3-9243-AAEC-6C68493994FB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/07DFD5C2-C620-1642-8779-A3FD17AC3020.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/0B5C9435-F7AE-5040-92D8-A9CE34BD72A0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/0D711F56-E54F-C640-9DDA-95120444FCA8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/3A0815A5-E54F-6A42-A23D-020AF783EF6C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/43C8A6A5-F252-FB41-A9BD-F859F7248AC6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/4E253A03-80CA-1049-BD19-AED5AF894C6B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/51A54E0E-7645-9C4A-907E-0AE3F6A3335B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/541EAABC-6D6B-6642-9B13-191AD6591D68.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/5EB3114C-1512-0742-92CC-52E200F87BDB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/6FC1F0A9-1631-9547-B9E3-4F616158E686.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/7200C4F0-5ACA-6743-825F-515BFFB1328D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/76402E45-B4FA-4146-A7B0-F1E0201E2784.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/770269E8-D4DF-3142-A7DA-B8307D6D4B2C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/7E02A5BE-D2A8-4541-907C-1339C83F3459.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8CDADD9E-A5F1-5946-A6F8-1CBBA53950B5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8D77DEE7-F5DB-0E4C-A5F4-4C3169B3922B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8F4D1437-6489-FA43-A89F-8A406CA71C48.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/933F8DA5-4623-3F41-8C67-46FED7D332EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/9445410F-E153-E64E-BA9C-113377237A02.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/9992B3EF-38A7-FA42-8ED5-BB39F1BE7340.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/B85FB8EB-01EF-5341-9E50-9F4ACB23FE4F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/BA8D535C-B345-FF49-AF9F-83AD53F17855.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/BB68BEC8-3CA0-7645-868B-36DCC16367AA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/BBD82070-4425-BB44-9057-1A8CC2D96E81.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/BD27E4BA-87FF-5842-BF92-1E3958EFD225.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/BE27A274-939C-8B4A-87C7-4C1508C4FD9C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/C89C3C1F-1306-3F4E-BEF3-048DA0C46694.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/CC5B8CE8-61F4-5F46-9FA7-507A2D460E87.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/D1DA6138-1AF0-D141-8DCB-6C8D46BED936.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/D411C1AD-0529-A44F-94F9-1DEE48D91248.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/D5492850-B86D-F545-B852-E2DBC1C4F13A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/DB676F5E-B3F5-D341-B836-0898CD5070DD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/E2AF5EA8-AB1F-A24C-993E-4F8BACB2A921.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/E65684E2-5C94-5B4E-BF54-3B302341499E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/30A19822-FE6D-3C43-9609-4D9EB946BDF9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/33D6BE8A-1F2E-7145-86B7-40BAE11BA9C9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/593D64B6-A8FA-5648-926D-2A31E7386040.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/5B3B15B2-452E-884E-9232-102D47EAC00B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/5E46F355-324E-434F-A0BC-126BAF490FB7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/6A5D9817-8AD3-A449-A567-D485D155A31E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/6DC79E99-CDB0-1B49-BD28-21A23E81C067.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9E655B52-BE00-5F4A-8C5F-264EBC9BAC4C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/BC222FD0-F233-FA40-B241-8E4B4B7424F5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/C1D0EA0E-5E09-FC48-B711-1E817BFEA63B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/E8FADDDB-61B3-BD4A-A3A7-17719CD86531.root',
] )
