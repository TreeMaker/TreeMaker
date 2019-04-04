import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/13120FAE-75FE-CB42-8250-B7B6F0507A13.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/3F574CFE-E1D5-434C-B4D5-671ABE01E1E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/52CC8E86-8ED7-B54E-A8B0-07A1EA143CFA.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/5F7AC3FE-01DF-EF4F-8F0F-41751B693AB7.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/6DE8AEA0-8B5C-904E-A961-1A91ECFC5C73.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/AACF8AE4-8910-2D48-917C-37C547DF51A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/B37A0192-401D-234D-B8B8-C618B89A1A06.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/00000/EF7C22C9-4183-9045-8935-8C186F716D6D.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/10000/B4C1C5FF-9AA7-5A47-974E-9DB67A1A156D.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/10000/E0B84BD6-494A-E346-93EC-2510D4D21F0B.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/100000/94CD7949-0F4E-3D4D-8B92-AA50E35F6C0E.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/100000/D4659663-209B-F448-8869-133AA456039E.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/53F86B16-2387-B14B-BE9A-94915CC74CA0.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/AA296ED2-4994-B046-8610-541895B1D01A.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/EDE90983-29CD-3E46-854F-BD0D624A38CD.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/F0A9993B-C81A-AF4E-8347-EC45B35BA99F.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/F210092D-5737-B041-ADBB-97316D2417BE.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/7F47BB69-D46F-734E-928C-652BC858B67C.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/B6577BCD-E5FF-EC42-BF02-D74388344D17.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/45B55278-8B21-1D41-9C9F-1972F096E7FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/BE6B4909-CBD0-7E42-A13E-3E4DA9ABD7F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/C231620A-83E9-814B-BF5F-5F3A0CB99D3E.root',
] )
