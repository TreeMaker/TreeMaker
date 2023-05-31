import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/CE9D0EF7-C2A8-6543-AB6E-7F775D3659B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/0D1FBB54-ADFD-5F4C-989A-D7AFA29CC66C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/11DEC039-6B7F-E14B-9607-D2973A865BD1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/1522A5C4-2B5B-5344-9882-6401B0BB3EEE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/170BFA1E-6481-4445-B1C2-14388CA5CA19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/187898CB-44FE-9B48-A98B-7C47FBC3237A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/54F3B88C-4D8C-844B-AD0E-1BDF304D404F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/6009CF25-6390-7041-839C-42FFCA10C465.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/6807199A-A725-B748-9FBD-F8D4129233AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/77D94828-5964-D744-86E7-32001D70DCF7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/8651F05D-101B-DE43-9681-3700E78CB63F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/9E7C32BE-CD5D-E14E-810F-060ED76B0F2C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/9FAC9B08-968D-714D-B28C-636BFA34075F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/AE868C4A-4288-AF4E-803F-B1F8B8D06E3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/BD42C701-0DED-7947-B23B-3ADF1149B1D1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/C7C1DC71-46CA-8A41-9539-038555C553C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/C8388E63-6368-B049-B3F9-750A47B71A80.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/CE7664CB-64DB-084B-ACC6-DD836BA30A56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/CF481471-8BA7-994F-8DAF-290287C280B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/DE73ACF6-021C-5B43-9A01-8D7BF88F1798.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/F290941F-E135-494A-BA0A-4EE55FB034D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/C8505C8F-6AF0-2848-A94D-5A2B3AA898BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/16C31BCA-D024-9541-B763-69BEAB588B73.root',
] )
