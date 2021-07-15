import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/025F4214-A43D-1440-8B4F-4722D46253F0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/04A98A8F-6803-104D-A2DF-28092239896D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/06C04734-05AE-424A-B847-4458C7E93B93.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/08CE918E-B3B1-4544-9F97-7F234DB86E86.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/08DA0F48-EE52-0340-BA9E-752DF7362D5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/176D85C1-1D0C-6A41-B475-354BCFA8E052.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/17A69176-194A-A84A-B9D3-9DB37A6F6F2E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/18701D3E-FCC2-DB4D-BDB3-A2A73EB03CB5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/199215F4-82AB-304B-AE3A-0338597079AB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/236BAFF8-21D6-E74A-877A-2323AE7CA7F3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/251FA6B5-9050-A241-BFD2-156B05230092.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/25AEB1BF-C0D8-9D4B-8024-62487D4F18A5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/29393C10-D24C-D848-9000-C2A58CA8D345.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/2AF3B700-09DD-A349-83E6-0EFBEED2D0A6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/2BB942F7-08F3-434E-B892-950B79F3D08F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/3458EC9B-B864-5341-B970-5F249B309A6A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/352CE397-6D30-B343-8E03-C1672A0CAC81.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/3C902E4A-B36E-194C-9C4A-291DC67B667C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/3E84E98F-AE3F-FE46-B2B8-347C1A28FFD9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/41C19E8B-C5AA-E64A-BD75-484F31CB6691.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/42FE10FA-5BA7-1547-9991-95E562DF5B4E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/476E7C2D-EB2D-4346-87E2-101AE0770B64.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/47768BCA-1CA3-3E40-BE10-654ACF1933FB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/4B5867D5-88B2-3F41-A815-2B9AB9830F26.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/4FBB7C9C-F48E-E54A-BE62-C63C72BAC847.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/54EC4F8F-E7FA-244E-9A25-D83327BA05CC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/576B2FA0-D575-C540-9741-5AA0A3E143E3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/5BF24B76-98BC-1A46-BB2A-7B9A06355127.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/5C8FBF36-B291-B44A-AE7A-0B1CD409F447.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/5DFD1AD5-A2C0-7645-BADA-A6FA36322E73.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/62A2E6F7-447F-3D4B-A2BA-85EAE1ECC99C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/672A2474-B985-144B-B0B2-5A61AF896B05.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/7352C8B1-9E15-BD49-9390-BA309DE59750.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/7D6A3CE6-F408-EF4C-A2C4-FDEBF4AF3299.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/7DBB58CE-E121-3C43-A7D1-2A48C22D64BC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/7F2A1DE8-9006-5541-8DD8-33ECFC3C72C7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/818498AB-0D48-264F-A5C8-128D2B04A0FC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/8A5CCB2E-AFB7-374B-B2E6-445841627993.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/8BD135F3-5BB2-A141-85A7-9EAB43F43280.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/92DF0F10-1A6C-0C4F-934E-9E67B9844617.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/98482D02-6B00-5C48-B5AB-13A7C464F9F9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/994448FE-AEAC-E74F-B1CD-75758E9AE244.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A043A44C-C77B-8845-929B-B21B38396374.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A1851F1E-6E48-684C-94CD-DC63632D3AAF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A6EE6A3A-9189-8B45-B0D6-526BF0F79006.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/B2713AF9-4D82-9542-BEFB-097E9CBD32CB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/BD68B458-BBE1-6140-83FC-272B849623F1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/C27FB8F4-841D-8641-9740-19825E466B67.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/C5CD9B04-9326-5D40-8CCF-D68021D84B93.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/CD15246F-4CF2-5644-A419-F30F0F86EB44.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/CE88D686-F646-F246-9247-E685497813C4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/DB09943B-D327-EE4C-B670-E4AD0C8B0C76.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/DCC39F4C-72EC-744C-8C65-AA1E16CD479D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/E02C5AEF-0ECA-954B-80C2-821026A0F71A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/EECE0AD4-D246-344E-84C0-B29275C5F73F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/EF9B30D4-0C3E-BB40-A6FA-23FE109270FB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/F0FD4B19-D342-FF48-8F75-E1CDF4BCF422.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/F19AFA83-C38A-0A47-8BF9-4EC227E89D33.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/F2D4DB39-16C3-A940-A4C9-B5A51098FEB1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/FA02A88A-9179-EC4A-A0D0-EE59152DC038.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/FB7F363F-DBFC-4940-8B7E-5605DE216833.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/06A88290-4D6A-6949-AA4E-6B5EAD0E450A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/09118A7A-0BB4-6840-88A2-4650A0D5CB38.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/21E98ACF-0394-E147-970A-9186F48F00C9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/2A8A5A2C-97E2-0F48-9A1A-4FE34D29D135.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/34E39258-8391-D845-99F9-683CBC4BB73E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/3B0D4208-059C-2147-859C-C3CB0E901EDA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/3D2F853E-FE48-2148-911E-ABF7ADC4EC04.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/41AF4A81-40B7-7D46-8DF5-D265EF61972D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/450354D9-F200-314C-96CD-EC417DCB31DB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/463BC646-ABB2-344F-AB9D-C80031057EA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/4D18EF57-66C2-DF4E-AE9B-5EDA20F61A05.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/50155A6E-0A96-024C-8DBA-DCBB4D8062B5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/5C687C39-4D14-D844-9313-FB64CE2AB265.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/610625D0-24E5-494B-9CED-7F03844EDD28.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/6142FA88-8E68-D84C-A186-14F7200D50B4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/61A0E401-FD04-4A4C-A9BE-506D55FA294B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/61E39778-83F8-4449-AD46-397A8B6F8C5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/6B7ECA86-665B-6140-93C1-0ADA8F0541D9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/71987700-2788-744F-879F-E0A08D35527E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/72D901FD-1C7E-AF46-925E-07E1942EC166.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/7FB796D6-0EDA-A844-9B7C-D0301178B8A7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/83F5639D-52A3-EB45-8A6F-7747363DC5DD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/8AB85063-B1C3-834D-9879-497F83F35F94.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/8EC86610-9425-2F4D-B660-7333B003DD17.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/921E22A8-AC73-FA4E-999A-83788D63526A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/93DCCFC6-4574-0540-84E3-E131110FE66C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/A21063BE-D548-4541-83A2-28D431156B44.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/A438E3E3-760F-4044-B3F9-06D30A63903C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/A46B1987-4357-024E-BD51-AD11A7BFFF04.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/A799E6DB-D4A2-564B-A4DA-1AD791AE0321.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/AE96DBFA-F0A9-A346-864C-48C7FEE21EAE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/B1C51CDB-4EE8-CB4F-B272-CF1B4C6272CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/B229C381-3E07-F743-B365-D75FFA601B9C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/B84FF683-AD19-1843-8ED2-BB13C1F0E529.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/BD1463C3-EB2E-F849-82E5-148644849441.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/BF77FDB5-5834-8442-848D-0A28027795AB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/C479BA15-D7B1-BC4F-9587-9A9478570208.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/D08F5356-E72D-DC43-9142-BA7050C8BAD3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/D5A71163-7F5D-8044-BC22-320D0048FEA6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/DC9DB0F2-13AF-1941-B27F-5D845CB67976.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/E0CED6C1-F6F4-854C-98A5-FC94354925C9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/E378CF4A-4080-3642-95F9-84DCDC8728E3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/F6BA5559-F1E1-9142-BC3A-2DACCAFEAF52.root',
] )
