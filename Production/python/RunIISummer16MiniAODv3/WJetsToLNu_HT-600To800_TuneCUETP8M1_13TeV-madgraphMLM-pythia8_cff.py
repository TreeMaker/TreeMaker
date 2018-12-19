import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0C43DBF9-F7E9-E811-9B03-A0369FC5E8FC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/14F2D26F-F6E9-E811-87CD-3417EBE5E7F3.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/16B1D0A2-F5E9-E811-B4CC-008CFA58074C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/18AE36A3-F4E9-E811-AA52-A0369FC52630.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/1AD9358F-F5E9-E811-835F-008CFA56D794.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/22B1EF65-F8E9-E811-8723-008CFA0A5808.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/36A7B785-F7E9-E811-A696-B496910A8A6C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/38C3C297-07EA-E811-8762-A0369FC5E49C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/4000EAEF-F7E9-E811-A097-008CFA197D38.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/40DF3659-2BEA-E811-BF15-008CFA1C64A0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/4657DB7C-F4E9-E811-AE8B-A0369F7F9EDC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/48ABBC81-F4E9-E811-8F29-A0369F7FC4E8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/4E6F9B41-22EA-E811-9DF2-008CFA197D2C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/52C0D365-F8E9-E811-BF6D-008CFA1CBB34.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/54FA9C87-F4E9-E811-B000-A0369F7FC5BC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/5674DEC9-F4E9-E811-AE0E-B496910A85E4.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/56F82EAF-F4E9-E811-B6FF-A0369FC5DCB8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/58139B36-F8E9-E811-ADF6-A0369FC5B848.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/5AC9BBA7-F4E9-E811-9C83-B496910A9A54.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/60B2AEF7-F4E9-E811-A6B7-549F35AE4F61.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/6401903D-1BEA-E811-9163-008CFA0A57C4.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/647DB8C9-FEE9-E811-BC10-549F35AE4FE3.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/68B62571-11EA-E811-9D8B-B496910A01F0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/725DA01F-F6E9-E811-BE1D-008CFA1660F8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/7CD7BFFC-F7E9-E811-8679-549F35AC7E22.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/90F07B37-F7E9-E811-9EC2-008CFA0A5808.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/96C48C18-0DEA-E811-BB7D-B496910A01F0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/BE09EAE5-F7E9-E811-AFD6-B496910A9A54.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/CA1B7DD8-08EA-E811-B630-A0369FC5E49C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/DC9D78F0-F7E9-E811-A3F5-B496910A8A88.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/EA319D87-F4E9-E811-BBF6-A0369F7FC5BC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/EC30B338-F5E9-E811-A6AE-008CFA1CB73C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F80CFB8F-F5E9-E811-AE84-008CFA198258.root',
] )
