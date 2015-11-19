import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0804E3C9-1982-E511-BA8C-38EAA7A6DCE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0AB48571-5581-E511-A10B-02163E0152CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1826FE23-6E81-E511-A44E-02163E00EA36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20E7F156-7981-E511-A66A-02163E013DD4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/22F233B6-6B81-E511-9465-001E675799D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2C6B3951-5281-E511-88A8-02163E0169F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/382E59A1-5E81-E511-BADA-02163E016703.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AB78159-5281-E511-91B3-02163E00E664.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/449FC439-7981-E511-A5EC-02163E0117DB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C3DE08B-CA80-E511-91EA-02163E013E44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E5A59CD-7281-E511-B09A-02163E013EF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50702E2D-6781-E511-8686-02163E0138D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/54C66843-5881-E511-B547-02163E013F6F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5CA5292C-A580-E511-970D-02163E01156F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/628FE00B-6E81-E511-8F25-02163E013EB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/660149DC-A680-E511-A36F-02163E0139FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66BE55C8-5E81-E511-A06B-02163E016A93.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CD8366A-5781-E511-B2BB-02163E016B98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/707766AB-4D81-E511-A3F6-02163E00E675.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7819042E-7981-E511-A2CE-02163E0115EB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7CE5C55A-7981-E511-BC58-0002C94D5522.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80559999-7081-E511-AE06-02163E016829.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8084A337-4981-E511-8934-00505602077B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/866264B2-6A81-E511-B6F1-02163E015CB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/867F3FB5-5681-E511-982A-02163E00E5CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CDB09DD-4D81-E511-8AC3-02163E00AC9D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CFCC951-6B81-E511-8579-02163E00F40C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A46423AC-5581-E511-AA0C-02163E00C60C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA3A6601-6881-E511-BA1A-02163E013F79.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BABE1567-9D80-E511-8D1C-02163E00B82F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC846323-7081-E511-B1F6-02163E0115F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C09E281B-6881-E511-9045-02163E00EB14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2657B24-6B81-E511-8D22-02163E015DBF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C68BE797-6681-E511-B3E6-02163E011742.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC48C458-7981-E511-B385-0002C94CD0BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CCA1D456-5881-E511-8BFB-02163E010CC3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D054101E-6C81-E511-8E8F-02163E016928.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D0585B3C-7281-E511-8D53-02163E00B2CD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D627D681-A680-E511-9090-02163E016746.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E098A49F-6B81-E511-938D-02163E01319E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4AF2573-5681-E511-BED1-02163E014D33.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E66207C2-5781-E511-BF37-02163E0153A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6D6BE00-4D81-E511-A5FA-02163E012E76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE05C0A5-7981-E511-920A-003048FEB8FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F023280E-6B81-E511-93EF-02163E014D57.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FC70417D-7081-E511-8AE4-02163E00B2AB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE8BA9A3-7981-E511-9933-02163E01319E.root' ] );


secFiles.extend( [
               ] )

