import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/09696660-1B25-F44A-BBA9-D93C3D0907DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1041609C-0EAC-0049-994A-8E0362505AA9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/14A26F6A-6D98-B34B-B7DC-8EE4B3A11850.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1804B7D1-1D02-A840-A04B-A31BFDD5E24C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/2640F9FE-99E8-3C4C-8A5B-EC2114B1CC34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/2CD52D7C-9AB7-F240-9CAE-95CA04932212.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/336BDC4C-2FBF-A54B-90C8-4EDC3D93D79D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/368A67E0-0E8C-094B-97B0-3A43E460DF6C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/43C18092-EB9C-5942-BCE0-84F914B29A2C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4A1E1AB7-5517-FC4F-A174-82046DABFE1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/50C7989D-12A6-D940-AF3D-EC4140C84A35.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/65F2AE38-9363-9A48-860B-AE89DBBE54D9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/687E0638-3242-7540-A5CA-DC60A798B53D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/8EE07DAB-290E-2949-A50E-661066405505.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/A61984E8-22B7-C94F-9E9E-1BD98592119A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/A6AD4DC0-3F33-094D-A4A5-853CEE6027F6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/AAFB04EB-79EE-244A-9840-6C07C9C0F036.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/B24B0A1C-CE8F-504B-8B59-F25B0C15C91F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C9D707B4-E9EC-8C4C-BB6D-6E181FD3A32A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/CD00FC90-CD9F-7E4C-B5B5-CA457DB1C16A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/CE172498-B2B7-8744-B5FB-A1390D18CAAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/DC0F78E6-BF94-6542-8725-3247EEA9D95D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/DD8B503C-5A29-6F4E-8F72-65DC7C8578C6.root',
] )
