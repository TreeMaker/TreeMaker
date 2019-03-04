import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/00B90BE6-B0A2-F544-82E2-7D755FAB971D.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/0EDEABB9-09C5-1844-83F7-9A19A5760C63.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/10602129-4EB9-F546-94F9-D36EB0F4040F.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/3F9C6252-BB9B-F04C-9BAA-1F92D72CFC81.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/4124CC01-C885-B747-87D7-0D70FE4B5495.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/55EE7C13-384F-E548-BD00-091206E43760.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/6655767A-5BAC-7B4D-BA66-0100CCB96FC6.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/6E770B6C-780C-8941-A001-6AD6F65BD666.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/7056266F-EC8E-DA4F-8A85-D44B8043A205.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/736E02F1-DE88-F045-B6FB-E330803A5898.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/73EC817D-40FB-F14D-B738-F63458391D85.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/7758D2EE-FD95-3346-8502-C41A270A15C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/778417C8-AE67-6846-9EA6-755185C79FE9.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/78609BD5-83A6-1B41-82D1-EFA653B1F106.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/7AD9806C-4FBB-C041-87AF-EF767315784D.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/886B9D5B-54FC-2E40-860C-CC3B787FCBD7.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/8F3BD21E-1682-5D4F-BFD9-23DCE628943B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/9470DC2B-0B55-8D4F-917F-083ABADC19EF.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/9DFE1EB6-CE97-B44C-8778-3461877A6776.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/A6847EC3-A643-E54D-8F58-3C0A82545B88.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/A9DDF812-463C-7C41-9F9C-C604C8E8DEA4.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/ABB3CB39-E7AC-194B-8CDD-BBAA18335905.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/B6959C7A-7640-E44B-AA96-89A76BEC86D4.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/BBE2C6F7-4493-CB45-96FE-B8A4DCB5BB9C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/BEEEDEFD-A832-0446-8664-435414ADD4D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/C025F4C2-4A3D-604D-91C8-95A840C8A44C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/C7600AEA-1B22-4C4B-8F1A-B1D6C8EF52E5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/CAD358DA-DC7F-7140-AE93-16B0218D555B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/DC7696D8-E06A-AA4E-8C4B-8CB0391ADF6C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/DE5F7507-3497-CB48-9912-1BF6B7BF28DB.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/DEA11505-16D9-0143-9AF6-EA9B9AA118CB.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/DF35E476-2E69-F742-B8BD-A4D82D2E0583.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/FD396911-EECE-7940-BA4D-EEB6F45F0E42.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/A4788EEA-F867-8349-985B-21AFDB0C9543.root',
] )
