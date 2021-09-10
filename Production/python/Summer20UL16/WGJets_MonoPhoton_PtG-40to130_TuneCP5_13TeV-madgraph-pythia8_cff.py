import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/100000/B3448D1C-B40C-4D4A-969B-F8037F5D1529.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/3EF52CB1-2267-2345-BD4A-0F4023E09C33.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/A148C0EC-7138-3042-9C50-94FA631BA151.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/00830CBE-28B8-A44F-8939-C04A5046D49E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/0253B839-FC9E-A643-83D8-34C9D53E846F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/180CE6F6-F14E-6849-BE31-9247112C45A7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/18BF189D-3135-4649-83BF-9CBB289897B4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/1CA924E6-B044-6A43-8202-2B729FC4D4A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/1FB9574D-A446-824F-9EF1-C802D6AC2AE4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/22F3E7B4-F60E-1C48-9288-B6CF061D57A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/30608A27-842A-744E-8896-292ECCF0D018.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/30CD870C-65E7-7344-9A12-2D45FC982521.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/334CF773-F8D0-2645-A1C0-D837B477A042.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/39A3E772-57F0-5E49-9F17-B139FB31F25D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/41E8B30F-C48F-1546-B191-15C1A99597B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/42B8AA10-1730-2C4C-932E-BD6B14162F51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/42F1D3D8-37B6-EE43-B632-D698C3FB8222.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/5FADDE56-CC88-9D4F-8AAB-DEBE3D968813.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/71926C6E-67A1-AA41-A37F-EAF39B3FACE5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/7B719181-3CDB-D64F-BC56-9FA2F3B9D466.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/84B171C0-81B1-A348-B3C7-4E7311B4A4C1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/943DE870-9535-404B-A314-2F746C5AE2B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/ED37F418-0D42-1A41-B551-9E0402A26705.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/374E4E71-ACA4-524F-94EA-143EAB57EA53.root',
] )
