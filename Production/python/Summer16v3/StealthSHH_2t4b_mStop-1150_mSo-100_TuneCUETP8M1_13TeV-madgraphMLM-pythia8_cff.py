import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/0AE4DF54-5005-EA11-9842-00266CFFCC7C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/1022DECB-5005-EA11-8228-A4BF01287DD9.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/22FA4E4E-5005-EA11-A6EA-0090FAA584D4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/3C70E7D4-5005-EA11-9BA0-8CDCD4A99E08.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/3EFA7281-5005-EA11-AFB2-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/5898C4BE-B805-EA11-9473-509A4C838C16.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/A20AE06D-5005-EA11-ABC0-FA163EEC1F05.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/B24942CB-5005-EA11-9459-44A84225C8FF.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/D0CC6552-5005-EA11-B954-0CC47A7C360E.root',
] )
