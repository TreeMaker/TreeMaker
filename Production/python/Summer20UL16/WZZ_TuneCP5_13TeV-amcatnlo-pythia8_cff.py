import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/249C7E16-D1B1-B44E-A9F0-4ACE50FF3E57.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/4BB925E9-4B11-0D42-8A2F-02F5A04EB73D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/5DD8B12C-102C-014A-952C-7D3E835C4D4B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/6E7DA98B-AFDA-724B-8335-5DDF82ECEB12.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/92F17A47-EAB1-F943-8922-1AF008A061C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/B303334D-B69E-E049-96F9-3E56682626E8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/A2082148-8E8E-BE4B-832F-48E8F5E1B7A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/52DAF86F-EB48-8648-81E0-779C28FE7651.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/128A4F4A-754F-DC4F-B425-2278A07473E0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1E73E70D-EC4D-9640-978C-D6572D0DBB69.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8EE63C03-2C0D-2742-BDC0-A3A76173D0E2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/BB6952D2-E7AA-1B46-9C30-3937D10134D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/76CF746D-A92F-ED4E-8153-015CE02E7F04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8453CB3E-00A9-2145-940F-6CC3F51C7396.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/891A120C-C6C5-3E4F-A060-17E6C1721B84.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/91E95C7F-607C-584F-BBA9-027C4237AE2F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A82D7CA8-C875-834F-9E36-2CC0A9A6EB09.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A94D3274-5A49-0440-BE1F-33D9069F666D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B50D336F-2500-E24D-A963-3E6D3CA1C9FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B6EA1CAB-13A3-4445-BD46-32749D04EA1D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F6309855-3BC6-E84A-A7F9-53B7C3650593.root',
] )
