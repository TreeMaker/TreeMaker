import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/06D13010-CF6D-E511-9E69-C4346BC00270.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0C12DF10-CF6D-E511-AF43-C4346BC7AAE0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0E423006-CF6D-E511-8595-0025905C2C84.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/28D7C408-CF6D-E511-8E6C-549F35AD8B95.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2A3FBA08-CF6D-E511-9D82-549F358EB7B0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2EE13F0A-CF6D-E511-8E8C-549F35AE4F95.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6E8ABB09-CF6D-E511-B125-549F35AD8B95.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/78613009-CF6D-E511-AC5A-549F35AD8BAF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/80BAA30C-CF6D-E511-8911-549F35AD8BE3.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/9064BE0F-CF6D-E511-B427-008CFA1CB740.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/9802430D-CF6D-E511-84AE-001B21AEEF2C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A457F90E-CF6D-E511-8912-008CFA0A5A10.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BC32740F-CF6D-E511-A53A-549F358EB755.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C27E3209-CF6D-E511-93A6-549F35AD8BAF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/CAA4440A-CF6D-E511-A6AA-549F35AE4F95.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/CC0F430D-CF6D-E511-99EC-001B21AEEF2C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E2097D0E-CF6D-E511-BFBC-008CFA0646A4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E2D05F0F-CF6D-E511-9321-008CFA0A58F8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/F037710B-CF6D-E511-87AA-C4346BBCD528.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/F089E21A-CF6D-E511-9D22-00266CFFBF80.root' ] );


secFiles.extend( [
               ] )

