import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B29DBFB1-4305-EA11-9804-1866DAEB1FC8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D4284944-92ED-E911-B898-FA163E549F72.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F6F239DA-4305-EA11-9F7E-AC1F6B596094.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F88433EB-4505-EA11-BA23-001CC4A65D70.root',
] )
