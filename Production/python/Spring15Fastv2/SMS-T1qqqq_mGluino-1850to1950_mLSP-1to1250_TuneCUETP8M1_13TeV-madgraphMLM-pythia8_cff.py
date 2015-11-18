import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/00FBF132-FD82-E511-9BCE-02163E014914.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0C05E4C8-FF82-E511-B86C-20CF305616E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/187FB86B-FD82-E511-9CBA-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1AE42E6B-FD82-E511-8C80-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1E0BB86B-FD82-E511-BC94-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/241375F1-B484-E511-AA39-E41D2D08E0C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/24142E7F-0083-E511-94B8-00259073E4F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3478AEF2-B484-E511-B831-002590AC4CC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/38651E05-B584-E511-A0A3-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/44B8ACF4-B484-E511-A7F3-F45214938690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4EB64B38-FE82-E511-ADCB-00259073E390.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5643A76B-FD82-E511-A74D-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/581AF5F4-B484-E511-90EB-F45214938690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5C817B34-FE82-E511-872E-0CC47A4DEED2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6018D1F4-B484-E511-8660-F45214938690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/64D24422-FD82-E511-AA99-02163E014C40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6C09887E-0083-E511-B21B-002590D0B0C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6E8EDBF2-B484-E511-9488-002590AC4CC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/70639D5E-FD82-E511-AD58-00259073E4F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/70ADC9F2-B484-E511-BD21-E41D2D08E060.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/70DD877E-0083-E511-8B25-002590D0B0C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/72FDFCF4-B484-E511-BEFA-F45214938690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/749FE878-FD82-E511-8D5D-005056020785.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/76DFC76B-FD82-E511-BF2B-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/78B6DEF4-B484-E511-8EBD-F45214938690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7A08CF69-FD82-E511-A039-002590D0B052.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7AF1C3F5-B484-E511-86ED-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8083B934-FE82-E511-B076-00259073E334.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8695B737-FE82-E511-90EC-00505602078C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/86AFF46D-FD82-E511-8338-20CF3027A611.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/889F5075-FD82-E511-9780-00505602078C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8C25E42A-B584-E511-BED1-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8CB3C7F5-B484-E511-9235-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92F4BEBC-FC82-E511-A228-02163E00B3F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92F6D3F5-B484-E511-880C-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/98DCFA38-B484-E511-9B5C-002590DB053C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9A958F29-B584-E511-A087-F45214938690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A228026C-FD82-E511-BA66-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A411CC33-FE82-E511-B638-0CC47A4D9A3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A43BCC69-FD82-E511-A673-20CF3027A600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A4B4C7F5-B484-E511-87B4-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A6DEEE6A-FD82-E511-9A93-20CF3027A600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AE2DC96B-FD82-E511-B18C-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C2C9C9F2-B484-E511-A40D-E41D2D08E060.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C8814D37-FE82-E511-B2A0-20CF305616E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D63B936B-FD82-E511-857F-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D63DE4F5-B484-E511-847A-0025907BAD4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D68740F5-FC82-E511-B117-00259073E344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D8E4706A-FD82-E511-9627-20CF3027A600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DC3F43F5-FF82-E511-89CF-00259074AE6A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E050D36B-FD82-E511-8911-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E4FE6003-FE82-E511-9D80-0025905964C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E60A23F3-B484-E511-AB03-E41D2D08E060.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EA7EEA2B-FD82-E511-901F-02163E014A0B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EC37E1FB-FD82-E511-A2F9-0026189438E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EE914F6E-FD82-E511-B3A8-20CF305616CC.root' ] );


secFiles.extend( [
               ] )

