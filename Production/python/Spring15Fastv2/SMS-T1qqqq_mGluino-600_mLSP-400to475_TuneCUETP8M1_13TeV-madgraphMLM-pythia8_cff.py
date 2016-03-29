import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/026ED2E9-C17F-E511-B16D-FA163E7E2FF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0C3D07AB-AC7F-E511-B493-02163E00F3E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/127DA6E2-C17F-E511-B979-FA163EFE6027.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/12943DDF-C17F-E511-A1FF-FA163E19FFD9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/18A1DBDD-C17F-E511-B689-FA163E552E17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1AAC10E2-C17F-E511-B01A-FA163E4635DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1EEDAADF-C17F-E511-9E05-FA163E50C94E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2076DCE1-C17F-E511-ABC5-FA163E3B0D45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/261502E5-C17F-E511-9D97-FA163EE61713.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/30E2FC61-BE7F-E511-9FA5-FA163E4635DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3E1FCDDE-C17F-E511-A5DD-FA163EA3B0B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3E771BE3-C17F-E511-92B1-FA163E4687E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/42557318-AD7F-E511-976E-02163E01682E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/54F532E2-C17F-E511-9B16-FA163E5819D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5EF29EE2-C17F-E511-9E09-FA163ECF339E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/64153EDE-C17F-E511-ADE4-FA163E1EDCF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/76AD15DF-C17F-E511-B61E-FA163E901F1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/78C801E5-C17F-E511-985D-FA163EE61713.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C2052E3-C17F-E511-9A89-FA163EB941FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/884909E3-C17F-E511-B8A7-FA163EB941FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8A3B250D-A67F-E511-B3B6-02163E00F6F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/989139E2-C17F-E511-AC7A-FA163E5819D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A03581DF-C17F-E511-BB89-FA163E718464.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A2882800-BE7F-E511-8BAD-02163E0148F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A8F6F6E1-C17F-E511-9316-FA163E5369B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B492B7E2-C17F-E511-A2FD-FA163EE004D3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B6D93491-C07F-E511-BFC4-02163E013577.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B86D27DF-C17F-E511-B1E9-FA163E5FAF88.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B86D46E3-C17F-E511-A3AC-FA163EFE6027.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BC95EDE2-C17F-E511-B7D3-FA163EB941FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C40077E1-C17F-E511-AA53-FA163E5369B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C47CB8E2-C17F-E511-AF4F-FA163EE004D3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CC3F1AE3-C17F-E511-BE7E-FA163EEF8E08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CC4F3036-C17F-E511-8393-002618943984.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D09115E2-C17F-E511-9EDA-FA163E4635DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DC929EE2-C17F-E511-A76F-FA163ECF339E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E4BC3DDF-C17F-E511-AB32-FA163E19FFD9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E820DCE7-C17F-E511-99EF-FA163E6A41D9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E87C7783-C07F-E511-9E27-02163E0115B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EE09B85E-C17F-E511-8E20-00261894387E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F2C2C4E9-C17F-E511-9584-FA163E7E2FF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F4F782AF-C07F-E511-B888-003048F00530.root' ] );


secFiles.extend( [
               ] )

