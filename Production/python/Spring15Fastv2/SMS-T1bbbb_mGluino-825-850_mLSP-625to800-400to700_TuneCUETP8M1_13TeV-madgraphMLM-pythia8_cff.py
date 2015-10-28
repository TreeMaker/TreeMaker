import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/04CD8CF8-877B-E511-B60F-00259074AEC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/06FA6074-867B-E511-8680-00259073E3DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0C20547D-867B-E511-8E54-20CF305616EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CA05C95-867B-E511-8E58-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0E1CB046-867B-E511-A520-00259073E4CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0EA302C2-867B-E511-8D96-003048FFCB84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/109D96C3-867B-E511-B17C-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CFCCBC3-867B-E511-9DFF-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2ACA4046-867B-E511-B706-00259073E44E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CAD1AFE-877B-E511-A615-20CF305616EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/30B8E9E3-877B-E511-BE57-00259073E44E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38A0CAC3-867B-E511-993C-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/42134946-867B-E511-B0B7-20CF305B051B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/44164E46-867B-E511-971C-002590747E40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A06EC43-867B-E511-AFD1-00259074AEC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4AC1A146-867B-E511-9431-00259073E45E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C03EBB3-867B-E511-B2D0-00259073E44C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/522701C4-867B-E511-92B5-002590593878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5451B6E6-877B-E511-A0FE-00259073E45E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5C7D6442-867B-E511-AD90-0CC47A4DECD4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7617E99A-867B-E511-B89C-00259073E516.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82843F7B-867B-E511-A8F3-00259073E32A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CF1DFF8-877B-E511-A04B-00259073E51A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/963BC2BE-867B-E511-927D-0026189438E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96B100C4-867B-E511-A97E-002590593878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9C0FC9A1-867B-E511-8B81-00259073E3AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A483AD50-867B-E511-A7B9-0CC47A4D9A2E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A8F1AE50-867B-E511-8598-0025905822B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B0ECB794-867B-E511-97E9-00259073E4D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC66B4C1-867B-E511-978E-0025905938A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC7F196C-867B-E511-A572-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C0A9C0BE-867B-E511-A57A-002618943915.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6203B81-867B-E511-8A9D-20CF3027A630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2D8C455-867B-E511-924E-20CF3027A577.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4C06084-867B-E511-A837-00259073E4CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA4BD646-867B-E511-B01A-20CF3027A5E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EAD5DAC1-867B-E511-84DA-003048FFD756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECBAC2AC-867B-E511-B2C2-00259073E514.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F402204B-867B-E511-B614-00259073E4FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F63544C4-867B-E511-BED6-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8D8E285-867B-E511-A58A-00259074AE40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA76D2FE-877B-E511-9024-00259073E4CE.root' ] );


secFiles.extend( [
               ] )

