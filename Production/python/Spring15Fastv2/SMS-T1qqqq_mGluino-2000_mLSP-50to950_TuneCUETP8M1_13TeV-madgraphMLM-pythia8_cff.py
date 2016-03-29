import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08BF7B7A-5281-E511-B333-02163E016B9B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A3D853D-5A81-E511-B22C-02163E00EB1B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3ADBBB3C-5C81-E511-ABC3-02163E01481B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E1D8924-5C81-E511-9404-D067E5F90FA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/501A2F01-5C81-E511-8E9B-02163E013D39.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/663CA265-5B81-E511-9472-02163E00B48D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/74EA1206-5781-E511-BBCA-02163E00E615.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7816D10A-5A81-E511-B99D-549F35AD8C0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9AA40081-5481-E511-9794-008CFA0A56C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA27F2A4-5B81-E511-A4D4-02163E00CA06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C04E160C-5C81-E511-ABB4-D067E5FAB927.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2D2D831-5281-E511-8D35-02163E00B48D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA1CF3C0-5B81-E511-983D-02163E016B1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D2C366EF-5581-E511-B81A-D067E5FAB903.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D6B76698-7D81-E511-A7FC-0025905B8610.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA2CB792-5981-E511-943A-549F35AE4F6E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE54D799-7D81-E511-BA28-0025905B8598.root' ] );


secFiles.extend( [
               ] )

