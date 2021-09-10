import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/675049E3-D8E2-F84C-943F-53817D8EDFE2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/7FE9A72D-3C96-1E44-AFEB-41C92B3DB03D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/A282F27E-5133-2848-9195-7A518BAC6951.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/B8DA7107-25A0-674F-AA78-A21A9387E1A8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0D977E57-462C-C941-9598-5E2651B7092F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/45EB24E3-8845-9F44-98AF-00327EA62680.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/DD28C2BC-E394-0C40-9C36-0E68BF9DDF5F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/1F1E9201-81D0-C342-9E6B-0A3FC7912CBE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/2257158F-C888-EB47-9D30-2220F179A7BB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/35269538-8154-014B-8B05-464F0EC2C0EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/359C7411-3C1B-DD47-A39B-894327120CD2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/3CF24101-D5CE-164B-B303-FC2B98EE13A1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/69FE261F-87A5-2747-BAF0-09C3D49AECE2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/0F945D61-45F2-AB48-8F55-7E19B7C93697.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/6DA7FAF1-5AAE-2944-B96E-88E223FD7303.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/8E197022-86AA-E94F-BEE0-74EB887242BC.root',
] )
