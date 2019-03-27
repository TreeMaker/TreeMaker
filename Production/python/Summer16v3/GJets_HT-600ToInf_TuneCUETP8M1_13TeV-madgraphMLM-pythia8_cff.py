import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0AFB2CC8-F9E9-E811-A2B1-A0369F7FC954.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/2C95520A-43EB-E811-A143-B496910A8098.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/343A6480-FBE9-E811-AA55-549F35AC7E3C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3A63A001-FBE9-E811-9F59-B496910A8AC0.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6051E30B-43EB-E811-87CE-A0369FC51BB4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/62FFF8F9-F9E9-E811-987D-B496910A041C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6AD67781-45EB-E811-9D2C-008CFA582D78.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6EA301FF-FAE9-E811-8918-008CFA1CB8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/7203260F-43EB-E811-826F-008CFA197D8C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/7624FADC-FAE9-E811-83D9-B4969109F68C.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/78E55365-FBE9-E811-BA98-B496910A9820.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/983EEF9D-F9E9-E811-A8A9-A0369F7FC954.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9EBB1AF4-F9E9-E811-9ECE-B496910A8AB4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9EFF0246-F9E9-E811-8ED6-A0369FC52134.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A44D3E29-FAE9-E811-94E7-B496910A9A68.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/BA796B10-43EB-E811-B3D6-008CFA56D770.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C2317D52-F9E9-E811-9256-B496910A9088.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CC0DC8A8-F9E9-E811-B128-A0369FC52630.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D4372306-FBE9-E811-ABE0-A0369FC52134.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D48B109E-F9E9-E811-BA42-A0369F7FC954.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D48F7D4F-44EB-E811-9A07-A0369FC5E0A4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/DA84CC95-FBE9-E811-A8D5-3417EBE480D1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EA81E08D-FBE9-E811-978B-A0369FC5B4F4.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EAA5B758-F9E9-E811-9BC6-B496910A8098.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EE695D21-FAE9-E811-93B2-008CFA111200.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE9D5228-FBE9-E811-8F9D-008CFA0A59C0.root',
] )
