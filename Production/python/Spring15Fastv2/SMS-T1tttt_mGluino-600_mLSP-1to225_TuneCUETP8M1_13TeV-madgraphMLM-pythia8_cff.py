import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/0292ABEF-E09E-E511-907E-003048FFCBA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/08FB571F-E19E-E511-8059-008CFA110C64.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/0A63A9F5-E09E-E511-B8DB-00259056F35A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/12014324-E19E-E511-882D-00266CFFA240.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/12D566F0-E09E-E511-B50C-901B0E5427AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/14F91228-E19E-E511-B8DC-008CFA1113F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/287577F2-E09E-E511-A476-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/2C750AF2-E09E-E511-AB07-0025905964BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/309A7FEF-E09E-E511-88A1-0CC47A7452D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/368A30F3-E09E-E511-B654-008CFA197D0C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/3CA8D7C7-E19E-E511-822B-0CC47A4C8F2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/441F0E22-E19E-E511-96C9-008CFA197AF4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/52AC7BF6-E09E-E511-B747-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/569E65C5-E19E-E511-AB98-008CFA111130.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5CCF92F3-E09E-E511-B570-00259055045A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5EA3B5F0-E09E-E511-B0DB-0025905A613C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6056C2ED-E09E-E511-BAD3-0CC47A4D75F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6C08A1F1-E09E-E511-9EC5-0025905A6082.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/7289A529-E19E-E511-AF24-008CFA1113A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/741B58F2-E09E-E511-9B3C-0025905A609A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/74A3751A-E19E-E511-B9C4-008CFA1974DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/76302E1E-E19E-E511-A330-008CFA110C74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/7A2A80C3-E19E-E511-BE29-0025905A60CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/7E6C5A21-E19E-E511-ACC7-008CFA19746C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/7EC197EE-E09E-E511-B4BA-0CC47A4D7618.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/86D5091A-E19E-E511-AA83-008CFA197488.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/884B38F6-E09E-E511-9051-0025905938A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/8EDF500C-E19E-E511-A576-02163E016BD2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/986803EF-E09E-E511-BCBC-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/9E2A62F5-E09E-E511-A5E3-008CFA111130.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/A0467523-E19E-E511-8E3A-008CFA11131C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/A85B1E0D-E19E-E511-BDB4-008CFA111244.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/A872A221-E19E-E511-8831-008CFA197C1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/AAE11BF1-E09E-E511-90FA-0025905B855C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/AC1BC1EC-E09E-E511-AE3A-0CC47A4D75F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/AE28BF20-E19E-E511-8E82-008CFA111148.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B01268F0-E09E-E511-8FFC-0025905A60CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B40B83F6-E09E-E511-AB94-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/D8BCB228-E19E-E511-80F7-008CFA111154.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/DE0C7100-E19E-E511-AEDE-002590552094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/E4AA6AEF-E09E-E511-80C4-0CC47A4C8E1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/E84CEAC8-E19E-E511-B548-0025905A48C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/EC96FCF5-E09E-E511-ADF0-0025905822B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/FC3E14F9-E09E-E511-A261-008CFA1974DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/FE6150F2-E09E-E511-BFF7-0CC47A4D7698.root' ] );


secFiles.extend( [
               ] )

