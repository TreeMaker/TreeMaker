import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/56BCF775-B163-8E49-8E0A-4BDC57C49B5B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/6DB35F8F-4295-DE4F-9FC0-9B7C43A514B3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/7DB01417-C14A-1F49-989B-EBB101F85B24.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/899FAC81-9F28-6A49-ADAB-0DE9DEDCF2BA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/C8B0C7B9-48BD-B341-B8A9-0E040220A143.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/53D3E9C4-CB17-1147-8D80-28F313118AE4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/C90772B5-4B49-5643-A6CA-6D15954551B8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/190A52C6-41AF-854A-A611-A6548DB13913.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/497B7A09-900F-E34B-9081-C7F39EBB7F50.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/962B1E80-F02E-E84C-8719-65D73D6B3F34.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AA1760AF-4068-1440-BC59-ECD1D13EBD74.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AF838BE6-64F2-B741-A685-A45C7F4B87D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/C49DBD1A-32EE-FC40-9C7F-7BB795BB5E0A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/C5C46D34-BD14-DD49-AD93-B6DA08856959.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/15641E94-B8AF-EF4B-88F8-4CB2B8A6448B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/2AC557AE-FF34-7242-A928-8CD518792FF1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/3799E446-31F0-AE47-B60C-8B3189D4A3A6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/431727D5-85A3-1542-98FC-BB0C41176837.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/44D531EA-7469-B44B-B68A-25DB7C265159.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/66BCF73D-7AE0-5C44-8C62-EE4E9CBACDE7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/FB7A4F64-B83D-6149-980E-A5757E83C834.root',
] )
