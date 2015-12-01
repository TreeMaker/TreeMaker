import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0AD2C65F-5296-E511-9670-00259073E506.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/188CC953-5296-E511-86CC-00259073E4DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2A26EFEA-5296-E511-8084-0CC47A4DED2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2C915554-5296-E511-9415-20CF3027A629.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2CA8AB55-5296-E511-9D13-0025907750A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3CD33AF4-5296-E511-AECE-00259073E3AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3E7C6E98-5296-E511-AB88-02163E00C81E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3EAB4763-5296-E511-91FE-002590747D94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3EE879F3-5296-E511-8670-00259073E4BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/407B2A59-5296-E511-9F40-00259073E4CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4C1F5655-5296-E511-AC2A-00259073E504.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/50208256-5296-E511-A6DD-B083FED1321B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/503CDD5C-5296-E511-AAB2-002590D0AFB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/567C2CF9-5296-E511-9F25-02163E015154.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5811EBE9-5296-E511-9272-00259073E334.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/605F42E7-5296-E511-B5ED-0025907B4F00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/662D15EB-5296-E511-BC57-0CC47A4DED2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6660C765-5296-E511-A8AE-00259074AEE6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/668C8765-5296-E511-8094-00259074AEE6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/68065F5D-5296-E511-BEF8-00259073E3A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6A5DE7F3-5296-E511-AB7B-00259073E3FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6C6217DA-5396-E511-9CA4-02163E011509.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6E78037D-5296-E511-B0F9-02163E00E7E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/70EC53F7-5296-E511-B876-00259074AEAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/74AD3D8A-5296-E511-B99D-02163E015C9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7A2E4D5D-5296-E511-A104-00259073E3D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7E2F2855-5296-E511-A82C-00259073E450.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/82A8E457-5296-E511-82ED-00259073E504.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/84C50955-5296-E511-B51F-00259073E390.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/8CBEBA57-5296-E511-A0EC-0025907277A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/948DE186-5296-E511-B39F-02163E013AB3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/98831B58-5296-E511-8935-00259073E398.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A4876C65-5296-E511-A00B-00259073E4E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AA7F5056-5296-E511-95AE-002590747D90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BAA600E7-5296-E511-AFF6-0CC47A4DEDF6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C41D885C-5296-E511-AFD3-002590D0B0C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C62EFF54-5296-E511-9FC0-00259073E34E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C8BA7F55-5296-E511-B232-00259074AEA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D00819E8-5296-E511-B3D6-00259074AE40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/DA494657-5296-E511-8804-0CC47A4DEE6A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E0BA8DED-5296-E511-B966-002590D0B0D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E495C360-5296-E511-B9F5-003048F0E84A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E89DE7E9-5296-E511-9144-002590D0AFB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F0326B5B-5296-E511-B146-00259073E464.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/FCBB5752-5296-E511-945D-0025907B4EF0.root' ] );


secFiles.extend( [
               ] )

