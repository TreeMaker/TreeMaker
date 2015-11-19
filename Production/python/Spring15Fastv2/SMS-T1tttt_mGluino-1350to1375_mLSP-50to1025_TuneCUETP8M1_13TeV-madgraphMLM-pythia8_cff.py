import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/000F9FC1-297F-E511-B182-02163E0114A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/00B94E9B-287F-E511-82FB-02163E00B25E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/087323AF-287F-E511-87CB-02163E016B45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1610D07A-287F-E511-BE7E-001E67579498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1C380888-287F-E511-AC09-02163E011529.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/347B2E9D-287F-E511-82DD-02163E011463.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/38AE85B4-287F-E511-B349-02163E0151D5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/42E72BDA-287F-E511-8436-02163E00EA89.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/44B9C099-287F-E511-B126-02163E016760.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4A25E783-287F-E511-9D15-02163E0114B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4CB9E878-287F-E511-864E-02163E013265.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4CD99191-287F-E511-9147-02163E015C6B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4E86CD6A-287F-E511-A9B8-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4EBDB19A-287F-E511-9E38-02163E00CDA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/506F4CD8-287F-E511-8081-02163E0150F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/52082E9D-287F-E511-A763-02163E011463.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5A9C9391-287F-E511-95CB-001E67579ED8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6AAE9F63-287F-E511-BCA7-002618943915.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/70D4D9C0-287F-E511-BC1E-02163E00B2AB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7473F368-287F-E511-B759-0025905964BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/74CF6D83-287F-E511-BFE4-02163E016B45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7860BFC4-287F-E511-90D0-02163E00E5EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/78697362-287F-E511-B2DF-00259021A4B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/78C9CBD6-287F-E511-9B31-02163E0114BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/804BEAA1-287F-E511-AC6F-02163E00E5EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/82EDF1AF-287F-E511-8B65-02163E011463.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/843C84A9-287F-E511-B52A-02163E016721.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8E40417A-287F-E511-9C91-02163E01141A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8E5D369A-287F-E511-8340-02163E00C35F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/96ED28B4-297F-E511-87C5-02163E011452.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9806B3BA-287F-E511-953B-02163E0153C5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A4623FD5-287F-E511-932E-02163E016B98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AEFA568A-287F-E511-BCE8-02163E00CE07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B2DA5287-287F-E511-85CC-02163E013A86.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BE10239D-287F-E511-891E-02163E00EA03.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CA946278-287F-E511-8A2B-02163E013A15.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CCBD478B-287F-E511-9BA6-02163E016A09.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D29CC7DF-287F-E511-97A9-02163E014D0D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D456B482-287F-E511-92ED-02163E012DCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DE3AD6D6-287F-E511-9319-02163E0114BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E0B9C86D-287F-E511-8AE7-02163E014C45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E49709BE-287F-E511-A883-02163E016C15.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E664626E-287F-E511-9342-02163E012E4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EC278C94-287F-E511-ADF2-02163E0152A5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EC304BB3-287F-E511-83FE-02163E016788.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F8464074-287F-E511-B84C-02163E013AE6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FA8B9A73-287F-E511-B89D-02163E00EB1D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FEF83490-287F-E511-9FA4-02163E00E5B4.root' ] );


secFiles.extend( [
               ] )

