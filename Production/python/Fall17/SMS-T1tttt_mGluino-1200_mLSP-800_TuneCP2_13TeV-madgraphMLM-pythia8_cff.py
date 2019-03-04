import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/06D76A6C-00C0-E811-88F9-3417EBE47FE5.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0C473239-00C0-E811-AD6D-44A84223FF3C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1039BF00-01C0-E811-B5DC-002481CFE5C4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/208DC021-0CC0-E811-9AFA-7CD30AD092FE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/22079B0E-00C0-E811-91BA-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2248C318-00C0-E811-BE06-A4BF0112BE0A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/263A9E48-F0BA-E811-B629-E0071B7A48A0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4E0F3342-00C0-E811-A626-44A842B420F1.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5036E84F-00C0-E811-BE4A-EC0D9A0B33B0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/54234507-00C0-E811-84CD-0090FAA57FE4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5A90BF14-00C0-E811-9B38-0025905D1D52.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7800A23F-00C0-E811-88A1-002590E7DFD6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9E11CA2B-00C0-E811-B38B-0CC47AD98BCC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9E1EDC25-00C0-E811-BE61-008CFAC93E3C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9E7A3048-00C0-E811-A8D9-44A842CF057E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B4AF510A-19BF-E811-90EF-001EC9ADCB45.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BCAE3447-00C0-E811-81A4-00259021A28E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C4E27C86-00C0-E811-99B0-002590908236.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F85FC767-00C0-E811-9E0A-008CFA1CBA20.root',
] )
