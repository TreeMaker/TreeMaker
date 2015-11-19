import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/00E27F60-8F80-E511-9954-02163E016C06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/06BC69D4-6080-E511-8C9E-002590E1E9B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/08AD8B99-5980-E511-B849-02163E010C60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/10946489-6A80-E511-A766-02163E00E621.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1ACF794B-7B80-E511-A0DB-02163E014822.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/22FDAFCA-7B80-E511-8F06-02163E010FA1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/241E4C4C-7280-E511-8D03-90B11C27E141.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2458D556-9080-E511-94B8-0CC47A0448BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/24A936AD-6980-E511-9E62-0CC47A13CDA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2A1F6677-6780-E511-A2BB-02163E01507A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2E0292A5-7B80-E511-9338-02163E00EA79.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/322AA1B3-6980-E511-8F80-002590E3A024.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4062E247-1983-E511-860D-02163E00EAFC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/42BD5E4A-7280-E511-9F62-0025901D094A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/44AE0B4A-4B80-E511-B656-02163E00EA4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5EB234EA-5E80-E511-A06D-02163E00B090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/622334E7-6080-E511-A33E-90B11C2CB7A9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6416ADAC-6980-E511-8BAC-D4AE5269DC07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/64A4C520-6380-E511-A8E6-02163E0147E3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/74918A7B-5F80-E511-9304-02163E010DF7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7A1C8FC4-7B80-E511-B3C6-02163E00CE7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8065FC5D-7B80-E511-B2D3-02163E0148C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8281A9A5-8180-E511-B018-02163E01666C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9469C89F-8280-E511-8974-002590E2DDC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/96B80D12-6B80-E511-BE52-02163E015E3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9C6F2864-5A80-E511-8BE1-02163E014F8B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A27128D3-6080-E511-8EBB-0CC47A0091C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A4BFCB7C-5F80-E511-A51D-02163E0130F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A6BF2AE8-6A80-E511-ADCE-02163E0167CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BA3397AE-6980-E511-90A3-001EC9B21425.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BC4297C8-7A80-E511-AFBA-001EC9AF1E66.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C688AD5F-7380-E511-B7D3-002590A83308.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C68FE693-9080-E511-A78A-0025904B1FB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CA562774-9080-E511-BDF5-02163E00B3F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CE7A487C-7B80-E511-B8E3-02163E0148F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D4B74004-9080-E511-9917-0CC47A0448BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D60F732E-6180-E511-8828-02163E010FC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE6E145A-9080-E511-97A3-0CC47A04CFFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F483AA72-7B80-E511-A5B3-02163E014853.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F8554C41-7B80-E511-9F48-02163E00CA3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FAB75ED6-6080-E511-8636-D4AE526A0A60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FAD7A879-7B80-E511-B8FD-02163E00B2CD.root' ] );


secFiles.extend( [
               ] )

