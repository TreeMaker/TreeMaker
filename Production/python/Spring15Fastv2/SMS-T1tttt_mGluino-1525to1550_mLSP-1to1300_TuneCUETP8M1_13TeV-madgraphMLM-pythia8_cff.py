import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/02E0BE58-FA7E-E511-913D-002590D94F8E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/086E2766-FA7E-E511-A02E-047D7B881D98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/10C5A4B1-FA7E-E511-B1C5-002590DB91CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/10D4A56A-FA7E-E511-B61F-00266CFFA5C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1C7E7DAF-FA7E-E511-9A45-002590DB921A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3A316D58-FA7E-E511-9252-002590DB041E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/46068C58-FA7E-E511-B773-002590AC4B5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4EA4576E-FA7E-E511-9F19-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/50DBC963-FA7E-E511-B9EE-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/521DBA5C-FA7E-E511-BF9C-E41D2D08DD10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/56494BB9-FA7E-E511-9002-00266CF32E70.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5A66C95B-FA7E-E511-9893-002590DB9216.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/605FDC5D-FA7E-E511-8A84-047D7BD6DE44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6078D163-FA7E-E511-B8B1-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/648F045C-FA7E-E511-86EB-002590DB053C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6CF41D58-FA7E-E511-878B-00259073E3AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6E30B5AA-FA7E-E511-8927-0025907FD3CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7653B458-FA7E-E511-8188-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/789FB25C-FA7E-E511-99E2-002590DB923C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7A89D854-FA7E-E511-88E9-0CC47A4DEDE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C9EAFB1-FA7E-E511-A379-002590DB91CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7EE87266-FA7E-E511-A761-0025901D4B06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/865C395B-FA7E-E511-BFFB-047D7B881DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/887AC85B-FA7E-E511-86F8-002590DB91BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/88DCD95B-FA7E-E511-A429-002590DB921A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/96851307-FA7E-E511-8B15-0CC47A1E048C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/96963D5D-FA7E-E511-A430-047D7BD6DDF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9A26915C-FA7E-E511-9284-E41D2D08DDB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9A652061-FA7E-E511-9556-00259074B2BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9ACB0557-FA7E-E511-A25C-002590AC4C72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9E6BBBAC-FA7E-E511-8EC7-002590A2CDA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A0B4F95A-FA7E-E511-88A6-E41D2D08DD80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A4D82EAD-FA7E-E511-8B41-002590AC4B3E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A826255B-FA7E-E511-800F-002590AC4FE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A8D44B59-FA7E-E511-BA72-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B6A8B959-FA7E-E511-85DF-0025907FD2DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B8725D58-FA7E-E511-947B-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B8CBCC58-FA7E-E511-B821-00259073E3AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BE33CBAA-FA7E-E511-9E52-0025907FD3CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C016A361-FA7E-E511-BC55-002590DB9298.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C83266B1-FA7E-E511-B2A5-002590DB91CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CCE0A268-FA7E-E511-BF36-0025907DC9C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D8FF0765-FA7E-E511-AFEB-0025901D4844.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DA910D58-FA7E-E511-BC4C-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E80AE459-FA7E-E511-920C-00259073E344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/ECF26AAF-FA7E-E511-BC81-002590DB921A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F6462358-FA7E-E511-8967-0025904B5FB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FCA6066E-FA7E-E511-8778-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FCBD7BB9-FA7E-E511-A61F-00266CF32E70.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FCFAC7B7-FA7E-E511-B376-00266CF422D8.root' ] );


secFiles.extend( [
               ] )

