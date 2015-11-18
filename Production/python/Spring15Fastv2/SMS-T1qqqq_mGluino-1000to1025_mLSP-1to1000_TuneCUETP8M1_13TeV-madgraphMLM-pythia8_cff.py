import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/00595482-007F-E511-9065-02163E016A5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/04FA3907-007F-E511-A3AB-02163E0167E3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0816C9DF-FF7E-E511-9786-0026189438D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08891719-007F-E511-80E9-02163E00F4A1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0AFC2D7E-007F-E511-AB53-02163E010DEF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/108673E0-FF7E-E511-95D9-AC162DA6E2F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1821F9FD-FF7E-E511-89BB-00215A490902.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/201EC4E2-FF7E-E511-9DE7-0025905A60F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CCD87E1-FF7E-E511-AA46-002618FDA28E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2E55F020-007F-E511-8994-02163E00F44F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/383A9CE0-FF7E-E511-BB6A-0030487C1174.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4268E9F1-FF7E-E511-8ED6-02163E0148C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A02CFE2-FF7E-E511-ABD7-0025905822B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5434EBDF-FF7E-E511-A27B-AC162DA6E2F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5698CA3F-007F-E511-884E-02163E014FA5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E2A5EE5-FF7E-E511-AFBE-0025905A48FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62B7FBE3-FF7E-E511-849A-0025905B85D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82A12352-007F-E511-B2BC-02163E00B3F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88924D59-007F-E511-A67E-02163E010FE7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E6E0A74-007F-E511-A95B-02163E011577.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8EE27D9B-007F-E511-B572-02163E013EE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/908A4C32-007F-E511-90CA-0022640671F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92C30B7E-007F-E511-91D7-02163E013A0D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/98E95198-007F-E511-B4A0-02163E016947.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6A6ECE2-FF7E-E511-B640-0025905A60A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6F14368-007F-E511-A95D-02163E00EABD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AAA1A764-007F-E511-B120-02163E014E7B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AEDE0DE6-FF7E-E511-92D1-0025905A60DE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AEE486E4-FF7E-E511-9112-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8223B10-007F-E511-BEE9-02163E010DB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8E37974-007F-E511-8ABE-02163E0168F1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA5BE264-007F-E511-9DE0-02163E01147F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BE3193E4-FF7E-E511-B8EF-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D851DEE1-FF7E-E511-9148-00261894382A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC002EE4-FF7E-E511-B5D4-00215A45F882.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E26352E2-007F-E511-A30E-02163E016740.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4423FE3-FF7E-E511-B272-0022640671F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC336A46-007F-E511-A150-02163E010C29.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECCAFFE7-FF7E-E511-89CC-0025905A60B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE20F099-007F-E511-9620-02163E01146B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F09FA5E1-FF7E-E511-9F1A-0025905A60E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F21B14E1-FF7E-E511-BC9A-0026189438DF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F46CCAF0-FF7E-E511-B14C-0025905A60BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4A8F2E6-FF7E-E511-9226-0025905B85D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6019FE4-FF7E-E511-9B0E-0025905A612E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8201BDE-FF7E-E511-A411-002618943949.root' ] );


secFiles.extend( [
               ] )

