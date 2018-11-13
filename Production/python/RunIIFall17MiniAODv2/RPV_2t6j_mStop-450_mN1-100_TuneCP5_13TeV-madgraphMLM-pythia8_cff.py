import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/E801732C-6CC0-E811-8FF6-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1E5D1D8F-4F9E-E811-92CD-F01FAFE5CA86.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/58731943-4F9E-E811-91C8-A4BF01158DB8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/66BB6FD7-1E9D-E811-BA7F-E0071B7A5650.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/729D7444-4F9E-E811-9FB9-00266CFFC4D4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/7AB4DD3E-4F9E-E811-B5CD-FA163EE87181.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/86F7BD2A-9E9D-E811-A84C-FA163ED01A68.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A8A40071-4F9E-E811-8504-E0071B6C9DD0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/CE2F2D4D-4F9E-E811-9FA3-0025905B85EC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E86A65E8-4F9D-E811-90EB-00266CFF0AF4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E8839C86-1F9E-E811-AA55-0CC47A7C34B0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/EC701405-899D-E811-9852-0CC47A4D7658.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F6485557-C39D-E811-AB6C-0CC47A4D762A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/1C4CD9B2-A7AB-E811-9E8A-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/FA2CA0FA-88C0-E811-B555-0242AC1C0500.root',
] )
