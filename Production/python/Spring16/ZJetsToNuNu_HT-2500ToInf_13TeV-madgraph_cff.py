import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/50C10CE1-D7FF-E511-A214-D4AE526A0B03.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/84089951-D8FF-E511-96F1-D4AE526A0419.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8A7768AC-F100-E611-8E67-001EC9B2189E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8AA6A2E6-3901-E611-92F8-001F29658458.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D6A3528A-0700-E611-84B7-D4AE526A0D2E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/DA18A57C-2501-E611-A54E-0090FAA581F4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/310000/D0D0E1F2-D503-E611-A2B1-842B2B7682C7.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/12EFDE32-F6FF-E511-B978-1CC1DE19274E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/246AF22B-D5FF-E511-A910-842B2B766242.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/3C0934AF-8F00-E611-8FBB-00259073E4F0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5CC721A3-44FF-E511-B9AC-D4AE526A0455.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/7AD29B12-2B01-E611-A293-D4AE526A0CFB.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/8A623635-7FFF-E511-971D-001EC9AEFC7E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/960EC35E-98FF-E511-B991-002481CFE648.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/C6CF18FC-3901-E611-B346-D48564591B64.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/CAD0BEC9-3901-E611-9779-B083FED13C9E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/DA253C40-F6FF-E511-B8B4-782BCB161F1B.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2AB4C6C6-4700-E611-A0D1-842B2B760921.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/3497E191-4700-E611-BC07-0090FAA57400.root',
] )
