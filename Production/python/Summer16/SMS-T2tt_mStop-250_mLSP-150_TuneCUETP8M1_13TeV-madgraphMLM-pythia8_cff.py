import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0418A809-24D5-E611-86D2-1866DAEA7EA8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/04769162-FCD4-E611-B3E8-90B11C0BD86E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/04AE5048-24D5-E611-83B3-002590A80E08.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0E613251-8CD4-E611-850A-44A842434739.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/14D9DB4A-24D5-E611-9E35-0090FAA575D0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/16049113-24D5-E611-98B0-001E67DDC2CC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/486300F0-23D5-E611-9A3D-FA163ECC4FF6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/542EC751-24D5-E611-97AC-0CC47A7DFDFA.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/5851F620-B9D4-E611-AD32-0CC47A1E0C70.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/5E4DE2A3-24D5-E611-9499-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/5ECAEBE6-23D5-E611-8677-0CC47AD98BC2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/64C420DA-23D5-E611-BEEC-0025905A60C6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6A9EB4F2-23D5-E611-AB0E-008CFA110AA8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/88308B0C-24D5-E611-A871-002590E7D5AE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/9A729ED7-23D5-E611-B90F-0025905A60CE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AC70C72F-24D5-E611-A796-20CF305616FF.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B29F2025-74D4-E611-BFA5-02163E00C0CD.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D2800937-B9D4-E611-A633-B083FED16468.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E41B55CE-23D5-E611-8125-0CC47A57D086.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E4875412-24D5-E611-94CE-20CF3027A5CC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E845EF14-24D5-E611-91BF-001E673476AA.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F017CFF6-74D4-E611-84A1-1C6A7A26C7B3.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F6F45461-1ED5-E611-9F27-FA163E5A38C2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F874263D-72D4-E611-A2BE-A0369F30FFD2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/284D2F85-50D4-E611-9F60-FA163EBA4FEC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/380411C4-4FD4-E611-BD9F-B083FECFEF7D.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A0E29DB-50D4-E611-BD2D-002590E7D7DE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8AF6E3C5-4FD4-E611-88A9-E0071B749C40.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AAEECCD8-4FD4-E611-8864-008CFA111310.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AE1779F5-4FD4-E611-A1D5-A4BF0101DB3E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B6A32154-50D4-E611-B54D-00259075D62E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BA81A3C8-4FD4-E611-B2E3-20CF3027A5EB.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C0065B2E-52D4-E611-925B-02163E0148EE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DCE5F1D0-4FD4-E611-BFE3-0CC47AD9908C.root',
] )
