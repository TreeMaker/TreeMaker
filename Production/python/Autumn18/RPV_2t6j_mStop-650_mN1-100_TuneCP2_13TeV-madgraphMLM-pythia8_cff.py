import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/26C7D612-795D-9149-B54F-EC060DB2FA90.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/5389F0E9-B34A-7D43-BB5E-B26FB96BC701.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/56714EC2-DFA9-D04B-9C4A-E7EFAA0F9A71.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/6131FF43-79FD-554A-ADA5-FF3601D5B82D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/6E489B64-C55D-0E4C-A089-D7333FC090F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/992461F7-C796-6148-93B4-3A24B6344430.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/AA53D49D-90E3-5346-B9D6-89991C816479.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/B143F62E-C88F-8542-9B32-A3C86F91F795.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/50000/C972CB2B-E578-1F4D-B41F-F4D3A4A17CCC.root',
] )
