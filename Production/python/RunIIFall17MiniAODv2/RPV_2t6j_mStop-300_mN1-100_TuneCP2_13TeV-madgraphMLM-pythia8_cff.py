import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/0E680C3C-DFC7-E811-A8AE-246E96D149C4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/102FE697-16BF-E811-8EBC-001E67DDC6C8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/12935499-97C7-E811-80B3-509A4C858ADC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/12E2DDE2-14C9-E811-A090-509A4C748146.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/1861F2EA-28C8-E811-AE63-A0369FC5B56C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/1C270748-A9C0-E811-A480-0025905B8604.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/22E59D87-ADC7-E811-9BEE-0CC47A6C1402.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/30A95EA8-37C1-E811-A498-842B2B6AE7AB.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/34F5EB2B-DCCA-E811-AED1-B499BAABD022.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/403E5EFA-44CC-E811-8C35-A0369FD0B1AC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/42AE243C-45C0-E811-995E-0CC47AD98C5E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/50579F05-ACC7-E811-8F16-00266CF8355C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/7E93B1F1-5FBF-E811-B5D4-0CC47A13D2A4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/820CF0E3-AEC7-E811-9F76-3417EBE47EBC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/88DFF53D-ADC7-E811-85AD-506B4BB16AE6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/927291D8-A2C7-E811-BFAB-901B0E5427A6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/9A494E39-37C8-E811-9112-ECB1D7B67E10.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B00AA44F-AAD0-E811-86C1-008CFA11137C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B0CBDEF3-A4C7-E811-96F9-A4BF0101DDD7.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B6E25375-A0C7-E811-94B4-001E677923AE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/BE03EE5E-1ABF-E811-AB28-0026B9278603.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C85D584A-D8BF-E811-86D8-24BE05CEADD1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/CCECF518-F7BF-E811-9703-90B11C050395.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D0C8721C-A8C7-E811-BA12-D4AE529022BD.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/E6646383-7EBF-E811-B025-24BE05BDAE61.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/E6DAAD2A-8FBF-E811-8AAD-0090FAA57B40.root',
] )
