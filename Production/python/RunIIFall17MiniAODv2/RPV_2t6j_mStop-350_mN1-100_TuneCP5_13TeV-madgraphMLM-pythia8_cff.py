import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/042E7912-65A2-E811-A9A2-001E67792866.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/52601449-D7A1-E811-89A3-A4BF01125D66.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/ACF19ACE-39A2-E811-92CF-EC0D9A04AE30.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/BAAB2C5F-63A2-E811-9D82-B8CA3A708F98.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0C58A52B-D89E-E811-B4B9-002590DE3AC0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/10BB753F-D89E-E811-ADAB-0025905C4264.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/125C8281-3E9C-E811-8D42-24BE05C32CA2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/14D8E945-D89E-E811-8ADF-40F2E9C6AE21.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/14F09B3F-D89E-E811-A7E4-002590DE6E2A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/2A8F4933-899C-E811-8599-28924A33AFC2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3C790039-D89E-E811-B3F8-008CFAF7245E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4067BC5A-DC9D-E811-96E2-A4BF0101DB93.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/40D50763-D89E-E811-9D23-0025905B8590.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/44B8B7FC-539D-E811-B6D3-90B11C28232B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/54211D66-D89E-E811-B019-A0369F30FFD2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/589CA063-D89E-E811-9D9C-001EC94BA185.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6E710CFC-C79C-E811-8624-24BE05C38CA1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/76E15B2C-D89E-E811-9B06-0CC47A13CECE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/7840202A-D89E-E811-B43C-A0B3CCDFB624.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/7AD80B5E-D89E-E811-BAAF-EC0D9A0B3330.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/82F5134A-D89E-E811-84B8-A4BF01125698.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8AFDC61C-C69D-E811-8E71-002590A887F2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8E66CA3E-D89E-E811-B331-246E96D10990.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A49FFD34-D89E-E811-8C17-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/AE495BE4-B79E-E811-8461-0090FAA58BF4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C6559F29-D89E-E811-99F6-00269E95ACE8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D85D98FD-0B9D-E811-8E29-3CFDFE634FA0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/BC9129FE-03AB-E811-8802-001E67E6F774.root',
] )
