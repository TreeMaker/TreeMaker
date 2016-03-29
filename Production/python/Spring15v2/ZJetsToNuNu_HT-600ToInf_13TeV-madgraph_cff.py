import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/6A6FB8F6-B976-E511-9A1B-002590D9DA9C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/70A7A408-BA76-E511-BC36-003048322CA0.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/8C39D501-BA76-E511-9AF7-00259048A860.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/AC9490FD-B976-E511-AE94-002590D9D9E4.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/E843B4F8-B976-E511-99B9-002590FD5122.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/EE56471A-BA76-E511-AE99-0CC47A0AD6F8.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/0A768AED-2677-E511-8B13-0025901FB188.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/3EFE7581-2777-E511-8055-0025901AC3F6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/4A7A88C4-2677-E511-826E-00259029E670.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/565ECD8E-2777-E511-89BF-00259048A87C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/5E72457D-2777-E511-BEF6-002590791DA2.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/64A6DAD1-2677-E511-B3C4-002590D9D9DA.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/76CB6177-2777-E511-A15F-002590D9D8C2.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/A6D610A1-2777-E511-8777-00259029E720.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/AE6FACE2-2677-E511-8DB9-00259029ED16.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/B0B6BE7C-2777-E511-A185-00304867FDF3.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/BE0DF437-2777-E511-8518-002590FD5A78.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/BE8EE97A-2777-E511-B94F-00259048AE50.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/C21CC53A-2777-E511-AC03-00259029E7FC.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/C6479D60-2777-E511-9745-003048FE40E2.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/CC5A5323-2777-E511-B738-00259029E922.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/80000/D0BA16B6-2677-E511-8270-002590D9D956.root' ] );


secFiles.extend( [
               ] )

