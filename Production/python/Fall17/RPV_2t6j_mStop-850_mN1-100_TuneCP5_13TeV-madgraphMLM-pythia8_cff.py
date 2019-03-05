import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/047C71EE-2E9D-E811-AD7D-0CC47A010010.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3A56039E-2D9D-E811-B002-28924A33AF26.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/487325B0-2D9D-E811-8266-D067E5F914D3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4CC74BAA-2D9D-E811-BE0F-008CFA197E0C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/60C5C24E-2D9D-E811-BBBE-0CC47A4DEE6E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/70EC00B1-2D9D-E811-B940-44A842BE8F71.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/AA69CBB1-2D9D-E811-A13C-002590E3A222.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/BC263D94-2D9D-E811-9948-001E6779279A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C282B48D-2D9D-E811-ADE4-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C2C8F23B-2D9D-E811-9F2B-24BE05C616C1.root',
] )
