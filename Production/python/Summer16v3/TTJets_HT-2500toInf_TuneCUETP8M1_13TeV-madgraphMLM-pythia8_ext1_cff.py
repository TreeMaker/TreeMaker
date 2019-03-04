import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/00B41873-BCF0-E811-958E-68B5996BD98E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/029889C0-B3F0-E811-AF3A-00269E95B128.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/0A01E44D-2DF1-E811-97D7-0CC47A5FC679.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/1CC25AFB-C2F0-E811-B379-0CC47A5FC619.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/522CF353-E6F0-E811-BEA7-002481DE47D0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/621E3C17-BFF0-E811-9883-B499BAA67C7E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/7866B6CC-B3F0-E811-AB40-0017A4770440.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/880F491E-F3F0-E811-B7B7-90B11CBCFF4E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/9296D144-B3F0-E811-B139-6CC2173D5F20.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/96E86EFF-C3F0-E811-A438-0CC47A5FBE25.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/B453441F-DCF0-E811-817C-6CC2173C4580.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/CE88BBEA-C2F0-E811-9A59-0CC47A5FBE35.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/D859590C-C4F0-E811-BEE9-0CC47A5FBE31.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/00000/EC072C59-B5F0-E811-9E97-0CC47A5FA3BD.root',
] )
