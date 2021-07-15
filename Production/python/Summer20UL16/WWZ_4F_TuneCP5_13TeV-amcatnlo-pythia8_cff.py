import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/050FD395-1EAE-084B-AAEC-00D8C5BA6C5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0D47B0A2-2CCC-C442-9559-BB0084ABA175.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/170FC984-3CB8-094B-9108-7598ABC71F8C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1AD49BB0-5F61-C54F-A2BF-32538B2766D1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/407B150B-3BA6-5543-A2CF-C7612F348C09.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/467FE8FB-4C3F-124C-9AED-7DD92EFFD854.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/470807E1-244B-1848-8FB1-C94656634372.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/514249E3-EADE-4244-9FE8-8DB6AAB77E9E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/559572ED-0B8F-C74D-BE61-D62EFEAED475.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/65084C3E-6861-3F47-95A3-B130D6B9816A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/70700A33-D712-4C45-89D4-02A878B2960F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/76821438-0295-EF41-BEC0-137A4A1FF525.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8E139D18-5E41-E94C-9853-998FCC0A5252.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/981A7F0A-369C-F646-8B79-05E00B1161C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9AA4A013-38E9-DA43-9835-3CD96BCF6788.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A1875141-E187-A344-97E2-94A33BD14D46.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/CF130D30-CE0E-504B-9532-EA1C7808A3EC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D7FA24F9-B640-EA42-9CC7-BBB926481199.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F48E9315-DBEE-1245-B14B-933D712613BD.root',
] )
