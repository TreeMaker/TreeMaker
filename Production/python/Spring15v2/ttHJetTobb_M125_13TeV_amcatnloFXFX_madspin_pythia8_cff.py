import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0680AD87-C26D-E511-8691-848F69FD24D2.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0EE5207F-C26D-E511-8935-3417EBE64C0C.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/12B59879-C26D-E511-A2B0-3417EBE2F44B.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/12DF532A-C36D-E511-B728-7845C4FC364D.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/1EFE4E78-C26D-E511-A3C9-0025905B860E.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2464F393-C36D-E511-B888-7845C4FC35DB.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/38BF4C77-C26D-E511-B34F-0025905A60B0.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/4075957A-C26D-E511-B4DF-3417EBE643CC.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/5E540A77-C26D-E511-9D98-0025905A6122.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6492A820-C36D-E511-BB7E-848F69FD45A4.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/64E4BD73-C26D-E511-8B5A-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/68BE1386-C26D-E511-9440-7845C4FC3635.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/68CEBD76-C26D-E511-83D7-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6CAFCB79-C26D-E511-A796-3417EBE3379E.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/7678748E-C36D-E511-9F45-7845C4FC35EA.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/80ADA781-C26D-E511-B457-3417EBE643F0.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/827AD691-C36D-E511-9E41-848F69FD28AD.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/885E7578-C26D-E511-ADA9-0025905B8576.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/8CB18674-C26D-E511-A637-0025905B8590.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/8EEB997A-C26D-E511-B6C3-3417EBE2F0DF.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/98676A74-C26D-E511-A1EA-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/98F0488E-C36D-E511-AB34-7845C4FC371F.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A0110B77-C26D-E511-BFAF-0025905A6122.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A6030D78-C26D-E511-A00A-3417EBE64BF7.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/AEC0E07A-C26D-E511-A1AE-3417EBE2EC95.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B026967B-C26D-E511-82BD-3417EBE2F0C7.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BA0F788D-C26D-E511-BFAF-7845C4FC36D7.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BC0B3F78-C26D-E511-81EB-0025905B860E.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C67A9F76-C26D-E511-ADDB-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/CA6EEB73-C26D-E511-9F1F-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/CE34F581-C26D-E511-96B6-3417EBE2F094.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/CE7EF082-C26D-E511-90C7-848F69FD2826.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D0388C80-C26D-E511-AAE8-3417EBE2EEC6.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D2BE6277-C26D-E511-85C6-0025905A60B0.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/DEAB967C-C26D-E511-A8B4-3417EBE64BA0.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/FA44BE81-C26D-E511-B6C7-7845C4FC3A67.root',
       '/store/mc/RunIISpring15MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/FCA0B473-C26D-E511-8B40-0025905B8582.root' ] );


secFiles.extend( [
               ] )

