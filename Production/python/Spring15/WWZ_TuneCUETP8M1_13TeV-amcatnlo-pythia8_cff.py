import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/2258B3DA-3963-E511-B949-002590E39F4E.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/36C58CDF-3963-E511-A7B5-0025907253D2.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/3E1AC4DC-3963-E511-ACFF-002590D60068.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/5276C5DE-3963-E511-899F-0CC47A13CB62.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/7C8884D4-3963-E511-ABA6-0025904C66A4.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/ACA59CDD-3963-E511-84BF-0CC47A13CB18.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/DC37E8D9-3963-E511-A07B-002590D60068.root',
       '/store/mc/RunIISpring15DR74/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/F0A027EB-3963-E511-9D15-00266CFFBC3C.root' ] );


secFiles.extend( [
               ] )

