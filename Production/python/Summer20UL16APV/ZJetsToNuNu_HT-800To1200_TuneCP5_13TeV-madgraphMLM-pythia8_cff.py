import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/B2B1396B-47AE-B943-93E9-6F809782BC42.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/0A067E25-D0DD-8C44-B336-898CDA0E99D3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/0AA36588-457B-2A4D-B665-4EF65B2F42E2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/0B45F556-D8CD-6A4C-AB47-4D7EE1EBD3ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/17AA809E-D96B-B547-8A37-B0FB41AED1FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/585FDB5E-16A5-394E-AD22-3C19F350DBF1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/8F2B44F1-EA31-7545-A7B0-7005D7E6E52F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/032E3F50-90C9-BD45-9B09-85F656B75B21.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/09DCB7A5-E3A7-F84C-9DB9-12063D56621F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/4A1A506D-0DCA-E943-BDDC-40D8F1CAE096.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/63B9147F-F017-F441-902C-5C7D38C0D1A8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/B017904E-79E2-CF4D-A86E-E997CCF21ECE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/88AD9E5C-311B-9247-949B-A2E884FB5713.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/A72499EC-69F4-1840-9680-58D671538BD1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/B9323096-9EB8-594D-A902-55601E172076.root',
] )
