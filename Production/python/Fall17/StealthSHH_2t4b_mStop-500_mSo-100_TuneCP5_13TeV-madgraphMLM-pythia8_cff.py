import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/62BE0429-BCA1-E811-BB38-EC0D9A0B3340.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/001C827F-BE9D-E811-8E00-002481D2495A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/18419165-BE9D-E811-ADFE-A0369F836392.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1C836681-BE9D-E811-BE9D-009C02AAB554.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4418DB6D-BE9D-E811-807B-0CC47A4DECD6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/5A446268-BE9D-E811-B840-0CC47AF9B2D2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/5A4B7FC6-BE9D-E811-BA0A-0CC47A0AD742.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/681C29E3-BE9D-E811-823E-008CFA197E8C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6CE32E86-BE9D-E811-BC3D-0CC47A4C8ECA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/92DA1D6B-BE9D-E811-A6FD-1866DAEA7E64.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/942D8D83-BE9D-E811-8543-1866DA87D585.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A2BA808E-989D-E811-8C29-E0071B749C80.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/CCE1302B-6E9D-E811-B182-A4BF0112BBF8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D6F8D884-BE9D-E811-98CC-001EC9ADCB45.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D81EC7BE-BE9D-E811-8815-D4AE52E7F60F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E622648D-BE9D-E811-A5CD-7CD30AC03006.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FCE7EFDA-BE9D-E811-AA72-0CC47AD9908C.root',
] )
