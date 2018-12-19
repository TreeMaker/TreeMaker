import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/28D1E302-C3F4-E811-8546-901B0E542756.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/56270CDA-DAF4-E811-88F4-0CC47AFC3C9A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/5AF598C3-BFF4-E811-B210-001E675827DC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/709FF0F8-EAF4-E811-A198-485B398972FC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/80BB6CB1-A3F4-E811-A715-901B0E5427B6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/82836BF6-EAF4-E811-983D-0CC47AFC3C6E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/9E80AB74-B9F4-E811-9E4A-0CC47AFC3D34.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/C0F6DB3E-B3F4-E811-82FA-246E96D117F4.root',
] )
