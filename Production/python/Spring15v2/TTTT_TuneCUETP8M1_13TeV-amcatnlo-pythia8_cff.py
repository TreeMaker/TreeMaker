import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/24F17409-B36D-E511-B4DC-002590C192A8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/44203278-CE6D-E511-9486-002219558002.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/5AE84AED-D06D-E511-9BC3-001EC9ADC0B4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6AFAE878-BC6D-E511-8292-001EC9ADDDA8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/7AD1A427-B66D-E511-8086-002590C19466.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D0A418AC-AD6D-E511-9C0B-0CC47A1244CC.root' ] );


secFiles.extend( [
               ] )

