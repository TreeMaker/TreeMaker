import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/DC8E1419-ED8B-8E4E-8BDB-DDC92C555F84.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/1A0B969F-BFA2-194D-8C1C-35DAC93782F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/20ED9F32-C150-304D-A778-38EB5E1CE520.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5635C830-3701-1146-9CB0-95F555E1659A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5F5F7D84-06D9-4F4F-A72B-D83319F39629.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/72E78A73-3BD9-4F48-8675-BD972EEC31F0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/8B60592B-B06B-9744-BB66-E7F8FC9978F9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/9BC64BE6-E336-2F4C-99AA-B92A43D79972.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A13A8726-4773-7146-B179-8A9CD4F76486.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/AC2045B3-67DC-1343-9B6D-A39EB2C5B06C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/027CF3A0-2103-4245-BA97-A269E8F1958F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/1F0E5A95-B724-0949-B89B-A42863BD709E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/2561B221-9A19-2F47-989A-AC32D9B392F7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/5292D97D-CF79-D848-9AE0-FDE5C64F4086.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/56B6CC50-105C-C14D-A099-187BC359833E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/73F4C52B-3B7E-E143-9D61-7BD292E0B49F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/B7AD8797-BB53-2342-A9E8-036A23C48FA9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/D71C7462-43EF-834E-8702-70B15940ED2D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/D93FD955-D9EF-4D44-9935-8CDB85741F58.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/E15E3040-B889-AC41-BDF0-46A608CD40E2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/F59D448C-44FF-0C45-8920-BF557153BAD8.root',
] )
