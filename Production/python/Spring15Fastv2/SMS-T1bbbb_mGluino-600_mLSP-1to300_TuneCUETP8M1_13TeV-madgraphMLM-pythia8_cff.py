import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A0C8E38-4C7C-E511-983F-001E67A3EBD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A1EA170-527C-E511-9750-001E675A6725.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/200D3E8E-487C-E511-8883-001E67A3FEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2011D08E-487C-E511-8777-001E67A3EF70.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EB4DC3B-4C7C-E511-B7E4-001E67A3EF48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3802E82D-4C7C-E511-9755-001E67A42BA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/426E994C-4C7C-E511-8C97-001517FAB928.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/46180C5C-497C-E511-B8E5-001E675A4759.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/545CD00E-4E7C-E511-B3E8-001E67A41EA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/547E8343-497C-E511-934D-001E675A6AB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/56F2E443-497C-E511-A9A4-001E675A622F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5A13344A-4C7C-E511-B94E-001E675A622F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5AF7154D-4C7C-E511-BDBB-001517FB1D0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E393B50-4C7C-E511-A863-001E67A3FC1D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/64A86898-487C-E511-8746-001E6758651B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E793DC0-487C-E511-B361-001E67A42026.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7ACE19CD-4E7C-E511-80F2-90B11C094A7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7EAEFC9F-4B7C-E511-92C5-90B11C070100.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80D802A5-4B7C-E511-A02C-90B11C0701C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/86F98F52-497C-E511-9E06-001E675A6AA9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E497598-487C-E511-81CD-001E6758651B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8EAECE53-4C7C-E511-AC16-001E67A42026.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9CD5173D-497C-E511-9FD3-001E67A3EB1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AECDF1A1-4B7C-E511-BC76-001E67A404B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B205439C-4B7C-E511-AC04-001E67A3F8A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BE654194-487C-E511-BDE1-90B11C064AD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C07FD7A5-487C-E511-A529-001E675A6AA9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C085752B-4C7C-E511-AD18-001E67A3EA11.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC175E66-497C-E511-A68D-001E675A69DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D230932D-4C7C-E511-B4C6-001E67A4061D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D41D748E-487C-E511-B7A6-001E67A3F70E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4DA4739-497C-E511-A994-001E67A42175.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D800F89A-497C-E511-92C7-001E675A68BF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D8D89147-497C-E511-B6D4-001E675A6A63.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA9EBDB0-4B7C-E511-B2A5-001E6758651B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC6BFC4C-4C7C-E511-8DF0-001E675A69DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE5AB543-4C7C-E511-B959-001E675A6C2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E404B19D-4B7C-E511-AE48-001E67A3FD26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E40F5154-497C-E511-9B2B-001E6758651B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4158341-4C7C-E511-A3D0-90B11C05054D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6221D46-497C-E511-9D32-001E67A3FDF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6B3683E-4C7C-E511-8188-90B11C08C1BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE3D7D45-497C-E511-B385-90B11C0506C6.root' ] );


secFiles.extend( [
               ] )

