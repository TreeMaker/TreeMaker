import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/00CEA4E0-FCDC-EF4A-9763-E014F99F66DE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/06F7723F-5973-0D4E-B4CB-297E527D4FAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/076732DD-3DFA-3A4E-985A-9CDE2F1AF9CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/08056E40-61A1-644E-B2B7-DDF1ADF9DB68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/30EE862D-5B4B-F74C-81A1-A6FE35E34255.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/31400ABA-7819-3F41-84C1-C5E5C29E0ECA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/57180430-EB70-054F-919F-E661AD7FD0A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/5D5F551E-922B-C04B-B393-43B24D2BD2B4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/5EECB26C-1A41-174E-8DDE-E55B5C4F842B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/67992BBD-BE40-AC44-9CA3-39EB5BB9E628.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/6A25312A-CE69-5944-A65F-7378723BC01B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/6F332429-C80E-5C4F-B586-039459621108.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/B5C1D41A-E373-2841-B3FC-20CFDF4B8EAD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/C453AF42-19B5-AC4A-9F11-D3CA527F647E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/CE774041-6AAF-4C4B-B49A-E46FFD72CB29.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/DE7C78F2-205E-ED42-B04C-F7D2F5704CDD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/EB684F1C-736C-4D48-B36E-59C55E9317E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/EC675A79-1721-E44C-A95D-5D108A8B5402.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/EE9F2097-6660-8C42-A550-7217B29B22CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/230000/EED009C8-3EB2-524B-A2A1-A1BC79877555.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/01AF1A54-193D-3440-A2AF-FC561A2F5E55.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/021BA3B1-BB7C-1B43-999C-17F1E4A277CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/043E4000-D084-D747-B35F-ECAC16997464.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/0C383620-FF0E-F548-B83C-5450D71B6FEF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/10D4CD52-0A80-DA40-971E-D2C03E88686E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/169196BD-6B6C-C54B-A419-45EECDD5FBE2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/183D7F49-C90D-E74C-8C6F-26E00B3060AA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/227C48AF-AB22-9B43-AE64-0B9FB5DBD85B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/24A69712-5859-2248-8A45-3733E8B47828.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/3101C425-B51C-0D45-B058-B46B3E0E3FCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/334257B7-2FD7-AD4D-A2F5-D71BE8FBB09D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/3DAAE00F-8D63-EB4B-BD2F-59AB42EF08BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/41D0A717-9EE3-3943-B8C8-F075B583F0D8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/447C8297-7FCD-294C-BE6A-BD79AC3B4C30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/4A6A8367-A01B-6549-A48A-C5BCE427D830.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/4E873425-EE0E-4B49-9FB0-66604A17E8E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5470A2D6-1027-9642-939C-7BE87CAB94AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/56CAB9A4-3566-AE47-9D3A-E18A69CE58BE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5CB4D12D-CCBE-0241-91F5-607399584803.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/5F9A1F45-6CE7-2846-B898-448445A62B34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/6179B6DD-AF01-3243-8AB3-BE0155605D57.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/70D4DC4D-F338-8E45-83AD-2C9276BF7C52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/815D4BFE-4A07-6243-BA08-926C21999F44.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/82692359-1CF7-C546-902A-E32EEFB3C276.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8303A7F8-CA67-B845-9581-E2E1DEE0C929.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/852DA67F-33B7-C040-8E71-F4E52B404677.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/87E31C6A-8273-7B47-B030-3535D312A5F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8856B9FC-235B-1444-8767-33204A641BD9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8A18D25A-3B74-6D45-A6BC-0E93A7F8479E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/8CD02C2D-06CB-B644-A347-48040FE06511.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/976D7857-58F3-4A45-BB47-73FE16AC51E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/98D2C7A8-92EE-FD4B-8C6F-4B07DBE1D618.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A12B0A37-31A9-F445-A065-D6ACE3734E8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A1EB728F-EF03-EB40-BFA4-029A79512E5B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A200BF4F-ED92-FD4F-9FC3-A5719139500C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A30B977A-9121-B54E-A9E2-72B7FA053C6F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/A850351D-A28F-9841-929F-B74735D5C2F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B0676C6F-4392-CC42-A063-50D69790C240.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B14E878C-01BF-A348-AC51-9DAD9258C377.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B4EB04DD-625F-AB46-A917-E3BE0B69D15C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/B5D4B12A-6300-AC40-8BDF-9E9A0777DDBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/BCEA604B-4B03-A248-8A02-044B73804D14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/C082CE28-7C7C-9D4A-9F8A-29C596C79A3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/C7537E7A-A324-F848-A3BD-A947937BF82C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/C8183B09-8C7D-3442-A4F8-D185EA217F27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/CA044F9A-17C9-6B49-84F4-3EEE6BF8C234.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/CA1FAEEF-1750-5E4E-ADCB-BE55CBC09EE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/D83D6DEF-3196-8949-9EC5-265823C51732.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/D9D98D93-8A8B-AE40-9BC2-8AAC41224ADD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/E084B8FE-9446-A14A-9441-944FBEDF0DE5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/E21199D8-3EB4-8A4C-BD2C-9C846B15247E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/E91E9216-7055-6E45-AF13-388B5E2A1735.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/E99B8A33-F7DE-B246-B93D-D8DE5C0757F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/ED779AC5-D48D-D14F-BED1-104178802605.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/EDFF57B3-2E5E-9945-A199-ACB62CF64CE1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/F34EFF1E-55E5-1844-914E-415333BC3AF3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/F46D0C3D-7779-6A4F-94D9-D0DDAE5DE841.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/F6B97FB4-4117-224F-B84A-D66C3347D2DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/F747CC82-7426-6F47-A030-CAD87951EE0C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/FBFB57AB-04E0-EB44-B6E6-867B0A5920C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/FCBC5FC3-F75F-D545-9C73-91045BCF5679.root',
] )