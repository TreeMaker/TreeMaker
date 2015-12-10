import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/08ABB1E4-2A9F-E511-9BB9-02163E013FA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/10080BE5-2A9F-E511-95A1-001EC94BA3CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/104285B3-2A9F-E511-87B8-02163E01778C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/129711D0-2A9F-E511-A330-782BCB20FDEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/168B4ACC-2A9F-E511-A3C8-B083FED42C03.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/1E23B9BD-2A9F-E511-AB59-B083FED045ED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/2E0EEAEB-2A9F-E511-9D2B-C81F66B78FF5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/32953818-2F9F-E511-9B22-E41D2D08DEE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/34E265D2-2A9F-E511-937F-02163E014DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/46ACB58F-2D9F-E511-B8F3-842B2B42B584.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/486C9DED-2A9F-E511-A4B8-D4AE526DF64C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/524AA4AE-2A9F-E511-BBD4-B083FED42FE4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6C4EE4C3-2A9F-E511-8B7B-A4BADB1E6796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6C7EA702-2B9F-E511-93D0-D4AE526DF562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6E7E0ED6-2A9F-E511-8877-02163E012FDA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/74AE38DA-2A9F-E511-A308-D4AE527F2883.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/74CAF166-2D9F-E511-91B3-0019B9CB0300.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/7830B3AC-2A9F-E511-BFAE-90B11C0BD676.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/8CB7CDBA-2A9F-E511-9833-001EC94BFFEB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/8CF658E1-2A9F-E511-8525-549F3525AE18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/90D341B4-2E9F-E511-849F-002590AC4C49.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/921DB3CD-2A9F-E511-93E1-842B2B180A9F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/944B9CBE-2A9F-E511-9427-782BCB1F5E6B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/9637E6EF-2A9F-E511-9EF6-842B2B42BC3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/A2329021-2F9F-E511-8450-E41D2D08DD10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/A435D607-2B9F-E511-B219-782BCB53B63D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/A4FCCFCE-2A9F-E511-B41D-02163E013BCB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/A60BBDF4-759E-E511-B825-782BCB50ACF1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/ACE670F0-2A9F-E511-9F4B-90B11C0BD467.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/BC6BCDE5-2A9F-E511-B3C8-782BCB20EDD2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/BEFB24F7-2A9F-E511-A7F7-D4AE526DF3BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/C0CF56B9-2E9F-E511-934F-047D7BD6DD64.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/CA274026-2B9F-E511-B7C7-C81F66B73923.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/CC2ACAC9-2A9F-E511-83BB-B083FED40671.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D0634CE3-2E9F-E511-94F8-002590DB9358.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D20D02BD-2A9F-E511-B408-02163E013168.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D40165CD-2A9F-E511-B358-02163E013E59.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D8D9F9B2-2E9F-E511-82C9-047D7BD6DF00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/DA9F057B-849E-E511-B6AA-0019B9CB01E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/E8635D09-2B9F-E511-83F2-001EC94BA146.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/E8FC0EF1-2A9F-E511-ADC3-B083FED177B1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/F4516FB8-2E9F-E511-BC71-0025907FD40C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/FC25231D-2B9F-E511-B63E-02163E016831.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/FCE78AE4-2A9F-E511-89AF-842B2B181727.root' ] );


secFiles.extend( [
               ] )

