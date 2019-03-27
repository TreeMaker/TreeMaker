import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/123D1E87-81EF-E811-8F4F-A0369F7FC608.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/3671EE5A-80EF-E811-9B80-008CFA0A57C4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/3CF5E040-BEEF-E811-9A21-B4969109FE2C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/445EDA21-82EF-E811-93B8-008CFA56D770.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/461F1595-7FEF-E811-BA3C-008CFA1CB73C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/4AE2DD41-7FEF-E811-AB71-A0369FC5E6FC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/62FB6F2E-7FEF-E811-8262-549F35AD8C24.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/82251B13-82EF-E811-AD45-A0369FC5DF9C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/94BCD204-BCEF-E811-8EA8-B496910A9A28.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/9AA4B98F-7FEF-E811-83A4-008CFA197A70.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/B2B57034-BEEF-E811-888D-549F35AF4488.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/C40CC04C-7FEF-E811-A3C0-A0369FC52134.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/C4D978A4-7EEF-E811-B34A-A0369F7F9EDC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/CA181630-7FEF-E811-AC4D-A0369F7F92D4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/CA6CC387-80EF-E811-9431-B496910A978C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/D00D950C-7EEF-E811-BC47-B4969109FDD8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/D08588C1-80EF-E811-A4ED-A0369FC5DF9C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/DC54AA36-82EF-E811-89F4-B496910A9A7C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/20000/E40F8194-80EF-E811-8C26-A0369FC51A44.root',
] )
