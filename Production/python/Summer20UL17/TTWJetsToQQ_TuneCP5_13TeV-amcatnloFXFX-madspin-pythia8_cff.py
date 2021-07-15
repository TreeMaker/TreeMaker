import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/042FB673-061B-FA4C-B828-7DEE264E6076.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/0C4F8377-0EBA-0B4E-A559-AD04F6696A0D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/23D63902-E142-394E-906B-D42214340343.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2DB4E432-63DD-0F43-AE41-FE84170543A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2FFE4D42-5221-7748-B833-32BABE50C293.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/3F608C26-4575-044F-A54B-D6C1D6F8937D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/4027BBD3-7C8F-E34C-A0F7-A8B75B478F92.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/540B3E3C-914F-0A48-86C6-8360DFD01146.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/55B9E899-F2EF-9843-A4A7-D39E32FE221F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6873F257-23E6-3744-916B-D8C4A90C8780.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6A86D56D-E0C4-D44B-9B23-514B22628594.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/73A43280-4D00-F841-8C3D-3777D1F47E75.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/7C716454-DF23-0441-AAE5-6BA7606A6FC4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/7FB901E0-242E-5548-9E2D-F80D631FA400.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/83F5B19A-660B-5B49-979F-9144ABBCE2A5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/91C23D4C-B401-9041-AD74-EB4DD2269D6B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/972449FB-5818-0A44-AFAF-BC0EF66A283F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A975CB8D-3992-DB49-9B57-4254EE7101A9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/B51CF2C2-B44F-534D-A327-9BCF31C2D238.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BA33C27F-2E80-A149-B37A-752900539A0A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/BDA70FE3-8ED9-D046-B543-C3D35F9B7302.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C4A69B12-3A91-DF42-B364-5F1D16204DD7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C77D72B1-4C57-5449-83B7-D44A035A0830.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DAF55A60-DA4F-0B49-84E1-F617A8999885.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DD624B9E-F4EC-7E47-A7AD-2CEB1624278F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DEA05783-37D4-5944-8071-51D55CD515C0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/FC3A1007-8185-464C-A1EF-0065771C8EB6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/55CF1CBF-E559-1241-8FF3-FF2826B445CB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/2710000/F252967B-4918-D24A-9D78-F9DC7C598FC2.root',
] )
