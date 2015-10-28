import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/02B3E2FE-9C7B-E511-A38B-0025905A6110.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0607C448-A67B-E511-9D7C-008CFA1112F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08E42D90-9D7B-E511-98A1-002618943916.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0E3D8494-9D7B-E511-9F3E-0025905A60C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/147D0173-507C-E511-8990-00266CF9C244.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1497AE38-A67B-E511-B94E-008CFA111310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/205C8792-9D7B-E511-AAB3-002618943930.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20665191-9D7B-E511-A321-00261894387A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2861700B-9D7B-E511-894D-003048FF9AA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CD5FA8F-9D7B-E511-A5B3-0026189437E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EF0E5F6-9C7B-E511-93DA-0025905A610C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3479D7CB-9C7B-E511-B23C-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A53B594-9D7B-E511-A0BA-0025905A60E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3CCF1D90-9D7B-E511-9780-002618943966.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3E37CD94-9D7B-E511-BDC1-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C2B19F7-9C7B-E511-BE4C-0025905A60B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4CAB6061-9D7B-E511-AFBC-0025905A60B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5288E594-9D7B-E511-8098-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/564C6796-9D7B-E511-8912-0025905A612C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E074236-A67B-E511-AE13-002590552126.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6421D33E-A67B-E511-97AE-008CFA1974CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66C0B294-9D7B-E511-96C2-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CDE0F4C-A67B-E511-A389-00259054C796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7441A771-507C-E511-BB6D-00266CF9B684.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7ABB2974-507C-E511-8A97-008CFA00148C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C8A3F6F-507C-E511-9F26-008CFA000BB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82A86B96-9D7B-E511-B076-0025905A60BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8438FD0E-A77B-E511-8D8C-008CFA111354.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86057B17-A77B-E511-A4DC-008CFA11139C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9E0A0E31-A67B-E511-9249-008CFA111310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9E99E794-9D7B-E511-9723-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA4947F7-9C7B-E511-A408-0025905A6110.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA773C29-9D7B-E511-959F-0025905964BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE3C6F78-517C-E511-BA6B-00A0D1EE8D7C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AEAFF295-9D7B-E511-8D51-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B41A7D1E-A67B-E511-AEA7-0025905487EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE79879F-507C-E511-BD9E-008CFA001DB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4600994-9D7B-E511-A1D5-0025905A611C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA88816C-507C-E511-80B9-3417EBE5281F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE296E21-A67B-E511-B319-008CFA1111A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E605E8B9-9B7B-E511-8332-02163E00F4AD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA37D96E-507C-E511-B93E-008CFA000BB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F402A84D-A67B-E511-8105-0025905488FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F403E3F2-9C7B-E511-B36A-0026189438E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA855296-9D7B-E511-ABC3-0025905A6126.root' ] );


secFiles.extend( [
               ] )

