import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0699C847-7F7B-E511-AD4B-00248C0BE014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CC7D029-847B-E511-BC7A-0025905A48D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/10521132-847B-E511-8021-003048FFD736.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/166AE945-7F7B-E511-B3FE-0026189438F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A12E6E4-827B-E511-8C1D-0025905A497A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20A831E4-827B-E511-9AD9-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2402314E-7F7B-E511-87B4-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/24864F4C-7F7B-E511-9C91-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2C36ADE2-827B-E511-A049-002590593902.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/304756E3-827B-E511-B6FD-00261894389D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3264F131-7F7B-E511-AB15-0026189438E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A7D8DDF-827B-E511-9264-0026189438E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3CF48CE4-827B-E511-9A0D-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/42B64A4E-7F7B-E511-AB52-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/446B674D-7F7B-E511-9708-0025905A611E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/46F486E5-827B-E511-AD46-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48D0B3E4-827B-E511-920A-0025905A60BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/540B1CE5-827B-E511-9232-003048FFCB9E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/543C7A4A-7F7B-E511-90BE-0025905A60A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/56BD6B4E-7F7B-E511-860A-0025905A608E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/602F2A4B-7F7B-E511-89F5-002590593920.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62F730E0-827B-E511-9A74-002618943984.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66786B5F-807B-E511-85AE-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/70DEA53D-7F7B-E511-834E-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/72185BE4-827B-E511-9DE6-0025905A60B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A56E314-7A7B-E511-99F8-0CC47A0AD742.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80CC920C-7A7B-E511-B658-0CC47A0AD630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/84CBD6E4-827B-E511-9BE0-0025905A48EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A30F9E3-827B-E511-9D19-0025905A6070.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A556308-7A7B-E511-9CD0-00259029E87C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A66CCE4-827B-E511-9868-0025905A60A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/905BC54E-7F7B-E511-96FD-002618943940.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92D8064D-7F7B-E511-986F-0025905A6066.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96F2AC47-7F7B-E511-90E7-002618943983.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9AEF3734-847B-E511-AA01-00261894389D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9C69F46D-807B-E511-9EDF-0026189438E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AC2B94E5-827B-E511-93EA-0025905B858C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B661E14C-7F7B-E511-ACA9-0025905A6136.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C06FFFE5-827B-E511-8A1B-0025905A48D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C475A2E3-827B-E511-9F07-003048FFD736.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C47B5DE6-827B-E511-AC3E-0025905B85EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6301BE5-827B-E511-8754-003048FFCB9E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CAEA294E-7F7B-E511-946A-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE3C44E3-827B-E511-A88A-0026189438F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2A750E5-827B-E511-A567-0025905B859E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6FBBCE3-827B-E511-9F2C-0025905A609A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F82D3DE4-827B-E511-B5A8-0025905B855C.root' ] );


secFiles.extend( [
               ] )

