import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/4E9A4E2A-AE56-7F49-B5DB-8B514BFDE1F3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/7E23F8C7-B5A4-6440-9A68-C1DBDA5081C3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/BE4316FD-1058-594D-AE2A-38361801343E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/C0870FF6-0C94-1C4F-A1E6-4BB018EC0525.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/C5FCACD9-09B9-6D4F-9252-807432042722.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/2CFE4ACA-6111-244F-9DB5-00E70840FDE4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/DDCE5BA9-A56E-2D4D-8A39-98AB2AAC4448.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0232507A-066C-9842-BF14-65D22EEA24D4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/15FDD8B6-9937-7B45-8627-E0A45BFF6A6A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/1929CA81-86BD-5E41-BA7E-C9E27708B78B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/101EED42-0215-F64C-880F-57A78F910397.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/28D24EFF-9072-A245-878B-F7B6A56EAE94.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/2BB7BEB2-EDE6-F14B-9891-72B670A06300.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/2ED889E8-2171-3E42-B21B-A80BD6C40180.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/393906BD-3393-8F4F-8163-3D4B354887F4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/46A33588-0878-DE4B-8E35-D3006F3ECBCB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/72607E40-1C44-1148-BB55-2ED2E333071C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/76FDBDB5-65C1-9D48-BD41-B1B6AEEDD16A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8E4A8B09-D690-284C-88D3-62E61D619E13.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/C83B87EB-66E1-A447-BDB1-56B12A6EB8BA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/CB60051E-A751-2E44-B5CC-57456CE15CAD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/CC7F5173-27E5-DF4A-87DF-A2ECE881A2AA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/CF267996-6005-C142-8B6A-A55EF7FBC285.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/D6352560-DCAD-384E-BE07-CFEBD0C225D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/ED063FE6-6AEF-694F-A870-6955902C8B9C.root',
] )
