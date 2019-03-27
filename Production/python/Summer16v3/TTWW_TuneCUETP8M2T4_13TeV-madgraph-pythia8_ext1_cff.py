import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0A26881D-8F32-E911-BCA9-0CC47AD98BEA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2C96FB80-8F32-E911-B019-00259019A41E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/34658862-9532-E911-9019-6C3BE5B594A8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3869A2AA-8F32-E911-AF3F-0090FAA57EA4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/4894B53E-8F32-E911-85AE-002590DBDFE2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/50FB9CF1-8F32-E911-B714-008CFA0A5614.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/58690FB5-8E32-E911-8E91-44A842BE8F7E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/62F63D03-8F32-E911-9A96-008CFAFBF4EC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/7A5FCA2C-8F32-E911-B505-1CB72C0A3DC5.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9023BDE1-8F32-E911-AC09-38EAA78D89C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9800A015-8F32-E911-96DA-A4BF0112BD22.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9EDA2523-8F32-E911-9391-0CC47A4C8F10.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A4725A14-8F32-E911-8FAA-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/AC9BF2DB-8F32-E911-A5DE-ECB1D79E5C40.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B29725D9-8F32-E911-90EE-1CB72C1B6574.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B2C0F620-8F32-E911-8093-90B11C518DA4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/BACF5212-8F32-E911-A4B2-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/BCB93318-8F32-E911-B62C-24BE05CEDC81.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/BEBD35CF-8E32-E911-A288-AC1F6B1AF05A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/D8CA51F5-8E32-E911-9CD8-0CC47AFB7D60.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/ECBC78DB-8F32-E911-A9D4-246E96D14C50.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/FC756CE3-8E32-E911-B404-FA163EEEB0C7.root',
] )
