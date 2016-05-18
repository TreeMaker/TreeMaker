import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1298E4E9-3CFE-E511-B7F5-003048CB8572.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3CFC7EE4-3CFE-E511-BB20-0025905A605E.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/54F75AD7-3CFE-E511-A84B-0025905B85EE.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/5A81A722-3DFE-E511-8F0B-0002C94D54F8.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/70CADEFE-3DFE-E511-8001-90B11C27EA38.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/AA229DF5-3CFE-E511-AE01-0CC47A78A4A0.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/B21AEB1A-3DFE-E511-9E9C-549F3525AE18.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/DCAAD6C0-3CFE-E511-BE8B-90B11C050371.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/FE00D5D1-3CFE-E511-9A92-000F530E4BD4.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/FABCA0AB-11FE-E511-B5B5-549F3525C0BC.root',
] )
