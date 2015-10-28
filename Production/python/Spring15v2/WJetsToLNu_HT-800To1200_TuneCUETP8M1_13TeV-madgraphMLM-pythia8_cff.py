import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/0AE05470-866F-E511-9317-6CC2173DC030.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/3CD49BD2-6174-E511-8658-0024E850DF73.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/52E32C9E-9D70-E511-B742-6CC2173D9FB0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/6071CD6F-866F-E511-9211-6CC2173DAC50.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/7EBEEB77-866F-E511-BE17-0024E85A4092.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/82204ADE-7870-E511-9A78-6CC2173DA2F0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/96721334-8674-E511-B84C-6CC2173D96C0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/9CEDEB26-6274-E511-A84A-0024E850DF73.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/9E7EAC72-866F-E511-9658-0024E850EE78.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/A0D80A3B-7B70-E511-8D15-6CC2173DBD00.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/B27D1D2D-7E70-E511-8659-6CC2173DA2F0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/CA7D166F-866F-E511-827D-6CC2173DC030.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/DA12296C-866F-E511-96A0-6CC2173DC240.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/F87D1D2D-7E70-E511-8FDF-6CC2173DA2F0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/F87F5073-8070-E511-A620-68B599BA1070.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/027323C2-9C71-E511-9366-00221981B450.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/18363C48-8971-E511-90BD-6CC2173DAD00.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/18A26421-9471-E511-8D5C-00221981BAA3.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/20B762EF-8C71-E511-913A-6CC2173D9300.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/343F7570-9E71-E511-B7E2-0024E850EE78.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/38F92ACC-9C71-E511-ABE4-0024E850EE78.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3AA024D9-9C71-E511-A77D-0022198273E4.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/46A06A1D-9871-E511-BECF-0022198273C0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4C9E1503-9C6F-E511-B7B0-68B599B95EC0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/601D745A-9271-E511-8B35-6CC2173DBFB0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/602C155E-8971-E511-84AA-6CC2173DC030.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6639E3EB-8D71-E511-A072-6CC2173D9300.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6CE91B58-8871-E511-93E6-6CC2173DC030.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/80C112C1-9671-E511-BE8B-6CC2173DAD00.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8A4C66C8-9771-E511-B012-6CC2173DAD00.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8CF73BDD-9671-E511-9230-6CC2173DC030.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8EA004BF-8C71-E511-9716-002219818E18.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/9641A4D2-9471-E511-B7E2-68B599B97928.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/9E214678-9271-E511-AB78-00221981BAA3.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B024FE46-8871-E511-8E5D-6CC2173DAD00.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C019F6F5-9571-E511-8F99-68B599B97928.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C8E4DC00-8671-E511-B566-6CC2173DC030.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D645AEBD-9C71-E511-B3FA-6CC2173DAD00.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DCAB5824-6770-E511-A956-6CC2173DAC50.root' ] );


secFiles.extend( [
               ] )

