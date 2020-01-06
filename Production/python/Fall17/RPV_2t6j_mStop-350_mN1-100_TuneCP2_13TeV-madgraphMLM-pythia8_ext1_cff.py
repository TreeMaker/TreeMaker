import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/0CB5508D-C1E0-E911-897C-D8D385B0EE2E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/0E12246F-FCE6-E911-98D4-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/16B1B5D2-63CA-E911-8CF1-FA163EAE3BD3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/1C4347BC-83C9-E911-B940-3417EBE528A6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/2688A9B6-63CA-E911-9455-FA163E09AD93.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/309796BA-63CA-E911-8C28-FA163E6DE7B9.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/48A1EFF8-FBE6-E911-8621-0025905C5484.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/564DDFED-A9E0-E911-B01B-782BCB20D86B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/6C89F86A-C6E0-E911-A0BA-008CFA1C6564.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/70716E7A-AFE0-E911-8425-0CC47A74524E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/887241DF-9AE0-E911-85D4-A0369FE2C208.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/9EC94169-10C9-E911-9AB6-0CC47A4D76C6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/A65A428D-5ECC-E911-8F84-3417EBE7062D.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/BAFDF32F-42C9-E911-B677-549F35AD8B7B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/BE5F9A80-96E0-E911-8E8E-405CFDFF480E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/C4FACA18-71C9-E911-936C-B496910A978C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D8CC1BAC-83C9-E911-879B-00266CFCC160.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/E4114EFB-9EE0-E911-AB6C-68CC6EA5BE22.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/EA66216D-47CA-E911-B940-0026B927866B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/F613B06D-A2E0-E911-8297-24BE05BD62B2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/FE5604BA-63CA-E911-97FA-FA163E0E3839.root',
] )
