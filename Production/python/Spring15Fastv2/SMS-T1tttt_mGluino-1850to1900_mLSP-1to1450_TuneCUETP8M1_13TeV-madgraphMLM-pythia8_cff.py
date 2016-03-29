import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/02482ECA-1F7F-E511-9BA9-02163E0115F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/048251AC-1F7F-E511-953E-002590A4C6AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/06374CAA-1F7F-E511-B118-D4AE526A023A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/08541EB4-1F7F-E511-93C0-D4AE5269F656.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/089EFAC9-1F7F-E511-8484-02163E013C5E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/08D1A6AE-1F7F-E511-BB7F-D4AE526A0488.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0C40BAB4-1F7F-E511-8257-1CC1DE192872.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/164EC2D0-1F7F-E511-B602-02163E013C12.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1A7B2ECA-1F7F-E511-8CC3-02163E0115F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1EED6A08-207F-E511-9C54-02163E016BDE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/22730BCA-1F7F-E511-883B-02163E00C4C9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/24E2D803-207F-E511-9449-02163E012ED2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2EEA8CB1-1F7F-E511-86C1-002590200A80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/30C08CAC-1F7F-E511-B599-D4AE5269FEF3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/38436BBA-D07E-E511-B2B3-02163E014AB9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3A5B28DA-1F7F-E511-8EDB-02163E01673C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/40F464D1-1F7F-E511-8116-02163E0168E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/42BE6BCC-1F7F-E511-96CB-02163E016BCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4E4C6AAC-1F7F-E511-A0E3-002590A37116.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5878B2D8-1F7F-E511-98D0-02163E015132.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5ABC40CD-1F7F-E511-A2A4-02163E013C87.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/60106CD9-1F7F-E511-B9D6-02163E016BF1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/622A0DB3-1F7F-E511-BB54-00221961CD22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/68F14757-D87E-E511-AD6E-02163E014CF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6EF59C2D-207F-E511-B438-B083FED0FFCF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/727D7DAD-1F7F-E511-8125-D4AE526A0C89.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/749AC824-207F-E511-9837-B083FECFD4F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7AEAFAAB-1F7F-E511-A962-D4AE526A0B03.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8005A5B3-1F7F-E511-8A9D-02163E013265.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/80D879CF-1F7F-E511-934C-02163E011626.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8C268AF1-1F7F-E511-8C50-02163E016631.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8CD45DB6-1F7F-E511-A8B4-1CC1DE18CD26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8EFEFA2D-207F-E511-8D78-02163E016BC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/90B11428-207F-E511-954E-001F2965F296.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/90C1D583-207F-E511-97BC-02163E016BC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A4705AAB-1F7F-E511-9364-002590A83136.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AC1835C1-1F7F-E511-8F3E-02163E013DB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B065ABD6-1F7F-E511-B057-02163E016BDE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B6117BF5-1F7F-E511-B991-02163E011542.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BC8BAAA5-1F7F-E511-B053-002590A36FA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BE9D9406-207F-E511-A445-02163E011529.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C24143C9-1F7F-E511-9C9A-02163E00E9D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C4E1E8B3-1F7F-E511-988D-D4AE526A0DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CC696BFB-1F7F-E511-BB3B-02163E00F4D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CCF1E0A8-1F7F-E511-B79B-001E67396897.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CE0B6357-D87E-E511-8541-02163E00C81E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E036C8A9-1F7F-E511-A823-D4AE5269DC07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F6C2A1A6-1F7F-E511-AFDB-FA163E6E2764.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F6CBD0EB-1F7F-E511-B33B-02163E016830.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F80388B9-1F7F-E511-A87D-02163E014FAA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FAA4D801-207F-E511-9586-02163E00F4D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FCCB6B9B-1F7F-E511-9AEA-02163E015D8D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE3334C8-1F7F-E511-8D48-02163E016C2F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE507A97-1F7F-E511-8A6C-02163E014D07.root' ] );


secFiles.extend( [
               ] )

