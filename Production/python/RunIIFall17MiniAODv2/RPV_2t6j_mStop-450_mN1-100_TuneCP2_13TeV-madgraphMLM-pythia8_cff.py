import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/06DC05AE-72CB-E811-B282-0CC47A13D0F2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/26ABCD2C-00CC-E811-9AB8-A4BF0112E490.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/30BEDF33-F7CB-E811-B0BE-008CFAFC594E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/449D88AD-78D0-E811-8299-008CFA165F48.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/60E8A595-EABF-E811-81EC-0CC47AD98C5E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/6A03D548-A1C0-E811-8282-5065F3815241.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/76089DBC-11CC-E811-9C3D-246E96D14D4C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/7A7CE9DA-2FCB-E811-A944-0025905B856C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/886DE47B-6EBF-E811-B2FA-346AC29F1198.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/9463EE26-14CC-E811-889C-001E67A3FD26.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A0C5B052-82C0-E811-A416-AC1F6B0DE30C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A8166B09-07CC-E811-98E8-0425C5DE7BF6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/AC4A02CE-73CB-E811-9A20-0CC47A745284.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C6DD1963-00CC-E811-80CD-44A842BE8F98.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C82FFAFC-F5CB-E811-B747-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D23C691F-F4C0-E811-855F-008CFA197C1C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D6977AB6-C7C2-E811-951B-3CFDFE63F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/DEC549DE-73CB-E811-A40C-E0071B7A68F0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E6AAFCEF-F3CB-E811-9D12-008CFA1C6458.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E82418AF-CECC-E811-846E-48FD8E2824C3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F63323C1-03CC-E811-968C-3CFDFE63EFE0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F6E8BBFA-12CC-E811-8AF6-509A4C781310.root',
] )
