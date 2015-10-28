import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/003DC68D-297C-E511-83A6-44A842CFC9D9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/02E462A4-B97B-E511-88DD-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/04A1CC38-297C-E511-8F14-B499BAAC068A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/06299100-B97B-E511-B189-0025905A60F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A069F25-277C-E511-BB7F-44A842CF058B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/142FB836-297C-E511-8BEC-6C3BE5A4D8E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/222CAC73-297C-E511-B295-44A842CFD633.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/247FACBB-277C-E511-9576-44A842CFCA0D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26DD601E-297C-E511-B3C3-44A842CFD640.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/28B2075F-9C7C-E511-9D3D-6C3BE5B5A088.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EAB703A-277C-E511-B87F-44A842CFD626.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A399A08-277C-E511-BDF4-001E0B466D08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/40272593-B97B-E511-B2E0-00261894393D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4488CDDD-5B7C-E511-9C24-001CC4C0B0DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A8D4E04-277C-E511-B122-44A842CF0634.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/504DD935-277C-E511-BA6D-44A842CFC998.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/54680A0E-277C-E511-848E-001CC47D8D40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/58110343-297C-E511-937A-6C3BE5B5F218.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5A4BBBF0-277C-E511-A8EB-6C3BE5B5B108.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66B7B2FF-B87B-E511-A218-0025905A612C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6ADF5EE5-277C-E511-86CE-44A842CFD640.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CAC50ED-277C-E511-ADAF-6C3BE5B5F218.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/727FC5E3-297C-E511-ADE2-001CC4A6DC78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7801962C-297C-E511-8356-44A842CFC9BF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7CE265A7-677C-E511-9118-6C3BE5B52368.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8603AF55-B97B-E511-A8E6-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/90FB0DF4-277C-E511-8856-001F2908EC96.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92C8CF31-277C-E511-9AFE-B499BAAC02CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96D7D331-297C-E511-B14F-6C3BE5B5A4C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/98A5B331-297C-E511-A484-44A842CFD626.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AAC7A56C-277C-E511-817B-44A842CFC9E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B43CEDD7-277C-E511-ADA1-001F29082E7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BED51D00-B97B-E511-A105-002590596468.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BEFB1535-297C-E511-941E-6C3BE5B50180.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C0CDBA26-A07C-E511-8D44-009C02AB98A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C64E2400-B97B-E511-B76C-002590596468.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE80C842-297C-E511-B314-B499BAAC055E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4A100FE-277C-E511-B90C-6C3BE5B56498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D8E077FE-B87B-E511-9502-003048FFD796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA421D2A-297C-E511-BB32-44A842CFD5B1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2862000-B97B-E511-A6E0-00261894385D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6C9C0E0-277C-E511-8299-6C3BE5B50210.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4320E4A-277C-E511-9469-44A842CFC9E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F88AF8A3-B97B-E511-BF73-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE80F000-B97B-E511-B8D6-0025905A6082.root' ] );


secFiles.extend( [
               ] )

