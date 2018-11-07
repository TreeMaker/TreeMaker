import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/04991636-AE41-E811-AD19-001E6739A781.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/10C2EA87-A742-E811-8DEE-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1209A3F9-6C41-E811-AF4D-001E67FA38A8.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/14504C9E-A742-E811-B71E-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1E2EA99F-A742-E811-AE26-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/26AF5CBB-9641-E811-88B9-001E67F8F9FC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/2A1B40FB-6C41-E811-95F2-001E6739B019.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/2AB02180-A742-E811-9A62-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/2E46FCD0-8341-E811-90EF-001E67F8FA38.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/30ED7886-A742-E811-A000-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/38FD2ECE-8341-E811-8594-001E67F8F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/541B5684-A742-E811-910D-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/5A8408CA-9641-E811-BD6B-001E67FA3812.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/623AF161-A742-E811-B065-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/6693339F-A742-E811-BA02-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/8C8BFDFC-6C41-E811-8393-001E67F8FA3D.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/949D269C-A742-E811-BFA6-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/96741D9F-A742-E811-A41D-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/984B7DF7-6C41-E811-A8A3-001E6739BC81.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/A63A5087-A742-E811-B6D3-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/C825383F-FB41-E811-96FE-001E67FA3920.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/D28BE86E-C941-E811-8C2A-001E67FA402D.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/E2DD638F-A742-E811-BC38-0242AC1C0503.root',
] )
