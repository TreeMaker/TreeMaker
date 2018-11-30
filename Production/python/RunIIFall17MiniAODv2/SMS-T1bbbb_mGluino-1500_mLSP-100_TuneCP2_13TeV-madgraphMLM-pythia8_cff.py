import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/928761F8-FEBB-E811-AFF6-14187764311A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/A6E03FF8-FEBB-E811-AC19-001E675051BD.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/AA5F33C8-FEBB-E811-B080-0025904C637A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/B2FFF2D3-FEBB-E811-9A32-A4BF01026229.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/C0F23EAA-FEBB-E811-BC9B-0CC47A7C3628.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/C8E7BAD1-FEBB-E811-B944-06A0A80001E6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/D41F42FC-FEBB-E811-AD6C-90E2BACBAA90.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/DECA62F9-FEBB-E811-A30D-1CC1DE1CF610.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/EC30D800-FFBB-E811-80E5-F4E9D4BC8B50.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/F0A973B1-FEBB-E811-AA16-0CC47A6C1866.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/F6B09FD2-FEBB-E811-AEC8-0CC47A0AD4A4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/F8DDF2C8-FEBB-E811-B1DA-A4BF01158DB0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/FED95D57-FEBB-E811-BFE5-E0071B7A48A0.root',
] )
