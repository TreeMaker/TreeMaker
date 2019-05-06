import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/015F0E73-E038-964A-86FC-A7B0CD085086.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/1389C28A-CC57-4349-B80E-267E7A82DA16.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/2884B24E-25BB-4B4B-A61E-6C49A8BC7BB1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/2E2723D9-7BF3-7E44-A65A-19105F7FB847.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/31B0E1A2-5521-8B4D-AB8F-CD1318BC22D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/33CCCB96-54FD-3742-86D6-AD91EBD324A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/46D4BA35-AF85-8544-962D-8D5B5E080683.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/5161B10D-1B8C-744F-82FC-A3EDAF553FED.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/65401E76-CF46-A640-96CD-8BA3564BD3C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/8A6055EB-1EBE-524B-82EE-9EE6DE9A4EA7.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/CDCD3E23-1AFC-4447-8D69-F5856B0CC882.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/D2A06DEF-98D3-D544-8ABD-296396E618C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/ECEBB42B-C1DC-9641-B9A8-2B7AACEBC226.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/F4F74F99-289F-A642-909D-28F9834274CE.root',
] )
