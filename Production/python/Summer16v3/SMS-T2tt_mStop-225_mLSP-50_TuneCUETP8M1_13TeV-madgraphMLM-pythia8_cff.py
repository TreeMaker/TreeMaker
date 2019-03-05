import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/3ABB0550-E3F0-E811-A370-24BE05C3EC61.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/582014A1-C4F0-E811-BD93-EC0D9A82237E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/62DB2CA3-85F0-E811-9363-EC0D9A8221D6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/86DC53F8-F7F0-E811-9D3D-5065F381E211.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/C071DD6D-7FF0-E811-B279-5065F3816251.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/CCEAB6D4-BEF0-E811-8EF4-5065F3818291.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/DCCD9BBB-82F0-E811-9626-24BE05C6E7C1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/E0A15E9A-9FF0-E811-A974-5065F3815281.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/FA9224DB-E2F0-E811-80D6-24BE05C38C91.root',
] )
