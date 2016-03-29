import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/007C950B-CA6D-E511-8B0E-008CFA0A57E4.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/14E95F0B-CA6D-E511-BA91-842B2B766849.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1ECEEF09-CA6D-E511-B701-842B2B765E01.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/24A1770D-CA6D-E511-8104-008CFA14F814.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/32DC8209-CA6D-E511-868B-008CFA165FD0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/342D207E-C96D-E511-920D-0025907DC9BC.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3CA4D10B-CA6D-E511-A4AC-008CFA0A57E4.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/427383C1-C96D-E511-873B-008CFA56D6F4.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4A3C210C-CA6D-E511-ACA8-008CFA0A5830.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4E44710A-CA6D-E511-B34F-008CFA0A570C.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/56E847AA-CA6D-E511-BC58-008CFA1CB8A8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/5A082C07-CA6D-E511-89EC-549F35AE4FE3.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/5EE11009-CA6D-E511-BF5A-008CFA56D794.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6406F80A-CA6D-E511-BC36-008CFA0F51EC.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6EC9760A-CA6D-E511-8212-008CFA064774.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/72904A0C-CA6D-E511-80FC-008CFA064704.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/78DFCC0C-CA6D-E511-8BE9-008CFA0A57E8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/90BFC50C-CA6D-E511-8E16-008CFA0A571C.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/9A12AFDF-C96D-E511-9CF7-008CFA1C64A0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AAF5AC07-CA6D-E511-8690-00266CFCC304.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BE6D160D-CA6D-E511-B960-549F35AD8BFD.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C653111A-CA6D-E511-8055-549F358EB76F.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D2BDA90B-CA6D-E511-9E99-008CFA0A58B8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FE67A10B-CA6D-E511-9F1A-008CFA0516BC.root' ] );


secFiles.extend( [
               ] )

