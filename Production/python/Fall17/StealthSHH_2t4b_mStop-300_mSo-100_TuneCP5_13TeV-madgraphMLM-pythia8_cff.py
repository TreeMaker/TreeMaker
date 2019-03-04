import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0056E4BD-029D-E811-A734-24BE05C6E7C1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/30BDAEA9-069C-E811-BD36-1866DA7F9265.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3CDE71C1-629C-E811-9934-0025905B85C6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5C7DDA1C-AD9C-E811-A27F-0025905B85BA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5E903BC9-029D-E811-931C-0CC47A78A446.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6A429BFC-169C-E811-8751-549F3525DD6C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/72B86E1D-839A-E811-8238-0CC47A78A2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/78016D04-359B-E811-BA38-EC0D9A822626.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7851F255-A49B-E811-8A9E-0CC47A4D767C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8440DDC9-089C-E811-A073-02163E017FB2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/86B44B2A-B59B-E811-958D-0CC47A7C34E6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A40090D2-029D-E811-9D40-0CC47AA53D60.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/AA5F8AC8-459B-E811-817E-0025905B858E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C6A87A40-839A-E811-8E90-0CC47A7C3610.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CED7853A-039D-E811-BECF-FA163E650EAE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D6A301BE-029D-E811-B2D0-001E67A406E0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E0389A54-7B9C-E811-83C4-0025905B85C0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F4ABA4C7-029D-E811-B4D2-3CFDFE639AE0.root',
] )
