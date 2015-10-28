import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/00484E03-F37C-E511-9CDA-001517F807D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0098D5EF-F27C-E511-B881-6CC2173BBD80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0236C8FD-F27C-E511-B90B-001E67A3EB1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A28D2EF-F27C-E511-ACD3-6CC2173BBD80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0C0BE0FC-F27C-E511-B1C9-AC162DACC3F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/22607CFA-F27C-E511-BC84-C4346BC7EE18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26625EFE-F27C-E511-9083-90B11C050395.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/269622F7-F27C-E511-B4F0-0026181D28EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/289310F1-F27C-E511-8601-00266CFFC598.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/320D8C05-F37C-E511-B675-001E67A3F49D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/36AD10F1-F27C-E511-99BD-00266CFFC598.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38390DC0-F37C-E511-A83A-C4346BC8C310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3CF806F5-F27C-E511-B7EF-00266CFFC51C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E59DAF0-F27C-E511-B4C8-6CC2173BC120.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/400C91FD-F27C-E511-A33A-001E67A3E8F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4CDC7DEE-F27C-E511-851D-00266CFFC7CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E0AF7EF-F27C-E511-88A2-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5C3CDFEF-F27C-E511-87F2-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62DAD3FC-F27C-E511-8F50-AC162DACC3F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/68603A0A-F37C-E511-BCD0-001E675A6630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C18BCF4-F27C-E511-888D-00266CFFBC74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E3776F1-F27C-E511-BA95-00266CFFC4E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/707406F5-F27C-E511-A6E5-00266CFFC51C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/708588F3-F27C-E511-8DA4-001E67A3FE66.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/729D30F5-F27C-E511-B63C-001E67A3F3DF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C96F6EF-F27C-E511-A21B-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E97FDEF-F27C-E511-9728-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8413C7F9-F27C-E511-A55F-90B11C04FE0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86B9A306-F37C-E511-92A8-90B11C08CDC7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86E14708-F37C-E511-8DA1-001517F7F6A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92F06AF7-F27C-E511-ABEF-001E67A3F70E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/946A91F5-F27C-E511-9859-001E67A42175.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/98019CFA-F27C-E511-8EF4-C4346BC7EE18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A05FDAF1-F27C-E511-B3E6-008CFA051DEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A438BA02-F37C-E511-98EB-001517FAAB30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B43C5EF0-F27C-E511-A303-C4346BC076D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA3CCEEC-F27C-E511-A2BF-C4346BC8C310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC5C11F6-F27C-E511-BC00-001E67A3EA11.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E63B1E04-F37C-E511-973B-90B11C067ADE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA9AF721-F37C-E511-AF9D-001E67A42175.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE5001F0-F27C-E511-A15E-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F03776F1-F27C-E511-B82F-00266CFFC4E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0ABC4F7-F27C-E511-93A5-001E67A3EC00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F85518F2-F27C-E511-BE54-008CFA051DEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F893080A-F37C-E511-BCA8-001517FB2458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8DDBDEC-F27C-E511-A8D2-C4346BC8C310.root' ] );


secFiles.extend( [
               ] )

