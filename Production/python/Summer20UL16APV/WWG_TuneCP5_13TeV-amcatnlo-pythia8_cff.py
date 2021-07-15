import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/03037F85-399B-5C48-BDDF-58A7E45DF5F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/04935323-9240-0849-989E-9C633D0BE173.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/0839E59A-6494-3E41-9FC5-E935764A73BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/0905EB27-DC61-DD45-A49A-6E39AF777930.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/15D02538-420E-5C4E-A6B2-22AB6277B6D9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/20D2E811-30F4-164C-9969-42C44E0D40E6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/37F33021-B831-9A42-AC31-3CA16163F26E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/4005C51C-7C78-214D-B8ED-4C3E2C06C346.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/49D20BBC-2E5A-9A4A-B47A-70246DBC03D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/4C833B78-736E-DB40-BE00-2D715B44A929.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/5370CF79-87AD-3B41-A1F1-2FDB3447C49F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/59A290E3-2934-884D-8DC6-AEE064C294EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/5E1ADDEC-BA83-9649-B550-E0228B18A7D9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/78F5047C-1D5E-5C4F-B915-12A105FFCCEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/7A0573E7-72AF-E249-818A-189F5B6C6B57.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/7F766E14-4ABF-A448-90FA-A23E2056D8F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/87FAD17B-80D6-D647-85F2-4D7CF07843E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/88259FB1-2201-EE40-B2FD-42E1EF55A123.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/8D622EA7-708A-EC4B-B52F-93EA10AC3E39.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/91100EAF-7346-7841-960C-7265EDCB8836.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/958651DB-CF2E-CA45-BF59-5D72D8F6902D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/9D474CF3-0052-1C4C-AEF3-13C325DC5126.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/A1F78BBD-FF4C-5149-B6DB-5641458FC19B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/ACEA6EC2-1019-6E4F-A5AF-0ABC4257724D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/130000/FDCE97E7-C1B2-F449-893F-BD0CEBF4609B.root',
] )
