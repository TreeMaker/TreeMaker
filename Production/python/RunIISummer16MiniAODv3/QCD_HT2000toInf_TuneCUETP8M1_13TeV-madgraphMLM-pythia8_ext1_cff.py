import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/04518D5A-A2EA-E811-82A5-0025904B7C42.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0A0AEAE7-58EA-E811-AE77-0025905C5438.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0A48EC4C-81EA-E811-8A0B-0CC47AFB80B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/18929C91-57EA-E811-B075-001E67247CC9.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2EA695A7-28EA-E811-BF2F-0CC47AF9B23A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/325BA40A-58EA-E811-B169-0CC47AFCC6C6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/34C15A4A-36EA-E811-B858-0CC47AFCC40A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/380AE59C-57EA-E811-978C-0025905C5500.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/3E6C7599-08EA-E811-8DD1-0025905C3D6C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/42570AC8-23EA-E811-B567-0CC47AC57942.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/5EB4A2D6-17EA-E811-A09E-0CC47AF9B51A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/687A689C-57EA-E811-B94B-0025905C54DA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/7C039AFE-58EA-E811-8737-0025904CF712.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/80FE2C32-5CEA-E811-9456-0CC47AF9B2C2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/88867D36-5EEA-E811-A5F0-0CC47AC17678.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8CFFDFA5-8CEA-E811-AD80-0025904C656A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/960B7596-55EA-E811-B388-0025905C53D0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9671132B-F3EA-E811-8291-0CC47AFCC6B2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/96E02CB1-08EA-E811-B417-0025904C66F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9CB7C806-58EA-E811-B5CB-0CC47AFCC68A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/AC5B4F37-51EA-E811-9C05-0025905C5488.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B6BE7DC1-58EA-E811-A784-001E6724816F.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BCDC61CB-82EA-E811-A01F-0CC47AFCC6DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/C29772E9-10EA-E811-8A0A-0025905C2C86.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D2023208-5DEA-E811-83DD-0025905C3E68.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D2956A57-5BEA-E811-A5D1-0CC47AFCC626.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D64271FD-5CEA-E811-AFF3-0CC47AF9B2E2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D65E2199-59EA-E811-A16B-0CC47AC52E2C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D88C39D4-17EA-E811-8B33-0025904C66A0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/DC306D8A-3AEA-E811-AFC5-0CC47A713926.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E4DE5B28-1BEA-E811-8751-0025905C542E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/ECA215F8-5BEA-E811-80C8-0025904C6414.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F4006AAD-46EA-E811-9CED-0CC47AC52A94.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FA4DA594-49EA-E811-9592-001E6724804D.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/680B2880-FBE9-E811-8D63-0CC47AFCC3AA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/FAAFAA34-FCE9-E811-8F69-0CC47AFCC40A.root',
] )
