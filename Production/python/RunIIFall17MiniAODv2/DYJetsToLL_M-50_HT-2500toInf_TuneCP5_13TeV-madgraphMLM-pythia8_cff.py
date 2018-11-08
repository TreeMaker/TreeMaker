import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/101378FA-6542-E811-8D96-0CC47A57D036.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/106ABB78-8E42-E811-B6C0-0CC47A0AD6F8.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/44ADB2B7-B342-E811-A551-0025907E343C.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/743897E5-9042-E811-9670-0CC47AA478BE.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/788242EB-C842-E811-8590-0CC47A745298.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/7A8F6FB9-9B42-E811-860F-002590791D60.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/9A9654AD-8C42-E811-8D80-002590D9D880.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/A05BE4AC-C842-E811-B629-002590D9D8AC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/F24AD99D-8D42-E811-A538-0CC47A0AD6AA.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/FA1664FD-8342-E811-B94B-0CC47AA53D64.root',
] )
