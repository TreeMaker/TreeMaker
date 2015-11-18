import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0ABB7FA4-9580-E511-8884-02163E0169FB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0AF77E76-6F80-E511-A22C-02163E013DE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0C37BAD3-6C80-E511-AEF0-0025902CFC3E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0CDE35A1-9080-E511-BA7E-02163E014F6A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/12686C48-B480-E511-9F43-02163E00B5EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1A7631C8-5E80-E511-9A04-F45214C748D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1EE012A5-8280-E511-B1BF-0002C92DB4CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/244BA266-6680-E511-96E6-02163E00BFC5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/26C6CD13-6680-E511-820B-02163E010CED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/32D678D1-6380-E511-AE46-02163E010CED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/365BDC6E-6180-E511-9AE1-02163E00EAA5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/461D006C-6480-E511-9A1C-02163E013108.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4ACE2D48-8280-E511-86D2-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4C6809A8-8280-E511-BC40-0002C92A1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/669BD5EC-5B80-E511-BD4F-0002C92DB4CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6C7D4204-7C80-E511-8710-02163E01487D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6EDB94A6-9080-E511-BBEE-002590494C38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7284F57D-5B80-E511-8546-02163E016846.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/728664F6-4E80-E511-8923-0002C92DB4CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/765A88C4-CF80-E511-B758-02163E0117DB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/82812E3D-6A80-E511-BCDB-02163E016747.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8478D1D6-9380-E511-96F0-02163E0114A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/848595CF-1C83-E511-9445-02163E010F93.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8673F9E4-5B80-E511-871A-5065F381C251.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8ABCD4C8-9080-E511-9C4F-02163E0169FB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8C10BFAB-9F80-E511-B353-02163E0135E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8C39E8F2-5B80-E511-845C-F45214C748C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8E0B7231-6F80-E511-8666-02163E01507A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/92CE1B54-9080-E511-BCC1-02163E014FA5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/964C00E2-5A80-E511-972B-02163E00EA20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/98B8D076-4B80-E511-9F85-02163E00EA06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9CDAFB6A-5B80-E511-8416-0025904CF972.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A6828C75-9580-E511-AE9C-02163E013EBE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B4FA51C1-9480-E511-A666-0025902CFC64.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B614B98D-9080-E511-90BE-02163E016B89.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B649B04C-4B80-E511-A603-02163E00F4F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B6F3FCC9-6380-E511-AA7E-02163E00EAA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BE728F03-6680-E511-9194-0002C92DB4CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C879C042-6C80-E511-9741-0025902CA976.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D0F72CA9-9580-E511-8063-02163E015FEB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DCBF40EA-4E80-E511-A506-24BE05C63651.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DEE52716-5A80-E511-B3D9-002590494DCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E29241C9-5E80-E511-B3EB-02163E0139E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F2AAFF6A-9080-E511-AA20-02163E016BC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F4BBF7A5-9F80-E511-A784-02163E016B62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F60A83BF-5E80-E511-B928-0002C92DB530.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F62F7F42-6A80-E511-9934-02163E00EB08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/78634B4F-D18A-E511-BB44-0025904CF050.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A89A7F3F-2D8A-E511-B9B0-02163E014B9E.root' ] );


secFiles.extend( [
               ] )

