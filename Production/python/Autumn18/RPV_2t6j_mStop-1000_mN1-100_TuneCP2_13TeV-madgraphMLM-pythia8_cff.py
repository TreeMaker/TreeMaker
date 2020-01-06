import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/36662A2C-4A8A-7F4A-B69E-4A6C3801B845.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4ABA5045-B5DE-7A4A-832D-71BE17D6DC2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5931D847-A212-3848-BCB2-76320671DC01.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/69CAC7B7-773F-2842-8EA4-DEF22A6934B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7B032191-9748-4E47-A1FC-2C41106B3A57.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/839C9807-FDA5-6E4A-8E36-420F0FFFA3D6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9257688E-B0E8-A84C-82A5-BE2E6CD7BD36.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A97A82FA-821D-564A-84B1-C73105C8DF5A.root',
] )
