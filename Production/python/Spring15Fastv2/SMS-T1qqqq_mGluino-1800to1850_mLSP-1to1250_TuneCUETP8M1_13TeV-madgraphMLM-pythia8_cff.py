import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/084258BC-8D8B-E511-B46B-00259073E526.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0C50BA8C-6F8D-E511-930C-02163E013EA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1278BABA-8D8B-E511-BB70-002590747D94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/142DD7B9-8D8B-E511-A7DE-0025907B4F44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1ACA7640-B08B-E511-99EA-90B11C0BB9FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/220585BC-8D8B-E511-81F3-20CF3027A62C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2A5757B8-8D8B-E511-965E-0025907B4F64.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2ADBC8B8-8D8B-E511-B639-00259073E3C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/30305DBA-8D8B-E511-826C-00259073E4B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/308924BD-8D8B-E511-BE29-20CF305616F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/30BF46BA-8D8B-E511-9D6C-00259073E34C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3480B60E-968B-E511-83AA-C4346BC8C638.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3872FFB9-8D8B-E511-B5E6-00259073E3A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4A1F83B2-6E8D-E511-B97A-02163E014E96.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5217E857-B18B-E511-8397-90B11C0BB9FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/562F7A1F-968B-E511-9774-6CC2173BBD40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5ADB7230-968B-E511-B229-008CFA051DEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5E566C25-B08B-E511-A4C5-001EC94BF999.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/604761C4-8D8B-E511-9F8C-A01D48EE8354.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62DA401F-968B-E511-BBDB-00266CFFBE68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/66438220-968B-E511-B7EA-00266CFFC9C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/70FFE2BB-8D8B-E511-82C6-00259073E4C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/72C4FC27-968B-E511-A946-00266CFEFF04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/785180BA-8D8B-E511-A8D9-00259073E506.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7C32211D-968B-E511-BAB4-C4346BC7AAE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/82C7052A-968B-E511-8563-6CC2173BC350.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8A03355A-B18B-E511-AF44-549F3525DFE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8A07011E-968B-E511-9FF9-C4346BC076D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8A1FFBC3-8D8B-E511-AB29-A01D48EE8354.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/986D71C3-6E8D-E511-9DCC-02163E011626.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/98DB1CBA-8D8B-E511-9B9C-00259073E41E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9CA8FEC0-8D8B-E511-BB6A-A01D48EE82C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A23AB8F8-BD8B-E511-9F23-782BCB53A0C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A23B32BD-8D8B-E511-BD18-00259073E466.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A2EF001E-968B-E511-BBC7-C4346BC076D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A6580ABA-8D8B-E511-A402-00259073E382.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/ACF94F1F-968B-E511-884E-00266CFFBF38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BA43E621-968B-E511-ACFA-00266CFFCAC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C2F3E8BA-8D8B-E511-B65C-00259073E37C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CAE6BBBA-8D8B-E511-8574-00259073E3E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D213B925-968B-E511-902B-00266CFFCD50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D2AC8AB9-8D8B-E511-AF2E-002590D0AFB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DA9630BD-8D8B-E511-BCA6-00259073E466.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DE6E2222-B58B-E511-AB66-74867AF198F1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E0660EB9-8D8B-E511-B87C-0025907B4F14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E21E4C1D-968B-E511-9422-6CC2173BC120.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E6DA5828-968B-E511-B33B-6CC2173BC990.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EA6FD3B8-8D8B-E511-9F1E-00259073E456.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE2B4AB9-8D8B-E511-836B-0025907B4F44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F467B4FF-958B-E511-9CA9-0CC47A4DEED2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FC1F7A1F-968B-E511-8269-6CC2173BBD40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FE4CAF9F-6E8D-E511-B221-02163E011570.root' ] );


secFiles.extend( [
               ] )

