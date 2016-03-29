import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/16A57608-3770-E511-B676-3417EBE51BD1.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1E0FE8FB-116E-E511-A12E-0002C92DB464.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2CA783EA-856F-E511-927E-7845C4FAEFE9.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3CD58D7B-126E-E511-99C7-0002C92DB530.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3EF349FB-3670-E511-BE02-848F69FD895A.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4A653978-126E-E511-8664-F45214C748D6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/68E54FBF-886F-E511-95D0-848F69FD0BAE.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6AECC1B1-CA6F-E511-88DC-3417EBE34A8F.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7CC5302A-856F-E511-97FA-003048CDC848.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/829217AA-966F-E511-9D00-00266CFE6C40.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/9A8389B5-886F-E511-BAD5-549F351EC506.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/9E61298C-8A6F-E511-BECD-0025905C96EA.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B61C1984-126E-E511-9BC6-0002C92DB46C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BC70B2FA-116E-E511-ABA8-24BE05C4D8C1.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D08B248C-886F-E511-BE77-3417EBE528EB.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D266E7B9-886F-E511-8194-00266CFE8008.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DE156F95-886F-E511-B3C8-549F351E6E16.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DEC6ACAB-886F-E511-9A87-00266CFE8008.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E846320B-3770-E511-966B-7845C4FBB764.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E8DFD596-886F-E511-B698-000AE488B7C8.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/EAD6C8F6-3670-E511-A538-3417EBE613DA.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/F43DB6AC-966F-E511-93F9-003048CF66D6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FC361F1D-856F-E511-B77D-5C260AFFFB63.root',
       '/store/mc/RunIISpring15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FCA61494-8A6F-E511-A112-0025904CDDEC.root' ] );


secFiles.extend( [
               ] )

