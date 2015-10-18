import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/10280607-CA6D-E511-B615-00259073E43E.root',
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/36896606-CA6D-E511-9F67-20CF305B05EA.root',
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6488FD19-CA6D-E511-9DCC-0025902BDC78.root',
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7CC53A05-CA6D-E511-AD85-20CF3027A662.root',
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B84AEE03-CA6D-E511-9BB1-20CF3027A5B8.root',
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C8D5AB0A-CA6D-E511-A15E-005056020781.root',
       '/store/mc/RunIISpring15MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D6A77E07-CA6D-E511-A832-20CF3027A663.root' ] );


secFiles.extend( [
               ] )

