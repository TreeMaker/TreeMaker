import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/202BC63D-413D-E511-9328-0CC47A13D176.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/2C87B233-423D-E511-AD65-0025905B857C.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/5A994039-413D-E511-8A55-001E673969D2.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/08739465-AD3C-E511-878C-0025904A8ECA.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1092AEE3-AC3C-E511-96B9-002590207C28.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/885AD7FC-753C-E511-84A1-002590E3A224.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/98A92A3A-723C-E511-B56D-90B11C2801E1.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/BA8816C2-AC3C-E511-BFB8-6CC2173BBE80.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/DE0B365A-713C-E511-BC58-00304865C464.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/FAFC862E-803C-E511-BCFC-0025900E3502.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5ADB6412-B73C-E511-999B-008CFA0A56F0.root',
       '/store/mc/RunIISpring15DR74/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B075FF87-B63C-E511-ABA5-001E673975F8.root' ] );


secFiles.extend( [
               ] )

