import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/128FAF2A-3A9C-E811-888E-0025905B861C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1C6E4B07-479C-E811-B36C-1866DA85DFA8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/705688C0-5F9C-E811-A095-B8CA3A70A520.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/86539501-459C-E811-A163-AC1F6B1AF224.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/980EA80E-499C-E811-B293-0CC47A706FF4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/AA92DE16-479C-E811-901C-0025904886E6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B0B3B380-FE9C-E811-8DF6-FA163E2EDF93.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D2ADD639-359B-E811-B05C-0025905B85C6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E21C9F23-7B9C-E811-B774-44A842CFD64D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F88FA5A3-D89D-E811-A14C-0CC47A4D75F2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/04797607-D6A8-E811-94DF-E0071B6C9DE0.root',
] )
