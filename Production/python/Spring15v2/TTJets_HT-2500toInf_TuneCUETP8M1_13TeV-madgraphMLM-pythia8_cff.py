import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/022A0496-CB6D-E511-BF06-008CFA197E18.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/223E5874-A66D-E511-B918-008CFA110C88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3C7E27F9-AC6D-E511-B3A6-008CFA197D18.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/46622B84-C66D-E511-BFF8-008CFA19743C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/540B13A7-B96D-E511-82C0-008CFA197E30.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7638D6E7-A76D-E511-8978-008CFA197990.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A21A591A-BC6D-E511-8E6F-008CFA197E30.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AED92062-9B6D-E511-A544-008CFA11113C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B86B5142-B76D-E511-82F0-008CFA197E30.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BA93D1C2-966D-E511-8BFC-00266CFFBF24.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/CABBF86E-C26D-E511-AF0B-008CFA00F690.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FA433983-A16D-E511-9742-008CFA010760.root' ] );


secFiles.extend( [
               ] )

