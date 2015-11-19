import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/02482F6C-097F-E511-8EE3-0CC47A13CCFC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/04E1631A-097F-E511-B385-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08869418-097F-E511-BB94-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/12F7A018-097F-E511-B4E9-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1451C015-097F-E511-BC76-00259073E3AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CFCB31E-097F-E511-B007-002590E2F9D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/22614A68-097F-E511-A91F-0025902CF9E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/24E55D1A-097F-E511-A4EA-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26F6861A-097F-E511-A653-0CC47A13D16E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CC2C266-097F-E511-B942-0CC47A13D16E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EE03D17-097F-E511-BFD6-0CC47A6C186E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/30C23815-097F-E511-9583-00259073E344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3C3A371A-097F-E511-9279-002590E3A0FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4051CD13-097F-E511-87F7-002590D0AF52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/486AA718-097F-E511-ABA1-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5432B31A-097F-E511-8988-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/583A431A-097F-E511-BB57-002590E2D9FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A170217-097F-E511-9C83-0CC47A6C17FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C877C16-097F-E511-9A8D-00259074AE7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E14681E-097F-E511-8869-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7210A018-097F-E511-B362-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7629C418-097F-E511-BF88-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/783FEA16-097F-E511-8852-0CC47A6C06C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/809BDA30-097F-E511-AD11-F8C288671E9F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86A1A518-097F-E511-8284-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E5DD015-097F-E511-92FC-00259073E344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9245A018-097F-E511-9FCB-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/94CA531A-097F-E511-B199-002590E3A212.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9801FA3D-097F-E511-BE28-003048976B1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9C391D6B-097F-E511-915F-002590E39F4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A494C767-097F-E511-8DEE-002590E3A0FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A66D1616-097F-E511-BF4C-00259073E344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A80E921F-097F-E511-A7D8-90B11C2AA16C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A8EFA016-097F-E511-BC6B-00259073E390.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA763116-097F-E511-A2E1-00259074AE7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE42D61E-097F-E511-95DF-0CC47A13D2A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC355418-097F-E511-AA9D-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BEF2CD16-097F-E511-A93A-0CC47A6C186E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C001E313-097F-E511-8DAA-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C456BE16-097F-E511-9DB3-00259073E390.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D0E28016-097F-E511-99C0-0CC47A6C0758.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D62D6C16-097F-E511-9059-00259074AE7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EC912718-097F-E511-A0E3-001E682F2054.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE09E313-097F-E511-93C4-20CF305B0572.root' ] );


secFiles.extend( [
               ] )

