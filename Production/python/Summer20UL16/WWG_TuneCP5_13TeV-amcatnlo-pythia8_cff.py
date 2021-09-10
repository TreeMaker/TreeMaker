import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/110000/1C7B5526-0FAE-544F-9B7D-95C9344AFE54.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/110000/E73805F0-F187-564B-B15A-D9A6FCC1E687.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/0B9FA58E-9F8A-9443-B06B-150E6EDC4D9D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/234D8BD4-0A1F-A647-A6D9-34A7365AF566.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/C0A95FF3-7B7B-ED43-91D2-05D8B720AF19.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/250000/B657EE06-D44B-C144-AEB8-A32592475B8B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/8F5DE34D-BE0A-F540-A3C9-E89D735C2397.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/08FB286B-80EB-0542-BF9F-048203BEA1F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0E210FAA-E732-F947-A0ED-2BBD5E949D3A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/109BB470-CFA5-1D4D-8274-87573C879388.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/34206E92-C7E3-1E46-A686-409BC8850717.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/43F52AF4-88E2-344C-B643-60F3A9C05951.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/5EA1F457-817B-EF44-A4BE-4D705A558875.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/79BB37C9-8855-A44B-81B5-697B5D355AF8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B5AFA1BE-317D-9C42-977D-234FF4A589E1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B618C3A8-EC28-B34C-988E-349A3AB52FF7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D5060BF7-7443-5943-BF7E-E27DA584C508.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D6A32857-DD20-9742-8177-C4A1B36F83FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/DF684724-6AA1-024C-B482-151FB75F4C38.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/EBB3026D-68D9-1642-B7FA-9DE5F5C5C470.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/FF87714B-9A05-3B4D-899E-A0005EDEAD5C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/57BC5A60-57CF-EF4B-BC5F-50AAACCDE3A7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6049A597-2600-1A4A-98BE-82FE272DD1F3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A39058A3-9189-F740-A33D-3A93B3571AB5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A942A8FB-AF1E-DE47-8D7F-F181D711FC0D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D957F4E9-556A-FA46-81E1-965068465CDA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FA2747CA-1AA8-E249-855C-8EBEA4EE1217.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FB69B5C7-C309-CB46-BEB6-F7C07691F218.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/EA3BBBE1-7ED7-5A42-B604-F650B87656CB.root',
] )
