import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0200E718-05EB-E811-8973-002590FD0F36.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0C268868-94EA-E811-89F9-C0BFC0E56866.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/34249529-7DEA-E811-9933-90E2BAD492E8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6E32513B-85EA-E811-BED4-68CC6EA5BD22.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/BC473756-85EA-E811-82FE-002590FD0F36.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C2DEBFE0-8EEA-E811-AF4F-90E2BAD1BDF0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D2A4903C-A0EA-E811-AAB0-1CB72C1B65D4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F837F38A-81EA-E811-967F-0425C5903030.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FC8A6AD6-80EA-E811-A0D5-0425C5DE7BF2.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FCF1B48D-86EA-E811-B2F5-18DED7C60DEB.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE23274C-81EA-E811-A0C1-C0BFC0E56846.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE519E60-81EA-E811-B7B9-68B59972BF62.root',
] )
