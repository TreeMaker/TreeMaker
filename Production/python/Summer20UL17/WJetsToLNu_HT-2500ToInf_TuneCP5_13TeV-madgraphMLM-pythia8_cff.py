import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/08976B14-1E87-D841-9407-CB61610D1C76.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/14C37E03-F8E3-C14E-83B6-0B341771BD74.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/328C8303-79F0-DB4A-87A0-22F0EE3A5663.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/3A27F1F1-43D5-074E-B021-2B1D95C70BEF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/3AF6EEDF-0517-1D47-A998-DACC6823788E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/439C2557-A55B-CD4A-A522-2EB1F3875367.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/4B5058D1-3CD5-0440-AADB-8B33F2B6C7A9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/4CB51A90-4C6C-2E48-89D7-5FEB3047ECE2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/50EFF205-8346-DF49-804B-01A38E355A33.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/5929AE7E-D0EE-7D4E-95A6-B2CFC92135DF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/5CBE0F2B-BC4D-6943-BA2B-C3607F3260E3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/606399E4-830F-4E42-BCAB-E59B21432857.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/612F6AEE-50C0-0C43-BC5D-5E298442858A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/6CA6C416-0939-CB47-B08E-549D77966E42.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/808447EC-7D24-FC42-9927-A0B31637C9FE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/855C4BFB-FE4E-0649-8515-861C0BDC2BD9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/887A3EB0-D540-8240-8101-FACC607A7289.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/C626286A-C812-E249-828F-02B2618A0DB9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/CB47AD90-5101-E74B-8467-7242F9469743.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/D10F1E69-BA81-CD46-801B-2C6ECB79E851.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/D3C10E22-E8B5-7645-92FB-536C8E4F2D46.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/E33C99A6-2FC8-564F-8CE0-D83DBF5CCC76.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/EAEB311B-620B-D34D-8B24-6D5D36354DE0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/F0CD47DC-4D49-5546-B980-21A8275D6239.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/F4D7C8CA-E242-EB48-BCB5-C9FD70D81309.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/F54CFD10-1E33-7342-869B-62FAB77F44CC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/230000/FDA23FC4-8380-6246-B876-AE3D65B5ABF1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2430000/C1F0C9CF-09B6-F24B-A120-4E6A9B7D2A30.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/250000/94755EC4-A6B8-0346-A0AB-34D757636923.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/250000/A03CD499-5B92-B94A-A6B7-A49D11A0C6F7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2510000/55F9D623-65C0-0940-AAD6-866DD30C7D1B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2510000/87978EE4-6D2B-0347-B373-3BF2DFF38109.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/9153C3A0-D619-EB4D-96C0-1ECD46FF8A3C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/C638D62C-CFC1-7A4E-9E31-4E36EF185DB2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/F7FC472E-307E-D847-A842-718FB60580C4.root',
] )
