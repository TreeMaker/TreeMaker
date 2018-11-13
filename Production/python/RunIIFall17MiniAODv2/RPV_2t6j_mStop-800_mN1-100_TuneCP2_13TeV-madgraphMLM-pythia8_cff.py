import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/2C317306-EBD0-E811-BC67-0025905C3E66.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/5C278730-EBD0-E811-9955-20CF3019DF08.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/5E09BC26-EBD0-E811-B995-506B4BB16016.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/661B7021-EBD0-E811-A661-008CFA165F44.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/9699E629-EBD0-E811-BDB3-0026B92785E9.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/A4B54BEB-EAD0-E811-A0CB-20CF3027A61A.root',
] )
