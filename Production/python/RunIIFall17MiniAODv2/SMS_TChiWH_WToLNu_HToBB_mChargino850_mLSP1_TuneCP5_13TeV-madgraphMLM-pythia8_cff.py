import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1E89EC18-B77F-E811-8AB3-008CFAF228FA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8A776EF9-CA8B-E811-9DB8-008CFAFBFDC2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1226D30A-6A72-E811-97D4-AC1F6B8DD1F8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1C50CE0D-6072-E811-88BB-44A842B4D8BE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/388654CB-6A72-E811-B2C0-A0369FD0B364.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/52C00BFC-6F72-E811-9344-EC0D9A0B3370.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5C37491F-6B72-E811-A181-6C3BE5A4D8E0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/70D56B92-5A72-E811-99B8-0025907254D6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/888D85CF-6A72-E811-B149-1CC1DE056008.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/A0FBB153-5772-E811-A17F-FA163E2A9833.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B6405B75-1273-E811-96AC-24BE05BD4F81.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F0B9BDEC-6772-E811-96AF-008CFA1111AC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F25FDC46-6A72-E811-BDEC-002590D60056.root',
] )
