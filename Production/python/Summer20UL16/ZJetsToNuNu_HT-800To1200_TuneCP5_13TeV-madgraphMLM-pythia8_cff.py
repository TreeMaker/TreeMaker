import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/33C88A1A-1345-4749-8342-6F5FB295B94C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/75818425-7307-204A-B89A-4A7EC08A635C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/E1F49760-0EFB-1542-ADAB-4593458A1CF6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/14141219-FE0F-D04E-ADC9-D200CC5025A3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8BB01E19-302C-7145-AF55-119C22913D4C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/15628756-9A57-7B4D-8BF3-8D192A868A7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3A035326-1F26-7149-85AF-BEA3BAE1A749.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/51C90DDD-8225-8541-99E6-14C0ECF3D0D2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5E9190DD-C492-474C-82C2-64BD7FBF03B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/724E2695-730F-9949-A681-33EB2EBE5F94.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/91A10299-2E4A-E145-908C-2F674B335074.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/BDDAAF06-69F8-3E4E-875D-8D35F65DAA85.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/ECCBDB11-0078-7648-8702-6A5B2EE463B6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/137B705A-87AA-244C-89D0-7C74C1E1260D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/1B09AC84-6D01-A341-A8F4-67D66116AFD0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/45775B29-2FF8-EA4A-85CE-157CF4E2ECD3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/7BEAA13E-41E6-8942-90CA-76ED890866BD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/80312A4E-464D-6449-BE92-2E7FC80F4511.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/81000E54-B09D-9249-8D5C-2401698B6711.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/845AC0E2-CDD3-064B-8441-958AA39F5C17.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/86422868-CC63-8A4E-96D3-861224A491B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/881D9735-36B2-B045-B3DB-8D05A7C9D18F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/986D947A-EE15-8F49-A0B6-647D2D1A54B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/D02BC4A1-1607-ED47-8C0C-35EB3ABC8056.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/E0DE61E7-464A-3D41-80C0-BB13356644BE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/2008F8AB-4A79-D841-9DFC-CBC5C0601D60.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/80000/414E9841-D6B9-3248-807E-717269C764F5.root',
] )
