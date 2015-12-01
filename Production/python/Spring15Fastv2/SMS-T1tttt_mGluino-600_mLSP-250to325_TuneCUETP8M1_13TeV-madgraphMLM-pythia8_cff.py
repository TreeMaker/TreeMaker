import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/04C38A8A-1392-E511-8D7E-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0884EE74-1492-E511-80D5-0CC47A4D769A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/26E4BD82-1392-E511-9B55-0CC47A78A32E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2A0E0977-1492-E511-B55E-0026189438FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2A422C7A-1492-E511-BBCE-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2E50667E-1492-E511-B6AD-0025905A6080.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/30C9C120-1492-E511-9DA1-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/36750F8B-1392-E511-A53B-0025905A60A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3C0A717E-1492-E511-9E5A-00259059642E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3C92288B-1392-E511-93F5-0025905A60A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4227118A-1392-E511-BCE0-0CC47A78A3E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/44BD798E-1392-E511-AC4A-0025905A6132.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/527D3A87-1392-E511-B653-002618943957.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/54E5C077-1492-E511-B649-0CC47A4D765A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/643D8786-1392-E511-AEFD-0026189438ED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6464D777-1492-E511-8D06-0CC47A4D7686.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/68FBF982-1492-E511-99CC-0025905A4964.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/72133A90-1392-E511-81EE-0CC47A78A4A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7444448A-1392-E511-BFB6-0025905A48D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/78D0D378-1492-E511-8369-003048FFD720.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7A099087-1392-E511-BAF1-0CC47A4D768E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7A114D76-1492-E511-9A2E-0CC47A78A32E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/84CD587C-1492-E511-8201-0025905964BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/8E9CCA82-1392-E511-B21F-0CC47A78A32E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/904C528A-1392-E511-AA90-0025905B858C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/90A38A87-1392-E511-AE48-0CC47A4D76B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/94726566-1392-E511-95C0-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/964F3683-1492-E511-A1CF-002590593920.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A8C50E88-1392-E511-AD96-0CC47A78A41C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AA50E48E-1392-E511-82E8-0025905964C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AC1404E0-1392-E511-BFA2-0025905A48D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AE64C2ED-1392-E511-A84F-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AE87778E-1392-E511-A67C-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B09B043C-1392-E511-8C0D-0CC47A4D761A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B24FE7B7-1292-E511-926C-0CC47A78A42E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BC79DA8A-1392-E511-A38E-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BE7AE977-1492-E511-9F31-0CC47A4D766C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D2017287-1392-E511-972C-0CC47A78A2F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/DA672A0C-1392-E511-A6C5-0CC47A78A4A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/EA870578-1492-E511-AA19-0CC47A78A4A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/EC3480DA-1492-E511-9104-0CC47A78A4A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F026A688-1392-E511-9B65-0CC47A4D768E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F2487487-1392-E511-8339-0CC47A78A41C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F6BB7889-1392-E511-9FAB-0025905A60CE.root' ] );


secFiles.extend( [
               ] )

