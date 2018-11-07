import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/ECE12D60-C742-E811-967A-0CC47AF9B1EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/FED4C0A3-D242-E811-B41A-0025905C53B2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0262A069-2942-E811-AE5C-0025905C5432.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3A020666-8A42-E811-B026-0025904C6566.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/40694D12-F841-E811-8E51-0025905C53D0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/42471E14-3142-E811-8D11-0025905C43EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6E3B714E-F241-E811-B842-0025905C54FC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6EABA368-0342-E811-A138-0025905C42F2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/70F38D62-9342-E811-B91D-0025904C4E2A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/72BE908B-8642-E811-8C1D-0025905D1E08.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C62234CA-0542-E811-9F84-0025905D1CB0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/CC7F8064-9342-E811-B687-0025905C43EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D6736E01-8842-E811-BE01-0CC47AF9B306.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D89DCCE2-9442-E811-AD39-0025905C9726.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/DE49AC65-8A42-E811-A7C4-0025904C4F52.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F40EAF8B-8642-E811-A6A8-0025905D1E08.root',
] )
