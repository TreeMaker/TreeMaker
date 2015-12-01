import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/04ABE4B5-E895-E511-B103-02163E00B2BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/06814739-E995-E511-A813-02163E00F33B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/08D5D7DA-E895-E511-A6E4-02163E013A08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0E3A97D8-E895-E511-A1AF-02163E016718.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/183725D0-E895-E511-B461-02163E013BE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/184F84EA-E895-E511-9AC6-02163E016C2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1C7824E6-E895-E511-99B8-02163E016A78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/207B64EF-E895-E511-B6BD-02163E00ACB3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2294C211-E995-E511-979B-02163E016724.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/24E65AEE-E895-E511-BB17-02163E015CC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/26D25AF1-E895-E511-A022-02163E016802.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2C0E520D-E995-E511-AE26-02163E011638.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/34836509-E995-E511-8295-02163E016B98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/38E836CA-E895-E511-9BD2-02163E013D7B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3EF0E92B-E995-E511-9946-02163E00E9E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4226DBFB-E895-E511-988C-02163E016C02.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/447CAFFC-E895-E511-ADF8-02163E016BE9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4485E98B-E995-E511-9B56-02163E016C35.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4603B8CF-E895-E511-8EBF-02163E010CEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5079DEEC-E895-E511-B4F6-02163E0169C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/62B714EE-E895-E511-B910-02163E015CCE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/66F46614-E995-E511-BFB0-02163E010FE9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/74CF3516-E995-E511-9D6D-02163E011449.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/789B57DE-E895-E511-8614-02163E0130AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7C1E28F0-E895-E511-B52A-02163E015C72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/885A3BDB-E895-E511-A199-02163E00BC67.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/8CB1A4CB-E895-E511-8E86-02163E013CC7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/921F7AF0-E895-E511-B988-02163E014D33.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9443D2CC-E895-E511-AD3D-02163E00E5D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/963441BB-E895-E511-84D2-02163E00AE7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9EACFACC-E895-E511-87F7-02163E012E7D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A0AA50C7-E895-E511-8E4D-02163E010D15.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A22C1AD9-E895-E511-B607-02163E00C035.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A28E22C4-E895-E511-A326-02163E010E7D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B4B6A402-E995-E511-B0FB-02163E0149F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B6DBCDD0-E895-E511-9DE9-02163E010CC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B8DB87E2-E895-E511-9A06-02163E00C4C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BC1493EF-E895-E511-A98A-02163E00EB23.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BC9A1EDE-E895-E511-81FF-02163E0152CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C645C4FB-E895-E511-B759-02163E01676A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C872DDBD-E895-E511-9AD4-02163E00BE78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D4F6CEFF-E895-E511-BF41-02163E014AB9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D8AD72D8-E895-E511-82CF-02163E013E60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/EED9E3D9-E895-E511-8D8B-02163E013AD5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F0CAEF16-E995-E511-9DDD-02163E00F3F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F277A9EA-E895-E511-B4E6-02163E013DDB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F4D0FD03-E995-E511-AE8E-02163E016B89.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/FC449BF4-E895-E511-B1BD-02163E00BBC0.root' ] );


secFiles.extend( [
               ] )

