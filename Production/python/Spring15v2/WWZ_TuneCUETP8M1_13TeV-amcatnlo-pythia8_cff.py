import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/624BC18A-CA6D-E511-A73B-003048F3511E.root',
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/28AA7693-CE6D-E511-8734-00304853EC42.root',
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3C889C67-CE6D-E511-A2C6-001E6724827D.root',
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/44707864-CE6D-E511-9CB3-001E67247BCF.root',
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/78223968-CE6D-E511-9793-001E672488A4.root',
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D4A91C65-CE6D-E511-AA5C-001E67247FE9.root',
       '/store/mc/RunIISpring15MiniAODv2/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/DE593961-CE6D-E511-B38F-001E672480E3.root' ] );


secFiles.extend( [
               ] )

