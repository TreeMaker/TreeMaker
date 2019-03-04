import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0CA9F9EC-A542-E811-BCB3-0025905B8576.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1291824C-BB42-E811-8B6B-4C79BA1809F1.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/183E31FC-B342-E811-A675-5065F3819241.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1A94344F-DE41-E811-A922-4C79BA181223.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2A895121-B242-E811-87EC-E0071B74AC00.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/324ECA45-CF42-E811-B933-24BE05CEEB81.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/36910188-C842-E811-A917-5065F3815221.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/42B012DF-F941-E811-AC2A-FA163EA5E58D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/4684123F-EF41-E811-8FE2-EC0D9A82260E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/46B817DB-AA42-E811-AE90-EC0D9A822636.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5A58D95F-C442-E811-81BE-FA163EF78C40.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/76F814F4-CE42-E811-BB09-549F3525BF58.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7E390EBD-B942-E811-825A-0CC47AD99062.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A2F74E0F-A942-E811-BE3C-E0071B7A58F0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/ACE5382F-B642-E811-81AF-24BE05C46B01.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B06AE8E4-AE42-E811-86FA-1866DAEB3628.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D23F2633-AE42-E811-8361-24BE05C62611.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/EE91F8DC-AA42-E811-9ECE-EC0D9A82261E.root',
] )
