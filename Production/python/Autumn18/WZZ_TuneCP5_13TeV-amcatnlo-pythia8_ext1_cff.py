import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/078A4263-8824-1947-BA18-2E38D7B34E49.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/2F0C4E7B-1AC8-CD4B-B48C-1D5865E808EA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/337D2348-7DA7-CE43-8B26-FBAD409323A3.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/6DB7F3BB-8FB7-7F43-9288-9B9A0700F467.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/729C8C73-53AA-BB49-ABAD-BEA181339608.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/7835DDC8-BFAA-9444-ADB7-7C48CA21F02F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/8A3E8BD4-EEDC-DC4A-B953-22C0510D24C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/8B685E81-B7D0-FE45-9CBB-C01AED547612.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/A02FC65A-32A4-D944-90CE-AB10FB651057.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/B3EB0A3D-C1F1-804E-A905-4F7A2E50DD1B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/B7AB7994-0C8C-1344-8935-55D5CFBCE718.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/B7D24C3B-991A-AA42-B9B3-90DA9597EDB4.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/BDD2DD82-55CD-1044-BA26-B6F58A6F1C3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/5D433CA2-4D67-4E48-82FA-80AD411F72F7.root',
] )
