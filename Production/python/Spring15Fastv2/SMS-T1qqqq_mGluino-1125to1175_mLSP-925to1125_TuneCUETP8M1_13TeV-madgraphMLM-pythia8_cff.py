import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/04C7A442-4981-E511-A2A4-00266CFBE88C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/108E2445-4981-E511-B18D-A0369F7F9EDC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/12896642-4981-E511-9103-549F35AE4F6E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/16F41A42-4981-E511-92A9-549F35AE5024.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1AE17E51-4981-E511-B9C2-549F35AF4524.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CE0B10D-4A81-E511-B779-008CFA1983E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CF8284D-4981-E511-AB46-00266CFCC304.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20F26549-4981-E511-B1BD-00266CF3DF14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/28DE610D-4A81-E511-81E0-008CFA198258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2A6B1643-4981-E511-9C09-A0369F739F08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CA89949-4981-E511-A393-00266CFCCD94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CF1594A-4981-E511-AC38-008CFA580920.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/388BDF0E-4A81-E511-98E8-008CFA151F98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3EB07F0C-4A81-E511-8BA8-008CFA56D58C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3EDEC00B-4A81-E511-BD96-008CFA1CB8A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48E9933D-4981-E511-8DBB-A0369F7FC608.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5A751E4C-4981-E511-9EE7-008CFA0A5818.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5C070710-4A81-E511-B762-008CFA0647E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5C7EB144-4981-E511-AC25-549F35AD8C0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5CF0F533-4981-E511-9786-001E67A3F70E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/60101749-4981-E511-B450-A0369F7FC070.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/842BF648-4981-E511-9B97-00266CFCC1B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86FEF04B-4981-E511-B672-008CFA0648E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CFC4C0E-4A81-E511-8117-008CFA0648FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96350E83-4981-E511-A557-A0369F7FC770.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/969C5E35-4981-E511-973C-90B11C0701C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9ED1ED0D-4A81-E511-90EE-008CFA110B10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA78944B-4981-E511-B904-549F358EB76F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B608453B-4981-E511-A5E7-001E675A6630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C452E650-4981-E511-9558-008CFA0A59E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6EA1046-4981-E511-B416-549F35AE5024.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D49D5144-4981-E511-8FA0-00266CF3DE70.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D652B740-4981-E511-8562-A0369F7F92FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2744345-4981-E511-B939-549F35AD8B61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4214BCA-4981-E511-8354-549F35AC7E22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8479D76-4981-E511-A027-549F35AC7E15.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8E4D90F-4A81-E511-9A04-008CFA0A5914.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA4D170D-4A81-E511-864E-008CFA198258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0AB6F42-4981-E511-AFAD-549F358EB796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0AFEEE1-4981-E511-8664-FA163EFE6027.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0D2060B-4A81-E511-9A3B-549F35AD8B88.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8B33E40-4981-E511-A254-001517E73CA0.root' ] );


secFiles.extend( [
               ] )

