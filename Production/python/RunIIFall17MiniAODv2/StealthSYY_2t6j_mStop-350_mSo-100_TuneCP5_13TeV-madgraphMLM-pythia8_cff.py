import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/363718C4-A0C6-E811-A041-00259075D702.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/80F0E8B8-A0C6-E811-9ECE-248A07C6D770.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D66AC1BA-A0C6-E811-B74B-008CFA1974DC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FCD20C86-A1C6-E811-AD47-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/703D3630-7FC3-E811-8A77-34E6D7E3878E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/74C27AEB-7DC3-E811-A903-0CC47A57D13E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/C8B4ED04-7EC3-E811-94D1-7CD30ABD295A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/02D76A15-61B0-E811-BEB4-AC1F6B0F6752.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/04655AE6-D8A6-E811-B6FE-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/200AF76E-61B0-E811-80BB-0CC47A1E089C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/2CEB0C13-84A5-E811-9536-00266CFFBCFC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/3293B835-61B0-E811-BFA8-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/542A3E00-19AE-E811-BD27-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5C81F760-61B0-E811-99B9-484D7E8DF0AC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/600EB50D-61B0-E811-81C9-C4346BC7EE18.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/606EF54D-62B0-E811-8586-0CC47A7EED28.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/729A1A92-81AD-E811-AEC6-008CFA0A57E8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/86116165-61B0-E811-9B04-1CB72C1B6CC6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/88D5A731-65B0-E811-ACE5-509A4C7288FE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/9035732A-61B0-E811-9033-0CC47AD98D26.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/90A95F10-61B0-E811-9E20-A4BF0112BC76.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/9C70AB0F-61B0-E811-8D1C-7CD30AD090DC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/A2E8954F-18A6-E811-AEA5-0017A4771058.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/A6AFA71F-61B0-E811-A394-003048F2E65E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B49749A0-53A0-E811-A7B0-A0369F310374.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B4DF9813-61B0-E811-B00E-0CC47A7C35D8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B8F55262-61B0-E811-891E-0CC47AFC3C76.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/BE04DF66-61B0-E811-9AB1-20CF305616D1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/BEC993A7-E8A5-E811-9F1C-44A842CF060D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/CE438EF0-D8A6-E811-95FB-0CC47AA98B8C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F0BAC709-61B0-E811-B44A-0025904B9B3E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F40A131A-61B0-E811-A791-008CFA197B14.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/FA31E619-61B0-E811-A35B-EC0D9A0B3080.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/FA33846F-61B0-E811-8162-0017A477045C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/FAD2FD83-AFAD-E811-91D9-FA163E6546AF.root',
] )
