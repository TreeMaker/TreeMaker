import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/00C16A66-F17B-E511-A7CB-0025905A6126.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/022F7043-EF7B-E511-8717-001EC9AF037C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/083C74EA-EF7B-E511-ADAE-0025905A6126.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0CEDC357-F17B-E511-A93C-0025905A48EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0E0EE3E9-EF7B-E511-9428-0025905B8598.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/10F93BEA-EF7B-E511-83EF-0025905A60F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1AD863F6-F07B-E511-9A15-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1CEA0BEB-EF7B-E511-9D86-0025905A48EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2299CB44-EF7B-E511-ABD8-0CC47A009E26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/263FC75B-F17B-E511-8AA5-0025905B8598.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/36077E18-F17B-E511-980B-00261894386D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/364E0B46-EF7B-E511-AC5A-D4AE526A05F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3C824F45-EF7B-E511-B34D-842B2B7680C9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3E2446EB-EF7B-E511-B606-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3E7C9F4C-F17B-E511-886E-002618943966.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/44231822-F17B-E511-97FD-00261894398B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/44AFCFE9-EF7B-E511-BBFD-0025905938B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/484C6EFF-EF7B-E511-B57C-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4A721255-F17B-E511-BEBB-0025905A60F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5404C94A-EF7B-E511-B851-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/548DF31C-F17B-E511-A322-0025905A48EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/587571FF-EF7B-E511-9350-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5CD4FC43-EF7B-E511-BF6B-0CC47A010010.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/60F370E8-EF7B-E511-8305-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/640E5BE9-EF7B-E511-B871-00261894385D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/665FB33C-F17B-E511-852E-00261894385D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/688636EC-EF7B-E511-9B65-0025905964A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6A431F13-EF7B-E511-85B5-001EC9B22502.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6E80E0EC-EF7B-E511-9352-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/74843944-EF7B-E511-B7E7-D4AE526A0461.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7AD8A6E5-EF7B-E511-81DA-0026189438BF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7C1DADE8-EF7B-E511-93C7-0025905938D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8ADADC48-EF7B-E511-A1C8-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/929B8AE5-EF7B-E511-B5A6-00261894394B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9A4CEB39-F07B-E511-8CFF-002618943966.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9E211D44-EF7B-E511-AF03-001EC9B218D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A43E343B-F07B-E511-904E-00259059649C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AA722DEA-EF7B-E511-8D8D-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AAD50139-F17B-E511-B6EC-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B29D0643-EF7B-E511-AEBF-0CC47A01CAEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B864BAE9-EF7B-E511-9ADE-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C6194245-EF7B-E511-AAC3-D4AE526A0A4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C84D9DEA-EF7B-E511-B330-0025905A60F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D012F142-EF7B-E511-9CDF-0CC47A009352.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DEE3821B-F17B-E511-8E12-0025905A48F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E0BD46EB-EF7B-E511-8A4A-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E2CF2E54-EF7B-E511-A8F4-1CC1DE192766.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E4999044-EF7B-E511-BAE2-0CC47A01CB76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E6E2FE3D-F17B-E511-92DF-002618943864.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F26467E9-EF7B-E511-87FB-003048FFD760.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F2C4B534-F17B-E511-8FF9-0026189438BF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F2ED0356-EF7B-E511-B6A4-0CC47A00934A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FAAB17EA-EF7B-E511-AE61-0025905A60AA.root' ] );


secFiles.extend( [
               ] )

