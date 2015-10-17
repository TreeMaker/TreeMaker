import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/0C34C895-CB6D-E511-A27F-008CFA197CA4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2EF76AD1-CB6D-E511-B368-008CFA197990.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3C55E42E-CA6D-E511-90AE-008CFA1979EC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/503D00CB-CA6D-E511-944F-008CFA197A80.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7C43A165-CB6D-E511-B923-00266CFFA240.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/80EE8C2B-CA6D-E511-8136-008CFA19743C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/82799792-CB6D-E511-9C92-008CFA111148.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/829E7ADA-CB6D-E511-9022-008CFA197D14.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/86120E98-CB6D-E511-B552-008CFA010E1C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8A2977DC-CB6D-E511-8C46-008CFA165F48.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8EDFD99C-CB6D-E511-B195-008CFA110C94.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/98B38ACD-CA6D-E511-9B0B-008CFA197948.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/98D9BBDE-CB6D-E511-A920-008CFA165F48.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A663CA60-CB6D-E511-A2CA-008CFA010718.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BA0C1F9A-CB6D-E511-BCCC-008CFA166188.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D67FFA93-CB6D-E511-ABA2-008CFA1661B4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/F0B2DE94-CB6D-E511-8B64-008CFA197CF0.root' ] );


secFiles.extend( [
               ] )

