import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/06CB730E-CF82-E511-BEA9-02163E00EB30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/12B4F1FC-FE82-E511-9906-02163E013CD2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/1620A6D2-F780-E511-B56C-001E67A406E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/166B1AA1-8C81-E511-9475-0025904AC2CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/184B1557-D082-E511-A77E-02163E010D22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/22117780-CF82-E511-84BE-02163E014831.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3E59C992-F980-E511-9F38-003048947DFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/466C8509-8D81-E511-8DC1-003048344C12.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4C784300-CF82-E511-8D7C-02163E014BB2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/54BB8AF7-8C81-E511-8533-1C6A7A263003.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/56E3103D-8D81-E511-BE49-002590491B22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5A67AA1D-D082-E511-BE82-0025903D1C32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5ADBE715-D182-E511-A3ED-02163E0168C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5CEB9E05-8D81-E511-BA4E-90E2BA726B5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/602CECCE-D082-E511-A8A3-02163E013B1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/60F19AD3-D082-E511-975B-02163E014CA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6E8488E7-0781-E511-9DFA-001517FB21CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/74F8B651-D082-E511-A130-02163E011411.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/7CD247E2-D182-E511-987F-02163E011756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/7EED5CA1-8C81-E511-B865-F8C288DA8479.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/82D2100C-CF82-E511-B250-02163E013F75.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/860167E9-8C81-E511-A14E-0CC47A6C1058.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/86CA2FF3-8C81-E511-9A52-003048F5B6B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/905DFEDC-8C81-E511-AC1F-1C6A7A26BF83.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/90E86A74-0183-E511-B111-02163E011544.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/94CC1C2D-8D81-E511-8A74-1C6A7A263003.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/94F7B1D2-D082-E511-9D53-02163E0151EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/964767FC-8C81-E511-9E78-0CC47A13D416.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/986956E2-CE82-E511-8747-02163E013573.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/B4202CF8-CE82-E511-84B8-02163E013C5E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BC609480-8D81-E511-9C48-F8C288DA7E2D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/C68F8AE8-8C81-E511-BCE4-003048344A88.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/D0080992-D182-E511-B142-02163E016BEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/D809753F-8D81-E511-8A4E-90B11C27F101.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/DC1F4154-FF82-E511-B035-02163E012A36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E07C4D37-8D81-E511-ACF2-003048F5ADF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E0FEA437-D082-E511-A1EB-02163E013048.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E2CBA093-8C81-E511-B710-F8C28867177B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E85162FA-8C81-E511-892A-1C6A7A26C347.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F09E86A2-0083-E511-8759-02163E0135AF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F20633C4-F780-E511-908A-90B11C094A7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F6B25D74-CF82-E511-94D0-02163E0161A7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F6C8151E-D082-E511-B1A4-02163E013A08.root' ] );


secFiles.extend( [
               ] )

