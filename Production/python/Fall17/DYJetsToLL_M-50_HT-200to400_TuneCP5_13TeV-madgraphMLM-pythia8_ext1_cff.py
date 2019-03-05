import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/00C5017C-9F42-E811-9410-1CC1DE046F00.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1CE88556-2542-E811-8762-7CD30AC030B4.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/302A91E6-4C42-E811-B83E-0023AEEEB6FA.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/30FE2985-3C42-E811-8A27-28924A33B9AA.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/36919F19-5D42-E811-BE8E-0026B92786AC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/3E387B65-9F42-E811-B475-AC1F6B1AEFFC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/48929CD8-4242-E811-9668-0026B92785E9.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/5A056D76-5442-E811-BAEF-0023AEEEB208.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/5C10464A-4F42-E811-A2DF-0023AEEEB6FA.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/66881608-4942-E811-8569-0026B92786AC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/6A6DE45E-5942-E811-8483-20474791CCC4.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/70FF2BD3-2D42-E811-ABC8-009C02AAB554.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/788021CC-3D42-E811-9F2D-1CB72C1B6574.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/869BC138-3A42-E811-BB31-B49691091EA2.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/8E2D9C7C-9F42-E811-B72B-C4346BBC1498.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/8E507E00-3042-E811-AFFE-3417EBE47EBC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/9E8D7268-4042-E811-8224-0026B9277A32.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/A09CE4DE-3742-E811-AE2C-28924A33B9AA.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/AE8C6F75-5E42-E811-AECE-20474791CCC4.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/CAB9A032-4542-E811-958C-0026B92786AC.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/CEF85C86-5142-E811-A7D5-1CB72C1B649A.root',
       '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/D883262B-2B42-E811-AE87-7CD30AC030B4.root',
] )
