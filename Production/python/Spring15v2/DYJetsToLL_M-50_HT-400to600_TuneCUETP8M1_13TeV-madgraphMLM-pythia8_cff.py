import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/10052FD5-DD76-E511-8188-002590D9D88C.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/2045F4C4-DD76-E511-8861-002590FD5A52.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/5E8162E8-D676-E511-B93B-002590FD5122.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/707660AB-D776-E511-AB61-002590FD5122.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/72C9E8E5-DD76-E511-B1B6-003048FE40E2.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/7AC1A381-DC76-E511-9B03-002590D9D8BC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/8855F7CB-DD76-E511-8C2B-002590D9D9BC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/9CF0C58B-D776-E511-B72E-0025902BD8CE.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/BA959B90-D576-E511-8158-002590FD5122.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/C8EB02C7-DD76-E511-AA43-002590D9D984.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/DE2B7AD1-DD76-E511-87F6-002590D9D894.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/E0DF3BC8-DD76-E511-B089-002590D9D8AA.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/30000/E8C6C57D-DC76-E511-875E-002590FD5694.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/0CFA5DC9-2877-E511-876D-0025901FB188.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/182C88B6-2877-E511-AC8F-00259048A87C.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/365A7D7F-2877-E511-A3B0-002590D9D9DA.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/4090A8E1-2877-E511-98A5-00259029E670.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/4282B27F-2877-E511-A2AD-002590D9D8B4.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/56C3AEDD-2877-E511-98D7-0025901FB438.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/5AC8DCCE-2877-E511-ABC7-002590D9D8B2.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/6423829C-2877-E511-99AB-002590D9D8BA.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/704041DC-2877-E511-98B2-002590D9D9DA.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/743EABA2-2877-E511-B81E-002590D9D880.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/A69A0BC8-2877-E511-99D5-00259075D702.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/C4921099-2877-E511-9BF0-002590D9D8C0.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/DC7E05A5-2877-E511-9B5F-0025901AC182.root' ] );


secFiles.extend( [
               ] )

