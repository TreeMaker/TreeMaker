import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A80EACD-C682-E511-BEF7-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0EBA42A8-C482-E511-868D-002618943974.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/14DFEAAC-C482-E511-A44E-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/300B39AD-C482-E511-86D1-0025905A607A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/302C2F16-C782-E511-A4A8-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3645C5B6-C682-E511-9F31-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3802F4A7-C482-E511-88AE-0026189437EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38D50D1D-C782-E511-830D-0025905A4964.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A6B79AD-C482-E511-A9A7-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3C6D6F29-C782-E511-954C-002618943966.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3CCA28BE-C682-E511-80B6-0025905A6076.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E829C4B-3685-E511-B1B4-001E67E68677.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/46C11AC1-C682-E511-AE9D-0025905A610A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/482751A2-C482-E511-93E6-0025905A6092.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/488812AD-C482-E511-B40C-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/58D942AD-C482-E511-B583-00261894390A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/622BD7AD-C482-E511-8E8A-0025905A6076.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6238C2AB-C482-E511-AA60-0025905A60B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/626E9BA4-C682-E511-A37B-00261894396E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62BBD2A9-C482-E511-AF28-0026189438F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/648C4CAD-C482-E511-814C-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6697CDEF-C682-E511-A5CC-0025905A48D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CC070AC-C482-E511-B073-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7AFFC601-C782-E511-B01B-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7EBCEDD3-C682-E511-939A-0025905B858E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/805A8A53-C482-E511-B038-00259059649C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/826DB4BE-C482-E511-A3D6-003048FFD740.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82BD7D65-C882-E511-9ADA-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A7816AE-C482-E511-8435-0025905B858E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/90B77AF8-C682-E511-959A-0025905A6134.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9435A000-C782-E511-A9AD-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A0F18624-C782-E511-94F1-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A4F2FFAD-C482-E511-900C-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AC393B1C-C782-E511-8D4F-0025905A60B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B2F35AAD-C482-E511-ABF5-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA620EEA-C682-E511-A93C-0025905A48D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC0F3BEB-C682-E511-9A40-0025905A497A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2A967AD-C482-E511-8946-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C48DD598-C682-E511-8FD1-002590593872.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C4EFE3AC-C482-E511-AB84-00261894383B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D26A8F4B-C482-E511-9B7E-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D67BC228-C782-E511-89C6-0025905A608E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D8F281AC-C482-E511-BBD0-0025905938AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE95A4E3-C682-E511-AC3A-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E24A15AD-C482-E511-8B32-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E40D5EE3-C682-E511-8C27-0025905B858A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8ECADAD-C482-E511-AF5B-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECD3EFE7-C682-E511-8FA4-0025905A612E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F23E7A0A-C782-E511-8CD1-0025905A612C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F41194AA-C482-E511-96A8-00261894396E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F496F228-C782-E511-9190-0025905A60BE.root' ] );


secFiles.extend( [
               ] )

