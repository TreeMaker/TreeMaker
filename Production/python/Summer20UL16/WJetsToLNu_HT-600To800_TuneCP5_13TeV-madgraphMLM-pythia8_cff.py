import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/07FB004E-1420-FD4F-8A73-4A83C2DCF9DF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/1CABF0EF-2214-AA4B-91A2-A1116F458D85.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/1DE9E6D1-459B-B144-BB8E-D4649B3929C1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/314C92EA-D37A-FC4A-B296-CD684041763A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/3A90B0C2-3740-EF44-86E8-FD0CB0EC0226.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/41687EBB-53D2-1544-A1D1-CA3C6D49A086.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/50C17978-F39E-0245-9E2C-66CF08F1C112.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/54767B0C-C3DC-E94D-B5DA-4972680C2B7D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/5E5738BF-7E1B-8848-BC98-1605975E1017.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/5EFC7C76-0AD1-204B-8B90-3B50D916E431.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/611726CA-6FE0-6245-BACB-4FA99C538EDC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/622A6CB9-9DE5-D749-AAB4-59476ED86A05.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/65DC5502-611F-0444-9F34-461F293758C6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/70BFC4CD-8C79-0A43-B4FD-0BF78F4C5BE5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/76253128-408A-3048-8FEC-EC36C789F58B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/8426901D-07F8-6E4F-8A6D-656667BBCB0F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/85DB20EF-ADB3-A347-9139-01E3FB29BE54.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/8943951E-4545-B744-851B-F40BE6B0935B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/8E7EE62C-8CC6-B448-B015-C2ADFF607CBA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/916F4CE0-7603-1A47-9D9E-22826202D603.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/996A3723-AD1E-EB4F-AD93-6A99DE774BDD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/9D154115-0986-174A-8CDC-E35DC8E71C8F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/9FFC4997-C81D-FE46-8CAF-A0942C8ADAE5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/AC729784-04E1-2A45-B1E5-28B01C87F604.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/AE2DAEED-26F7-9E41-BB5A-73671E6F722F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/B4F97F75-E50B-8543-B1E2-9D3963EE6A68.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/BFEEDA68-73BD-354D-9770-6525E14E39AE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/C07EDCB7-E3D0-FA42-A650-510E0113FFB3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/C5BB4F02-B280-ED4D-9DA2-2BE096C62B21.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/CAFB38A1-F4A2-2A41-82B9-DF0B282D68CB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/CE80792B-AFA2-A346-ADAF-D205D4785B29.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/D0D1A16D-8BFC-7F49-8B6F-73F04A892ACE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/D6C6FAEA-8509-B34D-8123-CE0AE40B8537.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/D719E876-6BB9-C94A-BB36-D589A335B78D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/DE82FE25-0118-2248-B3EB-CD84F2F2BC86.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/EB46E930-75FF-C947-B87C-98BACB80D60F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/EB86C8CB-B02D-C549-957A-377EC70E6F4E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0215523D-0291-094E-8035-9500973D6D55.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/09B9F443-BB08-AB47-95E2-1616079BD6C5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0EDBB483-005A-3B43-AF69-1D48FFE65724.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1357C9C7-704A-6E4F-BE4E-7B4AD885A921.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/176B396A-C473-FF4F-9076-1036BD1089E6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1BDB4AF9-F406-0A4E-B94B-0D58319336EF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/204651F0-B7DF-3646-AFB8-9864EF811285.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/223E9317-CC17-9143-AB48-5C1F6A142B99.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2683193B-C770-5E46-A30C-456D89E3F95E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2861BD5C-B1D4-A241-A562-CD4D70738E6F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2E4662F5-DAB7-8948-8ACB-BB2F57EB8C78.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2EBE6C10-FA59-9D4F-A540-562F95D66DF2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3438636F-B1A3-BE4C-9D21-8A081A03DBAA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3677A87E-79D3-C841-9EC8-E45D7F2F179D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3C9EAE44-A39E-BD4A-ABC2-3CD1A3BE3426.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/42213967-65B2-254D-808C-D807D4D995EE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4B845722-AD68-8544-8F7C-21F65F74C522.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5326292F-0DEC-C14A-B939-865E80B514AD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/56348FAF-A026-ED4C-9A8F-52616293E937.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/56B440F7-4BEE-2C47-99F1-DFCE04E82F02.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/58B7A2BF-E96B-E749-9448-23B72091128E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5B308719-EF6D-8F44-971B-D4155B365969.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/736309E7-91EA-5A48-95AD-BC3D5E45FECF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/78D0C46B-DED7-6E49-AE78-93C74EDF5BBF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/919E794D-B1B9-2B4B-AA26-D6DE42432A28.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/95346BB3-AC52-6E4A-84CE-B104549863B6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9D643B43-BF70-2246-A1CA-EBE0F7C7B530.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BCEB89E9-3345-594A-8913-F39F37D803C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BF5C5C60-5B89-E342-AA55-589C4B45AE33.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CF073345-D463-F842-A4FD-2C1B995CD235.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D160D850-BE47-1B4D-B0E5-10150B85AAE8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DBC4D526-DCE6-9B4E-8D67-286841927A18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F053CAD2-0A27-0E49-ADA7-3AA33DF5C88A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FC1CEB52-590D-4841-A6CC-BC948E183679.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FC8B100F-9F4B-3041-8499-6023337F5A6F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/016F835B-19BE-2742-AD23-A0CB1D9BB64E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/039720C1-C243-644E-B13E-E93C5A018BE2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/09599586-E817-9A4B-A811-2D4C2A246E51.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/103950E7-B9A5-414E-81D6-4B7C70F7E2F9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/1507ABB7-F40F-B54A-9A9C-4E356A804AA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/17369F26-6EDC-6D45-AF80-644F067F0D3F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/17D5CC15-4AD1-BA44-A722-02894D671FA4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/18DB44F3-38E8-0945-9142-A672C2ECAD9E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/19351654-0668-0249-8701-44D064493D18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/1EF4AE18-DB85-054C-9C53-3D179DEEF84F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2311FBE6-AA3B-8D48-BAE8-03228E553062.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/23865963-F9C7-5A43-9263-2FC7F3F95FB6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/265E33ED-7461-1445-B8F6-A945FEB8EE4A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/274636E2-5FD7-4A4B-9BA8-CCAC2E174852.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/288CC380-46FC-4B45-ACAD-584C55101979.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3A91C0A6-C33C-C646-8CF6-B3D91308FFF2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3B513E9D-58A7-9846-B21F-A73F87F54192.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3BF3A74C-B039-1642-959C-1B8F7C05A620.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3C5904ED-5A04-6440-8392-A5861F76FA1A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3CC66CAA-F210-C94F-AE1E-A1A974E6E689.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3D451ED3-B5BE-3349-975B-4B0FFFCCE389.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/44181AB8-49FA-A345-98FF-CAAC18E95752.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/47767599-85E9-7844-8089-A49ACE2F7289.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4885AD39-0A93-9049-9A32-85C118FBAA99.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4B971D9E-8458-3047-9DB3-7371B26343C3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4D8D608A-2F35-FE43-B1F7-7E3B6D7B2399.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/502B0491-287F-5748-AEC6-74410AFFB26F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/64199ED6-BAAA-BD4F-98F5-93D76568AB8E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/6E56DF49-99DD-BD43-B342-246271D50ED5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/80B40D76-57B7-624A-B257-62875DB5735D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/87A4FD33-BBB1-994D-9E58-FD551BAE2822.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/8E4E6519-95CB-F54B-B48B-AB2D51D1B1A6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/94A4D920-E2B4-4541-B3AA-25B2A63CAFCF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/989F769F-764F-624A-B82F-BC7F6921BA2E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/9F50E574-4C6F-0245-9BC7-890CE264A834.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AAD0AB18-5B40-BF4F-A603-468F6F7FF6FD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AADA84FD-1951-6A4B-BEE7-300E9999C422.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AD3DC690-8195-4441-877B-A0D6FD8D3D72.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B0FF8D0A-0E7A-4E44-A4E5-BBA7E3ED9BD3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B2975819-10CE-8648-BBA3-11E138701374.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B41D624C-AE0E-8E46-9D79-E0F0C902580D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B475A2E0-058D-0E44-89C0-3115240BF50E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B5B73E9E-534C-5741-9EAC-78DC8F7D605C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B627285A-5AF2-584E-AD40-E972CEC3CEEE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B7B34707-37BC-7945-AED7-F9391013697B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/BD526B22-39C1-8B40-B831-8DFECD38FC2C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C01134DD-6BE6-F34E-85EE-95812303C0B0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C1424713-4923-D74B-B50B-C844FE6E1CEC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C60D8417-6C73-4141-BD00-308AD1C5FAC2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/CBD9A15D-B8A9-7641-A4F2-C5DDB866D55E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/D83BEE03-AEBA-1E40-9F5F-E864AE024729.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/DE328194-E971-F64A-8476-1F9CC513BDF7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/DF7B291F-C468-544E-B82D-52D2A0E053B1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E0E54419-2A65-6A47-9092-5BB52A07881C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F06CB730-7CD3-0343-9070-517FC8FA14B2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F153C670-CF56-CF4D-9539-846ED97CF125.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F1F1C5E6-BB30-7F48-895E-7EF7BC123ACD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FB71CAB0-9035-294B-A8C7-6CEA1EB6AD79.root',
] )
