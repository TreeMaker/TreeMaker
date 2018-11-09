import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1C24F709-15D5-E611-815D-0CC47A0AD63E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/20C93F5F-C4D4-E611-9E86-0025905A611E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2E572357-15D5-E611-9E4D-0CC47AD98F74.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3E9111E5-B8D4-E611-928C-1866DAEA79A4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/469A4F25-15D5-E611-AB12-B083FED14CE0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4804FFA3-E4D4-E611-9D3B-02163E013F49.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4C55B83F-A9D4-E611-A465-0025905A6066.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5EA02855-16D5-E611-87C9-FA163ED27112.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6E48659F-AAD4-E611-AC58-0025905B85C6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8068CECA-15D5-E611-B422-008CFA197448.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/82B3A109-ADD4-E611-93DC-0CC47A745250.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/ACDD4FDF-B1D4-E611-A99A-0CC47A4C8EE2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B24E6F6C-15D5-E611-9203-0025905A48B2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2DBBE1B-16D5-E611-A663-A4BF0102A5BD.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2E9A753-E2D4-E611-9B03-02163E00E5B0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B41A6E54-15D5-E611-9618-FA163E3B9B91.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B4B381B8-AFD4-E611-85C1-0CC47A4C8E38.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B6FFE27B-CED4-E611-A990-0CC47A4D76D0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE449125-15D5-E611-A070-24BE05CE4D91.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C42CDD1A-B4D4-E611-A01E-0CC47A13CFC0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4E73E69-15D5-E611-A543-0025905B8580.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0BE3299-AAD4-E611-943C-0CC47A4D7668.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2AD919AF-85D4-E611-B678-0025905A60B6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/787160A5-ADD4-E611-A843-0CC47A7C34A6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C241EED9-ADD4-E611-BB9F-0025905A60EE.root',
] )
