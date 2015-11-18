import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/02E21BD6-EB83-E511-9E7D-02163E01510A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/062775B1-BE83-E511-9D54-0025901D08BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0E315D80-8C83-E511-AA63-90B11C2AB44B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/128969FF-EA83-E511-81BC-02163E01425C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1440883F-F683-E511-93B9-02163E016B98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/16C5E0B1-EA83-E511-B031-02163E014D34.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/18E15B14-9583-E511-AD67-008CFA1CB740.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1A4B729A-BE83-E511-9AE9-90B11C2801E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C599CBE-8D83-E511-8C38-008CFA064760.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/28614CCA-EA83-E511-BD83-02163E016B1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2ABDED55-F683-E511-8881-02163E013F5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/34736A74-8C83-E511-84FD-0CC47A13CD9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/34CB622A-EA83-E511-A78F-02163E0150EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3606BF61-F683-E511-9040-02163E013C7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/36395C34-EA83-E511-9BAB-02163E0147C7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3656C634-EA83-E511-BAAE-02163E014EC5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/409285A6-BE83-E511-9B64-0025901D08E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4C93F49D-BE83-E511-97C2-003048F5ADEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5097F214-8883-E511-8453-008CFA14F814.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/529E1B79-E783-E511-89E8-008CFA11134C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5EBABCE8-EA83-E511-B1B3-02163E016BC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/664FB68D-BE83-E511-BC54-0CC47A6C1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/74239013-9683-E511-977C-549F35AF4517.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/78252993-EA83-E511-933B-02163E016B28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7AE29D86-8C83-E511-96C1-00238B64E02A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8A271172-F683-E511-B275-02163E0115E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8E9CDF4F-EA83-E511-8410-02163E014D90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/90B5FE29-9F83-E511-BA6C-008CFA197FAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/928FB974-9F83-E511-B004-008CFA05EA2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/96EDDF8A-F683-E511-AF1A-02163E012F2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/98B5CE5F-8C83-E511-9E73-A4BADB38E25B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A2183D98-BE83-E511-B6D7-A4BADB38FD44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AAD685A8-EA83-E511-85C2-02163E016BE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B05736B0-8883-E511-B250-549F35AF44AF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BE8A3E86-BE83-E511-AB4A-00238BBD7682.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C0813542-8B83-E511-8F30-002590E3A004.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C0A62D2A-9F83-E511-ADD0-008CFA1CBA20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C295E08E-8C83-E511-8E5B-0CC47A6C1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C6848677-F683-E511-B577-02163E016B8A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E8945C8E-9B83-E511-930E-A0369F7FC210.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE723E2C-F683-E511-86BC-02163E014D90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F8577494-BE83-E511-91B7-00238BCE4634.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F8C8522B-F683-E511-816C-02163E0152CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FE4DB19C-BE83-E511-8FF7-0025904A8EC8.root' ] );


secFiles.extend( [
               ] )

