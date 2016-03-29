import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/02F36E26-2D7F-E511-AAFD-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/166A302F-2D7F-E511-B230-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1C066F26-2D7F-E511-A725-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E5AD587-2D7F-E511-8D61-00259074AE2E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/20AC7624-2D7F-E511-BE56-A0369F7FC770.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2283AC29-2D7F-E511-82A3-008CFA0A570C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/32F10A1B-2D7F-E511-A52D-001E4F1BC725.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/38586337-2D7F-E511-82F7-02163E013DB2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3C765325-2D7F-E511-B446-549F358EB76F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4C705F23-2D7F-E511-A2EF-44A84225D36F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/545D8567-2D7F-E511-9905-00259073E522.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/54CAE026-2D7F-E511-B56D-008CFA1CB55C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/54F87626-2D7F-E511-ACFD-008CFA197D10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6A8B061B-2D7F-E511-B751-00259073E4F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6CE61428-2D7F-E511-88AC-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/76069C2B-2D7F-E511-AC65-00266CF3DF14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/78293428-2D7F-E511-A452-549F35AE4FE3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7A115225-2D7F-E511-98FF-549F358EB76F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C470D28-2D7F-E511-8C0C-002590D5FFF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7E47CA72-2D7F-E511-8279-00259074AE5E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8074DD26-2D7F-E511-BE98-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/82322CA9-2D7F-E511-B8EB-02163E016C07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8286746C-2D7F-E511-87AF-02163E00EA13.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8897362F-2D7F-E511-94A3-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/92162026-2D7F-E511-9A2B-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/92666798-2D7F-E511-B96F-02163E00EA7B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9C0C302F-2D7F-E511-894C-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9C0FD626-2D7F-E511-BB26-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9C76E226-2D7F-E511-96CA-549F35AD8C17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9CAE1746-2D7F-E511-867D-02163E014DA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A8C83A2A-2D7F-E511-B0EC-00259073E344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B0334098-2D7F-E511-B4DF-02163E016A78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B4671B26-2D7F-E511-80C7-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B4F80028-2D7F-E511-B835-002590574A44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C255ED2A-2D7F-E511-A0CE-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C26C132A-2D7F-E511-B83B-008CFA0A5640.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C687662B-2D7F-E511-9B26-00266CF3DF14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C6F26E26-2D7F-E511-8FC8-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C8CA312F-2D7F-E511-9594-A01D48EE831E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D4A6E326-2D7F-E511-9041-549F35AD8C17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DEEFEF26-2D7F-E511-8856-549F35AE4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EA8A8463-2D7F-E511-969D-549F35AD8C17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/ECC5DA66-2D7F-E511-B5F2-02163E011529.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/ECF83542-2D7F-E511-9383-02163E016BA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F4378367-2D7F-E511-9BA3-00259057490C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE9B60B2-2D7F-E511-8B47-02163E0169DD.root' ] );


secFiles.extend( [
               ] )

