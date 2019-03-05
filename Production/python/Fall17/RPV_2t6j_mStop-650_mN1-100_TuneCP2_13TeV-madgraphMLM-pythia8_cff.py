import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/505ADE8C-E7D1-E811-AC52-001E67DFFB31.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/6A46F100-E7D1-E811-B0C4-008CFAE45310.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/9047CAFB-E6D1-E811-ACB4-002481CFE708.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/ACA19A00-E7D1-E811-9767-EC0D9A822626.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B4444EF2-E6D1-E811-812B-F02FA768CE6A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B6CADF00-E7D1-E811-98B5-0CC47A13D3A8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/CCD33BFE-E6D1-E811-904D-1CB72C1B6CCA.root',
] )
