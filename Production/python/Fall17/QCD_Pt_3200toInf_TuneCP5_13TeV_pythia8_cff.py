import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/04CB399E-2C42-E811-8486-B496910A041C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/06BFB52A-5142-E811-A7AE-008CFA0A5808.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/0A1192E7-3942-E811-A5CB-008CFA1CBB34.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/1AE41B1E-3C42-E811-9A5F-008CFA1CB55C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/2C47C5D7-5442-E811-AA36-B496910A9088.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/32B326B9-0E42-E811-8D8A-B496910A8AB4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/32BAB7D2-6B42-E811-81C5-B496910A9820.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4ACD35C0-4D42-E811-B412-008CFA0A58F8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/60144E13-5D42-E811-9BF1-B496910A9088.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/6AB770C0-3F42-E811-8284-008CFA1983E0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/8249A5BD-7742-E811-BD19-B496910A8AB4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/8AF39470-4642-E811-833B-B4969109FE54.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/92E5E7B3-E841-E811-8711-B496910A041C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/9ACFBACD-E042-E811-BB4B-008CFA1C6414.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/A86CB7AF-3442-E811-91C5-B4969109FA60.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/BA2ED629-6342-E811-A435-008CFA0A5818.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/CCB27E9D-2942-E811-8F3D-008CFA14FA8C.root',
] )
