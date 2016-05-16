import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06F3F567-9102-E611-86DE-D4856459AC30.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/46B1B173-6103-E611-A3CB-0025907B501C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/6EB3945B-E903-E611-80B0-002590D60090.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/70362FBF-3804-E611-A517-44A842240F8D.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D2976A78-B902-E611-AF7D-001E6757CD34.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/762EDF12-CE03-E611-AC72-0090FAA57E84.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/906D7B31-CE03-E611-BBB5-44A84225C3D0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/C27EF143-B302-E611-9561-20CF30725200.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D43DAB5B-CE03-E611-A8BE-44A84224053C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/14AE6DC0-1F08-E611-AF3B-20CF3027A5A7.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/16A42FB1-1F08-E611-A6B5-00259021A4A2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7668AAF8-C601-E611-8648-0025907B4F04.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F46B5AF4-C601-E611-983B-44A84225C8FF.root',
] )
