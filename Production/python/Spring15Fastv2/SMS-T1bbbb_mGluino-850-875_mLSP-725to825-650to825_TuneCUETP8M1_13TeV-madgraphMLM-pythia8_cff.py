import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/049BE935-A77B-E511-A1A9-000F53273650.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/086632CA-A57B-E511-B9CA-ECF4BBE15DA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0EFB0A14-A77B-E511-8E32-000F53273738.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/12985BED-A47B-E511-9678-782BCB283FAD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/165FACB4-7B7B-E511-AA2D-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2224389E-7B7B-E511-95F3-00261894390B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/242133B3-7B7B-E511-916B-0025905964C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/380AC903-A77B-E511-A76C-AC853D9DACE5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E413F1B-A57B-E511-B961-782BCB407EDE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/403CDEF5-A67B-E511-BE0E-782BCB6E13BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C11210E-A77B-E511-85B1-842B2B298D13.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50B65EE6-A67B-E511-8E4C-B083FED7477A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5ACB3BB6-7B7B-E511-9EE5-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/600437DE-A57B-E511-BA28-782BCB6E1220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/623A3AAA-7B7B-E511-8E9C-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6688F903-A77B-E511-98D2-008CFAF060D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66C3B2EC-A67B-E511-BDA0-AC853D9F5344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A69ECB6-7B7B-E511-95DD-0025905A611E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EC6D9DE-A57B-E511-B6AD-AC853D9F52D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EE29BB7-7B7B-E511-B22A-0025905A609E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/764CCBEB-A57B-E511-A15E-000F53273738.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C10CAD2-A57B-E511-8186-B083FED7593B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8416DBB5-7B7B-E511-B887-0025905A60B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/847359CE-A57B-E511-B377-B083FED76520.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88568AB8-7B7B-E511-BC9D-0025905B8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8AA28FA6-7B7B-E511-A674-002618943926.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8AAFA9D2-A57B-E511-88E3-008CFA111310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/904FCDE5-A57B-E511-AA32-782BCB6E0A6D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96C740E4-A67B-E511-BB12-008CFAF06CA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A2E1B08-A77B-E511-A6B0-AC853DA06B7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9ABB4208-A77B-E511-8328-782BCB407CF7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9E1508B6-7B7B-E511-BDA6-0025905A60B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A8F841B2-7B7B-E511-B232-0025905B85D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE199D94-7B7B-E511-886B-0026189438E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BED32AD1-A57B-E511-A146-AC853DA06A54.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6270CE5-A47B-E511-BBE1-008CFAF07110.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA93F2B6-7B7B-E511-8FCB-0025905A6122.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DAEC8E13-A77B-E511-8605-AC853DA06A54.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DEB41408-A77B-E511-A8B2-008CFAF0751E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2064F71-7B7B-E511-9FFB-0025905B85B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E20BD00A-A77B-E511-955D-008CFA501F68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2928BBA-A57B-E511-A2E6-AC853D9F5344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E8DACBF0-A47B-E511-9E9B-AC853D9F5120.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F02A48F4-A47B-E511-A1F6-782BCB408B63.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6DF0FF2-A67B-E511-83DA-008CFAF060D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA7F43BC-A57B-E511-85AD-AC853D9DAC29.root' ] );


secFiles.extend( [
               ] )

