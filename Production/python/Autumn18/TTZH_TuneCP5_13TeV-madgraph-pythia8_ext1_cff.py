import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/13FDD71E-3FF6-7041-B495-2EED05473191.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/15D02B6C-4350-8949-B992-0F445A65E230.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/1694684C-8ECB-5D4A-9460-B6AD7D3560FA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/2D4197BD-ABBC-0541-A8DD-9760D7B4B0E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/363D57A0-8BE3-9742-999D-2F945F8D035C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/77A94C89-F990-614D-9D0F-C241FECEF034.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/7E377F5A-3606-374E-B114-5EF5D8FBC1FF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/84FC80B8-92A0-2645-8C26-3A9B5B2EAE86.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/A318FF00-6663-7741-B8B2-9D658C01CDB0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/B18B0DC5-3D0A-D844-9BD8-85381BFCA6CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/C3FDD003-EBC6-6F4F-947E-AEF9D3C13E9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/DDA59CA7-F3D5-7943-9813-A905FEC1D513.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/F2DC48D0-63D4-F145-8F38-27D61C12D461.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/30000/028BCA09-D3A3-CD4C-9DC6-4F2087E9157B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/30000/20FD5D34-072E-6A4C-9AC8-E75F263B6636.root',
] )
