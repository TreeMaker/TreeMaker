import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0473CB4E-607C-E511-A1E2-00266CFFC76C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/16CCE51F-5F7C-E511-A6DD-6CC2173BBAA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CB3B927-5F7C-E511-928B-00266CFFBCFC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1E402A3B-607C-E511-BD18-C4346BC7EDD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2477B573-5F7C-E511-9276-00266CFEFF04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/30A71149-607C-E511-ADCD-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3223EF20-5F7C-E511-9F37-6CC2173BC220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38643624-5F7C-E511-B308-00266CF91A18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E14EC4E-5F7C-E511-AA3B-00266CFFBF90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/44A6FF77-E57B-E511-892D-D4AE526A0419.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4AEDE853-5F7C-E511-B69F-00266CFFC4E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4CBC5520-5F7C-E511-87A6-6CC2173BC1D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E84574E-607C-E511-9175-00266CFFC4E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50598B48-607C-E511-A64B-C4346BC85718.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5493E920-5F7C-E511-A315-C4346BC70B58.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/64979F0C-E67B-E511-9A14-842B2B7682B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EB0A84C-607C-E511-B242-AC162DABBBA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/74A2D483-5F7C-E511-9142-C4346BBF3E78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/766ACF4F-607C-E511-AEFF-00266CFFCD50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C1B6060-E57B-E511-A2B4-0CC47A009E22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E163F4A-607C-E511-BEB5-C4346BC076D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82107E1D-5F7C-E511-AB37-6CC2173BBA60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8ACB397B-5F7C-E511-956F-00266CFEFF04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CD72A18-5F7C-E511-AF2B-008CFA052C0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9231FA41-607C-E511-B436-008CFA052C0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/961CDC48-607C-E511-B90E-6CC2173BBA30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A62CB820-5F7C-E511-ABC5-AC162DABAF78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B0F1CDA9-5F7C-E511-B8CA-00266CFF0ACC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA01AA0A-E67B-E511-B64D-D4AE526A0DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D0DCDB1D-5F7C-E511-B468-6CC2173BC2E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D63D1B22-5F7C-E511-9641-00266CFE79A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E02FDC45-607C-E511-84AB-6CC2173BBAA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0E3F550-5F7C-E511-8F7E-00266CFFC76C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6E6254E-607C-E511-B8B4-00266CFFC4E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA17590B-E67B-E511-8AAC-D4AE526A0A4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE39051F-5F7C-E511-98DC-C4346BC7EDD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F02BBC27-607C-E511-8703-6CC2173BBAA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0829676-E57B-E511-8247-D4AE5269FD24.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0AA942B-5F7C-E511-B306-00266CFFC76C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F225E449-607C-E511-BBB0-00266CFFC4C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F839CA1D-5F7C-E511-9733-6CC2173BC2E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8949C1D-5F7C-E511-9E19-6CC2173BBA60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA7A1B52-5F7C-E511-BAE3-00266CFFCC50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA9CC974-E57B-E511-BBA8-D4AE5269DC07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FC0091A9-5F7C-E511-8588-00266CFFC4E0.root' ] );


secFiles.extend( [
               ] )

