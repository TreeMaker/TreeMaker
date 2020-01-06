import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/36FF70F1-8D11-EA11-9B19-B083FED43140.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/42253671-6711-EA11-8102-6C2B5990D1BF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/7EB915A5-6B10-EA11-A05D-7CD30AC03006.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/80FCA788-7F0F-EA11-B7A7-0025901AEDA4.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/8EF9506D-5514-EA11-A17E-AC1F6BAC7EAE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A658DB49-7C0F-EA11-9DB0-00269E95B17C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A6FD992E-750F-EA11-9F51-90E2BAD57CD0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/AAD8503C-9A0F-EA11-9E3B-0CC47A2B0744.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B65CF98E-DA11-EA11-B461-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CABE9B72-770F-EA11-A0E9-7CD30AD0A684.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E0BAA46B-770F-EA11-94DD-B496910A9820.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E249145A-740F-EA11-B1FE-B49691386CFC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E2FF6A90-9A0F-EA11-9281-F4E9D4AF7940.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/EE09AAFD-730F-EA11-B01A-1866DA8F75C0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1100_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F6A29011-BF14-EA11-A303-FA163E36F4A1.root',
] )
