import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/0ED1B2D6-94F8-E911-81E1-0CC47A7FC746.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1852FB25-B4ED-E911-9B11-FA163E69DA51.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/18DFCD12-9FED-E911-BB96-FA163E2E4E96.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1E2F5FBB-5FED-E911-9CA8-40F2E9C6AF70.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/22B7F34C-48F8-E911-BE55-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/3C28E0A4-69F8-E911-8E61-AC1F6B0DE3A4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/408B5B3C-71EF-E911-A2C3-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6495A78B-94F8-E911-8973-141877637A57.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/74CBB591-94F8-E911-A2F1-C45444922ADE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/781DD457-41EE-E911-A410-24BE05C48841.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/7CAA8917-77F8-E911-8F83-E0071B7A3540.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/8C91B675-6DF8-E911-93B2-FA163E2295F2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9E4FC6A3-3DED-E911-BA09-FA163EE52FA2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9E5C75D2-5BF8-E911-AC3A-0CC47AFCC372.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/A6A89135-6AF8-E911-AE36-003048F5ADEA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BA6DDE48-81F8-E911-990B-CCC5E5F29061.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BC953560-5CF8-E911-A1F7-C0BFC0E5685E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D00D276D-86EE-E911-B556-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D66033E9-96ED-E911-9FE0-A4BF0128811C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E0BBF369-95F8-E911-B910-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/EE02D9E4-94F8-E911-814B-0CC47A5FA211.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F8BA3E90-94F8-E911-8771-008CFAFBE8F2.root',
] )
