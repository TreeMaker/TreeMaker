import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/1883FC49-C031-E911-9B3A-0CC47AFC3CA4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/26D56E90-B631-E911-9CEE-48D539F38636.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/3A0264A6-E934-E911-807E-001E67581344.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/3A4429F9-BA31-E911-A2F4-346AC29F11B8.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/44C7D84B-A931-E911-9F13-48FD8E28248B.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/46A5C974-A031-E911-A849-485B3989725A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/52F895F1-0B32-E911-9263-001E675827DC.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/6633E44C-AA31-E911-834B-001E67580704.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/721FD176-CD31-E911-8C85-48FD8EE739ED.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/7E0AB193-9331-E911-BB2B-48FD8E282979.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/8A65CF86-B631-E911-B9FC-F02FA768CF7C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/9CEDFC97-BF31-E911-BDAE-A0369FE2C08E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/B239A424-9831-E911-8D90-001EC9ADCBEF.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/BC84A8AF-8131-E911-A3D4-0090FAA57AA0.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/BCD6498D-5F32-E911-94C3-F02FA768CB4A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/D0AB362A-BB31-E911-86DD-20CF305616FF.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/E85C9098-B631-E911-B121-A0369FD0B362.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/60000/F21A387E-B631-E911-890C-A0369FD0B15C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/16641DF1-441A-E911-8215-246E96D74858.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/2685C68E-E119-E911-8A3F-0CC47AFC3C72.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/7EE396F1-421A-E911-A003-901B0E5427B0.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/A85CD795-4C1A-E911-9EBA-001E67504AA5.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/B4977A17-3F1B-E911-BB0A-001E6757F1D4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/BC75A904-431A-E911-8D72-246E96D14D18.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/C0A70177-561A-E911-A1B4-0CC47AFC3CA0.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/CA36FD04-431A-E911-B098-0CC47AFC3D34.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/80000/FEB2CE00-431A-E911-8CEF-0CC47AFC3C9A.root',
] )
