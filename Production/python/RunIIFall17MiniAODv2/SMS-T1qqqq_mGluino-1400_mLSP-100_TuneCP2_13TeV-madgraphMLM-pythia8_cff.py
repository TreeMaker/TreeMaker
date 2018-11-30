import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0EA4CCA6-4DBB-E811-9645-0CC47AD98F74.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1AEAF0BC-4DBB-E811-A210-002590D9D8C2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/24D47265-4DBB-E811-8656-0025905D1E08.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/28FE3BA0-4DBB-E811-8235-48D539F3840E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2A34399D-4DBB-E811-9045-246E96D10F44.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3A34415D-47BC-E811-B66B-14187741136B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6A166CC0-4DBB-E811-80F9-002590D6012E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/70003836-67BB-E811-A9C9-A4BF010122D7.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7403379A-4DBB-E811-B36D-008CFA0A58B0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9EC7ABBE-4DBB-E811-92D1-0CC47A5FBE25.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D4C7FC78-4DBB-E811-9DEB-001E67E6F7D3.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E64B8C58-4DBB-E811-AB90-E0071B7A58B0.root',
] )
