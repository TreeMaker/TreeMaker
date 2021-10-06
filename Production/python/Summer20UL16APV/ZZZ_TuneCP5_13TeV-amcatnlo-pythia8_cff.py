import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/BBCF67A3-751B-DA43-BC70-8FD0A654049F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/05A54AD6-B1F5-B44A-BA3F-F1F1DF0AEE41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/46E61904-1CA7-4543-BAE2-B044189ECF0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/4BE50409-87D3-1B48-B0D0-C3530F5EA56A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5341A068-F409-BF4D-B3BF-1101EF90BF6A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5BD7C96D-E90C-3B44-9EDB-CD69410D05AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D818B247-59B9-9246-ADB6-AF7EE37AC03F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/34BF7A31-B3E2-2145-9427-942D4F901C6B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/46870146-1A78-7C4B-A64A-F937F76A1E14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B0D4A2F4-BAC3-FB46-B9B6-FF8A4910B3F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C0793DBD-9F4A-714F-A674-41640D2B3134.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/BB637610-0F3A-D04B-9500-88AA18D4398D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D30FA486-5ACF-8D43-8FB5-01A300F45360.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2179BCF9-B5F3-D545-9B1E-561AED94E9A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CC941E27-4BEA-1A40-91EF-F1317A0E1999.root',
] )
