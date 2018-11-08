import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/02D4B241-4330-E811-A858-6C3BE5B513E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/06DC2A20-4530-E811-8928-001CC47B8E48.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/0CAE4948-4E30-E811-BA80-6C3BE5B5B108.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/161AE6AF-3D30-E811-A7DB-44A842CF0598.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/2664C791-7030-E811-808D-44A842CF0571.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/3077272D-3F30-E811-BF10-6C3BE5B513E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/32AE7580-7330-E811-B28C-A0B3CCE45C2A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/42FDF63B-5530-E811-9930-484D7E8DF078.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/4E640D64-5330-E811-9480-6C3BE5B54138.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/5E3352B0-3D30-E811-AF73-D8D385B0EE2E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/64D1E87F-7430-E811-A90F-44A842CFC9E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/66EF74AC-3730-E811-8370-B499BAAC09C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/6C7A9D8A-5E30-E811-818F-484D7E8DF092.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/78A68A8E-7130-E811-B783-6C3BE5B5C0B0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/8E60F096-3830-E811-ABF7-44A842CFD5B1.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/96AE9A66-4F30-E811-9AA3-6C3BE5B54138.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/BA5C738B-3E30-E811-B240-44A842CFC9E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/C6B230DB-4730-E811-8065-B499BAABF212.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/E605BF89-7930-E811-89A5-6C3BE5B58058.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/FE962D0B-3B30-E811-89B8-B499BAAC09C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_pilot_94X_mc2017_realistic_v14-v1/80000/FEF2A6AE-4930-E811-8EA4-6C3BE5B513E0.root',
] )
