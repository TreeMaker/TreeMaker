import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/042D560D-7C7B-E511-BDA2-0002C92DB46C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/06B0B0B9-997C-E511-ACD4-E41D2D08DF30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/08DA91AC-997C-E511-A2D3-E41D2D08DDF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0AACA4A7-997C-E511-9CF8-002590494E38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0ADD7444-7A7B-E511-85F3-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1643F44D-7A7B-E511-8E70-0002C94CDAE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/16675EA4-997C-E511-91C2-002590A2CDA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/18E51270-7C7B-E511-9116-5065F381D2C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/204BC948-7A7B-E511-BF88-F45214C748C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2819CC54-997C-E511-B371-047D7B881D62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2E1CA635-997C-E511-9CAA-002590AC4C56.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/349888B7-997C-E511-AB0E-002590AC4C6C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/38B6EE0C-7C7B-E511-87D4-0002C90F8094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3CE2D948-7A7B-E511-AB8A-0002C92DB45C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3E9D07B1-997C-E511-B388-F45214939730.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4403EBB1-997C-E511-8F2E-047D7B881DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4657AF44-7A7B-E511-925B-24BE05C6E561.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/48360B7B-7A7B-E511-B814-0002C92958E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5001D6B2-997C-E511-847D-E41D2D08E100.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/502F2775-7C7B-E511-83C0-0002C92958E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/58EC5150-7A7B-E511-8BE7-0002C94CD120.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5A95C54F-7A7B-E511-AF5C-0002C94CD120.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5CFC1729-997C-E511-A0C3-0025907FD242.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6A7CCE6B-7C7B-E511-82CF-5065F381E1A1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6E001243-7A7B-E511-9CFB-24BE05C44BC1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/721CFF4C-997C-E511-892D-002590A2CDA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/76996B87-997C-E511-94A5-002590AC4CC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7AD57C8B-997C-E511-8313-0025907FD428.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/821D2743-7A7B-E511-9A35-5065F381E1A1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/827200D3-7A7B-E511-9145-24BE05C6E561.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8461BD48-7A7B-E511-A88E-0002C92DB45C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/848FF744-7A7B-E511-A058-24BE05C46B01.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8890B34C-7A7B-E511-9E50-0002C92DB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92950A50-7A7B-E511-A056-F45214C748CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/98DA706F-7C7B-E511-838F-24BE05C48801.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9C102F45-997C-E511-90E4-002590DB919E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9E080248-7A7B-E511-8663-0002C90F8094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A467B552-7A7B-E511-B080-24BE05BD0F81.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AE1D0E53-7A7B-E511-A534-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C08234DD-7A7B-E511-8B13-24BE05C46B01.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C21D0E53-7A7B-E511-8CAE-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D0CEEBB3-997C-E511-B042-047D7BD6DEFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D2A6CD07-7C7B-E511-9E52-24BE05C60641.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D44C3F2F-7C7B-E511-B18B-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DACF9BD2-7A7B-E511-96F5-24BE05C44BC1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DEF8B7D9-7A7B-E511-84F5-24BE05BD0F81.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E029EFB3-997C-E511-AE9C-047D7BD6DEFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E624C548-7A7B-E511-A63C-0002C92DB530.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FC99B64E-7A7B-E511-B947-0002C92DB46C.root' ] );


secFiles.extend( [
               ] )

