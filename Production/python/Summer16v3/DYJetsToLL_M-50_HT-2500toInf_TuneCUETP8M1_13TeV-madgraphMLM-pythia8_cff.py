import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/0AA63BDC-02EB-E811-B3DE-001E67A40514.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/0C9D3C04-04EB-E811-8372-90B11C06954E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/1EBC8122-01EB-E811-82F6-EC0D9A0B3190.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/681178AC-E6EA-E811-BC4B-001E675A6928.root',
] )
