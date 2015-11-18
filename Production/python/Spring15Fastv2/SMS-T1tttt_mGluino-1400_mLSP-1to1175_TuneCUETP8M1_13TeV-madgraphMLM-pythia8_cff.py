import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/02BD196D-1180-E511-ADA1-008CFA052C0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0CB66277-1080-E511-AB4E-001E675799D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1048F193-1080-E511-AFC3-C4346BC78D10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/10D5A197-1080-E511-BE97-6CC2173BC050.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/18509990-1080-E511-8793-3417EBE6475F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1A361A95-1180-E511-B92F-6CC2173BC8B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/26A27783-1180-E511-91E0-00266CFFC544.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2EF2AD91-1080-E511-B4F2-00266CFEFC38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3A00917A-1180-E511-A286-C4346BC8F6D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3C9E8997-1080-E511-8E5C-20CF3019DEF5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/44B30288-1180-E511-ACC0-C4346BC78D10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/48FDCA95-1080-E511-991E-AC162DA8E1E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4AD1D4A1-1080-E511-A6E4-AC162DACC3F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4E29ADDB-1080-E511-9A86-901B0E5427A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4E889DB4-1080-E511-9E0E-001E67504FED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5277F492-1080-E511-8986-AC162DA8E1E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A54CB8B-1080-E511-80BF-C4346BC00270.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5E7F5982-1180-E511-8627-00266CFFC940.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/687E2783-1180-E511-B0CA-6CC2173BC050.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/68DF9C89-1180-E511-A9FE-00266CFFCAF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6AA59899-1080-E511-B13D-00266CFEFF04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6C4BB494-1080-E511-9CC6-C4346BC08440.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6E5615C2-1080-E511-B55C-AC162DACC328.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7250B280-1180-E511-905C-C4346BC8C310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/822A4852-1080-E511-85B3-3417EBE64591.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8CD5D4A1-1080-E511-AFA9-AC162DACC3F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8E29628B-1180-E511-8AB2-6CC2173BBE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9A280DDB-1080-E511-85E5-901B0E542804.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9EE61CA5-1080-E511-9330-00266CFFC13C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A2614F84-1180-E511-97E8-AC162DA8E1E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AA0F6794-1080-E511-8E78-00266CFFCAF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B215F697-1080-E511-ABAD-00266CFFC940.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B496E29B-1080-E511-BF7B-6CC2173BBF60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B662178F-1080-E511-9ED3-008CFA052C0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B6FC6F92-1080-E511-B46E-008CFA051DEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BA0A0596-1080-E511-883B-AC162DA87230.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BC58949D-1080-E511-B99F-20CF3027A5E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C470BB51-1080-E511-8869-3417EBE64774.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C4E2E393-1080-E511-9A23-C4346BC78D10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CA77549C-1080-E511-92B5-00266CFFC544.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CED7817D-1180-E511-85B8-6CC2173BBF60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D2D48F97-1080-E511-B221-C4346BC8C310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D4A6EF90-1080-E511-8FB8-00266CFFC544.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D6320B97-1080-E511-9683-00259021A4A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D69CDB98-1080-E511-B304-C4346BC7AAE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EA2E7283-1180-E511-9837-00266CFFCC18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EEE4107B-1180-E511-BF4E-008CFA052C0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F21BDD97-1080-E511-9477-6CC2173BBD80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F43E569F-1080-E511-A84F-AC162DACE1B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FA73AC80-1180-E511-9E72-C4346BC7AAE0.root' ] );


secFiles.extend( [
               ] )

