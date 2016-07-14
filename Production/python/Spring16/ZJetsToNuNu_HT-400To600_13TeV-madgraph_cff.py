import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/1C75E9DF-AA3F-E611-8242-0090FAA573E0.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/32D9A1DF-AA3F-E611-A306-0090FAA573E0.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/3EDD874E-AA3F-E611-BED1-0090FAA57380.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/44DB2EF3-AA3F-E611-8B32-0090FAA57780.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/6828DCF2-AA3F-E611-82FF-001F2908CFBC.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/AA9DE7DA-AA3F-E611-AAB8-0090FAA58194.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/B683ABDE-AA3F-E611-A763-0CC47A1DF7FE.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/D84F85B7-AA3F-E611-B15F-001F2908BE42.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/DE9896D9-AA3F-E611-9F3E-002590D0AFA4.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/20000/F458315A-AA3F-E611-8C40-44A842CFD640.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/2A423C67-323F-E611-80D4-002590D0AF84.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/80000/948685B4-333F-E611-87E9-009C02AB98A6.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/2C38A58C-D146-E611-ACB4-00259073E3E0.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/36DD7256-E348-E611-B123-44A842CF05B2.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/488A86E9-EB48-E611-A61A-44A842CF058B.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/76E21BA2-A646-E611-89D0-0CC47A4D99CA.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/90F2E78A-D146-E611-9911-20CF305B0594.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/9689377C-C146-E611-8921-BCAEC54B3067.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/A6BE7EE6-EB48-E611-8E3B-44A842CFD5B1.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/B8BDFBA4-A646-E611-88DF-002590775158.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/BAB6EF2B-AE46-E611-97A8-0090FAA57E24.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/BC1FA796-FB48-E611-AFA9-44A842CFD60C.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/C82DE060-AE46-E611-8284-0CC47A1DF616.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/CCEE61DF-FA48-E611-AEF2-44A842CF05A5.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/F661992C-AE46-E611-9B2D-0CC47A1E0476.root',
       '/store/mc/RunIISpring16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/90000/FA22B8D3-A046-E611-AEB6-00259073E4C8.root',
] )
