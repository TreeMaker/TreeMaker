import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/0C08B155-C26D-E511-AD62-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/162DC430-C36D-E511-92CC-002590593878.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/184DEA57-C26D-E511-975A-0025905B85D0.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1C30D756-C26D-E511-922C-0025905A6126.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1E963559-C26D-E511-AB1D-0025905A6092.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3A5E3557-C26D-E511-8631-0025905A6068.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3A8C802D-C36D-E511-AF80-0025905B85AA.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4C41C757-C26D-E511-BF22-0025905A611E.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4E2D6F58-C26D-E511-AE58-0025905B858E.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/50AF7258-C26D-E511-AA84-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/56D3C558-C26D-E511-94C0-0025905B8590.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/587AE92B-C36D-E511-A429-0025905A612C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/58D6C157-C26D-E511-9231-0025905A610C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/5A1C8F56-C26D-E511-BB0D-0025905B85D6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/608D0C2A-C36D-E511-A18B-0025905A6090.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/662C7856-C26D-E511-8C8E-0025905B85D6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/72708058-C26D-E511-8913-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/76121FAF-C26D-E511-85E6-0025905A611C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8093D82D-C36D-E511-A09D-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/809B802D-C36D-E511-B464-0025905B85AA.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/88CF8A2D-C36D-E511-BE68-0025905A6134.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/92474929-C36D-E511-906F-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/929FBD2A-C36D-E511-9E2A-002618943836.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/94A27531-C36D-E511-B386-00259059649C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9841C72D-C36D-E511-8D40-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9C29C430-C36D-E511-A4AE-002590593878.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9ED57257-C26D-E511-8E12-0025905A608C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A4B46B60-C26D-E511-8558-0025905A48BB.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A4F87331-C36D-E511-AD59-00259059649C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AA6FCE2C-C36D-E511-B7A1-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AC1F7755-C26D-E511-ACD7-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AECBC157-C26D-E511-81E9-0025905B8606.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B209F428-C36D-E511-9488-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/BE27435B-C26D-E511-8CB5-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C00FDF29-C36D-E511-AB71-0025905A6090.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C243CE6E-C26D-E511-9E01-0025905A611C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C2969059-C26D-E511-9012-0025905A60B4.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C6629458-C26D-E511-A1D4-0025905B858E.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CC1EA558-C26D-E511-8198-0025905B858E.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CC796B2C-C36D-E511-B221-0025905A612C.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D60B0A2E-C36D-E511-A3E5-0026189438B1.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/EAC22F29-C36D-E511-82FF-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/EE47AC56-C26D-E511-B8B9-0025905B8592.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/EEA00658-C26D-E511-94F9-0025905A605E.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F022932D-C36D-E511-BFFC-0025905A6134.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F087932C-C36D-E511-8DCC-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F290BC2A-C36D-E511-AEC7-002618943836.root',
       '/store/mc/RunIISpring15MiniAODv2/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F4540658-C26D-E511-829C-0025905A605E.root' ] );


secFiles.extend( [
               ] )

