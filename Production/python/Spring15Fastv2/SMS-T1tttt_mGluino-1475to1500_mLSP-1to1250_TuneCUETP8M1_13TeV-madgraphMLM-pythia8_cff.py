import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/06218945-637E-E511-9729-001E67A4061D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A256F6B-637E-E511-AB0B-0026181D28F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A932556-637E-E511-9E4E-002590DB923E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/12F20A4B-637E-E511-AA66-047D7BD6DE16.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26A2E943-637E-E511-A09D-002590DB9172.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/28170619-647E-E511-977E-E41D2D08E0E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2C750C48-637E-E511-8FE3-E41D2D08DE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A993844-637E-E511-BA41-00259074AE7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AE85640-637E-E511-8A9D-F45214939740.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4698C429-647E-E511-9A91-E41D2D08DE40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/46A89A44-637E-E511-9346-047D7BD6DE30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48ED7644-637E-E511-90D0-E41D2D08E080.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E9A0E4F-637E-E511-A649-047D7B881D06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50884D43-637E-E511-B837-002590DB9286.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5630614A-637E-E511-A23F-002590DB9196.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E046948-637E-E511-9B85-E41D2D08DD90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E05BE51-637E-E511-A723-0CC47A4DEE36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/60447E41-637E-E511-822A-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/624ED240-637E-E511-BD96-E41D2D08DDD0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66A0C141-637E-E511-B3C3-002590A2CDA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/701B3822-647E-E511-BE2C-002590DB91D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7071A541-637E-E511-A5FD-002590747DEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/70B7B248-637E-E511-B166-002590DB91E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/72819959-637E-E511-B73B-00266CF32F14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80484844-637E-E511-9E6F-001E67A3FDF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/84774E19-647E-E511-A0CF-E41D2D08DDC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E4B8E42-637E-E511-AE47-002590747E0E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/927F944A-637E-E511-8CF6-047D7B881D98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9AC5AF4A-637E-E511-9BA7-047D7B881D06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A619FA1C-647E-E511-8F74-002590DB92BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6452166-637E-E511-AEB5-00266CFFA5C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA1C6E3E-637E-E511-A8BA-002590D0B00E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B02F7E4C-637E-E511-9C81-002590DB92BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B4D51E43-637E-E511-A32A-20CF305616D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B4F09F19-647E-E511-AE60-002590AC4FC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8961442-637E-E511-92E0-E41D2D08DFA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2933019-647E-E511-902A-E41D2D08DDC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6468F4A-637E-E511-AB02-002590DB9196.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA4C9C19-647E-E511-B7DD-047D7BD6DE16.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CAB69755-637E-E511-869E-002590A8DC50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D0205A22-647E-E511-9AB4-E41D2D08DF60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC17C442-637E-E511-9D76-001E67A3EF48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E250E744-637E-E511-A5C2-001E67A39C17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6DD4C44-637E-E511-AAAA-001E67A404B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8E55063-637E-E511-8104-002590DB91FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA313752-637E-E511-B635-0CC47A4DEE36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC58133E-637E-E511-B7ED-002590D0B014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECF7A449-637E-E511-8B5A-047D7BD6DE14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE589C53-637E-E511-8948-0026181D2917.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F444135E-637E-E511-A745-002590DB91F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F45F6518-647E-E511-9E1E-E41D2D08E100.root' ] );


secFiles.extend( [
               ] )

