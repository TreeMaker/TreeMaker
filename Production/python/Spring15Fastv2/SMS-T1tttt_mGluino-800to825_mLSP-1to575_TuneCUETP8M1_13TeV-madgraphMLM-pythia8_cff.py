import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/08FECADE-BB7F-E511-AEEB-002590DE6C48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/129FD81B-A37F-E511-B521-0CC47A4D9A3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1AE580AD-A27F-E511-B6B3-842B2B76653D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1C05C5AB-BB7F-E511-8961-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E2E71E1-B37F-E511-AC83-FA163EA65750.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E9449B8-A87F-E511-AA58-20CF305B052B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/22AB22F6-997F-E511-B2F7-02163E011487.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/244AA460-9E7F-E511-9737-001EC9B215FB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/247F8781-B07F-E511-8E47-FA163E7E2FF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2C26F1B7-A27F-E511-87CD-00505602078E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3CE9330B-BC7F-E511-99AA-02163E016B76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3E72739C-AB7F-E511-AFD4-0025901D40D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/46ACC24F-A87F-E511-8741-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4A2D3304-9F7F-E511-8105-0CC47A4D9A3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4EA3266A-B27F-E511-9B20-FA163E19FFD9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5804CAE1-B37F-E511-AD54-FA163E7E9947.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/68E27DC6-A57F-E511-8E9C-0CC47A4DEEF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6AD211D6-BA7F-E511-ABD7-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/705FD901-997F-E511-8C32-02163E0115EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/78DE2425-997F-E511-A0B4-02163E014F8B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8079630E-BA7F-E511-92A1-02163E016B62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8C7F6D9B-A27F-E511-AAB4-0CC47A4DEEFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/92AB4B2A-B37F-E511-BD8B-20CF30561711.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A89B3FAB-A67F-E511-B169-02163E00C81E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AA1FE9F7-BB7F-E511-A38B-02163E016B94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AC249AD7-BA7F-E511-95B8-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B25437FF-B57F-E511-8AA7-FA163E49D792.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BC096E82-B07F-E511-B17E-FA163E7E2FF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BE2B76F5-A77F-E511-9674-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C2D2B494-A67F-E511-9C22-02163E00F386.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C4355146-B27F-E511-AC22-FA163EEF8E08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CA32A882-B27F-E511-AFE4-00505602077C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D630E52B-B37F-E511-8307-20CF305B059C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D8AF055D-9F7F-E511-9A7A-0CC47A4D9A3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DEAA0868-9A7F-E511-80F1-02163E016922.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E6B7B89B-B57F-E511-92C1-02163E014CFE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E8E009CB-A57F-E511-88CD-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EEE7E1BA-BC7F-E511-93AE-FA163E4635DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F00F180B-BC7F-E511-91A5-02163E016B76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F088C7F1-A27F-E511-8DD9-0CC47A4D9A3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F2CB1731-BA7F-E511-BF00-0CC47A04CFFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F2D464FC-BB7F-E511-9BE9-02163E012E4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FC254995-BB7F-E511-B236-02163E014FC5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE69FA0A-9F7F-E511-BFAF-842B2B75FFFD.root' ] );


secFiles.extend( [
               ] )

