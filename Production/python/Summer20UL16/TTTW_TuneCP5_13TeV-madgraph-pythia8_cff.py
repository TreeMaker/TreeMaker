import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/153B6017-8193-224A-992B-B68C305BF762.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/4B0A11B2-9337-1C43-916A-69C6CAB3D92A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/5F06943E-4767-A04E-9AE6-2F8D765ED988.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/74337FA6-3781-564A-B741-5136FEE89B2B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/86A8940B-C9B3-3B46-AA57-61F996E9AED2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/F0FCDD1E-5009-DC47-A215-9FB87FDE4FC6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/06C061BD-3B2A-3843-9D35-DDAD9BC05FE8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3A93B1E6-A8AC-F642-B233-61946D1EA279.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/EA870284-5569-0E44-AAE2-A6855767EB63.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2550000/C14B826C-02D4-3E41-82A4-1FF69A398972.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/13B78D8F-7E4B-734F-912D-F063C0A72E63.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/171B96A8-3373-0C4E-8675-61B0781598F1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/631326AE-E556-7B43-B793-7527AA6C998A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/6B24C749-081B-704F-A897-25A0BBF71878.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/AE23B6F1-FE5B-EF44-936F-5AC9D68161E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/6546CAAD-C1AC-C047-B31A-8028DEA40B2C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/798F008E-003A-AC4E-88F9-722AC8CC0F7F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/7C5CC5C1-DF46-D142-B0C3-1345FEDBE04C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/7C62A78D-C054-F341-A394-967CC839D9FF.root',
] )
