import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/006F7824-1DF9-094A-8587-DECBB769C4E7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/00E668AC-90F4-4946-9ADE-D8FC1ECAABA0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/08F1AAF5-B487-AC48-B4BC-B161B236B673.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/0B01A0FD-8B3B-DF40-BCBA-AD191EB5D061.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/15BA5E62-6AF1-324D-AD9A-8AA60EBD5FF5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/17915149-57B0-7C48-9A74-11494E2A0A01.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/33345E33-BEE1-3848-80E5-308BF6A429FC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3E4F1DDC-EBD3-DA47-8E6E-65D9C971ABDD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/6579DE83-4E9D-A047-A460-E565FEA16B29.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/71878C80-B5F9-084C-A78D-898C5938BA04.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7369D999-1128-0648-8452-D1ED26A1B9D0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/75E75DA2-6F84-4B48-92A2-C97D853D76E8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/87C54F89-43AF-3046-BFD2-9D0B30F44989.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/907B3B9C-574A-B344-979C-E3CC3D856F4E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/A7162680-E959-514F-8FA9-D5C47D315814.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/A9365DBB-D2E7-8748-A69F-8D08DE45134E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B0C09C2B-85CB-D242-BA1B-21DE830BCDF9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B69D406E-F6DE-414B-AB7A-1FD1E0988E4E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C032A951-5C80-F442-8470-FFBDEEEE27DD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C9888AC5-D7C4-B248-8D4E-9936C5D59779.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CB64CEBF-6889-8D41-A8F4-9B308CDCCC57.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CDA4E78B-9A7A-124B-BDBF-2AAA9B3CF4B1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CDE049C2-2B14-9140-90DE-C0BE45AD4A89.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D653E8B6-DD2A-5545-9599-FCCBAB625D06.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D7361D81-15EC-1F43-A3B0-4D93C1697077.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E51FA71A-FDE9-FB4E-9D21-A34F35D530A5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F141657A-CE6A-E746-BD4F-07DA315E3262.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F232C683-76CC-6748-81EE-43EC7C040F2A.root',
] )
