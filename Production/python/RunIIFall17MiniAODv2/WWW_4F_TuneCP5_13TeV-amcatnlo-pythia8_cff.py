import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/02CEB4CC-BAD1-E811-8A8C-48FD8EE73AC5.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/0E4758EA-BAD1-E811-B3C2-14187762D010.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/12F7F9DF-BAD1-E811-AB11-D8D385AE84C4.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/168098C3-BAD1-E811-B90D-7CD30AD0A1E6.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/188C5AF8-BAD1-E811-B11E-0025901D1668.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/1C1403E2-BAD1-E811-9D40-0CC47A1DF806.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/1CCA4183-BBD1-E811-ACD7-A4BF01025A8B.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/2670E1E3-BAD1-E811-9FE8-405CFDFF480E.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/2A35BEE4-3CCC-E811-A5AD-A4BF01125DEE.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/2E87D2E7-BAD1-E811-893B-B496910A9A7C.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/585CC4E2-BAD1-E811-B90C-6C3BE5B580C8.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/840498DB-BAD1-E811-BD82-6CC2173C4580.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/8A8F2CE3-BAD1-E811-AD21-509A4C84542D.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/94EC9360-51CC-E811-A376-0025905C3D40.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/963E44E8-BAD1-E811-A0C9-00259021A306.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/BA4F75DC-BAD1-E811-B534-008CFAC93CE4.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/C0C7BD7D-BCD1-E811-A1BF-7CD30ABD2EE8.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/C26AD348-5FCC-E811-A1A4-506B4BB134CE.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/C6CC36F6-BAD1-E811-A9CF-0025905B85C0.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/CC1906E8-BAD1-E811-B80C-F01FAFE5E984.root',
       '/store/mc/RunIIFall17MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/60000/E4CF3BDA-BAD1-E811-8D70-B4969121F8E8.root',
] )
