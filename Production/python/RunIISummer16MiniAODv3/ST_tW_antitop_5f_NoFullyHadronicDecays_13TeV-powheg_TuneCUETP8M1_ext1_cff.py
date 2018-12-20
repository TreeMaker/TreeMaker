import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/020C77D9-FEE9-E811-9E8A-A0369F63681A.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/0EEFA156-FEE9-E811-9910-3417EBE52651.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/2A7C618D-FAE9-E811-A43B-3417EBE5048C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/2AA67A02-FCE9-E811-8508-405CFDFF481B.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/2C2659B4-16EA-E811-8FAE-44A842B4CC7E.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/30FBAF7E-0DEA-E811-8206-44A842BECCB1.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/3C991D34-0EEA-E811-BB64-B496912ED83C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/42BAF09C-1EEA-E811-8AAE-F04DA2754190.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4860352B-04EA-E811-A090-44A842B4D8CB.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4EA0A3C1-18EA-E811-8F4E-00266CF8337C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/507FF0CD-15EA-E811-896C-44A842B4D8D8.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/62A43A61-0BEA-E811-B021-A0369F5BD8D4.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/66E58062-01EA-E811-906B-44A842BECCBE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/7AAB55C0-21EA-E811-865C-A0369F63681A.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/7CB704E8-00EA-E811-AE04-00266CF85C48.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/808B9A24-01EA-E811-928D-405CFDE57581.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/82F6E2CF-18EA-E811-ADDE-3417EBE46601.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/88A90AB7-0FEA-E811-9B72-F04DA274BB9C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D04056D2-82EA-E811-ABCA-44A842BE8F7E.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D67E501D-1DEA-E811-8AC0-00266CF83638.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D8E42FD9-FBE9-E811-862F-10983627C3DB.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/EEC72072-0FEA-E811-9A4F-44A842BE7718.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FACDC30E-0EEA-E811-82C5-F04DA274BB9C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FE34AE30-19EA-E811-BC97-44A842BE770B.root',
] )
