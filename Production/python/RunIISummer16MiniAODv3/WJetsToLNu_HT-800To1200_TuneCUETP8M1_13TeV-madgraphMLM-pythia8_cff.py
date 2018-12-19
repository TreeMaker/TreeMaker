import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/168414D3-21EA-E811-94BD-90B11C06BDDA.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3E2897B4-F0EA-E811-8788-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3EDA1DB3-28EA-E811-82FB-001517FAB928.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/44B37691-21EA-E811-A1B3-001E67D195F0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5EAFB975-0CEA-E811-BFCD-001E675A58D9.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/60280B1A-1EEA-E811-BDAB-001E67DFFF5F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/722B10D0-1BEA-E811-9ADE-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9CCE054E-1CEA-E811-A44A-A4BF0102572F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/AAD228B7-23EA-E811-93EC-90B11C06BDDA.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/B2CB750F-1EEA-E811-A75D-001E675A6AB8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/E4B866C7-1EEA-E811-8177-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/E86544BF-83EA-E811-A346-001E675A67BB.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F01382D3-21EA-E811-B905-EC0D9A04AE30.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F63D5866-38EA-E811-8931-001E67A3EA11.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FAB8699D-1BEA-E811-9358-001E675A622F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE44FB52-67EA-E811-8F0D-A4BF0101F533.root',
] )
