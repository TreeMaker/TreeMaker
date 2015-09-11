import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/04193251-243B-E511-AABB-00259073E322.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/38A83903-9D3B-E511-8709-6CC2173BBD70.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/44111FB2-713A-E511-927D-001E67397058.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/448E89DB-9B3B-E511-AC1A-001E673973C8.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5645A033-3C3B-E511-9DB0-20CF3027A61E.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/58B26FC0-523B-E511-8BA6-842B2B185AAA.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5CF175F1-9B3B-E511-93D4-005056A8588A.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5ED5A2C8-523B-E511-9F6A-AC853D9DAD0D.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/66033E68-0A3B-E511-A7C3-001E67397314.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9A7B8243-9D3B-E511-A078-0002C92A1020.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9ACCC3EC-523B-E511-877F-842B2B2A7CF2.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AC22120F-9D3B-E511-9919-0002C92DB530.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AE4EAC22-593A-E511-A046-0025902009C8.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F09E9BCF-9C3B-E511-827A-002590FD5A3A.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC1A858A-4E3A-E511-8D0D-002590A37116.root',
       '/store/mc/RunIISpring15DR74/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC278F49-7D3A-E511-A579-001E673969D2.root' ] );


secFiles.extend( [
               ] )

