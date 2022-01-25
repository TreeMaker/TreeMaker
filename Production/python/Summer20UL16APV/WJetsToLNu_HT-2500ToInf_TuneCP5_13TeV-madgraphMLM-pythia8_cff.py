import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/010C07A2-9C62-DE4D-81AC-DB1B98AB9F73.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/05453EE4-1C26-E245-9C0F-5816EABB5898.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1507DD4D-58F3-1247-A584-D349802B12A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1E29C378-733E-F84F-932F-0CE0B3BD3682.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/3D07BEA8-D3B2-E945-B8BA-7BE070D4BD94.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/3FADAFEF-9FED-D746-8D61-16CB7F6CB9CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/41D63866-5D36-E344-91F4-4853E5529A60.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4659AECD-7751-7D49-BC5D-501FFBC728B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4D808F52-0543-C34D-8804-7747BC9FD844.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/4E57DAAB-D232-6848-9407-E14E70FC0437.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/584FD9EA-266B-7647-9686-3ABE0D761011.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/5A6C0C6E-F93A-794F-9282-125708FBA4A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/62D225C6-8611-6A4F-8C74-913411201B36.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/7F72CB3D-AE97-904D-AF13-8C8AC16C8ECB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/84A12B99-1361-6C4B-8831-E29C85EAFE22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/98B5CE8A-72AC-CF4F-9934-163CED1BC84B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/9FFC54CB-9A17-CC4D-ADDC-FFBB610970EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/A4084294-1BA7-774D-BA51-4B1A15052DA0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C3E1CCB2-723E-EA4C-A3FE-062E1A3D5C28.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/C50FBBF4-542E-BA47-8FA8-953CA17F8D66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/F13B7C0A-6244-C845-80F5-D9CEAB3A6CB0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/F4B266A2-4C83-EA41-BCE4-D62FBF711382.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/0497A266-1C4D-8949-AF47-7598789485F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/07C9A580-56F0-934B-95F7-078B44C078EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/53BF2A63-B44C-F543-9572-38D3F1F18F60.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/70EAA3E6-4133-9240-B3D9-2BB54231C971.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7B3A470D-6A0E-1943-B9ED-33CB0C6CAC8F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/8AD31754-F75F-2447-A657-559390FC1FF0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/91CBF23F-724B-EF47-8864-FB738B9D772C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/BD23970D-28C9-E54A-8E45-6C4F8902B2C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/D9F7C21A-48CF-4248-A850-DFE0B0F29393.root',
] )
