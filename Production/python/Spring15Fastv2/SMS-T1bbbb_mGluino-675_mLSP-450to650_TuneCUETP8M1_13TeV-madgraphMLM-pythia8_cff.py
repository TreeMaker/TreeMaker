import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/043965BD-377C-E511-84ED-008CFA197D74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CBAE0F4-317C-E511-ACA5-00259055057C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1EE985C8-327C-E511-A8C8-0025904B2C5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/22575A73-377C-E511-97A5-00259055053A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/282C8068-327C-E511-9ED8-02163E00BBE5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2A2E0706-327C-E511-AA41-008CFA197B10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AA84E70-327C-E511-BEE6-02163E01324D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/426A30DD-377C-E511-A7B6-0025905487CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/444106BB-377C-E511-B558-008CFA197AEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48889E55-327C-E511-BD16-02163E00EAEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E4CBD86-367C-E511-BE7D-008CFA197AC4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/509A7B95-327C-E511-9BE6-02163E016143.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/546C33EE-377C-E511-B61C-008CFA010760.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5A226C54-327C-E511-8762-02163E00BF30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5AFB4006-327C-E511-8D61-008CFA110A98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6272205C-327C-E511-84A1-02163E00E9FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7862EC43-327C-E511-B42F-02163E010D31.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A2DC5FD-317C-E511-AAD4-008CFA1112F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E43D884-377C-E511-B5C9-008CFA197D74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80ED7045-327C-E511-9C2D-003048F0E7D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/823BE558-327C-E511-BC54-02163E00E849.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/84C242AE-327C-E511-B20C-02163E014BE1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A296A06-327C-E511-925D-008CFA1111C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E9281FA-317C-E511-B089-008CFA1979AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/98732D4A-327C-E511-850A-001E67579ED8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9ABCB68E-327C-E511-8C00-02163E015D9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A08B935F-327C-E511-A46B-02163E013F09.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A25330EE-377C-E511-9598-00259076082A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A8354A00-337C-E511-88CA-02163E00E5CF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B25DC918-327C-E511-96DD-02163E013112.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8B81340-327C-E511-A660-02163E013E43.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8C9EAED-377C-E511-8885-00259055053A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA0FEB87-327C-E511-9284-02163E00AC48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA67B99D-327C-E511-8A96-02163E00E74F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C24822C9-377C-E511-BBEB-008CFA197C10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C27B065D-327C-E511-9585-02163E013A82.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2D3A7A4-377C-E511-9273-008CFA197A60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D04B3FF6-317C-E511-8C1B-008CFA110C78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D614E1F8-317C-E511-9099-008CFA197928.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC6AF398-327C-E511-AD49-02163E010E5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC6CAB70-327C-E511-B3F5-008CFA197460.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE44E903-327C-E511-85F1-008CFA11118C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2A1A847-327C-E511-B8FA-02163E010CEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E41F0E94-327C-E511-B8BA-02163E010E14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E827A2F9-317C-E511-ABEF-008CFA1111EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4AB62A8-377C-E511-95F3-008CFA197AC4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6076778-327C-E511-A053-02163E013DBC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE6B8D7C-327C-E511-B933-02163E0150EC.root' ] );


secFiles.extend( [
               ] )

