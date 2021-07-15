import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/102C17E5-2E0D-644A-89F9-A08AA3636840.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/29B8A72F-00D2-0B4F-917E-C500ED4DFFC9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2C7AB116-3BD5-6A4C-B79A-5B157B9050F7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2FD8045A-7EC7-4E4E-9098-5C7BEDA577CA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3201F818-8AAA-1C41-A93D-C21913EE521A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/347521C5-1CE6-7C4E-A1D1-B638084142CE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/5055B1A7-C7F2-9D4D-8110-942E454B73B2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/520C7FFD-0DF6-D34D-9A6D-164BA64F7DBB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/67000E95-19E3-A442-97B9-2FAA0CD225B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7B1912C1-BDF1-754D-8ADF-D12E45235C25.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/81C98502-8179-B54E-B88E-E97F1152FF13.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A8844EDD-FCE5-DA42-AC6E-49772594C2F7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A9A7AE61-0074-104A-BD8A-22F4EC4FEC24.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/BBC33248-28E9-2A46-BC78-7EC1641DFB48.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C4F3F7D6-889C-BF4A-A5B4-0FBA8733518A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DC2C2CEE-BA9C-1145-88C2-F9201D949049.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E2C5A1E0-5F67-C048-8581-8ED0CB4D4A4F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E79C5A63-B543-0A4B-91E5-FA031694DC19.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F15BF050-E695-6F40-8315-20071CD98A46.root',
] )
