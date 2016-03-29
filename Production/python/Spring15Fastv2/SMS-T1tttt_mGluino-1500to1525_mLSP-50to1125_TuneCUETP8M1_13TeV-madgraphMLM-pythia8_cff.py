import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0A5EEA32-037C-E511-9870-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0C553A9A-027C-E511-A36F-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0CCFB32D-037C-E511-A59A-002618943974.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0EE8313B-F87B-E511-8085-842B2B760921.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/16CF4CA9-027C-E511-9F6D-0025905B8586.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/18AA6DC9-0C7C-E511-B90F-002618943896.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/28B5142F-037C-E511-BCA3-002618943940.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3A4D7A39-F87B-E511-9B15-B499BAAF9920.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3C38575D-827C-E511-A1F4-02163E013AED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3E0365CB-0C7C-E511-9D16-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/42C6AE88-027C-E511-BD11-00261894393A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/42FE6D19-F87B-E511-8C5B-0002C92DB46C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/48BF6DCA-0C7C-E511-818C-0025905A6126.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4A086215-D37B-E511-BCC8-0CC47A00941C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4C97D48C-027C-E511-91BB-0025905B855E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/50ED45CB-0C7C-E511-8812-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5278BDF8-027C-E511-92EA-0025905964C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/566CFEC9-0C7C-E511-AB34-0025905A612E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/56957123-867B-E511-B318-0025905938AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5C27FF3A-F87B-E511-9C4D-842B2B7669E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5EF20430-037C-E511-844F-0025905964A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6279DE5B-817C-E511-A7C8-02163E00F521.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/62DD3539-F87B-E511-8FD6-842B2B71F663.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6854AAC9-0C7C-E511-B9C3-0025905A6136.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/70BC5075-0E7C-E511-8495-0025905A60BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7EC44ACB-0C7C-E511-9109-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8462EFA5-027C-E511-B0F3-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/84944FA5-027C-E511-BBD0-00261894393A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/863CF7CB-0C7C-E511-8554-00259059649C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8ECA6DC9-0C7C-E511-B75E-002618943896.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/987CA831-037C-E511-AB09-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9ECE4EB1-027C-E511-B890-0025905A606A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A05A6E86-027C-E511-B7FC-003048FFD756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A8167CAD-817C-E511-869A-001E675793A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A8809030-037C-E511-AA49-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A8A08624-867B-E511-B842-0025905A60F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/AC464FBC-027C-E511-B955-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B2433D85-027C-E511-BFA6-0025905B85AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B6009133-037C-E511-B5FF-003048FFD7A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C0A63C32-037C-E511-9528-0025905A6126.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C0CFD8C2-027C-E511-9C5C-0025905A612E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D0893B76-817C-E511-A28A-02163E012F98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E00CCA97-027C-E511-9B08-002618943886.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E029F62F-037C-E511-8AC3-00259059649C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E06A20CA-0C7C-E511-A983-0025905A48C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E07FFECC-0C7C-E511-AB04-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E42AE6C7-0C7C-E511-99C9-002618943875.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F2F5AE74-817C-E511-A40B-02163E0166A9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F851F8B2-F77B-E511-86BF-1CC1DE18D026.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FCAEAA0C-037C-E511-8D31-003048FFD732.root' ] );


secFiles.extend( [
               ] )

