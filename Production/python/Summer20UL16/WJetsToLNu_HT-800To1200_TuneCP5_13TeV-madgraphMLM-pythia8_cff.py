import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/0F2979F5-DE39-2E41-A52B-363A5000EBB4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/151A2364-B216-E04B-A32B-8B6F561E7ECB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/22AE9A3A-3E52-3944-9B6E-EA6F56809CB0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/6B0A71A1-7407-0A46-99E5-3436E0277801.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/A2588582-06F2-7E4D-BE10-B35DEB6A9EDB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/BEE95788-13B5-1F43-B76C-0F5DC528E95E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/C3A2D460-E71C-484F-8E7D-58F1F65E7E88.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/C8736BD6-2551-AB4B-88E8-0B7D48C0F8C8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/E97C3860-883E-9449-892C-2B89ED4AFE9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/F2221925-7DF4-C54F-B210-7B311E342F31.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/F8DB39CD-11F7-D141-821D-2F482E006958.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/FB617460-A4F6-094D-AE24-E17EC22FA6BC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/00B368D4-34D0-BA4E-B1B7-E2B240EB7655.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0DADAD06-359E-EA40-8951-9BA5D87798F2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/211B4853-A908-6E4B-9DF3-6F381AF2160C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/326503DA-448F-7E44-9CFB-62D5DE6B9DD8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/361CEB21-1F50-CA4B-957C-1F626F0AF1F9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/41FBFF2A-1E48-ED41-BBD1-835D819739AC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/434A7E71-C0D4-4A4A-996C-85F62CD39216.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4539A6E6-6562-6249-9600-F72A519761D3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/492A25BD-603B-BE46-BE0A-CC60B4A5907A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/76B2F0A5-61BA-5345-8F7F-BE89BDA81CA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/77AA7D30-4851-BE4A-9CC4-F0556CCB15F0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7E0E21B9-6526-DD46-854D-547E5125D9CF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7ECF583C-8564-DC43-A706-48A8A80D73D5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/80A6AAEE-40D9-5140-8090-EA839E22D560.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/86921C38-CC9F-354E-963E-1CE626BE2FC3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8C4281DC-9A05-3440-9DF6-B912B4A0852A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/91D9A5B7-4D3F-9549-B17E-1EFB2E85C9AD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/93F4916F-A765-0647-A7E9-063EE32D073F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/995C0CBC-2BF4-4145-91F7-F1312A844AFF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9DB3CE05-8732-964A-B935-65B778A466C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A983D07A-1F28-F141-9581-258E5D8298F4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A99DC924-46E8-D74F-97CE-2DE1384F235F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B5840801-4D88-C942-9EA5-7E378DE67A85.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BE3549D1-BD6F-3946-8079-DE7A3E7F111C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CFCA8AAD-4AA5-1344-B396-BA6141C4605F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D28F4F33-2C34-AD40-A760-023753E242B0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DF8B2E0C-CD86-4E4E-B2EC-F2728512C41C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E8C3BDE3-2093-3643-98F1-B91514FCCAB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F0DA8127-C830-524C-BD7E-C0DCA30F2478.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F9DBA4A7-4465-3048-B9C4-323ADC4382F6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/108DF9E6-AD5D-A543-94B9-BAE1053439DA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2851ADB7-14B1-224B-A521-6330F795DDC4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2FDDD3E8-8761-A24D-963F-3FD431DBBF9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3248229D-86F2-214C-BC42-732C5043CDEF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/35AF115F-93DD-F440-AFC7-B254AFA6FA39.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/36B24736-EE56-C040-9FB8-F1B264DD893D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3D9E593A-3A50-AC42-9F60-8846F87654E7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4D42D126-98B6-1148-9BC2-5E661086D661.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4F1BF53E-BE97-A04C-89B2-CDED6DEC982C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4F3724D6-6103-8F47-9831-D3DFEDBFAB07.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/5F29CF39-39ED-F142-99D3-3B467B482B80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/697ADFFB-27DE-914D-A3D5-2DA9DC82BF9A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/6C483141-BFF9-EE41-9DBB-532F0C51445E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/6E9AB05D-0C2E-4C47-8733-62FDE6266F88.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/722C8574-4882-A24E-858E-442AB004435C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/7C0EFC46-E830-864C-AB5A-2E2CE79679D5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/7E1777CD-4F4F-514C-A98A-1FE3F39575C9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/9DF811E6-87AD-5B4C-94E3-4F3BC13410C6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A8E005E5-DDDC-C046-B3C2-2D17053D793B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B56E7501-F60D-E747-B11C-722EC3DA1D16.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C3A63847-1D17-D344-8014-EC549C77DC28.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C4CC7928-A622-1141-B0A5-C018CEF38BAD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C6C9E23B-658B-454C-82AB-2871A7AB9F15.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C78BBCCF-F0BA-7040-8FEA-E6ACE7E5812C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/D883A666-1B92-4545-97ED-12364A6FE814.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E3647A18-8DBD-1845-A00F-C96D178426B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E59DD842-E8C0-2249-9EAB-B39DA9F130ED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E5DE46E8-FBE5-1845-B12F-C1C8C2C96B71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F1D8A167-62C6-A645-AB55-3AA651F4A255.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FA904F07-9877-4A4E-9194-198A805976B5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FD0ED9C7-D021-E74B-9F48-473EA32AEDF5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0A91B586-F14C-B440-907C-0394C58C6E28.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/100F078D-2F18-5D43-8F97-30FB2F12AB74.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1769A43C-57FE-E744-9F04-AEDE45A5D7AA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/27744387-863A-F443-83CF-0619298D5BDE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2CDB2D54-B5FB-8945-AA70-7BD1ED3F9E6F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2E6D5D04-1C92-D041-BD81-8958AE500EFA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3930DDDE-A960-9640-A4E6-3491214779B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3ADDACBC-A56A-9548-89C9-7AA944D99FA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/40CE0F27-1C67-2E4E-9E84-AE0DA6D614BE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/484942B8-0D42-BA4A-B2B3-FCEE198B85E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/56976052-533C-7549-B20B-907DDA452FCB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5ACD8E0B-64FE-2B4B-9083-F2F34EA3A7DF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5F446117-D5F5-2443-87A9-AF62664E6E8B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6CC01FC4-F274-AA45-8AF8-5F98A1B25DA9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6F4F12CB-B4E8-3440-B6FF-30D98667A8FD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/79AF265C-8C98-D446-A412-3CF6C5B082A1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/80582DE8-52FF-CD43-9A71-43F4ED485A27.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/82B0CB28-63BE-D14D-87C1-D22F8AD9B752.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8386C731-537E-474D-AC78-33C197720ED6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/83D17170-C034-5E45-8939-A0B49E6116AC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8C89927C-A027-F447-AFE2-88A3CEA67CF1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/922793D4-9BE1-7448-829F-9264D3F6B8BE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/973AFCB5-144D-C040-AAD6-D4C831D3F3A0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/989728EF-1A1E-154A-9B7C-D774CEC3F14B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A25AD69A-0A1D-CD4B-99EA-4FC3408DC8F6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B395FB51-D629-0046-BFF2-79758C549674.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B86A0299-7B3A-484A-8D53-678BC5A4DF48.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C35355A5-9422-F64A-AAD3-D89A02166926.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/CF10D6A5-A781-DB4A-B34D-148B7AAA5B18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D1ED5CFD-BDDE-D14C-A881-9E667FEA3EE9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D37371F2-ECB8-2C4E-910F-EAA0E6BADBBB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D6D1D037-2C2E-914E-99D9-AF8F01808C25.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E60BE29C-A3F8-AC42-96F0-6B508035BFCA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E8DF06C2-5764-064C-85BD-C8C80F000187.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F6A68D65-4B39-1B45-BB44-BA86DDB254A7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/04D16B3E-0285-D649-A832-1FEE610BC1FC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/0D2F42DD-11B4-8C4D-A597-D9D7B41FD73C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/1157E8B5-7530-7042-98D5-48FD652890E7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/16B5A078-47AF-124D-8B69-AEFE632747FC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/172CB7A2-7FF4-1A44-9CEE-DC027CF6B112.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2285C705-0444-7D4F-9291-D206399779D4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/28EF7D05-E345-E444-86C2-E9147904ABEE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2D747625-9D0D-B240-802A-676AF9959C73.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/30BB2E41-F39E-2C4E-AF63-C3E541762B37.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/35E03255-E25C-8843-88A2-1BF0C7CA5DF3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3BC51E9C-1767-5B4D-B47C-48F74ECCB667.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3CC48A00-2697-0F4F-9D4C-C270748359A2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/40315C35-BE7F-E345-A1A8-9B568E6DC745.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/5CCDF74A-A818-8545-9EFC-B7A41C57632D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/69606D60-6B97-E142-B242-265270CDD5A5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/6F5B27D5-25E6-0944-A683-586B4DDAA64E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/7DB0024C-B425-AB42-93E1-19CBC42B5A82.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/989CB671-5AED-F547-9880-881BC1B2ADF9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/A207CEDF-B329-E342-A5C2-E5D5D04752ED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/A5624EB8-416A-B042-94CC-71D0C2F2FF9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/AC19C945-ADB5-304A-976B-3869821AE06C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/AD3564A8-2DD8-5B4A-81B1-A3B222B9CD63.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/B5914ABE-17E7-1A42-A620-C5066D7184FB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/BCDFF561-B744-5947-9ABE-9343733F5DD9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/BFA53FDB-5BAE-1048-9DC1-CAB48D0217C6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/C5350116-655E-C94F-9EA9-273A43603801.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D81E1A34-6FFA-D348-A6D2-A7768C73F1D4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/DF6FAB1E-FDD8-1748-9823-F3D781BA0B73.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E6B29532-3261-524B-8DB2-9509F5CB36D2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F0F41C43-7F72-654F-9DD3-D7FF9539DC8B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F1B507AE-69A2-D946-A2E2-5FBD9B5771F2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F5AC746D-68CE-6244-ACAF-6C49F073B49C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F9061B40-33F0-004F-9C91-F6FCD83897F2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/40000/FCA02FF0-2D5D-B14E-BB06-D31081263D12.root',
] )
