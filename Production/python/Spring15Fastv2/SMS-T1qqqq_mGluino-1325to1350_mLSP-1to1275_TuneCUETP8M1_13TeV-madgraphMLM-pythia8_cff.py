import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0E17FBF2-5681-E511-8FD8-02163E00B54A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1627368C-1982-E511-B22A-001E673C7EF4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/168F343E-6181-E511-8587-003048F0E858.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/18BE3809-3E81-E511-8423-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1C14BF92-7E81-E511-9FA5-00248C0BE014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20615DBC-1982-E511-B493-001E673D21B9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2070A6FD-3F81-E511-8686-02163E00E6BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/22E958C3-1982-E511-9FD8-001E673C84B9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/248AC0D6-1982-E511-A105-38EAA7A309FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26DA6B4D-7E81-E511-9269-0025905A6080.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EC7F839-4281-E511-9A23-02163E013D3B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3022E388-3D81-E511-8C57-002618943974.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/323A2942-7E81-E511-86A2-0025905A608E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A44DA56-7E81-E511-9815-0025905A60F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3C55489A-7D81-E511-BCF4-0025905A7786.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4060C2B7-3B81-E511-A1B1-002618943974.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/468A414D-7E81-E511-AA14-0025905A6080.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C207E79-7E81-E511-B80B-002590593872.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5C946202-7E81-E511-AAB2-0025905A60E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5CBD015D-7E81-E511-8707-0025905B8598.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6230BC10-7E81-E511-A070-0025905B8598.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/627A61D5-1982-E511-A9DC-001E6739AB19.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62A25320-7E81-E511-9885-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/643397BC-3D81-E511-899F-02163E00ADAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/68A8127D-7E81-E511-AF4C-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/68C2FA2F-7E81-E511-865E-0025905A606A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/68DE1729-7E81-E511-8321-0025905A609E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C302B8C-7E81-E511-96A3-0025905A60E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/90ADFF2B-7E81-E511-90DF-0025905A6088.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/94D2D093-3F81-E511-B510-02163E010E52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A257C76B-7E81-E511-B78A-0026189438B9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B0F31A4E-5881-E511-8BFA-02163E00B5D7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B6D13E57-7E81-E511-96A2-0025905A60F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8536F37-5881-E511-BC58-02163E015E68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA7E95D7-4181-E511-95E5-001E674FB3CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C037AC28-3E81-E511-96B7-D067E5F91F44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2F6A186-7E81-E511-A367-0025905964C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C447C57E-7E81-E511-B59C-0025905964BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C8369B22-5D81-E511-90E7-02163E013EB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA715BA4-1982-E511-BDBE-A0000100FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CAD71F7A-7E81-E511-B00F-0025905A60CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC404387-7E81-E511-9DF7-0025905938AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4C0A885-7E81-E511-9637-0025905A60F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE92C24D-5781-E511-ABC0-02163E016B72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0D5567F-7E81-E511-A783-0025905A60C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E83CF258-3B81-E511-AFD2-D067E5F91F71.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8C5129D-6181-E511-B310-02163E013E57.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECBD6F4F-7E81-E511-81D8-003048D15E36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECE005BB-3B81-E511-AB6F-0025905A60AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F01C8D92-3D81-E511-99D8-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA48F539-6181-E511-8004-D067E5F91CCE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FC22D281-7E81-E511-8F2D-0025905B8562.root' ] );


secFiles.extend( [
               ] )

