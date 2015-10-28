import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0223C2B4-977B-E511-ACAE-003048FFCB9E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0EA3D9B6-977B-E511-8830-0025905AA9F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0EA41E65-947B-E511-9CF2-0025905A48FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/142B81AC-947B-E511-9C40-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/144210B3-977B-E511-AD93-0025905964C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/181A5EB6-977B-E511-B7CA-003048FFCC1E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A3F6860-947B-E511-9EFC-0025905A48BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1E2930B1-977B-E511-828D-00261894390E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/244E0FAA-947B-E511-BDF1-002618943964.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26514673-947B-E511-B426-0025905B85B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26C3F3AD-947B-E511-A387-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/28BC5CB0-977B-E511-8BA1-002618943954.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4282F3B6-977B-E511-B69A-0025905A48D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A2710B6-977B-E511-81E6-0025905A60AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A4454AD-947B-E511-8042-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4CEE8D6D-947B-E511-B884-0025905B859E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E672961-947B-E511-874E-0025905A60F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62BDCF5F-947B-E511-9FEA-003048FFCBA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/729093B5-977B-E511-9519-0025905A610C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A0E2F79-947B-E511-A274-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7EDF70AD-947B-E511-9A59-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/84BA836E-947B-E511-9B7F-0025905A60A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/900BCFAC-947B-E511-BE18-0025905A60E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96757CAD-947B-E511-BDD0-0025905B860C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96EBB26F-947B-E511-9530-003048FFCB96.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9858E5B6-977B-E511-953D-0025905AA9F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/98BB755D-947B-E511-9AAA-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A863157-947B-E511-A6F7-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A9F20B5-977B-E511-8F82-0025905A612E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A4EC22B6-977B-E511-8387-0025905A6068.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C0BD5076-947B-E511-A137-0025905A60B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA640DB5-977B-E511-89D8-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC2131AD-947B-E511-91B8-0025905A609E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CEAB48B6-977B-E511-8D0B-0025905A606A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC3CC3B5-977B-E511-9B27-0025905A60AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC8C825E-947B-E511-817F-003048FFCC18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE1D7B69-947B-E511-B14D-003048FFD720.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E285D269-947B-E511-8313-0025905A611C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EEB753B6-977B-E511-83D2-0025905A612A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA9263B0-977B-E511-983F-00261894393C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FC30F47D-947B-E511-B624-0025905A48D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FCF090AD-947B-E511-8F62-0025905A48D8.root' ] );


secFiles.extend( [
               ] )

