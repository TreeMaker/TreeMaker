import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/00CD9CD9-1F83-E511-8CDD-002590494DCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/045E5117-2083-E511-AE2A-02163E00C4FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/047853C9-AC82-E511-B4C2-5065F38162B1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/06EA8167-2083-E511-B13B-02163E00C4C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0CDABC18-2083-E511-9CA4-02163E01449A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/12D84A36-2083-E511-AA05-02163E014E5D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/18FD9B3F-2283-E511-BC65-782BCB40899C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1AC6860E-2083-E511-94AD-02163E011BDE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C3FD6A4-1E83-E511-AE2A-02163E00AD7B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2C5781AD-1F83-E511-9E69-02163E013DAA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2CB0EBE5-1E83-E511-9C63-02163E014888.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3243524B-1E83-E511-AB9A-02163E00C4C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4066F11B-1E83-E511-9FFD-02163E013562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/40C4CB48-2283-E511-B377-000F53273740.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/449D1C04-2083-E511-B683-02163E013A0E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4808877C-1E83-E511-9CC2-02163E00E5E7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4C12EEEC-1F83-E511-90F5-02163E0115AF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4CA982DA-1F83-E511-AA9D-02163E011DFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/56E63756-2083-E511-8F9C-02163E0141DD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/58BACDDD-1D83-E511-A8F2-02163E013C79.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5C8EDF11-1E83-E511-81B7-02163E013DAA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5E390A0B-2083-E511-999E-02163E016A5A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62505551-1E83-E511-9094-02163E013F32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/68661055-2083-E511-B43E-02163E00BF33.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6A7FEA50-2083-E511-9A14-001E675049F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/72C7550E-2083-E511-AED1-02163E010E5A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/740B0037-2083-E511-8C72-02163E0114EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/90212A76-2083-E511-96DD-02163E016685.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/90F27720-2083-E511-8F1F-02163E012A98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/923DACA7-0D83-E511-BA45-0CC47A13CB36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/96240123-2083-E511-8979-02163E013F32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9E034C70-1E83-E511-BE9D-02163E00EB25.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A87587D3-4F82-E511-8E63-74867AF198F1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AAF62CDD-2183-E511-91E5-782BCB285E3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C2129DDF-2083-E511-B1F1-02163E0115F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CC7AA3F4-AC82-E511-9670-001EC94BF710.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D4FBF004-2083-E511-A6A5-02163E013F9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DAF72C98-2183-E511-9131-ECF4BBE1CD58.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E48EFB56-2083-E511-A266-02163E011A84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E6531A12-2083-E511-981B-02163E010DB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EA22B210-AD82-E511-8A9D-D4AE527F2883.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F2459CC9-1F83-E511-9D3E-02163E013D67.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F88729D4-2183-E511-A2C5-000F530E4AB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FE5C89F7-1D83-E511-934F-02163E015205.root' ] );


secFiles.extend( [
               ] )

