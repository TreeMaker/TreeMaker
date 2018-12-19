import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/16BA8BF9-74F0-E811-8296-A0369FC5DCBC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/18CB5EA5-7EF0-E811-8551-A0369F7FC0BC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/18E96D70-77F0-E811-9CCA-B496910A9828.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/1E0AE710-73F0-E811-86B9-B496910A9790.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/385EFA1E-6BF0-E811-B656-B4969109FE30.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/4A1AF27F-80F0-E811-BF41-008CFA1C645C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/4C8BA6C6-CBF0-E811-87D2-A0369FC51A44.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/58ADFBA8-89F0-E811-BA9A-B4969109FE30.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/5E62BAD5-83F0-E811-A3D1-549F35AC7E08.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/6A0E3615-B1F0-E811-85F7-008CFA197FAC.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/6AB2E98D-90F0-E811-9A5C-B4969109F68C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/705D8C27-76F0-E811-A20F-A0369FC51A44.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/785A437F-CBF0-E811-AECD-B4969109F628.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/7C85C6AE-99F0-E811-8BC4-B496910A0554.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/7E55F783-A3F0-E811-9211-008CFA56D770.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/7ECFF907-80F0-E811-9B12-A0369FC52630.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/7EECD79C-7CF0-E811-801B-008CFA197D98.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/9ECE3F11-2AF1-E811-89FC-008CFA0A5614.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/B2BF7122-74F0-E811-8EEA-549F358EB7D7.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/B8854851-9DF0-E811-9923-008CFA1C907C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/C6378510-C8F0-E811-9B38-A0369FC5D5D8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/CE39C5C7-76F0-E811-8CD3-A0369FC5D5D8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/DE5FB792-97F0-E811-8679-A0369FC5B7B0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/80000/EE7DB4CF-9DF0-E811-9D6F-A0369FC5DCBC.root',
] )
