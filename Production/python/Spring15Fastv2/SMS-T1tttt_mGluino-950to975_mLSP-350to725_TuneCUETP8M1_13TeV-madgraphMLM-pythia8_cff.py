import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/0A039C34-8E7F-E511-B3D5-02163E013027.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/0C2F2CB8-8D7F-E511-ABF4-00238BBD75D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/0C5FFAB9-8D7F-E511-8CBB-0CC47A6C1402.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/10C4C6C5-8D7F-E511-8639-0CC47A13D284.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/148488C1-8E7F-E511-9D2C-0025901D08D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/2086D3B9-8D7F-E511-BB25-0002C92A1024.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/229CD3BA-8D7F-E511-A9A1-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/243E3EBB-8D7F-E511-BEDA-90B11C282313.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/30C9FDC3-8D7F-E511-817F-0025904A9472.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/36A7AFF6-8D7F-E511-B7E4-02163E014F1F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3A42B8C2-8D7F-E511-A05C-0025904886E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3C3482C3-8D7F-E511-8E1A-002590E39D8A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4EA5C7BE-8D7F-E511-B810-0025901D08B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5E7C74BC-8D7F-E511-9D2B-002590488694.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5EB4D0BE-8D7F-E511-A84D-0025901D16AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/608EEC89-8E7F-E511-AEA7-02163E0168E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/629E2AB8-8D7F-E511-87DB-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6884189F-907F-E511-BC7F-02163E011458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6EC698B6-8D7F-E511-960E-00261894382A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/74FBE0BA-8D7F-E511-B5BE-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/80782BC4-8D7F-E511-9D9D-0025904897C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/80BC78BA-8D7F-E511-B462-0002C90F8030.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/86240ABB-8D7F-E511-AB5B-002590EFF972.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8C202BE8-8D7F-E511-BF18-0002C90F6792.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8C731EBB-8D7F-E511-B4B4-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8E09C1B7-8D7F-E511-A1FA-00238BBD7682.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/920E58BD-8D7F-E511-98F6-0CC47A13D416.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/9C09FFBB-8D7F-E511-AE2C-90B11C2CB121.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/9E90ACBC-8D7F-E511-9D78-0025901D0946.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A26107C4-8D7F-E511-8A7B-0025904A9430.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/AA9FA5BC-8D7F-E511-8257-0CC47A13D16A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/AC82A7C1-8D7F-E511-B17F-0025905A612C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BAEB2B84-8E7F-E511-822D-0CC47A13CEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/C4E672C0-8D7F-E511-8C78-24BE05C3DB61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/CC12DEBC-8D7F-E511-BE89-003048F5B6B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/CCA1E6BF-8E7F-E511-9255-02163E00E5B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/D8E82FC5-8D7F-E511-B809-0025901D16B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E2D3C95D-8E7F-E511-B1B5-02163E016922.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/ECCFAD5A-8E7F-E511-AD44-02163E014A45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F2C99FBE-8D7F-E511-B257-0025904AC2C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/FC600BC1-8D7F-E511-9D51-002590490020.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/FE082FC6-8D7F-E511-BDDB-00259048812E.root' ] );


secFiles.extend( [
               ] )

