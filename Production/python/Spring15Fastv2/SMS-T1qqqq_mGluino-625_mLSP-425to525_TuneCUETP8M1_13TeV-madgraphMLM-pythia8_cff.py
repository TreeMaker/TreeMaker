import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/10CEC6CB-AE80-E511-9096-003048FEB8FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/147CEB1F-A280-E511-AEAF-02163E013023.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2C12D22A-A380-E511-83C7-0025904B11AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2ECFC0D2-A280-E511-BA6B-02163E011570.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3001B627-AD84-E511-A969-02163E013480.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3878BF1C-A280-E511-A164-02163E0147C7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3AFBC416-9B80-E511-A2ED-02163E014EE9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/40EA6078-A380-E511-93E1-02163E013D85.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/48B64953-A780-E511-AA25-02163E014B1D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4C1D1C61-A280-E511-A9F6-02163E013EF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/50BFF3AA-A380-E511-82E2-002590494E18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/58013F19-AF80-E511-A902-02163E014F13.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5CB43080-A980-E511-AC39-02163E013EF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5E079854-AF80-E511-B3B2-02163E00E621.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5E6C0B4C-A380-E511-B724-02163E015F0D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6AC929FE-A580-E511-B2FB-02163E014E1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6CEABAF9-A080-E511-BA91-003048F0E858.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/70584D00-AF80-E511-A040-02163E01502D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/768A02EE-A180-E511-85A4-02163E01372D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/86D195C4-A480-E511-93CD-02163E016B40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8AB783A2-A380-E511-A11D-02163E0147C7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8C92B133-A380-E511-B700-02163E016A40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8E7DA143-A280-E511-98E0-0025904B11AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/906F42E7-AA80-E511-BA4A-002590D9DA9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A0D79754-A780-E511-B024-02163E013EF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A4BD2A3D-AB80-E511-B2B4-002590D9D968.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A8E633E5-A980-E511-95E6-0CC47A0AD6E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/ACB37464-9B80-E511-A6E3-003048F0E7BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B6158523-A180-E511-962A-02163E011570.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B6F98AFD-AA80-E511-ACA4-02163E013C4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C6DDBC0F-A080-E511-A829-0CC47A0AD6C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CA03164A-C480-E511-BF17-0025904B26B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D0A4BD74-AA80-E511-A75F-002590D9D8AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DE69A69B-A480-E511-A8DE-02163E013EF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E23DE7B7-A180-E511-9199-02163E0153C5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E2A65EA2-A980-E511-A5A8-002590FD5A48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E6D1E126-9B80-E511-AB9B-02163E01140F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/EAFBFAF6-A180-E511-B3AC-02163E011570.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/ECC11CA9-A180-E511-8E69-001E67C7AF3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/EE01C95C-A580-E511-A7D8-02163E01320C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FAAE5F1A-A280-E511-9FB3-002590494E18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FCB4F2D3-A280-E511-9388-003048F0E858.root' ] );


secFiles.extend( [
               ] )

