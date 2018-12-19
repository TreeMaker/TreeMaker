import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/00F0C9B2-45EA-E811-89FF-A0369F7F9EDC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/00F377A1-F1E9-E811-A619-0CC47AFB7D80.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/04E44FE7-33EA-E811-8215-A0369FC5DCBC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0AED124D-EDE9-E811-A7C6-0025904C641C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/12393DFF-BBEA-E811-A6F4-0CC47AFCC396.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2C4760EF-EFE9-E811-B59F-0025904C637A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3C32C857-F2E9-E811-9457-008CFA1CB470.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3E4588B0-F1E9-E811-A677-0025905C54B8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/76CC9F98-ECE9-E811-A1E7-0CC47AFCC6BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/84DF61D8-ECE9-E811-ADEA-0025904C68DA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8A59B45A-F2E9-E811-AE54-3417EBE4E882.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/90C51023-EDE9-E811-9C07-008CFA0F5040.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A695F42B-1FEA-E811-A0F8-008CFA152144.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A887FEBE-EDE9-E811-BF4A-0CC47AFCC62A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A8FD3C71-13EA-E811-8DD5-A0369FC5E530.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E2E1CAAE-F2E9-E811-83A9-00266CFCCDC8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EC918E3E-0DEA-E811-99B9-008CFA1C907C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EE113212-ECE9-E811-942B-549F358EB755.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EEED8DA7-ECE9-E811-BD56-008CFA1C6458.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F83D285D-EDE9-E811-92AA-0CC47AFCC396.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F8805579-01EA-E811-8A53-0CC47AFB7F5C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/FA1E7DFC-F2E9-E811-BF28-0CC47AFCC662.root',
] )
