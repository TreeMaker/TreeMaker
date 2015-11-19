import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/10B71C5C-6780-E511-BAF7-02163E00F33C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/16335AD5-6F80-E511-B71E-0025901D16AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1A449DBE-7480-E511-82A9-002590E39D8A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1E8B1568-6780-E511-A82F-0026B95BE32C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2029AAA7-5280-E511-9964-02163E015CC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/246B1EDC-6D80-E511-AAEF-002590E3A286.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2687DD56-6180-E511-9133-02163E00C65D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2E5AF371-9B80-E511-8F7F-02163E0115E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3075A5BB-5F80-E511-9F83-000F530E46D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3624E510-7F80-E511-9422-A4BADB38ECBB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/38EFC89D-5F80-E511-B6B7-AC853D9F5256.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3C8A8FDF-9980-E511-86EE-02163E00F4F7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3CF65002-5980-E511-81B4-02163E00EABD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/48120B7D-6F80-E511-B06F-00304865C45A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4EABAD88-9A80-E511-8228-02163E015034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4EE91249-4B80-E511-9929-0CC47A13D0F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/50920EDF-6D80-E511-AAB6-0025900E3502.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/527E5BB1-7480-E511-94FB-1C6A7A264D4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/52C41C9D-5980-E511-A6F0-02163E00C4C9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/64DEF7A0-5D80-E511-BAB9-02163E00C65D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6A65DFBF-5B80-E511-8C6B-02163E013A27.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/728D2D43-4B80-E511-9B97-002590725380.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/787422F9-5880-E511-A04E-02163E016BCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7878D38E-5E80-E511-85B3-02163E00F3AD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7CD75063-9A80-E511-BDCC-0025904B2C4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/84AF623E-9B80-E511-9788-02163E015DE6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/86C532B4-6A80-E511-B995-0025901D0C68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9638067E-6380-E511-99DB-0025901D08E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A090CA83-4180-E511-96C7-02163E00AD3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A8AD55CD-6580-E511-AB58-02163E00CA84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/AA0617BD-5980-E511-A61B-02163E00C65D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B29583BC-6A80-E511-8E90-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B6CC21E4-6480-E511-981B-02163E00C65D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B8328304-6280-E511-A3E0-002590E3A0EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B8DEE60D-6280-E511-80A2-0025908653C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C6C24175-5380-E511-8E71-02163E00CA84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CC507082-6F80-E511-8A44-00304865C456.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CE7EDE38-7080-E511-A43C-842B2B185470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D827FD6E-6380-E511-89C4-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DA10A5B2-6980-E511-BEEC-003048F5B2B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DE1F80AB-7380-E511-8013-0025901D08D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DE54016D-5B80-E511-BDE4-02163E010FDE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E8626C48-6680-E511-BBFE-02163E013D0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/EAE03892-6180-E511-954F-02163E014E64.root' ] );


secFiles.extend( [
               ] )

