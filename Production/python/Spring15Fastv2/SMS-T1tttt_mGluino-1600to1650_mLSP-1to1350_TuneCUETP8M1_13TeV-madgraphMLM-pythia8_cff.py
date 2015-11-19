import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0405A851-1E7F-E511-A260-02163E011452.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/04E7620B-1D7F-E511-8F73-02163E0114B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2021CCBE-E17E-E511-B6E3-02163E014C45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/24A4F209-1B7F-E511-9F60-0002C92DB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/26732184-C47E-E511-87C5-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/34FFD885-1B7F-E511-A1F7-02163E016631.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/368C3040-1B7F-E511-97FB-02163E0117D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/36E16D08-1B7F-E511-A50A-02163E013D67.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3CF7AD51-1B7F-E511-AA8D-02163E01147F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/44E7E800-1B7F-E511-9F95-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/469A912A-1B7F-E511-A65D-02163E013BE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5018D33D-1B7F-E511-ADBB-02163E01666C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/52222300-1B7F-E511-99C1-D4AE52651CE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/58546409-1B7F-E511-9F0B-02163E00F539.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/68441512-1B7F-E511-A11E-02163E013CF9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6C7F834A-DB7E-E511-A602-02163E00C862.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6E731A28-1B7F-E511-AD0F-02163E01677C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6E99AB25-1B7F-E511-9BBE-02163E0150ED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/72CE4B29-1B7F-E511-BDDF-02163E00EA4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/74B0F9FB-1A7F-E511-B127-842B2B1814F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/76B41138-1B7F-E511-89A0-02163E016919.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/78456F1F-1B7F-E511-8732-02163E00B884.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7A1ECD13-1B7F-E511-AC4B-02163E0131E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8050FC01-1B7F-E511-BF77-D4AE527EE0FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8875D104-1B7F-E511-BF80-02163E013E07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/88BEBC37-D27E-E511-A511-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8C95932D-1B7F-E511-B89B-02163E00EA4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9ABB0BFF-1A7F-E511-A4B6-D4AE52651C5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9AF6D918-1B7F-E511-B237-02163E016B84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9C360A29-1B7F-E511-B498-02163E012699.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A864C669-1B7F-E511-AE2A-02163E016B8E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B04A9967-1B7F-E511-BE22-02163E016903.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B49E3708-1B7F-E511-A8D8-D4AE526DF2E3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B88089FD-1A7F-E511-8D22-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BA39A20C-1F7F-E511-BE47-02163E011419.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BA9B9F10-1B7F-E511-BA18-02163E014C40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C208580B-1B7F-E511-89CA-02163E016B62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C4FDE701-1B7F-E511-99C2-02163E010E17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CCC818F9-1A7F-E511-BEE9-002590D0AF82.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D81CA66B-FC7E-E511-A52E-02163E01684E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D8599912-1B7F-E511-AE44-02163E00C0EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D8CB5719-1B7F-E511-8DF0-02163E015CB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DA951BFC-1B7F-E511-A922-02163E0139EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DED7F293-1B7F-E511-9D6E-02163E016719.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E27C1609-1B7F-E511-A294-02163E016965.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E2EC1D0A-1B7F-E511-9475-02163E0131DF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EAAE9608-1B7F-E511-BD2D-02163E0115FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EEE7EA26-1B7F-E511-B602-02163E00BFFF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FC1C3B02-1B7F-E511-A113-782BCB678096.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE3B5332-1B7F-E511-B919-02163E01503B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE7F8A11-1B7F-E511-9400-02163E013D56.root' ] );


secFiles.extend( [
               ] )

