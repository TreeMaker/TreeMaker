import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/029A96F3-3E13-EA11-B754-90B11C1E0717.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/083E85C2-0314-EA11-B1D4-0CC47AFF0270.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0A4B5CF7-3E13-EA11-A3A5-A0369FD2068C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0C1E29F0-3F13-EA11-A266-0CC47AD98BEA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/10CEE9A0-BE14-EA11-A476-FA163E690C19.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/1C9F4CAB-6113-EA11-8D39-20040FE9E278.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2AA0C20C-3F13-EA11-A3FE-00259094F2BF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2E16C71F-3F13-EA11-A1F7-90B11C0506C6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/501A64FD-3E13-EA11-A265-002590791DA2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/5C2C92F7-3E13-EA11-A250-B026283D9C80.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6A29B510-BF14-EA11-BA97-FA163E6D56AE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6E997D19-3F13-EA11-9F6B-24BE05C48801.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6ECFB1D1-3F13-EA11-9C29-A4BF011256F8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/707751D2-4013-EA11-A772-0025901D40A6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/7C117023-3F13-EA11-8137-3417EBE7446B.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/84200120-4013-EA11-A327-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/882A393A-3F13-EA11-87E6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9A11A761-5514-EA11-9E3C-0CC47A4D7674.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9C3F46DB-3F13-EA11-ADA3-00266CFFC9EC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/AC5755E0-5313-EA11-9748-008CFA56D770.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B4DA6579-5613-EA11-A7D6-008CFAC91E40.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B6365719-3F13-EA11-AB9E-3417EBE644B3.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D4395158-3F13-EA11-BDDC-0023AEEEB6FA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/DEA1836E-5A0B-EA11-8FBA-FA163E9A80BD.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/EA0C5F0C-3F13-EA11-8B95-C0BFC0E56836.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F2859F54-3F13-EA11-8324-002590D600E6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/70000/1CDE508B-E115-EA11-8E49-48FD8EE73AEF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/70000/42BD82E3-ED15-EA11-AA59-A0369FC5EE94.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/70000/6CC6A513-0D16-EA11-A2EE-003048F3112E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/70000/CE41B049-0D16-EA11-85BA-B496910A80E8.root',
] )
