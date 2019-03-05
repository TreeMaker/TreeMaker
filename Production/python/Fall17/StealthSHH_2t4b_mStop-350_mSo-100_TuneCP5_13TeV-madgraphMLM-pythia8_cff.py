import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/04E50EED-DA9B-E811-A08C-1866DAEA8230.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/08BF8B5A-6698-E811-BCDA-484D7E8DF0ED.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0A96D578-DB9B-E811-A5FF-D48564593FAC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/16B49A85-849C-E811-903A-001E677926C4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/344740F2-DA9B-E811-ABD7-1866DA7F9556.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4246BFC5-DA9B-E811-95FE-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/48958EB0-DA9B-E811-9796-0CC47AFB7FFC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4C3227CC-DA9B-E811-8D69-E0071B7AC700.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4E46F915-DB9B-E811-A6B2-D067E5F91B8A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/50695B36-0A98-E811-92F0-3CFDFE63D360.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/52895538-8E96-E811-B2B5-0CC47AD98F74.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/58BF223A-DD9B-E811-A4B8-6C3BE5B5F210.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5E0EB88A-9198-E811-980B-008CFA197B14.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/606F04B7-DA9B-E811-86DF-FA163E683B83.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6C8CFA5F-DB9B-E811-B11C-002590E7DE70.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7CCB3DEF-EE98-E811-BD96-1866DA87AB73.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8236A959-7495-E811-96C4-0CC47A2B04CC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8246B837-2C9A-E811-974E-5065F38122A1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/84596BDD-DA9B-E811-B845-0CC47AD99044.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/84E5F671-BE98-E811-B735-001E6779245C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A05666C1-069B-E811-8DD8-0CC47A7C357E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A8E4F6DE-DA9B-E811-8C10-0CC47A57D164.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B8BA0666-DB9B-E811-9291-1866DA879EDE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BA0F67B4-DA9B-E811-AF61-A0369FE2C11C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BEB3B9C8-DA9B-E811-A250-0CC47A4D75F6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C01915B5-DA9B-E811-A5EE-00266CFFCAC0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CABE83C9-0396-E811-8853-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E8D2EB56-9C99-E811-849B-A0369F836392.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/EA742669-DB9B-E811-B25B-0025901E5556.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F0D1B355-DB9B-E811-AE3A-0CC47A5FA3BD.root',
] )
