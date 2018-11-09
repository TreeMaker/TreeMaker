import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/0200586E-5BD0-E611-AEE7-D4AE527EDE00.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/04A3D96A-5BD0-E611-8B9B-1866DAEEB0C0.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/0E755D0F-5CD0-E611-A840-141877411FCD.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/1E09B5AC-87CF-E611-8AA9-C81F66B7910D.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/1E2749DA-58CE-E611-8EC6-C81F66B78749.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/22389D71-4ECE-E611-A54F-549F3525C380.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/2E89F0AE-87CF-E611-A79D-1866DAEA8190.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/343CCCDB-5BD0-E611-9DC9-A4BADB1E6031.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/3463FB0C-5CD0-E611-A1CB-14187733AD89.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/36749EB6-53CE-E611-B72E-1866DAEB296C.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/3AD381AE-87CF-E611-B955-1866DAEA7E64.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/401A8A91-50CE-E611-AC7A-141877411C7F.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/46DC0DAE-4CCE-E611-A08D-1866DAEECFDC.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/5056A176-7FCF-E611-B2D6-D4AE527EDE00.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/54E38367-5BD0-E611-943A-90B11C0BB9FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/68B3C544-4BCE-E611-B69C-1866DAEA8190.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/70BCECB0-87CF-E611-902F-B083FED406AD.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/72F4E479-56CE-E611-84E4-1866DAEEB0A8.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/7465E855-4FCE-E611-BD3B-1866DAEB5C94.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/74C7CC1C-51CE-E611-A13E-1866DAEEB358.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/887D03AD-87CF-E611-BC38-B083FED18596.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/96340E12-5CD0-E611-9CA9-14187740D279.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/A627C60B-5CD0-E611-A21F-141877411936.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AA3811AD-52CE-E611-8625-549F3525C380.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AEE253C8-13CF-E611-92B9-001C23C0F203.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/C4095FBB-87CF-E611-B977-842B2B42BC3A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/C6B49498-55CE-E611-9702-B083FED42FB0.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/CE252F2E-88CF-E611-A289-001EC94B51EE.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/D6747449-54CE-E611-8519-1866DAEEB358.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/DEDA3774-52CE-E611-A275-B083FED046D9.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/E2019355-4FCE-E611-B827-B083FED42FB0.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/E2DB1704-51CE-E611-A222-842B2B17F73D.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F4650866-5BD0-E611-9A9D-14187740D279.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F4765F67-5BD0-E611-A13F-90B11C0BB9FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/FA0D2612-5CD0-E611-97F8-90B11C0BB9FC.root',
] )
