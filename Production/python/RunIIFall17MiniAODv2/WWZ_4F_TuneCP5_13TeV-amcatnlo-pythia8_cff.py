import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/067E786D-ABC3-E811-8455-1866DA85DC8B.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/1E2133FB-89C3-E811-A744-28924A33AF26.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/26ED3F0D-D3C3-E811-BA27-0CC47AFC3D34.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/2CB07ED3-BEC3-E811-80CD-7CD30AD0A1F8.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/2E9F5B07-1CC4-E811-B508-0CC47A1DF806.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/320FEF3C-E3C4-E811-8ED4-B499BAABD28C.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/324199C4-ADC3-E811-8755-0CC47A5FC67D.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/3ECCDCEE-B5C0-E811-8489-EC0D9A0B31B0.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/44F1DD7B-86C3-E811-AC15-0025905B8606.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/469B925C-08C4-E811-BCA0-A0369FC51A44.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/76E3E61F-8DC3-E811-B122-6C3BE5B580C8.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/787A4CF4-9BC3-E811-B4A0-008CFAE45128.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/86DF496F-7AC2-E811-B3C5-0025905C2CD2.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/8CDAD5BC-E3C4-E811-8FA1-002590908FA2.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/90A57DA3-96C3-E811-97D9-002590D60194.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/A25F33B6-F7C3-E811-A8F2-0242AC1C0505.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/C660C9DB-8AC3-E811-B349-0CC47AD99144.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E25EEFCD-B0C0-E811-9072-AC1F6B0DE228.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E417A587-37C4-E811-B11A-1866DA87D585.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E859E61A-C8C3-E811-B985-509A4C8395C6.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E8782068-86C3-E811-A178-001E67E6F855.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/FCF70D63-8CC4-E811-BE82-3417EBE5062D.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/6EE94B14-84D4-E811-BA56-0CC47A6C138A.root',
       '/store/mc/RunIIFall17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/86A28B12-84D4-E811-B473-AC1F6B56768A.root',
] )
