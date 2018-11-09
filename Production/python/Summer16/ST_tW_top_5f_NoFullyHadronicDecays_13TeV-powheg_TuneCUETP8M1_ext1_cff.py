import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/028F1002-3FD0-E611-AFC1-0CC47A13CEF4.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/0C004A24-3BD0-E611-9B48-0CC47AD9901E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/0C27776A-55D0-E611-8B99-0CC47AD98CF0.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/224FC4B5-51D0-E611-A1A0-002A6ADFC615.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/28750924-3BD0-E611-9118-0CC47A13CEF4.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/426BC02A-3BD0-E611-BFE9-0CC47AD991FA.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/42C53D53-5ED0-E611-BE5D-001E67456EBE.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/4EF61961-5AD0-E611-9664-0CC47A13D416.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/6C47633F-50D0-E611-9E6E-002590E1E9B8.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/6EEE000A-49D0-E611-A128-001E67586A2F.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/700BA6C3-4DD0-E611-85BB-002590E39F4E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/7AE257FE-3ED0-E611-BCB8-0CC47A6C063E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/7CD1BC16-58D0-E611-93A0-001E673476AA.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/7CDF0C61-41D0-E611-A53F-002590E3A224.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/909C254A-3CD0-E611-A9A2-90B11C2C93C9.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/A0E5D955-3CD0-E611-B9D3-0CC47AD98F64.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/A23143B1-42D0-E611-9102-0CC47A537688.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/B258AD6A-3DD0-E611-BFD9-0CC47A6C138A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/B425AC6A-3DD0-E611-95BE-0CC47A6C138A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/B687BD20-53D0-E611-B456-0CC47A6C186E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/C2A45D29-3BD0-E611-8E38-0CC47AD991FA.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/CE1205F5-57D0-E611-8782-0CC47AD98C5E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/D06F241C-3AD0-E611-BD27-0CC47AD99144.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/D257C056-56D0-E611-AD2D-001E67456F68.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/DCE09197-3DD0-E611-9E12-0025904886E6.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/DE4F7221-53D0-E611-A1A7-002590E3A0D4.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/DEE130E9-53D0-E611-90BD-001E67346BA1.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/E0497BE4-53D0-E611-B583-0CC47AD98C5E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/E4C4AE05-58D0-E611-8C60-0CC47AA98B8C.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/E6EDC93D-3ED0-E611-8A56-001E674DA1AD.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/EC43839C-56D0-E611-B6B1-0CC47A13CD44.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/F02EA024-3BD0-E611-A4CB-0CC47AD9901E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/F2254433-3AD0-E611-981B-002590E3A0FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/FA12586A-5ED0-E611-ADED-0CC47AD98D6C.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/FAB418E5-53D0-E611-B30E-0CC47A13D16A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/FEA37089-3CD0-E611-9DE9-0025900E3514.root',
] )
