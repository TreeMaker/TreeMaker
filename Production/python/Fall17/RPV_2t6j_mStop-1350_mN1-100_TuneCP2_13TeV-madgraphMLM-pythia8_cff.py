import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4E75EA62-E004-EA11-8B09-24BE05CEEDB1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/56569187-E004-EA11-B3D5-3417EBE706C3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/660D1C8B-E004-EA11-AC84-6C3BE5B5F210.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/74E1FA79-E004-EA11-9912-00259094F2BF.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/7CC2957D-E004-EA11-B052-AC1F6B595EAE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C070E43F-58EE-E911-B67C-FA163E99B13A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C6D42FBD-E104-EA11-A9C3-FA163E7BCE3E.root',
] )
