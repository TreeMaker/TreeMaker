import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/017048B7-C8FB-1C48-948D-4865313A65B5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/02FEFC40-A85B-4541-8C26-06B17EE64730.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/05A535E5-8654-5D4E-AA49-43170274AF9D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/05D88FBD-D3D3-074F-9392-A64812080447.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/101B79EC-4274-674F-A3B0-2F1595BF7E51.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/10FFA6D6-8CB7-AD4C-8EC2-15C693826B73.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/11E3181C-B69A-3B48-B942-DF3977558E81.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/15E35C6D-ACBD-D747-BFB5-3FC058AA1CAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/1705AF4D-FC69-734D-8D40-5A96D95052D3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/1CD20614-5CB0-EA4D-B00E-ACDEF6AEAA30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/2088171E-DBBD-7243-9178-FD3F43A490B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/20DA7471-283D-4349-8DE5-B3BADA03CA3C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/21E04362-AB01-EC4A-99C7-6F51BF3D1938.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/26E5B58E-EECF-104E-BBA0-9664529B4C41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/28885731-8CEA-9445-A4BE-A9C8B4DE853C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/2A12A99B-6EE0-E345-BDFE-3DB884BA5308.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/2ADBFEEE-EECD-C34F-9D72-D991917CCA74.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/2B30C855-C37D-3348-B3F7-B9ED4F728F18.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/2C8E1934-5E12-A141-B601-DC9BC2F794AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/2CB73508-494E-624D-8908-D0981D9CA5EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/33FBB4B4-DC5B-314C-A478-938B9FBD007E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/350DEA76-3DDF-2D4C-A0E8-984E7140568A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/368A59D5-BA16-D649-BD39-E5C8BE4AD876.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/3782BB70-DFD9-6A42-A30A-423A8DB79DF5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/3C51F0EC-CD55-314C-A319-360C7E6F4961.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/3DAF65C8-F8A2-9343-B872-B272A4364441.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/3E9DCD2F-E5A9-0246-8C24-76F3EE904AE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/4483C385-9914-B347-BBE4-4699DA90C3B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/48EA6ED2-1CE1-5742-A2B3-F2F8F735D0C6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/4B896E91-D7DD-EB41-8BF4-FB178DE843DC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/4FA49A8B-9168-E042-B0EE-529B8E694F73.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/4FD56076-12D4-0C47-AFAF-480A3C02D7BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/511BD679-D17F-7842-9D74-A4E4CBF2179E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/5125E363-DEFF-C54E-A2BB-AFD0281AC328.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/530BD393-ACF9-7144-A7BD-4B205FDBF871.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/531F3267-F074-A541-98E5-7B22AD886D37.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/56D1DAEC-6930-AE47-9688-835105935551.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/591FA629-01DC-BB48-AC4D-CE9F2B1CEF2B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/5D7CC93B-2368-9646-B31C-0D38CCF6558C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/6292F61C-C93C-204F-B34B-75EA6D99783E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/65F42D5B-EAC0-0642-A59E-AD7BD9A917E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/66399FD1-C5EF-0F4E-BCEA-37A040E77D4E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/67124B0C-C596-814E-BABB-5087EBE97E5F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/70C0A8FD-4D55-A548-87C4-909BA317DB0E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/72E79A77-F46E-6447-A541-CE3177F1D732.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7492B88C-B868-9B40-B5B7-3DB042CA2BD1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/74D9DB6C-2131-5241-81DF-B72032C971D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/79DDEA83-1C54-204B-BB6E-AC8BAA13A9D7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7A57E484-9FFE-FD4C-845A-F6E32551603B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7BAF7240-585D-9645-9296-B3DDAF282076.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7EC3C4FE-8E64-2F44-971A-366D09A298BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7ED80540-3BED-664A-98F5-4FF9A8FB716B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/806AE4DC-B88C-2F4F-98AC-2B192DBF0FEF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/83BD06AB-4C89-E449-9506-21B482AFF6CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/869CE606-6D74-9240-AE81-1CC270DCB8B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/8835CF79-757C-2048-A3BE-8BE37B0EE6B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/89D2C083-A9C4-5040-A193-F45A455A6A6E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/8A5E4F49-0CE5-5347-97A6-614D184C3AE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/8AAF27BE-B167-8148-A597-84246D1E469E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/8F5F49B4-9970-2C42-BF3F-7299CFE83B25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/93936EFB-F67A-4948-9884-CF30EDDBD5DE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/94405943-6CCB-104E-8C5C-45D57FFAE391.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/9560D6EE-4E25-3640-BD65-C2E62C0FB313.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/962F8541-A507-EF4A-AC1E-5D0E9A76DBC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/97789E2E-202D-3F49-AEE1-5937A34D1999.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/984919B0-5936-BF4E-A3CA-B05F9B0682D1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/9C0A2C7F-5B06-C245-96E0-7A81F4DC2DCA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/9CF097CA-3EF9-DD45-8B37-63C152DE0D79.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/9EA7DBCC-C086-774F-8E89-5095369E558A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/A6095F32-D3E3-E549-AEF8-17426C9873C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/A73ECFFE-368E-5342-A3DF-5430660F69EB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/A776B0A5-0EB2-594B-A1AF-9DDF698EB333.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/A87B834E-791F-664B-995A-0751DA8531B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/A955DAFB-6FBD-A141-BC46-593AF42EAD8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/AE2FB8BD-5BA6-7746-952C-BDEB038C6009.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/AF644377-3E57-B041-96D8-161920C8DE75.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/B0D56A36-BFC1-AB48-A5D3-BAA6F8E13E97.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/B502ED32-74C3-014D-B2A9-9D51FBCF26CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/B6B5FFEC-2FC6-9B42-AFC2-4BBAC19475AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/BA1AEF99-2AB1-5543-9486-A5D6857BE40F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/BCE4CFC0-0157-B14F-82B1-7CEEFBA2BC72.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/BCEAAB12-B18B-C24A-8327-A587F2A5E55E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/C0C7BDFD-E5D7-3643-8E1C-A6B002030262.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/C7241610-CCB5-6A42-A82D-D1707B93C88E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/CC14A7A5-BFE1-8B4D-B2EF-33FC22430314.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/CC755BF7-68CE-D04A-8350-D8B61C95AEF0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/CDC54AEC-381F-DD46-B4C6-3B03B6C6065D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/CE4BAB38-D3B8-384B-AAFC-57F510F57C0F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/CFC1130D-8321-1F45-9F8D-64BD9397B38C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/D4E3C80A-8E4D-0549-8760-B5CE8AB52B13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/D799E37D-A5FD-B34D-B67E-EFA72ECA51CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/D96947CB-DE2D-CC47-8A62-7D51A5BFD7C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/DBADF9A2-E549-EA43-BB68-4100B16EC2F2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/DCF1E0FF-6CD8-1E4A-B141-B04095F7EFBC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/DF5BB081-8E29-1341-8489-CA489BA96FC0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/E01FF1F2-EDF9-7B44-B7B3-DA20D8D58FFF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/E5E7B013-C999-D94C-A44C-FAF283C45451.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/E9570AEE-07A3-8A49-A64C-549E2FD44A25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/E98AF017-3375-3D41-9060-FA1A7B06AD59.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/EAE1032D-36A3-6D4B-B55E-EC90E4130738.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/F3682FE3-1F38-BB4F-AC37-26B4659E4B3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/F572B926-6537-8F40-8B19-B9EAA0526316.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/FAE69880-232F-A842-95FA-E01F45F1D9FE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/FCC52B45-DB09-E14F-B61E-CE821D5247B5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/FD0D9C90-775E-7F4C-8C67-920F1B48BAE3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/FDE342CA-9865-684C-9181-7D30DA315BC3.root',
] )