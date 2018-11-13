import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/183B8745-DBBF-E811-A2AB-44A84223FF3C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/3EB64248-DBBF-E811-BAF2-008CFA1CBA20.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/40530244-DBBF-E811-9248-002590489776.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/828A5A59-DBBF-E811-998A-1866DA85D88B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/B8D76651-DBBF-E811-BA1B-D8D385AF8994.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/DCE71348-DBBF-E811-B125-0CC47A7EEE32.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E605124F-DBBF-E811-9B58-248A07C6D770.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/EA091ADB-DABF-E811-BD9D-EC0D9A8222F6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/FC560A27-DBBF-E811-8070-0CC47A7C3410.root',
] )
