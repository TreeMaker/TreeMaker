import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/1DE133FF-6F98-5D48-A133-9F9C802BCC4B.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/CCBF1261-BED6-AA43-98AC-EF2739575029.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/F0388DE6-F7D4-D043-8428-FA975771F449.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/9482D5C1-2714-474A-B56F-FE75681DBEB3.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B15C9AB6-7F9F-5C42-9294-D5FC3624DA85.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CD3C7D8C-A550-D047-ADC4-64CD99463CB3.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F654A069-1676-534F-A04D-ABD6BCAAC7E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/71F657F8-0EE7-CE4B-9AFB-2E729D33AA8C.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/A4E2F1D3-520D-1C4D-922B-D10D69F7C3EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/02E5E4E1-37FA-7542-947A-07BE4E2C473D.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/1655D153-41AB-CA4C-BC10-C19B730D4313.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/4D9B7326-9A16-A343-8B02-0DED9FDF3FD0.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/57B4A2B3-7AE3-9B43-8A97-87004F0AEA3F.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/6CEE3531-5E4C-6047-A508-624F04215255.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/8B00FC9B-43C3-1049-8317-CBFF31260D7D.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/9754B12B-ECE0-474C-9BBD-6D0762DCD235.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/A00A33A9-6041-C240-816F-5DE8DA035A88.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/B5DB33C3-620A-A849-82A0-23B6694BA979.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/241DF588-5C9B-144A-BB1C-580698995E81.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/339F1FDE-240C-9242-BF8C-93BE1FDFB5B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/68000DC2-39AA-8F4C-9102-76963244A924.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/7C1C4711-A7CF-E042-BEAD-9B662B9576B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/DB4A9551-0CB5-0C4E-8A77-673C55DC42A5.root',
] )
