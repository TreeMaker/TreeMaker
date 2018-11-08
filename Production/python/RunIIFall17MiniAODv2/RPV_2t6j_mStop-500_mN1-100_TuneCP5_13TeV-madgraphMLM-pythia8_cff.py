import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/1C5B3822-14A8-E811-83B2-001E677926A2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/1EB7A767-D0AB-E811-9A59-D0946626135C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/286FF74B-D0AB-E811-BE2C-0025904CF764.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/2AEA3775-D0AB-E811-B0E1-001E675A690A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/40169088-6BA9-E811-AF08-001E67792422.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/561C9050-8EA7-E811-B5D8-002590A371AA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/86CB0A60-D0AB-E811-9D1F-484D7E8DF0D3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/90099862-D0AB-E811-84A1-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B27ED94D-D0AB-E811-921E-0090FAA57C74.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/BCD934B2-F6A6-E811-9114-A4BF01125828.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/CA0AB63B-D0AB-E811-919A-FA163EEEF2BA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F2BD567E-D0AB-E811-9EA7-00259075D62E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F4E3943B-D0AB-E811-B079-E0071B7AC710.root',
] )
