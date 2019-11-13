import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1A72164E-7E35-BE48-93F4-51B6A56AB387.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/23B7582C-CFFE-D047-9D90-B1AB20E8460E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/242F17FC-CCE3-5247-B6E3-F9C60EE0BB0E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4EDFE926-072E-4040-AD2A-72590327AE44.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4F1426AD-286C-264A-8329-ED7EA04FB16A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/50A822A2-174A-AF4E-A9E7-41D0481B49F4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5732D25E-2B0A-1B40-AC97-666DA053D583.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/690AEB5F-B848-1742-8BBC-E00DFCFEB3F4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/75B39567-D8EB-8248-9A2C-12C82E92D5C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8662C5ED-186B-6040-8927-EEB9B38DD1E8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9C4895D2-E2A6-684D-8A47-1DE03CC307A3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9F03752E-18A7-7A43-BF64-F4F322FEA017.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9FDE3C91-1555-AD48-98E5-ED50217D992A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A389E8D9-B7FC-BF46-AC66-8E6BAA7EE586.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A7966514-AA81-364A-A6BE-1BC66A1110C2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B79AC8B5-B6DB-EF4E-8FCE-59702DDEE86E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B86B69C9-E654-FA48-8552-EF1E2B6CA7B2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B99ED273-F20A-114D-8BD1-CAD86C32B048.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/BF155687-9CB8-9B40-BB4E-D957D42026B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C40A5067-2A58-0847-84BF-F54A8B722CE2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CA0F1C9A-BE60-0541-9329-15AADA5E05C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CBB08FA3-1757-B64C-8503-CB42D0102C0E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D2BB86E4-82D6-7645-8F66-3FD9DEA64463.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DB32F19A-7DCA-CB42-A4DF-89C93A910167.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E8BDCF1D-0976-2C43-8857-186C589D584B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F2BF0D96-1981-F942-A9F2-48AFD121D453.root',
] )
