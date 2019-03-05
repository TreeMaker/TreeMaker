import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/02AF3277-10EB-E811-82F6-001E67DDC0FB.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0CDDCB89-EBEA-E811-AE3C-0026182FD740.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/12B5B69D-13EB-E811-9FAF-001E67DFFB31.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/30EBF5A2-16EB-E811-B0E1-001E67A42026.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/50A962A7-03EB-E811-8A2A-90B11C08AD7D.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/70B42905-13EB-E811-B4ED-001E67DDBFC5.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/7828D9B7-0CEB-E811-B514-001E67A3E872.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/8AC4D659-0FEB-E811-8102-001E67A3FD26.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9CC4486E-76EB-E811-A8BA-001E67A3EA11.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/AE98FC47-12EB-E811-8777-A4BF01027688.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/BA9AA21A-13EB-E811-BFE4-D4AE529D9537.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/C42F2ACA-0AEB-E811-AE9E-A4BF01025568.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/C643351D-0AEB-E811-BAF3-001E67E0061C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/CA9095F2-F6EA-E811-BA98-90B11C0701C1.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/587058BF-63EA-E811-9B28-001E67DDCC81.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5E4CCD18-5EEA-E811-82BB-001517FBE024.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6C7D52BE-62EA-E811-A98B-EC0D9A0B30D0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7034C67E-78EA-E811-9AA1-A4BF0101202F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C43C80A8-65EA-E811-8CB5-90B11C06CD59.root',
] )
