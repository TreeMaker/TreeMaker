import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/4656455F-7D46-E511-8F4C-002590E2DD10.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/544F5198-4843-E511-9A7B-B083FED00118.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/6CEEE3ED-EF42-E511-B9C2-20CF3019DF03.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/92141161-7D46-E511-8954-0CC47A13D110.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/A43ECAA5-1443-E511-9EF7-047D7B2E84EC.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/A81DD0F4-1843-E511-8A0D-842B2B7680DF.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/B2EAABB1-7D46-E511-B55A-008CFA197B6C.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/C27FA881-4742-E511-847B-D4AE526A0A7B.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/C4290FA0-3442-E511-9D84-001E67A3E8CC.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/E4D6E87A-7142-E511-A717-001EC94BFB39.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/F42203B1-1443-E511-B7FB-90B11C08CA45.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/F6996CC5-1E42-E511-85E8-00269E95ACE8.root',
       '/store/mc/RunIISpring15DR74/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/F8E8E54A-1A42-E511-B87C-00259073E4B6.root' ] );


secFiles.extend( [
               ] )

