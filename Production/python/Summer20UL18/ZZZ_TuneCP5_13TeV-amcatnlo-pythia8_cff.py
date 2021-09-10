import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/6BFF3C75-0EC1-1746-991A-4D4A72F23348.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/734B456A-C201-F142-A830-379060C93244.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/8E78BEA8-FF23-7B45-AD4E-CC25137403C4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/206F4343-F2CC-3A49-9BF3-063DE94094ED.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/EAFE9BD9-CDB5-0B4B-9A33-74DA81785A05.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/136FFF51-9641-0E4A-8BE2-33A08813301B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/5731E0A3-4707-3C4D-845E-1E50878BA604.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/74E519C2-3862-564C-A647-B996661DE75C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/75F24EB9-124A-4943-8080-B673CBC53DCB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/CE153B40-6E7E-D644-BF16-4825219FBC3D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/2D0546EC-AB3C-5F4B-90C9-C16ABB8AB692.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/4DD7B277-EA11-EA4D-929F-36A8FCBFC41B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/A5C339DA-DA58-2840-BD04-97D12708FC03.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/A93F18EE-B771-2148-8A04-CB59C0335F95.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/FC405A4F-2287-B449-A342-C77DBE9AC4EF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/645004C7-E8F6-0347-899B-C570975AECD3.root',
] )
