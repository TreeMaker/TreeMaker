import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/12608B5D-E66D-E511-B233-441EA173397A.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/24A1DB5A-E66D-E511-A5B8-441EA17344AC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/2EDBAA60-E66D-E511-8E10-D8D385AF8ACC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/42A76F61-E66D-E511-A164-842B2B76653D.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/58AE5171-E66D-E511-ADD6-441EA1733A74.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/5A08B061-E66D-E511-AAFC-441EA171A0FC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/648828A0-E66D-E511-A5DD-34E6D7E387A8.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/64A8C5B0-E66D-E511-8201-02163E014FF8.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/68DA5F5E-E66D-E511-A798-441EA1733CCC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7E37BE5F-E66D-E511-8139-68B5996B4520.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/80D2A260-E66D-E511-817C-D8D385AF8ACC.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/864F6B5B-E66D-E511-9E19-D8D385AF8AB2.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/869CC35B-E66D-E511-A128-34E6D7E38781.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/88D3EE56-E66D-E511-A1C1-0025905C42A6.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9406785C-E66D-E511-A0A6-D8D385AF8AE2.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/942A765D-E66D-E511-806F-34E6D7BDDECE.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/985E4F5B-E66D-E511-BE8C-34E6D7E05F1B.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AEDFFC5C-E66D-E511-927B-00266CF9B5D0.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B04B148C-E66D-E511-8B1E-34E6D7BDDECE.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CC3A7C73-E66D-E511-8BAD-0026B9278685.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E00B9B5B-E66D-E511-B015-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E6B90060-E66D-E511-9025-D8D385AE8C68.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FADC2860-E66D-E511-8B2C-441EA1733A9E.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/34877C5A-E66D-E511-B9C9-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B85F8437-E66D-E511-92FD-D8D385AF8A12.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DE576439-E66D-E511-9835-D8D385AF8A88.root' ] );


secFiles.extend( [
               ] )

