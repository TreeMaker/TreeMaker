import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0AF58F62-43EA-E811-8885-0025904C66EE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0CCBB66B-5EEA-E811-845C-0CC47AFCC372.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/124E4D7A-67EA-E811-AD8C-0025905C53A6.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/20549E9C-62EA-E811-8EC9-0025905C96EA.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2EA8A384-5EEA-E811-8AE3-0025905C2D98.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/4C52D8DD-62EA-E811-9D2B-0025905C4264.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/4E822284-5EEA-E811-942A-0025905C4264.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/5CABD6C2-61EA-E811-B378-0025905C53A6.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/7857870B-69EA-E811-8AC5-0025905D1C54.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/78D4C690-5EEA-E811-9C6A-0025904C66F0.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/7C19802E-69EA-E811-A160-0CC47AFCC6EE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8436B7CC-5AEA-E811-A2D3-0CC47AF9B2C2.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/86D9816E-62EA-E811-B250-0025904C6226.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/88458C99-5FEA-E811-8CF6-0025905C2CE8.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8E12E5FD-6AEA-E811-A0EB-0CC47AF9B2CE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A8336143-69EA-E811-ACB3-0CC47AFB81BC.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B0568998-61EA-E811-8484-0025904C4F9E.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B64DB3E1-5FEA-E811-BB19-0025905C54B8.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/C6486E9C-61EA-E811-B68B-0025904C540C.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/CA233CC0-68EA-E811-9059-0025905D1E08.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D862E23B-5EEA-E811-A24F-0025905C548A.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D8B7F2B4-61EA-E811-AB2C-0CC47AF9B1DE.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E42C66C0-48EA-E811-B81D-0CC47AF9B1D2.root',
       '/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E4D5021B-62EA-E811-9370-0025904C66EE.root',
] )
