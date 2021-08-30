import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/7A82B4ED-DECB-1040-8640-094409083B22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/828252BC-64CB-9340-B5E4-8D8886776F3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8AB8488C-6AFB-D644-85B0-0B2C6F9D8ECA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8E3099EA-CBE0-614D-B47D-65173DF5480B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/B6539F48-9BB1-B148-A0B1-A8E7E7CABB5B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/D5739357-6A6B-D14C-86D5-023186C8A597.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/E22B07C4-E33C-7C42-8107-1A3883E82300.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/F496F6B6-53A0-ED4A-BBEA-549D2EF112DF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/F5D1A804-251A-3A47-A29A-D3174AC66119.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/1240AC34-80E5-054A-9FB0-A745E94A5757.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/131AB7BF-E4A9-674B-BFE2-CB0596393164.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/14F5C7A5-7A85-4947-9D92-FAF4C63610C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/1A294155-5A91-D840-8970-5D762E8393C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/1ACF2141-A20C-D44F-BC71-24EE5FCCBBE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/232FEE98-1C03-554A-AC3E-AE46D5C31DAE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/23F85F22-1EED-7B46-96BA-27A42A7C4E84.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/2820FDCB-447D-E442-8528-99AFDA48A5C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/2F09001C-E447-D142-9B01-3FCC72F2962E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/318F41BC-4F3D-A242-986E-5F0B96DAD663.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/32D941AC-D3ED-9145-A633-7B95D52F50D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/35802EF5-EAAB-E540-A1B4-FFFB5DBBA6B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/3D3E9237-F5E3-C942-84D4-86521295483A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/3E22D181-D914-EE4E-96E4-6F4B7FEAF9BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/3E980216-E746-DB49-8D29-007DEDABB6FC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/40AAA330-1718-D94A-B18D-903569A5E2CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/42D1C8B5-643B-624B-8BA4-7FC04FC78536.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/4A7160B1-9AB4-174F-8AF7-CAF8B355B0E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/4CCE5E7A-0BC1-104D-BAC5-FAA87E9D004E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/4DD0D40A-78C7-0142-83A7-D6C0D057339A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/4E326188-E3D8-914F-862A-A792029326A8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/4F37C9DA-F46E-924D-B0DF-9930A66243BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/4F97A904-1F54-F545-B895-16671C810936.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/5C910F2C-ED07-1745-BBD8-C77B5666078C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/6AC2A7DA-5386-2942-A81D-AD23730ECFDF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/6B611474-029F-DB4F-AD8B-935FAFAD1B13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/6F5E9118-A4C3-FC4F-96FA-BAA93D213B69.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/72DCBB74-39B0-7146-B5D4-B4EBF2846BDD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/75CA134A-51E9-E549-ABD3-6E737A8CE4FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/7808AE18-610E-A14B-B6FE-6C414CB14A9A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/7856DA2D-7790-B648-8F5F-663C3A803135.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/78AA00C4-9F67-174A-B282-F28A5404A3AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/7B6B8F92-E69C-F145-93E6-B0302AA775DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/7BA407DB-AA60-6546-A167-6AB502F1F0A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/7CB384EC-DD5A-254A-A6D5-5BF91D0493BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/82A0550A-7629-9345-BDA0-CA3C92E863A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/8AA1AECF-1730-2243-8E49-6F7E0E2A1BDA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/8B5AAE4C-268A-4C40-8A94-E0FE28715EB4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/8D069431-8EAD-3C4D-B8B7-B995F3476484.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/8D0B3916-EBB9-C744-9488-23F592B436FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/93F7E018-C2DE-5C45-8FB5-61322ACD0A51.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/9AB812B3-8148-3449-A517-95C14A5F757E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/A6CDB333-AB62-5E41-9BBA-D322CC78FF56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/AB43ACEE-A19D-9249-AB4E-939FD58FF31D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/AB817B38-68BB-EE43-8E1A-B6C60451C8CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/AC8DD955-6803-F04A-90F0-DBD5F27DE0EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/B5FE0CE0-4E62-EB48-8C05-847DA6149B85.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/B6D6785F-71BE-4A48-AD74-685E9A9F8EFC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/B87F4DA9-3398-A14F-94A0-F1C9DADEB1FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/B8B8C22E-290D-3141-9DE0-ADF48C8222C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/BA56FEEB-76AA-0349-9760-682436091549.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/BFFBEDAE-8B23-2044-88BE-335F66544645.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/C357695C-8A90-934F-B832-AD6D48D1BD0B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/C37351E5-24DA-834F-B129-FBD8655DCDB2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/CCC874E2-F255-3F48-B00E-6DA444AA55DC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/CE91C9B2-7E70-CE45-B184-885B0E2C0ACE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/D9AC7AD7-B22B-154D-9247-BEFBAAD55BF8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/DA70BE0E-6716-FE4E-8804-D08F556DE2D3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/DC0E41C1-141C-5648-BCFE-8C0BDBB0408C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/DC566A63-B287-384C-B62D-024CD34D6C40.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/DCDD675D-3FC8-2C49-B76E-575D856D3CE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/DD5F58C8-6207-F74B-A93A-D104A4F06CDE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/DDD1054D-89CC-4E41-A607-DFB024507FC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/F3D00EC5-7F56-3946-9603-F2DD34BD61E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/FDB1042E-0A23-B34E-B3AF-848EAD21A0F3.root',
] )