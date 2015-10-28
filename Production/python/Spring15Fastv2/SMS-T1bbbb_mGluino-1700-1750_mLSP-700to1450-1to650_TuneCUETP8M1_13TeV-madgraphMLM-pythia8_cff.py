import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/00143444-8D7C-E511-BA74-7845C4FC39C5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/22C6BDDC-647C-E511-8AA1-008CFA00FCC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/36E3F4C1-537C-E511-9B95-00266CF9B970.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3AC921C9-537C-E511-AF92-00266CF9B878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3EB8B9F2-3A7C-E511-8BFD-5065F38162B1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/421BFA52-657C-E511-86B8-00266CFFA240.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4652D3FA-537C-E511-BCD0-00266CFABAF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4A679ABE-647C-E511-93F7-008CFA00FF00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4EBD76A5-657C-E511-ADB8-008CFA010718.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/541AA32A-657C-E511-9627-008CFA111220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/585701A0-467C-E511-8B70-24BE05C6C741.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/620BB9AB-657C-E511-AD5A-008CFA00F690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/62C87CC7-647C-E511-A096-008CFA111220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/642C41E0-537C-E511-8AAB-00266CF9B318.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/667238BA-537C-E511-BA66-3417EBE65E39.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6A0A2F66-657C-E511-AA62-008CFA010718.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7415BC87-3D7C-E511-956B-5065F381E201.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7812C2AD-567C-E511-B032-D4AE526A0CFB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7C39FA45-8D7C-E511-BFA9-00266CFADEC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7CCDB5BE-517C-E511-B2EC-001EC9B2147A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/849D26BA-537C-E511-8E4A-3417EBE65F56.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8E2384A6-657C-E511-92A8-008CFA010E1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9075ADA6-657C-E511-9640-008CFA00FCC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/90ECFFBF-647C-E511-8A6A-008CFA00F690.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/983069BA-647C-E511-A923-0025904A8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/988039BD-647C-E511-A131-00266CFFA240.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9E88425F-657C-E511-92C4-008CFA111220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A264D3FA-537C-E511-9E1F-00266CFABAF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A63FFE5E-547C-E511-AA75-00266CF271E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B02F3347-8D7C-E511-BC2D-00266CFAE1EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B0E5B874-657C-E511-8091-0025904A8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B47A3FC1-537C-E511-B0A1-00266CF250C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B867D212-567C-E511-9F5F-842B2B76653D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/BC6C0C25-657C-E511-B2DB-008CFA111220.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C64CAB55-657C-E511-A494-008CFA00FCC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DA78AFC3-537C-E511-9478-00266CF9C318.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E4032AE8-517C-E511-AB12-001EC9AF1FD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E44DDA43-8D7C-E511-B486-7845C4FC374C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F2ABE45E-657C-E511-804B-008CFA00FF00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F4ACA4C1-537C-E511-A435-7845C4FC35CF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FCAFE725-657C-E511-B398-008CFA00FF00.root' ] );


secFiles.extend( [
               ] )

