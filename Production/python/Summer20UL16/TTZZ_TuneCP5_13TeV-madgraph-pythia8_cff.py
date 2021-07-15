import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/054DE1F2-BD86-3042-8F46-2B32D70AB8CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/0941761D-938D-1E40-8177-BC7679AE6571.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2750F759-68C8-534A-B8D9-4BB920916001.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2A28E0A8-F841-F940-A05A-9B2A08AD9F62.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/458EF37A-FF91-3A46-B145-253DE1D203A5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/46B6BD34-19A5-454F-B568-3B69B86A8C24.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5440DE99-AB62-A842-9B78-51E894DB9A65.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/56B69F50-10FE-7B40-9462-26C6686375CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5F3D5B28-6C5E-604F-BF51-4EFF54F06A27.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/62A0BBEC-94D4-1E45-B41A-769A1703B6E2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/63D086BB-B584-AC45-800C-F4D8C0B30697.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/681835B4-7A7B-864B-AA89-2E09FEE36BDA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7266CB54-1A16-EE4B-899A-1302630BFBF2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7548CBB3-8DE4-3843-8B8A-1E48D6475C0E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/80D40C5E-3BDE-0E4A-A3D1-92154B59FD84.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/84220FBB-9142-E746-81FA-720333062487.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/95F758F1-DA23-A345-9791-D78B215E4CA6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9C3E14B3-7D36-CA4E-BC0A-F9C21DD3D1E7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/A0703EC1-D1C1-EC42-AC74-0A53D14FEE06.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B1837771-3457-954F-9089-DC8F389DFC82.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B35EBE54-CA31-A646-8735-4A99A371200B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B6B31296-2641-E14E-B7CC-5E138516744C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B9D9F111-8087-B94F-9720-B2B4684A8743.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C6D01661-F8D1-9E47-B4CC-27008006B4BE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/FBBA3263-5D6E-504B-891F-AB1A2A7F289B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/FDBA2063-F50D-2146-A01B-C751D10B82EB.root',
] )
