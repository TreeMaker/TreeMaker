import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/140000/3020FD3D-EE39-DD4B-B8A7-EF12BB006DD3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/140000/8CC12EC6-7756-0444-90CD-742FDC8FACE8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/144B4B69-6520-CC49-966C-9B576C073784.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/14C509B1-732B-DD47-AA0D-CA1024973EBF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/14E6A7E3-EA78-BA4C-A4BF-6EDD78606E0F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/17038C6F-FF15-8A40-A17E-956488531F91.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/1C450C52-8B32-4E4B-87DA-8B6E6D512A07.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/24EFDC68-9813-4E4C-82D3-1065FB171B81.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/4324ECF4-6A48-2142-80D4-AEFF87AF75C5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/4CC16550-9CBE-C04E-9D0F-7626CDA0A7CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/5DD7C671-9509-424E-898E-AB67D2DECDCB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/98A64569-4D83-5945-B99C-EE29DA396EDA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/A571861C-1145-0742-BF87-FD1C92B87B4F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/ACC191CE-A84F-174D-ADF9-F632610B6669.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/BA23B0E3-CA80-0344-87A3-0285A0698E3C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/BC637627-0B1E-164D-9EE5-5B27A237FE3C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/C4C8CD96-0B2F-F549-BFEF-5A2F092F9A2B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/C75A695D-1971-D345-AB2E-90ACEEE01461.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/D132BC97-7C73-CB42-8E50-3CDE612ACEB0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/F897961A-E996-2D46-BC09-970270019103.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/428639F0-B889-694F-BE31-22EA36652282.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/F9C7A5D2-983C-6443-85F1-479A6546F1ED.root',
] )
