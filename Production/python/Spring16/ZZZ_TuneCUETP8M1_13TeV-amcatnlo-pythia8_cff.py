import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/401B30E5-CA04-E611-A086-0CC47A6C1034.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/B2BC9AF2-CB04-E611-9FD2-C4346BC75558.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/F2543681-C904-E611-B322-24BE05C63631.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/3EBA0FA7-5F04-E611-9B6E-90B11CBCFFF7.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/76F3C5AD-EF04-E611-9C6C-B083FED42A1A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/96A22CA5-EF04-E611-A9D5-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/AE61BB9E-EF04-E611-AAB0-008CFA1112F4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/BE37BCEE-EF04-E611-84C6-001E67D195F0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/CE6A19B8-EF04-E611-83D8-0025901D08BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/CE6B471F-0405-E611-90C2-34E6D7BEAF28.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/F46408B8-EF04-E611-9AFE-6CC2173C3DD0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/02B1FAA3-4805-E611-823B-90B11C27F383.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1C7A237A-4805-E611-8CAC-842B2B2922E2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/584E40C5-4805-E611-943E-1C6A7A21A8B1.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/76244784-4805-E611-A689-0CC47A13D16E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7A855999-4805-E611-BCFD-0CC47A6C1864.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A42D8456-4805-E611-B149-002590E3A0FA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/B211DC73-4B04-E611-BF91-008CFA000B68.root',
] )
