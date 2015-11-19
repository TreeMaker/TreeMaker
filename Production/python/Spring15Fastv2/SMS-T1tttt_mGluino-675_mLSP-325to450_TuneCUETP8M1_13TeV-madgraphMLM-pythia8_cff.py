import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0A637701-7B8A-E511-8930-02163E00C757.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0C54A6AC-7B8A-E511-BD45-02163E013FB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0C8A3384-9A8A-E511-AA2A-02163E014C23.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1865F580-7C8A-E511-A5EA-02163E012E76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2049ACF3-8E8A-E511-9EE8-02163E016B60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/22099796-998A-E511-997D-003048FEBA12.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/32ABB5B9-828A-E511-9F44-00266CF9BBE4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4C7F91B8-828A-E511-9D2E-7845C4FC3B18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/50B0AD78-8F8A-E511-A6ED-02163E00E5FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/729AFDCF-778A-E511-A52A-02163E00BAD6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/74444803-8F8A-E511-90B5-02163E015F3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7AD5B3C3-998A-E511-9206-02163E00E81F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7E57FE69-A08A-E511-8EBB-008CFA002490.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8AF2878D-AB8A-E511-9316-02163E014D3E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8E0FE267-AB8A-E511-ACC6-02163E013E8D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8ED9D064-A58A-E511-B905-02163E00E838.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92343B8D-778A-E511-B7FE-02163E00E9F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9AA5B9E4-828A-E511-A5DE-02163E014BE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9AFEEC1D-9A8A-E511-94B9-02163E00F46A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AA1DB91D-9A8A-E511-A22D-02163E01468A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/ACA452D9-8E8A-E511-953C-02163E0117C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/BC71745C-8F8A-E511-B612-02163E013108.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C83B386B-A08A-E511-9B80-02163E014FD6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/CCD601AF-998A-E511-8580-02163E00B34D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D45143CA-828A-E511-B40F-02163E016685.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D4CE8477-8F8A-E511-8AEB-02163E00F44B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E2DBB260-998A-E511-9E12-00266CFAEA68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F47DDD5F-9D8A-E511-B9CF-02163E010D11.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F6A1D96C-A08A-E511-9C2B-02163E016ABE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FA98F0D2-828A-E511-99B5-02163E014FD9.root' ] );


secFiles.extend( [
               ] )

