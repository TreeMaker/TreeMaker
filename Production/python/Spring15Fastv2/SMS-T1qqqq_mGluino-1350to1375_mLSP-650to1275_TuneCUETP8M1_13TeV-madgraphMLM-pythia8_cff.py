import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/069F2B79-EE8A-E511-AEE1-0025905964A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/26A96579-EE8A-E511-A69E-0025905964A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3415EE76-EE8A-E511-94D8-0CC47A4C8F08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3A76F1C8-DF8C-E511-8006-00304865C478.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/669F657A-EE8A-E511-9B0E-0CC47A4C8EC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/66B5907A-EE8A-E511-B698-0CC47A4D7666.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/68BAC37F-DF8C-E511-9588-002590E2F664.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6C4CB550-CD8C-E511-89A2-02163E00ACC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6EF13975-CD8C-E511-B3DC-02163E00B366.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8EE0699F-CD8C-E511-B406-02163E013241.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/98E82080-EE8A-E511-9D5D-0CC47A4D76B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A409E445-CD8C-E511-940A-0CC47A04488C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A4D38D7E-DF8C-E511-8C42-003048F5970A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/AC1FD57B-EE8A-E511-99F2-0025905B8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/B8EEB3BA-DF8C-E511-AC76-0CC47A13D09C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BA2A0D76-EE8A-E511-854A-002618943975.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/C8D26176-CD8C-E511-A1E6-0CC47A04CFFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/D852547A-EE8A-E511-92EC-0CC47A78A32E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E868CA81-DF8C-E511-AFE6-00304865C45A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F065F13F-CD8C-E511-8B05-02163E013F93.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/FC0D247B-EE8A-E511-A7B6-0025905A60E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/FCD794CF-DF8C-E511-B934-0CC47A6C0758.root' ] );


secFiles.extend( [
               ] )

