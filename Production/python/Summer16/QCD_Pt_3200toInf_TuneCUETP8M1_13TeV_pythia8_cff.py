import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/00012742-23BC-E611-BF02-1C6A7A21AE41.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/14512DF0-23BC-E611-92D5-001C23C0DE8E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/2234F6A5-69BB-E611-8B92-0CC47A537688.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/2487978F-F1BC-E611-825D-90B11C056AAD.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/3E94EBDB-F7BC-E611-B2E8-0CC47AD99050.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/4E392F2E-F3BC-E611-B288-549F3525BF58.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/4E589DCF-ECBC-E611-BD00-5065F3820341.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/4EFA7A9A-2ABC-E611-89B4-0CC47A7C35A4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/562F9F06-2BBC-E611-A265-FA163EDFD4EE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/7024C7A6-30BC-E611-9AC1-0CC47A0AD668.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/7C03C49B-21BC-E611-9976-001E67DFF61D.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/8A3E7B01-50BE-E611-8887-0CC47A78A4A6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/8CFE0BA9-1BBC-E611-B1D4-24BE05CEBD61.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/8EE545AB-56BB-E611-AF54-001E67457E7C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/90144AC2-5FBB-E611-8514-001E674FB24D.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/923073E9-03BD-E611-A6EB-0025905B8606.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/A0B9C63F-2DBC-E611-819A-0025905B8568.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/B8E530FE-70BB-E611-A135-001E67586A2F.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/D09AA7D1-3EBD-E611-9FDF-FA163E053F1E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/D61FD459-2DBC-E611-8183-FA163E0D96B1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/60000/D64A1A25-3CBC-E611-A827-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/2A20B297-59BB-E611-A192-001E674FB2D4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/80000/C41F73F0-DBBC-E611-8BE9-0242AC130008.root',
] )
