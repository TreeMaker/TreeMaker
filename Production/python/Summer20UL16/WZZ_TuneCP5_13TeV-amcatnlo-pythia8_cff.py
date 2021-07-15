import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/042773CD-B883-714B-BF7E-9DF3A573D914.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/2271E675-D199-E640-A853-A862EF5A6371.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/27B2E6C3-57D7-E54B-87A9-8E73CFD2277B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/3165B290-2BE6-344E-A12D-B3B1BF8B0EED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/3D251C1F-CAAB-314D-9FDE-BB24BDB825A8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/3E7358A4-6DCA-B140-B797-B9520DD33B30.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/59A1CFBA-52E6-E04A-B110-CAFA263C2BA8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/5C0D8B73-7F67-1746-8DFD-7BA6253C286C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/6A0E80B6-ECFF-CF47-8F6D-338CF431B0E6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/808F8309-CEBF-A24F-BF48-511657506802.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/865A0088-227B-AC41-A15F-5C9872E6190C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/9D312514-E04D-194A-AA9B-4CC156F3EE9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/A6882CE0-70C9-E342-908F-2210E523DDFB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/AFBADE98-E172-5844-94E5-5F872571ED11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/BA628083-779F-8D46-8551-D6300925CB87.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/D5B08EE2-C722-AF4F-8455-E8A04B45104B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/D7915A7A-02FB-CA43-AD8A-45B7349F9DA8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/E29E58CA-008A-D247-94ED-753A12BDB0D7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/EE0B24B3-1EE7-5C45-B340-8DC38613077D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/F233B852-646E-B74B-AC0E-A1D039F76058.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/F7C85C30-9DF1-9947-9738-7BB570FD5C80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/FEB86C40-AA07-4443-9405-1794DC85698B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/FFE312C2-D075-7640-A475-1E9B7F2CF600.root',
] )
