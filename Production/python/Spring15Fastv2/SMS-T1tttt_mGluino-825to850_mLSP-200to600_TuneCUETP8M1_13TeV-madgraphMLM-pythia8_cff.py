import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0018238F-B07F-E511-8D83-0026189438C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/08F9A492-B07F-E511-9B08-0025905B8590.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2249F393-B07F-E511-A02D-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2E7AD58D-B07F-E511-96F4-002618943880.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2ECFDC08-B17F-E511-A07F-0025904A93AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3A926598-B07F-E511-ACED-0025905A608A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/464C5C44-B17F-E511-8E3C-FA163E0FB63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4A4B7998-B07F-E511-A7FC-0025905A606A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4C86AC45-B17F-E511-A2B0-FA163EA3B0B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5052EB45-B17F-E511-B4A3-FA163EA3B0B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/549F4301-B17F-E511-B9C2-0CC47A13D2A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/68A06192-B07F-E511-9875-0025905964BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6C57A047-B17F-E511-A955-FA163E5FAF88.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/701B599A-B07F-E511-8F6C-0025905A6088.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/72E3EC9B-B07F-E511-A286-0025901AFEA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/768DBB97-B07F-E511-8009-0CC47A13D16A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7892DC74-B07F-E511-B612-02163E016A40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C275A9A-B07F-E511-A107-0025905A6088.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7E60E0B0-B07F-E511-AD99-E41D2D08E0D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8275F3A2-B07F-E511-ACBA-0025904A91F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/84121D9E-B07F-E511-BFE0-90B11C2ACF20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/886C30AA-B07F-E511-B6EC-0025907DC9C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8E4E7690-B07F-E511-9355-0025905964C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/96D75844-B17F-E511-8036-FA163E0FB63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A2890693-B07F-E511-9BF5-0025905A48F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B02BB39A-B07F-E511-BC61-90B11C27F383.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B0496093-B07F-E511-A74D-0025905AA9F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B05C518F-B07F-E511-B9C4-00261894390C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B0D3DF47-B17F-E511-B74C-FA163E19FFD9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BA54D29D-B07F-E511-99DB-0025901D08BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BC3D4C47-B17F-E511-8BF9-FA163E552E17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C03EAE90-B07F-E511-B99E-002618943949.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C223599A-B07F-E511-8000-0025905A6088.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C6757091-B07F-E511-87EA-0025905A60BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CC4A769C-B07F-E511-9EAD-0025901D0C4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CCF05A9E-B07F-E511-A6EB-0025905938A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D26CCE48-B17F-E511-89FA-FA163EEF8E08.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E6459706-B17F-E511-B9F6-90B11C27E141.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E6B00A9C-B07F-E511-91E5-0025900B5648.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E6D8CC93-B07F-E511-8B4E-0CC47A13CCEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F00CFE41-B17F-E511-B383-FA163E7E2FF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F89FB7A2-B07F-E511-A656-0025907DC9DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FAC50893-B07F-E511-9C89-0025905AA9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FAD14397-B07F-E511-9EED-003048FFD71E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FEE0708E-B07F-E511-905B-002618943922.root' ] );


secFiles.extend( [
               ] )

