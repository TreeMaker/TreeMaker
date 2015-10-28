import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/00EE32EF-787B-E511-95E3-00259073E2F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/021495B7-7B7B-E511-8D35-0025905A60BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/04D69BEF-787B-E511-83A1-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/060F63B3-7B7B-E511-B790-002618943856.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/084FD1F1-787B-E511-8516-002590747E14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0C47CD4D-7A7B-E511-AECC-0025905A60F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CADA6F1-787B-E511-BAE0-002590747E14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CEF604E-7A7B-E511-9CDD-003048FFD7BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0E0BD511-7A7B-E511-A38B-20CF305B050D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/18930E5F-7A7B-E511-BF19-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A37FE0C-7D7B-E511-A39A-0026189438E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2204F854-7A7B-E511-B558-0025905A607A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/264F37F0-787B-E511-BE3B-00259073E4D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26B68EB1-7B7B-E511-834D-002618943923.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/465A634C-7A7B-E511-9A1B-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48D31BB8-7B7B-E511-8B42-0025905A60E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A34464A-7A7B-E511-9466-002618943926.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C6D164E-7A7B-E511-8D67-003048FFD754.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E9DECB2-7B7B-E511-AEDA-0026189438B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/54A1F7F0-787B-E511-96A2-00259073E3D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/604E80F0-787B-E511-A17F-20CF305B056C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6643B8EF-787B-E511-9626-00259073E53E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/668062EF-787B-E511-A8E6-00259073E3AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A057E4E-7A7B-E511-810F-003048FFCBA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/789B72C5-7E7B-E511-8D71-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/78D45850-7A7B-E511-AA88-0025905964A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E5B104D-7A7B-E511-B1D3-003048FFCC0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82BA6AF0-787B-E511-B492-00259073E4D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86010E4C-7A7B-E511-9216-0025905B85D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8C912FB6-7B7B-E511-BF72-003048FFCB84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E9583BB-7B7B-E511-8745-0025905964C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9007A2EF-787B-E511-92D9-20CF305B050D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/920D2AF1-787B-E511-A36F-00259073E3D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92EE72EF-787B-E511-B908-00259073E51C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/968DD646-7A7B-E511-8CA9-00261894390B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AC35A6F1-787B-E511-8575-002590747E14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B65A4D51-7A7B-E511-A601-003048FF86CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C614054D-7A7B-E511-847F-0025905A6076.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CCCCF548-7A7B-E511-B298-0026189438E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D42DE4B8-7B7B-E511-9D24-0025905A60AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4F2CCEF-787B-E511-9113-00259073E4F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D62D6A4B-7A7B-E511-B1D8-003048FFD720.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC187D06-7A7B-E511-B9AE-20CF3056170A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE7376B8-7B7B-E511-A0C0-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E01A20B8-7E7B-E511-A630-0025905B85B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E02FCF4D-7A7B-E511-B153-0025905A48D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4F2844E-7A7B-E511-8B8B-0025905938A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EAD225F1-787B-E511-8F67-002590747E40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC8FB54B-7A7B-E511-A337-0025905B860C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F253CC4C-7A7B-E511-971C-003048FFD7C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FCF4DE4D-7A7B-E511-8991-0025905B859E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE338FBA-7B7B-E511-AD11-0025905938A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE7506F0-787B-E511-9729-00259073E510.root' ] );


secFiles.extend( [
               ] )

