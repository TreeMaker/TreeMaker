import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/103B1BD8-DC61-E511-8867-3417EBE539DA.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/12CE96E0-DC61-E511-A8BE-C4346BC8D390.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/16798DE0-DC61-E511-8076-842B2B766849.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/1C845CDD-DC61-E511-B504-D4AE5269F656.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/60A767DE-DC61-E511-BCEC-D4AE526A0AB5.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/9447EC80-DC61-E511-8E9F-00259073E4E4.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/AE0A637C-DD61-E511-89E6-002618943935.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/CE85B57F-DD61-E511-9D23-0025905A60DA.root',
       '/store/mc/RunIISpring15DR74/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/60000/CEAA28F7-DC61-E511-A968-D4AE526A03AD.root' ] );


secFiles.extend( [
               ] )

