import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/02B4176C-9A7B-E511-9F34-00259073E466.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2AED5A6D-9A7B-E511-B380-20CF305616E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4E08846E-9A7B-E511-9EDB-002590747E1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/50428815-9A7B-E511-A899-001F2965D442.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/74BFFBA6-617C-E511-A1F9-001E67E71BDC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/788715A8-617C-E511-BC45-001E67E6F80A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/88028E6C-9A7B-E511-88F0-20CF305B057E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8808A56D-9A7B-E511-8087-20CF300E9ECF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/88A3EEED-997B-E511-82F8-002590760A10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8C9CE36E-9A7B-E511-9DCB-20CF305B056C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/981A0B6D-9A7B-E511-B601-00259073E410.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A678D66C-9A7B-E511-B817-00259074AEC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A897336C-9A7B-E511-82AB-00259073E3E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/AA9497AA-617C-E511-9E68-001E6739723D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CC2CF217-9A7B-E511-A184-00259073E520.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CCC55CB0-617C-E511-A437-002590A88736.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DAA7D26C-9A7B-E511-B295-00259073E4CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DCF3C86E-9A7B-E511-886A-002590747E28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E05E0B6D-9A7B-E511-9C67-00259073E4AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/EC03526B-9A7B-E511-8174-002590747E40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FA325E6D-9A7B-E511-9661-20CF3027A5B5.root' ] );


secFiles.extend( [
               ] )

