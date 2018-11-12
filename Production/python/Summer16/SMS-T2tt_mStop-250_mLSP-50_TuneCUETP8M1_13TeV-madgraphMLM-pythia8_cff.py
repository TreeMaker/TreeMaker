import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/38EF186F-8ED4-E611-AC60-0025901D08B0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3E2FAE88-CBD4-E611-9B5C-0CC47A4D768E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E1187F7-90D4-E611-B866-5065F3817221.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6A1E2920-CBD4-E611-80E9-842B2B173478.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/74B1F420-CBD4-E611-9D2E-FA163E2C9EAC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/80A75C20-CBD4-E611-A3CD-001E67348055.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8A491164-95D4-E611-8681-1866DAEB5C94.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/904BFF00-CBD4-E611-A76D-FA163E12AAD8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/90F33608-CBD4-E611-8408-002590D9D976.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/943F1E9D-95D4-E611-914B-0CC47A4D7666.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C6285C3-91D4-E611-AB70-001E67A3EC05.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A2D84EF9-8ED4-E611-9D80-001C23C0B781.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AC0E5C0B-CBD4-E611-872A-0CC47AD98D6E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AC5CAE3A-97D4-E611-99A3-0CC47A78A3EC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B8ACF202-93D4-E611-8FB5-0CC47A7C3458.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE5EF184-9BD4-E611-84CB-0CC47A4D75F4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D8197338-87D4-E611-906E-5065F381E251.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA0CE09B-CBD4-E611-BAAB-0025905B858A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0E9C528-94D4-E611-810D-0CC47A4D7664.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E4843C2C-CBD4-E611-9FF3-A4BF0101DE18.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F8C4190F-CBD4-E611-A2DD-008CFA197D48.root',
] )
