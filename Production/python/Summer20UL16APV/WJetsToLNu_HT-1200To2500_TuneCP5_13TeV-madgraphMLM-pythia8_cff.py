import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/00E2B9E4-E227-1248-A24E-455ABD42B75A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/06F6E28E-E217-AF43-81E0-95777A2ECF8B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/0D9DB228-7CFE-824D-B1EA-1E1A7765365C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/22765A92-747C-6344-A1AA-BCA46126BDFC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/2F3DFBB1-4959-574E-AC83-1BABF145965F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/2F78A93F-9086-9744-BEFA-BF3199E9DE0F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/30894BFC-3137-404F-BCEF-C272A52CC3B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/3C9ACE6C-9F6B-474F-8BFE-F85D069A64BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/47C9FE3C-B5B0-9C48-A026-1AC05CE5E7F2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/58CEB73B-A604-7449-AADF-B7EA72A923AA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/59BD720B-3796-E243-9CFF-1D288B3B9338.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/71772DA1-F07A-E741-AA41-09713BED0097.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/7FC6C53A-75E7-4841-9DBE-F9423E014090.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/804EC5C1-F8F1-4843-AFCD-53418AA49D29.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/83BC0AF5-3112-CA43-B358-3A891A3A48FC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/8BE367F0-94A2-9748-8C72-186740DE7F54.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/8C798795-E928-EA43-8741-7D6D62D34487.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/B071FF8B-438F-8748-887A-C3A99B8BB3A1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/B36449F5-3FC3-A94B-BE47-422DA4F40908.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/CA8531B5-56ED-3344-86B5-266B96CA7A87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/CEC9DED4-496F-B048-8609-253922E175C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/D5967296-4D41-744C-ADFF-3912E0B5513F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/D943C2E7-D45D-1141-A5B3-7E7A76E9DC9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/E80346BD-9C13-DF4A-99D4-A426B16DB817.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/EE66DF6C-96FB-444E-8DC1-14556409507C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/F57EE650-7B3F-334F-BCD8-47EBD3DB6BA0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/00000/FCCD1AA3-FD11-5041-A821-0E8CF3E5A936.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/140000/0680F7C3-C76A-E14B-9E01-430BDE56E51A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/240000/C25A1450-5B95-C64A-A5DC-456ADBFEDF61.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/01ACD492-076E-6243-AED3-C4690CEB50B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/08AD2637-5EC3-554E-B5EF-3F545ED71383.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/115A30B3-045F-7845-9BD4-2F79F5E0854D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/115BBDDE-AF0B-594F-ACBA-0C2B3CF47AF1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/1759B106-A4CD-E04A-B328-B1529AEB5E27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/183461BA-C256-1649-9594-2CB0F29254A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/1E588625-1710-014D-AE05-077C8CF2CD0C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/2B1A82E6-E655-7B4A-8D95-A30EFCFD0779.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/383462EC-C769-2747-86DC-46D7451BAA2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/3B791C7D-D845-134B-BA19-6DA8D632F32F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/3C01CFED-4C30-4548-9025-6421905CCCDF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/3EA8F7B5-0E09-0B45-8684-87CD24270163.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/4C17AB11-A17B-A649-9032-C986324BBEE2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/4CBC44C5-6BFF-E844-9C9D-AD378505CE52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5649C5D5-02F9-6E4D-BA7E-CB68908229E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/594FE70B-6364-564C-9DF6-83908365837B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/59D78251-CED4-8F45-A611-3A56A2D61DBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5AC85CB8-F7FA-E349-A991-18771DC48067.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5B9E913B-FF57-3442-890A-27CD7A52CE90.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5F68B2DE-1935-7D4B-AE9E-71D73DF74D4E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/6AD03AF6-F067-7F46-902B-0DF564AECFB4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/7870774E-EF67-B84F-94E3-7A2AEF589F06.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/79189681-2B69-C140-9180-A36E03BEFE77.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/824F6703-F85D-764C-959E-88C6B62A6310.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8908F5F2-0ACE-DA40-A290-4247F36EE150.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8AE3DEF6-40B1-C041-A6F0-8F8839FFD2D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8D8B40E8-0CC3-2D45-8357-6683CA6099DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8FE8F55C-E103-4545-A023-A816319A9D6F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/9113A95D-F74F-B045-812E-4A46DB592F51.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/918B9EAE-E859-5048-A1E4-9723A974828E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/9FBF3F4A-175F-BC46-9408-9AC00E4E3205.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A290161A-6707-CD46-9CD5-BE33377FF6C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A7B19800-3D43-564B-8612-01D21C90B9BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A9EC6D60-1504-9640-9902-6D50EB352E43.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/AB193E03-80CE-9C4E-A516-B04F300DDC9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B1256DB3-CADF-6B44-A984-82A7D1AB79D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B83C2498-5058-8E49-90F3-46C03AC7B529.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B91FC203-EEBB-6047-97FD-1AB33CC4FB6B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/C627233B-44A2-4E40-9C58-1C0CE513A23D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/C8CE872D-B80B-6E4A-B4BA-2E0BACEA6091.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/C9DC8438-7364-4049-8898-35CBC3CA149D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/CC614D97-C00F-D54C-961E-565E3E97FFB2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/CEC81976-8AC4-0C4A-BCBF-5FDD713421A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/D115B016-7880-3B4B-9602-219958F66988.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/D7052477-356C-3A41-8BDD-8A5A93F91AF1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/D774AD70-E69C-9A48-8085-ABAA7A3921C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/E395D354-8B09-4F48-B420-52AA522F9464.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/E5A8DBEE-6881-4740-8B0B-5A6C9717C120.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/EA5AEBFB-A821-A64C-8C69-7754AAB4977B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/EC0E41E3-9976-9A48-B8BA-727C4DEB03B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/EEB47EBA-D2B0-2245-8D15-5ABFE4C45DDB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/0C652B0D-46EE-1A41-8D5B-FBBB0A2B03ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/0EEF8906-AAF5-6B46-A380-FCC8DD4AAB4E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/105DEAB7-18DD-6943-99E9-E48D8A0B756D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/1280E2F2-C10E-364E-ACE9-45B6D8D68E24.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/1B5344F7-1C56-624C-ADDF-AF34A3E6FDD9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/22844078-5E39-2647-80EA-5263570DF43F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/33F7EEA7-B0CA-4649-81C1-B5DF2D0D7E7C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/3DC708AF-4963-E048-BA7A-3448C1DE508A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/3F905CE7-FDD2-CC48-9884-2999360FE025.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/432EC3AD-CCD1-5446-9F36-A46E0552FE14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/483B9202-6A8A-9F47-B84C-86477A994897.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/4D31F6F0-A0BD-FA4E-A2FC-ACE1B6BFC51C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/543EE405-F642-1E4B-96EC-5CE46970EDE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/56755A57-457F-6648-BBE5-987487081A9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/6A2C5937-6976-EA4B-9C27-518D339DBE2A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/6CA13C3C-E907-574E-9FC1-3D5F43D55CF8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/7B38CFC5-2195-C742-AFC3-5BEB656363BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/7ED037C7-5733-504F-B461-603700BF462F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/90E2414C-AE6D-AB42-90AF-DB2C9F139029.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/9DAC6AF2-9E7B-3445-8302-69A59AB9CC2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/9EFA5C64-6388-074B-957A-7BEC4C046CEF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/A350BCA1-8B33-654B-9ED3-BC807683A160.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/AB4C4B53-3357-244A-BC63-5A921ED7A245.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/C511134F-4F68-F048-B53B-E6E55257200F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/E375DD94-146E-E342-93D2-182BF0DE0C54.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/E6488D82-8AAE-D448-9B5C-A590F30E0322.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/40000/F3E77B6F-B36A-0C4C-8037-8A68FF310954.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/70000/5F52BF61-06D6-3B4D-AF2D-CE73B711CEE2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/70000/61D7AE47-2252-B645-B769-E668FDAC81F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/70000/E3A28083-FD21-0340-97B1-3385D09DB852.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/70000/F6255998-F989-9C43-8397-FBD7F17706DC.root',
] )