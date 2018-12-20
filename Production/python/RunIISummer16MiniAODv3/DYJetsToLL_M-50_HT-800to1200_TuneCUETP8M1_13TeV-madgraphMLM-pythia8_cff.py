import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/2E0B064E-42EB-E811-8A64-0025905AC822.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/F4311B5E-76EB-E811-BCDB-0025905C4328.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/102D3808-DAEA-E811-B57D-0025905AC960.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/12594F61-D7EA-E811-A06F-0025905C4470.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/142AFAB0-E6EA-E811-BF1D-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/181A8CDA-DCEA-E811-9148-0025905AF57E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/1EC5EF44-E5EA-E811-A20F-0025905C22B0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/3250BDB6-CAEA-E811-8374-0025905AC984.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/44D6FFD7-37EB-E811-BF21-0025905C42D4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/4856D54C-B4EB-E811-B38A-0025905C4328.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/4A2B8887-18EB-E811-BB8A-0025905AC804.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/563F7574-E2EA-E811-8BB4-0025905C446C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/6A39E214-CCEA-E811-8E46-0025905C446C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/7A88793F-C9EA-E811-96F4-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/7C292231-27EB-E811-8003-0025905C446C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/964D6A7D-DCEA-E811-B805-0025905AC822.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/A6D48C9A-E7EA-E811-999B-0025905C4270.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/AA3AEC31-1DEB-E811-9B10-0025905AC984.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/B6850683-3CEB-E811-A4A1-0025905AC804.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/BCB3A74B-E5EA-E811-914C-0025905C4270.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/C07A568B-CCEA-E811-A2A9-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/C2A6E272-DAEA-E811-A79E-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/D611E117-CCEA-E811-95CC-0025905C4270.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/DA528487-E2EA-E811-B097-0025905C4270.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/F6105ABF-36EB-E811-924F-0025905AC822.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/F8E6A5BE-22EB-E811-94CA-0025905AC960.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/FA06AB69-D3EA-E811-9BFD-0025905AC97A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/FEE7E8BA-40EB-E811-B72E-3464A9B95FF0.root',
] )
