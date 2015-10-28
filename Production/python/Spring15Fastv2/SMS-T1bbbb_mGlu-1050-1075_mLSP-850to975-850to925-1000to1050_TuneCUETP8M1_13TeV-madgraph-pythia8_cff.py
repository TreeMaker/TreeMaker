import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/065AE531-0C7C-E511-96D8-20CF3027A58B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0AC51DEF-977C-E511-8E30-00259054C796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1086C9E3-127C-E511-8B6B-00259021A14E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1C1D66B7-E17B-E511-A647-002590207E3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1C9321DE-ED7B-E511-BA79-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2037C9E5-F57B-E511-9519-20CF3027A568.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/26C753EB-977C-E511-BF20-008CFA1112CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/287483DA-887C-E511-BF49-02163E0118E3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2AD3E171-0F7C-E511-A3CC-20CF3027A58B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2CC22686-887C-E511-94C0-02163E01692C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2E5C98EC-057C-E511-A098-001E675825D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3081E985-F97B-E511-9671-008CFA1112A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/342C99BB-877C-E511-8988-02163E015241.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3857A479-F97B-E511-BDEF-008CFA1113F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4A9ACAED-187C-E511-85C7-901B0E5427BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5669A0CF-087C-E511-8726-20CF3027A58B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/648435C5-E17B-E511-A494-02163E010C60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/66112027-887C-E511-BE03-FA163EF4C95B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6CFFCECA-0F7C-E511-80A8-001E67504255.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/70F459CB-087C-E511-8ACC-001E675050F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/78A9F9E9-877C-E511-BF99-02163E015D9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/886DC6DE-977C-E511-A500-008CFA1112BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8CD14963-0A7C-E511-B8B1-901B0E5427A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92263194-877C-E511-9EE2-02163E015402.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9AE6FFB2-047C-E511-9D1A-001E675825D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9E542287-877C-E511-8C3A-02163E00EA9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9EC46C1C-0B7C-E511-A82B-901B0E542962.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A47173B4-137C-E511-991E-002590207B90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A8D78B7C-0A7C-E511-ADEB-20CF3027A58B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AA31F45F-0D7C-E511-89C9-901B0E542962.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AEF68896-877C-E511-904F-02163E0149EB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B0F134BC-D17C-E511-B959-008CFA00FF80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B0F93CCD-2E7C-E511-A5F5-00259021A4B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/BA1E106F-127C-E511-B06D-002590207B90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/BCB3C282-877C-E511-9557-02163E010DF5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C028E3D3-E87B-E511-BA18-008CFA111314.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C08A193E-F57B-E511-98C8-901B0E542756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D4BAB03E-877C-E511-A1A2-02163E00F547.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DC1F1BED-977C-E511-814A-008CFA111354.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E26A4806-887C-E511-AEB1-02163E0147F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E4CFB428-887C-E511-AD9F-02163E01663A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E64F1752-0C7C-E511-A1E1-901B0E542962.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E812DEE1-E17B-E511-9B19-02163E00C920.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EC5A838C-0E7C-E511-9C0C-001E67504255.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F6DA20BA-E17B-E511-A792-901B0E542756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FA363095-877C-E511-8B86-02163E016BB2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FE82C799-877C-E511-B0F6-02163E013C5C.root' ] );


secFiles.extend( [
               ] )

