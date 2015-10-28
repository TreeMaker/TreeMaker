import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/02A7252E-7D7B-E511-B840-00259073E51C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08BEBAFB-7F7B-E511-8697-00259048A862.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08FD5DE7-7F7B-E511-8109-002590D9D8B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A94452D-7D7B-E511-B01A-00259073E4F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1C218AA7-7E7B-E511-83D4-00259073E3AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2048DE96-7E7B-E511-9F81-00259073E51C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A16D02C-7D7B-E511-83FA-00259073E504.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E1ECED4-7F7B-E511-8C64-002590FD5A78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/427D412E-7D7B-E511-B52D-00259073E4F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A6590DD-7F7B-E511-AF12-0025901FB438.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4AA33D2C-7D7B-E511-B9EF-00259073E384.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/58802D2E-7D7B-E511-AA35-20CF3027A5E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5CE28A2E-7D7B-E511-9643-20CF305616EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5EB18388-7C7B-E511-92BF-20CF3056170A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6023EC2D-7D7B-E511-A7AA-00259073E3AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/64F35BDA-7D7B-E511-965D-20CF3056170A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66E2BCAF-7E7B-E511-BDF1-00259073E4CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E6C402D-7D7B-E511-B05D-00259073E53E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/70E0C52C-7D7B-E511-BBFA-00259073E45E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/787C4E2D-7D7B-E511-A66D-20CF3027A5E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A2DB11E-807B-E511-9AAA-0025901FB100.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A49109B-7E7B-E511-A8F9-00259073E4F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82D8CC2A-7D7B-E511-BEF2-0CC47A4DEDAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88956F2E-7D7B-E511-B9AF-002590747E28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CD145B2-7E7B-E511-97C3-002590574604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CEBAF2F-7D7B-E511-9CAC-20CF3027A5E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92AB2F2B-7D7B-E511-AC3E-0CC47A4DECD4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92F929E0-7F7B-E511-A318-0025901AEBD4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A29461DF-7F7B-E511-9432-00304867FE4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A46E2A2E-7D7B-E511-9A44-00259074AE40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6181AD2-7E7B-E511-8312-00259073E4BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6FD5ED0-7E7B-E511-87A6-00259073E53E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A817CDC2-7F7B-E511-A935-0CC47A0AD704.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA5C24BC-7E7B-E511-8538-00259073E504.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B251398E-7C7B-E511-9DC7-002590747E40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA84C294-7E7B-E511-B17B-00259074AE40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC28572E-7D7B-E511-B98B-00259073E4FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC439A08-807B-E511-ADF1-00304867FE5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E23EC5BF-7E7B-E511-BAF9-20CF305616EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E66C8B2D-7D7B-E511-9A51-002590574604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E67E91BE-7E7B-E511-A1D7-00259073E45E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6E9672E-7D7B-E511-A749-20CF305616E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8686B2C-7D7B-E511-91A2-0CC47A4D9A2E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC8A012A-7D7B-E511-A922-20CF3027A631.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0CD3B00-807B-E511-856E-00259029E87C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4F005D5-7D7B-E511-87CE-002590747E40.root' ] );


secFiles.extend( [
               ] )

