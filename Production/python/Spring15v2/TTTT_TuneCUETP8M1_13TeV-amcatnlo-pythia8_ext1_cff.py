import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/02C0CE7C-9D6D-E511-A3D2-44A842CF058B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/06A74C33-886D-E511-B607-B499BAAC082E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/0AD95D32-E76D-E511-811A-90B11C06954E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/1C8AA29A-9F6D-E511-B054-44A842CFD5FF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/32019F55-886D-E511-9D03-44A842CFD64D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/388D52CE-886D-E511-9D41-6C3BE5B5B080.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/3A708F52-A66D-E511-9F1D-44A842CFD5CB.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/3A861A1C-826D-E511-ADA0-0025905C9726.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/3C8CCFD9-896D-E511-B888-001EC9AEF558.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/46166DBC-C56D-E511-BFCC-B499BAAC09A0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/4665481B-E76D-E511-8BF7-6C3BE5B5C0B0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/4CE03E3F-B06D-E511-BB3D-B499BAAC054A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/527E8B3F-886D-E511-B269-6C3BE5B51168.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/52973BFA-B36D-E511-9B78-B083FED0FFCF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/548A8320-886D-E511-B79F-44A842CFC9A5.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/587D2118-E76D-E511-B7DF-0026B94DBDA2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/58E2ED68-E76D-E511-AFB8-F04DA23BBCCA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/5C2B1FEA-A66D-E511-8878-20CF3027A5A2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/78FED4B5-9A6D-E511-8220-44A842CFD65A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/8A6B97DA-B66D-E511-9207-6C3BE5B56498.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/8E99B4FA-DD6D-E511-9C04-20CF3027A62B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/A2D48E48-AD6D-E511-96B7-6C3BE5B594A8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/A6D5EB0B-E76D-E511-A28D-0025904C67B4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/B4620110-E76D-E511-B74A-00266CFFBF80.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/CAFFA03E-936D-E511-92E5-6C3BE5B5B080.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/CCF4A10B-E76D-E511-AFBC-002481DE4A28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/F25ED510-E76D-E511-AF55-002590D60150.root',
       '/store/mc/RunIISpring15MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/40000/FC9E9F10-E76D-E511-A124-008CFA1983E0.root' ] );


secFiles.extend( [
               ] )

