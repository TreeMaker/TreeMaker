import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A083DFC-CC82-E511-A65A-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A6E82FB-CC82-E511-AD5A-0025905A6082.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0C0B7BFA-CC82-E511-9E0C-002618943980.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CDE96FC-9582-E511-B9A8-0026189438D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0E970D0E-CB82-E511-A648-002590596498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/14713F10-CB82-E511-8383-0025905A60B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/14754FDC-CC82-E511-B950-002618943800.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/14C0D9FC-CC82-E511-BEFA-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1807C211-CB82-E511-80A6-002618943800.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/28F15767-CC82-E511-B16C-0025905B858A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2A57A92D-B682-E511-A09B-0025905964BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EBE58FC-CC82-E511-8F13-0025905A4964.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EEDBD0F-CB82-E511-B922-0026189438ED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/34485E62-CC82-E511-A13F-002618943869.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/34C19B11-CB82-E511-A876-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38940C0B-CB82-E511-9691-003048D15E36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AB93010-CB82-E511-8210-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AC3EC0D-CB82-E511-97FC-0025905A6110.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3EF782F7-CC82-E511-ABF6-0026189438E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C272E0B-CB82-E511-A411-0026189437EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50380C0E-CB82-E511-A4A7-0025905A608E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/509173FB-CC82-E511-97D8-0025905A60B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/52BB82F7-CC82-E511-A223-0026189438E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/628131FA-CC82-E511-BBC5-0025905A6080.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62F7BA7B-C482-E511-A782-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/649767FC-CC82-E511-8AC4-0025905A6132.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/64A0800E-CB82-E511-93C4-0025905A605E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/760419F1-CA82-E511-B186-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/768BC8F9-CC82-E511-84D9-0025905A6110.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80567DF7-CC82-E511-84DF-0026189438E7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8098880B-CB82-E511-9E67-002618943869.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/820CABB9-CA82-E511-B35F-0025905938D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8411CE73-B482-E511-B702-0025905A60CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E21650B-CB82-E511-ACAC-002618943869.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9CF964AF-B482-E511-A33E-003048D25BA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A054D10E-CB82-E511-BEE2-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A0A9A210-CB82-E511-ABBE-0025905938A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA7E3611-CB82-E511-8D34-0025905A4964.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AC6AEA0A-CB82-E511-85CE-003048D15E36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AC7D1BFC-CC82-E511-8E33-0025905A60B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ACD866AF-B482-E511-9704-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AEC2A9FE-CC82-E511-B5B6-0025905964C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B02C312A-9A82-E511-87A1-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B21112C1-CC82-E511-8481-003048D15E36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C22D220E-CB82-E511-BE8B-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE6F5910-CB82-E511-AA29-0025905B859E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DACCC90E-CB82-E511-B15D-0025905A609E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E04A1581-CA82-E511-9F0A-0025905A497A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E61092EB-9982-E511-928E-003048D25BA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6235912-CB82-E511-91DA-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE17291A-9D82-E511-AE1E-0025905A48D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA4D3CB8-CC82-E511-AEDF-0025905A60B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA8E73FE-CC82-E511-9EE9-002618943875.root' ] );


secFiles.extend( [
               ] )

