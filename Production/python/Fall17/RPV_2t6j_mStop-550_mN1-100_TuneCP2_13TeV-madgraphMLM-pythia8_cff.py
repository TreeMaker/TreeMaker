import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/38B81DDD-A1BF-E811-84F6-001517F7F410.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/608DC49D-4CD3-E811-8816-90B11C2CC96F.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/86AB7099-4CD3-E811-8667-EC0D9A0B3360.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/8E6394D5-CAC1-E811-8429-0CC47AD98CEA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/9C6CFB96-4CD3-E811-B534-E0071B7A8560.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/CE662596-4CD3-E811-8B43-0CC47A4D75EC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D05FBFA1-4CD3-E811-A0DD-008CFA110C88.root',
] )
