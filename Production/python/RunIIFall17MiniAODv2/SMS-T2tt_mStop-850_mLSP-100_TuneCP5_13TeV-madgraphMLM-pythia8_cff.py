import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/26B6987A-FC8D-E811-B153-509A4C747778.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6863CB6D-FB8D-E811-99EC-509A4C7812E7.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BE4CC8A7-DA8D-E811-909B-00266CFFBF84.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C43CF789-C479-E811-800B-1418774A24D2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D44B08A3-DA8D-E811-BA64-3417EBE34BFD.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/189A0CED-9D7B-E811-8507-00266CFFBE5C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9C042E6F-797C-E811-A553-FA163E7ABBFC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D07F84F7-C97A-E811-8DD1-008CFAF52120.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/16B3F461-DB74-E811-B379-A4BF01125608.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1C48B838-1871-E811-BB51-0CC47AA989CA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/28083AA1-DB74-E811-97F4-A0369F5BD91C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/2C0E5DA6-DB74-E811-B65B-E0071B73C650.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/4CBFE669-DB74-E811-AAEF-008CFAF7245E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/802B8891-DB74-E811-BFAE-0CC47ABAC0CE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/8202CD87-DB74-E811-B651-008CFAF74E6A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/A233A2CB-DA74-E811-8469-90E2BAD1C730.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/AC750B66-DB74-E811-B495-AC1F6B1B238A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B015D0AC-DB74-E811-BBC2-0025901A9EFC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/CA243FA1-DB74-E811-8F99-14187741278B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/D09671B0-DB74-E811-96B6-001E67DDC051.root',
] )
