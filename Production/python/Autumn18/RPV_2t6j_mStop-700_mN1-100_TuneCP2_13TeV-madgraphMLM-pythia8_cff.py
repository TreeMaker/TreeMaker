import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/24D29E68-B97E-C446-8F78-39EA321BA77D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/28301A03-BBC1-AF4F-ADCA-44AFB95FAAEF.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/3B3B7AB9-A377-C741-96D4-8F11685D8128.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/40638A10-B03E-A64E-88BC-FB218190FBCE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/7C905295-14EA-4D4B-88D8-B8533AE5F662.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/86DA0116-9DD5-A045-99DD-2411B9D6FD7E.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/8E745CBA-C3DD-CD43-B8D5-902C7ABD7A38.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/BC72673D-6C91-FD4D-B391-670B6E6541CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/C11AC7CA-76B3-4847-B949-229A2B9D8BA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/C97FCDCD-A2AB-0B4C-855E-4E56F041DB11.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/D1C92D6C-E04C-F34D-959B-40D239EEBC62.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/ED486D29-B347-B64E-A30A-7BC70A7D95DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/F592F587-FEBF-0140-B597-66BA98333F91.root',
] )
