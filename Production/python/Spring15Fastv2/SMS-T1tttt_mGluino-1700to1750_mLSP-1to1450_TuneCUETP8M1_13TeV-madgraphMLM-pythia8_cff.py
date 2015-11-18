import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0628CF26-0180-E511-8FA9-0025905B8606.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/069ECEA1-0180-E511-88DC-02163E01690F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0AC1283A-0180-E511-99F1-0025905B85D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0EEFE6EE-0180-E511-8AD4-00261894385A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1090F5EC-0180-E511-8E82-0025905B8592.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/14D0E6EE-0180-E511-8432-00261894385A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/18269866-0180-E511-8684-0025905A6068.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1AA04326-0180-E511-A17E-0025905A60CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C220531-0180-E511-A5B3-0025905A60DE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1E597C26-0180-E511-A751-00261894390C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/20EE39EA-0180-E511-8DF5-0026189438F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4AB3B840-0180-E511-8BD7-002590A2BCBC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4AD7DFEF-0180-E511-84B1-003048FFD7D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4C32C026-0180-E511-A45B-002618FDA279.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4CBF8D2B-0180-E511-BAFB-0025905B861C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/568D4A28-0180-E511-A238-00261894397A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/56B4BF27-0180-E511-A850-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5AD0EF27-0180-E511-B328-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62282F38-0180-E511-B804-002590490020.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62C6CD28-0180-E511-B558-0025905B8568.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62E78BF3-0180-E511-B1E1-0025905938A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/64B016F3-0180-E511-8BC9-0025905B8572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/64C4995C-0180-E511-8319-C81F66B7910D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6ADE7326-0180-E511-8D64-0025905A6066.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6C33BC27-0180-E511-89D2-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7A634943-0180-E511-9742-02163E00B48D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7E1E3827-0180-E511-BEB6-0026189438A7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/82A7F7ED-0180-E511-944B-00261894392F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/86B89B26-0180-E511-94BE-D4AE527F338C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8C47842B-0180-E511-A00B-0025905B861C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8E2F7C26-0180-E511-9737-00261894390C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/927A5D6A-B57F-E511-9AE7-90B11C2AAEEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9845B6CA-0280-E511-B787-02163E01159D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9E1FAEEE-0180-E511-B550-003048FFCC2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A4297440-0280-E511-8B19-02163E01152F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AA2D2329-0180-E511-9F19-0025905A611C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AED54A28-0180-E511-8907-00261894397A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B4538226-0180-E511-90A8-00261894390C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B499E027-0180-E511-9F94-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BA610A26-0180-E511-9F11-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BC1ABC27-0180-E511-81BD-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BC8B2A2F-0180-E511-A651-0025900E3508.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C4CD8F25-0180-E511-B59D-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C4E38B2C-0180-E511-819F-0025905B85AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CA6D2535-0180-E511-8950-002590EFF972.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DA960FEE-0180-E511-BC06-002618943940.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DE0019EF-0180-E511-8EC5-0026189438C9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E2E57635-0180-E511-9445-003048344C68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E6037CEF-0180-E511-A2DE-0025905B858E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EA0249ED-0180-E511-A44A-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE11B127-0180-E511-958F-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F6001BEE-0180-E511-8F71-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F68FDB67-0180-E511-B7F8-02163E00F778.root' ] );


secFiles.extend( [
               ] )

