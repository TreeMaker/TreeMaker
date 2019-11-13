import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0CC07B4A-13D9-5643-B250-125B02DB67E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/22997A75-A67B-FB4B-BC5D-E2F646A185CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/562E1CA1-8D84-A548-86E4-CCFEB8174FAD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/798DDA6F-52AB-A54D-B749-9CC6378EF145.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8C25ACD9-7FE7-BE46-8E6F-9F81DD0FDCA7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8D7410A0-6968-EE48-A175-F4E5C39A725F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AFA9F06B-C884-9E4F-A47A-C95FE0625DB1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B474D6C9-8E4C-EC40-815E-C52D460A52DF.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/BCA992A9-3E7B-F141-9449-EE9E647B2110.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DE5BD225-66CC-2248-9652-36FD263A4709.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E18507C9-7138-324C-B1E7-05C35C57D1AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E5D1F44B-D7DF-634C-AB13-8893A10C65AE.root',
] )
