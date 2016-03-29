import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0AC70F07-6C7E-E511-A56B-0CC47A6C1806.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CB679D3-6C7E-E511-84BA-0030488D0062.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/12CE0F47-907E-E511-AC3F-0CC47A0AD6AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2200DEC8-6C7E-E511-9755-0CC47A6C063E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/246C0309-6C7E-E511-A40B-0CC47A13CEF4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2693600F-6C7E-E511-875D-0CC47A6C063E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/28AF7207-6C7E-E511-B28C-0CC47A6C17FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3EBFBF5C-6C7E-E511-AC0C-002590D9D92A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/427C9A98-6C7E-E511-8476-00304867FE3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/42BBCF06-6C7E-E511-9DC9-0CC47A6C138A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5097A60E-6C7E-E511-8F59-0025904A96BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/623E4B3D-6C7E-E511-B53E-90B11C2AA388.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/702F7503-6E7E-E511-AFE6-0CC47A0AD4A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/764A1D0F-6C7E-E511-9B05-0025907253E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C373509-6C7E-E511-9971-0CC47A6B5B20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A00F95E-6C7E-E511-84A7-0CC47A6C1060.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A29FF1B-6C7E-E511-AA66-0CC47A13D416.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8C55750E-6C7E-E511-896C-02163E011924.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/90F7AD61-6C7E-E511-BD70-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/921DD206-6C7E-E511-89D6-0CC47A6C06C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92AE250E-6C7E-E511-B196-0025901D08B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92AF220B-6C7E-E511-BF5D-002590E39D8A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96826EC0-6B7E-E511-ACC3-90B11C2AA430.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6B2E805-6C7E-E511-B193-0CC47A6C138A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AC909619-6C7E-E511-BF20-0CC47A13D3A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE22B80E-6C7E-E511-B48F-90B11C27E14D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B24F0509-6C7E-E511-9585-0CC47A6C1866.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC81D709-6C7E-E511-9A00-002590E2F5CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C053E061-6C7E-E511-B0D8-0CC47A13CB62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2F2CC0B-6C7E-E511-BBE0-0025900EAB5E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2FFEB0C-6C7E-E511-B8FF-0025902D021A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C638CEE8-6B7E-E511-935C-0025901D08EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C88CBA0F-6C7E-E511-BC8F-0026182FD7A3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC608963-6C7E-E511-95E9-0025902D944E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE97D60A-6C7E-E511-85C4-0025904B8ABC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CEF3844B-6C7E-E511-8F4C-0025907D244A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA364609-6C7E-E511-BC29-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DEF21A60-6C7E-E511-8759-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E26CF20A-6C7E-E511-A20D-0025904A9472.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8D32C0E-6C7E-E511-A1F6-002590E3A224.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC5D1213-6C7E-E511-890F-003048F5B2A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC896E0D-6C7E-E511-972C-002590E2F65E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE41001C-6C7E-E511-85A7-0CC47A13D416.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8476961-6C7E-E511-B4B3-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FEBDF049-6C7E-E511-AA5A-02163E010F7B.root' ] );


secFiles.extend( [
               ] )

