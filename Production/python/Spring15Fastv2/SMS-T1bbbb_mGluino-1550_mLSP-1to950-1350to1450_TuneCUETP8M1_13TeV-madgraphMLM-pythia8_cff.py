import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/086201E6-7D7B-E511-BE76-002618943984.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/12C1AEE8-7D7B-E511-8822-00261894392F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1C537AF4-7D7B-E511-ACDA-002590E3A004.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/202C17E9-7D7B-E511-88DF-0025905938A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/22F8CAE9-7D7B-E511-B9F8-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/28FC2CE7-7D7B-E511-B284-002590E3A224.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3079C8DF-7D7B-E511-8CCF-0025904897C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4C3068EA-7D7B-E511-B550-0025905A6066.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/54E981E7-7D7B-E511-9E3B-00238BCE45A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/605C910A-7C7B-E511-BE11-0CC47A6C115A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/62DD6FE3-7D7B-E511-8314-0CC47A6C0682.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/66A67EDA-7D7B-E511-A313-00238BCE45E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6CA50269-7F7B-E511-9A4D-0CC47A6C0758.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6E83E5D9-7D7B-E511-9D13-0CC47A6C17FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8011A5D9-7D7B-E511-BC5D-0CC47A6C138A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8069BCE7-7D7B-E511-ABBA-00261894387A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/82FCD4E9-7D7B-E511-A76E-0025905A613C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8A851968-7F7B-E511-A720-0CC47A6C17FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8E2109E9-7D7B-E511-8A65-0CC47A6C1038.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/94BA15ED-7D7B-E511-8EB3-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/94D25EE6-7D7B-E511-AC75-0026189438E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A01B94ED-7D7B-E511-A413-00259059642E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A44F19EA-7D7B-E511-BC12-0025905A6110.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A46B39EA-7D7B-E511-9F50-0025905A608C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A89151DA-7D7B-E511-AAC2-0CC47A13CB18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AE4AD4E3-7D7B-E511-9F3A-0025901D08B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B4F2D8E0-7D7B-E511-B6A1-0CC47A13CB18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/BAA5F9E8-7D7B-E511-8FB8-00261894389F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C01695EA-7D7B-E511-8FA1-0025905A60BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C218D2E5-7D7B-E511-9020-0025907254B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DAB3A1EA-7D7B-E511-A46D-00261894389D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DE3DCFDE-7D7B-E511-82D8-00259023466C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F21744E0-7D7B-E511-A9EF-0025904AC2C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F6B271E1-7D7B-E511-8E4E-1C6A7A266B2F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FA8194E6-7D7B-E511-B602-90B11C282313.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FCB91C73-7F7B-E511-B54A-0025904A9472.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FE3821EF-7D7B-E511-80BF-90B11C28232B.root' ] );


secFiles.extend( [
               ] )

