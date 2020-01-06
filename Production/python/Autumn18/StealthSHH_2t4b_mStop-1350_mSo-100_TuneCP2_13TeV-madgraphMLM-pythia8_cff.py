import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/1FE3637D-2BA4-804A-B31E-73609FDE5274.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/34FE2F19-B5F8-1445-B051-7A67A505A8F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/41B652C0-9F3A-5345-93CC-E4374091D2E1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/4FC754EA-F201-3545-AA7E-40118E508258.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/6FBED918-980E-7D41-A99B-BBC35BD03E5F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/8791DBAE-C7BD-6845-921C-E3C17BAB6EFB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/88B0A935-A951-0149-8034-3C55820A76F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/8DA4C9B5-1B4F-8548-A4DB-E1F899033A02.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/8F9B31D6-F37E-EC4E-BC68-857689D7D0D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/BD9800D2-6A62-4C4B-9579-3D44F5F47820.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/CA4BBE7D-DE72-2045-B92C-F6429EEEC2C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/CC448235-F41E-D541-A1D2-58BB42F0B395.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/F70C680E-6668-4A49-A3D7-55EDB4966BB4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/FFE2AB1B-CEA7-C943-B698-24A45253BEB2.root',
] )
