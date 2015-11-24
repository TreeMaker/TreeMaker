import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/1000A780-EE88-E511-A185-0026189438F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/14D38093-F388-E511-A261-0CC47A4D7644.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/1667C194-F388-E511-861D-002618943875.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/1EE70799-F388-E511-81AC-0CC47A7452DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/247B1142-ED88-E511-B0EE-0CC47A4C8EB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/287562A2-ED88-E511-B5D0-0CC47A78A42E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/2E7A7583-EE88-E511-B265-003048FFCB84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/32923B97-F388-E511-BF43-0CC47A78A42E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/36A0B182-EE88-E511-ABDC-0CC47A4D7604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5267AA6B-E388-E511-BDC3-02163E013A43.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/52709882-EE88-E511-9C71-0CC47A4D766C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5AE45F99-F388-E511-8682-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5EA1C496-F388-E511-9E0D-0025905964C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/60323F98-F388-E511-A4FD-0CC47A78A340.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6A45428A-868E-E511-AC78-008CFA165F34.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/88D61F4E-868E-E511-823D-00259055045A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/94C22782-EE88-E511-827E-0CC47A78A456.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/94C4E382-EE88-E511-82C9-0CC47A4C8ECA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/9EAA6C87-EE88-E511-BE0A-003048FF9AA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/A62B5F84-EE88-E511-B9D2-0025905A48D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/AA640399-F388-E511-9CD4-0CC47A4D768E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/AC6B029E-868E-E511-9F09-008CFA197CCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B4424399-F388-E511-A21B-0CC47A78A4A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B4440B84-EE88-E511-8FFE-0CC47A4C8E56.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B8294084-EE88-E511-9EAB-0CC47A4D75F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/C03283AE-E388-E511-A729-02163E00E9FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/C6670983-EE88-E511-8D73-0CC47A4D7670.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/CAD91A98-8889-E511-9F69-0CC47A4D767A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/CE3B6D93-F388-E511-9892-0026189438EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/D0B5B192-ED88-E511-B29E-0CC47A78A414.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/D6363F97-8889-E511-A9C9-0CC47A78A468.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/D835BFC5-E388-E511-852E-02163E00EA75.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/DC53CA83-EE88-E511-AA0D-0CC47A4D761A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/DC76C48A-ED88-E511-BBFD-0025905964BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/DCF7809C-F388-E511-89AE-0CC47A4C8E66.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/E4CAAA97-F388-E511-B98C-003048FFCC2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/E6ADEA5F-ED88-E511-A263-0CC47A78A472.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/EAAA3205-868E-E511-A183-008CFA197B1C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/EECAD2D4-ED88-E511-AE52-0CC47A4D7634.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/F6309E41-ED88-E511-B95B-0025905A605E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/F8149B85-EE88-E511-8483-0025905A6056.root' ] );


secFiles.extend( [
               ] )

