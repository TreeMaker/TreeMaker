import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/0AA900B8-E6FC-E511-AE56-A0369F3102B6.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/22D7AC7D-EDFC-E511-9C04-000F530E46D0.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/26FA44D2-A6FD-E511-808B-0CC47A4D7628.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/28B49F6A-61FD-E511-981C-0CC47A1DFE60.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/32536445-05FD-E511-8279-0CC47A4D7628.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/3A21DB7E-EDFC-E511-9D95-008CFA502F76.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/42E8C110-87FD-E511-83C6-6CC2173C9150.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/48192ACA-A6FD-E511-A7BF-5065F3815241.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/48DAE0F5-F9FC-E511-BEA8-44A8423C4026.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5EF0BB47-0AFD-E511-B18C-001E688629D2.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/66306F58-9EFD-E511-A4E8-44A84225CABC.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/743DD2EB-CEFC-E511-9955-24BE05C49891.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/76F1F196-9DFD-E511-A5F3-001E67A3FD26.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/7E238F6A-F8FC-E511-8A7A-24BE05C3CBE1.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/80EBD8CA-A6FD-E511-AA87-0090FAA58BF4.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/8E1078F9-CEFC-E511-AF2F-0002C94DBB20.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/A6180F17-FFFC-E511-A6F6-0025905A48D6.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/AC9AF8CB-23FD-E511-A6F1-0CC47A1DF7FE.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/B42BC2E7-E6FC-E511-86D9-A0369F310374.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/C83BB23B-A1FD-E511-B22F-0CC47A00A832.root',
] )
