import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/2A0F4DCE-31CA-E911-9999-5065F381B271.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/58B388AC-63CA-E911-946F-FA163EAB5C97.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/6018319D-56CC-E911-8D4D-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/66D9E3B3-63CA-E911-9862-FA163EA2D080.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/68AA567A-5CCA-E911-B342-FA163EE2CDB4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/7A5683B9-0BC9-E911-8CA7-0CC47A4D7616.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/8674D0DF-FDCA-E911-B665-0CC47AFF02EC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/8CFCC33E-32CA-E911-83A5-20040FF47804.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/9AF04191-32CA-E911-9C8E-008CFA197D10.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/AAE201D1-A5C8-E911-A600-00266CFE797C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D2054CEF-63CA-E911-A05E-FA163EA35A6C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D662D967-34CA-E911-B8F2-0CC47A4C8E16.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/DC0A0CC6-63CA-E911-81FC-FA163E89AAF4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/DEE7C8AC-63CA-E911-8AFE-FA163E4FAD77.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/E62191EB-6ACA-E911-9A12-FA163EE381CC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/E8E3DC9B-32CA-E911-9CF0-24B6FDFFBC63.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/F851F5AD-A3C9-E911-B0F2-008CFA58074C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/FCFA687C-18CA-E911-87A3-44A842CFD60C.root',
] )
