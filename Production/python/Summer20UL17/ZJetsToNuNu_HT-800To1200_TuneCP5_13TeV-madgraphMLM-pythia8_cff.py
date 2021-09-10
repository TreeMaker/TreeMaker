import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/4AD99B0C-C550-0C48-AE69-425C75791476.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/52DC43D1-DF91-BD4A-A15A-7A73FC399AC4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/C5BF0F54-08F5-B94E-8218-678644BBE367.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/465766B0-89ED-E848-9866-E789C04F86DB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/699C10D2-128C-724A-B3EC-89DFA5889BEF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/E681A378-1860-874D-91B7-AC15785DD810.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/1CAD6592-4CE0-8C48-AB6B-34189451BA60.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/25F2218B-B76B-E240-8F8B-FFB513150087.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/3C5C9E08-75F5-5A46-A498-56D4D8BFBB3D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/3F6A50FE-B6A1-A344-A8D7-A382E167F3FC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/43535F00-4CFB-9043-9B30-DCEFA96A65CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/55D7B2C6-111A-9F42-B921-F6012A4272D8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/69000965-338E-6442-916A-0FAE89E2DAFC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/6BDC68F1-98B4-8246-89FE-814B36F19967.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/7451D00D-FCD1-FB41-8BE6-117482C9946E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/7A98EB66-3F27-FC4E-9018-E8A1D7EC70D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/894D6B67-B768-7243-ABB3-7C1D233E71FF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/8AD70376-880F-2446-8768-8CB697D8431A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/94B51E13-BE51-044D-A943-0D68CB8A7E92.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/9B3723C7-59F6-9A44-8307-8A0EA4B21C59.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/9BF8BE59-1E0F-7247-BD4E-0429BBF7FB17.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/9D3AB6B0-AD57-054F-96B8-F675FACD6D44.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/A0E95BEA-BB7F-3147-BF95-96FCF78F6B16.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AAF9177B-CEFA-6A46-BE87-19030F9CEFAA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AB421ECC-1266-2F47-A603-D300828498B7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AFEB104A-26F2-E445-A1F2-60B69712E969.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/E7B408FA-93AF-CC43-97C6-9C22AFA3B1A0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/EFDE5D5A-F75B-864F-AD51-1EF331CD3D7B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/F9DE2F93-2FB7-E548-864C-D1C476151343.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/454A9D46-6C4F-3149-AD3D-66615AC2B6A4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/96523C41-9DBC-DA4B-AD19-178514694AE6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/D8CC9A68-493C-ED40-8AED-D9BAC398CE9E.root',
] )
