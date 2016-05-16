import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/0417FE3C-3B04-E611-9817-3417EBE64CA8.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/0C6E53E5-8804-E611-9015-14187741278B.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/12CCE037-5003-E611-987F-001E6878FB21.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/148C1CEF-4503-E611-A9BB-3417EBE5281F.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/26483AE1-5303-E611-BCAF-7845C4FC3B8A.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2E5C8EDB-8804-E611-BA5E-008CFA197B4C.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/38FEA7D4-8804-E611-AC12-B083FED76637.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/44FB3838-5003-E611-89FD-0026B95C2418.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/4AA39ED6-8804-E611-BBA4-008CFA0025A4.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/5E4FF4E4-6404-E611-AF57-000F53273758.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6E0718D5-8804-E611-8FCD-0002C94CD0D8.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6E52C66B-8103-E611-B4A5-B083FED76DBD.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/70131349-8904-E611-8FE9-0025901AC1F8.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/70685013-3803-E611-81D4-AC853D9DAC25.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7870FD31-4303-E611-A812-B083FED76637.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/9432FCAA-6F03-E611-8DD3-842B2B2B0E64.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/943C93E5-8804-E611-ADEA-001E675A690A.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/96D8F52A-5803-E611-9098-842B2B2AEE96.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/9A353144-4303-E611-ADEF-842B2B2925F5.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/BE328A20-1404-E611-AA4B-B8CA3A709028.root',
       '/store/mc/RunIISpring16MiniAODv1/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D2E1571B-BB03-E611-BEF5-001E675A6AA9.root',
] )
