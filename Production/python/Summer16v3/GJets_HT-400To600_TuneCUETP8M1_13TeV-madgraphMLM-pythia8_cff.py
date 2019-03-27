import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0A8FE052-22EA-E811-A2CD-1866DAEB5230.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1A7DCC3D-1BEA-E811-B291-90B11C0BCE73.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/286D0271-18EA-E811-9D1E-20040FE9CBB8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/36F88B9B-11EA-E811-8D77-801844E560A4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/56C5BE8E-17EA-E811-9C90-D4AE526DF5F9.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5CFBB9FB-18EA-E811-8CDA-14187741121F.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5E8C4F32-19EA-E811-B097-1866DAEA7C48.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/605D16D4-2DEA-E811-8B28-1866DAEA6C40.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/62007BF8-18EA-E811-99DE-549F3525B220.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6AC75959-19EA-E811-8643-20040FE9CF38.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/78E3D619-16EA-E811-9D01-20040FE8E914.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/7A41ADC4-2FEA-E811-9C91-801844E561F8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/7E75FE03-1CEA-E811-8DF7-20040FEABE68.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/84B015D5-9CEA-E811-8874-B083FECFEF7C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/886FD522-1DEA-E811-BF9E-549F3525B154.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/96C99351-18EA-E811-A737-20040FE9AD64.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/96F81ADE-2AEA-E811-8270-141877411FCD.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A2947580-17EA-E811-A3EB-1866DAEA6E00.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A87841DC-19EA-E811-AE17-0019B9CAC0F6.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/AEA48A55-1BEA-E811-8A95-801844DEF100.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C08DB80A-1AEA-E811-BBB1-801844E41028.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CEACC20D-1CEA-E811-8D0F-141877411936.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D6E71CA5-19EA-E811-A1F7-90B11C0BD48A.root',
] )
