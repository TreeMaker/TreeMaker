import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/02324F67-B7F0-E811-979D-A0369FE2C02E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/02799B04-BEF0-E811-9651-A0369FD0B1B0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/08B24B2E-B4F0-E811-80C8-AC1F6B0DE3A4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/1E56E935-B4F0-E811-B1AC-A0369FE2C1B6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/308E2A26-B1F0-E811-89E0-A0369FE2C204.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/32BDFD8F-B1F0-E811-B2AA-AC1F6B0F7196.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/3A184248-B1F0-E811-908F-AC1F6B0DE2AA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/3A4C48E3-CCF0-E811-B9C6-48FD8EE73A67.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/522B9FC9-B6F0-E811-9CFC-A0369FD0B15C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/54B6AAFE-B1F0-E811-9D7F-A0369FE2C204.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/7632AB49-B4F0-E811-A11C-A0369FD0B198.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/8257DBCA-B3F0-E811-9929-AC1F6B0DE33A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/843DF687-B2F0-E811-9D10-AC1F6B0DE3D8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/904D6C4C-B6F0-E811-AC43-A0369FE2C132.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/90A2637B-B3F0-E811-AEB9-AC1F6B0DE4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/9E0CD31D-C5F0-E811-A2BC-A0369FE2C132.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/A41B3722-B6F0-E811-BD7C-AC1F6B0DE3A4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/A42C15EC-D9F0-E811-B7FF-48D539F3887A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/AC4A9A10-B5F0-E811-80C9-AC1F6B0DE3F4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/B4B1D342-B7F0-E811-AEDB-A0369FE2C094.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/B61B9E98-B2F0-E811-A915-48FD8EE73ADF.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/B883FDCA-B1F0-E811-801C-A0369FD0B2F4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/C46222F5-B3F0-E811-93EA-48FD8EE73A8B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/D2A9D76E-B2F0-E811-B707-A0369FE2C228.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/DA8EE94D-B6F0-E811-83A6-A0369FD0B1AA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/DAB7D683-B5F0-E811-A794-A0369FD0B1C2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/E24AC224-B6F0-E811-9DAA-48FD8EE73A31.root',
] )
