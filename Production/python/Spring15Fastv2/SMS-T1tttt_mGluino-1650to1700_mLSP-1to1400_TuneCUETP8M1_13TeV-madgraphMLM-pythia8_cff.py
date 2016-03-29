import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/029D5362-708A-E511-98CD-02163E00BE2F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/08CF646E-0C85-E511-948B-001E675A690A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0A071F3A-978A-E511-BEF3-02163E0148C5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1A2FF012-978A-E511-B926-02163E00E736.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/22EB5516-978A-E511-B3AC-02163E01523E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/30BEE2D3-E484-E511-A22A-02163E0168EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/327F4D06-988A-E511-BFF1-02163E013F0B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3695BDA3-708A-E511-A981-02163E00C7A7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/36A6022A-718A-E511-AE9F-02163E013E39.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/38533A99-708A-E511-BA09-02163E012E4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3C7F20E3-978A-E511-8AE3-02163E011CCE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/40CA9C5D-708A-E511-83E3-02163E013562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/441C20C1-D484-E511-9F07-02163E012F06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/50DC64FC-968A-E511-B4F6-02163E012E4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5473AFA7-1085-E511-9B7F-02163E0114F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/56D740BA-D484-E511-985B-02163E010FB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/64C97011-988A-E511-A5E9-02163E00F490.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6C00C441-718A-E511-A965-02163E015F9F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6C398598-E484-E511-B76A-02163E01531E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6C9E6D54-718A-E511-9FDF-02163E00F35F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6E510353-3285-E511-A51C-02163E013BD6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/72CF29B2-708A-E511-A4DE-02163E012906.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/745CE616-988A-E511-AC43-02163E013E7C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7CCA1B48-988A-E511-8B13-02163E00E63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7CD7AF28-718A-E511-A50E-02163E011B4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/86B65252-708A-E511-9C6C-02163E00BE0F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8C80D8F2-978A-E511-AFC2-02163E012E49.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9637632D-718A-E511-A464-02163E00CE5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/96B17CEB-D484-E511-A21E-02163E016A55.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9C940F28-718A-E511-A766-02163E01687B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9E18B692-E484-E511-849D-02163E010BF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A840FDE0-1285-E511-BFE8-003048F0E7BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B0010AE9-708A-E511-9DB2-02163E013BE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B07D65B7-E484-E511-AD07-02163E016712.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B29F7839-1285-E511-AA2F-02163E00F4E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B62C0BDF-D584-E511-BBAD-02163E013F00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B6E82CAD-1085-E511-9D55-02163E012EC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B89CD192-708A-E511-BADA-02163E00E805.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B8CD29AA-708A-E511-AE55-02163E00CEB5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C0F899C0-708A-E511-9014-02163E010C25.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C2BFD2E2-1085-E511-BD2D-02163E015FB9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D03BB999-E484-E511-B716-02163E00F51E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D6FE01BB-1085-E511-98F1-02163E016BB2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D84D9CED-1085-E511-8E04-02163E00EBA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DA0ABA55-718A-E511-AD89-02163E00E9EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DA7DF92F-718A-E511-961B-02163E010E52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DCC317C0-E484-E511-99B1-02163E0167F3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E0460921-978A-E511-9D18-02163E00F721.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E4901F29-718A-E511-A206-02163E015C72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E6707645-D684-E511-8140-02163E016A8E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/ECC11630-718A-E511-9F51-02163E012E5D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/EEDA6C07-D484-E511-AFC5-02163E013F00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F67BAC2D-978A-E511-9788-02163E00ACC0.root' ] );


secFiles.extend( [
               ] )

