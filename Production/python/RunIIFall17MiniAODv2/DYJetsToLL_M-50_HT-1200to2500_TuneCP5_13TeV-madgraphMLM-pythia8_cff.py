import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/002F36E1-0E43-E811-90B1-D8D385AF8AB2.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/12B02DB7-2742-E811-AD84-D8D385AF8B7A.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/20288BEA-4C42-E811-9D45-14DDA924324B.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3AB6496D-5942-E811-BBD5-68CC6EA5BCAA.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/58BFDCD9-2D42-E811-B0E8-68B59972BFD8.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/60A94334-8E42-E811-A7A6-90E2BAD492E8.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6C0E1266-8142-E811-B6D6-1CB72C0A3A61.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8AAEF60F-4442-E811-AD53-0425C5DE7BE6.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8EE6522D-6142-E811-9FFF-18DED7C60DEB.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/98B61EE6-E842-E811-A1E8-0CC47A7C35F8.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9E43B20A-B242-E811-AF10-68CC6EA5BE0A.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B6F5652D-4E42-E811-BCB6-D8D385FF1996.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C01F3F9B-5042-E811-9BD7-D8D385AF8AB2.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E061BA5F-1D42-E811-B3AE-34E6D7BEAF0E.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E62529CD-1242-E811-8A9E-D8D385AF8B40.root',
] )
