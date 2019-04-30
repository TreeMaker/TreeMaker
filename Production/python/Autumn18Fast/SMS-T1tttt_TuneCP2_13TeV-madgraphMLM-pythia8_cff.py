import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/11850A85-60AD-5940-B87B-E6C79CF6DE17.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/16396176-5929-BE40-B81E-4DD389E6FDB6.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/26306449-CE1C-A44B-82BF-F10F27F06CA6.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/323864AC-2568-8F41-B606-EE0DB0A887DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/346DB1A4-BF7E-E342-A659-97A940091DF7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/5632F50D-CE85-8449-ABF6-6785566F0F70.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/875B1D57-23AB-8544-93C7-13E68F91942E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/9DE3DCEA-E1F6-3D42-9628-C65B17F37C95.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/9ECA09B9-361A-4046-86FD-ADE1F4F09016.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/AC879DA3-0D15-B34F-9AC0-938D72E22D43.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/B3FD5485-88B1-194B-9018-74E4EC9A6EAF.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/BD4AB1E0-2239-864E-853F-B536AA57BA05.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/C2897730-D1B8-9D49-8F0D-FBD8D9C44BD7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/CB5C760D-824E-7B44-BED4-5483A50BF9EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_pilot_102X_upgrade2018_realistic_v15-v1/60000/EBCFF349-7B39-FD4F-AFAA-1C67AAB4C7F8.root',
] )
